# Manuale d’Uso dell’IA Generativa

## Prompt engineering per generazione di testi

# Manuale d'Uso dell'IA per Copywriter e Content Strategist

## Prompt Engineering per la Generazione di Testi

### 1. Cos'è e quando usarlo

**Obiettivo:** Capire come "parlare" all'IA per ottenere i testi che desideri.

Immagina di dare istruzioni a un nuovo stagista molto bravo, ma che non conosce il tuo brand. Il "prompt" è esattamente questo: l'insieme di istruzioni che dai all'Intelligenza Artificiale per fargli creare un testo. Più le istruzioni sono chiare e complete, migliore sarà il risultato.

**Quando usarlo:**
Ogni volta che vuoi che l'IA scriva qualcosa per te. Che sia un post per i social, una bozza di newsletter, un titolo per un articolo del blog o una descrizione prodotto.

**Come usarlo:**
Ci sono due modi principali per dare istruzioni:

1.  **Istruzione Diretta:** Dici all'IA esattamente cosa vuoi che faccia. Ad esempio: "Scrivi un post su X". Puoi mettere le istruzioni all'inizio, alla fine o in entrambi i punti del tuo messaggio. Sii dettagliato: non aver paura di scrivere un paragrafo intero per descrivere l'output desiderato.
    *   *Esempio semplice:*
        ```
        Estrai il nome dell'autore dalla citazione seguente.

        “Alcuni umani teorizzano che le specie intelligenti si estinguano prima di poter espandersi nello spazio. Se hanno ragione, allora il silenzio del cielo notturno è il silenzio del cimitero.”
        ― Ted Chiang, Exhalation
        ```
        *Output:* Ted Chiang
        (Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1`)

2.  **Completamento:** Inizi tu una frase o un modello di testo, e l'IA cerca di completarlo nel modo più logico. Questo richiede più sperimentazione e l'IA potrebbe non sapere dove fermarsi, quindi potresti dover "tagliare" il testo extra.
    *   *Esempio semplice:*
        ```
        “Alcuni umani teorizzano che le specie intelligenti si estinguano p
        ```
        L'IA cercherà di completare la frase.
        (Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1`)

Le IA più recenti sono molto brave a seguire le istruzioni e a presentare il testo in modo ordinato, specialmente se sei preciso.
(Fonte: `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)

---

### 2. Checklist Prompt (Ruolo, Contesto, Vincoli, Formato)

**Obiettivo:** Creare prompt efficaci e strutturati per ottenere risultati migliori e più pertinenti.

Pensa al tuo prompt come a un brief creativo. Deve contenere tutte le informazioni essenziali.

Ecco una checklist per costruire un prompt completo:

*   **1. Ruolo:** Assegna un ruolo all'IA. Questo la aiuta a capire la prospettiva e il tono.
    *   *Esempio:* "Sei un copywriter esperto in marketing digitale per il settore food."
    *   (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1` - concetto di "system prompt" e sezioni)

