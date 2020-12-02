""" 
Kindly install these libraries before executing this code:
  1. numpy
  2. matplotlib
  3. scipy
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random
from scipy.special import beta
from scipy import stats
import time

# if using a Jupyter notebook, kindly uncomment following line:
%matplotlib inline


def boxMuller():
  sample = [50, 5000]
  random_numbers = []

  for i in sample:
    iter = 50
    total_time = 0
    for count in range(0, iter):
      time1 = time.time()
      U1 = np.random.uniform(size = i)
      U2 = np.random.uniform(size = i)
      
      R = [-2*math.log(ui) for ui in U1]
      V = [2*math.pi*ui for ui in U2]

      Z = []
      for idx in range(0, i):
        Z.append(math.sqrt(R[idx]) * math.cos(V[idx]))
        Z.append(math.sqrt(R[idx]) * math.sin(V[idx]))

      time2 = time.time()
      random_numbers.append(Z)

      count += 1
      total_time += time2 - time1

    print("\n\n****************** Box-Muller Method ******************")
    print("Size of sample\t= {}".format(len(Z)))
    print("Time difference\t= {} sec".format(total_time/iter))
    
  return random_numbers



def marsagliaAndBray():
  sample = [50, 5000]
  random_numbers = []

  for i in sample:
    iter = 50
    total_time = 0
    for count in range(0, iter):
      X = []
      U1 = []
      U2 = []
      
      counter = 0
      time1 = time.time()
      while len(X) != i:
        u1 = np.random.random()
        u2 = np.random.random()

        counter += 1
        u1 = 2*u1 - 1
        u2 = 2*u2 - 1
        x = u1*u1 + u2*u2

        if(x > 1):
          continue

        X.append(x)
        U1.append(u1)
        U2.append(u2)

      Y = [math.sqrt(-2*math.log(x)/x) for x in X]

      Z = []
      for idx in range(0, i):
        Z.append(U1[idx]*Y[idx])
        Z.append(U2[idx]*Y[idx])
      
      time2 = time.time()
      random_numbers.append(Z)

      count += 1
      total_time += time2 - time1

    print("\n\n****************** Marsaglia and Bray Method ******************")
    print("Size of sample\t= {}".format(len(Z)))
    print("Time difference\t= {} sec".format(total_time/iter))
      
  return random_numbers



def main(): 
  print(" ---------------------- Solutions for sample from N(0, 1) ----------------------")
  sample1 = boxMuller()
  sample2 = marsagliaAndBray()

  

if __name__ == "__main__": 
    main() 