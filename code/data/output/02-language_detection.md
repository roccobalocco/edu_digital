# Prompt engineering per rilevamento lingua

# Rilevamento Lingua con l'IA

Questa sezione ti mostra come usare l'Intelligenza Artificiale per identificare la lingua di un testo. È uno strumento utile per gestire grandi volumi di contenuti multilingue o per assicurarti che la tua comunicazione sia sempre nel giusto idioma.

## Obiettivo

Identificare la lingua di un testo in modo rapido e affidabile.

## Quando serve in agenzia

Come copywriter o content strategist, ti troverai spesso a gestire contenuti provenienti da diverse fonti o destinati a pubblici internazionali. L'IA per il rilevamento lingua è utile in questi casi:

*   **Gestione di contenuti generati dagli utenti (UGC):** Se la tua azienda riceve commenti, recensioni o post sui social da clienti di tutto il mondo, l'IA può aiutarti a capire rapidamente in che lingua sono scritti. Questo è fondamentale per la moderazione o per rispondere in modo appropriato.
*   **Personalizzazione della comunicazione:** Prima di inviare email o messaggi, puoi usare l'IA per verificare la lingua preferita del destinatario, assicurandoti che il tuo messaggio sia sempre pertinente.
*   **Classificazione e organizzazione:** Per archiviare o categorizzare articoli, post di blog o documenti in base alla loro lingua, facilitando la ricerca e la gestione dei contenuti.
*   **Analisi di mercato:** Quando analizzi conversazioni online o feedback dei clienti da diverse aree geografiche, l'IA ti aiuta a filtrare e raggruppare i dati per lingua.

## Prompt template

Per chiedere all'IA di rilevare una lingua, devi essere chiaro e specifico. Il template di base è semplice:

```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua (es. "Italiano", "Inglese", "Spagnolo").

Testo:
[INSERISCI QUI IL TESTO DA ANALIZZARE]
```
*(Riferimento: `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3` - adattato per classificazione lingua)*

**Per un output più strutturato e preciso (utile per l'integrazione con altri strumenti):**

```
Identifica la lingua del seguente testo.
Rispondi solo con il codice ISO 639-1 a due lettere della lingua (es. "it", "en", "es").

Testo:
[INSERISCI QUI IL TESTO DA ANALIZZARE]
```
*(Riferimento: `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2` - per output strutturati)*

## Esempi pratici da agenzia

Ecco come puoi usare questi prompt con testi reali:

### Esempio 1: Commento social

Immagina di monitorare i commenti sui social media per un brand internazionale.

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua.

Testo:
"This product is amazing! I love the new features."
```

**Output dell'IA:**
```
Inglese
```

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua.

Testo:
"No estoy seguro de lo que pienso sobre este producto."
```

**Output dell'IA:**
```
Spagnolo
```
*(Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` - testi di esempio)*

### Esempio 2: Recensione utente (UGC)

Un cliente ha lasciato una recensione sul tuo sito e vuoi sapere in che lingua è.

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il codice ISO 639-1 a due lettere.

Testo:
"总体来说，我对这款产品很满意。"
```

**Output dell'IA:**
```
zh
```
*(Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` - testo di esempio)*

### Esempio 3: Oggetto di un'email

Stai gestendo una campagna email multilingue e vuoi assicurarti che l'oggetto sia nella lingua giusta.

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua.

Testo:
"Scopri le nostre nuove offerte esclusive!"
```

**Output dell'IA:**
```
Italiano
```

## Ambiguità e casi misti

Non tutti i testi sono "puri". L'IA può incontrare difficoltà con:

*   **Testi molto brevi:** Meno parole significano meno contesto per l'IA. "Ciao!" potrebbe essere italiano, ma anche un saluto informale in altre lingue.
*   **Code-switching (cambio di codice):** Quando una persona mescola due o più lingue nella stessa frase o paragrafo (es. "Ho avuto un meeting super busy oggi").
*   **Slang, dialetti o gergo specifico:** L'IA potrebbe non riconoscere forme linguistiche non standard.
*   **Testi con citazioni in altre lingue:** Un testo principalmente in italiano che include una frase in inglese potrebbe confondere l'IA se non istruita correttamente.

**Come gestire i casi misti:**

Puoi istruire l'IA su come comportarsi in queste situazioni.

**Prompt per lingua principale:**
```
Identifica la lingua principale del seguente testo. Se ci sono più lingue, indica solo quella predominante.
Rispondi solo con il nome della lingua.

Testo:
"Ho avuto un meeting super busy oggi, ma alla fine abbiamo chiuso il deal!"
```

**Output dell'IA:**
```
Italiano
```

**Prompt per tutte le lingue:**
```
Elenca tutte le lingue presenti nel seguente testo.
Rispondi con un elenco puntato dei nomi delle lingue.

Testo:
"The new campaign is amazing! La nuova campagna è fantastica!"
```

**Output dell'IA:**
```
- Inglese
- Italiano
```
*(Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5` - concetto di "code switching")*

## Limiti e buone pratiche

### Limiti

*   **Precisione con testi brevi o specifici:** L'IA è meno affidabile con frasi molto corte o con testi che contengono molto gergo tecnico o slang non comune.
*   **Lingue rare o dialetti:** Potrebbe avere difficoltà a identificare lingue meno diffuse o dialetti specifici per i quali ha meno dati di addestramento.
*   **Non è "comprensione umana":** L'IA rileva la lingua basandosi su modelli e statistiche, non sulla comprensione del significato come farebbe un essere umano.

### Buone pratiche

1.  **Sii specifico nel prompt:**
    *   Indica chiaramente il formato di output desiderato (nome completo, codice ISO, ecc.).
    *   Specifica cosa fare in caso di testi misti (es. "lingua principale" o "elenca tutte").
    *(Riferimento: `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26` - enforce strict guidelines)*

2.  **Fornisci esempi (Few-shot prompting):**
    *   Se l'IA fatica con un tipo specifico di testo, puoi includere nel prompt alcuni esempi di input e l'output corretto che ti aspetti. Questo "addestra" l'IA sul momento.
    *(Riferimento: `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26` - includes few-shot examples)*

3.  **Chiedi un livello di "sicurezza" (se disponibile):**
    *   Per decisioni critiche, alcuni strumenti IA possono indicare quanto sono "sicuri" della loro risposta. Se disponibile, chiedi all'IA di fornire un punteggio di confidenza. Questo ti aiuta a capire quando potresti aver bisogno di una verifica manuale.
    *(Riferimento: `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1` - concetto di confidence score)*

4.  **Testa e itera:**
    *   Prova il tuo prompt con diversi tipi di testo che potresti incontrare. Se l'IA non risponde come previsto, modifica il prompt per renderlo più chiaro o aggiungi esempi.

## Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`
