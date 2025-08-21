# Previsione di ictus

## Descrizione del progetto
Questo progetto ha l'obiettivo di costruire e confrontare diversi modelli di machine learning per prevedere il rischio di ictus. L'analisi si basa sul dataset stroke prediction di kaggle, contenente dai estremamente sbilanciati, infatti solo il 5% risulta con il parametro stroke a 1 (ictus), il resto è a 0 (non ictus), lo scopo è creare un modello capace di predire gli Ictus.
Per gestire la sfida ho applicato metodologie di class imbalance e mi sono focalizzato su matrice di confusione, roc auc curve e classification report per avere una situazione più dettagliata.

## Struttura del progetto
Il progetto è organizzato nelle seguenti cartelle:
* `data/`: Contiene il dataset `healthcare-dataset-stroke-data.csv` utilizzato per l'analisi.
* `studio/`: Contiene studi fatti sul modello, prima uno studio dove rendo il dataset in un insieme di features booleane, poi un analisi di questo modello per l'heatmap
* `scripts/`: contiene funzioni di utility utilizzate in altri punti ed è integrato al virtual env
  * `csv_continue_to_ds_discreet.py`: prende i dati dal dataset stroke e li ritrasforma secondo la struttura definita dall'analisi preliminare, dopodichè restituisce il dataset già formattato nella struttura trovata e divide le variabili indipendente dalla variabile target
  * `evaluate_model.py`: astrae la procedura di valutazione della pipeline, accettando in input le predizioni, le y reali, il numero di probabilità e il nome del modello e mostrando matrice di confusione, classification report e curva dei roc auc
  * `print_features_bar.py`: mostra i dati come un diagramma a barre dove sull'asse delle X c'è il valore, sull'asse delle y il numero di persone che rientrano in quella classe mentre la percentuale di sopravvissuti è data dal colore
* `modelli/`: Contiene i notebook Jupyter per i modelli di machine learning sviluppati:
    * `randomforest.ipynb`: Implementazione, hyperparameters tuning e valutazione tramite matrice di confusione, classification report e roc curve di un modello basato sulla random forest
    * `xgboost.ipynb`: Implementazione, hyperparameters tuning e valutazione tramite matrice di confusione, classification report e roc curve di un modello basato su XGBoost
    * `analisis_model_xgboost_multiple.ipynb`: Implementazione, hyperparameters tuning e valutazione tramite matrice di confusione, classification report e roc curve di un metamodello basato su una regressione che apprende il risultato migliore tra 7 modelli di XGBoost (che massimizzano roc auc, recall su classe 0, recall su classe 1, precision su classe 0, precision su classe 1, f1 su classe 0 e f1 su classe 1)

## Dipendenze
Le dipendenze necessarie per eseguire i notebook si trovano nel file `requirements.txt`[cite: 5].

Per installare le dipendenze, esegui il seguente comando:
```bash
pip install -r requirements.txt