"""
Kindly install these libraries before executing this code:
  1. numpy
  2. scipy
"""

import math
import numpy as np
from scipy.stats import norm


M = [100, 1000, 10000, 100000]


def generate_random_numbers(idx):
  np.random.seed(42)    
  random_nums = np.random.uniform(0, 1, M[idx])
  return random_nums


def simpleEstimator():
  for idx in range(0, 4):
    print("\n# Iteration - {}\t\tM = {}\n".format(idx + 1, M[idx]))

    Y = []
    random_nums = generate_random_numbers(idx)
    for i in range(0, M[idx]):
      Y.append(math.exp(math.sqrt(random_nums[i])))
    
    Z_delta = norm.ppf(0.05/2)
    s = np.var(Y)
    I_m = np.mean(Y)
    l = I_m + (Z_delta * math.sqrt(s))/math.sqrt(M[idx])
    r = I_m - (Z_delta * math.sqrt(s))/math.sqrt(M[idx])

    print("I_m \t\t\t= {}".format(I_m))
    print("Confidence Interval \t= [{}, {}]".format(l, r))
    print("variance \t\t= {}".format(s))


def antitheticVariateEstimator():
  for idx in range(0, 4):
    print("\n# Iteration - {}\t\tM = {}\n".format(idx + 1, M[idx]))

    Y = []
    Y_hat = []
    random_nums = generate_random_numbers(idx)

    for i in range(0, M[idx]):
      Y.append(math.exp(math.sqrt(random_nums[i])))
      Y_hat.append((math.exp(math.sqrt(random_nums[i])) + math.exp(math.sqrt(1 - random_nums[i])))/2)
    
    Z_delta = norm.ppf(0.05/2)
    s = np.var(Y_hat)
    I_m = np.mean(Y_hat) 
    l = I_m + (Z_delta * math.sqrt(s))/math.sqrt(M[idx])
    r = I_m - (Z_delta * math.sqrt(s))/math.sqrt(M[idx])

    print("I_m \t\t\t= {}".format(I_m))
    print("Confidence Interval \t= [{}, {}]".format(l, r))
    print("variance \t\t= {}".format(s))


def main():
  print("************ Part 1 ************")
  simpleEstimator()

  print("\n\n\n\n************ Part 2 ************")
  antitheticVariateEstimator()
  

if __name__=="__main__":
    main()