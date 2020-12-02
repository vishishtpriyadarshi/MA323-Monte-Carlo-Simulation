"""
Kindly install these libraries before executing this code:
  1. numpy
"""

import math
import numpy as np
import csv


def readCSV():
    csv_file = open("data.csv", "r")
    reader = csv.reader(csv_file)

    data = []
    for row in reader:
        data.append(row[4])

    data = data[1:]
    data = [float(x) for x in data]
    return data


def compute(data):
    u = []
    for idx in range(1, len(data)):
        u.append(math.log(data[idx]/data[idx - 1]))

    E = 0
    variance = 0
    mean = 0
    n = len(u)

    for i in u:
        E += i
    E /= len(u)

    for i in u:
        variance += (i - E)*(i - E)
    variance /= (n - 1)

    mean = E + variance/2
    return mean, variance


def estimate(mean, variance, data):
    s0 = data[len(data) - 1]
    predicted = [0, 0, 0]

    for i in range(0, 1000):
        si = s0
        
        # Generating Normal Random Variables
        Z = np.random.normal(0, 1, 14)
        idx = 0

        
        # Computation for dates from 1st Oct to 7th oct
        # Holidays - 2nd Oct, 3rd Oct, 4th Oct
        for j in range(0, 4):
            s = si*math.exp((mean - 0.5*variance) + math.sqrt(variance)*Z[idx])
            si = s
            idx += 1
        predicted[0] += s

        
        # Computation for dates from 8th Oct to 14th Oct
        # Holidays - 10th Oct, 11th Oct
        for j in range(0, 5):
            s = si*math.exp((mean - 0.5*variance) + math.sqrt(variance)*Z[idx])
            si = s
            idx += 1
        predicted[1] += s

        
        # Computation for dates from 15th Oct to 21st Oct
        # Holidays - 17th Oct, 18th Oct
        for j in range(0, 5):
            s = si*math.exp((mean - 0.5*variance) + math.sqrt(variance)*Z[idx])
            si = s
            idx += 1
        predicted[2] += s

    for idx in range(0, 3):
        predicted[idx] /= 1000

    return predicted


def main():

    # Reading from csv files
    data = readCSV()

    # Computing mean and variance from historical data
    mean, variance = compute(data)

    print('Mean = {}'.format(mean))
    print('Variance = {}'.format(variance))

    # Making predictions using gBm Model
    predicted = estimate(mean, variance, data)
    actual = [190.70, 200.05, 203.75]
    percentageError = []

    # Calculating Percentage Error
    for idx in range(0, 3):
        percentageError.append(((actual[idx] - predicted[idx]) * 100)/actual[idx])

    print('\n------ Predicted closing stock prices ------')
    print('\n\n### Date = 7th Oct ###\n')
    print('Predicted price = {}'.format(predicted[0]))
    print('Actual Price = {}'.format(actual[0]))
    print('Percentage error = {} %'.format(percentageError[0]))

    print('\n\n### Date = 14th Oct ###\n')
    print('Predicted price = {}'.format(predicted[1]))
    print('Actual Price = {}'.format(actual[1]))
    print('Percentage error = {} %'.format(percentageError[1]))

    print('\n\n### Date = 21st Oct ###\n')
    print('Predicted price = {}'.format(predicted[2]))
    print('Actual Price = {}'.format(actual[2]))
    print('Percentage error = {} %'.format(percentageError[2]))



if __name__=="__main__":
    main()