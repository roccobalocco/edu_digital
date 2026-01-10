from __future__ import annotations
import argparse
from pathlib import Path

from config import Settings
from graph import build_graph, State
from manual import write_section_files, write_readme, assemble_full_manual, write_summary, write_book_toml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reindex", action="store_true")
    parser.add_argument("--full", action="store_true", help="Genera anche il manuale completo")
    args = parser.parse_args()

    settings = Settings()
    if args.reindex:
        settings.force_reindex = True

    app = build_graph()
    state = State(settings=settings)
    out = app.invoke(state)

    sections = out.get("approved_sections") or out.get("manual_sections", {})
    output_dir = Path(settings.output_path).parent

    write_section_files(sections, output_dir)
    write_readme(sections, output_dir)
    write_summary(sections, output_dir)
    write_book_toml("Manuale d’Uso dell’IA Generativa", "Masolini Pietro", output_dir)

    if args.full:
        full_md = assemble_full_manual(sections)
        (output_dir / "manuale_completo.md").write_text(
            full_md, encoding="utf-8"
        )

    print(f"Manuale modulare generato in: {output_dir}")


if __name__ == "__main__":
    main()
