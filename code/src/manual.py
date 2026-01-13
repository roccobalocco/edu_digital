from typing import Dict
from prompts import TOPIC_SPECS
from pathlib import Path


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


def write_section_files(sections: Dict[str, str], output_dir: Path):
    '''
    Scrive i file markdown per ogni sezione del manuale.
    Inoltre cancella i file review.

    Args:
        sections(Dict[str, str]): Dizionario contenente le sezioni del manuale.
        output_dir(Path): Cartella di output dove salvare i file.
    '''
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, (key, content) in enumerate(sections.items(), start=1):
        spec = TOPIC_SPECS[key]
        filename = f"{i:02d}-{key}.md"

        path = output_dir / filename
        path.write_text(
            f"# {spec['title']}\n\n{content}\n",
            encoding="utf-8",
        )
        
    for p in output_dir.glob("review_*.md"):
        try:
            p.unlink()
        except OSError:
            print(f"Impossibile cancellare {p}")


def write_readme(sections: Dict[str, str], output_dir: Path):
    '''
    Scrive il file README.md con l'indice delle sezioni del manuale.

    Args:
        sections(Dict[str, str]): Dizionario contenente le sezioni del manuale.
        output_dir(Path): Cartella di output dove salvare il file.
    '''
    lines = [
        "# Manuale d’Uso dell’IA Generativa\n",
        "Manuale prodotto tramite workflow editoriale automatizzato con revisione umana.\n",
        "## Indice\n",
    ]

    for i, key in enumerate(sections.keys(), start=1):
        spec = TOPIC_SPECS[key]
        fname = f"{i:02d}-{key}.md"
        lines.append(f"- [{spec['title']}]({fname})")

    (output_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def write_summary(output_dir: Path):
    """
    Genera automaticamente SUMMARY.md leggendo i file .md nella cartella.
    Usa i primi 3-4 parole del file come titolo, o il nome file se non trova titolo.
    
    Args:
        output_dir(Path): Cartella di output dove salvare il file.
    """
    summary_lines = ["# Summary\n", "- [Manuale d’Uso](README.md)\n"]
    
    # Ordina i file per numero iniziale (01-, 02-, etc.)
    md_files = sorted(output_dir.glob("*.md"))
    
    for md_file in md_files:
        if md_file.name in ["README.md", "SUMMARY.md"]:
            continue  # saltali
        
        # Leggi le prime righe del file per trovare un titolo
        with md_file.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):  # trova il primo titolo Markdown
                    title = line.lstrip("# ").strip()
                    break
            else:
                title = md_file.stem  # fallback: nome del file senza estensione
        
        summary_lines.append(f"- [{title}]({md_file.name})")
    
    # Scrivi SUMMARY.md
    summary_path = output_dir / "SUMMARY.md"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"SUMMARY.md generato in {summary_path}")

def write_book_toml(title: str, author: str, output_dir: Path, build_dir: str = "html"):
    """
    Scrive il file book.toml per mdBook. NECESSARIO PER USARE mdBook.

    Args:
        title (str): Titolo del libro.
        author (str): Nome dell'autore.
        output_dir (Path): Cartella di output dove salvare il file.
        build_dir (str, optional): Cartella dove mdBook genera il sito HTML. Default: "html".
    """
    toml_content = f"""
[book]
title = "{title}"
author = "{author}"
src = "."

[build]
build-dir = "{build_dir}"
"""

    book_toml_path = output_dir / "book.toml"
    book_toml_path.write_text(toml_content.strip() + "\n", encoding="utf-8")


def assemble_full_manual(sections: Dict[str, str]) -> str:
    '''
    Assembla il manuale completo in formato markdown.

    Args:
        sections(Dict[str, str]): Dizionario contenente le sezioni del manuale.

    Returns:
        str: Testo completo del manuale in formato markdown.
    '''
    parts = ["# Manuale d’Uso dell’IA Generativa\n"]

    for key, content in sections.items():
        spec = TOPIC_SPECS[key]
        parts.append(f"## {spec['title']}\n")
        parts.append(content)
        parts.append("\n")

    return "\n".join(parts)
