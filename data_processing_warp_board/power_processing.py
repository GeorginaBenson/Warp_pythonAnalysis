#!/usr/bin/env python3

import csv

def data_stats(data):
  mean = np.mean(data)
  sd = np.std(data)
  iqr = stats.iqr(data)
  skew = stats.skew(data)
  kurtosis = stats.kurtosis(data) 
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
  parser = argparse.ArgumentParser(description = 'Takes power file and outputs statistical data')
  parser.add_argument('power_data', help = 'Input transaction csv file')
  args = parser.parse_args()
  powers = csv_processing(args.power_data)
  #print(powers)
  mean_power, sd_power, iqr_power, skew_power, kurtosis_power = data_stats(powers)
  
  print('power = [{}, {}, {}, {}, {}]'.format(mean_power, sd_power, iqr_power, skew_power, kurtosis_power))
  

          

          

if __name__ == "__main__":
  import numpy as np
  import scipy.stats as stats
  main()
