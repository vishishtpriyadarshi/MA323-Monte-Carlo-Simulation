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

# if using a Jupyter notebook, kindly uncomment following line:
%matplotlib inline

def fx(a1, a2, x):
  val = (1/beta(a1, a2))*math.pow(x, a1 - 1)*math.pow(1 - x, a2 - 1)
  return val


def main(): 
  a1 = [1, 2, 3, 4, 5]
  a2 = [5, 4, 3, 2, 1]
  iterations_count = [5000, 10000, 50000, 100000]


  for i in range(0, 5):
    x = (a1[i] - 1)/(a1[i] + a2[i] - 2)
    c = fx(a1[i], a2[i], x)

    print("\nCase {}: a1 = {}, a2 = {}".format(i + 1, a1[i], a2[i]))
    print("x* = ", x)
    print("c = ", c)

    for max_iter in iterations_count:
      iter = 0
      numbers = list()
      sample_c = list()

      while iter <= max_iter:
        limit = 10000
        X = np.random.uniform(size = limit)
        U = np.random.uniform(size = limit)
        
        idx = 0
        counter = 0
        for val in X:
          ui = U[idx]
          if(ui <= fx(a1[i], a2[i], val) / c):
            numbers.append(val)
          else:
            break

          idx += 1
        
        iter += 1
        
      
      plt.title('Frequency Distribution: a1 = {},  a2 = {}; Max iterations = {}'.format(a1[i], a2[i], max_iter))
      hist, bins = np.histogram(numbers, bins = 80)
      w = 0.7 * (bins[1] - bins[0])
      center = (bins[:-1] + bins[1:]) / 2
      plt.bar(center, hist, align = 'center', width = w)
      plt.ylabel('Frequency')
      plt.xlabel('X (generated values)')
      plt.show()

      sorted_Y = np.sort(numbers)
      y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)

      plt.title('CDF of generated Random Numbers: a1 = {},  a2 = {}; Max iterations = {}'.format(a1[i], a2[i], max_iter))
      plt.ylabel('Probability - P(X <= x)')
      plt.xlabel('X (generated values)')
      plt.plot(sorted_Y, y_val, color = 'blue')
      plt.show()
  

if __name__ == "__main__": 
    main() 