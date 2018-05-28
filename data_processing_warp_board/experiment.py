#!/usr/bin/env python3
from collections.abc import Iterable
from glob import glob
import csv
import os
from itertools import groupby
from data_from_raw import ProcessCalc
from warpParser import TranscriptData

class MeasurementRun:
  def __init__(self, dataset_id, sensor_file, power_file):
    self.dataset_id = dataset_id
    self.ts = TranscriptData(sensor_file)
    self.sensor_name = self.sensor_name() #check this is valid? Otherwise have to put run.sensor_name() in stat_gen
    self.sensor_data = ProcessCalc(self.ts.chunked_data_dict, self.ts.sensor_name)
    self.power = self.read_power_csv(power_file)
    self.chamber_temp, self.voltage, self.repetition = self.name_info(dataset_id)

  @classmethod
  def from_dataset_files(cls, dataset_id, dataset_files):
    sensor_file = None
    power_file = None
    for f in dataset_files:
      if "sensor" in f:
        sensor_file = f
      if "power" in f:
        power_file = f
    if sensor_file is None:
      raise Exception("Could not find 'sensor' file for run '{}'".format(dataset_id))
    if power_file is None:
      raise Exception("Could not find 'power' file for run '{}'".format(dataset_id))
      
    return cls(dataset_id, sensor_file, power_file)

  def __repr__(self):
    return "MeasurementRun({}, {})".format(self.dataset_id, self.sensor_name())

  def sensor_name(self):
    return self.ts.sensor_name
      
  @staticmethod
  def read_power_csv(power_file):
    with open(power_file) as csvfile:
      reading_power = csvfile.readlines()[100:] #this skips the first 100 lines as before this point sensor may not be on
      readCSV = csv.reader(reading_power, delimiter=',')
      powers = []
      for row in readCSV:
        power = row[1] #date and time are just one thing when delimit with commas.
        powers.append(float(power))
    return powers
  
  @staticmethod
  def name_info(dataset_id):
    split_name = dataset_id.split('-')
    chamber_temp = split_name[2]
    voltage = split_name[1]
    repetition = split_name[-1]
    return chamber_temp, voltage, repetition
    

class Experiment(Iterable):
  def __init__(self, data):
    self.measurement_runs = data
    if not all(run.sensor_name == next(iter(self)).sensor_name for run in self):
      raise Exception("Sensor names did not match. Data may be invalid")

  @classmethod
  def dir_input(cls, directory):
    measurement_runs = []
    filenames = glob("{}/data-*".format(directory))
    filenames.sort(key=cls._dataset_id_key)
    for ds_id, ds_files in groupby(filenames, key=cls._dataset_id_key):
      measurement_runs.append(MeasurementRun.from_dataset_files(ds_id, ds_files))
    return cls(measurement_runs)

  @classmethod
  def file_input(cls, files):
    measurement_runs = []
    name_id = cls._dataset_id_key(files[0])
    if not all(cls._dataset_id_key(file) == name_id for file in files):
      raise Exception("file names did not match. Data may be invalid")
    measurement_runs.append(MeasurementRun.from_dataset_files(name_id, files))
    return cls(measurement_runs)

  @staticmethod
  def _dataset_id_key(filename):
    return os.path.basename(filename).split(".")[0]

  def __iter__(self):
    return iter(self.measurement_runs)
