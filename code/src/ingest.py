from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, List
import uuid

import nbformat

@dataclass
class DocChunk:
    '''
    Classe che rappresenta un chunk del documento.
    '''
    id: str
    path: str
    content: str


def iter_source_files(cookbook_path: str) -> Iterable[Path]:
    '''
    Itera sui file sorgente nella cartella del cookbook.

    Args:
        cookbook_path(str): Percorso alla cartella del cookbook.
    
    Returns:
        Iterable[Path]: Iteratore sui percorsi dei file sorgente.
    '''
    root = Path(cookbook_path)
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in [".md", ".ipynb"]:
            yield p


def add_missing_cell_ids(nb:Any):
    for cell in nb.cells:
        if 'id' not in cell:
            cell['id'] = str(uuid.uuid4())
    return nb

    
def ipynb_to_markdown_text(p: Path) -> str:
    '''
    Converte un file .ipynb in testo markdown.

    Args:
        p(Path): Percorso al file .ipynb.

    Returns:
        str: Testo markdown estratto dal notebook.
    '''
    nb = nbformat.read(p, as_version=4)  # legge senza validare
    
    parts = []
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            parts.append(cell.source)
        elif cell.cell_type == "code":
            code = cell.source.strip()
            if code and len(code) <= 1200:  
                parts.append("```python\n" + code + "\n```")

    return "\n\n".join(parts).strip()


def read_file_text(p: Path) -> str:
    '''
    Legge il testo da un file, supportando .md e .ipynb.

    Args:
        p(Path): Percorso al file.

    Returns:
        str: Testo letto dal file.
    '''
    if p.suffix.lower() == ".md":
        return p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix.lower() == ".ipynb":
        return ipynb_to_markdown_text(p)
    return ""


def chunk_text(text: str, max_chars: int = 1800, overlap: int = 200) -> List[str]:
    '''
    Divide il testo in chunk di dimensione massima specificata, con sovrapposizione.

    Args:
        text(str): Testo da dividere in chunk.
        max_chars(int): Numero massimo di caratteri per chunk.
        overlap(int): Numero di caratteri di sovrapposizione tra chunk.
    
    Returns:
        List[str]: Lista di chunk di testo.
    '''
    text = text.replace("\r\n", "\n")
    chunks = []
    i = 0
    while i < len(text):
        j = min(len(text), i + max_chars)
        chunk = text[i:j]
        cut = chunk.rfind("\n\n")
        if cut > 500:
            chunk = chunk[:cut]
            j = i + cut
        chunks.append(chunk.strip())
        i = max(j - overlap, j)
    return [c for c in chunks if c]


def build_chunks(cookbook_path: str) -> List[DocChunk]:
    '''
    Costruisce i chunk dei documenti dalla cartella del cookbook.

    Args:
        cookbook_path(str): Percorso alla cartella del cookbook.
    
    Returns:
        List[DocChunk]: Lista di chunk dei documenti.
    '''
    chunks: List[DocChunk] = []
    for p in iter_source_files(cookbook_path):
        txt = read_file_text(p)
        if not txt or len(txt) < 200:
            continue
        for idx, ch in enumerate(chunk_text(txt)):
            chunks.append(
                DocChunk(
                    id=f"{p.as_posix()}::chunk{idx}",
                    path=p.as_posix(),
                    content=ch,
                )
            )
    return chunks


def save_manifest(chunks: List[DocChunk], out_path: str) -> None:
    '''
    Salva il manifesto dei chunk in un file JSON.

    Args:
        chunks(List[DocChunk]): Lista di chunk dei documenti.
        out_path(str): Percorso del file di output per il manifesto.
    
    Returns:
        None
    '''
    data = [{"id": c.id, "path": c.path, "content": c.content} for c in chunks]
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
