from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, roc_curve, roc_auc_score, make_scorer, recall_score, precision_score
import matplotlib.pyplot as plt

def evaluate_predictions(predictions, y_true, y_proba=None, model_name="Modello"):
  cm = confusion_matrix(y_true, predictions)
  class_names = ['Classe 0 (Morto)', 'Classe 1 (Sopravvissuto)']
  
  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
  disp.plot(values_format='d')
  plt.show()
  
  perc_true_negative = cm[0,0]*100/(cm[0,0]+cm[0,1])
  perc_true_positive = cm[1,1]*100/(cm[1,0]+cm[1,1])
  
  print(f"Percentuale di veri negativi: {perc_true_negative:.2f}%")
  print(f"Percentuale di veri positivi: {perc_true_positive:.2f}%")
  
  print(classification_report(y_true, predictions, target_names=class_names))
  print(cm)
  
  # Se sono disponibili le probabilità, usiamole per ROC/AUC
  if y_proba is not None:
      fpr, tpr, thresholds = roc_curve(y_true, y_proba)
      auc = roc_auc_score(y_true, y_proba)
  else:
      fpr, tpr, thresholds = roc_curve(y_true, predictions)
      auc = roc_auc_score(y_true, predictions)
      
  plt.figure()
  plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.4f})')
  plt.plot([0, 1], [0, 1], 'k--')
  plt.xlabel('False Positive Rate')
  plt.ylabel('True Positive Rate')
  plt.title(f'ROC Curve - {model_name}')
  plt.legend(loc='lower right')
  plt.show()
    