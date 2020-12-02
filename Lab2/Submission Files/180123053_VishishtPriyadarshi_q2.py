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

  theta = cmath.pi/2
  X = list()

  for i in sequence:
    val = -theta * math.log(1 - i)
    X.append(val)

  sorted_Y = np.sort(X)
  y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
  
  plt.title('Distribution Function of X ( sample count = {} )'.format(data_points))
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(sorted_Y, y_val, color='blue')
  plt.show()

  plt.title('Frequency Distribution of X ( sample count = {} )'.format(data_points))
  counts, bin_edges = np.histogram(X, bins=np.arange(min(X), max(X)+1, 0.1))
  plt.ylabel('Frequency')
  plt.xlabel('X (generated values)')
  plt.plot(bin_edges[1:], counts)
  plt.show()

  print("Sample count =", data_points)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()


x = np.arange(0, 25, 0.01)
Fx = [1 - math.exp(-i/theta) for i in x]

plt.plot(x, Fx, color='red')
plt.title('Actual Distribution Function')
plt.ylabel('F (x) ')
plt.xlabel('x')
plt.show()

print("Theoretical Mean =", theta)
print("Theoretical Variance =", theta*theta)

