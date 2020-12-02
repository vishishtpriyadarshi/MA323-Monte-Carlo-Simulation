"""
Kindly install these libraries before executing this code:
  1. numpy
"""

import numpy as np


N = [10, 20, 50, 100]

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


def calc_discrepancy(str):
  a = []

  if str == 'custom':
    a = LCG(1229, 1, 2048, 1, 1000)
  else:
    a = np.random.uniform(0, 1, 1000)

  for idx in range(0, len(N)):
    l = 0
    r = 1/N[idx]

    discrepancy = 0

    while(r <= 1):
      ct = 0
      for i in range(0, len(a)):
        if (a[i] >= l and a[i] <= r):
          ct += 1

      # print(ct, abs(ct/len(a) - 1/N[idx]))
      discrepancy = max(discrepancy, abs(ct/len(a) - 1/N[idx]))
      l += 1/N[idx]
      r += 1/N[idx]

    print("N = {}\tDiscrepancy = {}\n".format(N[idx], discrepancy))


def main():
  print("Results using custom LCG with a = 1229, b = 1, m = 2048, seed = 1:\n")
  calc_discrepancy('custom')

  print("\n\nResults using in-built LCG of python:\n")
  calc_discrepancy('in-built')


if __name__=="__main__":
  main()