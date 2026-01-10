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