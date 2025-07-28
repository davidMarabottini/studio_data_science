# Machine Learning - Studio Personale e Progetti Pratici
Questo repository raccoglie i miei notebook che sto realizzando per il mio percorso di reskilling in Machine Learning. L'obiettivo è esplorare progressivamente i principali algoritmi e tecniche di apprendimento automatico con esempi pratici in Python.

## Obiettivi del progetto
Rafforzare le basi teoriche dell' apprendimento automatico.

Sperimentare varie tecniche e modelli.

Comprendere l'importanza della regolarizzazione e delle tecniche di validazione.

Creare una base solida per progetti futuri o applicazioni reali.

#### Struttura del repository
```
├──  00 - Data
│   ├── Advertising.csv
│   ├── data.csv
│   ├── healthcare-dataset-stroke-data.csv
│   ├── Real estate.csv
│   └── Salary_dataset.csv
│
├── 02 - Il dataset
│   ├── Tipi di dati
│   ├── Label 1 hot encoder
│   ├── Missing data
│   ├── Normalizzazione e standardizzazione
│   └── Split di dati
│
├── 03-apprendimento-supervisionato-regressione/
│   ├── Regressione lineare semplice 
│   ├── Regressione lineare multipla
│   └── Regressione polinomiale
│
├── 04-regolarizzazioni-modelli-regolarizzati/
│   └── Overfitting, L1 (Lasso), L2 (Ridge)
│
├── 05-apprendimento-supervisionato-classificazione/
│   ├── Regressione logistica
│   ├── Classificazione one-vs-all (load_digits)
│   └── Classificazione one-vs-all (Olivetti faces)
│
├── 06-classificazioni-non-lineari/
│   ├── k-NN (Olivetti faces)
│   ├── Alberi decisionali (load_wine)
│   ├── Alberi decisionali (stroke dataset)
│   ├── Foreste casuali (stroke dataset)
│   ├── Foreste casuali (wine_dataset)
│   ├── SVM Lineari (wine_dataset)
│   ├── SVM Kernel Trick (make_circles)
│   └── Percettore multistrato (reti neurali - census)
│
├── 07-tecniche-validazioni-ottimizzazioni/
│   ├── Stochastic, minibatch e gradient descend (make_classification)
│   ├── K-Fold Cross Validation (stroke dataset)
│   └── GridSearchCV, RandomizedSearchCV (real estate csv)
│
└── 08-apprendimento-non-supervisionato-clustering/
    ├── K-Means (elbow method manuale + automatico)
    ├── Clustering gerarchico (make_blobs manuale + automatico)
    ├── Clustering gerarchico (make_blobs manuale + automatico)
    ├── Clustering gerarchico (Centinaia di cluster automatico ottimizzato)
    └── Dbscan (make_moons ipotesi autotune epsilon)
```
### Requisiti
I notebook sono scritti in Python 3.8+ e utilizzano le seguenti principali librerie:

numpy, pandas, matplotlib, seaborn, imblearn, scikit-learn, scipy, joblib

#### Per installarle:

pip install numpy pandas matplotlib seaborn scikit-learn scipy joblib
(Per ora ancora non è presente un virtual env ma ho intenzione di integrarlo)

#### Come iniziare
Clona il repository:
```
git clone https://github.com/davidMarabottini/studio_data_science.git
```

Avvia un programma capace di leggere notebook yupiter

Esplora liberamente i notebook. Ogni cartella e ogni file è stato creato dopo aver appreso delle nozioni da un corso udemy, spesso cercando sfide più complesse rispetto a quelle proposte dal corso ed essendo così costretto ad apprendere e sperimentare molte più tecniche di quelle proposte fino a quel punto (vedi pipeline, oversampling, undersampling, tentativi di clustering automatico e altro).

Note
Attualmente i file .ipynb contengono codice e considerazioni varie.

Autore
Progetto personale di reskilling in Machine Learning curato da David Marabottini.
