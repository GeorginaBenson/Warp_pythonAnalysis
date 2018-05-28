#!/usr/bin/env python3
#print(__doc__)

# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause


import csv

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


def data_labelling(test, label_state):
    h = .02  # step size in the mesh

    clf = joblib.load('classifier_states/classifier_Naive_Bayes.pkl')
    print(clf)

    if label_state in ('Y', 'y', 'yes', 'Yes'):
        X_test = []
        y_test = []

        for data in test:
            X_test.append([float(i) for i in data[4:]])
            y_test.append(data[1])

        score = clf.score(X_test, y_test)
        predictions = clf.predict(X_test)
        param_theta = clf.theta_
        param_var = clf.sigma_
        #print(param_theta) # uncomment for mean of each feature to be printed
        #print(param_var) # uncomment for variance of each feature to be printed
        print(score)
        names = []
        for label in predictions:
            names.append(name_from_label(label))
        print(names)

    else:
        X_test = []

        for data in test:
            X_test.append([float(i) for i in data[4:]])


        predictions = clf.predict(X_test)
        print(predictions)
        names = []
        for label in predictions:
            names.append(name_from_label(label))
        print(names)


def name_from_label(label_pred):
    for label in label_pred:
        if label == '1':
            name = 'BMX055gyro'
        elif label == '2':
            name = 'BMX055accel'
        elif label == '3':
            name = 'MMA8451Q'
        else:
            name = 'unknown'
        return name

def list_splitter(stats_list):
  test_list = []
  for data in stats_list:
    if data[0] in ('Te', 'TE', 'te', 'tE'):
      test_list.append(data)
  return test_list

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

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Machine learning from input csv')
    parser.add_argument('test_stats_data_csv', help='Input stats data csv file')
    parser.add_argument('label_state', help='y if data has labels. n if not')

    args = parser.parse_args()

    stats_data_dict = csv_processing(args.test_stats_data_csv)
    stats_test_data = data_selection(stats_data_dict)
    test_list = list_splitter(stats_test_data)
    data_labelling(test_list, args.label_state)


if __name__ == "__main__":
    main()