#!/usr/bin/env python3
print(__doc__)


# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.colors import ListedColormap
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
from sklearn.datasets import load_iris


def ML_classifiers(train, validation, blind_test):
  h = .02  # step size in the mesh

  names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
           "Decision Tree", "Random Forest", "Neural Net", "AdaBoost", "Naive Bayes", "QDA"]

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
  X_test = []
  y_test = []
  
  if not blind_test:  
    for data in train:
      X.append([float(i) for i in data[2:]])
      y.append(data[1])
    for data in validation:
      X_test.append([float(i) for i in data[2:]])
      y_test.append(data[1])
      
  
  else:
    for data in train:
      X.append([float(i) for i in data[2:]])
      y.append(data[1])
    for data in validation:
      X.append([float(i) for i in data[2:]])
      y.append(data[1])    
    for data in blind_test:
      X_test.append([float(i) for i in data[2:]])
      y_test.append(data[1])


  # iterate over classifiers
  for name, clf in zip(names, classifiers):
      clf.fit(X, y)	
      score = clf.score(X_test, y_test)
      print("name = {}, score = {}".format(name, score))
      predictions = clf.predict(X_test)
      print(predictions)
      print(confusion_matrix(y_test, predictions))


def csv_processing(stats_csv):
  with open(stats_csv) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    stats_data = []
    next(readCSV) #skips header line
    for row in readCSV:
      stat_data = row
      stats_data.append(stat_data)
  return stats_data
  
def list_splitter(stats_list):
  training_list = []
  validation_list = []
  for data in stats_list:
    if data[0] in ('V' or 'v'):
      validation_list.append(data)
    else:
      training_list.append(data)
  return training_list, validation_list
  
def data_selection(stats_data_list):
  selected_data = []
  # can edit these for whatever selection wanted. For now look at headings of csv to work out what values to use.
  # would be good at later date to have select from csv headings. (or at least define better)
  for data in stats_data_list:
    selected_data.append(data[:5] + data[9:13] + data[14:18] + data[19:23])  
  return selected_data

def main():
  import argparse
  parser = argparse.ArgumentParser(description = 'Machine learning from input csv')
  parser.add_argument('stats_data_csv', help = 'Input stats data csv file')
  parser.add_argument('--blind_test', help = 'Optional blind test csv', default=0) #Not required. Can be used if want to try on completely separate csv
  args = parser.parse_args()
  
  stats_data_list = csv_processing(args.stats_data_csv)
  stats_selected_data = data_selection(stats_data_list)
  training_list, validation_list = list_splitter(stats_selected_data)
  ML_classifiers(training_list, validation_list, args.blind_test)

if __name__ == "__main__":
  main()
