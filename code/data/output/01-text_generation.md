# Prompt engineering per generazione di testi

# Guida all'IA per Copywriter e Content Strategist

## Prompt Engineering per la Generazione di Testi

### 1. Cos'è e quando usarlo

**Obiettivo:** Capire come dare istruzioni efficaci all'IA per ottenere i testi che desideri.

**Cos'è:**
Il "Prompt Engineering" è l'arte di scrivere le istruzioni (i "prompt") per l'intelligenza artificiale in modo chiaro e preciso. Immagina di parlare con un assistente molto intelligente ma che ha bisogno di indicazioni dettagliate per fare un buon lavoro.

**Quando usarlo:**
L'IA è un alleato potente nel tuo lavoro quotidiano. Usala per:
*   **Brainstorming:** Generare idee per titoli, slogan, argomenti.
*   **Bozze rapide:** Creare velocemente prime versioni di testi (post social, email, descrizioni).
*   **Riassunti:** Sintetizzare articoli lunghi o report.
*   **Adattamento:** Riscrivere un testo per un pubblico o un canale diverso.
*   **Espansione:** Sviluppare un'idea o un punto in un testo più lungo.

---
*Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`*

### 2. Checklist per un Prompt Efficace

**Obiettivo:** Costruire prompt completi che guidano l'IA verso il risultato desiderato.

Un buon prompt è come un briefing ben fatto. Deve contenere tutti gli elementi chiave. Pensa a queste domande prima di scrivere:

*   **Ruolo:**
    *   **Chi sei?** Chiedi all'IA di assumere un ruolo specifico. Questo la aiuta a capire il tono e lo stile.
    *   *Esempio:* "Sei un copywriter esperto di marketing digitale."
    *   *Esempio:* "Agisci come un social media manager."

*   **Contesto:**
    *   **Di cosa stiamo parlando?** Fornisci l'argomento principale.
    *   **Per chi?** Specifica il pubblico di riferimento (es. giovani, professionisti, neogenitori).
    *   **Qual è lo scopo?** Vuoi informare, vendere, intrattenere, generare lead?
    *   *Esempio:* "L'argomento è il lancio del nostro nuovo prodotto ecologico, una borraccia riutilizzabile."
    *   *Esempio:* "Il pubblico sono giovani adulti attenti all'ambiente."
    *   *Esempio:* "L'obiettivo è generare interesse e spingere all'acquisto."

*   **Vincoli e Dettagli:**
    *   **Tono:** Che emozione deve trasmettere il testo? (Es. entusiasta, professionale, amichevole, autorevole).
    *   **Lunghezza:** Quante parole, caratteri o paragrafi? Sii specifico.
    *   **Parole chiave:** Ci sono termini che devono essere inclusi?
    *   **Call to Action (CTA):** Cosa deve fare il lettore dopo aver letto il testo?
    *   **Cosa evitare:** Ci sono parole, frasi o argomenti da non usare?
    *   *Esempio:* "Il tono deve essere entusiasta e motivante."
    *   *Esempio:* "Il testo deve avere una lunghezza massima di 150 caratteri."
    *   *Esempio:* "Includi le parole chiave 'sostenibilità' e 'idratazione'."
    *   *Esempio:* "La CTA deve essere 'Acquista ora sul nostro sito!'"
    *   *Esempio:* "Evita un linguaggio troppo tecnico."

*   **Formato:**
    *   **Come deve essere strutturato il risultato?** (Es. un paragrafo, punti elenco, una tabella, un elenco numerato, in formato Markdown).
    *   *Esempio:* "Il risultato deve essere un elenco di 3 punti."
    *   *Esempio:* "Scrivi il testo in un unico paragrafo."

---
*Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`, `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`, `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`, `../data/openai-cookbook/examples/Optimize_Prompts.ipynb`*

### 3. Esempi Pratici per il Tuo Lavoro

**Obiettivo:** Vedere come applicare la checklist a scenari reali.

Ecco alcuni esempi di prompt ben strutturati per diverse esigenze:

#### Esempio 1: Post per Social Media (Instagram)

