#!/usr/bin/env python3

def data_stats(data):
  sd = np.std(data)
  iqr = stats.iqr(data)
  skew = stats.skew(data)
  kurtosis = stats.kurtosis(data) 
  mean = np.mean(data)
  return mean, sd, iqr, skew, kurtosis

  
def csv_processing(power_csv):
  with open(power_csv) as csvfile:
      readCSV = csv.reader(csvfile, delimiter=',')
      powers = []
      next(readCSV) #skips header line
      for row in readCSV:
          power = row[2]
          powers.append(float(power))
  return powers

def main():
  import argparse
  from gyro import GyroCalc
  from warpParser import TranscriptData
  parser = argparse.ArgumentParser(description = 'Gets accelerometer and power results')
  parser.add_argument('transcript_accel', help = 'Input accel transaction txt file')
  parser.add_argument('transcript_power', help = 'Input power transaction txt file')
  args = parser.parse_args()

  data_instance = TranscriptData(args.transcript_accel)
  gyro_data = GyroCalc(data_instance.chunked_data, data_instance.sensor_name)
  powers = csv_processing(args.transcript_power)
  
  mean_x, sd_x, iqr_x, skew_x, kurtosis_x = data_stats(gyro_data.x_2_comp)
  mean_y, sd_y, iqr_y, skew_y, kurtosis_y = data_stats(gyro_data.y_2_comp)
  mean_z, sd_z, iqr_z, skew_z, kurtosis_z = data_stats(gyro_data.z_2_comp)
  mean_power, sd_power, iqr_power, skew_power, kurtosis_power = data_stats(powers)
  '''
  print('x = [{}, {}, {}, {}]'.format(sd_x, iqr_x, skew_x, kurtosis_x))
  print('y = [{}, {}, {}, {}]'.format(sd_y, iqr_y, skew_y, kurtosis_y))
  print('z = [{}, {}, {}, {}]'.format(sd_z, iqr_z, skew_z, kurtosis_z))
  '''
  #for gyro accel comparison only need SD from accel data
  print('[{}, {}, {}, {}, {}]'.format(sd_power, sd_power, sd_x, sd_y, sd_z))
  
if __name__ == "__main__":
  import numpy as np
  import scipy.stats as stats
  import csv
  main()
