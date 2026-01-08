from __future__ import annotations
import argparse
from pathlib import Path

from config import Settings
from graph import build_graph, State
from prompts import TOPIC_SPECS

def assemble_manual(sections: dict) -> str:
    '''
    Assembla il manuale completo in formato markdown.
    
    Args:
        sections(dict): Dizionario contenente le sezioni del manuale.

    Returns:
        str: Testo completo del manuale in formato markdown.
    '''
    parts = []
    parts.append("# Manuale d’Uso dell’IA (Bozza automatizzata)\n")
    parts.append("## Introduzione\n")
    parts.append(
        "Questa bozza è stata generata automaticamente a partire da contenuti del repository OpenAI Cookbook, "
        "selezionati e rielaborati per un contesto di agenzia (copywriter e content strategist).\n"
    )
    parts.append("## Indice\n")
    for k, spec in TOPIC_SPECS.items():
        parts.append(f"- [{spec['title']}](#{spec['title'].lower().replace(' ', '-')})")
    parts.append("\n---\n")

    # sezioni
    for k, spec in TOPIC_SPECS.items():
        parts.append(f"## {spec['title']}\n")
        parts.append(sections.get(k, "_Sezione non generata._"))
        parts.append("\n---\n")

    return "\n".join(parts).strip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reindex", action="store_true", help="Ricostruisce l'indice (ricalcola embeddings).")
    args = parser.parse_args()

    settings = Settings()
    if args.reindex:
        settings.force_reindex = True 
        
    app = build_graph()
    state = State(settings=settings)
    out = app.invoke(state)

    md = assemble_manual(out["manual_sections"] or {})
    Path(settings.output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(settings.output_path).write_text(md, encoding="utf-8")
    print(f"Manuale generato: {settings.output_path}")


if __name__ == "__main__":
    main()