*   **Prompt:**
    "Sei un social media manager esperto.
    Scrivi un post breve per Instagram che annunci il lancio del nostro nuovo prodotto: l'Eco-Borraccia, realizzata al 100% con materiali riciclati.
    Il pubblico sono giovani adulti attenti all'ambiente.
    Il tono deve essere entusiasta e ispirazionale.
    Includi almeno due hashtag pertinenti.
    La call to action deve invitare a scoprire di più sul nostro sito.
    Lunghezza massima: 180 caratteri.
    Formato: un paragrafo con emoji."

*   **Output Esempio:**
    "È arrivata l'Eco-Borraccia! 🌿 La tua idratazione quotidiana diventa sostenibile con la nostra nuova borraccia 100% riciclata. Fai la tua parte per il pianeta, con stile! ✨ Scopri di più sul nostro sito! #EcoBorraccia #Sostenibilità"

#### Esempio 2: Oggetto per Newsletter

*   **Prompt:**
    "Sei un copywriter specializzato in email marketing.
    Genera 3 idee per l'oggetto di una newsletter che promuove uno sconto del 20% su tutti i prodotti per i nuovi iscritti.
    Il pubblico sono persone che si sono appena iscritte e non hanno ancora acquistato.
    L'obiettivo è spingere all'apertura e al primo acquisto.
    Gli oggetti devono essere accattivanti, chiari sul beneficio e non troppo "spammosi".
    Lunghezza massima per oggetto: 50 caratteri.
    Formato: un elenco numerato."

*   **Output Esempio:**
    "1. Benvenuto! Il tuo sconto del 20% ti aspetta!
    2. Solo per te: -20% sul primo acquisto!
    3. Non perdere il tuo 20% di benvenuto!"

#### Esempio 3: Descrizione Prodotto per Sito E-commerce

*   **Prompt:**
    "Sei un copywriter per un e-commerce di tecnologia.
    Scrivi una descrizione di prodotto per il nostro sito.
    Prodotto: 'Cuffie Wireless SuperSound Pro'.
    Pubblico: amanti della musica e professionisti che cercano qualità audio superiore e comfort.
    Caratteristiche chiave da evidenziare: suono immersivo ad alta fedeltà, cancellazione del rumore attiva, batteria a lunga durata (30 ore), design ergonomico e leggero.
    Il tono deve essere moderno, coinvolgente e professionale.
    Lunghezza: circa 100-120 parole.
    Formato: due paragrafi, con un elenco puntato per le caratteristiche principali."

*   **Output Esempio:**
    "Immergiti in un'esperienza sonora senza precedenti con le Cuffie Wireless SuperSound Pro. Progettate per gli audiofili e i professionisti, offrono una fedeltà audio cristallina e una cancellazione del rumore attiva che ti isola dal mondo esterno, permettendoti di concentrarti sulla tua musica o sulle tue chiamate. Il design ergonomico e leggero assicura un comfort eccezionale anche durante sessioni di ascolto prolungate.

    Con una batteria che dura fino a 30 ore, le SuperSound Pro sono le compagne ideali per le tue giornate più intense. Scopri la libertà del wireless unita a prestazioni audio di altissimo livello.

    *   Suono immersivo ad alta fedeltà
    *   Cancellazione del rumore attiva
    *   Batteria da 30 ore
    *   Design ergonomico e leggero"

