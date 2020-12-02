"""
Kindly install these libraries before executing this code:
  1. numpy
  2. matplotlib
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def generate_random_numbers(lambd, delta):
  np.random.seed(42)
  normal_random_numbers = np.random.normal(0, 1, 4000)
  poisson_random_numbers = []

  for idx in range(0, 4):
    poisson_random_numbers.append(np.random.poisson(lambd[idx]*delta, 1000))

  return normal_random_numbers, poisson_random_numbers


def compute_M(N, mu, sigma):
  M = 0
  if N == 0:
    return M

  Z = np.random.normal(mu, sigma, N)
  for i in Z:
    M += i

  return M

  
def compute_sample_path(S0, mu, sigma, normal_random_numbers, poisson_random_numbers, init, delta):
  X = [math.log(S0)]
  X_prev = math.log(S0)

  for idx in range(0, 1000):
    Z = normal_random_numbers[init + idx]
    N = poisson_random_numbers[math.floor(init/1000)][idx]
    M = compute_M(N, mu, sigma)
      
    X_next = X_prev + (mu - 0.5*sigma*sigma)*delta + sigma*math.sqrt(delta)*Z + M
    X.append(X_next)
    X_prev = X_next

  S = [math.exp(i) for i in X]
  return S


def plot_graph(S, lambd):
  x = range(0, 1001)
  plt.plot(x, S) 
  plt.xlabel("Time points (t)")
  plt.ylabel("S(t)")
  plt.title("Path of S(t) for lambda = {}".format(lambd))
  plt.show()

  
def main():

  # Default values & Initialisation
  S0 = 185.40	
  mu = 0.00029810607002
  sigma = math.sqrt(0.000496475360719)
  lambd = [0.01, 0.05, 0.1, 0.2]
  delta = 4

  # Generate random numbers
  normal_random_numbers, poisson_random_numbers = generate_random_numbers(lambd, delta)
  
  # Generate and plot the sample path
  for i in range(0, 4):
    S = compute_sample_path(S0, mu, sigma, normal_random_numbers, poisson_random_numbers, i*1000, delta)
    plot_graph(S, lambd[i]) 


if __name__=="__main__":
    main()