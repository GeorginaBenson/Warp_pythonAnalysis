Setup to run data collection
============================

If you just want to run the data collection, first run `pip3 install --user -r requirements.txt`

## Setup to develop SMU driver

If you want to develop the SMU driver, clone the following repo somewhere else on your machine (outside of this repo):

https://bitbucket.org/georginabenson/bel-kit-drivers

And then run `pip3 install --user -e .` from within the clone. You can then modify and commit changes to the driver in its clone and the changes will be effective immediately in this repo.

Data processing process
=======================

## Human readable data generation

To generate data from the raw sensor output, run:

`./data_from_raw.py /path/to/sensor.txt`

This takes the sensor.txt file to be processed and outputs a list in the terminal of human readable data from the sensor

## Human readable data to statistical data

In the accelerations_warp_board directory run:

`./statistics_generator /path/to/csv/ /path/to/data/or/directory [opt --val_temp yy --test_temp zz]`

The `/path/to/data/or/directory` can be either 2 files (a sensor.txt file and the corresponding power.csv file, in no particular order) or at least one directory (there can be multiple different directories specified if desired)

`/path/to/csv` is the name of the csv that the data should be saved to.
It should be done in the following format:

stats-data-(V_yy(-yy))-(Te_zz(-zz))-issue-xxx(-xxx).csv

Where in this:

* yy is the temperatures to validate on (others are to train and test on). This should also be defined on the command line, although if it is not, the default temperature is 20 degrees. There can be 0 or more temperatures specified. If none are specified, but the --temp_val argument is called on the command line then all the data will be for training and testing. If this is the case, V_yy can be left out.

* xxx is the issue number that the data is coming from. This is also defined on the command line, as the name of the directory the data is coming from.

* zz is the temperatures to test on (others are for training and validation). This should also be defined on the command line, although if it is not, the default temperature is 24 degrees. There can be 0 or more temperatures specified. If none are specified, but the --temp_test argument is called on the command line then all the data will be for training and validation. If this is the case, Te_zz can be left out.


## Machine Learning

The files in this directory can be used to generate predictions of what the label of a measured sensor should be, based on the
statistics csv generated as described above.

#### classifier_decider.py
1. classifier_decider.py uses Scikit-learn and looks at multiple different classifiers to see which would be best to use to label the data correctly.
  It takes in a csv file that was generated as described above in the [Human readable data to statistical data](#human-readable-data-to-statistical-data) section.
  
1. It generates a score based on how well each classifier has perfomed using the validation data and also generates files with the saved state for each classifier.
   
#### sensor_classifier.py
1. sensor_classifier.py takes in a csv of statistical data, but only looks at the test data

1. It loads in the state of the desired classifier (for now uses Gaussian Naive_Bayes) and gives it a label based on the data it can see.

1. It has the option to take in unlabelled data.
  
  
