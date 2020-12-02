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
%matplotlib inline

def fx(i):
  return 20*i*math.pow(1 - i, 3)

def plot_graph(numbers):
  x = np.arange(0, 1, 0.01)
  Fx = [10*i*i - 20*math.pow(i, 3) + 15*math.pow(i, 4) - 4*math.pow(i, 5) for i in x]
  plt.plot(x, Fx, color = 'red', label = "CDF")

  sorted_Y = np.sort(numbers)
  y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
  
  plt.title('Distribution Function of X plotted along with the CDF - Convergence Analysis')
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(sorted_Y, y_val, color = 'blue', label = "generated X")
  plt.legend(loc = "upper left")
  plt.show()

  x = np.arange(0, 1, 0.01)
  pdf = [fx(i) for i in x]
  plt.plot(x, pdf, color = 'red', label = "PDF")
  plt.title('Density function comparison')
  counts, bin_edges = np.histogram(numbers, bins = 50)

  max_len = 0
  for i in counts:
    max_len = max(max_len, i)
    
  counts = [i*2.109375/max_len for i in counts]
  plt.ylabel('f(X)')
  plt.xlabel('X (generated values)')
  plt.plot(bin_edges[1:], counts, color = 'blue', label = "generated PDF")
  plt.legend(loc = "upper left")
  plt.show()

  plt.title('Frequency Distribution of X - Histograms')
  hist, bins = np.histogram(numbers, bins = 50)
  w = 0.7 * (bins[1] - bins[0])
  center = (bins[:-1] + bins[1:]) / 2
  plt.bar(center, hist, align = 'center', width = w)
  plt.ylabel('Frequency')
  plt.xlabel('X (generated values)')
  plt.show()

def main(): 
  x = np.arange(0, 1, 0.001)
  f = [fx(i) for i in x]
  C = [max(f), 15, 30]
  
  """
  f(x) =  1  if x in [a, b]  or  0, otherwise
  F(x) = (x - a)/(b - a)

  Generate a random number U
  X = a + U*(b - a)

  Here, X    = 0 + U*(1 - 0) = U
        F(x) = x
  """

  for c in C:
    iter = 0
    numbers = list()
    sample_c = list()

    while iter <= 10000:
      limit = 1000
      X = np.random.uniform(size = limit)
      U = np.random.uniform(size = limit)
      
      idx = 0
      counter = 0
      for i in X:
        ui = U[idx]
        if(ui <= fx(i) / c):
          numbers.append(i)
        else:
          break

        idx += 1
        counter += 1

      iter += 1
      if(counter > 0):
        sample_c.append(counter)

    print("Actual c = {}\nSample c = {}".format(c, sum(sample_c)/len(sample_c)))
    print(len(numbers))
    plot_graph(numbers)
  
  

if __name__ == "__main__": 
    main() 