#!/usr/bin/env python3
from warpParser import TranscriptData
import math

class ProcessCalc:
  def __init__(self, chunked_data, sensor_name):
    self.sensor_name = sensor_name
    
    self.x = []
    self.y = []
    self.z = []
    self.board_temp = []

    for chunk in chunked_data:
      self.x.append(self._process_axis(chunk, "x"))
      self.y.append(self._process_axis(chunk, "y"))
      self.z.append(self._process_axis(chunk, "z"))
      self.board_temp.append(self._process_temp(chunk))

  _SENSOR_BMX055accel_REG = {
    "x": {"msb": 0x03, "lsb": 0x02},
    "y": {"msb": 0x05, "lsb": 0x04},
    "z": {"msb": 0x07, "lsb": 0x06},
    "temp": 0x08,
  }

  _SENSOR_BMX055gyro_REG = {
    "x": {"msb": 0x03, "lsb": 0x02},
    "y": {"msb": 0x05, "lsb": 0x04},
    "z": {"msb": 0x07, "lsb": 0x06},
  }
  
  _SENSOR_MMA8451Q_REG = {
    "x": {"msb": 0x01, "lsb": 0x02},
    "y": {"msb": 0x03, "lsb": 0x04},
    "z": {"msb": 0x05, "lsb": 0x06},
  }
  
  _SENSOR_ADXL362_REG = {
    "x": {"msb": 0x0F, "lsb": 0x0E},
    "y": {"msb": 0x11, "lsb": 0x10},
    "z": {"msb": 0x13, "lsb": 0x12},
    "temp": {"msb": 0x15, "lsb": 0x14},
  }

  def _process_axis(self, chunk, axis):
    if self.sensor_name == TranscriptData.SENSOR_BMX055accel:
      msb_reg = self._SENSOR_BMX055accel_REG[axis]["msb"]
      lsb_reg = self._SENSOR_BMX055accel_REG[axis]["lsb"]
      msb_val = chunk[msb_reg]
      lsb_val = chunk[lsb_reg]
      concat = (msb_val<<4) + (lsb_val>>4)
      format_concat = format(concat, '#014b')
      data_twos_comp = self._twos_complement(format_concat)/970
    
    if self.sensor_name == TranscriptData.SENSOR_BMX055gyro:
      msb_reg = self._SENSOR_BMX055gyro_REG[axis]["msb"]
      lsb_reg = self._SENSOR_BMX055gyro_REG[axis]["lsb"]
      msb_val = chunk[msb_reg]
      lsb_val = chunk[lsb_reg]
      concat = (msb_val<<8) + (lsb_val)
      format_concat = format(concat, '#018b')
      data_twos_comp = self._twos_complement(format_concat)/16.4
    
    if self.sensor_name == TranscriptData.SENSOR_ADXL362:
      msb_reg = self._SENSOR_ADXL362_REG[axis]["msb"]
      lsb_reg = self._SENSOR_ADXL362_REG[axis]["lsb"]
      msb_val = self._stripped_sign_extend(chunk[msb_reg])
      lsb_val = chunk[lsb_reg]
      concat = (msb_val<<8) + (lsb_val)
      format_concat = format((concat), '#014b')
      data_twos_comp = self._twos_complement(format_concat)/1000
      
    
    if self.sensor_name == TranscriptData.SENSOR_MMA8451Q:
      msb_reg = self._SENSOR_MMA8451Q_REG[axis]["msb"]
      lsb_reg = self._SENSOR_MMA8451Q_REG[axis]["lsb"]
      msb_val = chunk[msb_reg]
      lsb_val = chunk[lsb_reg]
      concat = (msb_val<<6) + (lsb_val>>2)
      format_concat = format(concat, '#016b')
      data_twos_comp = self._twos_complement(format_concat)/4096  
    return data_twos_comp

  def _process_temp(self, chunk):
    if self.sensor_name == TranscriptData.SENSOR_BMX055accel:
      temp_reg = self._SENSOR_BMX055accel_REG["temp"]
      try:
        temp_val = 23+ self._twos_complement(bin(chunk[temp_reg]))/2  
      except:
        temp_val = math.nan
    elif self.sensor_name == TranscriptData.SENSOR_ADXL362:
      msb_reg = self._SENSOR_ADXL362_REG["temp"]["msb"]
      lsb_reg = self._SENSOR_ADXL362_REG["temp"]["lsb"]
      msb_val = self._stripped_sign_extend(chunk[msb_reg])
      lsb_val = chunk[lsb_reg]
      concat = (msb_val<<8) + (lsb_val)
      format_concat = format((concat), '#014b')
      try:
        temp_val = 25+self._twos_complement(format_concat)*0.065 # Not entirely sure this is correct, but data is unusual so cannot tell very easily
      except:
        temp_val = math.nan
    else:
      temp_val = math.nan
    return temp_val

  def _stripped_sign_extend(self, value):
    if self.sensor_name == TranscriptData.SENSOR_ADXL362:
      mask = 0b00001111
      stripped_value = mask & value
    else:
      stripped_value = value #May change but haven't set up any others yet that required this
    return stripped_value
  
  @staticmethod
  def _twos_complement(value):
    '''
    Takes a string containing binary representation of a value and returns an integer
    '''
    binary1s = str('1'*(len(value)-2))
    data_invert = bin(int(value[2:], 2)^int(binary1s, 2))
    if int(value[2]) == 1:
      data_twos_comp_raw = (-(int(data_invert, 2)+1))
    else:
      data_twos_comp_raw = int(value, 2)
    return data_twos_comp_raw
    

def main():
  import csv
  import argparse
  from warpParser import TranscriptData
  parser = argparse.ArgumentParser(description = 'Parses sensor data from warp transcript')
  parser.add_argument('transcript', help = 'Input transaction txt file')
  args = parser.parse_args()

  data_instance = TranscriptData(args.transcript)
  processed_data = ProcessCalc(data_instance.chunked_data_dict, data_instance.sensor_name)
  print(processed_data.x)
  print(processed_data.y)
  print(processed_data.z)
  print(processed_data.board_temp)


if __name__ == "__main__":
  main()
