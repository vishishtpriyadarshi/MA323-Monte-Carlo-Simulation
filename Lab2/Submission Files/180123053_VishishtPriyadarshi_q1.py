""" 
Kindly install these libraries before executing this code:
	1. numpy
	2. matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# if using a Jupyter notebook, kindly uncomment following line:
# %matplotlib inline

def generator1(a, b, m, seed):
    x = seed
    ui = list()
    xi = list()
    while True:
        x = (a * x + b) % m
        u = x/m
        if x in xi or u in ui:
            break

        if(x == 0):
            continue
        xi.append(x)
        ui.append(u)

    # print("length =", len(xi))
    return ui

def generator2(limit, U):
  idx = len(U)
  limit -= 17
  for i in range(1, limit + 1):
    x = U[idx - 17] - U[idx - 5]
    
    if x < 0:
      x += 1

    U.append(x)
    idx += 1

  return U
    
def solve(a, b, m, seed, limit):
  sequence1 = generator1(a, b, m, seed)
  sequence2 = generator1(a, b, m, seed)
  x = generator2(limit, sequence1[0: 17])
  y = generator2(limit, sequence2[0: 17])

  # print(len(x), len(y))
  plt.title("Question 1: Frequency Distribution plot for total no of values = {}".format(limit))
  plt.hist(x, bins=np.arange(min(x), max(x)+0.001, 0.01))
  plt.xlabel("Ui")
  plt.ylabel("Frequency")
  plt.show()

  x_bar = np.arange(0, limit)
  # print(len(x_bar), len(y))
  plt.bar(x_bar, y, color='green', width=0.8) 
  plt.xlabel("i")
  plt.ylabel("U_i")
  plt.title("Question 1: Bar plot for total no of values = {}".format(limit))
  plt.show()

  del x[len(x) - 1]
  del y[0]

  fig, ax = plt.subplots()
  ax.scatter(x, y, alpha=0.5)
  plt.xlabel("X axis")
  plt.ylabel("Y axis")
  plt.title("Question 1: Scatter plot for total no of values = {}".format(limit))
  plt.show()

  

  

solve(1229, 1, 2048, 1, 1000)
solve(1229, 1, 2048, 1, 10000)
solve(1229, 1, 2048, 1, 100000)

