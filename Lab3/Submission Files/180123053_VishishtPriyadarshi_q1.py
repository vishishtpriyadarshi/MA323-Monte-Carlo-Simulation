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


def main(): 
  C = [i for i in range(1, 10000, 2)]
  q = [i/5000 for i in range(1, 5001)]

  sizes = [50000, 100000, 500000, 1000000, 5000000]
  for sz in sizes:
    # np.random.seed(42)
    U = random.uniform(size = sz) 

    X = list()
    for ui in U:
      idx = binary_search(q, ui)
      X.append(C[idx - 1])

    hist, bins = np.histogram(X, bins = 50)
    w = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align = 'center', width = w)
    plt.xlabel('Random Numbers (X)    (divided in intervals)')
    plt.ylabel('Frequency')
    plt.title('Frequency distribution of X - total count = {}'.format(sz))
    plt.show()

    freq = {}
    for i in C:
      freq[i] = 0
    for i in X:
      freq[i] += 1

    for key, value in freq.items():
      freq[key] = value/len(X)

    plt.bar(C, list(freq.values()), align = 'center', label = 'Actual PDF')
    plt.xlabel('Random Numbers (X)')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function of X - total count = {}'.format(sz))
    plt.show()
    
    # print(C)
    # print(q)
    # print(len(C), len(q))
    # print(len(X))
  
if __name__ == "__main__": 
    main() 