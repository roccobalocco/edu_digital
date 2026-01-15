# Prompt engineering per rilevamento lingua

Ecco una sezione del manuale d'uso dell'IA per copywriter e content strategist, focalizzata sul rilevamento della lingua.

---

# Rilevamento della Lingua con l'IA

Capire in che lingua è scritto un testo è fondamentale per molte attività in agenzia. L'IA può farlo per te in modo rapido e preciso.

## Quando serve in agenzia

Il rilevamento della lingua è utile in molte situazioni quotidiane:

*   **Gestione dei social media:** Per capire subito in che lingua sono scritti i commenti o i messaggi dei tuoi follower. Questo ti aiuta a rispondere nella lingua giusta o a indirizzare il commento al team appropriato.
*   **Analisi dei contenuti generati dagli utenti (UGC):** Se raccogli recensioni, feedback o post da diverse piattaforme, l'IA può categorizzarli per lingua. Così puoi analizzare il sentiment o le tendenze specifiche per ogni mercato.
*   **Smistamento email:** Se ricevi email da clienti internazionali, l'IA può identificare la lingua e indirizzare il messaggio al team di supporto o al copywriter che parla quella lingua.
*   **Localizzazione dei contenuti:** Prima di tradurre o adattare un contenuto, l'IA può confermare la lingua originale, evitando errori e ottimizzando il processo.
*   **Personalizzazione della comunicazione:** Per assicurarti che il messaggio giusto arrivi al pubblico giusto, nella lingua giusta.

*(Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3, ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1)*

## Prompt template

Per chiedere all'IA di rilevare la lingua, usa un prompt chiaro e diretto. Chiedi di restituire solo il nome della lingua.

**Obiettivo:** Identificare la lingua di un testo.

**Come usarlo:**

```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua (es. "Italiano", "Inglese", "Spagnolo").

Testo:
[INSERISCI QUI IL TESTO DA ANALIZZARE]
```

**Buona pratica:** Se hai un elenco specifico di lingue che ti aspetti, puoi includerle nel prompt per guidare meglio l'IA:

```
Identifica la lingua del seguente testo, scegliendo tra: Italiano, Inglese, Spagnolo, Francese, Tedesco, Cinese.
Rispondi solo con il nome della lingua.

Testo:
[INSERISCI QUI IL TESTO DA ANALIZZARE]
```
*(Fonte: ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk3, ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26)*

## Esempi pratici

Vediamo come applicare il prompt a diversi tipi di contenuti che trovi in agenzia.

### Esempio 1: Commento social

**Scenario:** Un utente ha lasciato un commento sulla pagina Facebook del tuo cliente.

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua.

Testo:
I love this product! It's amazing.
```

**Output dell'IA:**
```
Inglese
```

### Esempio 2: Contenuto generato dagli utenti (UGC)

**Scenario:** Una recensione di un prodotto su un forum internazionale.

**Prompt:**
```
Identifica la lingua del seguente testo, scegliendo tra: Inglese, Spagnolo, Cinese.
Rispondi solo con il nome della lingua.

Testo:
No estoy seguro de lo que pienso sobre este producto.
```

**Output dell'IA:**
```
Spagnolo
```

### Esempio 3: Estratto di email

**Scenario:** Parte del corpo di un'email di supporto clienti.

**Prompt:**
```
Identifica la lingua del seguente testo.
Rispondi solo con il nome della lingua.

Testo:
总体来说，我对这款产品很满意。
```

**Output dell'IA:**
```
Cinese
```
*(Fonte: ../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb::chunk3)*

## Ambiguità e casi misti

L'IA è brava, ma non infallibile, specialmente con testi particolari.

*   **Testi molto brevi:** Frasi di una o due parole possono essere ambigue. "Ciao" potrebbe essere italiano o un saluto informale in altre lingue.
*   **Parole straniere:** Un testo italiano con molte parole inglesi (es. "Ho fatto un meeting e il feedback è stato positivo") verrà probabilmente identificato come italiano, ma l'IA potrebbe notare le influenze.
*   **Code-switching (cambio di codice):** Quando una persona passa da una lingua all'altra all'interno della stessa frase o paragrafo (es. "I love this pasta, è buonissima!"). L'IA cercherà di identificare la lingua predominante o potrebbe segnalare un'incertezza.
*   **Dialetti o lingue meno comuni:** L'IA è addestrata su un'enorme quantità di dati, ma potrebbe avere difficoltà con dialetti molto specifici o lingue con poca rappresentazione online.

**Come gestire:**
*   **Sii specifico:** Se sai che il testo potrebbe essere misto, chiedi all'IA di identificare la lingua *predominante* o di segnalare se il testo contiene *più lingue*.
*   **Opzione "Sconosciuta" o "Mista":** Puoi aggiungere queste opzioni al tuo elenco di lingue nel prompt, per dare all'IA una via d'uscita quando non è sicura.

*(Fonte: ../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb::chunk5 - concetto di "code switching" e gestione delle istruzioni)*

## Limiti e buone pratiche

Per ottenere i migliori risultati e capire quando l'IA potrebbe non essere perfetta:

### Limiti
*   **Precisione:** L'IA è molto precisa per le lingue più diffuse e testi di media lunghezza, ma la precisione può diminuire con testi molto brevi, dialetti rari o gerghi specifici.
*   **Contesto:** L'IA analizza il testo che le dai. Non ha il contesto culturale o la conoscenza del parlante che un umano avrebbe.
*   **"Sicurezza" della risposta:** A volte l'IA potrebbe darti una risposta senza indicare quanto è "sicura". Se la tua piattaforma IA lo permette, puoi chiedere un punteggio di confidenza (anche se è un concetto più tecnico, l'idea è che l'IA ti dica quanto è certa della sua risposta). *(Concetto derivato da ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1, riformulato per non usare gergo tecnico)*

### Buone pratiche
*   **Sii chiaro e conciso nel prompt:** Meno ambiguità, migliori risultati.
*   **Fornisci un elenco di lingue attese:** Se sai quali lingue potresti incontrare, elenca le opzioni nel prompt. Questo restringe il campo e migliora la precisione.
*   **Testa con vari esempi:** Prima di usare l'IA su larga scala, prova con diversi tipi di testo che ti aspetti di incontrare.
*   **Definisci una strategia per i casi ambigui:** Cosa fai se l'IA risponde "Sconosciuta" o "Mista"? Prevedi un controllo manuale o un'altra azione.
*   **Non dare per scontato:** Anche se l'IA è potente, un controllo umano è sempre consigliato per decisioni critiche, soprattutto con testi complessi o ambigui.

*(Fonte: ../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb::chunk26 - concetto di "strict guidelines" ed "few-shot examples" riformulato; ../data/openai-cookbook/examples/Using_logprobs.ipynb::chunk1 - concetto di "confidence" riformulato)*

---

## Fonti

*   `../data/openai-cookbook/examples/evaluation/use-cases/structured-outputs-evaluation.ipynb`
*   `../data/openai-cookbook/examples/Using_logprobs.ipynb`
*   `../data/openai-cookbook/examples/Realtime_prompting_guide.ipynb`
*   `../data/openai-cookbook/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents.ipynb`
