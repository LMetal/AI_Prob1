# Decisione sulla Produzione con Rete Bayesiana

## 📌 Descrizione
Questo progetto modella un processo decisionale per un’industria manifatturiera che deve stabilire se **andare avanti con la produzione di un nuovo prodotto** o fermarla.  

Le decisioni sono influenzate da due fattori principali:
- **Qualità del prodotto**: può essere *standard* o *alta*
- **Domanda di mercato**: può essere *bassa* o *alta*

Prima di decidere sulla produzione, l’azienda può effettuare due azioni opzionali:
1. **Ricerche di marketing** (costo: **$1000**) – accurate al 90% nell’indicare la domanda di mercato.  
2. **Sviluppo di un prototipo** (costo: **$5000**) – aumenta la probabilità di ottenere alta qualità con una confidenza dell’85%.  

L’azienda può anche scegliere di effettuare entrambe le azioni, nell’ordine:  
**prima ricerca di mercato → poi prototipo**.  

Il modello viene implementato tramite una **rete bayesiana** che stima la probabilità dei diversi scenari e guida l’azienda verso la **sequenza di azioni ottimale** per massimizzare l’**utile atteso**.  

---

## 📊 Specifiche del Modello
- **Costi**
  - Produzione: **$2500**  
  - Ricerca di mercato: **$1000**  
  - Prototipo: **$5000**  

- **Profitti**
  - Nessuno: **$0**  
  - Basso: **$10000**  
  - Alto: **$50000**  

- **Vincoli probabilistici**
  - Accuratezza ricerche di mercato: **90%**  
  - Probabilità di miglioramento qualità tramite prototipo: **85%**  
  - Probabilità di profitto: dipendono da qualità × domanda, con valori ragionevoli.  
    - **Qualità alta + domanda alta → più probabile profitto alto**  
    - **Qualità bassa + domanda bassa → più probabile nessun profitto**  

---

## ⚙️ Funzionalità
- Modellazione del problema con una **rete bayesiana**.  
- Calcolo delle **probabilità condizionate** di profitto in base alle scelte fatte.  
- Stima dell’**utile atteso** per ciascuna strategia (produzione diretta, ricerca, prototipo, entrambe).  
- Identificazione della **decisione ottimale**.  

---

