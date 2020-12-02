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


def marsagliaAndBray():
  sample = [50, 5000]
  random_numbers = []

  for i in sample:
    iter = 10
    for count in range(0, iter):
      X = []
      U1 = []
      U2 = []
      
      counter = 0
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
      
      random_numbers.append(Z)

      print("\n\n****************** Iteration - {} ******************".format( count + 1))
      print("Size of sample\t= {}".format(len(Z)))
      print("Proportion of value rejected\t= {}".format(1 - len(Z)/(2*counter)))
      print("Theoretical value\t= {}".format(1 - math.pi/4))

    count += 1
   


def main(): 
  print(" ---------------------- Solutions for sample from N(0, 1) ----------------------")
  marsagliaAndBray()  



if __name__ == "__main__": 
    main() 