# Manuale d’Uso dell’IA Generativa

## Prompt engineering per generazione di testi

# Manuale d'Uso dell'IA per Copywriter e Content Strategist: Prompt Engineering per Generazione di Testi

Questa sezione ti guiderà nell'arte di "parlare" all'Intelligenza Artificiale per ottenere i testi che desideri, in modo efficace e mirato al tuo lavoro quotidiano in agenzia.

---

## 1. Cos'è e quando usarlo

### Cos'è il Prompt Engineering?
Immagina di avere un assistente molto intelligente ma che ha bisogno di istruzioni precise. Il "Prompt Engineering" è proprio questo: l'arte di dare istruzioni chiare, dettagliate e ben strutturate all'IA per farle generare il testo che hai in mente. Non è programmazione, ma piuttosto una conversazione guidata per ottenere il massimo dall'IA.

### Quando usarlo?
Usa il prompt engineering ogni volta che vuoi che l'IA ti aiuti a:
*   **Generare bozze rapide**: Per post social, titoli, descrizioni prodotto, email, newsletter.
*   **Brainstorming**: Per idee su argomenti, slogan, angolazioni narrative.
*   **Riformulare testi**: Per adattare un contenuto a un pubblico diverso o a un tono specifico.
*   **Riassumere informazioni**: Per condensare articoli lunghi in punti chiave.
*   **Creare varianti**: Per testare diverse versioni di un messaggio pubblicitario.

In pratica, ogni volta che hai un'idea per un testo e vuoi accelerare il processo di scrittura, esplorare diverse opzioni o superare il blocco dello scrittore, il prompt engineering è il tuo alleato.

---

## 2. Checklist per un Prompt Efficace

Un buon prompt è come un briefing ben fatto. Deve contenere tutte le informazioni necessarie affinché l'IA capisca cosa vuoi. Ecco gli elementi chiave da includere:

### A. Ruolo (Chi deve essere l'IA?)
Dai all'IA una "personalità" o un ruolo specifico. Questo la aiuta a calarsi nella parte e a produrre un testo più coerente.
*   **Obiettivo**: Far sì che l'IA adotti il tono e lo stile appropriato.
*   **Come usarlo**: Inizia il prompt specificando il ruolo.
*   **Esempio**:
    *   `Sei un copywriter esperto di marketing digitale specializzato in sostenibilità.`
    *   `Agisci come un social media manager giovane e dinamico.`
    *   `Sei un esperto di SEO e devi ottimizzare un testo.`

### B. Contesto (Di cosa stiamo parlando?)
Fornisci all'IA tutte le informazioni di base sul compito.
*   **Obiettivo**: Dare all'IA il quadro completo per generare un testo pertinente.
*   **Come usarlo**: Spiega l'argomento, il pubblico, l'obiettivo del testo e dove verrà pubblicato.
*   **Esempio**:
    *   `Devi scrivere un post per Instagram. Il nostro brand è "BioDelizie", un'azienda che vende prodotti alimentari biologici e a km zero. Il post deve promuovere il lancio del nostro nuovo caffè 100% arabica biologico.`
    *   `Il pubblico a cui ci rivolgiamo sono giovani professionisti tra i 25 e i 40 anni, attenti alla salute e all'ambiente.`
    *   `L'obiettivo è generare interesse e portare traffico alla pagina prodotto sul nostro sito.`

