import pandas as pd

def csv_continue_to_ds_discreet():
  
  
  stroke = pd.read_csv('../data/healthcare-dataset-stroke-data.csv')
  
  no_bmi_error = ~stroke['bmi'].isnull() & (stroke['bmi'] >= 15) & (stroke['bmi'] < 60)
  stroke = stroke[no_bmi_error]

  no_other_gender = stroke['gender'] != 'Other'
  stroke = stroke[no_other_gender]
  
  stroke = stroke.reset_index(drop=True)

  X = stroke.drop(columns=['stroke', 'id'])
  y = stroke['stroke'].values

  X['age_low_risk'] = X['age'] < 40
  X['age_medium_risk'] = (X['age'] >= 40) & (X['age'] < 60)
  X['age_high_risk'] = X['age'] >= 60
  X.drop(columns=['age'], inplace=True)

  X['glucose_low_risk'] = X['avg_glucose_level'] < 120
  X['glucose_medium_risk'] = (X['avg_glucose_level'] >= 120) & (X['avg_glucose_level'] < 220)
  X['glucose_high_risk'] = X['avg_glucose_level'] >= 220
  X.drop(columns=['avg_glucose_level'], inplace=True)

  X['bmi_low_risk'] = X['bmi'] < 25
  X['bmi_medium_risk'] = (X['bmi'] >= 25) & (X['bmi'] < 40)
  X['bmi_high_risk'] = X['bmi'] >= 40
  X.drop(columns=['bmi'], inplace=True)

  X['male'] = X['gender'] == 'Male'
  X.drop(columns=['gender'], inplace=True)

  X['work_governative'] = X['work_type'] == 'Govt_job'
  X['work_private'] = X['work_type'] == 'Private'
  X['work_self'] = X['work_type'] == 'Self-employed'
  X['work_never'] = X['work_type'].isin(['children', 'Never_worked'])

  X.drop(columns=['work_type'], inplace=True)

  X['ever_married'] = X['ever_married'] == 'Yes'

  X['Residence_type_Urban'] = X['Residence_type'] == 'Urban'
  X.drop(columns=['Residence_type'], inplace=True)

  X['smoking_status_former'] = X['smoking_status'] == 'formerly smoked'
  X['smoking_status_never'] = X['smoking_status'] == 'never smoked'
  X['smoking_status_smokes'] = X['smoking_status'] == 'smokes'
  X['smoking_status_unknown'] = X['smoking_status'] == 'Unknown'
  X.drop(columns=['smoking_status'], inplace=True)
  
  return X, y
  