*   **2. Contesto:** Fornisci tutte le informazioni di base necessarie.
    *   **Chi è il brand?** (Nome, settore, valori, mission)
    *   **Chi è il pubblico target?** (Età, interessi, problemi, desideri)
    *   **Qual è l'obiettivo del testo?** (Informare, vendere, intrattenere, generare lead)
    *   **Qual è il prodotto/servizio?** (Nome, caratteristiche principali, benefici unici)
    *   (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1` - "Organizing your prompt makes it easier for the model to understand context")

*   **3. Vincoli e Requisiti:** Sii specifico su cosa includere e cosa evitare.
    *   **Lunghezza:** "Massimo 150 parole", "3 paragrafi", "non più di 280 caratteri".
        (Fonte: `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)
    *   **Tono di voce:** "Amichevole e informale", "professionale e autorevole", "ironico", "entusiasta".
    *   **Parole chiave:** "Includi le parole chiave 'sostenibilità', 'innovazione', 'qualità artigianale'".
    *   **Call to Action (CTA):** "Includi una CTA chiara: 'Scopri di più sul nostro sito'".
    *   **Esclusioni:** "Non usare gergo tecnico", "Evita frasi come 'clicca qui'".
    *   **Lingua:** "Scrivi in italiano", "Assicurati che l'output sia in italiano".
        (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
    *   **Varietà:** Se dai esempi, chiedi all'IA di non ripeterli alla lettera ma di usarli come ispirazione per creare frasi nuove e varie.
        (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`, `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

*   **4. Formato dell'Output:** Specifica come vuoi che sia strutturato il testo.
    *   "Formato Markdown (con titoli e liste puntate)."
        (Fonte: `../data/openai-cookbook/examples/Optimize_Prompts.ipynb::chunk8`)
    *   "Lista puntata", "paragrafi separati", "tabella", "solo il testo del post senza introduzioni".
    *   "Usa sezioni chiare e intitolate per organizzare le informazioni."
        (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

*   **5. Esempi (se utili):** Se hai un esempio di testo che ti piace o un modello da seguire, includilo. L'IA tende a seguire molto da vicino gli esempi forniti.
    *   (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`, `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

*   **6. Chiarezza e Precisione:**
    *   Usa frasi brevi e chiare.
    *   Preferisci elenchi puntati ai paragrafi lunghi per le istruzioni.
    *   Evita ambiguità: istruzioni confuse portano a risultati scadenti.
    *   Usa il maiuscolo per enfatizzare le regole più importanti.
    *   Trasforma regole non testuali in testo (es. invece di "SE X > 3 ALLORA ESCALATE", scrivi "SE CI SONO PIÙ DI TRE FALLIMENTI ALLORA ESCALATE").
    *   (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

---

### 3. Esempi Pratici per Social, Newsletter, Sito

**Obiettivo:** Vedere come applicare la checklist a scenari reali di agenzia.

#### Esempio 1: Post per Social Media (Instagram)

**Scenario:** Lanciare un nuovo gusto di gelato artigianale "Pistacchio Salato" per un brand che punta su ingredienti di qualità e innovazione.

```
**Ruolo:** Sei un social media copywriter esperto per brand food.

**Contesto:**
- **Brand:** Gelateria "Dolce Tentazione".
- **Prodotto:** Nuovo gelato "Pistacchio Salato".
- **Valori:** Qualità artigianale, ingredienti selezionati, innovazione nei gusti.
- **Target:** Giovani adulti (25-40 anni), amanti del buon cibo, curiosi di nuove esperienze gustative.
- **Obiettivo:** Creare hype per il lancio, invitare a provare il nuovo gusto.

**Vincoli e Requisiti:**
- **Lunghezza:** Massimo 180 caratteri per il testo principale.
- **Tono di voce:** Entusiasta, goloso, un po' audace.
- **Parole chiave:** "Pistacchio Salato", "Gelato Artigianale", "Novità".
- **Emoji:** Includi 2-3 emoji pertinenti.
- **Hashtag:** Suggerisci 3-5 hashtag popolari e di nicchia.
- **Call to Action:** "Vieni a provarlo!" o simile.

**Formato dell'Output:**
- Testo del post.
- Elenco puntato degli hashtag.
```
(Fonte: Basato sui principi di `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1` per istruzioni dettagliate e `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9` per la specificità delle regole.)

#### Esempio 2: Oggetto e Anteprima per Newsletter

**Scenario:** Promuovere un webinar gratuito su "Strategie SEO per E-commerce" per un'agenzia di marketing digitale.

```
**Ruolo:** Sei un email marketing specialist per un'agenzia di comunicazione digitale.

**Contesto:**
- **Brand:** "Digital Boost Agency".
- **Evento:** Webinar gratuito "Strategie SEO per E-commerce".
- **Valori:** Competenza, utilità, risultati concreti.
- **Target:** Proprietari di e-commerce, marketing manager, professionisti del digitale.
- **Obiettivo:** Massimizzare le iscrizioni al webinar.

**Vincoli e Requisiti:**
- **Lunghezza Oggetto:** Massimo 50 caratteri.
- **Lunghezza Anteprima:** Massimo 80 caratteri.
- **Tono di voce:** Professionale, informativo, persuasivo.
- **Urgenza/Beneficio:** Sottolinea il valore del webinar e l'opportunità.
- **Emoji:** Non usare emoji nell'oggetto o nell'anteprima.

**Formato dell'Output:**
- Oggetto: [Testo]
- Anteprima: [Testo]
```
(Fonte: Basato sui principi di `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1` per istruzioni dettagliate e `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9` per la specificità delle regole.)

#### Esempio 3: Descrizione Prodotto per Sito E-commerce

**Scenario:** Scrivere una descrizione per un paio di scarpe da running ecologiche.

```
**Ruolo:** Sei un copywriter e-commerce specializzato in prodotti sostenibili.

**Contesto:**
- **Brand:** "GreenStride".
- **Prodotto:** Scarpe da running modello "EcoRunner".
- **Caratteristiche:** Realizzate con materiali riciclati, suola ammortizzata, leggere, traspiranti.
- **Benefici:** Comfort, performance, rispetto per l'ambiente, stile moderno.
- **Target:** Atleti e appassionati di running attenti all'ambiente e alla sostenibilità.
- **Obiettivo:** Convincere all'acquisto evidenziando i benefici e i valori etici.

**Vincoli e Requisiti:**
- **Lunghezza:** Circa 200 parole, suddivise in 3-4 paragrafi.
- **Tono di voce:** Ispirazionale, tecnico ma accessibile, orientato ai valori.
- **Parole chiave:** "Scarpe running ecologiche", "materiali riciclati", "sostenibilità", "performance".
- **Struttura:** Introduzione accattivante, dettagli sui materiali/tecnologia, benefici per l'utente, conclusione con invito all'azione implicito.

**Formato dell'Output:**
- Testo descrittivo in paragrafi.
```
(Fonte: Basato sui principi di `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1` per istruzioni dettagliate e `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9` per la specificità delle regole.)

---

### 4. Errori Comuni

**Obiettivo:** Imparare dagli errori più frequenti per migliorare i tuoi prompt.

Anche le IA più avanzate possono dare risultati deludenti se le istruzioni non sono chiare. Ecco gli errori più comuni da evitare:

*   **1. Istruzioni Vaghi o Ambigue:**
    *   **Errore:** "Scrivi qualcosa sul nostro nuovo prodotto."
    *   **Perché è un errore:** L'IA non sa cosa scrivere, per chi, con quale obiettivo o tono.
    *   **Soluzione:** Sii sempre specifico. Chi, cosa, quando, dove, perché e come.
    *   (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1` - "Be precise: Ambiguity or conflicting instructions = degraded performance")

*   **2. Troppi Vincoli o Vincoli Contraddittori:**
    *   **Errore:** "Scrivi un post divertente, ma molto formale, di massimo 10 parole, che spieghi in dettaglio un concetto complesso."
    *   **Perché è un errore:** L'IA si trova in un vicolo cieco. Un tono divertente e formale sono difficili da conciliare, e 10 parole non bastano per un concetto complesso.
    *   **Soluzione:** Rivedi i tuoi vincoli. Assicurati che siano realistici e non si contraddicano. Se chiedi un comportamento specifico ("devi sempre fare X"), aggiungi una via d'uscita ("se non hai abbastanza informazioni, chiedi all'utente").
    *   (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)

*   **3. Mancanza di Esempi o Istruzioni per la Varietà:**
    *   **Errore:** Fornire all'IA una lista di frasi di esempio senza istruzioni aggiuntive.
    *   **Perché è un errore:** L'IA potrebbe usare quelle frasi alla lettera, rendendo il testo ripetitivo e "robotico".
    *   **Soluzione:** Se usi esempi, istruisci l'IA a "usare queste frasi come ispirazione, ma variarle per evitare ripetizioni".
    *   (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`, `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

*   **4. Non Specificare il Formato o la Lunghezza:**
    *   **Errore:** "Scrivi un testo per il blog."
    *   **Perché è un errore:** L'IA potrebbe produrre un testo troppo lungo, troppo corto, senza titoli, o con una formattazione indesiderata (es. spiegazioni extra sul perché ha scritto così).
    *   **Soluzione:** Specifica sempre il formato (es. "in Markdown, con un titolo H1 e 3 paragrafi") e la lunghezza ("circa 300 parole").
    *   (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`, `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)

*   **5. Non Organizzare il Prompt:**
    *   **Errore:** Scrivere tutte le istruzioni in un unico, lungo paragrafo.
    *   **Perché è un errore:** Rende difficile per l'IA (e per te) identificare le diverse parti delle istruzioni e seguirle.
    *   **Soluzione:** Usa sezioni chiare e intitolate (come in questa guida: Ruolo, Contesto, Vincoli, Formato) e elenchi puntati. Questo aiuta l'IA a elaborare meglio le informazioni.
    *   (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

---

### 5. Limiti e Buone Pratiche

**Obiettivo:** Gestire le aspettative sull'IA e adottare strategie per massimizzare i risultati.

L'IA è uno strumento potente, ma ha i suoi limiti. Conoscendoli e adottando buone pratiche, puoi usarla al meglio.

#### Limiti

*   **1. Non è un Essere Umano:** L'IA non "capisce" nel senso umano. Segue schemi e probabilità. Non ha intuizione, emozioni o esperienza di vita.
*   **2. Può "Allucinare":** A volte, l'IA può inventare fatti, citazioni o informazioni che sembrano plausibili ma non sono vere. Questo è particolarmente vero se non ha abbastanza dati o se le istruzioni sono ambigue.
    (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **3. Sensibilità alla Lunghezza:** I prompt molto lunghi possono confondere l'IA o farle perdere il contesto iniziale. Anche se non c'è un limite fisso universale, è bene essere concisi pur essendo completi.
    (Fonte: `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0` - concetto di limite di token, generalizzato per LLMs)
*   **4. Ripetizioni:** Senza istruzioni specifiche, l'IA può cadere in schemi ripetitivi o frasi generiche.
    (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **5. Dipendenza dal Contesto del Prompt:** In alcuni contesti (es. trascrizione audio), l'IA potrebbe seguire più lo "stile" del prompt che le istruzioni dirette contenute in esso. Per la generazione di testo, le istruzioni dirette sono solitamente ben seguite, ma è un promemoria dell'importanza del *come* si formula il prompt.
    (Fonte: `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0`, adattato per il contesto di generazione testo)

#### Buone Pratiche

*   **1. Iterare Senza Sosta:** Il primo prompt raramente è quello perfetto. Modifica piccole parole, cambia l'ordine delle istruzioni, aggiungi o togli dettagli. Ogni piccola modifica può fare una grande differenza nel risultato.
    (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **2. Dai Esempi:** Se hai un'idea precisa di stile, tono o struttura, fornire uno o più esempi all'IA è uno dei modi più efficaci per guidarla.
    (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **3. Sii Preciso e Chiaro:** La chiarezza è fondamentale. Evita ambiguità. Se un'istruzione può essere interpretata in più modi, l'IA potrebbe scegliere quello sbagliato.
    (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **4. Controlla Sempre l'Output:** L'IA è un assistente, non un sostituto. Rileggi sempre il testo generato, verifica i fatti, adatta il tono e assicurati che sia in linea con il brand e gli obiettivi. Non pubblicare mai un testo generato dall'IA senza revisione.
*   **5. Struttura il Tuo Prompt:** Usa sezioni chiare, elenchi puntati e, se necessario, il maiuscolo per enfatizzare le regole chiave. Un prompt ben organizzato è più facile da capire per l'IA e da modificare per te.
    (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **6. Chiedi Chiarimenti:** Se l'IA non ha abbastanza informazioni per eseguire un compito, istruiscila a "chiedere all'utente le informazioni mancanti" piuttosto che inventare.
    (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)

---

### Fonti

*   `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`
*   `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Optimize_Prompts.ipynb`
*   `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`


## Prompt engineering per rilevamento lingua

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


## Prompt engineering per cross-tabular analysis

Ecco la sezione del manuale sull'uso dell'IA per l'analisi cross-tabulare, pensata per copywriter e content strategist.

---

# Analisi Cross-Tabulare con l'IA: Scopri i Dati Nascosti

L'analisi cross-tabulare ti aiuta a incrociare dati diversi per trovare relazioni e insight. L'IA può semplificare enormemente questo processo, trasformando tabelle complesse in risposte chiare e azioni concrete.

## Obiettivo
Usare l'IA per analizzare tabelle di dati, identificare trend, anomalie e ottenere suggerimenti pratici per migliorare le tue strategie di contenuto e marketing.

## Quando serve (keyword x canale x conversioni)

Immagina di avere un foglio Excel con dati sulle performance delle tue campagne. L'analisi cross-tabulare con l'IA è il tuo superpotere quando devi:

*   **Capire cosa funziona meglio:** Quali keyword generano più conversioni su Google Ads rispetto a Facebook?
*   **Ottimizzare i canali:** Quali canali portano più lead qualificati per un certo tipo di contenuto (es. guide, post blog, video)?
*   **Identificare problemi o opportunità:** C'è un canale che ha un costo per acquisizione troppo alto per una specifica keyword? O un contenuto che performa benissimo su un canale e potresti replicare altrove?
*   **Valutare l'efficacia delle tue strategie:** Le tue nuove headline o call-to-action hanno migliorato il tasso di conversione su un segmento specifico di pubblico?

In pratica, ogni volta che hai dati in tabella e vuoi farli "parlare" per prendere decisioni migliori.

## Come descrivere la tabella al modello

L'IA non è un mago, ma un assistente molto intelligente. Per farla lavorare al meglio, devi darle i dati in modo chiaro.

1.  **Copia e Incolla:** Il modo più semplice è copiare l'intera tabella (o una sua parte significativa) direttamente nel prompt.
2.  **Descrivi le Colonne:** Se la tabella è molto grande o complessa, puoi prima descrivere le colonne principali e il loro significato.
    *   Esempio: "Ho una tabella con le seguenti colonne: 'Keyword', 'Canale', 'Impression', 'Clic', 'Conversioni', 'Costo per Conversione'."
3.  **Indica l'Obiettivo:** Spiega chiaramente cosa vuoi scoprire.

**Esempio di descrizione:**

"Ho una tabella che mostra i risultati di un A/B test per due modelli di copy (Controllo e Modello X). Le colonne sono:
*   `Group`: Il nome del gruppo (Controllo o Modello X).
*   `Users Assigned`: Numero di utenti assegnati a quel gruppo.
*   `Conversions`: Numero di conversioni ottenute.
*   `Conversion Rate`: Tasso di conversione.
*   `p-value`: Valore statistico per la significatività.
*   `Stat. Significant?`: Indica se il risultato è statisticamente significativo.
*   `Winner?`: Indica se il modello è il vincitore.
*   `Type I Error Guarded?`: Indica se il rischio di falso positivo è controllato.
*   `Type II Error Guarded?`: Indica se la dimensione del campione è sufficiente per rilevare un effetto reale.

Ecco la tabella:"
```
| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|-----------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                   | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                   | Yes                    |
```
*Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5*

## Prompt template (pattern, outlier, azioni)

Una volta che l'IA ha la tua tabella, puoi farle domande specifiche.

### Per trovare pattern (modelli ricorrenti)

*   "Analizza la tabella seguente: [incolla tabella]. Quali sono i pattern più evidenti tra le colonne 'Keyword', 'Canale' e 'Conversioni'? C'è una combinazione che performa meglio?"
*   "Basandoti su questi dati, quali tipi di contenuti (se presenti in tabella) sembrano generare più engagement su Instagram rispetto a LinkedIn?"
*   "C'è una correlazione tra il 'Costo per Clic' e il 'Tasso di Conversione' per le keyword a coda lunga?"

### Per identificare outlier (dati anomali)

*   "Nella tabella [incolla tabella], ci sono valori anomali o inaspettati nella colonna 'Costo per Acquisizione'? Se sì, quali sono e per quali keyword/canali?"
*   "Identifica eventuali performance eccezionalmente alte o basse nella colonna 'Tasso di Conversione' e suggerisci possibili ragioni."
*   "C'è qualche riga che si discosta significativamente dalla media per 'Clic' e 'Impression'?"
*   *Riferimento implicito all'identificazione di problemi:* L'IA può aiutare a "trovare rapidamente esempi di fallimenti nella consegna" o "identificare il problema esatto nei dati".
    *Fonte: ../data/openai-cookbook/examples/Semantic_text_search_using_embeddings.ipynb::chunk1, ../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb::chunk3*

### Per suggerire azioni concrete

*   "Basandoti sull'analisi di questa tabella [incolla tabella], suggerisci 3 azioni concrete che potremmo intraprendere per migliorare il tasso di conversione complessivo."
*   "Quali modifiche al copy o alla strategia di targeting suggeriresti per i canali con il 'Costo per Lead' più alto?"
*   "Se l'obiettivo è aumentare le conversioni del 20%, quali keyword o canali dovremmo prioritizzare e perché?"
*   "Data la performance del 'Modello X' rispetto al 'Controllo' (vedi tabella sopra), quale azione dovremmo intraprendere per la nostra prossima campagna?"

## Esempio con tabella piccola (da agenzia)

**Scenario:** La tua agenzia ha condotto un A/B test per due versioni di un copy pubblicitario (Controllo vs. Modello X) su una landing page, per vedere quale genera più iscrizioni alla newsletter.

**Il tuo prompt:**

"Ho i risultati di un A/B test per due varianti di copy. Analizza questa tabella e dimmi quale copy ha performato meglio e perché. Suggerisci un'azione basata su questi dati.

Ecco la tabella:
```
| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|-----------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                   | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                   | Yes                    |
```
*Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5*

**Risposta attesa dall'IA (parafrasata):**

"Il 'Modello X' ha performato meglio. Ha raddoppiato il tasso di conversione (2.0% vs 1.0%) rispetto al 'Controllo', con lo stesso numero di utenti. Il 'p-value' di 0.012 indica che questa differenza è statisticamente significativa, quindi è molto improbabile che sia dovuta al caso.

**Azione suggerita:** Dovresti implementare il 'Modello X' come copy standard per la tua landing page, poiché ha dimostrato di essere significativamente più efficace nel generare conversioni."

## Limiti e buone pratiche

### Limiti

*   **Qualità dei dati:** L'IA è brava solo quanto i dati che le dai. Se la tua tabella contiene errori o dati incompleti, anche l'analisi dell'IA sarà imprecisa.
*   **Complessità eccessiva:** Per tabelle estremamente grandi o con relazioni molto complesse tra centinaia di colonne, l'IA potrebbe faticare a dare insight profondi senza una guida molto specifica.
*   **"Allucinazioni":** A volte l'IA può "inventare" interpretazioni o conclusioni che non sono supportate dai dati. Verifica sempre le sue affermazioni.
*   **Mancanza di contesto:** L'IA non conosce il tuo business, i tuoi clienti o le condizioni di mercato. Le sue raccomandazioni sono basate solo sui dati forniti.

### Buone pratiche

*   **Sii specifico:** Più la tua domanda è chiara e dettagliata, migliore sarà la risposta. Non chiedere solo "cosa vedi?", ma "quali keyword hanno il CPA più basso su Google Ads?"
*   **Fornisci contesto:** Se ci sono fattori esterni importanti (es. un lancio di prodotto recente, una festività), menzionali nel prompt.
*   **Verifica sempre:** Le analisi dell'IA sono un ottimo punto di partenza, ma non sostituire mai il tuo giudizio professionale. Controlla i numeri e le conclusioni.
*   **Itera:** Se la prima risposta non è soddisfacente, riformula la domanda o aggiungi più dettagli. Pensa a una conversazione.
*   **Chiedi spiegazioni:** Se l'IA ti dà un'azione, chiedile "Perché lo suggerisci?" o "Su quali dati specifici ti basi?".
*   **Attenzione alla precisione:** L'IA può generare "alta precisione/recall per l'identificazione dei problemi" e "buona accuratezza nel individuare il problema esatto nei dati", ma questo dipende dalla qualità del prompt e dei dati.
    *Fonte: ../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb::chunk3*

---

## Fonti

*   `../data/openai-cookbook/examples/completions_usage_api.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb`
*   `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb`
*   `../data/openai-cookbook/examples/Semantic_text_search_using_embeddings.ipynb`

