#!/usr/bin/env python3

class TranscriptData:
  SENSOR_BMX055gyro = "BMX055gyro"
  SENSOR_BMX055accel = "BMX055accel"
  SENSOR_MMA8451Q = "MMA8451Q"
  SENSOR_ADXL362 = "ADXL362"

  def __init__(self, filename):
    self.filename = filename
    lines = open(filename, 'r').readlines()
    try:
      self._parse(lines)
    except Exception as e:
      raise Exception("Failed to parse '{}'".format(self.filename)) from e

  @staticmethod
  def _chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

  def _parse(self, lines):
    # Strip leading and trailing white space
    stripped_lines = [line.strip() for line in lines]

    # Skip ahead to start of data
    start_info_index = stripped_lines.index('Enter selection> j')
    start_data_index = start_info_index+13
    info_lines = stripped_lines[start_info_index:start_data_index]

    # Extract useful info lines
    chunks_raw = info_lines[3]
    reps_raw = info_lines[6]
    start_addr_raw = info_lines[9]
    sensor_name_raw = info_lines[12]

    last_value_fn = lambda line: int(line.split(' ')[-1])

    self.chunk_size = last_value_fn(chunks_raw)
    self.reps = last_value_fn(reps_raw)
    if '1idx' not in reps_raw:
      self.reps += 1 #In original code uses 0 indexing style when counting. Makes more sense to me to start counting at 1.
    self.sensor_name = sensor_name_raw[:-1]

    data_lines = stripped_lines[start_data_index:(self.chunk_size*self.reps)+start_data_index]
    
    if self.sensor_name == self.SENSOR_MMA8451Q:
        data_tuples = self._mma8451q(data_lines)
    elif self.sensor_name == self.SENSOR_ADXL362:
        data_tuples = self._adxl362(data_lines)
    elif self.sensor_name == self.SENSOR_BMX055accel:
        data_tuples = self._bmx055(data_lines)
    elif self.sensor_name == self.SENSOR_BMX055gyro:
        data_tuples = self._bmx055(data_lines)
    else:
        print('not currently set up for processing this kind of sensor')
        data_tuples = []
        
    if len(data_tuples) % self.chunk_size != 0:
      raise Exception('len(data_tuples)={} is not a multiple of chunk_size={}.'.format(len(data_tuples), self.chunk_size))

    self.chunked_data = list(self._chunks(data_tuples, self.chunk_size))
    self.chunked_data_dict = self._return_dict(self.chunked_data)
   
   
  def _mma8451q(self, data_lines):
    data_tuples = []
    for data in data_lines:
        data_addr, __, data_value = data.split(' ')
        data_tuples.append((int(data_addr, 0), (int(data_value, 0))))
    return data_tuples

  def _adxl362(self, data_lines):
    data_tuples = []
    for data in data_lines:
        data_addr, __, __, __, data_value_raw = data.split(' ')
        data_value = data_value_raw[:-1]
        data_tuples.append((int(data_addr, 0), (int(data_value, 0))))
    return data_tuples
    
  def _bmx055(self, data_lines):
    data_tuples = []
    for data in data_lines:
        data_addr, __, data_value = data.split(' ')
        data_tuples.append((int(data_addr, 0), (int(data_value, 0))))
    return data_tuples
  
  @staticmethod           
  def _return_dict(chunked_data):
    chunked_data_dict = []
    for data in chunked_data:
      chunked_data_dict.append(dict(data))
    return chunked_data_dict


def main():
  import argparse
  parser = argparse.ArgumentParser(description = 'Parses sensor data from warp transcript')
  parser.add_argument('transcript', help = 'Input transaction txt file')
  args = parser.parse_args()
  
  data_instance = TranscriptData(args.transcript)
  print(data_instance.sensor_name)
  print(data_instance.chunked_data)


if __name__ == "__main__":
  main()
