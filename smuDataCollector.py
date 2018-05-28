#!/usr/bin/env python3
from bennellickeng.kitdrivers.usbtmc.smu import Smu
import time
import csv
import numpy as np


def main():
  import argparse
  parser = argparse.ArgumentParser(description = 'Creates csv of power data')
  parser.add_argument('csv_name', help = 'Name of csv file to be created')
  args = parser.parse_args()
  
  smu = Smu("/dev/usbtmc0")
  smu.reset()
  
  smu.set_source_voltage(3)
  smu.set_source_voltage_current_limit(500e-3)
  smu.set_sense_current()
  smu.set_sense_current_range()
  smu.set_sense_current_unit(smu.SenseUnit.W)
  smu.set_trigger_simple_loop(500, 0.01)
  smu.output_on()

  list_of_data = smu.trigger_and_collect(500, wait_time=55)

  i = 1
  while (i<=len(list_of_data)):
    list_of_data[i-1].append(i)
    list_of_data[i-1][2] #Think this is left over from earlier. Try and see if ok to remove
    i+=1

  with open(args.csv_name, 'w') as f:
      writer = csv.writer(f, delimiter=',')
      writer.writerow(['date','time','power', 'step'])
      for row in list_of_data:
        writer.writerow(row)
  
  
  
  smu.output_off()
  smu.reset()

if __name__ == "__main__":
  main()
