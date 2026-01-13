# Prompt engineering per rilevamento lingua

# Rilevare la Lingua di un Testo con l'IA

**Obiettivo:** Utilizzare l'Intelligenza Artificiale per identificare rapidamente e con precisione la lingua di qualsiasi testo, dai commenti social alle email. Questo ti aiuta a organizzare e gestire i contenuti multilingue in modo più efficiente.

---

### Quando serve in agenzia

In agenzia, ti capiterà spesso di dover gestire contenuti in diverse lingue. L'IA per il rilevamento della lingua è utile in molti scenari:

*   **Gestione Commenti Social**: Immagina di avere una pagina Facebook o Instagram con follower da tutto il mondo. L'IA può aiutarti a identificare la lingua dei commenti per rispondere nella lingua giusta o inoltrare al team competente.
    *   *Esempio pratico:* Un brand globale riceve centinaia di commenti al giorno. L'IA li classifica per lingua, permettendo ai community manager di concentrarsi sui commenti nella loro lingua madre.
    *   `Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`
*   **Analisi UGC (User Generated Content)**: Se raccogli contenuti generati dagli utenti (recensioni, testimonianze, post), l'IA può categorizzarli per lingua, facilitando l'analisi e l'utilizzo in campagne mirate.
*   **Smistamento Email e Richieste Clienti**: Per i team di customer service o sales, l'IA può identificare la lingua delle email in arrivo, indirizzandole automaticamente all'agente che parla quella lingua.
*   **Preparazione Contenuti per Traduzione**: Prima di inviare un testo a un traduttore, puoi usare l'IA per confermare la lingua originale, evitando errori e costi aggiuntivi.
*   **Controllo Qualità Contenuti**: Assicurarsi che un contenuto sia effettivamente nella lingua prevista, specialmente in progetti multilingue complessi.

---

### Prompt template

Per chiedere all'IA di rilevare la lingua, la chiave è essere chiari e specifici sul formato di output desiderato.

**Struttura del prompt:**

```
Sei un esperto di lingue. Il tuo compito è identificare la lingua del testo che ti fornirò.

Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo, 'fr' per francese, 'de' per tedesco, 'zh' per cinese). Non aggiungere altro testo, spiegazioni o punteggiatura.

Testo: {il tuo testo qui}
```

**Perché funziona:**

*   **Ruolo chiaro**: "Sei un esperto di lingue" imposta il contesto e le aspettative.
*   **Compito specifico**: "Il tuo compito è identificare la lingua" è inequivocabile.
*   **Formato di output rigido**: "Rispondi solo con il codice ISO 639-1... Non aggiungere altro testo" è fondamentale per ottenere un output pulito e facile da usare (ad esempio, per automatizzare processi).
    *   `Fonte: ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3`
    *   `Fonte: ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26`
    *   `Fonte: ../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2`

---

### Esempi pratici (commenti social, UGC, email)

Vediamo come applicare il prompt template a diversi tipi di testo.

**Esempio 1: Commento Social**

*   **Testo input:** "I love this product!"
*   **Prompt:**
    ```
    Sei un esperto di lingue. Il tuo compito è identificare la lingua del testo che ti fornirò.

    Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo, 'fr' per francese, 'de' per tedesco, 'zh' per cinese). Non aggiungere altro testo, spiegazioni o punteggiatura.

    Testo: I love this product!
    ```
*   **Output IA:** `en`

**Esempio 2: Commento Social (Spagnolo)**

*   **Testo input:** "No estoy seguro de lo que pienso sobre este producto."
*   **Prompt:** (come sopra, con il testo spagnolo)
*   **Output IA:** `es`

**Esempio 3: Commento Social (Cinese)**

*   **Testo input:** "总体来说，我对这款产品很满意。"
*   **Prompt:** (come sopra, con il testo cinese)
*   **Output IA:** `zh`
    *   `Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3`

**Esempio 4: Email Cliente**

*   **Testo input:** "Gentile cliente, la sua richiesta è stata presa in carico e le risponderemo al più presto."
*   **Prompt:** (come sopra, con il testo italiano)
*   **Output IA:** `it`

**Esempio 5: Contenuto Generato dall'Utente (Francese)**

*   **Testo input:** "C'est magnifique! J'adore votre nouvelle collection et la qualité est superbe."
*   **Prompt:** (come sopra, con il testo francese)
*   **Output IA:** `fr`

---

### Ambiguità e casi misti

L'IA è brava, ma non infallibile. Ci sono situazioni in cui il rilevamento della lingua può essere più complesso.

*   **Testi Brevi o Senza Contesto**: Frasi molto corte (es. "Ok, grazie.") o singole parole possono rendere difficile per l'IA identificare con certezza la lingua. Potrebbe non avere abbastanza informazioni per decidere.
*   **Lingue Simili**: Alcune lingue condividono molte parole o strutture grammaticali (es. italiano, spagnolo e portoghese). L'IA potrebbe confondersi se le differenze sono sottili o il testo è breve.
*   **Code-switching / Lingue Miste**: Questo accade quando un testo contiene frasi o parole di più lingue. Ad esempio: "Ciao, I need help with my *ordine*."
    *   In questi casi, l'IA tenderà a identificare la lingua predominante. Se vuoi un'analisi più dettagliata, dovrai modificare il prompt per chiedere all'IA di identificare *tutte* le lingue presenti o la lingua *principale* e le lingue *secondarie*.
    *   *Esempio pratico:* Se il tuo prompt chiede solo "la lingua", l'IA potrebbe rispondere `en` per "Ciao, I need help with my *ordine*", perché l'inglese è la lingua principale della frase.
    *   `Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5`

---

### Limiti e buone pratiche

Per ottenere i migliori risultati e capire quando l'IA potrebbe avere difficoltà:

**Limiti:**

*   **Precisione con testi molto brevi**: Più il testo è corto, maggiore è la possibilità di errore. L'IA ha bisogno di contesto per essere precisa.
*   **Dialetti e gerghi specifici**: Alcuni dialetti regionali o gerghi molto specifici potrebbero non essere riconosciuti correttamente come parte di una lingua standard.
*   **Lingue rare o nuove**: Se l'IA non è stata addestrata su una lingua specifica, potrebbe non riconoscerla o confonderla con un'altra.
*   **Confidenza del modello**: L'IA non ti dice "quanto è sicura" della sua risposta in modo diretto e semplice. Devi fidarti del risultato o fare dei controlli a campione.
    *   `Fonte: ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1` (concetto di confidenza rielaborato)

**Buone pratiche:**

*   **Sii specifico nel prompt**: Chiedi sempre il formato di output esatto (es. codice ISO 639-1) per evitare risposte prolisse o ambigue.
    *   `Fonte: ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26`
*   **Fornisci il maggior contesto possibile**: Se hai un paragrafo intero, è meglio di una singola parola. Più testo dai, più l'IA sarà accurata.
*   **Testa e verifica**: Non dare per scontato che l'IA sia sempre perfetta. Fai dei test con testi noti e verifica i risultati, specialmente per le lingue che ti interessano di più.
*   **Itera sul prompt**: Se i risultati non sono soddisfacenti, prova a modificare il prompt. Ad esempio, puoi aggiungere una lista di lingue attese: "Rispondi solo con 'it', 'en', 'es', 'fr'..."
*   **Considera l'uso di strumenti dedicati**: Per volumi molto elevati o esigenze di precisione estreme, potresti voler integrare l'IA con servizi di rilevamento lingua specifici, spesso più robusti per casistiche particolari.

---

### Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`
