# Previsione di sopravvivenza del Titanic

## Descrizione del progetto
Questo progetto ha l'obiettivo di costruire e confrontare diversi modelli di machine learning per prevedere la sopravvivenza dei passeggeri del Titanic. L'analisi si basa sul famoso dataset del Titanic, disponibile in questo repository. Vengono esplorati approcci di analisi dei dati, feature engeenering e modellazione con reti neurali e XGBoost.

## Struttura del progetto
Il progetto è organizzato nelle seguenti cartelle:
* `data/`: Contiene il dataset `Titanic-Dataset.csv` utilizzato per l'analisi.
* `studio/`: Contiene il notebook Jupyter `analisi_dataset.ipynb` con l'analisi esplorativa iniziale dei dati, l'ingegneria delle feature e la preparazione del dataset.
* `scripts/`: contiene funzioni di utility utilizzate in altri punti ed è integrato al virtual env
  * `csv_continue_to_ds_discreet.py`: prende i dati dal dataset titanic e li ritrasforma secondo la struttura definita dall'analisi preliminare, dopodichè torna il dataset già formattato nella struttura trovata e divide le variabili indipendente dalla variabile target
  * `evaluate_model.py`: astrae la procedura di valutazione della pipeline, accettando in input le predizioni, le y reali, il numero di probabilità e il nome del modello e mostrando matrice di confusione, classification report e curva dei roc auc
  * `print_features_bar.py`: mostra i dati come un diagramma a barre dove sull'asse delle X c'è il valore, sull'asse delle y il numero di persone che rientrano in quella classe mentre la percentuale di sopravvissuti è data dal colore
* `modelli/`: Contiene i notebook Jupyter per i modelli di machine learning sviluppati:
    * `analisis_model_neural_network.ipynb`: Implementazione di un modello basato su rete neurale (`MLPClassifier`) e undersampler.
    * `analisis_model_xgboost.ipynb`: Implementazione di un modello XGBoost con ottimizzazione degli iperparametri.
    * `analisis_model_xgboost_multiple.ipynb`: Implementazione di un modello basato sui migliori XGBoost per diverse metriche e un sistema di soft voting

## Dipendenze
Le dipendenze necessarie per eseguire i notebook si trovano nel file `requirements.txt`[cite: 5].

Per installare le dipendenze, esegui il seguente comando:
```bash
pip install -r requirements.txt