---
*Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`, `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`*

### 4. Errori Comuni da Evitare

**Obiettivo:** Riconoscere e correggere le inefficienze nei prompt.

Anche con le migliori intenzioni, è facile cadere in alcune trappole. Ecco gli errori più comuni:

*   **Istruzioni vaghe o ambigue:**
    *   *Errore:* "Scrivi qualcosa di bello sul nostro prodotto." (Cosa significa "bello" per l'IA?)
    *   *Correzione:* Sii specifico su tono, stile, emozioni da evocare.

*   **Contraddizioni nel prompt:**
    *   *Errore:* "Sii molto formale ma usa un linguaggio giovanile e slang." (L'IA non saprà quale indicazione seguire.)
    *   *Correzione:* Rivedi le istruzioni per assicurarti che siano coerenti.

*   **Mancanza di contesto:**
    *   *Errore:* "Scrivi un post." (Per quale piattaforma? Su cosa? Per chi?)
    *   *Correzione:* Includi sempre ruolo, contesto, pubblico e scopo.

*   **Aspettative irrealistiche:**
    *   *Errore:* Chiedere all'IA di creare una campagna marketing completa con immagini e video in un solo prompt.
    *   *Correzione:* Suddividi i compiti complessi in passaggi più piccoli e gestibili.

*   **Non specificare il formato:**
    *   *Errore:* Chiedere "idee per titoli" senza specificare il formato, ottenendo un blocco di testo.
    *   *Correzione:* Indica sempre il formato desiderato (punti elenco, tabella, paragrafo).

*   **Non dare esempi quando serve:**
    *   *Errore:* Chiedere un testo in uno stile molto particolare senza mostrare un riferimento.
    *   *Correzione:* Se hai un esempio di tono o stile, includilo nel prompt.

---
*Fonte: `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`, `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`*

### 5. Limiti e Buone Pratiche

**Obiettivo:** Usare l'IA in modo consapevole, massimizzando i benefici e mitigando i rischi.

#### Limiti dell'IA

Ricorda che l'IA è uno strumento, non un sostituto del copywriter umano. Ha delle limitazioni:

*   **Mancanza di intuizione e creatività profonda:** L'IA elabora dati, non "crea" nel senso umano. Non ha esperienze, emozioni o una vera comprensione culturale.
*   **Può "allucinare":** A volte l'IA inventa fatti, citazioni o informazioni che sembrano plausibili ma sono false. **Verifica sempre l'accuratezza dei contenuti generati.**
*   **Ripetitività:** Se non istruita diversamente, tende a usare frasi e strutture simili, rendendo il testo monotono.
*   **Bias:** L'IA apprende dai dati con cui è stata addestrata. Se questi dati contengono pregiudizi, l'IA potrebbe riprodurli nei suoi output.
*   **Non capisce il "non detto":** Ha bisogno di tutto esplicitato. Non può leggere tra le righe o intuire le tue intenzioni non espresse.
*   **Comportamento variabile:** Modelli diversi o anche piccole modifiche al prompt possono portare a risultati inaspettati.

---
*Fonte: `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`, `../data/openai-cookbook/examples/Whisper_prompting_guide.ipynb`*

#### Buone Pratiche per un Uso Ottimale

Per ottenere il meglio dall'IA, adotta queste abitudini:

*   **Sii specifico e chiaro:** Più dettagli e contesto fornisci, migliore sarà il risultato. Non dare nulla per scontato.
*   **Usa un linguaggio semplice e diretto:** Evita frasi complesse o ambigue nel tuo prompt.
*   **Struttura il tuo prompt:**
    *   Usa punti elenco o sezioni etichettate per organizzare le tue istruzioni.
    *   Puoi usare il MAIUSCOLO per enfatizzare regole chiave.
    *   Converti regole non testuali in testo (es. invece di "SE X > 3 ALLORA ESCALATE", scrivi "SE CI SONO PIÙ DI TRE ERRORI ALLORA SCALA LA SEGNALAZIONE").
*   **Fornisci esempi:** Se vuoi un certo stile, tono o formato, includi un piccolo esempio nel prompt. L'IA è molto brava a seguire i modelli.
*   **Itera e sperimenta:** Non aver paura di modificare il prompt più volte. Anche piccoli cambiamenti nelle parole possono fare una grande differenza nel risultato.
*   **Verifica sempre l'output:** L'IA è un assistente, non un editore finale. Rileggi, modifica e adatta sempre i testi prima di pubblicarli.
*   **Chiedi all'IA di fare domande:** Se l'IA non ha abbastanza informazioni, istruiscila a chiederti chiarimenti.
*   **Controlla la lunghezza:** Specifica sempre il numero di parole o caratteri desiderato per evitare testi troppo lunghi o troppo corti.
*   **Chiedi di variare il linguaggio:** Se noti ripetizioni, aggiungi una regola nel prompt come "Varia il linguaggio per evitare ripetizioni" o "Usa sinonimi per rendere il testo più ricco".
*   **Controlla la lingua di output:** Se lavori in un contesto multilingue, specifica sempre la lingua in cui vuoi il testo.

---
*Fonte: `../data/openai-cookbook/articles/how_to_work_with_large_language_models.md`, `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`, `../data/openai-cookbook/examples/gpt4-1_prompting_guide.ipynb`, `../data/openai-cookbook/examples/gpt-5/gpt-5-2_prompting_guide.ipynb`*
