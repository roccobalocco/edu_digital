# Prompt engineering per cross-tabular analysis

# Analisi Dati Tabellari con l'IA: Trovare Pattern e Azioni

Questo capitolo ti guiderà nell'uso dell'Intelligenza Artificiale per analizzare dati organizzati in tabelle. Imparerai a estrarre insight, identificare tendenze e ricevere suggerimenti pratici per le tue strategie di contenuto e marketing.

---

### Obiettivo

Usare l'IA per esaminare dati strutturati (come tabelle di Excel o fogli Google) e ottenere analisi rapide su:
*   **Pattern:** Cosa sta succedendo? Ci sono tendenze evidenti?
*   **Outlier:** Ci sono valori anomali o inaspettati?
*   **Azioni:** Cosa possiamo fare con queste informazioni?

---

### Quando serve (keyword x canale x conversioni)

Hai una tabella con i risultati delle tue campagne? L'IA può aiutarti a capirli meglio quando:

*   **Analizzi le performance delle keyword:** Vuoi sapere quali parole chiave portano più conversioni su un certo canale?
*   **Valuti l'efficacia dei canali:** Quali canali (es. Social, SEO, Email) generano il miglior tasso di conversione per un prodotto specifico?
*   **Confronti i risultati di A/B test:** Hai lanciato due versioni di una landing page e vuoi capire quale ha performato meglio e perché.
*   **Identifichi problemi o opportunità:** Noti un calo improvviso nelle iscrizioni o un picco inaspettato di traffico da una fonte insolita? L'IA può aiutarti a investigare.
*   **Hai bisogno di un riassunto rapido:** Invece di passare ore a spulciare numeri, chiedi all'IA di darti i punti chiave e le raccomandazioni.

---

### Come descrivere la tabella al modello

L'IA non "vede" la tua tabella come faresti tu. Devi fornirle i dati in un formato che possa leggere e interpretare facilmente. Il modo migliore è copiarla e incollarla direttamente nel prompt, usando un formato chiaro come una tabella Markdown o un testo delimitato.

**Consigli pratici:**

1.  **Includi le intestazioni:** Assicurati che ogni colonna abbia un nome chiaro e descrittivo.
2.  **Mantieni il formato pulito:** Evita celle unite, formattazioni complesse o note a piè di pagina.
3.  **Spiega le colonne (se necessario):** Se i nomi delle colonne non sono autoesplicativi, aggiungi una breve descrizione.

**Esempio di formato ideale:**

```
| Colonna A | Colonna B | Colonna C |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
```
*(Riferimento: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5)*

---

### Prompt template (pattern, outlier, azioni)

Ecco un modello di prompt che puoi adattare. Ricorda di essere specifico su cosa vuoi che l'IA analizzi e su quale tipo di output ti aspetti.

**Struttura del Prompt:**

```
Sei un analista di marketing esperto. Analizza la seguente tabella di dati.

[INCOLLA QUI LA TUA TABELLA DI DATI]

Ecco la descrizione delle colonne:
- [Nome Colonna 1]: [Breve descrizione della colonna 1]
- [Nome Colonna 2]: [Breve descrizione della colonna 2]
- ...

Il mio obiettivo è [SPECIFICA IL TUO OBIETTIVO, es: "capire le performance di conversione dei diversi modelli di campagna"].

Basandoti su questi dati, rispondi a queste domande:
1.  **Pattern/Tendenze:** Quali sono i principali pattern o tendenze che emergono dai dati?
2.  **Outlier/Anomalie:** Ci sono valori o comportamenti anomali che meritano attenzione?
3.  **Azioni/Raccomandazioni:** Quali azioni concrete mi suggerisci di intraprendere per migliorare i risultati, basandoti su queste osservazioni? Sii specifico e orientato al marketing digitale.
```

---

### Esempio con tabella piccola

Immagina di aver condotto un A/B test su due modelli di pagina di checkout (Controllo e Modello X) per un pagamento via Stripe.

**Tabella di input (da copiare nel prompt):**

```
| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|-----------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                   | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                   | Yes                    |
```
*(Riferimento: ../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5)*

**Descrizione delle colonne (da includere nel prompt):**

*   **Group:** Il gruppo di utenti (Controllo o Modello X).
*   **Users Assigned:** Numero di utenti assegnati casualmente a ciascun gruppo.
*   **Conversions:** Quanti utenti hanno completato il pagamento via Stripe in ciascun gruppo.
*   **Conversion Rate:** Tasso di conversione (Conversioni / Utenti Assegnati).
*   **p-value:** Il risultato del test statistico, indica se la differenza è probabilmente dovuta al caso.
*   **Stat. Significant?:** Indica se il p-value è inferiore alla soglia di significatività (es. 0.05).
*   **Winner?:** Indica se il Modello X è il vincitore statisticamente significativo.
*   **Type I Error Guarded?:** Indica se il rischio di falso positivo è stato mantenuto sotto controllo.
*   **Type II Error Guarded?:** Indica se la dimensione del campione era sufficiente per rilevare un effetto reale.

**Prompt di esempio:**

