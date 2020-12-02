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

def binary_search(q, ui):
  start = 0
  end = len(q) - 1

  while start < end:
    mid = math.floor((start + end)/2)
    if(ui <= q[mid]):
      end = mid
    else:
      start = mid + 1
  
  return start

def plot_graph(numbers, fx):
  
  hist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
  for i in numbers:
    hist[i] += 1

  for key, value in hist.items():
    hist[key] = value/len(numbers)
 
  x_axis = np.arange(1, 11)
  plt.bar(x_axis - 0.12, list(hist.values()), align = 'center', width = 0.3, label = 'Generated PDF')
  plt.bar(x_axis + 0.12, list(fx.values()), align = 'center', width = 0.3, label = 'Actual PDF')
  
  plt.legend(loc="upper left")
  plt.title('Probability Mass Function of X')
  plt.xlabel('Random Variable')
  plt.ylabel('Probabiltiy')
  plt.figure(figsize=(20,10))
  plt.show()


def main(): 
  fx = {1: 0.11, 2: 0.12, 3: 0.09, 4: 0.08, 5: 0.12, 6: 0.10, 7: 0.09, 8: 0.09, 9: 0.10, 10:0.10}
  RVs = np.arange(1, 11)
  C = [1.2, 10, 25]
  total_iterations = [1000, 2000, 5000, 10000, 25000, 50000]
  q = [i/10 for i in range (0, 11)]
  np.random.seed(42)

  for total_length in total_iterations:
    print("No of random numbers generated = {}".format(total_length))
    for c in C:
      iter = 0
      numbers = list()
      sample_c = list()

      while iter <= total_length:
        limit = 1000
        U_helper = np.random.uniform(size = limit)
        X = list()
        for ui in U_helper:
          idx = binary_search(q, ui)
          X.append(RVs[idx - 1])

        # print(X)
        U = np.random.uniform(size = limit)
        idx = 0
        counter = 0
        for i in X:
          ui = U[idx]
          if(ui <= fx[i] / c):
            numbers.append(i)
          else:
            break

          idx += 1
          counter += 1

        iter += 1
        if(counter > 0):
          sample_c.append(counter)

      if(len(sample_c) == 0):
        print("Actual c = {}\nSample c = {}".format(c, 0))
      else:
        print("Actual c = {}\nSample c = {}".format(c, sum(sample_c)/len(sample_c)))
      
      print("\nGenerated Probability - ")
      for i in RVs:
        ct = 0
        for j in numbers:
          if j == i:
            ct += 1

        if(len(numbers) == 0):
          print("P(X = {}) = {}".format(i, 0))
        else:
          print("P(X = {}) = {}".format(i, ct/len(numbers)))
      plot_graph(numbers, fx)
 

if __name__ == "__main__": 
    main() 