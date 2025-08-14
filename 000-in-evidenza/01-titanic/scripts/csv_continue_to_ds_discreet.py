import pandas as pd

# riprendo lo studio fatto in ../studio/analisi_dataset.ipynb e creo una funzione per avere il dataset secondo quanto emerso in quello studio

def csvContinue2DSDiscreet():
    titanic = pd.read_csv('../data/Titanic-Dataset.csv')
    X = titanic.drop(['PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin', 'Survived'], axis=1)
    y = titanic['Survived']
    
    # gestisco le età
    X['age_is_null'] = X['Age'].isnull()
    X['isChild'] = X['Age'].between(0,12, inclusive='both')
    X['isTeen'] = X['Age'].between(13,18, inclusive='both')
    X['isAdult'] = X['Age'].between(19,35, inclusive='both')
    X['isSenior'] = X['Age'].between(36,59, inclusive='both')
    X['isOld'] = X['Age'] >= 60
    
    X = X.drop(['Age'], axis=1)
    
    # gestisco il numero di familiari
    X['FamilySize'] = X['SibSp'] + X['Parch'] + 1
    
    X['IsAlone'] = X['FamilySize'] == 1
    X['IsSmallFamily'] = X['FamilySize'].between(2,4, inclusive='both')
    X['IsBigFamily'] = X['FamilySize'] > 4
    
    X = X.drop(['FamilySize', 'SibSp', 'Parch'], axis=1)
    
    #gestisco le classi
    
    X['FirstClass'] = X['Pclass'] == 1
    X['SecondClass'] = X['Pclass'] == 2
    X['ThirdClass'] = X['Pclass'] == 3
    X = X.drop(['Pclass'], axis=1)
    
    # gestisco il porto di imbarco
    
    X['EmbarkedS'] = (X['Embarked'] == 'S') | (X['Embarked'].isnull())
    X['EmbarkedC'] = X['Embarked'] == 'C'
    X['EmbarkedQ'] = X['Embarked'] == 'Q'
    
    X = X.drop(['Embarked'], axis=1)
    
    # gestisco il sesso
    X['Male'] = X['Sex'] == 'male'
    
    X = X.drop(['Sex'], axis=1)

    # ritorno il nuovo dataset
    return X, y    