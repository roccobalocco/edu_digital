# Prompt engineering per rilevamento lingua

# Rilevare la lingua di un testo con l'IA

Capire in che lingua è scritto un testo è un passaggio fondamentale per molte attività di marketing e comunicazione. L'Intelligenza Artificiale può farlo in modo rapido e affidabile, aiutandoti a organizzare e gestire i tuoi contenuti.

### Quando serve in agenzia

Rilevare la lingua di un testo è utile in tantissime situazioni quotidiane:

*   **Gestione contenuti multilingue**: Se hai un sito web o dei profili social in più lingue, l'IA può aiutarti a categorizzare i testi in arrivo (es. commenti, recensioni) per indirizzarli al team giusto o per analizzarli.
*   **Analisi del sentiment**: Prima di capire se un commento è positivo o negativo, devi sapere in che lingua è scritto. L'IA può identificare la lingua, permettendoti di applicare poi l'analisi del sentiment specifica per quella lingua.
    *   *Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`*
*   **Personalizzazione delle comunicazioni**: Se ricevi email o messaggi da clienti in diverse lingue, puoi usare l'IA per identificare la lingua e rispondere automaticamente nella stessa lingua, o indirizzare la richiesta al team madrelingua.
*   **Localizzazione e traduzione**: Per preparare un testo alla traduzione o alla localizzazione, sapere con certezza la lingua di partenza è il primo passo.
*   **Moderazione dei contenuti**: Identificare la lingua può essere utile per applicare regole di moderazione specifiche per ogni mercato.

### Prompt template

Per chiedere all'IA di rilevare la lingua, il prompt deve essere chiaro e diretto.

**Obiettivo**: Ottenere solo la lingua del testo, senza fronzoli.

**Prompt base**:
```
Qual è la lingua di questo testo?
Testo: [INSERISCI TESTO QUI]
```

**Prompt avanzato (per risultati più puliti)**:
```
Sei un esperto di lingue. Il tuo compito è identificare la lingua del testo fornito.
Rispondi solo con il nome della lingua, scritto in italiano, senza aggiungere altre frasi o spiegazioni.
Testo: [INSERISCI TESTO QUI]
```
*   *Riferimento: `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3` (per l'istruzione "Return only the name of the category, and nothing else.")*

**Prompt con output strutturato (consigliato per l'integrazione)**:
Se devi elaborare i risultati in modo automatico (es. per un foglio Excel o un database), chiedi un formato specifico, come il JSON.

```
Identifica la lingua del seguente testo.
Rispondi in formato JSON, usando la chiave "lingua" per il nome della lingua rilevata.
Testo: [INSERISCI TESTO QUI]
```
*   *Riferimento: `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2` (per il concetto di output strutturato)*

**Prompt con lingue predefinite**:
Se sai che i tuoi testi provengono solo da un set limitato di lingue, puoi aiutare l'IA a essere più precisa.

```
Qual è la lingua di questo testo? Scegli tra: italiano, inglese, spagnolo, francese, tedesco.
Rispondi solo con il nome della lingua.
Testo: [INSERISCI TESTO QUI]
```

### Esempi pratici

Ecco come puoi usare questi prompt con testi reali da agenzia:

**1. Commenti social**

*   **Testo**: "I love this product! It's amazing how well it works."
*   **Prompt**:
    ```
    Identifica la lingua del seguente testo.
    Rispondi in formato JSON, usando la chiave "lingua" per il nome della lingua rilevata.
    Testo: I love this product! It's amazing how well it works.
    ```
*   **Output IA**:
    ```json
    {
      "lingua": "inglese"
    }
    ```
    *   *Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`*

**2. Contenuti generati dagli utenti (UGC)**

*   **Testo**: "No estoy seguro de lo que pienso sobre este producto."
*   **Prompt**:
    ```
    Qual è la lingua di questo testo? Scegli tra: italiano, inglese, spagnolo, francese, tedesco.
    Rispondi solo con il nome della lingua.
    Testo: No estoy seguro de lo que pienso sobre este producto.
    ```
