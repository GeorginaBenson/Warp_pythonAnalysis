#!/usr/bin/env python3
import csv
import numpy as np
import scipy.stats as stats
from itertools import chain
import os

class DataStatsProcessing:
  SENSOR_BMX055gyro = "BMX055gyro"
  SENSOR_BMX055accel = "BMX055accel"
  SENSOR_MMA8451Q = "MMA8451Q"
  SENSOR_ADXL362 = "ADXL362"
    
  def __init__(self, sensor_data, powers, sensor_name, chamber_temp, voltage, validation_temp, test_temp):
    self.sensor_data = sensor_data
    self.powers = powers
    self.sensor_name = sensor_name
    self.chamber_temp = chamber_temp
    self.voltage = voltage
    self.validation_temp = validation_temp
    self.test_temp = test_temp
    self.label = self._label_generator()
    self.t_or_v_or_te = self._t_or_v_or_te()
    self.stats_list = self._stats_list()
    
    
  def _label_generator(self):
    if self.sensor_name == self.SENSOR_BMX055gyro:
      label = 1
    elif self.sensor_name == self.SENSOR_BMX055accel:
      label = 2
    elif self.sensor_name == self.SENSOR_MMA8451Q:
      label = 3
    elif self.sensor_name == self.SENSOR_ADXL362:
      label = 4
    else:
      raise Exception("There is currently no label for the {} sensor. Please create one".format(self.sensor_name))
    return label
    
  
  def _t_or_v_or_te(self):
    if any(int(self.chamber_temp) in self.validation_temp for temp in self.validation_temp):
      value = 'V'
    elif any(int(self.chamber_temp) in self.test_temp for temp in self.test_temp):
      value = 'Te'
    else:
      value = 'T'
    return value
    
    
  def _stats_list(self):
    stats_processed_list = []
    stats_processed_list.append((self.t_or_v_or_te, self.label, self.chamber_temp, self.voltage))
    stats_processed_list.append(self._process_power_list(self.powers))
    stats_processed_list.append(self._process_data_list(self.sensor_data.x))
    stats_processed_list.append(self._process_data_list(self.sensor_data.y))
    stats_processed_list.append(self._process_data_list(self.sensor_data.z))
    stats_processed_list.append(self._process_board_temp(self.sensor_data.board_temp))
    stats_list_unpacked = self._remove_tuple(stats_processed_list)
    return stats_list_unpacked


  @staticmethod
  def _remove_tuple(stats_list):
    stats_list_unpacked = list(chain.from_iterable(stats_list))
    return stats_list_unpacked

  @staticmethod
  def _data_stats(data):
    sd = np.std(data)
    iqr = stats.iqr(data)
    skew = stats.skew(data)
    kurtosis = stats.kurtosis(data) 
    mean = np.mean(data)
    return mean, sd, iqr, skew, kurtosis

  def _process_data_list(self, data):
    data_mean, data_sd, data_iqr, data_skew, data_kurtosis = self._data_stats(data)
    return data_mean, data_sd, data_iqr, data_skew, data_kurtosis

  def _process_power_list(self, powers):
    powers_mean, powers_sd, powers_iqr, powers_skew, powers_kurtosis = self._data_stats(powers)
    return powers_mean, powers_sd, powers_iqr, powers_skew, powers_kurtosis

  def _process_board_temp(self, board_temp):
    if board_temp:
      bt_mean, bt_sd, bt_iqr, bt_skew, bt_kurtosis = self._data_stats(board_temp)
    else:
      bt_mean = bt_sd = bt_iqr = bt_skew = bt_kurtosis = 0 #set to 0 so that can at least take in for machine learning if want to.
    return bt_mean, bt_sd, bt_iqr, bt_skew, bt_kurtosis


def processed_data_csv(list_of_stats_data, csv_name):
  data_path_check = os.path.isfile(csv_name)
  with open(csv_name, 'a') as f:
    writer = csv.writer(f, delimiter=',')
    header = ['T_or_V_or_Te', 'label', 'Chamber_temp', 'voltage_mV', 'power_mean','power_SD','power_iqr', 'power_skew', 'power_kurtosis',  'x_mean', 'x_SD', 'x_IQR', 'x_skew', 'x_kurtosis', 'y_mean', 'y_SD', 'y_IQR', 'y_skew', 'y_kurtosis', 'z_mean', 'z_SD', 'z_IQR', 'z_skew', 'z_kurtosis', 'board_temp_mean', 'board_temp_SD', 'board_temp_iqr', 'board_temp_skew', 'board_temp_kurtosis']
    if not data_path_check:
      writer.writerow(header)
    writer.writerow(list_of_stats_data)    

  
  

def main():
  import argparse
  from experiment import Experiment
  parser = argparse.ArgumentParser(description = 'Gets accelerometer and power stats results in csv')
  parser.add_argument('stats_csv_name', help = 'File name for stats data csv')
  parser.add_argument('input_data', help = 'Either a directory, or 2 files want to process data from', nargs='+')
  parser.add_argument('--val_temp', help = 'Temperatures you want the data for to be used for validation (as opposed to training or test)', nargs='*',  type=int, default = [20])
  parser.add_argument('--test_temp', help='Temperatures you want the data for to be used for test (as opposed to training or validation)', nargs='*', type=int, default=[24])
  args = parser.parse_args()
  if all(os.path.isdir(data) for data in args.input_data):
    for data in args.input_data:
      exp = Experiment.dir_input(data)
      for run in exp:
        processed_data = DataStatsProcessing(run.sensor_data, run.power, run.sensor_name, run.chamber_temp, run.voltage, args.val_temp, args.test_temp).stats_list
        processed_data_csv(processed_data, args.stats_csv_name)
  elif all(os.path.isfile(data) for data in args.input_data) and len(args.input_data)==2: #Would be good to check if from same folder and have same name
    exp = Experiment.file_input(args.input_data)
    for run in exp:
      processed_data = DataStatsProcessing(run.sensor_data, run.power, run.sensor_name, run.chamber_temp, run.voltage, args.val_temp, args.test_temp).stats_list
      processed_data_csv(processed_data, args.stats_csv_name)
  else:
    print("This is not a defined input. Please try again")


if __name__ == "__main__":
  main()
