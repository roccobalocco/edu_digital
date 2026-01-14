# edu_digital

Progetto relativo al corso Editoria Digitale 2025/206 - UNIMI.

## Pagina dedicata

[Github Page](https://roccobalocco.github.io/edu_digital/)

## Comandi

- `python run.py` – preferisce il riutilizzo dell'indice e crea il manuale

## Opzioni

- `--reindex` – reindicizza e crea il manuale
- `--full` – unisce le sezioni in un unico manuale Markdown

## Next steps

- [Crea manuale](https://github.com/roccobalocco/MD_Doc_Gen) – integralo ed eseguilo per avere il manuale del manuale ><

## Strumenti utilizzati

- [Google AI Studio](https://aistudio.google.com) – per creare il progetto e la sua API key
- [ChatGPT](https://chatgpt.com) e [Claude](https://claude.ai) – come supporto per la stesura del codice
- Knowhow ottenuto implementando [SofIA](https://www.softeam.it/prodotti/sofia/) (LangGraph, Embedding, Python, etc...)
- [Github Codespaces](https://github.com/features/codespaces) – per lo sviluppo in cloud
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook/tree/main) – git clone del repo per ottenere le fonti
- [FAISS](https://faiss.ai) – per cercare le similarità

<hr/>

## Comandi di trasformazione `report.md`

- `pandoc --embed-resources --resource-path='./assets' -f markdown-implicit_figures -s report.md -o report.pdf --lua-filter=html-img-to-md.lua --toc -F mermaid-filter` per generare il file pdf
- `pandoc --embed-resources --resource-path='./assets' -f markdown-implicit_figures -s report.md -o report.html --lua-filter=html-img-to-md.lua --toc -F mermaid-filter` per generare il file html
- `pandoc --embed-resources --resource-path='./assets' -f markdown-implicit_figures -s report.md -o report.epub --lua-filter=html-img-to-md.lua --toc -F mermaid-filter` per generare il file epub
- `pandoc --embed-resources --resource-path='./assets' -f markdown-implicit_figures -s report.md -o report.tex --lua-filter=html-img-to-md.lua --toc -F mermaid-filter` per generare il file tex