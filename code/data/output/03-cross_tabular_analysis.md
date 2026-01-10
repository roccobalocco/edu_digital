# Prompt engineering per cross-tabular analysis

# Analisi Dati Tabellari con l'IA: Trovare Insight per Contenuti e Campagne

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
*   `../data/openai-cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/prompts/code_interpreter.md`
