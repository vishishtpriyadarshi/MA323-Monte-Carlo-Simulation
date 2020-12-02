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
    

def LCG(a, b, m, seed, limit):
  sequence = generator1(a, b, m, seed)
  x = generator2(limit, sequence[0: 17])
  
  return x


def VanDerCorputSeq(n, b):
  seq = []

  for i in range(0, n):
    base = np.base_repr(i, base = b)
    mult = b
    num = 0

    while len(base) != 0:
      # print(base, int(base[len(base) - 1]))
      num += (int (base[len(base) - 1] ))/mult
      mult *= b
      base = base[: len(base) - 1]

    seq.append(num)

  return seq


def plot1(x, y, n, str):
  if str == "Halton Sequence":
    plt.title('Halton sequence for n = {}'.format(n))
  else:
    plt.title('(x_i, x_i+1) for n = {} -> {}'.format(n, str))
    plt.ylabel('$x_{i+1}$')
    plt.xlabel('$x_{i}$')
  
  plt.scatter(x, y)
  plt.show() 


def plot2(x1, n, str):  
  a = 1229
  b = 1
  m = 2048
  seed = 1

  sequence = generator1(a, b, m, seed)
  x2 = generator2(n, sequence[0: 17])
  
  bins = np.linspace(0, 1, 100)
  plt.hist(x1, bins, density=True)
  plt.title('Sampled Distribution for n = {} -->  Van der Corput Sequence'.format(n))
  plt.show()

  plt.hist(x2, bins, density=True)
  plt.title('Sampled Distribution for n = {} -->  LCG'.format(n))
  plt.show()
 


def question1():
  seq_25 = VanDerCorputSeq(25, 2)
  print("First 25 values of the Van der Corput sequence:")
  print(seq_25)

  seq_1000_x = VanDerCorputSeq(1000, 2)
  seq_1000_y = VanDerCorputSeq(1000, 2)
  del seq_1000_x[999]
  del seq_1000_y[0]
  plot1(seq_1000_x, seq_1000_y, 1000, "Van der Corput sequence")


  seq_100 = VanDerCorputSeq(100, 2)
  plot2(seq_100, 100, "Van der Corput sequence")

  seq_100000 = VanDerCorputSeq(100000, 2)
  plot2(seq_100000, 100000, "Van der Corput sequence")


def question2():
  x = VanDerCorputSeq(12, 2)
  y = VanDerCorputSeq(12, 3)
  print(x)
  print(y)
  plot1(x, y, 12, "Halton Sequence")

  x = VanDerCorputSeq(100, 2)
  y = VanDerCorputSeq(100, 3)
  plot1(x, y, 100, "Halton Sequence")

  x = VanDerCorputSeq(100000, 2)
  y = VanDerCorputSeq(100000, 3)
  plot1(x, y, 100000, "Halton Sequence")


def main():
  question1()
  question2()


if __name__=="__main__":
  main()