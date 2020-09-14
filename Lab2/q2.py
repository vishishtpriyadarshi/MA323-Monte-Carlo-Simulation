import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from numpy import random

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

  
# def cdf1(data):
#     data_size=len(data)

#     # Set bins edges
#     data_set=sorted(set(data))
#     bins=np.append(data_set, data_set[-1]+1)

#     # Use the histogram function to bin the data
#     counts, bin_edges = np.histogram(data, bins=bins, density=False)

#     counts=counts.astype(float)/data_size

#     # Find the cdf
#     cdf = np.cumsum(counts)

#     # Plot the cdf
#     plt.plot(bin_edges[0:-1], cdf, linestyle='--', marker="o", color='b')
#     plt.ylim((0,1))
#     plt.ylabel("CDF")
#     plt.grid(True)

#     plt.show()


# def cdf2(data):
#   sorted_Y = np.sort(data)
#   y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
#   print(len(y_val))
#   plt.plot(sorted_Y, y_val, color='blue')
#   plt.show()


samples = [100, 1000, 10000, 100000, 1000000, 10000000]

for data_points in samples:
  sequence = generator1(1229, 1, 2048, 1)
  sequence = generator2(data_points, sequence[0: 17])

  theta = cmath.pi
  X = list()

  for i in sequence:
    val = -theta * math.log(1 - i)
    X.append(val)

  x = np.arange(0, 25, 0.01)
  Fx = [1 - math.exp(-i/theta) for i in x]

  # plt.plot(x, Fx, color='red')
  # plt.title('CDF of Fx')
  # plt.show()

  # data = X
  # sorted_Y = np.sort(data)
  # y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
  # print(len(data))
  # print(y_val)
  # plt.title('CDF of X')
  # plt.plot(sorted_Y, y_val, color='blue')
  # plt.show()

  # plt.title('Frequency Distribution of X - using Histogram')
  # plt.hist(data, bins=np.arange(min(data), max(data)+1, 0.1))
  # plt.show()

  # plt.title('Frequency Distribution of X - using Smooth curve')
  # counts, bin_edges = np.histogram(data, bins=np.arange(min(data), max(data)+1, 0.1))
  # plt.plot(bin_edges[1:], counts)
  # plt.show()

  print("Sample count =", data_points)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()

print()
print("Inbuit Function Used -\n")

for data_points in samples:
  sequence = random.uniform(size=data_points) 

  theta = cmath.pi
  X = list()

  for i in sequence:
    val = -theta * math.log(1 - i)
    X.append(val)

  x = np.arange(0, 25, 0.01)
  Fx = [1 - math.exp(-i/theta) for i in x]

  # plt.plot(x, Fx, color='red')
  # plt.title('CDF of Fx')
  # plt.show()

  # data = X
  # sorted_Y = np.sort(data)
  # y_val = np.arange(len(sorted_Y))/float(len(sorted_Y) - 1)
  # print(len(data))
  # print(y_val)
  # plt.title('CDF of X')
  # plt.plot(sorted_Y, y_val, color='blue')
  # plt.show()

  # plt.title('Frequency Distribution of X - using Histogram')
  # plt.hist(data, bins=np.arange(min(data), max(data)+1, 0.1))
  # plt.show()

  # plt.title('Frequency Distribution of X - using Smooth curve')
  # counts, bin_edges = np.histogram(data, bins=np.arange(min(data), max(data)+1, 0.1))
  # plt.plot(bin_edges[1:], counts)
  # plt.show()

  print("Sample count =", data_points)
  print("Mean =", np.mean(X))
  print("Variance =", np.var(X))
  print()

print("Theoretical Mean =", theta)
print("Theoretical Variance =", theta*theta)