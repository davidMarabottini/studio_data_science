# Machine Learning - Studio Personale e Progetti Pratici
Questo repository raccoglie i miei notebook che sto realizzando per il mio percorso di reskilling in Machine Learning. L'obiettivo è esplorare progressivamente i principali algoritmi e tecniche di apprendimento automatico con esempi pratici in Python.

## Obiettivi del progetto
Rafforzare le basi teoriche dell' apprendimento automatico.

Sperimentare varie tecniche e modelli.

Comprendere l'importanza della regolarizzazione e delle tecniche di validazione.

Creare una base solida per progetti futuri o applicazioni reali.

#### Struttura del repository
<pre>
├──  00 - Data
│   ├── <a href="./00-data/advertising.csv">Advertising.csv</a>
│   ├── <a href="./00-data/data.csv">data.csv</a>
│   ├── <a href="./00-data/healthcare-dataset-stroke-data.csv">healthcare-dataset-stroke-data.csv</a>
│   ├── <a href="./00-data/Real estate.csv">Real estate.csv</a>
│   └── <a href="./00-data/Salary_dataset.csv">Salary_dataset.csv</a>
│
├── 02 - Il dataset
│   ├── <a href="./02-il-dataset/13-tipi_dati.ipynb">Tipi di dati</a>
│   ├── <a href="./02-il-dataset/14-label-1h-encoder.ipynb">Label 1 hot encoder</a>
│   ├── <a href="./02-il-dataset/15-missing-data.ipynb">Missing data</a>
│   ├── <a href="./02-il-dataset/17-normalizzazione_e_standardizzazione.ipynb">Normalizzazione e standardizzazione</a>
│   └── <a href="./02-il-dataset/19-split_dati.ipynb">Split di dati</a>
│
├── 03-apprendimento-supervisionato-regressione/
│   ├── <a href="./03-apprendimento-supervisionato-regressione/23-regressione-lineare-semplice.ipynb">Regressione lineare semplice</a>
│   ├── <a href="./03-apprendimento-supervisionato-regressione/25-regressione-lineare-multipla.ipynb">Regressione lineare multipla</a>
│   └── <a href="./03-apprendimento-supervisionato-regressione/27-polynomial-regression.ipynb">Regressione polinomiale</a>
│
├── 04-regolarizzazioni-modelli-regolarizzati/
│   └── <a href="./04-regolarizzazioni-modelli-regolarizzati/31-overfitting-l1-l2.ipynb">Overfitting, L1 (Lasso), L2 (Ridge) dataset taiwan</a>
│
├── 05-apprendimento-supervisionato-classificazione/
│   ├── <a href="./05-apprendimento-supervisionato-classificazione/33-regressione-logistica.ipynb">Regressione logistica</a>
│   ├── <a href="./05-apprendimento-supervisionato-classificazione/35-classificazione_onevsall.ipynb">Classificazione one-vs-all (load_digits)</a>
│   └── <a href="./05-apprendimento-supervisionato-classificazione/35.2-classificazione_onevsall-olivetti_faces.ipynb">Classificazione one-vs-all (Olivetti faces)</a>
│
├── 06-classificazioni-non-lineari/
│   ├── <a href="./06-classificazioni-non-lineari/37-knn.ipynb">k-NN (Olivetti faces)</a>
│   ├── <a href="./06-classificazioni-non-lineari/39-alberi-decisionali.ipynb">Alberi decisionali (load_wine)</a>
│   ├── <a href="./06-classificazioni-non-lineari/39-failed-alberi-decisionali.ipynb">Alberi decisionali (stroke dataset)</a>
│   ├── <a href="./06-classificazioni-non-lineari/41-foreste-casuali.ipynb">Foreste casuali (stroke dataset)</a>
│   ├── <a href="./06-classificazioni-non-lineari/41.2-foreste-casuali.ipynb">Foreste casuali (wine_dataset)</a>
│   ├── <a href="./06-classificazioni-non-lineari/43-svm-lineari.ipynb">SVM Lineari (wine_dataset)</a>
│   ├── <a href="./06-classificazioni-non-lineari/45-svn-kernel-trick.ipynb">SVM Kernel Trick (make_circles)</a>
│   └── <a href="./06-classificazioni-non-lineari/48-percettore-multistrato-rete-neurale.ipynb">Percettore multistrato (reti neurali - census)</a>
│
├── 07-tecniche-validazioni-ottimizzazioni/
│   ├── <a href="./07-tecniche-validazioni-ottimizzazioni/50-stochastic-minibatch-gradient-desc.ipynb">Stochastic, minibatch e gradient descend (make_classification)</a>
│   ├── <a href="./07-tecniche-validazioni-ottimizzazioni/52-k-fold-cross-validation.ipynb">K-Fold Cross Validation (stroke dataset)</a>
│   └── <a href="./07-tecniche-validazioni-ottimizzazioni/54-gridsearchcv-randomsearchcv.ipynb">GridSearchCV, RandomizedSearchCV (real estate csv)</a>
│
├── 08-apprendimento-non-supervisionato-clustering/
│   ├── <a href="./08-apprendimento-non-supervisionato-clustering/56-kmeans.ipynb">K-Means (elbow method manuale + automatico)</a>
│   ├── <a href="./08-apprendimento-non-supervisionato-clustering/58-clustering-gerarchico.ipynb">Clustering gerarchico (make_blobs manuale + automatico)</a>
│   ├── <a href="./08-apprendimento-non-supervisionato-clustering/58.2-clustering-gerarchico-ottimizzato.ipynb">Clustering gerarchico (make_blobs manuale + automatico)</a>
│   ├── <a href="./08-apprendimento-non-supervisionato-clustering/58.3-clustering-gerarchico-ottimizzato.ipynb">Clustering gerarchico (Centinaia di cluster automatico ottimizzato)</a>
│   └── <a href="./08-apprendimento-non-supervisionato-clustering/60-dbscan.ipynb">Dbscan (make_moons ipotesi autotune epsilon)</a>
│
├── 09-riduzione-dimensionalita
│   ├── <a href="./09-riduzione-dimensionalita/61-principal-component-analisis-solo-pandas-numpy.ipynb">PCA solo pandas e numpy ( dataset stroke portato a 2 dimesnioni)</a>
│   ├── <a href="./09-riduzione-dimensionalita/61.2-pca-solo-pandas-numpy-function.ipynb">PCA 2 solo pandas e numpy ( dataset stroke portato a 2 dimesnioni)</a>
│   ├── <a href="./09-riduzione-dimensionalita/62-pca-visualizzazione-dataset-analisi-stroke.ipynb">PCA visualizzazione e modello ( dataset stroke portato a 2 dimesnioni)</a>
│   ├── <a href="./09-riduzione-dimensionalita/63-selezionare-nr-componenti-principali.ipynb">PCA Selezionare nr componenti principali (dataset stroke a 11 dimensioni, hard voting a 2 livelli con macchina a vettori di supporto)</a>

</pre>
## Requisiti
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
