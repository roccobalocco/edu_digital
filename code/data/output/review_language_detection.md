Ecco la sezione del manuale dedicata al rilevamento della lingua tramite IA.

---

# Rilevamento della Lingua con l'IA

Capire in che lingua è scritto un testo è il primo passo per molte attività di marketing e comunicazione. L'IA può aiutarti a identificare rapidamente la lingua di qualsiasi contenuto, rendendo più efficienti i tuoi flussi di lavoro.

## Quando serve in agenzia

Identificare la lingua di un testo è fondamentale in diverse situazioni quotidiane:

*   **Gestione commenti social**: Per smistare i commenti dei follower in base alla lingua e rispondere in modo appropriato, oppure per analizzare il sentiment specifico per mercato.
*   **Analisi UGC (User Generated Content)**: Quando raccogli recensioni, testimonianze o contenuti creati dagli utenti, l'IA può aiutarti a categorizzarli per lingua prima di un'analisi più approfondita (ad esempio, per capire il sentiment in diverse lingue).
*   **Smistamento email e richieste di supporto**: Instradare automaticamente le email dei clienti al team di supporto o al copywriter giusto in base alla lingua.
*   **Localizzazione contenuti**: Preparare i testi per la traduzione, assicurandosi di conoscere la lingua di partenza.
*   **Ricerca di mercato**: Analizzare conversazioni online o trend in diverse aree geografiche.

*(Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb)*

## Prompt template

Per chiedere all'IA di rilevare la lingua, devi essere chiaro e specifico. L'obiettivo è ottenere una risposta pulita e standardizzata, come un codice lingua.

**Obiettivo del prompt**: Identificare la lingua di un testo e restituire solo il codice ISO 639-1 (es. `it`, `en`, `es`).

**Come usarlo**: Copia e incolla questo template nel tuo strumento IA, sostituendo `[Il tuo testo qui]` con il contenuto da analizzare.

```
Sei un esperto di lingue.
Il tuo compito è identificare la lingua del testo che ti fornirò.
Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo), e nient'altro.

Testo:
[Il tuo testo qui]
```

**Spiegazione del prompt**:
*   `Sei un esperto di lingue.`: Assegna un "ruolo" all'IA, aiutandola a focalizzarsi sul compito.
*   `Il tuo compito è identificare la lingua del testo che ti fornirò.`: Definisce chiaramente l'azione richiesta.
*   `Rispondi solo con il codice ISO 639-1 della lingua (...) e nient'altro.`: Questa è la parte più importante. Forza l'IA a dare una risposta precisa e senza fronzoli, facilitando l'automazione o l'analisi successiva.
*   `Testo:`: Indica chiaramente dove inserire il contenuto da analizzare.

*(Fonte: ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3, ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26, ../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2)*

## Esempi pratici (da agenzia)

Ecco come puoi usare il prompt con diversi tipi di contenuto:

### 1. Commenti social

**Input (Testo da analizzare):**
"Che bello questo post! Complimenti al team, continuate così!"

**Prompt completo:**
```
Sei un esperto di lingue.
Il tuo compito è identificare la lingua del testo che ti fornirò.
Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo), e nient'altro.

Testo:
Che bello questo post! Complimenti al team, continuate così!
```

**Output atteso dall'IA:**
`it`

### 2. Recensione UGC (User Generated Content)

**Input (Testo da analizzare):**
"This product is amazing, totally recommend it! Fast delivery and great quality."

**Prompt completo:**
```
Sei un esperto di lingue.
Il tuo compito è identificare la lingua del testo che ti fornirò.
Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo), e nient'altro.

Testo:
This product is amazing, totally recommend it! Fast delivery and great quality.
```

**Output atteso dall'IA:**
`en`

### 3. Email o messaggio cliente

**Input (Testo da analizzare):**
"No estoy seguro de lo que pienso sobre este producto. ¿Podrían darme más información?"