### C. Vincoli (Cosa deve o non deve fare?)
Qui definisci le regole e i limiti per l'IA. Più sei specifico, migliore sarà il risultato.
*   **Obiettivo**: Controllare la lunghezza, il tono, le parole chiave e altri requisiti specifici.
*   **Come usarlo**: Usa elenchi puntati o frasi chiare per specificare ogni vincolo.
*   **Esempio**:
    *   `Il testo deve essere di massimo 150 parole.`
    *   `Il tono deve essere entusiasta, amichevole e leggermente informale.`
    *   `Includi le parole chiave "caffè biologico", "aroma intenso", "sostenibile".`
    *   `Non usare gergo tecnico o frasi troppo complesse.`
    *   `Aggiungi una call to action chiara: "Scopri di più sul nostro sito!"`
    *   `Evita ripetizioni di frasi o concetti.` (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
    *   `Se non hai abbastanza informazioni per completare il compito, chiedimi chiarimenti.` (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)

### D. Formato (Come deve essere il risultato?)
Indica all'IA come vuoi che sia strutturato il testo finale.
*   **Obiettivo**: Ottenere un output già pronto per l'uso o facile da modificare.
*   **Come usarlo**: Specifica il tipo di formato desiderato.
*   **Esempio**:
    *   `Il testo deve essere formattato come un post Instagram, con emoji pertinenti e almeno 5 hashtag.`
    *   `Presenta il contenuto come un elenco puntato.`
    *   `Fornisci il testo in formato Markdown.` (Fonte: `../data/openai-cookbook/examples/Optimize_Prompts.ipynb::chunk8`)
    *   `Includi un titolo accattivante e una breve descrizione.`

---

## 3. Esempi Pratici "da Agenzia"

Ecco alcuni esempi di prompt completi, basati sulla checklist, per diversi scenari lavorativi.

### Esempio 1: Post per Social Media (Instagram)

```
Sei un social media manager esperto per brand di prodotti biologici.

Devi creare un post per Instagram per "BioDelizie", che promuove il lancio del nostro nuovo caffè 100% arabica biologico.
Il pubblico sono giovani professionisti attenti alla salute e all'ambiente.
L'obiettivo è generare interesse e portare traffico alla pagina prodotto.

Vincoli:
- Lunghezza massima: 120 parole.
- Tono: entusiasta, amichevole, leggermente informale.
- Includi le parole chiave: "caffè biologico", "aroma intenso", "sostenibile", "energia naturale".
- Non usare gergo tecnico.
- Includi una call to action chiara: "Link in bio per scoprire di più!".
- Evita ripetizioni.

Formato:
- Post Instagram completo di testo, emoji pertinenti e 5-7 hashtag.
```
(Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1` per l'idea di istruzioni dettagliate)

### Esempio 2: Oggetto e Anteprima per Newsletter

```
Sei un copywriter specializzato in email marketing per il settore e-commerce.

Devi scrivere l'oggetto e il testo di anteprima (preheader) per una newsletter che annuncia una vendita flash del 30% su tutti i prodotti per la casa di "DesignSmart", un brand di arredamento moderno e minimalista.
Il pubblico sono clienti già iscritti, interessati a offerte e novità.
L'obiettivo è massimizzare il tasso di apertura della newsletter.

Vincoli:
- Oggetto: massimo 60 caratteri, deve creare urgenza e curiosità.
- Anteprima: massimo 100 caratteri, deve rafforzare l'offerta e invitare all'apertura.
- Tono: diretto, accattivante, orientato all'azione.
- Includi la percentuale di sconto e la categoria di prodotti.

Formato:
- Presenta l'oggetto e l'anteprima separatamente, con etichette chiare.
```

### Esempio 3: Descrizione Prodotto per Sito Web

```
Sei un copywriter SEO-oriented per un e-commerce di abbigliamento sportivo.

Devi scrivere una descrizione prodotto per il nostro nuovo "Leggings Performance Pro", un leggings da allenamento ad alta compressione, traspirante e con tasca porta-telefono.
Il pubblico sono atlete e appassionate di fitness che cercano qualità e funzionalità.
L'obiettivo è informare, convincere all'acquisto e migliorare il posizionamento SEO.

Vincoli:
- Lunghezza: 200-250 parole.
- Tono: professionale, motivante, focalizzato sui benefici.
- Includi le parole chiave: "leggings sportivo", "alta compressione", "traspirante", "tasca telefono", "allenamento", "performance".
- Evidenzia 3-4 benefici principali in un elenco puntato.
- Non usare linguaggio troppo tecnico o gergale.

Formato:
- Titolo H2 per il nome del prodotto.
- Paragrafo introduttivo.
- Elenco puntato dei benefici.
- Paragrafo conclusivo con call to action implicita (es. "Aggiungi al carrello").
```

---

## 4. Errori Comuni nel Prompt Engineering

Anche con le migliori intenzioni, è facile cadere in alcune trappole. Conoscerle ti aiuterà a evitarle:

*   **Istruzioni Vaghe**: Chiedere "Scrivi qualcosa sul caffè" è troppo generico. L'IA non sa cosa vuoi esattamente.
*   **Mancanza di Contesto**: Non specificare il pubblico, il brand o l'obiettivo del testo porta a risposte generiche e poco utili.
*   **Troppe Richieste in un Colpo Solo**: Se il compito è complesso, spezzalo in più prompt. Chiedere all'IA di scrivere un intero piano editoriale in un solo prompt è meno efficace che chiederle prima le idee per i temi, poi i titoli, poi le bozze.
*   **Non Specificare il Formato**: Se vuoi un elenco puntato e non lo chiedi, potresti ricevere un blocco di testo difficile da leggere.
*   **Non Iterare**: La prima risposta dell'IA è un punto di partenza. Non aver paura di chiedere modifiche o miglioramenti. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Istruzioni Contraddittorie o Ambiguë**: Se le tue istruzioni si scontrano tra loro (es. "sii formale ma anche divertente"), l'IA farà fatica a capire la direzione e il risultato sarà scadente. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Richiedere un Comportamento "Assoluto"**: Evita frasi come "devi sempre fare X". A volte è meglio aggiungere una clausola come "se non hai abbastanza informazioni, chiedi all'utente". (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)

---

## 5. Limiti e Buone Pratiche

L'IA è uno strumento potente, ma ha i suoi limiti. Usarla al meglio significa conoscerli e adottare strategie intelligenti.

### Limiti dell'IA nella Generazione di Testi
*   **"Allucinazioni"**: L'IA può inventare fatti, dati o citazioni che sembrano plausibili ma sono completamente falsi. **Verifica sempre ogni informazione!** (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **Creatività Limitata**: L'IA rielabora schemi e informazioni esistenti. Non ha vera intuizione o creatività umana. Può sorprenderti, ma non avrà mai un'idea completamente originale nel senso umano del termine.
*   **Ripetitività**: A volte l'IA può usare frasi simili o ripetere concetti, rendendo il testo un po' "robotico". (Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9`)
*   **Mancanza di Sensibilità Umana**: Tono, ironia, sarcasmo e sfumature culturali possono essere difficili da cogliere per l'IA, portando a testi che suonano un po' piatti o inappropriati.
*   **Dipendenza dalle Istruzioni**: La qualità dell'output dipende direttamente dalla qualità del tuo prompt. "Garbage in, garbage out" vale anche qui.

### Buone Pratiche per Massimizzare i Risultati
*   **Sii Specifico e Chiaro**: Non lasciare spazio a interpretazioni. Ogni dettaglio conta. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Usa Esempi**: Se hai uno stile o un formato molto specifico in mente, includi un piccolo esempio nel prompt. L'IA è molto brava a seguire modelli. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Itera e Affina**: Considera la prima risposta dell'IA come una bozza. Chiedi modifiche, aggiustamenti, tagli o espansioni. È un processo collaborativo. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Dividi Compiti Complessi**: Per lavori grandi (es. un intero articolo), chiedi prima la struttura, poi i paragrafi uno alla volta, poi la revisione del tono.
*   **Verifica Sempre**: Fatti, dati, nomi, coerenza del brand e tono di voce. L'IA è un assistente, non un sostituto del tuo giudizio professionale.
*   **Dai un Ruolo all'IA**: Come visto nella checklist, questo aiuta a focalizzare la risposta.
*   **Struttura il Tuo Prompt**: Usa sezioni chiare (come quelle di questa guida) per organizzare le tue istruzioni. Questo rende il prompt più leggibile per te e per l'IA. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Enfatizza le Regole Chiave**: Puoi usare il maiuscolo per evidenziare le istruzioni più importanti. (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Chiedi Varietà**: Se noti che l'IA tende a ripetersi, aggiungi una regola come "Varia il linguaggio e le espressioni per evitare ripetizioni". (Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1`)
*   **Controlla la Lunghezza**: Specifica sempre un limite di parole o caratteri se è importante per la piattaforma di destinazione. (Fonte: `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb::chunk1`)

---

## Fonti

*   `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`
*   `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Optimize_Prompts.ipynb`
*   `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`


## Prompt engineering per rilevamento lingua

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


## Prompt engineering per cross-tabular analysis

# Analisi Dati Incrociati con l'IA: Guida Rapida per Copywriter e Content Strategist

Questa sezione ti mostra come usare l'Intelligenza Artificiale per analizzare rapidamente tabelle di dati, trovare tendenze e ottenere spunti utili per i tuoi contenuti e le tue strategie.

---

### Quando serve (keyword x canale x conversioni)

**Obiettivo:** Trovare rapidamente insight da dati complessi per prendere decisioni informate su contenuti e campagne.

**Quando usarlo:**
*   Hai un foglio Excel o un report con dati che incrociano diverse metriche (es. keyword, canale, conversioni, costo per click).
*   Vuoi capire al volo quali elementi performano meglio o peggio.
*   Hai bisogno di identificare tendenze, anomalie o opportunità per ottimizzare i tuoi testi, le tue landing page o le tue strategie di distribuzione.
*   Devi preparare un riassunto veloce per un cliente o un collega, evidenziando i punti chiave dei dati.

**Esempio pratico da agenzia:**
Immagina di avere un report che mostra le performance delle tue campagne Google Ads e Social Media. Vuoi capire quali keyword o messaggi stanno generando più conversioni su ciascun canale, o se un canale specifico ha un costo per conversione troppo alto. Invece di analizzare riga per riga, puoi chiedere all'IA di fare il lavoro per te.

---

### Come descrivere la tabella al modello

**Obiettivo:** Presentare i tuoi dati all'IA in modo chiaro e comprensibile per ottenere analisi accurate.

**Come usarlo:**
L'IA non "vede" la tua tabella come faresti tu. Devi fornirgliela in un formato testuale semplice e strutturato. Il modo migliore è usare una **tabella in formato Markdown**.

1.  **Copia e incolla i dati:** Se hai una tabella in Excel o Google Sheets, puoi copiarla e incollarla direttamente in un editor di testo, poi formattarla in Markdown.
2.  **Usa le intestazioni:** Assicurati che ogni colonna abbia un nome chiaro e descrittivo.
3.  **Spiega le colonne (se necessario):** Se i nomi delle colonne non sono autoesplicativi o contengono sigle, aggiungi una breve spiegazione sotto la tabella.

**Esempio di descrizione di una tabella (da integrare con i tuoi dati):**

```markdown
Ecco una tabella con i risultati di un A/B test per due modelli di landing page:

| Gruppo                      | Utenti Assegnati | Conversioni | Tasso di Conversione | p-value | Significatività Statistica? | Vincitore? | Errore di Tipo I Controllato? | Errore di Tipo II Controllato? |
|----------------------------|------------------|-------------|----------------------|---------|-----------------------------|------------|-------------------------------|--------------------------------|
| Controllo (Modello Attuale) | 1500             | 15          | 1.0%                 | --      | Riferimento                 | No         | Sì                            | Sì                             |
| Modello X (Variante)       | 1500             | 30          | 2.0%                 | 0.012   | Sì                          | Sì         | Sì                            | Sì                             |

-   **Utenti Assegnati:** Numero di utenti assegnati casualmente a ciascun gruppo.
-   **Conversioni:** Quanti utenti hanno completato l'azione desiderata (es. acquisto, iscrizione).
-   **Tasso di Conversione:** Conversioni divise per utenti assegnati.
-   **p-value:** Indica la probabilità che la differenza osservata sia dovuta al caso. Un valore basso (es. < 0.05) suggerisce che la differenza è significativa.
-   **Significatività Statistica?:** Indica se il p-value è inferiore alla soglia di significatività (solitamente 0.05).
-   **Vincitore?:** Se statisticamente significativo, il modello con il tasso di conversione più alto è il vincitore.
-   **Errore di Tipo I Controllato?:** Indica se il rischio di un falso positivo è stato mantenuto entro la soglia desiderata.
-   **Errore di Tipo II Controllato?:** Indica se la dimensione del campione era sufficiente per rilevare un effetto reale.
```
*Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5*

---

### Prompt template (pattern, outlier, azioni)

**Obiettivo:** Ottenere dall'IA un'analisi strutturata che evidenzi tendenze, anomalie e suggerisca azioni concrete.

**Come usarlo:**
Usa questo template come base, adattandolo ai tuoi dati e al tuo obiettivo specifico.

```
Analizza la seguente tabella di dati:

[INSERISCI QUI LA TUA TABELLA IN FORMATO MARKDOWN]

[INSERISCI QUI LE SPIEGAZIONI DELLE COLONNE, SE NECESSARIO, COME NELL'ESEMPIO PRECEDENTE]

Obiettivo dell'analisi: [Spiega chiaramente cosa vuoi scoprire. Esempio: "Identificare il modello di landing page più performante per aumentare le conversioni."]

Cerca e riassumi in modo conciso:
*   **Pattern e Tendenze:** Quali relazioni o andamenti evidenti emergono tra le diverse colonne?
*   **Outlier e Anomalie:** Ci sono dati insoliti, valori eccezionali o risultati inaspettati che meritano attenzione?
*   **Azioni e Raccomandazioni:** Basandoti su questi dati, quali sono i 3-5 suggerimenti concreti che un copywriter o content strategist dovrebbe considerare per migliorare le performance?

Formato dell'output: Utilizza un elenco puntato per ogni sezione (Pattern, Outlier, Azioni).
```
*Fonte: Da integrare (template creato per l'obiettivo)*

---

### Esempio con tabella piccola

**Obiettivo:** Vedere un esempio completo di prompt e output per un'analisi di dati incrociati.

**Prompt di esempio (da agenzia):**

```
Analizza la seguente tabella con i risultati di un A/B test per due modelli di landing page:

| Gruppo                      | Utenti Assegnati | Conversioni | Tasso di Conversione | p-value | Significatività Statistica? | Vincitore? | Errore di Tipo I Controllato? | Errore di Tipo II Controllato? |
|----------------------------|------------------|-------------|----------------------|---------|-----------------------------|------------|-------------------------------|--------------------------------|
| Controllo (Modello Attuale) | 1500             | 15          | 1.0%                 | --      | Riferimento                 | No         | Sì                            | Sì                             |
| Modello X (Variante)       | 1500             | 30          | 2.0%                 | 0.012   | Sì                          | Sì         | Sì                            | Sì                             |

-   **Utenti Assegnati:** Numero di utenti assegnati casualmente a ciascun gruppo.
-   **Conversioni:** Quanti utenti hanno completato l'azione desiderata (es. acquisto, iscrizione).
-   **Tasso di Conversione:** Conversioni divise per utenti assegnati.
-   **p-value:** Indica la probabilità che la differenza osservata sia dovuta al caso. Un valore basso (es. < 0.05) suggerisce che la differenza è significativa.
-   **Significatività Statistica?:** Indica se il p-value è inferiore alla soglia di significatività (solitamente 0.05).
-   **Vincitore?:** Se statisticamente significativo, il modello con il tasso di conversione più alto è il vincitore.
-   **Errore di Tipo I Controllato?:** Indica se il rischio di un falso positivo è stato mantenuto entro la soglia desiderata.
-   **Errore di Tipo II Controllato?:** Indica se la dimensione del campione era sufficiente per rilevare un effetto reale.

Obiettivo dell'analisi: Identificare il modello di landing page più performante per aumentare le conversioni e suggerire azioni per un copywriter.

Cerca e riassumi in modo conciso:
*   **Pattern e Tendenze:** Quali relazioni o andamenti evidenti emergono tra le diverse colonne?
*   **Outlier e Anomalie:** Ci sono dati insoliti, valori eccezionali o risultati inaspettati che meritano attenzione?
*   **Azioni e Raccomandazioni:** Basandoti su questi dati, quali sono i 3-5 suggerimenti concreti che un copywriter o content strategist dovrebbe considerare per migliorare le performance?

Formato dell'output: Utilizza un elenco puntato per ogni sezione (Pattern, Outlier, Azioni).
```
*Fonte: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5 (per la tabella e le descrizioni)*

**Output atteso dall'IA:**

```
**Analisi dei Risultati dell'A/B Test**

*   **Pattern e Tendenze:**
    *   Il "Modello X (Variante)" ha un tasso di conversione del 2.0%, il doppio rispetto al "Controllo (Modello Attuale)" che ha l'1.0%.
    *   La differenza tra i due modelli è statisticamente significativa (p-value di 0.012), indicando che il miglioramento del Modello X non è dovuto al caso.
    *   Entrambi i modelli hanno avuto un numero uguale di utenti assegnati (1500), garantendo una base di confronto equa.
    *   Il Modello X è stato identificato come il vincitore, con entrambi gli errori di Tipo I e Tipo II controllati, il che rafforza l'affidabilità del risultato.

*   **Outlier e Anomalie:**
    *   Il p-value di 0.012 è significativamente inferiore alla soglia comune di 0.05, confermando la forte evidenza a favore del Modello X. Non ci sono anomalie evidenti che invalidino i risultati.

*   **Azioni e Raccomandazioni per Copywriter/Content Strategist:**
    1.  **Adottare il Modello X:** Sostituire immediatamente il "Modello Attuale" con il "Modello X" per tutte le nuove campagne e traffico, dato il suo comprovato doppio tasso di conversione.
    2.  **Analizzare gli elementi del Modello X:** Collaborare con il team di design/sviluppo per identificare gli elementi chiave (headline, CTA, copy, immagini, layout) che hanno contribuito al successo del Modello X.
    3.  **Testare ulteriormente gli elementi vincenti:** Una volta identificati gli elementi di successo del Modello X, creare nuove varianti testando singolarmente questi elementi su altre landing page o campagne per replicarne il successo.
    4.  **Aggiornare le linee guida di copywriting:** Integrare le lezioni apprese dal Modello X nelle linee guida di copywriting dell'agenzia per future creazioni di contenuti e landing page.
    5.  **Monitorare le performance post-implementazione:** Continuare a monitorare il tasso di conversione del Modello X dopo l'implementazione per assicurarsi che mantenga le sue performance nel tempo e identificare eventuali cali.
```
*Fonte: Da integrare (output simulato basato sull'analisi della tabella)*

---

### Limiti e buone pratiche

**Obiettivo:** Comprendere le capacità e i limiti dell'IA nell'analisi dei dati e adottare strategie per ottenere i migliori risultati.

**Limiti:**
*   **L'IA non "capisce" come un umano:** Non ha intuito o esperienza. Si basa solo sui dati che le fornisci. Se i dati sono ambigui o manca contesto, l'analisi potrebbe essere superficiale o errata.
*   **Dipende dalla qualità dell'input:** "Garbage in, garbage out". Se la tua tabella contiene errori, dati mancanti o è formattata male, l'IA farà fatica a fornire un'analisi utile.
*   **Non sostituisce l'analista:** L'IA è un assistente potente, ma non un decisore finale. Le sue raccomandazioni devono essere sempre validate dalla tua esperienza e conoscenza del business.
*   **Limiti di dati sensibili:** Non inserire mai dati personali, riservati o proprietari senza le dovute autorizzazioni e senza aver verificato le policy di sicurezza del tool IA che stai usando.

**Buone pratiche:**
*   **Sii specifico nel prompt:** Più dettagli dai sul tuo obiettivo e sul formato dell'output desiderato, migliori saranno i risultati.
*   **Verifica sempre i risultati:** Non prendere per oro colato l'output dell'IA. Confrontalo con la tua conoscenza e, se possibile, con un esperto o un'altra fonte di dati.
*   **Inizia semplice, poi approfondisci:** Se hai una tabella complessa, inizia con una domanda generale. Una volta ottenuta una panoramica, puoi fare domande più specifiche per approfondire.
*   **Fornisci contesto:** Spiega all'IA il tuo ruolo (es. "Sono un copywriter che cerca spunti per migliorare le CTA") e l'obiettivo generale dell'analisi.
*   **Formato chiaro per l'output:** Chiedi all'IA di presentare i risultati in un formato specifico (es. "elenco puntato", "tabella riassuntiva", "breve paragrafo").

---

### Fonti

*   `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5`

