from __future__ import annotations

import json
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Dict, Any, List

from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document

from helper import ensure_str
from config import Settings
from ingest import build_chunks, save_manifest
from retriever import build_or_load_vectorstore, retrieve
from prompts import TOPIC_SPECS, TOPIC_SELECTOR_SYSTEM, ADAPT_SYSTEM


@dataclass
class State:
    '''
    Classe che descrive lo stato del grafo.

    Args:
        settings(Settings): Impostazioni di configurazione.
        vectorstore(Any | None): Vectorstore per il recupero dei documenti.
        retrieved(Dict[str, List[Document]] | None): Documenti recuperati per ogni argomento.
        selected(Dict[str, List[Dict[str, Any]]] | None): Documenti selezionati per ogni argomento.
        manual_sections(Dict[str, str] | None): Sezioni del manuale generate per ogni argomento.
        approved_sections(Dict[str, str] | None): Sezioni del manuale approvate per ogni argomento.
    '''
    settings: Settings
    vectorstore: Any | None = None
    retrieved: Dict[str, List[Document]] | None = None
    selected: Dict[str, List[Dict[str, Any]]] | None = None
    manual_sections: Dict[str, str] | None = None
    approved_sections: Dict[str, str] | None = None


def node_index(state: State) -> State:
    '''
    Nodo per l'indicizzazione delle fonti.
    
    Args:
        state(State): Stato corrente del grafo.

    Returns:
        State: Stato aggiornato con il vectorstore indicizzato.
    '''
    chunks = build_chunks(state.settings.cookbook_path)
    save_manifest(chunks, str(Path(state.settings.index_path) / "manifest.json"))
    vs = build_or_load_vectorstore(
        chunks=chunks,
        index_path=state.settings.index_path,
        embed_model=state.settings.embed_model,
        force_reindex=state.settings.force_reindex,
    )
    state.vectorstore = vs
    return state


def node_retrieve(state: State) -> State:
    '''
    Nodo per il recupero dei documenti rilevanti.
    
    Args:
        state(State): Stato corrente del grafo.

    Returns:
        State: Stato aggiornato con i documenti recuperati.
    '''
    assert state.vectorstore is not None
    retrieved = {}
    for key, spec in TOPIC_SPECS.items():
        retrieved[key] = retrieve(state.vectorstore, spec["query"], k=14)
    state.retrieved = retrieved
    return state


def node_select(state: State) -> State:
    '''
    Nodo per la selezione dei documenti più rilevanti.
    
    Args:
        state(State): Stato corrente del grafo.
    
    Returns:
        State: Stato aggiornato con i documenti selezionati.    
    '''
    assert state.retrieved is not None

    llm = ChatGoogleGenerativeAI(
        model=state.settings.gemini_model,
        temperature=0.2,
    )

    selected: Dict[str, List[Dict[str, Any]]] = {}

    for key, docs in state.retrieved.items():
        # assembla lista estratti con id
        items = []
        for d in docs:
            items.append({
                "id": d.metadata.get("id"),
                "path": d.metadata.get("path"),
                "excerpt": d.page_content[:1400],
            })

        prompt = (
            f"{TOPIC_SELECTOR_SYSTEM}\n\n"
            f"TOPIC: {TOPIC_SPECS[key]['title']}\n\n"
            f"ESTRATTI:\n{json.dumps(items, ensure_ascii=False, indent=2)}\n\n"
            "Rispondi SOLO con JSON valido."
        )
        resp = llm.invoke(prompt).content
        try:
            data = json.loads(str(resp))
        except Exception:
            # fallback: seleziona i primi 6
            data = {"selected": [{"id": it["id"], "reason": "fallback"} for it in items[:6]], "rejected": []}

        # materializza i selezionati con contenuto
        sel_ids = {x["id"] for x in data.get("selected", []) if x.get("id")}
        chosen = []
        for it in items:
            if it["id"] in sel_ids:
                chosen.append(it)
        selected[key] = chosen

    state.selected = selected
    return state


