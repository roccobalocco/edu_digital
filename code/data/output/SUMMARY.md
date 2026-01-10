# Summary

- [Manuale d’Uso](README.md)

- [# Manuale d'Uso dell'IA per Copywriter e Content Strategist

## Prompt Engineering per Generazione di Testi

### 1. Cos'è e quando usarlo

**Obiettivo:** Capire cosa sia il "prompt engineering" e quando usarlo per il tuo lavoro quotidiano.

Il "prompt engineering" è l'arte di dare istruzioni chiare e precise a un'Intelligenza Artificiale per ottenere il testo che desideri. Immagina di essere un regista e l'IA è il tuo attore: più dettagliata è la tua sceneggiatura (il prompt), migliore sarà la performance.

**Quando usarlo:**
L'IA è un assistente potente per:
*   **Generare idee:** Brainstorming di titoli, slogan, concetti per campagne.
*   **Drafting veloce:** Scrivere bozze di post social, email, descrizioni prodotto.
*   **Riformulare testi:** Adattare un contenuto per un pubblico diverso o un tono specifico.
*   **Riassumere:** Estrarre i punti chiave da testi lunghi.
*   **Creare varianti:** Ottenere diverse opzioni per lo stesso messaggio (es. 5 versioni di un copy Instagram).
*   **Migliorare la coerenza:** Mantenere uno stile o un tono uniforme su più pezzi di contenuto.

In pratica, ogni volta che hai bisogno di testo e vuoi accelerare il processo creativo o ottenere nuove prospettive, il prompt engineering è il tuo strumento.

### 2. Checklist prompt: Ruolo, Contesto, Obiettivo, Vincoli, Formato

**Obiettivo:** Imparare a costruire un prompt efficace, passo dopo passo, per guidare l'IA al meglio.

Un buon prompt è come un briefing ben fatto. Deve essere chiaro, completo e strutturato. Ecco gli elementi chiave da includere:

*   **1. Ruolo:**
    *   **Cosa:** Chiedi all'IA di "vestire i panni" di una figura specifica. Questo la aiuta a capire la prospettiva e il tono.
    *   **Come:** Inizia con frasi come: "Agisci come un copywriter esperto di marketing digitale...", "Sei un social media manager...", "Immagina di essere un giornalista specializzato in tecnologia...".
    *   **Esempio:** `Agisci come un copywriter esperto di e-commerce.`

*   **2. Contesto:**
    *   **Cosa:** Descrivi la situazione o lo scenario in cui si inserisce il testo.
    *   **Come:** Spiega il prodotto/servizio, il pubblico di riferimento, l'occasione (es. lancio, promozione, articolo di blog).
    *   **Esempio:** `Stiamo lanciando un nuovo paio di scarpe da corsa leggere e ammortizzate, pensate per runner amatoriali che cercano comfort e prestazioni.`

*   **3. Obiettivo:**
    *   **Cosa:** Indica chiaramente cosa vuoi che l'IA produca.
    *   **Come:** Sii specifico: "Genera 3 idee per post Instagram...", "Scrivi un oggetto e un'anteprima per una newsletter...", "Crea una meta description per questa pagina...".
    *   **Esempio:** `Genera 3 idee per post Instagram per il lancio di queste scarpe.`

*   **4. Vincoli:**
    *   **Cosa:** Specifica le regole e i limiti che l'IA deve rispettare. Questi sono fondamentali per un output di qualità.
    *   **Come:**
        *   **Lunghezza:** "Massimo 150 caratteri", "circa 100 parole".
        *   **Tono:** "Tono amichevole e motivante", "professionale ma accessibile", "ironico".
        *   **Parole chiave:** "Includi le parole chiave 'comfort', 'leggerezza', 'ammortizzazione'".
        *   **Pubblico:** "Rivolgiti a un pubblico giovane e attivo".
        *   **Cosa evitare:** "Non usare gergo tecnico", "evita frasi troppo lunghe".
    *   **Esempio:** `Ogni post deve avere un tono motivante e includere un invito all'azione. Usa gli hashtag #NuoveScarpe #Corsa #Comfort. La lunghezza massima per ogni copy è di 200 caratteri. Non usare emoji.`

*   **5. Formato:**
    *   **Cosa:** Indica come deve essere organizzato l'output.
    *   **Come:** "Elenco puntato", "formato Markdown", "solo il testo del post, senza introduzioni o commenti", "tabella".
    *   **Esempio:** `Restituisci i 3 post in un elenco numerato, con il copy e gli hashtag separati.`

*   **6. Esempi (se utile):**
    *   **Cosa:** A volte, mostrare all'IA un esempio di ciò che cerchi può essere più efficace di mille parole.
    *   **Come:** Includi un piccolo esempio di stile, struttura o contenuto desiderato.
    *   **Esempio:** `Ecco un esempio di stile che mi piace: "Senti il vento tra i capelli e la libertà ai tuoi piedi. Le nostre nuove scarpe ti portano oltre ogni limite!"`

**Ricorda:** Organizza il tuo prompt in sezioni chiare (anche con titoli come "RUOLO:", "CONTESTO:", ecc.) per renderlo più leggibile per l'IA e per te stesso. Le istruzioni più importanti possono essere evidenziate, magari in maiuscolo.
*(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*
*(Fonte: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*

### 3. Esempi pratici per social, newsletter, sito

**Obiettivo:** Vedere come applicare la checklist a scenari reali di agenzia.

#### Esempio 1: Post Instagram per lancio prodotto

**Prompt:**
```
RUOLO: Agisci come un copywriter esperto di social media.

CONTESTO: Stiamo lanciando una nuova linea di snack proteici vegani, "GreenBoost", pensati per sportivi e persone attente alla dieta che cercano uno spuntino sano e gustoso.

OBIETTIVO: Genera 3 idee per post Instagram per il lancio.

VINCOLI:
- Tono: energico, positivo, inclusivo.
- Ogni post deve includere un invito all'azione chiaro (es. "Scopri di più", "Provali ora").
- Includi gli hashtag: #GreenBoost #SnackVegano #ProteineVegetali #VitaSana.
- Lunghezza massima per ogni copy: 220 caratteri.
- Non usare emoji.

FORMATO: Restituisci i 3 post in un elenco numerato. Per ogni post, indica prima il copy e poi gli hashtag.
```

**Output (esempio):**
1.  **Copy:** Energia pulita per le tue giornate! I nuovi snack GreenBoost sono qui per darti la carica con gusto e ingredienti 100% vegetali. Provali ora e senti la differenza!
    **Hashtag:** #GreenBoost #SnackVegano #ProteineVegetali #VitaSana
2.  **Copy:** Il tuo allenamento merita il meglio. Con GreenBoost, hai lo spuntino proteico vegano perfetto per recuperare e ripartire. Non aspettare, scopri tutta la linea!
    **Hashtag:** #GreenBoost #SnackVegano #ProteineVegetali #VitaSana
3.  **Copy:** Sano, gustoso, vegano. GreenBoost è lo snack che stavi aspettando per nutrire il tuo corpo con il potere delle piante. Clicca sul link in bio per acquistarli!
    **Hashtag:** #GreenBoost #SnackVegano #ProteineVegetali #VitaSana

#### Esempio 2: Oggetto e anteprima per Newsletter

**Prompt:**
```
RUOLO: Sei un esperto di email marketing.

CONTESTO: Dobbiamo inviare una newsletter ai nostri clienti per promuovere una vendita flash del 30% su tutti i prodotti per la casa intelligente (lampadine, termostati, assistenti vocali). La vendita dura solo 48 ore.

OBIETTIVO: Crea 5 opzioni di oggetto e testo di anteprima (preheader) per la newsletter.

VINCOLI:
- Tono: urgente, vantaggioso, entusiasmante.
- L'oggetto deve essere accattivante e far capire l'urgenza.
- L'anteprima deve completare l'oggetto e invogliare all'apertura.
- Lunghezza oggetto: massimo 50 caratteri.
- Lunghezza anteprima: massimo 75 caratteri.
- Includi il riferimento al "30% di sconto" e "48 ore".

FORMATO: Presenta le 5 opzioni in un elenco puntato, con "Oggetto:" e "Anteprima:" per ogni opzione.
```

**Output (esempio):**
*   **Oggetto:** ⚡️ Vendita Flash: -30% su Smart Home!
    **Anteprima:** Solo 48 ore per trasformare la tua casa. Non perdere il 30% di sconto!
*   **Oggetto:** La tua casa intelligente al -30% (solo 48h)
    **Anteprima:** Affrettati! Sconti incredibili su lampadine, termostati e altro.
*   **Oggetto:** Ultima Chance: 30% Off Smart Home!
    **Anteprima:** La nostra vendita lampo finisce presto. Cogli l'occasione entro 48 ore!
*   **Oggetto:** Casa Smart: -30% per 48 Ore!
    **Anteprima:** Non sognare, agisci! Sconti imperdibili ti aspettano.
*   **Oggetto:** Sconto 30% Smart Home: Solo 2 Giorni!
    **Anteprima:** Upgrade la tua casa con offerte che non dureranno.

#### Esempio 3: Descrizione prodotto e Meta Description per Sito Web

**Prompt:**
```
RUOLO: Agisci come un copywriter SEO specializzato in descrizioni di prodotti.

CONTESTO: Devi scrivere una descrizione prodotto e una meta description per una nuova tazza termica riutilizzabile, "ThermoMug Pro", ideale per bevande calde e fredde, realizzata in acciaio inossidabile, con design elegante e chiusura ermetica.

OBIETTIVO: Genera:
1.  Una descrizione prodotto persuasiva (circa 150 parole).
2.  Una meta description ottimizzata per SEO (massimo 160 caratteri).

VINCOLI:
- Tono: pratico, ecologico, di alta qualità.
- Descrizione prodotto: Evidenzia i benefici (mantiene caldo/freddo, riutilizzabile, design, ermetica). Includi le parole chiave "tazza termica", "acciaio inossidabile", "bevande calde e fredde", "riutilizzabile".
- Meta Description: Deve essere concisa, includere le parole chiave principali e un invito all'azione implicito.

FORMATO: Presenta prima la descrizione prodotto e poi la meta description, chiaramente etichettate.
```

**Output (esempio):**
**Descrizione Prodotto:**
La ThermoMug Pro è la compagna ideale per le tue giornate, perfetta per chi non rinuncia al comfort e allo stile. Realizzata in robusto **acciaio inossidabile** di alta qualità, questa **tazza termica** avanzata mantiene le tue **bevande calde e fredde** alla temperatura perfetta per ore. Dimentica tazze usa e getta: con ThermoMug Pro scegli la sostenibilità. Il suo design elegante si adatta a ogni contesto, dalla scrivania all'avventura. Grazie alla chiusura ermetica, puoi portarla con te senza preoccupazioni di perdite. È la soluzione **riutilizzabile** definitiva per caffè, tè, acqua o frullati. Scegli ThermoMug Pro e goditi ogni sorso, ovunque tu sia.

**Meta Description:**
Tazza termica ThermoMug Pro in acciaio inossidabile: mantiene bevande calde e fredde per ore. Design elegante, riutilizzabile e 100% ermetica. Scopri la qualità!

### 4. Errori comuni

**Obiettivo:** Riconoscere e evitare gli errori più frequenti nell'uso dell'IA per la generazione di testi.

Anche l'IA più avanzata può darti risultati deludenti se non la guidi correttamente. Ecco gli errori da evitare:

*   **1. Istruzioni vaghe o ambigue:**
    *   **Errore:** "Scrivi qualcosa sul nostro nuovo prodotto."
    *   **Perché è un errore:** L'IA non sa cosa "qualcosa" significhi. Non ha contesto, tono o obiettivo.
    *   **Soluzione:** Sii sempre specifico su cosa vuoi, per chi, con quale tono e perché.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **2. Non specificare formato o lunghezza:**
    *   **Errore:** Chiedere un "post" senza dire se è per Facebook, Instagram, LinkedIn, o quanti caratteri.
    *   **Perché è un errore:** L'IA potrebbe generare un testo troppo lungo, troppo corto, o in un formato inutilizzabile.
    *   **Soluzione:** Indica sempre il formato (elenco, paragrafo, Markdown) e i limiti di lunghezza (caratteri, parole).
    *(Fonte: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*

*   **3. Non dare un ruolo all'IA:**
    *   **Errore:** Chiedere "Scrivi un testo di vendita."
    *   **Perché è un errore:** L'IA non sa se deve essere un venditore aggressivo, un consulente amichevole o un esperto tecnico.
    *   **Soluzione:** Assegna un ruolo specifico (es. "Agisci come un copywriter esperto di vendita B2B").

*   **4. Aspettarsi che l'IA "sappia" o "capisca" tutto (Allucinazioni):**
    *   **Errore:** Dare per scontato che l'IA conosca dettagli specifici del tuo brand, dati recenti o eventi non ampiamente pubblicati.
    *   **Perché è un errore:** L'IA può "allucinare", ovvero inventare fatti, dati o citazioni che sembrano veri ma non lo sono, se non ha abbastanza informazioni o se le istruzioni sono troppo generiche.
    *   **Soluzione:** Fornisci sempre le informazioni chiave e verifica sempre l'accuratezza dei fatti generati. Se l'IA non ha abbastanza informazioni per una richiesta, istruiscila a chiedere chiarimenti.
    *(Fonte: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*

*   **5. Non chiedere varietà (output ripetitivo):**
    *   **Errore:** Chiedere "Scrivi 5 slogan per il prodotto X" senza specificare che devono essere diversi.
    *   **Perché è un errore:** L'IA potrebbe generare slogan molto simili tra loro, o usare le stesse frasi.
    *   **Soluzione:** Includi sempre istruzioni come "Genera 5 varianti diverse", "Usa un linguaggio vario e creativo", "Evita ripetizioni".
    *(Fonte: ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb::chunk9)*
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **6. Istruzioni contraddittorie:**
    *   **Errore:** Chiedere un testo "formale" ma anche "giovanile e slang".
    *   **Perché è un errore:** L'IA si confonde e l'output sarà di scarsa qualità o incoerente.
    *   **Soluzione:** Rileggi il prompt per assicurarti che tutte le istruzioni siano allineate e non si contraddicano.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

### 5. Limiti e buone pratiche

**Obiettivo:** Comprendere le capacità e i confini dell'IA e adottare le migliori strategie per massimizzarne l'efficacia.

#### Limiti dell'IA

*   **Non è un essere umano:** L'IA non ha intuito, empatia reale, esperienza di vita o capacità di comprendere il sarcasmo o le sfumature culturali implicite come un umano. Genera testo basandosi su schemi appresi.
*   **Può inventare fatti (allucinazioni):** Come menzionato, se non ha dati sufficienti o se le viene chiesto di speculare, l'IA può generare informazioni false ma plausibili. **Verifica sempre ogni dato o affermazione.**
*   **Non capisce il contesto implicito:** Ha bisogno di tutto esplicitamente. Ciò che per noi è ovvio, per l'IA non lo è.
*   **Non tutte le IA funzionano allo stesso modo:** Alcuni modelli AI (come quelli per la trascrizione audio) potrebbero seguire lo "stile" di un esempio più che le istruzioni dirette. Per la generazione di testo, i modelli più recenti sono molto bravi a seguire le istruzioni, ma è bene sapere che le tecnologie AI possono avere comportamenti diversi.
    *(Fonte: ../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0)*
*   **Ha limiti di lunghezza:** Ogni IA può elaborare solo una certa quantità di testo alla volta (il tuo prompt più la risposta). Se il prompt è troppo lungo, potrebbe ignorare le parti iniziali. Sii conciso ma completo.
    *(Fonte: ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md::chunk1)*
    *(Fonte: ../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb::chunk0)*

#### Buone pratiche

*   **1. Iterare senza sosta:**
    *   **Cosa:** Non aspettarti il risultato perfetto al primo tentativo. Modifica il prompt, aggiungi dettagli, prova diverse formulazioni. Piccole modifiche possono fare una grande differenza.
    *   **Come:** Prendi l'output, analizza cosa non va e modifica il prompt di conseguenza.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **2. Sii preciso e specifico:**
    *   **Cosa:** Ogni parola conta. Evita ambiguità. Più dettagli fornisci, più l'output sarà allineato alle tue aspettative.
    *   **Come:** Invece di "Scrivi un testo bello", prova "Scrivi un testo persuasivo, con tono entusiasta, che evidenzi i benefici X, Y, Z per il pubblico A".
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **3. Guida con esempi:**
    *   **Cosa:** Se hai in mente uno stile o un formato particolare, mostra all'IA un esempio.
    *   **Come:** Includi nel prompt "Ecco un esempio di tono che mi piace: '...'". L'IA è brava a replicare pattern.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **4. Struttura il prompt:**
    *   **Cosa:** Organizza il tuo prompt in sezioni chiare e facili da leggere.
    *   **Come:** Usa punti elenco, titoli in maiuscolo (es. "RUOLO:", "CONTESTO:", "OBIETTIVO:") per rendere le istruzioni più evidenti. Questo aiuta l'IA a elaborare le informazioni in modo più coerente.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **5. Chiedi varietà:**
    *   **Cosa:** Per evitare output ripetitivi, chiedi esplicitamente all'IA di variare il linguaggio.
    *   **Come:** Aggiungi una regola come "Assicurati che le frasi siano diverse e non ripetitive" o "Genera 3 opzioni con stili leggermente diversi".
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **6. Controlla sempre l'output:**
    *   **Cosa:** L'IA è un assistente, non un sostituto. Ogni testo generato deve essere revisionato, corretto e adattato da te.
    *   **Come:** Leggi criticamente, verifica i fatti, adatta il tono e lo stile per renderlo autentico e in linea con il tuo brand.

*   **7. Usa il maiuscolo per enfasi:**
    *   **Cosa:** Per le regole o le istruzioni più importanti, usa il maiuscolo.
    *   **Come:** "NON INCLUDERE PREZZI NEL COPY", "LUNGHEZZA MASSIMA 150 CARATTERI". Questo le rende più visibili all'IA.
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

*   **8. Converti regole non testuali in testo:**
    *   **Cosa:** Se hai una regola logica o numerica, esprimila in parole.
    *   **Come:** Invece di "SE X > 3 ALLORA ESCALA", scrivi "SE CI SONO PIÙ DI TRE ERRORI, ALLORA SEGNALA IL PROBLEMA".
    *(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk1)*

---

### Fonti

*   ../data/openai-cookbook/articles/how_to_work_with_large_language_models.md
*   ../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb
*   ../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb
*   ../data/openai-cookbook/examples/Optimize_Prompts.ipynb
*   ../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb
*   ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb](01-text_generation.md)
- [# Rilevamento Lingua con l'IA

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
*   `../data/openai-cookbook/examples/o1/Using_chained_calls_for_o1_structured_outputs.ipynb`](02-language_detection.md)
- [# Analisi Dati Tabellari con l'IA: Trovare Insight per Contenuti e Campagne

Questa sezione ti guiderà su come usare l'Intelligenza Artificiale per analizzare tabelle di dati, scoprendo trend, anomalie e suggerimenti utili per le tue strategie di contenuto e campagne.

---

### Obiettivo

Usare l'IA per interpretare rapidamente dati tabellari complessi, identificare pattern, outlier e ricevere suggerimenti azionabili per ottimizzare le performance di contenuti e campagne.

---

### Quando serve (Esempio: keyword x canale x conversioni)

Immagina di avere una tabella con i risultati delle tue campagne digitali: quali keyword funzionano meglio su quale canale, o quali tipi di contenuto generano più conversioni. L'IA può aiutarti a:

*   **Valutare le performance:** Hai lanciato un test A/B su due versioni di una landing page o due modelli di annunci? L'IA può analizzare i tassi di conversione e dirti quale ha performato meglio e se la differenza è significativa.
    *   *Esempio pratico da agenzia:* Stai confrontando due modelli di annunci (Controllo vs. Modello X) per un cliente. Hai dati su utenti assegnati, conversioni e tassi di conversione. L'IA può aiutarti a capire se il Modello X è un vincitore statisticamente significativo.
    *   Fonte: `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5`
*   **Identificare trend e pattern:** Scoprire quali combinazioni di keyword e canali portano i migliori risultati, o quali tipi di contenuto risuonano di più con specifici segmenti di pubblico.
*   **Rilevare anomalie:** Notare cali improvvisi nelle conversioni o picchi inaspettati che potrebbero indicare problemi o opportunità.
*   **Ottenere suggerimenti:** Ricevere idee su come migliorare i tuoi contenuti o la strategia di distribuzione basandosi sui dati.

---

### Come descrivere la tabella al modello

Per ottenere il meglio dall'IA, devi descrivere la tua tabella in modo chiaro e completo.

1.  **Fornisci la tabella:** Incolla i dati direttamente nel prompt. Puoi usare un formato Markdown per chiarezza.
2.  **Spiega le colonne:** Descrivi brevemente cosa rappresenta ogni colonna. Questo aiuta l'IA a capire il contesto.
3.  **Indica l'obiettivo:** Dì all'IA cosa vuoi scoprire o analizzare.

**Esempio di descrizione:**

"Ecco una tabella che mostra i risultati di un test A/B per due modelli di annunci (Controllo e Modello X) su una piattaforma di pagamento. Voglio capire quale modello ha performato meglio e perché."

```markdown
| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|-----------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                   | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                   | Yes                    |
```

*   **Users Assigned:** Numero di utenti assegnati casualmente a ciascun gruppo.
*   **Conversions:** Quanti utenti hanno completato l'azione desiderata (es. pagato via Stripe).
*   **Conversion Rate:** Tasso di conversione (Conversioni / Utenti Assegnati).
*   **p-value:** Valore statistico che indica se la differenza è probabilmente non casuale.
*   **Stat. Significant?:** Indica se il p-value è inferiore alla soglia di significatività (es. 0.05).
*   **Winner?:** Indica se il Modello X è il vincitore.
*   **Type I Error Guarded?:** Indica se il rischio di falso positivo è sotto controllo.
*   **Type II Error Guarded?:** Indica se la dimensione del campione è sufficiente a rilevare un effetto reale.

Fonte: `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5`

---

### Prompt template (pattern, outlier, azioni)

Ecco un template che puoi adattare per analizzare i tuoi dati tabellari.

**Prompt generico:**

```
Analizza la seguente tabella di dati.
[INCOLLA QUI LA TUA TABELLA IN FORMATO MARKDOWN]

[INCOLLA QUI LA DESCRIZIONE DELLE COLONNE E IL CONTESTO, COME NELL'ESEMPIO PRECEDENTE]

Basandoti su questi dati:
1.  Quali sono i principali pattern o trend che emergono?
2.  Ci sono anomalie o dati che si discostano significativamente dalla norma?
3.  Quali azioni concrete potrei intraprendere per migliorare le performance, basandomi su queste osservazioni?
4.  Quali sono le conclusioni chiave che dovrei comunicare al mio team o al cliente?
```

---

### Esempio con tabella piccola

Usiamo l'esempio del test A/B per i modelli di annunci.

**Il tuo prompt:**

```
Analizza la seguente tabella di dati che mostra i risultati di un test A/B per due modelli di annunci (Controllo e Modello X) su una piattaforma di pagamento.

| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|--------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                | Yes                    |

- **Users Assigned:** Numero di utenti assegnati casualmente a ciascun gruppo.
- **Conversions:** Quanti utenti hanno completato l'azione desiderata (es. pagato via Stripe).
- **Conversion Rate:** Tasso di conversione (Conversioni / Utenti Assegnati).
- **p-value:** Valore statistico che indica se la differenza è probabilmente non casuale.
- **Stat. Significant?:** Indica se il p-value è inferiore alla soglia di significatività (es. 0.05).
- **Winner?:** Indica se il Modello X è il vincitore.
- **Type I Error Guarded?:** Indica se il rischio di falso positivo è sotto controllo.
- **Type II Error Guarded?:** Indica se la dimensione del campione è sufficiente a rilevare un effetto reale.

Basandoti su questi dati:
1.  Quali sono i principali pattern o trend che emergono?
2.  Ci sono anomalie o dati che si discostano significativamente dalla norma?
3.  Quali azioni concrete potrei intraprendere per migliorare le performance, basandomi su queste osservazioni?
4.  Quali sono le conclusioni chiave che dovrei comunicare al mio team o al cliente?
```

**Risposta (ipotetica) dell'IA:**

```
Ecco l'analisi dei dati forniti:

1.  **Pattern o trend principali:**
    *   Il "Modello X (Variant)" ha un tasso di conversione doppio (2.0%) rispetto al "Control (Current Model)" (1.0%).
    *   La differenza nel tasso di conversione è statisticamente significativa (p-value = 0.012), il che significa che è improbabile che sia dovuta al caso.
    *   Il Modello X è stato identificato come il "Winner".
    *   Entrambi i test sono stati condotti con attenzione agli errori di Tipo I (falsi positivi) e Tipo II (falsi negativi), garantendo l'affidabilità dei risultati.

2.  **Anomalie o dati che si discostano:**
    *   Non ci sono anomalie evidenti o dati che si discostano dalla norma, ma piuttosto una chiara differenza di performance tra i due gruppi, che è l'obiettivo del test A/B.

3.  **Azioni concrete suggerite:**
    *   **Implementare il Modello X:** Dato che il Modello X è un vincitore statisticamente significativo e ha raddoppiato il tasso di conversione, dovrebbe essere implementato come nuovo standard.
    *   **Analizzare le differenze:** Studiare cosa rende il Modello X più efficace (es. copy, visual, CTA) per replicare questi elementi in future campagne.
    *   **Test continui:** Continuare a testare nuove varianti per cercare ulteriori miglioramenti, usando il Modello X come nuovo "controllo".

4.  **Conclusioni chiave da comunicare:**
    *   Abbiamo identificato un nuovo modello di annuncio (Modello X) che raddoppia il tasso di conversione rispetto al modello attuale.
    *   I risultati sono statisticamente significativi e affidabili.
    *   Raccomandiamo l'implementazione immediata del Modello X per migliorare le performance complessive.
```
Fonte: `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5` (per la tabella e le descrizioni)

---

### Limiti e buone pratiche

L'IA è un potente alleato, ma ha i suoi limiti.

**Limiti:**

*   **Non è un esperto di business:** L'IA non conosce il contesto specifico della tua agenzia o del tuo cliente. Le sue raccomandazioni sono basate solo sui dati forniti.
*   **Complessità statistica:** Sebbene possa interpretare valori come il "p-value", l'IA non è un sostituto per un'analisi statistica approfondita da parte di un esperto, specialmente per set di dati molto grandi o complessi.
*   **Qualità dei dati:** "Garbage in, garbage out." Se i dati che fornisci sono errati o incompleti, anche l'analisi dell'IA lo sarà.
    *   L'IA può aiutare a identificare problemi nei dati (come menzionato in `../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb::chunk3`), ma la responsabilità della pulizia iniziale è tua.
*   **Interpretazione:** L'IA può presentare i fatti, ma l'interpretazione strategica e la decisione finale spettano sempre a te.

**Buone pratiche:**

*   **Sii specifico:** Più dettagli fornisci sul contesto e sui tuoi obiettivi, migliore sarà l'analisi dell'IA.
*   **Verifica sempre:** Le risposte dell'IA sono un ottimo punto di partenza, ma verifica sempre le conclusioni e i suggerimenti con la tua conoscenza del settore e del cliente.
*   **Formato chiaro:** Usa formati leggibili come Markdown per le tabelle.
*   **Itera:** Se la prima risposta non è soddisfacente, riformula il prompt, aggiungi più contesto o chiedi all'IA di approfondire aspetti specifici.
*   **Pensa in modo critico:** Non accettare ciecamente ogni suggerimento. Usa l'IA come un "secondo cervello" per stimolare la tua analisi, non per sostituirla.

---

### Fonti

*   `../data/openai-cookbook/examples/completions_usage_api.ipynb`
*   `../data/openai-cookbook/examples/o1/Using_reasoning_for_data_validation.ipynb`
*   `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb`
*   `../data/openai-cookbook/examples/vector_databases/kusto/Getting_started_with_kusto_and_openai_embeddings.ipynb`
*   `../data/openai-cookbook/examples/Semantic_text_search_using_embeddings.ipynb`
*   `../data/openai-cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/prompts/code_interpreter.md`](03-cross_tabular_analysis.md)
