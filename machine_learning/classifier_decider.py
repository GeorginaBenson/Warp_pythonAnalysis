#!/usr/bin/env python3
print(__doc__)


# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause


import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


def ML_classifiers(train, validation):
  h = .02  # step size in the mesh

  names = ["Nearest_Neighbors", "Linear_SVM", "RBF_SVM", "Gaussian_Process",
           "Decision_Tree", "Random_Forest", "Neural_Net", "AdaBoost", "Naive_Bayes", "QDA"]

  classifiers = [
      KNeighborsClassifier(3),
      SVC(kernel="linear", C=0.025),
      SVC(gamma=2, C=1),
      GaussianProcessClassifier(1.0 * RBF(1.0)),
      DecisionTreeClassifier(max_depth=5),
      RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
      MLPClassifier(alpha=1),
      AdaBoostClassifier(),
      GaussianNB(),
      QuadraticDiscriminantAnalysis()]

  X = []
  y = []
  X_val = []
  y_val = []
  

  for data in train:
    X.append([float(i) for i in data[4:]])
    y.append(data[1])
  for data in validation:
    X_val.append([float(i) for i in data[4:]])
    y_val.append(data[1])


  # iterate over classifiers
  for name, clf in zip(names, classifiers):
      clf.fit(X, y)	
      score = clf.score(X_val, y_val)
      print("name = {}, score = {}".format(name, score))
      predictions = clf.predict(X_val)
      #print(predictions)
      print(confusion_matrix(y_val, predictions))
      #if name == "Naive_Bayes":
        #print(clf._joint_log_likelihood(X))
      joblib.dump(clf, 'classifier_states/classifier_{}.pkl'.format(name))
      #print(joblib.dump(clf, 'classifier_states/classifier_{}.pkl'.format(name)))


def csv_processing(stats_csv):
  f = open(stats_csv, 'r')
  reader = csv.reader(f)
  headers = next(reader)
  stats_data = {}
  for h in headers:
    stats_data[h] = []
  for row in reader:
    for h, v in zip(headers, row):
      stats_data[h].append(v)
  return stats_data


def list_splitter(stats_list):
  training_list = []
  validation_list = []
  for data in stats_list:
    if data[0] in ('V' or 'v'):
      validation_list.append(data)
    elif data[0] in ('Te', 'TE', 'te', 'tE'):
        pass
    else:
      training_list.append(data)
  return training_list, validation_list
  
def data_selection(stats_data_dict):
  selected_data = []
  i = 0
  while i < len(stats_data_dict.get('label')):
    selected_data.append([stats_data_dict.get('T_or_V_or_Te')[i],
    stats_data_dict.get('label')[i], stats_data_dict.get('Chamber_temp')[i],
    stats_data_dict.get('voltage_mV')[i], stats_data_dict.get('power_mean')[i],
    stats_data_dict.get('power_SD')[i], stats_data_dict.get('power_iqr')[i],
    stats_data_dict.get('x_SD')[i], stats_data_dict.get('x_IQR')[i],
    stats_data_dict.get('x_skew')[i], stats_data_dict.get('x_kurtosis')[i],
    stats_data_dict.get('y_SD')[i], stats_data_dict.get('y_IQR')[i],
    stats_data_dict.get('y_skew')[i], stats_data_dict.get('y_kurtosis')[i],
    stats_data_dict.get('z_SD')[i], stats_data_dict.get('z_IQR')[i],
    stats_data_dict.get('z_skew')[i], stats_data_dict.get('z_kurtosis')[i]])  
    i +=1
  return selected_data

  
def main():
  import argparse
  parser = argparse.ArgumentParser(description = 'Machine learning from input csv')
  parser.add_argument('stats_data_csv', help = 'Input stats data csv file')
  args = parser.parse_args()
  
  stats_data_dict = csv_processing(args.stats_data_csv)
  stats_selected_data = data_selection(stats_data_dict)
  training_list, validation_list = list_splitter(stats_selected_data)
  ML_classifiers(training_list, validation_list)

if __name__ == "__main__":
  main()