def node_adapt(state: State) -> State:
    '''
    Nodo per l'adattamento e la generazione delle sezioni del manuale.

    Args:
        state(State): Stato corrente del grafo.
    
    Returns:
        State: Stato aggiornato con le sezioni del manuale generate.    
    '''
    assert state.selected is not None

    llm = ChatGoogleGenerativeAI(
        model=state.settings.gemini_model,
        temperature=0.4,
    )

    manual_sections: Dict[str, str] = {}

    for key, items in state.selected.items():
        spec = TOPIC_SPECS[key]

        payload = {
            "topic": spec["title"],
            "required_sections": spec["deliverable_sections"],
            "sources": items,
        }

        prompt = (
            f"{ADAPT_SYSTEM}\n\n"
            "Crea una sezione di manuale in Markdown seguendo la struttura richiesta.\n"
            "Includi esempi pratici 'da agenzia'.\n"
            "In fondo inserisci una sezione 'Fonti' con elenco puntato dei path dei file usati.\n\n"
            f"INPUT:\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n\n"
            "OUTPUT: Markdown completo (solo testo)."
        )

        md = llm.invoke(prompt).content

        if isinstance(md, list):
            md = json.dumps(md)  # o altra conversione appropriata

        manual_sections[key] = md

    state.manual_sections = manual_sections
    return state


def node_review(state: State) -> State:
    '''
    Nodo per la revisione e l'approvazione delle sezioni del manuale.
    
    Args:
        state(State): Stato corrente del grafo.
        
    Returns:
        State: Stato aggiornato con le sezioni del manuale approvate.
    '''
    assert state.manual_sections is not None
    assert state.selected is not None

    approved: Dict[str, str] = {}
    output_dir = Path(state.settings.output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    editor = os.environ.get("EDITOR", "nano")  # usa l'editor di sistema, default nano

    for key, raw_content in state.manual_sections.items():
        spec = TOPIC_SPECS[key]
        review_file = output_dir / f"review_{key}.md"

        while True:
            # Scrive il contenuto corrente su file
            content: str = ensure_str(raw_content)
            review_file.write_text(content, encoding="utf-8")

            print("\n" + "=" * 80)
            print(f"SEZIONE: {spec['title']}")
            print("=" * 80)
            print(f"Apri il file e modificalo nell'editor. Salva e chiudi per continuare.")
            print("-" * 80)

            # apre l'editor di sistema
            os.system(f"{editor} {review_file.resolve()}")

            choice = input("Approvare questa sezione? [Y/N]: ").strip().lower()

            if choice == "y":
                # Rileggi il file aggiornato
                updated_content = review_file.read_text(encoding="utf-8")
                approved[key] = updated_content
                break

            elif choice == "n":
                feedback = input(
                    "Descrivi cosa va modificato (tono, esempi, struttura, contenuti):\n> "
                )

                # Rigenera la sezione con LLM usando il feedback
                payload = {
                    "topic": spec["title"],
                    "required_sections": spec["deliverable_sections"],
                    "sources": state.selected[key],
                    "editor_feedback": feedback,
                }

                prompt = (
                    f"{ADAPT_SYSTEM}\n\n"
                    "Rigenera la sezione TENENDO CONTO del feedback editoriale.\n"
                    "Migliora chiarezza, aderenza al contesto aziendale e struttura.\n\n"
                    f"INPUT:\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n\n"
                    "OUTPUT: Markdown completo (solo testo)."
                )

                raw_content = ChatGoogleGenerativeAI(
                    model=state.settings.gemini_model,
                    temperature=0.4,
                ).invoke(prompt).content

                raw_content = ensure_str(raw_content)

            else:
                print("Risposta non valida. Inserisci Y o N.")

    state.approved_sections = approved
    return state


def build_graph() -> CompiledStateGraph[State, None, State, State]:
    '''
    Costruisce e restituisce il grafo di elaborazione.

    Returns:
        StateGraph: Grafo di elaborazione configurato.
    '''
    g = StateGraph(State)
    g.add_node("index", node_index)
    g.add_node("retrieve", node_retrieve)
    g.add_node("select", node_select)
    g.add_node("adapt", node_adapt)
    g.add_node("review", node_review)

    g.set_entry_point("index")
    g.add_edge("index", "retrieve")
    g.add_edge("retrieve", "select")
    g.add_edge("select", "adapt")
    g.add_edge("adapt", "review")
    g.add_edge("review", END)

    return g.compile()
