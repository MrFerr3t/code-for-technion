import numpy as np
import matplotlib.pyplot as plt

def binary_confusion_matrix(y_true, y_pred):
  """calculates the true positive, true negative,
    false positive and false negative and returns those values"""
  y_true = np.array(y_true)
  y_pred = np.array(y_pred)
  TP = np.sum((y_true == 1) & (y_pred == 1))
  FN = np.sum((y_true == 1) & (y_pred == 0))
  FP = np.sum((y_true == 0) & (y_pred == 1))
  TN = np.sum((y_true == 0) & (y_pred == 0))

  return TN, FP, FN, TP

def f1_score(y_true, y_pred):
    """ returns f1_score of binary classification task with true labels y_true and predicted labels y_pred """ 
    TN, FP, FN, TP = binary_confusion_matrix(y_true, y_pred)
    if(TP + FN != 0):
      recall = TP / (TP + FN)
    else:
       recall = 0
    if(TP + FP != 0):     
      precision = TP / (TP + FP)
    else:
       precision = 0  
    return (2 * recall * precision) / (recall + precision) if recall + precision != 0 else 0


def rmse(y_true, y_pred):
   """returns RMSE of regression task with true labels y_true and predicted labels y_pred""" 
   return np.sqrt(np.mean((y_true - y_pred) ** 2))

def visualize_results(k_list, scores, metric, title, path): 
    """ plot a results graph of cross validation scores """ 

    plt.plot(k_list, scores, marker='o', linestyle='-')
    plt.xlabel('k')
    plt.ylabel(metric)
    plt.title(title)

    plt.savefig(path)
    plt.close()

