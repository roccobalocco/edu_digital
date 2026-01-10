# Manuale d’Uso dell’IA Generativa

## Prompt engineering per generazione di testi

# Manuale IA per Copywriter e Content Strategist: Prompt Engineering per Generazione di Testi

## Cos'è e quando usarlo

Il "Prompt Engineering" è semplicemente l'arte di dare istruzioni chiare e precise all'Intelligenza Artificiale per ottenere il testo che desideri. Immagina di parlare con un assistente molto intelligente ma che ha bisogno di indicazioni dettagliate per capire esattamente cosa vuoi.

**Obiettivo:** Imparare a formulare richieste efficaci per far sì che l'IA produca contenuti utili e pertinenti per il tuo lavoro.

**Quando usarlo:**
*   **Generare idee e bozze:** Hai bisogno di spunti per un post social, un titolo per una newsletter o un'idea per un articolo? L'IA può darti una base di partenza.
*   **Scrivere testi completi:** Dalla bozza di un'email a un paragrafo per una pagina web, l'IA può aiutarti a creare contenuti in linea con il tuo brief.
*   **Adattare o riassumere testi:** Vuoi trasformare un lungo articolo in un post breve per i social media o riassumere un report? L'IA può farlo.
*   **Migliorare lo stile o il tono:** Hai un testo ma vuoi renderlo più persuasivo, più formale o più amichevole? L'IA può aiutarti a rifinirlo.
*   **Tradurre o localizzare:** Per testi semplici, l'IA può essere un valido supporto.

**Come funziona:**
Scrivi le tue istruzioni all'inizio o alla fine del tuo messaggio all'IA. Più sei dettagliato, più l'IA capirà cosa vuoi. Non aver paura di scrivere un paragrafo intero per spiegare l'output desiderato. L'IA farà del suo meglio per seguire le tue indicazioni e poi si fermerà.

