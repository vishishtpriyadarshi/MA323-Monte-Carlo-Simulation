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


def plot(numbers, size, flag, mean = 0, var = 1):
  normalize = False
  if(flag):
    normalize = True
    plt.title('Density Function Comparison: Sample size = {}'.format(size))
  else:
    plt.title('Frequency Distribution: Sample size = {}'.format(size))

  hist, bins = np.histogram(numbers, bins = 80, normed = normalize)
  w = 0.7 * (bins[1] - bins[0])
  center = (bins[:-1] + bins[1:]) / 2
  plt.bar(center, hist, align = 'center', width = w, label = 'Sample PDF')
  if(flag == 0):
    plt.ylabel('Frequency')
  else:
    plt.ylabel('Probability (P(x))')
  plt.xlabel('X (generated values)')

  if(normalize):
    x = np.arange(mean - 7.5, mean + 7.5, 0.1)
    y = stats.norm.pdf(x, mean, math.sqrt(var))
    plt.plot(x, y, color = 'red', label = 'Theoretical PDF')
    plt.legend(loc = "upper left")
  
  plt.show()  



def plot_cdf(numbers, size):
  sorted_Y = np.sort(numbers)
  y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)

  plt.title('CDF of generated Random Numbers: Sample size = {}'.format(size))
  plt.ylabel('Probability - P(X <= x)')
  plt.xlabel('X (generated values)')
  plt.plot(sorted_Y, y_val, color = 'blue')
  plt.show()



def boxMuller():
  sample = [50, 5000]
  random_numbers = []

  for i in sample:
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

    print("\n\n****************** Box-Muller Method ******************")
    print("Theoretical Mean\t= 0")
    print("Theoretical Variance\t= 1") 
    print("Sample Mean\t= {}".format(np.mean(Z)))
    print("Sample Variance\t= {}".format(np.var(Z)))
    print("Size of sample\t= {}".format(len(Z)))
      
    plot(Z, len(Z), 0) 
    
  return random_numbers



def marsagliaAndBray():
  sample = [50, 5000]
  random_numbers = []

  for i in sample:
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

    print("\n\n****************** Marsaglia and Bray Method ******************")
    print("Theoretical Mean\t= 0")
    print("Theoretical Variance\t= 1")
    print("Sample Mean\t= {}".format(np.mean(Z)))
    print("Sample Variance\t= {}".format(np.var(Z)))
    print("Size of sample\t= {}".format(len(Z)))
      
    plot(Z, len(Z), 0)
      
  return random_numbers



def normal_dist(sample1, sample2, mean, var):
  
  std = math.sqrt(var)
  for i in range(0, 2):
    modified_dist = []
    for idx in range(0, len(sample1[i])):
      modified_dist.append(mean + std*sample1[i][idx])

    print("\n\n****************** Box-Muller Method ******************")
    print("Theoretical Mean\t= {}".format(mean))
    print("Theoretical Variance\t= {}".format(var))    
    print("Sample Mean\t= {}".format(np.mean(modified_dist)))
    print("Sample Variance\t= {}".format(np.var(modified_dist)))
    print("Size of sample\t= {}".format(len(modified_dist)))
    plot(modified_dist, len(modified_dist), 1, mean, var)
    plot_cdf(modified_dist, len(modified_dist))

  for i in range(0, 2):
    modified_dist = []
    for idx in range(0, len(sample2[i])):
       modified_dist.append(mean + std*sample2[i][idx])

    print("\n\n****************** Marsaglia and Bray Method ******************")
    print("Theoretical Mean\t= {}".format(mean))
    print("Theoretical Variance\t= {}".format(var))
    print("Sample Mean\t= {}".format(np.mean(modified_dist)))
    print("Sample Variance\t= {}".format(np.var(modified_dist)))
    print("Size of sample\t= {}".format(len(modified_dist)))
    plot(modified_dist, len(modified_dist), 1, mean, var)
    plot_cdf(modified_dist, len(modified_dist))
    


def main(): 
  print(" ---------------------- Solutions for sample from N(0, 1) ----------------------")
  sample1 = boxMuller()
  sample2 = marsagliaAndBray()

  print(" ---------------------- Solutions for sample from N(0, 5) ----------------------")
  normal_dist(sample1, sample2, 0, 5)

  print(" ---------------------- Solutions for sample from N(5, 5) ----------------------")
  normal_dist(sample1, sample2, 5, 5)
  


if __name__ == "__main__": 
    main() 