from __future__ import annotations

from pathlib import Path
from typing import List

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from ingest import DocChunk


def build_or_load_vectorstore(
    *,
    chunks: List[DocChunk],
    index_path: str,
    embed_model: str,
    force_reindex: bool = False,
) -> FAISS:
    '''
    Costruisce o carica un vectorstore FAISS dai chunk dei documenti.
    
    Args:
        chunks(List[DocChunk]): Lista di chunk dei documenti.
        index_path(str): Percorso della cartella per salvare/caricare l'indice.
        embed_model(str): Nome del modello di embedding da utilizzare.
        force_reindex(bool): Flag per forzare la reindicizzazione delle fonti.
    
    Returns:
        FAISS: Vectorstore FAISS costruito o caricato.
    '''
    index_dir = Path(index_path)
    index_dir.mkdir(parents=True, exist_ok=True)

    faiss_file = index_dir / "index.faiss"
    store_file = index_dir / "index.pkl"

    embeddings = GoogleGenerativeAIEmbeddings(model=embed_model)

    # Load se esiste e non forzi rebuild
    if not force_reindex and faiss_file.exists() and store_file.exists():
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    # Rebuild
    docs = [
        Document(page_content=c.content, metadata={"id": c.id, "path": c.path})
        for c in chunks
        if c.content and c.content.strip()
    ]
    if not docs:
        raise RuntimeError("0 docs: niente da indicizzare. Controlla COOKBOOK_PATH.")

    # sanity check embeddings (evita IndexError “muto”)
    test = embeddings.embed_documents([docs[0].page_content[:1500]])
    if not test or not test[0]:
        raise RuntimeError(
            "Embedding vuoto: verifica GOOGLE_API_KEY, GEMINI_EMBED_MODEL (es. text-embedding-004), quota/permessi."
        )

    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(index_path)
    return vs


def retrieve(vs: FAISS, query: str, k: int = 12) -> List[Document]:
    '''
    Recupera i documenti rilevanti dal vectorstore per una query data.

    Args:
        vs(FAISS): Vectorstore FAISS.
        query(str): Query di ricerca.
        k(int): Numero di documenti da recuperare.

    Returns:
        List[Document]: Lista di documenti recuperati.
    '''
    return vs.similarity_search(query, k=k)