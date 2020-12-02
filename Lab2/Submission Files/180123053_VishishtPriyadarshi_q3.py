""" 
Kindly install these libraries before executing this code:
  1. numpy
  2. matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

# if using a Jupyter notebook, kindly uncomment following line:
# %matplotlib inline

samples = [1000, 10000, 100000, 1000000, 10000000]

for data_points in samples:
  np.random.seed(42)
  sequence = random.uniform(size=data_points) 
  print(len(sequence))

  X = list()
  for i in sequence:
    val = 0.5 - 0.5*math.cos(i*cmath.pi)
    X.append(val)

  sorted_Y = np.sort(X)
  y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
  
  plt.title('Distribution Function of X ( sample count = {} )'.format(data_points))
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(sorted_Y, y_val, color='blue')
  plt.show()

  plt.title('Frequency Distribution of X ( sample count = {} )'.format(data_points))
  counts, bin_edges = np.histogram(X, bins=np.arange(min(X), max(X)+0.001, 0.01))
  plt.ylabel('Frequency')
  plt.xlabel('X (generated values)')
  plt.plot(bin_edges[1:], counts)
  plt.show()


  print("Sample count =", data_points)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()


x = np.arange(0, 1.001, 0.01)
Fx = [(2/cmath.pi)*math.asin(math.sqrt(i)) for i in x]

plt.plot(x, Fx, color='red')
plt.title('Actual Distribution Function')
plt.ylabel('F (x) ')
plt.xlabel('x')
plt.show()