*   **Output IA**:
    ```
    spagnolo
    ```
    *   *Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`*

**3. Estratto da email o recensioni**

*   **Testo**: "总体来说，我对这款产品很满意。"
*   **Prompt**:
    ```
    Sei un esperto di lingue. Il tuo compito è identificare la lingua del testo fornito.
    Rispondi solo con il nome della lingua, scritto in italiano, senza aggiungere altre frasi o spiegazioni.
    Testo: 总体来说，我对这款产品很满意。
    ```
*   **Output IA**:
    ```
    cinese
    ```
    *   *Riferimento: `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`*

### Ambiguità e casi misti

A volte, i testi non sono così semplici. L'IA può incontrare difficoltà con:

*   **Testi brevi**: Frasi molto corte (es. "LOL" o "Ok, thanks!") possono essere difficili da attribuire a una lingua specifica.
*   **Code-switching (cambio di codice)**: Quando un testo mescola intenzionalmente due o più lingue. Ad esempio: "Ciao, I received your email. Thanks!"
*   **Slang e gergo**: L'uso di slang o abbreviazioni può rendere il riconoscimento più complesso.

**Come gestire i casi misti**:
Puoi dare istruzioni specifiche all'IA per questi scenari.

*   **Prompt per lingua predominante**:
    ```
    Identifica la lingua del seguente testo. Se il testo contiene più lingue, indica la lingua predominante. Se non c'è una lingua predominante chiara, elenca tutte le lingue presenti separate da una virgola.
    Rispondi in formato JSON con la chiave "lingua" o "lingue".
    Testo: Ciao, I received your email. Thanks!
    ```
*   **Output IA (esempio)**:
    ```json
    {
      "lingue": "italiano, inglese"
    }
    ```
    o, se l'IA identifica una predominanza:
    ```json
    {
      "lingua": "inglese"
    }
    ```
    *   *Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5` (per la capacità del modello di gestire e rispondere in più lingue basandosi su istruzioni)*

### Limiti e buone pratiche

Anche se l'IA è molto brava a rilevare le lingue, ci sono alcune cose da tenere a mente:

**Limiti:**

*   **Precisione con testi brevi**: Più il testo è corto, più è difficile per l'IA essere sicura al 100% della lingua.
*   **Dialetti e lingue meno diffuse**: L'IA è addestrata su grandi quantità di dati, ma potrebbe avere difficoltà con dialetti molto specifici o lingue con poca presenza online.
*   **Errori e ambiguità**: Testi con molti errori di battitura o frasi molto ambigue possono confondere il modello.
*   **Sicurezza della risposta**: L'IA non sempre ti dice "quanto è sicura" della sua risposta. In casi critici, una verifica umana può essere necessaria.
    *   *Riferimento: `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1` (concetto di confidenza, semplificato)*

**Buone pratiche:**

*   **Sii specifico nel prompt**: Chiedi esattamente quello che vuoi ("Rispondi solo con il nome della lingua") per evitare risposte prolisse o inutili.
    *   *Riferimento: `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3`*
*   **Fornisci un elenco di lingue**: Se conosci le lingue possibili, elencale nel prompt. Questo restringe il campo e migliora la precisione.
*   **Chiedi un formato di output strutturato (JSON)**: Questo rende i risultati facili da usare in altri strumenti o sistemi, automatizzando il flusso di lavoro.
    *   *Riferimento: `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26` e `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2`*
*   **Testa con i tuoi dati**: Prova l'IA con esempi reali dei testi che gestisci per capire come si comporta e dove potrebbe avere difficoltà.
*   **Definisci la gestione dei casi misti**: Se sai che avrai testi in più lingue, istruisci l'IA su come vuoi che li gestisca (es. lingua predominante, elenco di lingue).
    *   *Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5`*

---

### Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`
