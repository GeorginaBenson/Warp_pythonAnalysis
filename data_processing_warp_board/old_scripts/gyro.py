#!/usr/bin/env python3


class GyroCalc:
  def __init__(self, chunked_data, sensor_name):
    x_pairs, y_pairs, z_pairs = self._pair_data(chunked_data)
    #print(chunked_data)
    self.x_concat = self._concatenate_data(x_pairs, sensor_name)
    self.y_concat = self._concatenate_data(y_pairs, sensor_name)
    self.z_concat = self._concatenate_data(z_pairs, sensor_name)
    self.x_2_comp = self._twos_complement(self.x_concat, sensor_name)
    self.y_2_comp = self._twos_complement(self.y_concat, sensor_name)
    self.z_2_comp = self._twos_complement(self.z_concat, sensor_name)

    
  @staticmethod
  def _pair_data(chunked_data):
    x = []
    y = []
    z = []
    for data in chunked_data:
      #print(data)
      x.append([i[1] for i in data[0:2]])
      y.append([i[1] for i in data[2:4]])
      z.append([i[1] for i in data[4:6]])
    return x, y, z
  
  
  @staticmethod
  def _concatenate_data(paired_data, sensor_name):
    concat_values = []
    for values in paired_data:
      if sensor_name == 'BMX055gyro':
        #print(values)
        LSB_value = format(int(values[0], 2), '#010b')
        MSB_value = format(int(values[1], 2), '#010b')
        concat = bin((int((MSB_value), 2) <<8) + (int(LSB_value, 2)))
        format_concat = format(int(concat, 2), '#018b')
        #print(format_concat)
      else:
        pass
      concat_values.append(format_concat)
    return concat_values
  
  @staticmethod
  def _twos_complement(concat_values, sensor_name):
    twos_comp_list = []
    for value in concat_values:
      binary1s = str('1'*(len(value)-2))
      data_invert = bin(int(value[2:], 2)^int(binary1s, 2))
      if int(value[2]) == 1:
        data_twos_comp_raw = (-(int(data_invert, 2)+1))
      else:
        data_twos_comp_raw = int(value, 2)
      if sensor_name == 'BMX055gyro':
        data_twos_comp = (data_twos_comp_raw)/16.4
      else:
        data_twos_comp = 'NaN'
      twos_comp_list.append(data_twos_comp)
    return twos_comp_list   

def main():
  import csv
  import argparse
  from warpParser import TranscriptData
  parser = argparse.ArgumentParser(description = 'Parses sensor data from warp transcript')
  parser.add_argument('transcript', help = 'Input transaction txt file')
  args = parser.parse_args()

  data_instance = TranscriptData(args.transcript)
  gyro_data = GyroCalc(data_instance.chunked_data, data_instance.sensor_name)
  print(gyro_data.x_2_comp)
  print(gyro_data.y_2_comp)
  print(gyro_data.z_2_comp)
  
  #Uncomment as necessary
  '''
  with open('../../data/issue-115/data_gyro_temp20_1.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['x','y','z'])
    rows = zip(gyro_data.x_2_comp, gyro_data.y_2_comp, gyro_data.z_2_comp)
    for row in rows:
      writer.writerow(row)
  '''

if __name__ == "__main__":
  main()
