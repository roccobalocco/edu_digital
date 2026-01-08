# Manuale d’Uso dell’IA (Bozza automatizzata)

## Introduzione

Questa bozza è stata generata automaticamente a partire da contenuti del repository OpenAI Cookbook, selezionati e rielaborati per un contesto di agenzia (copywriter e content strategist).

## Indice

- [Prompt engineering per generazione di testi](#prompt-engineering-per-generazione-di-testi)
- [Prompt engineering per rilevamento lingua](#prompt-engineering-per-rilevamento-lingua)
- [Prompt engineering per cross-tabular analysis](#prompt-engineering-per-cross-tabular-analysis)

---

## Prompt engineering per generazione di testi

# Manuale d'Uso dell'IA per Copywriter e Content Strategist: Prompt Engineering per la Generazione di Testi

L'Intelligenza Artificiale è uno strumento potente, ma la sua efficacia dipende da come le parliamo. Il "Prompt Engineering" è l'arte di dare istruzioni chiare e precise all'IA per ottenere i risultati desiderati. Pensala come l'arte di scrivere un brief perfetto, ma per una macchina.

## 1. Cos'è e quando usarlo

**Cos'è il Prompt Engineering?**
È il processo di formulare le domande o le istruzioni (i "prompt") che dai all'IA per guidarla nella generazione di testo. Non è magia, ma comunicazione efficace. Più sei chiaro e specifico, più l'IA sarà in grado di darti ciò che cerchi. L'IA, infatti, cerca di prevedere la "prossima parola" più probabile in base al tuo input, e un buon prompt la indirizza verso la direzione giusta.

**Obiettivo:**
L'obiettivo è ottenere testi di qualità, pertinenti e utili dall'IA, riducendo al minimo le revisioni e il tempo speso per correggere output generici o sbagliati.

**Quando usarlo (e perché è utile nel tuo lavoro quotidiano):**

*   **Generare bozze iniziali:** Hai bisogno di un punto di partenza per un articolo, un post social, una newsletter o una landing page? L'IA può creare una prima stesura in pochi secondi.
*   **Riformulare testi esistenti:** Devi adattare un testo a un tono di voce diverso, accorciarlo, allungarlo o renderlo più coinvolgente? L'IA può farlo per te.
*   **Brainstorming di idee:** Sei a corto di idee per titoli, slogan, argomenti per blog o CTA? L'IA può darti una spinta creativa.
*   **Estrarre informazioni specifiche:** Hai un lungo testo e vuoi solo riassumerlo o estrarre dati chiave (es. nomi, date, concetti principali)? L'IA può aiutarti.
*   **Adattare contenuti per diverse piattaforme:** Trasformare un post di blog in una serie di tweet o in una didascalia Instagram.

**Come funziona (in breve):**
Quando scrivi un prompt, stai dando all'IA un'indicazione su cosa scrivere dopo. Ci sono due modi principali per farlo:

*   **Istruzione diretta:** Dici all'IA esattamente cosa vuoi che faccia.
    *   *Esempio:* "Estrai il nome dell'autore dalla citazione seguente: 'Alcuni umani teorizzano che le specie intelligenti si estinguano prima di potersi espandere nello spazio. Se hanno ragione, allora il silenzio del cielo notturno è il silenzio del cimitero.' ― Ted Chiang, Exhalation"
    *   *Output atteso:* "Ted Chiang"
    *   *(Riferimento: ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1)*
*   **Completamento:** Inizi tu una frase o un pattern, e l'IA lo continua. Questo metodo richiede più sperimentazione e spesso è usato per frasi brevi o per continuare un elenco.
    *   *(Riferimento: ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1)*

## 2. Checklist prompt (ruolo, contesto, vincoli, formato)

Un prompt ben fatto è come un brief di progetto impeccabile: fornisce tutte le informazioni necessarie per ottenere il risultato desiderato. Ecco gli elementi chiave da includere:

1.  **Ruolo:**
    *   **Obiettivo:** Dire all'IA "chi deve essere" per orientare il suo stile e la sua prospettiva.
    *   **Come usarlo:** Inizia il prompt con "Sei un..." o "Agisci come un...".
    *   **Esempio da agenzia:**
        *   "Sei un copywriter esperto di marketing digitale specializzato in SEO."
        *   "Sei un social media manager per un brand di moda sostenibile."
        *   "Sei un giornalista investigativo che scrive un articolo imparziale."
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

2.  **Obiettivo/Task:**
    *   **Obiettivo:** Spiegare chiaramente cosa deve fare l'IA.
    *   **Come usarlo:** Sii diretto e specifico sul compito.
    *   **Esempio da agenzia:**
        *   "Scrivi 3 idee per post Instagram."
        *   "Genera 5 opzioni per l'oggetto di una newsletter."
        *   "Riscrivi questo paragrafo per un pubblico B2B."
    *   *(Riferimento: ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1)*

3.  **Contesto:**
    *   **Obiettivo:** Fornire all'IA tutte le informazioni di base necessarie per comprendere la situazione.
    *   **Come usarlo:** Includi dettagli sul cliente, prodotto, servizio, target, evento, ecc.
    *   **Esempio da agenzia:**
        *   "Il nostro cliente è un'azienda che produce caffè biologico equosolidale."
        *   "Il prodotto è un nuovo smartphone con fotocamera avanzata e batteria a lunga durata."
        *   "Il target sono giovani professionisti tra i 25 e i 35 anni, attenti alla tecnologia e all'ambiente."
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

4.  **Vincoli/Linee guida:**
    *   **Obiettivo:** Stabilire regole chiare su cosa includere, cosa evitare e come presentare il testo.
    *   **Come usarlo:** Elenca requisiti specifici.
    *   **Esempio da agenzia:**
        *   **Tono di voce:** "Il tono deve essere amichevole e professionale." / "Usa un linguaggio giovane, ironico e informale."
        *   **Lunghezza:** "Ogni post non deve superare i 180 caratteri." / "L'email deve essere concisa, massimo 150 parole."
            *   *(Riferimento: ../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1)*
        *   **Parole chiave:** "Includi le parole chiave 'sostenibilità', 'innovazione' e 'futuro digitale'."
        *   **Call to Action (CTA):** "Includi una CTA chiara: 'Scopri di più sul nostro sito' o 'Scarica la guida gratuita'."
        *   **Cosa evitare:** "Non usare superlativi assoluti." / "Evita il gergo tecnico troppo complesso."
        *   **Varietà:** "Varia il linguaggio e le espressioni per non sembrare ripetitivo."
            *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

5.  **Formato:**
    *   **Obiettivo:** Indicare all'IA come deve essere strutturato l'output per renderlo immediatamente utilizzabile.
    *   **Come usarlo:** Specifica il tipo di formattazione desiderato.
    *   **Esempio da agenzia:**
        *   "Formato: elenco puntato con didascalia e hashtag separati."
        *   "Formato: tabella con due colonne: 'Oggetto' e 'Descrizione'."
        *   "Formato: testo in Markdown con intestazioni e grassetti."
        *   "Formato: 3 paragrafi separati."
    *   *(Riferimento: ../data/openai-cookbook/examples/Optimize_Prompts.ipynb::chunk8, ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

6.  **Esempi (se utili):**
    *   **Obiettivo:** Se hai un'idea molto precisa dello stile o della struttura, fornire un esempio può essere estremamente efficace. L'IA tende a seguire da vicino gli esempi.
    *   **Come usarlo:** Includi un breve esempio di testo che ti piace o che vorresti come modello.
    *   **Esempio da agenzia:** "Ecco un esempio di post che ci piace: [Testo del post di esempio]. Segui questo stile."
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

## 3. Esempi per social/newsletter/sito

Ecco alcuni esempi pratici di prompt "da agenzia" che puoi usare e adattare.

### Esempio 1: Post Instagram

**Prompt:**
"Sei un social media manager per un brand di abbigliamento sostenibile chiamato 'EcoChic'.
Scrivi 3 idee per un post Instagram che annunci la nuova collezione primavera/estate.
Il target sono giovani adulti (20-35 anni) attenti all'ambiente e alla moda etica.
Il tono deve essere ispirazionale, fresco e leggermente giocoso.
Ogni post deve includere 3 hashtag pertinenti e una Call to Action che inviti a visitare il nostro sito (www.ecochic.it).
Non superare i 180 caratteri per la didascalia.
Formato: elenco puntato, con didascalia e hashtag separati per ogni idea."

**Output Atteso (esempio generato dall'IA):**

*   **Idea 1**
    *   **Didascalia:** Colori che sbocciano, tessuti che rispettano. La nostra P/E è qui per farti brillare, in armonia con la natura. 🌸✨ Scopri la collezione!
    *   **Hashtag:** #EcoChic #ModaSostenibile #NuovaCollezione
*   **Idea 2**
    *   **Didascalia:** Pronta a indossare il futuro? La collezione P/E di EcoChic unisce stile e responsabilità. Fai la differenza, un outfit alla volta. 💚 Visita il sito!
    *   **Hashtag:** #FashionEtica #PrimaveraEstate #EcoFriendly
*   **Idea 3**
    *   **Didascalia:** Sole, stile e sostenibilità! ☀️ La nostra nuova collezione P/E ti aspetta. Eleganza che fa bene al pianeta. Esplora ora su www.ecochic.it!
    *   **Hashtag:** #StileConsapevole #EcoFashion #MadeWithLove

### Esempio 2: Oggetto Newsletter

**Prompt:**
"Sei un copywriter per un'azienda di software B2B, 'TechSolutions', che offre soluzioni di gestione progetti.
Genera 5 opzioni per l'oggetto di una newsletter che promuove un webinar gratuito sul 'Project Management Agile: Dalla Teoria alla Pratica'.
Il target sono Project Manager, team leader e responsabili IT.
Il tono deve essere professionale, informativo e accattivante, con un senso di urgenza o esclusività.
Formato: elenco numerato."

**Output Atteso (esempio generato dall'IA):**

1.  Webinar Esclusivo: Domina l'Agile Project Management
2.  Ultimi Posti! Scopri l'Agile PM con TechSolutions
3.  Trasforma i Tuoi Progetti: Iscriviti al Webinar Agile Gratuito
4.  Agile Project Management: Le Strategie che Funzionano (Webinar)
5.  Non Perdere: Webinar Gratuito su Agile PM per Leader

### Esempio 3: Sezione Sito Web

**Prompt:**
"Sei un content strategist.
Scrivi il testo per la sezione 'Chi Siamo' di un'agenzia di comunicazione digitale specializzata in performance marketing, 'PixelBoost'.
Il testo deve trasmettere professionalità, innovazione, orientamento ai risultati e un approccio strategico.
Includi la nostra mission: 'Trasformare idee in successi misurabili'.
Lunghezza massima: 200 parole, diviso in 2-3 paragrafi.
Formato: testo continuo."

**Output Atteso (esempio generato dall'IA):**

**Chi Siamo: PixelBoost – La Tua Strategia Digitale, Misurata.**

In PixelBoost, crediamo che ogni idea abbia il potenziale per diventare un grande successo. Siamo un'agenzia di comunicazione digitale specializzata in performance marketing, con una missione chiara: trasformare idee in successi misurabili. Con un team di esperti appassionati, combiniamo creatività, analisi dei dati e le più recenti tecnologie per costruire strategie digitali che non solo catturano l'attenzione, ma generano risultati concreti e tangibili per il tuo business.

Il nostro approccio è basato sulla trasparenza e sull'innovazione. Lavoriamo fianco a fianco con i nostri clienti, trasformando le loro sfide in opportunità e guidandoli attraverso il complesso panorama digitale. Dal SEO alle campagne a pagamento, dai social media alla content strategy, ogni azione è pensata per massimizzare il ROI e garantire una crescita sostenibile. Scegli PixelBoost per un partner che non si limita a promettere, ma a realizzare.

## 4. Errori comuni

Anche con la migliore IA, un prompt mal formulato può portare a risultati deludenti. Ecco gli errori più comuni da evitare:

*   **Istruzioni vaghe o ambigue:**
    *   *Errore:* "Scrivi qualcosa di bello sul nostro prodotto."
    *   *Perché è un errore:* Cosa significa "bello" per l'IA? Non ha un senso estetico umano.
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Mancanza di contesto:**
    *   *Errore:* "Scrivi un post per Facebook."
    *   *Perché è un errore:* Su quale prodotto? Per quale target? Qual è l'obiettivo? L'IA inventerà o darà un output generico.
*   **Non specificare il formato:**
    *   *Errore:* "Dammi delle idee per titoli."
    *   *Perché è un errore:* Potresti ricevere un blocco di testo anziché un elenco puntato o numerato, rendendo più difficile l'uso.
*   **Non definire il tono di voce:**
    *   *Errore:* "Scrivi un testo per il sito."
    *   *Perché è un errore:* Il testo potrebbe risultare piatto, generico o inappropriato per il tuo brand.
*   **Aspettarsi magia (o che l'IA legga nel pensiero):**
    *   *Errore:* Non fornire all'IA gli elementi chiave e aspettarsi un capolavoro.
    *   *Perché è un errore:* L'IA è un motore linguistico, non un creativo autonomo. Se non le dai gli ingredienti, non può cucinare.
*   **Istruzioni contraddittorie:**
    *   *Errore:* "Sii conciso ma spiega ogni dettaglio in modo approfondito."
    *   *Perché è un errore:* L'IA si confonderà e l'output sarà probabilmente insoddisfacente su entrambi i fronti.
*   **Mancanza di varietà:**
    *   *Errore:* Non chiedere all'IA di variare il linguaggio o le espressioni.
    *   *Perché è un errore:* L'IA può usare frasi simili o ripetere concetti, rendendo il testo monotono.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*
*   **Eccessiva verbosità dell'IA:**
    *   *Errore:* Non specificare limiti di lunghezza o chiedere un output troppo dettagliato quando non serve.
    *   *Perché è un errore:* L'IA potrebbe aggiungere prose non necessarie o spiegazioni ridondanti.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*
*   **Allucinazioni/Informazioni errate:**
    *   *Errore:* Fidarsi ciecamente di ogni affermazione dell'IA.
    *   *Perché è un errore:* L'IA può generare informazioni false o fuorvianti con grande sicurezza.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*

## 5. Limiti e buone pratiche

L'IA è uno strumento potente, ma ha i suoi limiti. Conoscendoli e adottando le giuste pratiche, potrai massimizzare i benefici e minimizzare i rischi.

### Limiti dell'IA nella generazione di testi:

*   **Creatività limitata:** L'IA "ricombina" informazioni e stili esistenti. Non crea idee completamente nuove o concetti rivoluzionari come un copywriter umano.
*   **Mancanza di empatia e comprensione profonda:** Non capisce le sfumature culturali, le emozioni complesse, l'umorismo sottile o il sarcasmo come un essere umano.
*   **Bias:** L'IA è addestrata su enormi quantità di dati. Se questi dati contengono pregiudizi (culturali, di genere, ecc.), l'IA potrebbe riprodurli nei suoi output.
*   **"Allucinazioni":** L'IA può generare informazioni false, inventare fatti o citazioni inesistenti con grande sicurezza. È fondamentale verificare sempre i dati.
*   **Conoscenza limitata nel tempo:** La sua conoscenza si ferma alla data del suo ultimo addestramento. Non ha accesso a informazioni in tempo reale o a eventi recenti (a meno che non sia collegata a internet, ma anche in quel caso, la sua capacità di discernimento è limitata).
*   **Limite di "memoria" (o contesto):** L'IA può elaborare solo una certa quantità di testo alla volta. Se il tuo prompt o la conversazione diventano troppo lunghi, potrebbe "dimenticare" le prime parti o non considerarle. Questo è il concetto semplificato di "token limit".
    *   *(Riferimento: ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1, ../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0)*

### Buone pratiche per un Prompt Engineering efficace:

*   **Itera, itera, itera:** Il primo prompt non è quasi mai quello perfetto. Modifica, aggiungi dettagli, prova diverse formulazioni. Piccoli cambiamenti nelle parole possono fare una grande differenza nel risultato.
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Sii specifico e dettagliato:** Più informazioni dai all'IA, migliore sarà il risultato. Non lasciare nulla al caso.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Usa sezioni chiare e punti elenco:** Organizza il prompt con intestazioni, punti elenco o grassetti per renderlo più leggibile per l'IA (e per te). Questo aiuta l'IA a capire il contesto e a mantenere la coerenza.
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Fornisci esempi:** Se hai un'idea precisa del formato o dello stile, mostra all'IA un esempio di come vorresti il risultato. L'IA tende a seguire da vicino gli esempi forniti.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9, ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Definisci i vincoli:** Specifica sempre lunghezza, tono, parole chiave da includere, CTA e, soprattutto, cosa evitare.
*   **Verifica sempre l'output:** L'IA è un assistente, non un sostituto. Controlla fatti, coerenza, tono, originalità e aderenza al brief. Non pubblicare mai un testo generato dall'IA senza una revisione umana.
*   **Chiedi all'IA di fare domande:** Se l'IA non ha abbastanza informazioni per completare il compito, istruiscila a chiedere chiarimenti anziché inventare.
    *   *(Riferimento: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*
*   **Usa il Markdown per enfatizzare:** Le maiuscole o la formattazione possono aiutare a far risaltare le regole chiave nel tuo prompt, rendendole più facili da seguire per l'IA.
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*   **Semplifica concetti complessi:** Se hai regole complesse, cerca di trasformarle in istruzioni testuali chiare e dirette.
    *   *(Riferimento: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

---

## Fonti

*   `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`
*   `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Optimize_Prompts.ipynb`
*   `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`

---

## Prompt engineering per rilevamento lingua

# Rilevamento Lingua con l'IA: La Guida per Copywriter e Content Strategist

Capire in che lingua è scritto un testo è fondamentale per chi lavora con i contenuti. L'Intelligenza Artificiale può aiutarci a farlo in modo rapido e su larga scala, liberandoci da compiti ripetitivi e permettendoci di concentrarci sulla strategia.

---

## Quando serve in agenzia

Identificare la lingua di un testo è un'esigenza comune in molte attività quotidiane di un'agenzia. Ecco alcuni scenari pratici:

*   **Gestione Social Media Multilingue**: Immagina di dover monitorare i commenti su un post che ha raggiunto utenti in diversi paesi. L'IA può aiutarti a capire subito se un commento è in italiano, spagnolo o cinese, permettendoti di rispondere nella lingua corretta o di indirizzarlo al team giusto.
    *   *Riferimento:* `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` (riferimento all'estrazione di sentiment multilingue che richiede la conoscenza della lingua).
*   **Analisi di Contenuti Generati dagli Utenti (UGC)**: Se la tua agenzia gestisce campagne che raccolgono recensioni, post o feedback da tutto il mondo, l'IA può categorizzare questi contenuti per lingua, rendendo l'analisi molto più efficiente.
*   **Personalizzazione di Campagne Email**: Vuoi inviare email promozionali ma non sei sicuro della lingua preferita da ogni utente? L'IA può analizzare le interazioni passate o i dati disponibili per suggerire la lingua più appropriata per la comunicazione.
*   **Smistamento Contenuti per Team Specifici**: Per agenzie con team dedicati a mercati diversi, l'IA può automaticamente instradare i testi (es. richieste di supporto, articoli di blog) al team che parla quella lingua.
*   **Estrazione di Sentiment su Mercati Diversi**: Prima di analizzare il tono (positivo, negativo, neutro) di un testo, è essenziale sapere in che lingua è scritto. L'IA può prima identificare la lingua e poi procedere con l'analisi del sentiment.
    *   *Riferimento:* `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` (esempio di dataset per estrazione di sentiment multilingue).

---

## Prompt Template

Per chiedere all'IA di rilevare la lingua, puoi usare un prompt semplice e diretto. L'obiettivo è ottenere una risposta chiara e concisa.

**Obiettivo:** Chiedere all'IA di identificare la lingua di un testo.

**Come usarlo:** Inserisci il testo da analizzare nel prompt.

```
Sei un esperto di lingue.
Ti verrà fornito un testo. Il tuo compito è identificare la lingua in cui è scritto.
Restituisci solo il nome della lingua (es. "Italiano", "Inglese", "Spagnolo") e nient'altro.
Assicurati che la tua risposta sia solo il nome della lingua.

Testo: "{testo_da_analizzare}"
```
*   *Riferimento:* Adattato da `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3` (struttura di prompt per classificazione).

---

## Esempi pratici

Vediamo come applicare il prompt template a diversi tipi di contenuti che potresti incontrare in agenzia.

### Esempio 1: Commento Social Media

**Scenario:** Un utente ha lasciato un commento sulla pagina Facebook di un cliente.

**Testo da analizzare:** "No estoy seguro de lo que pienso sobre este producto."

**Prompt:**
```
Sei un esperto di lingue.
Ti verrà fornito un testo. Il tuo compito è identificare la lingua in cui è scritto.
Restituisci solo il nome della lingua (es. "Italiano", "Inglese", "Spagnolo") e nient'altro.
Assicurati che la tua risposta sia solo il nome della lingua.

Testo: "No estoy seguro de lo que pienso sobre este producto."
```

**Output dell'IA:**
```
Spagnolo
```
*   *Riferimento:* `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` (testo di esempio in spagnolo).

### Esempio 2: Recensione Prodotto (UGC)

**Scenario:** Una recensione di un'app, da categorizzare per il team di marketing.

**Testo da analizzare:** "It's okay – not great but not bad either."

**Prompt:**
```
Sei un esperto di lingue.
Ti verrà fornito un testo. Il tuo compito è identificare la lingua in cui è scritto.
Restituisci solo il nome della lingua (es. "Italiano", "Inglese", "Spagnolo") e nient'altro.
Assicurati che la tua risposta sia solo il nome della lingua.

Testo: "It's okay – not great but not bad either."
```

**Output dell'IA:**
```
Inglese
```
*   *Riferimento:* `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` (testo di esempio in inglese).

### Esempio 3: Feedback Cliente (Email/Ticket)

**Scenario:** Un feedback ricevuto tramite un modulo di contatto, da smistare al servizio clienti corretto.

**Testo da analizzare:** "总体来说，我对这款产品很满意。"

**Prompt:**
```
Sei un esperto di lingue.
Ti verrà fornito un testo. Il tuo compito è identificare la lingua in cui è scritto.
Restituisci solo il nome della lingua (es. "Italiano", "Inglese", "Spagnolo") e nient'altro.
Assicurati che la tua risposta sia solo il nome della lingua.

Testo: "总体来说，我对这款产品很满意。"
```

**Output dell'IA:**
```
Cinese
```
*   *Riferimento:* `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3` (testo di esempio in cinese).

---

## Ambiguità e casi misti

L'IA è potente, ma non infallibile. Ci sono situazioni in cui il rilevamento della lingua può essere più complesso:

*   **Testi Brevi o Frammentati**: Un singolo hashtag, un'abbreviazione o una frase molto corta possono non contenere abbastanza informazioni per un'identificazione precisa.
*   **Code-Switching (Lingue Miste)**: Quando un testo contiene frasi o parole di più lingue (es. "Mi piace molto this product!"), l'IA potrebbe avere difficoltà a scegliere una lingua predominante o a identificare tutte le lingue presenti.
    *   *Riferimento:* `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5` (il modello può "code switch" tra lingue).
*   **Lingue Molto Simili**: Alcune lingue, come lo spagnolo e il portoghese, o il ceco e lo slovacco, possono avere somiglianze che rendono difficile la distinzione per l'IA, specialmente con testi brevi.
*   **Errori di Battitura o Grammaticali**: Un testo con molti errori può confondere l'IA, portandola a un'identificazione errata.

**Come gestire l'ambiguità:**

Per questi casi, puoi modificare il prompt per chiedere all'IA di:
*   **Indicare la fiducia**: "Identifica la lingua e dammi un punteggio di fiducia da 0 a 100."
    *   *Riferimento:* `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1` (menziona l'uso di `logprobs` per misurare la fiducia).
*   **Elencare più lingue**: "Identifica tutte le lingue presenti nel testo."
*   **Specificare la lingua principale**: "Identifica la lingua principale del testo."

---

## Limiti e buone pratiche

Per ottenere il massimo dall'IA nel rilevamento della lingua, è utile conoscere i suoi limiti e seguire alcune buone pratiche.

### Limiti

*   **Non è un traduttore**: L'IA rileva la lingua, non la traduce. Per la traduzione, userai strumenti specifici.
*   **Mancanza di contesto culturale profondo**: L'IA non comprende le sfumature culturali o i dialetti regionali come farebbe un madrelingua.
*   **Performance variabile con lingue meno diffuse**: Le lingue con meno dati di addestramento potrebbero essere rilevate con minore accuratezza.

### Buone Pratiche

*   **Sii specifico nel prompt**: Chiedi esattamente ciò che vuoi. Se vuoi solo il nome della lingua, dillo chiaramente.
    *   *Riferimento:* `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26` (l'importanza di "enforce strict extraction guidelines").
*   **Richiedi un formato strutturato**: Se possibile, chiedi all'IA di restituire la risposta in un formato che sia facile da usare, come "Lingua: [nome lingua]". Questo rende l'integrazione con altri strumenti più semplice.
    *   *Riferimento:* `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb::chunk2` (i formati strutturati rendono il prompting più semplice e affidabile).
*   **Usa esempi (Few-shot prompting)**: Se l'IA ha difficoltà con tipi specifici di testo o lingue, puoi includere 1-2 esempi nel prompt per mostrarle come vuoi che risponda.
    *   *Riferimento:* `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26` ("Includes few-shot examples").
*   **Chiedi un punteggio di fiducia**: Per i casi ambigui, chiedere un punteggio di fiducia può aiutarti a decidere se un'identificazione è affidabile o se richiede una revisione umana.
    *   *Riferimento:* `../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1` (l'uso di `logprobs` per la fiducia nelle classificazioni).
*   **Pre-elabora testi molto brevi**: Per testi estremamente corti (es. una singola parola), l'accuratezza del rilevamento diminuisce. Valuta se questi testi sono davvero rilevanti per l'analisi o se possono essere ignorati.
*   **Evita la ripetizione inutile**: Se stai usando l'IA per generare risposte complesse che includono il rilevamento della lingua, assicurati che le istruzioni non portino a risposte robotiche o ripetitive.
    *   *Riferimento:* `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5` (regola per "Reduce Repetition").

---

## Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`

---

## Prompt engineering per cross-tabular analysis

# Analisi di Dati Tabellari con l'IA: Trovare Pattern e Azioni

Come content strategist o copywriter, ti trovi spesso a dover interpretare dati per capire cosa funziona, cosa no e dove migliorare. L'IA può essere un alleato potente per analizzare tabelle di dati, identificare tendenze e suggerire azioni concrete, senza dover essere un esperto di statistica.

---

### Quando serve (Analisi Keyword x Canale x Conversioni)

**Obiettivo:** Usare l'IA per dare un senso a tabelle di dati, scoprendo rapidamente cosa sta succedendo e cosa potresti fare.

Immagina di avere una tabella con i risultati delle tue campagne di content marketing: quali keyword hanno portato più traffico da un certo canale? Quali contenuti hanno generato più conversioni? L'IA può aiutarti a:

*   **Identificare i "pezzi forti"**: Quali combinazioni di keyword, canali o tipi di contenuto stanno performando meglio?
*   **Scovare i "punti deboli"**: Dove ci sono cali inaspettati o performance sotto la media?
*   **Capire le relazioni**: C'è un legame tra l'uso di una certa call-to-action e un aumento delle conversioni?
*   **Prendere decisioni rapide**: Basandoti su dati chiari, puoi ottimizzare le tue strategie di contenuto e copywriting.

**Esempio pratico da agenzia:**
Hai i dati di un A/B test su due versioni di una landing page. L'IA può dirti quale versione ha convertito di più e se la differenza è significativa, aiutandoti a scegliere la versione migliore per il lancio.

---

### Come descrivere la tabella al modello

**Obiettivo:** Presentare i tuoi dati all'IA in un formato che sia facile da capire e analizzare.

Non devi essere un programmatore. L'IA capisce bene i dati se glieli presenti in modo chiaro e strutturato.

**Come fare:**
1.  **Copia e incolla:** Il modo più semplice è copiare la tabella direttamente da un foglio di calcolo o da un report e incollarla nel tuo prompt.
2.  **Formato leggibile:** Assicurati che le colonne siano ben separate (es. con tab, spazi o pipe `|`) e che le intestazioni siano chiare.
3.  **Spiega il contesto:** Prima della tabella, dai all'IA un'idea generale di cosa stai analizzando.

**Esempio di presentazione (da integrare con istruzioni chiare):**
Non ci sono istruzioni dirette nelle fonti su "come descrivere la tabella al modello", ma possiamo dedurre che un formato testuale chiaro è l'ideale.

```
Ecco una tabella con i risultati di un A/B test su due modelli di pagina di conversione.
Analizza i dati e dimmi quale modello ha performato meglio e perché.

| Gruppo                      | Utenti Assegnati | Conversioni | Tasso di Conversione | p-value | Significativo? | Vincitore? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|
| Controllo (Modello Attuale)    | 1500           | 15          | 1.0%            | --      | Riferimento          | No      |
| Modello X (Variante)          | 1500           | 30          | 2.0%            | 0.012   | Sì                 | Sì      |
```
*(Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5)*

---

### Prompt template (pattern, outlier, azioni)

**Obiettivo:** Creare prompt efficaci per ottenere dall'IA le analisi che ti servono.

Un buon prompt guida l'IA a cercare esattamente ciò che ti interessa.

**Struttura del prompt:**

1.  **Contesto:** Spiega di cosa tratta la tabella.
2.  **Obiettivo:** Chiedi all'IA cosa vuoi che faccia (es. "analizza", "identifica", "suggerisci").
3.  **Cosa cercare:** Specifica pattern, anomalie o relazioni.
4.  **Output desiderato:** Chiedi suggerimenti pratici o un riassunto.

**Prompt Template Esempio:**

```
"Ho la seguente tabella di dati [descrivi brevemente il tipo di dati, es. 'performance di campagne digitali'].

[Incolla qui la tua tabella di dati]

Analizza questi dati e:
1.  Identifica i **pattern principali** o le tendenze più evidenti (es. quali elementi performano meglio/peggio).
2.  Segnala eventuali **anomalie o valori anomali** (outlier) che meritano attenzione.
3.  Sulla base di questa analisi, suggerisci **3-5 azioni concrete** che un content strategist o copywriter potrebbe intraprendere per migliorare i risultati.
4.  Spiega brevemente il **perché** di ogni suggerimento."
```

---

### Esempio con tabella piccola

**Obiettivo:** Vedere un esempio pratico di come funziona l'analisi con l'IA.

Usiamo la tabella dell'A/B test vista prima.

**Prompt:**

```
"Ho la seguente tabella che mostra i risultati di un A/B test per due versioni di una pagina di conversione. 'Modello Attuale' è la versione di controllo, 'Modello X' è la variante.

| Gruppo                      | Utenti Assegnati | Conversioni | Tasso di Conversione | p-value | Significativo? | Vincitore? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|
| Controllo (Modello Attuale)    | 1500           | 15          | 1.0%            | --      | Riferimento          | No      |
| Modello X (Variante)          | 1500           | 30          | 2.0%            | 0.012   | Sì                 | Sì      |

Analizza questi dati e:
1.  Qual è il modello vincitore e perché?
2.  Quali sono le implicazioni per la nostra strategia di contenuto e copywriting?
3.  Suggerisci un'azione immediata basata su questi risultati."
```
*(Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5)*

**Output (Esempio di risposta dell'IA):**

"Analizzando i dati forniti:

1.  **Il modello vincitore è il 'Modello X (Variante)'**. Ha un tasso di conversione del 2.0% rispetto all'1.0% del 'Modello Attuale'. Il 'p-value' di 0.012 indica che questa differenza è statisticamente significativa, il che significa che è molto improbabile che il risultato sia dovuto al caso.
2.  **Implicazioni per la strategia:** Il 'Modello X' ha dimostrato di essere due volte più efficace nel convertire gli utenti. Questo suggerisce che gli elementi di contenuto e copywriting specifici di questa variante (es. headline, call-to-action, layout, argomentazioni) risuonano meglio con il pubblico e sono più persuasivi.
3.  **Azione immediata:** Sostituire immediatamente il 'Modello Attuale' con il 'Modello X' su tutte le pagine pertinenti per massimizzare le conversioni. Successivamente, analizzare in dettaglio cosa rende il 'Modello X' così efficace per replicare questi elementi in altre aree del sito o in future campagne."

---

### Limiti e buone pratiche

**Obiettivo:** Comprendere cosa l'IA può e non può fare, per usarla al meglio.

L'IA è uno strumento potente, ma non è infallibile.

**Limiti:**

*   **Qualità dei dati:** Se i dati che fornisci sono incompleti o errati, l'analisi dell'IA sarà altrettanto imprecisa. L'IA non può correggere dati sporchi.
*   **Contesto mancante:** L'IA non conosce il contesto più ampio della tua agenzia, del tuo cliente o del mercato. Le sue analisi si basano solo sui dati forniti.
*   **Profondità statistica:** L'IA può identificare pattern e anomalie, ma non esegue analisi statistiche complesse con la stessa rigorosità di un data scientist. Il "p-value" nell'esempio è un dato che deve essere già presente nella tabella.
*   **"Allucinazioni":** A volte l'IA può inventare conclusioni o spiegazioni che sembrano plausibili ma non sono supportate dai dati.
*   **Complessità eccessiva:** Tabelle molto grandi o con troppe colonne possono confondere l'IA, portando a risultati meno accurati.

**Buone pratiche:**

1.  **Inizia in piccolo:** Comincia con tabelle semplici e domande chiare.
2.  **Verifica sempre:** Le conclusioni dell'IA sono un ottimo punto di partenza, ma verifica sempre i dati e le logiche sottostanti, soprattutto per decisioni importanti.
3.  **Fornisci contesto:** Più contesto dai nel prompt, più l'IA sarà in grado di fornire analisi pertinenti.
4.  **Sii specifico:** Chiedi esattamente cosa vuoi sapere (es. "identifica i 3 prodotti più venduti", "spiega perché il tasso di conversione è calato").
5.  **Itera:** Se la prima risposta non è soddisfacente, riformula il prompt o aggiungi più dettagli.
6.  **Pensa come un analista:** Anche se l'IA fa il lavoro pesante, devi comunque pensare criticamente ai dati e alle domande che poni.

---

### Fonti

*   ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb
*   ../data/openai-cookbook/examples/completions_usage_api.ipynb
*   ../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb

---