**Prompt completo:**
```
Sei un esperto di lingue.
Il tuo compito è identificare la lingua del testo che ti fornirò.
Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo), e nient'altro.

Testo:
No estoy seguro de lo que pienso sobre este producto. ¿Podrían darme más información?
```

**Output atteso dall'IA:**
`es`

### 4. Recensione app (lingue non latine)

**Input (Testo da analizzare):**
"总体来说，我对这款产品很满意。功能强大，界面友好。"

**Prompt completo:**
```
Sei un esperto di lingue.
Il tuo compito è identificare la lingua del testo che ti fornirò.
Rispondi solo con il codice ISO 639-1 della lingua (es. 'it' per italiano, 'en' per inglese, 'es' per spagnolo), e nient'altro.

Testo:
总体来说，我对这款产品很满意。功能强大，界面友好。
```

**Output atteso dall'IA:**
`zh`

*(Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3)*

## Ambiguità e casi misti

L'IA è molto brava, ma non è infallibile. Ci sono situazioni in cui il rilevamento della lingua può essere più complesso:

*   **Testi molto brevi**: Con poche parole, l'IA ha meno indizi e potrebbe fare errori. Ad esempio, "Ok" potrebbe essere in molte lingue.
*   **Gergo, slang o nomi propri**: Parole non standard o nomi di persone/luoghi possono confondere l'IA, soprattutto se sembrano appartenere a un'altra lingua.
*   **Code-switching (lingue mescolate)**: Quando un testo contiene frasi o parole di più lingue ("Questo è un *must-have* per il mio *workflow*"). L'IA di solito identifica la lingua predominante, ma non sempre è quello che cerchi.
*   **Lingue simili**: Italiano e spagnolo, o portoghese e spagnolo, possono essere difficili da distinguere per l'IA con testi brevi o con lessico comune.

**Come gestire questi casi**:

*   **Sii più specifico nel prompt**: Se sai che potresti avere testi misti, puoi chiedere all'IA di identificare la lingua *principale* o di segnalare se il testo è *multilingue*.
*   **Fornisci contesto**: Se possibile, aggiungi informazioni che possano aiutare l'IA (es. "Questo testo proviene da un utente in Italia").
*   **Definisci una risposta per l'incertezza**: Puoi aggiungere al prompt: "Se non sei sicuro, rispondi 'sconosciuto'".

*(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5)*

## Limiti e buone pratiche

Per ottenere i migliori risultati e gestire le aspettative:

### Limiti da considerare

*   **Non è sempre 100% accurato**: Specialmente con testi brevi, ambigui o con molte parole straniere.
*   **Non "capisce" il contesto culturale**: L'IA si basa sul modello linguistico, non sulla comprensione profonda delle sfumature culturali o regionali.
*   **Difficoltà con dialetti o lingue meno diffuse**: L'IA è addestrata su grandi quantità di testo, ma se una lingua o un dialetto è poco rappresentato, l'accuratezza diminuisce.

### Buone pratiche per i copywriter e content strategist

1.  **Sii sempre specifico nel prompt**: Chiedi esattamente ciò che vuoi (es. "solo il codice ISO 639-1"). Questo riduce le risposte non pertinenti.
2.  **Testa il tuo prompt**: Prima di usarlo su larga scala, prova il prompt con diversi tipi di testo (brevi, lunghi, misti, in lingue diverse) per capire come si comporta l'IA.
3.  **Non dare per scontato**: Per contenuti critici, controlla sempre i risultati, soprattutto se l'IA ha segnalato incertezza o se il testo era particolarmente complesso.
4.  **Fornisci esempi (few-shot)**: Se hai testi molto specifici o con ambiguità ricorrenti, puoi includere nel prompt 1-2 esempi di testo con la lingua corretta. Questo "insegna" all'IA come vuoi che risponda.
5.  **Integra con altri strumenti**: Per volumi molto grandi o esigenze di alta precisione, considera di affiancare l'IA a strumenti di rilevamento lingua più specifici o a una revisione umana.

*(Fonte: ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1, ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26, ../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2)*

---

## Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`