*Esempio base:*
```
Estrai il nome dell'autore dalla citazione qui sotto.

“Alcuni esseri umani teorizzano che le specie intelligenti si estinguano prima di potersi espandere nello spazio. Se hanno ragione, allora il silenzio del cielo notturno è il silenzio del cimitero.”
― Ted Chiang, Exhalation
```
*Output dell'IA:*
```
Ted Chiang
```
(Riferimento: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1`)

## Checklist per un Prompt Efficace

Per ottenere i migliori risultati, pensa al tuo prompt come a un mini-brief. Ecco gli elementi chiave da includere:

*   **Ruolo:** Chiedi all'IA di assumere un ruolo specifico. Questo la aiuta a capire la prospettiva e il tono.
    *   *Esempio:* "Sei un copywriter esperto di marketing digitale."
*   **Contesto:** Fornisci tutte le informazioni rilevanti sulla situazione, il prodotto, il pubblico e l'obiettivo del testo.
    *   *Esempio:* "Stiamo lanciando un nuovo servizio di consulenza SEO per piccole imprese. Il nostro pubblico sono imprenditori che non hanno tempo per l'ottimizzazione e cercano risultati rapidi."
*   **Vincoli e Istruzioni Specifiche:** Dettaglia cosa deve fare l'IA e cosa deve evitare.
    *   **Obiettivo del testo:** "L'obiettivo è generare lead qualificati e spingere all'iscrizione alla nostra newsletter."
    *   **Tono di voce:** "Il tono deve essere professionale ma amichevole, autorevole ma accessibile."
    *   **Punti chiave da includere:** "Includi i benefici principali: aumento visibilità, risparmio di tempo, reportistica chiara."
    *   **Punti chiave da evitare:** "Non usare gergo troppo tecnico. Non promettere risultati irrealistici."
    *   **Lunghezza:** "Il testo deve essere conciso, massimo 150 parole." (Riferimento: `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)
    *   **Varietà:** Se chiedi più opzioni, specifica "assicurati che le opzioni siano diverse tra loro per stile e approccio." (Riferimento: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **Formato:** Specifica come vuoi che sia strutturata la risposta.
    *   *Esempio:* "Fornisci 3 opzioni diverse. Ogni opzione deve includere: Titolo, Corpo del testo, Call to Action. Usa il formato Markdown." (Riferimento: `../data/openai-cookbook/examples/Optimize_Prompts.ipynb::chunk8`)
*   **Esempi (se utili):** Se hai un esempio di stile o di output che ti piace, includilo. L'IA tende a seguire da vicino gli esempi forniti.
    *   *Esempio:* "Ecco un esempio di post che ci piace per il tono: [link o testo di esempio]." (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

**Consiglio:** Organizza il tuo prompt in sezioni chiare e usa i punti elenco. Questo rende più facile per l'IA capire il contesto e per te modificare le sezioni problematiche. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)

## Esempi Pratici "da Agenzia"

Ecco come applicare la checklist a scenari comuni:

### Esempio 1: Post per Social Media (LinkedIn)

**Obiettivo:** Generare un post LinkedIn per promuovere un webinar gratuito sul content marketing.

```
**Ruolo:** Sei un Social Media Manager esperto di LinkedIn.
**Contesto:**
-   **Azienda:** "ContentFlow", agenzia di content marketing.
-   **Prodotto/Servizio:** Webinar gratuito "Strategie di Content Marketing per il 2024".
-   **Pubblico:** Imprenditori, marketing manager, liberi professionisti interessati a migliorare la loro strategia di contenuti.
-   **Obiettivo:** Generare iscrizioni al webinar.
**Vincoli e Istruzioni Specifiche:**
-   **Tono:** Professionale, informativo, leggermente persuasivo, orientato ai benefici.
-   **Punti chiave da includere:**
    -   Data e ora del webinar: 15 maggio, ore 10:00.
    -   Cosa impareranno: tecniche SEO per contenuti, storytelling efficace, misurazione ROI.
    -   Beneficio principale: Ottimizzare la propria strategia di contenuti per il successo nel 2024.
    -   Call to Action chiara per l'iscrizione.
-   **Lunghezza:** Massimo 1000 caratteri (circa 150 parole).
-   **Hashtag:** Suggerisci 3-5 hashtag pertinenti.
**Formato:** Fornisci 2 opzioni di post, diverse per approccio. Ogni opzione deve avere: Titolo accattivante, Corpo del testo, Call to Action, Hashtag.
```

### Esempio 2: Oggetto e Anteprima per Newsletter

**Obiettivo:** Creare oggetto e testo di anteprima per una newsletter che annuncia una nuova guida gratuita sull'email marketing.

```
**Ruolo:** Sei un Copywriter specializzato in Email Marketing.
**Contesto:**
-   **Azienda:** "MailBoost", piattaforma di email marketing.
-   **Prodotto/Servizio:** Nuova guida gratuita "Email Marketing per Principianti: La Guida Completa".
-   **Pubblico:** Piccoli imprenditori, blogger, startup che vogliono iniziare o migliorare il loro email marketing.
-   **Obiettivo:** Spingere al download della guida.
**Vincoli e Istruzioni Specifiche:**
-   **Tono:** Entusiasta, utile, orientato alla soluzione di un problema.
-   **Punti chiave da includere:**
    -   La guida è gratuita.
    -   Cosa impareranno: costruire liste, scrivere email efficaci, evitare spam.
    -   Beneficio principale: Avviare campagne email di successo senza sforzo.
-   **Lunghezza:** Oggetto massimo 60 caratteri. Testo di anteprima massimo 100 caratteri.
-   **Evita:** Linguaggio troppo promozionale o "clickbait" esagerato.
**Formato:** Fornisci 3 combinazioni diverse di Oggetto e Testo di Anteprima.
```

### Esempio 3: Paragrafo per Pagina Sito Web (Sezione "Chi Siamo")

**Obiettivo:** Scrivere un paragrafo per la sezione "Chi Siamo" di un'agenzia di web design.

```
**Ruolo:** Sei un Brand Storyteller per un'agenzia di web design.
**Contesto:**
-   **Azienda:** "PixelPerfect Studio", agenzia di web design che crea siti web su misura.
-   **Pubblico:** Aziende e professionisti che cercano un partner per la loro presenza online.
-   **Obiettivo:** Trasmettere professionalità, creatività e un approccio orientato al cliente.
**Vincoli e Istruzioni Specifiche:**
-   **Tono:** Ispirante, professionale, focalizzato sulla partnership e sui risultati.
-   **Punti chiave da includere:**
    -   La nostra passione per il design e la tecnologia.
    -   L'importanza di un sito web efficace per il business.
    -   Il nostro approccio collaborativo con il cliente.
    -   L'obiettivo di trasformare idee in realtà digitali di successo.
-   **Lunghezza:** Massimo 120 parole.
-   **Evita:** Frasi fatte o troppo generiche.
**Formato:** Fornisci un singolo paragrafo ben strutturato.
```

## Errori Comuni

Anche con un buon prompt, a volte l'IA può non dare il risultato sperato. Ecco alcuni errori comuni da cui imparare:

*   **Istruzioni ambigue o contrastanti:** Se le tue indicazioni non sono chiare o si contraddicono, l'IA farà fatica a capire cosa vuoi, portando a risultati scadenti. Sii preciso. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Troppa verbosità dell'IA:** A volte l'IA tende a dilungarsi troppo o a spiegare le sue decisioni. Se non vuoi questo, devi specificarlo.
    *   *Soluzione:* "Sii conciso. Non aggiungere spiegazioni o introduzioni." (Riferimento: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **Ripetizioni o frasi robotiche:** Senza istruzioni specifiche, l'IA può usare le stesse frasi o suonare un po' "robotica".
    *   *Soluzione:* "Varia il linguaggio e le espressioni. Evita ripetizioni." (Riferimento: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`, `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **"Allucinazioni" o informazioni inventate:** L'IA può a volte inventare fatti o dettagli se non ha abbastanza informazioni per rispondere.
    *   *Soluzione:* Se l'IA non ha abbastanza informazioni per completare un compito, chiedile di segnalartelo o di fare domande. (Riferimento: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **Istruzioni non seguite alla lettera:** Alcuni modelli di IA, o in contesti specifici (come la trascrizione audio), potrebbero non interpretare le istruzioni dirette come faresti tu, ma piuttosto cercare di emulare uno stile o un pattern.
    *   *Soluzione:* Se un'istruzione diretta non funziona, prova a fornire un esempio dello stile o del formato desiderato. (Riferimento: `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0`)

## Limiti e Buone Pratiche

### Limiti dell'IA

*   **Lunghezza del prompt:** Ogni IA ha un limite sulla quantità di testo che può elaborare in una singola interazione (sia per le tue istruzioni che per la sua risposta). Se il tuo prompt è troppo lungo, l'IA potrebbe ignorare le parti finali. Sii conciso ma completo. (Riferimento: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1`, `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0`)
*   **Comprensione del contesto:** L'IA non ha una vera "comprensione" come un essere umano. Si basa sui pattern e sulle probabilità. Questo significa che sfumature, ironia o contesti molto complessi possono essere difficili da cogliere.
*   **Creatività limitata:** L'IA è eccellente nel generare variazioni su un tema o combinare idee esistenti. La vera innovazione o la creatività "fuori dagli schemi" rimane una prerogativa umana.
*   **Bias nei dati di addestramento:** L'IA riflette i bias presenti nei dati con cui è stata addestrata. Questo può portare a contenuti stereotipati o non inclusivi. È fondamentale rivedere criticamente ogni output.

### Buone Pratiche per i Copywriter e Content Strategist

1.  **Itera senza sosta:** Non aspettarti la perfezione al primo colpo. Modifica il tuo prompt, prova piccole variazioni nelle parole, aggiungi o togli dettagli. Piccoli cambiamenti possono fare una grande differenza. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
2.  **Sii preciso e specifico:** Evita generalizzazioni. Più dettagli dai, migliore sarà il risultato. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
3.  **Usa i punti elenco e sezioni chiare:** Struttura il tuo prompt in modo logico. Questo aiuta l'IA a elaborare le informazioni e rende il tuo prompt più facile da leggere e modificare. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
4.  **Fornisci esempi:** Se hai un esempio di testo, tono o formato che ti piace, includilo. L'IA è molto brava a seguire gli esempi. (Riferimento: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
5.  **Controlla la lunghezza e la verbosità:** Specifica sempre limiti di lunghezza chiari. Se l'IA è troppo prolissa, chiedile di essere più concisa. (Riferimento: `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)
6.  **Chiedi chiarimenti:** Se l'IA non ha abbastanza informazioni per svolgere un compito, istruiscila a chiederti i dettagli mancanti piuttosto che inventare. (Riferimento: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
7.  **Rivedi e rifinisci:** L'IA è un assistente, non un sostituto. Ogni testo generato deve essere attentamente rivisto, modificato e adattato al tuo brand e al tuo pubblico. Aggiungi il tuo tocco umano, la tua esperienza e la tua creatività.

---

## Fonti

*   `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`
*   `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Optimize_Prompts.ipynb`
*   `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`


## Prompt engineering per rilevamento lingua

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


## Prompt engineering per cross-tabular analysis

Ecco la sezione del manuale d'uso dell'IA, pensata per copywriter e content strategist, focalizzata sull'analisi di dati tabellari.

---

# Analisi di Dati Tabellari con l'IA

Questa sezione ti mostra come usare l'intelligenza artificiale per dare un senso rapido ai tuoi dati, come quelli di performance delle campagne o del sito web, presentati in tabelle.

## Obiettivo

Trasformare tabelle di numeri in insight chiari e azioni concrete per la tua strategia di contenuto e marketing. L'IA ti aiuta a:
*   Trovare velocemente trend e pattern.
*   Identificare cosa funziona bene e cosa meno.
*   Ricevere suggerimenti per migliorare le tue campagne o i tuoi contenuti.

## Quando serve (es. keyword x canale x conversioni)

Immagina di avere un foglio Excel o un report con dati come questi:
*   **Performance delle keyword:** quali keyword portano più traffico o conversioni su diversi canali (Google Ads, SEO, Social).
*   **Risultati A/B test:** confrontare due versioni di una landing page o di un copy per vedere quale converte meglio.
*   **Analisi dei canali:** capire quale canale (email, social, blog) genera più engagement o vendite per specifici tipi di contenuto.
*   **Monitoraggio costi:** tenere d'occhio le spese e identificare picchi o anomalie.

In tutti questi casi, l'IA può farti risparmiare ore di analisi manuale, evidenziando subito i punti chiave.

## Come descrivere la tabella al modello

Per far sì che l'IA capisca i tuoi dati, devi presentarli in modo chiaro. Il modo più semplice è copiare e incollare la tabella direttamente nel prompt, o descriverla con precisione.

**Consigli utili:**
*   **Incolla la tabella:** Se possibile, copia e incolla la tabella direttamente dal tuo foglio di calcolo o report. L'IA è brava a leggere formati tabellari.
*   **Nomi delle colonne:** Assicurati che i nomi delle colonne siano chiari e descrittivi (es. "Tasso di Conversione", "Utenti Assegnati", "Costo per Click").
*   **Contesto:** Aggiungi una breve frase che spieghi di cosa parla la tabella e qual è il tuo obiettivo (es. "Questa è una tabella con i risultati di un A/B test per la nostra nuova landing page").

**Esempio di descrizione (da usare nel prompt):**

```
Ecco una tabella che mostra i risultati di un A/B test per due modelli di pagina (Controllo vs. Modello X) in termini di utenti, conversioni e tassi di conversione.
```

## Prompt template (pattern, outlier, azioni)

Usa questo schema per chiedere all'IA di analizzare i tuoi dati. Ricorda di adattarlo alle tue esigenze specifiche.

**Struttura del Prompt:**

```
[CONTESTO GENERALE: Spiega brevemente di cosa tratta la tabella e qual è il tuo obiettivo.]

Ecco la tabella di dati che voglio analizzare:
[INCOLLA QUI LA TUA TABELLA]

Basandoti su questi dati, per favore:
1.  **Identifica pattern o tendenze significative:** Ci sono elementi che spiccano per performance (positive o negative)?
2.  **Segnala eventuali anomalie o valori anomali:** C'è qualcosa che sembra fuori posto o inaspettato?
3.  **Suggerisci azioni concrete:** Quali decisioni dovrei prendere o quali modifiche dovrei apportare alla mia strategia di contenuto/marketing basandomi su questi insight?
```

*Fonte: Adattato da concetti di analisi dati presenti in diversi chunk.*

## Esempio con tabella piccola

Prendiamo un esempio pratico da agenzia: un A/B test per una pagina di conversione.

**Scenario:** Abbiamo testato due versioni di una pagina di iscrizione (Controllo e Modello X) e vogliamo capire quale ha performato meglio e perché.

**Input (nel tuo prompt):**

```
Ho i risultati di un A/B test per due modelli di pagina di conversione (Controllo e Modello X).
La tabella mostra il numero di utenti assegnati a ciascun gruppo, le conversioni ottenute, il tasso di conversione, il p-value (che indica la significatività statistica) e se il risultato è significativo.

Analizza questa tabella e dimmi cosa dovrei fare per ottimizzare la nostra strategia di contenuto/UX.

| Gruppo                     | Utenti Assegnati | Conversioni | Tasso di Conversione | p-value | Significativo? | Vincitore? |
|----------------------------|------------------|-------------|----------------------|---------|----------------|------------|
| Controllo (Modello Attuale)| 1500             | 15          | 1.0%                 | --      | Riferimento    | No         |
| Modello X (Variante)       | 1500             | 30          | 2.0%                 | 0.012   | Sì             | Sì         |
```
*Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5*

**Output (esempio di risposta dell'IA):**

```
**Analisi dei Pattern:**
*   Il "Modello X (Variante)" ha un tasso di conversione doppio (2.0%) rispetto al "Controllo (Modello Attuale)" (1.0%).
*   Il p-value di 0.012 per il Modello X indica che questa differenza è statisticamente significativa, cioè è molto improbabile che sia dovuta al caso.

**Anomalie:**
*   Non ci sono anomalie evidenti nei dati presentati. Il Modello X si distingue chiaramente come la performance migliore.

**Azioni Concrete:**
1.  **Implementa il Modello X:** Dato che il Modello X è il vincitore statisticamente significativo, dovresti procedere con la sua implementazione come nuova versione standard della pagina di conversione.
2.  **Analizza gli elementi vincenti:** Rivedi attentamente il Modello X per identificare quali specifici elementi di contenuto, copy, design o user experience hanno contribuito a questo miglioramento. Potrebbe essere il titolo, la call-to-action, la disposizione degli elementi o la chiarezza del messaggio.
3.  **Applica gli insight:** Una volta identificati gli elementi di successo, cerca di replicarli o testarli in altre pagine o campagne per migliorare ulteriormente le performance complessive.
4.  **Continua a testare:** Anche se il Modello X è il vincitore attuale, il testing continuo è fondamentale. Potresti usare il Modello X come nuovo "Controllo" per futuri A/B test.
```

## Limiti e buone pratiche

L'IA è un assistente potente, ma non sostituisce il tuo cervello da content strategist.

### Limiti
*   **Mancanza di contesto:** L'IA vede solo i numeri che le dai. Non conosce la storia dietro quei numeri, le campagne passate, le tendenze di mercato o le specificità del tuo pubblico, a meno che tu non gliele fornisca.
*   **Errori di interpretazione:** Può fare errori di calcolo o interpretazione, specialmente con tabelle complesse o dati ambigui.
*   **Non è un analista dati:** Non ha la stessa capacità di un analista umano di fare inferenze complesse, validare ipotesi o progettare esperimenti statistici rigorosi.
*   **Qualità dei dati:** "Garbage in, garbage out." Se i dati che le fornisci sono sbagliati o incompleti, anche l'analisi dell'IA lo sarà.

### Buone pratiche
1.  **Verifica sempre:** Non prendere mai le conclusioni dell'IA come oro colato. Controlla i dati, i calcoli e il ragionamento.
2.  **Fornisci contesto:** Più informazioni e contesto dai all'IA, migliore sarà la sua analisi. Spiega cosa rappresentano i dati, qual è l'obiettivo della tua analisi e cosa sai già.
3.  **Chiedi il ragionamento:** Se l'IA ti dà un'azione, chiedile "Perché lo suggerisci?" o "Su quali dati ti basi per questa conclusione?". Questo ti aiuta a capire e a validare.
4.  **Inizia in piccolo:** Per familiarizzare, inizia con tabelle semplici e domande dirette.
5.  **Non per decisioni critiche senza supervisione:** Per decisioni ad alto impatto (es. budget consistenti, strategie a lungo termine), usa l'IA come punto di partenza per l'analisi, ma fai sempre validare le conclusioni da un esperto umano.
6.  **Pulisci i dati:** Se i tuoi dati sono disordinati, cerca di pulirli prima di darli all'IA. Rimuovi duplicati, correggi errori di battitura, standardizza i formati.

---

## Fonti

*   `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5`
*   `../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb::chunk3`
*   `../data/openai-cookbook/examples/completions_usage_api.ipynb::chunk5`

