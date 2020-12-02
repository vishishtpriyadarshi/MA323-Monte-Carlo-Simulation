"""
Kindly install these libraries before executing this code:
  1. numpy
"""

import math
import numpy as np


def generate_random_numbers():
  np.random.seed(42)
  normal_random_numbers = np.random.normal(0, 1, 300*1000)

  return normal_random_numbers

  
def compute_sample_path(S0, mu, sigma, normal_random_numbers, delta, init):
  S = [S0]
  S_prev = S0

  for idx in range(0, 300):
    Z = normal_random_numbers[init + idx]      
    S_next = S_prev*math.exp((mu - 0.5*sigma*sigma)*delta + sigma*math.sqrt(delta)*Z)
    S.append(S_next)
    S_prev = S_next

  return S


def plot_graph(S):
  x = range(0, 301)
  plt.plot(x, S) 
  plt.xlabel("Time points (t)")
  plt.ylabel("S(t)")
  plt.title("Path of S(t)")
  plt.show()


def part1():
  # Default values & Initialisation
  S0 = 185.40	
  mu = 0.00029810607002
  sigma = math.sqrt(0.000496475360719)
  delta = 0.1   #  = 30/300
  K = 1.1*S0
  M = 1000
  r = 0.04
  t = 30/365

  # Generate random numbers
  normal_random_numbers = generate_random_numbers()
  
  # Generate the sample path
  payoff = []

  for i in range(0, M):
    S = compute_sample_path(S0, mu, sigma, normal_random_numbers, delta, i*300)

    sum = 0
    for s in S:
      sum += s
    sum /= len(S)

    payoff.append(max(K - sum, 0)*math.exp(-r*t))

  mu = np.mean(payoff)
  sigma = np.std(payoff)

  confidence_level1 = mu - (1.96*sigma)/math.sqrt(M)
  confidence_level2 = mu + (1.96*sigma)/math.sqrt(M)
  print("mu \t\t\t = {}\nsigma\t\t\t = {}\nConfidence Level\t = [{}, {}]".format(mu, sigma, confidence_level1, confidence_level2));


def part2():
  S0 = 185.40	
  mu = 0.00029810607002
  sigma = math.sqrt(0.000496475360719)
  delta = 0.1   #  = 30/300
  K = 1.1*S0
  M = 1000
  r = 0.04
  t = 30/365

  # Generate random numbers
  normal_random_numbers = generate_random_numbers()
  
  # Generate the sample path
  Y = []
  X = []
  for i in range(0, M):
    S = compute_sample_path(S0, mu, sigma, normal_random_numbers, delta, i*300)

    sum = 0
    for s in S:
      sum += s
    sum /= len(S)

    Y.append(max(K - sum, 0)*math.exp(-r*t))
    X.append(max(K - S[len(S) - 1], 0)*math.exp(-r*t))
  
  b = 0
  X_bar = np.mean(X)
  Y_bar = np.mean(Y)
  num = 0
  denom = 0
  for idx in range(0, len(X)):
    num += (X[idx] - X_bar)*(Y[idx] - Y_bar)
    denom += (X[idx] - X_bar)*(X[idx] - X_bar)

  b = num/denom
  Y_b = []

  for idx in range(0, len(X)):
    Y_b.append((Y[idx] - b*(X[idx] - X_bar)*math.exp(-r*t)))

  mu = np.mean(Y_b)
  sigma = np.std(Y_b)

  confidence_level1 = mu - (1.96*sigma)/math.sqrt(M)
  confidence_level2 = mu + (1.96*sigma)/math.sqrt(M)
  print("mu \t\t\t = {}\nsigma\t\t\t = {}\nConfidence Level\t = [{}, {}]".format(mu, sigma, confidence_level1, confidence_level2));


def main():
  print("************Part 1************")
  part1()

  print("\n\n************Part 2************")
  part2()
  

if __name__=="__main__":
    main()