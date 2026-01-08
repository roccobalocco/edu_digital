from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    '''
    Classe che descrive le impostazioni di configurazione per lo script.

    Args:
        cookbook_path(str): Percorso alla cartella contenente il cookbook di OpenAI.
        index_path(str): Percorso alla cartella dove verrà salvato l'indice delle fonti.
        output_path(str): Percorso del file di output per il manuale generato.
        gemini_model(str): Nome del modello Gemini da utilizzare.
        embed_model(str): Nome del modello di embedding da utilizzare.
        force_reindex(str): Flag per forzare la reindicizzazione delle fonti.
    '''
    cookbook_path: str = os.getenv("COOKBOOK_PATH", "./data/openai-cookbook")
    index_path: str = os.getenv("INDEX_PATH", "./data/sources_index")
    output_path: str = os.getenv("OUTPUT_PATH", "./data/output/manuale.md")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    embed_model: str = os.getenv("GEMINI_EMBED_MODEL", "text-embedding-004")
    force_reindex: bool = os.getenv("REINDEX", "0") == "1"