```
Sei un analista di marketing esperto. Analizza la seguente tabella di dati.

| Group                      | Users Assigned | Conversions | Conversion Rate | p-value | Stat. Significant? | Winner? | Type I Error Guarded? | Type II Error Guarded? |
|----------------------------|----------------|-------------|-----------------|---------|--------------------|---------|-----------------------|------------------------|
| Control (Current Model)    | 1500           | 15          | 1.0%            | --      | Reference          | No      | Yes                   | Yes                    |
| Model X (Variant)          | 1500           | 30          | 2.0%            | 0.012   | Yes                | Yes     | Yes                   | Yes                    |

Ecco la descrizione delle colonne:
- Group: Il gruppo di utenti (Controllo o Modello X).
- Users Assigned: Numero di utenti assegnati casualmente a ciascun gruppo.
- Conversions: Quanti utenti hanno completato il pagamento via Stripe in ciascun gruppo.
- Conversion Rate: Tasso di conversione (Conversioni / Utenti Assegnati).
- p-value: Il risultato del test statistico, indica se la differenza è probabilmente dovuta al caso.
- Stat. Significant?: Indica se il p-value è inferiore alla soglia di significatività (es. 0.05).
- Winner?: Indica se il Modello X è il vincitore statisticamente significativo.
- Type I Error Guarded?: Indica se il rischio di falso positivo è stato mantenuto sotto controllo.
- Type II Error Guarded?: Indica se la dimensione del campione era sufficiente per rilevare un effetto reale.

Il mio obiettivo è capire le performance di conversione dei due modelli di checkout e decidere quale adottare.

Basandoti su questi dati, rispondi a queste domande:
1.  **Pattern/Tendenze:** Quali sono i principali pattern o tendenze che emergono dai dati?
2.  **Outlier/Anomalie:** Ci sono valori o comportamenti anomali che meritano attenzione?
3.  **Azioni/Raccomandazioni:** Quali azioni concrete mi suggerisci di intraprendere per migliorare i risultati, basandoti su queste osservazioni? Sii specifico e orientato al marketing digitale.
```

**Esempio di Output IA (ipotetico):**

1.  **Pattern/Tendenze:**
    *   Il "Modello X (Variant)" ha un tasso di conversione doppio (2.0%) rispetto al "Control (Current Model)" (1.0%).
    *   Questa differenza è statisticamente significativa (p-value di 0.012), il che significa che è molto improbabile che sia dovuta al caso.
    *   Entrambi i test sono stati condotti con sufficiente cautela riguardo agli errori di Tipo I e Tipo II.

2.  **Outlier/Anomalie:**
    *   Non ci sono outlier evidenti o anomalie negative in questa piccola tabella. Il Modello X si distingue positivamente.

3.  **Azioni/Raccomandazioni:**
    *   **Adotta il Modello X:** Dato che il Modello X ha dimostrato un aumento significativo del tasso di conversione, dovresti implementarlo come nuovo standard per il checkout.
    *   **Analizza le differenze:** Cerca di capire *cosa* ha reso il Modello X più efficace. Era il design, il copy, la facilità d'uso? Queste intuizioni possono essere applicate ad altre aree del tuo sito.
    *   **Monitora le performance:** Dopo l'implementazione, continua a monitorare il tasso di conversione del Modello X per assicurarti che mantenga le sue performance nel tempo.
    *   **Pensa al prossimo test:** Ora che hai un nuovo "Controllo", inizia a ideare e testare nuove varianti per migliorare ulteriormente il tasso di conversione.

---

### Limiti e buone pratiche

L'IA è un ottimo strumento, ma non è infallibile.

**Limiti:**

*   **Non capisce il contesto completo:** L'IA lavora solo con i dati che le fornisci. Non conosce la storia della tua agenzia, le strategie passate o le dinamiche del mercato, a meno che tu non gliele spieghi.
*   **Può "allucinare":** A volte l'IA può inventare conclusioni o raccomandazioni che non sono supportate dai dati.
*   **Dipende dalla qualità dei dati:** Se i tuoi dati sono sporchi, incompleti o errati, anche l'analisi dell'IA lo sarà.
*   **Non è un sostituto dell'esperto umano:** L'IA può evidenziare pattern, ma l'interpretazione strategica finale e la decisione spettano sempre a te.

**Buone pratiche:**

*   **Verifica sempre:** Controlla i numeri e le conclusioni dell'IA. Non prendere nulla per oro colato.
*   **Sii specifico:** Più dettagli fornisci nel prompt (obiettivo, descrizione colonne, formato output desiderato), migliori saranno i risultati.
*   **Inizia in piccolo:** Non dare all'IA tabelle enormi e complesse all'inizio. Parti con dati più gestibili.
*   **Itera:** Se il primo output non è soddisfacente, riformula il prompt, aggiungi contesto o chiedi di approfondire un aspetto specifico.
*   **Chiedi spiegazioni:** Se l'IA fa un'affermazione, chiedile "Perché lo dici?" o "Su quali dati ti basi per questa conclusione?".
*   **Fornisci il contesto:** Se ci sono fattori esterni importanti (es. un lancio di prodotto, una festività), menzionali nel prompt per aiutare l'IA a interpretare meglio i dati.

---

### Fonti

*   `../data/openai-cookbook/examples/stripe_model_eval/selecting_a_model_based_on_stripe_conversion.ipynb::chunk5`
