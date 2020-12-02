""" 
Kindly install these libraries before executing this code:
	1. numpy
	2. matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, kindly uncomment following line:
# %matplotlib inline


def generator(a, b, m, seed):
    x = seed
    xi = list()
    while True:
        x = (a * x + b) % m
        if x in xi:
            break
        xi.append(x)

    return xi


print("a = 6, b = 0, m = 11:")
for i in range(0, 11):
    print("seed =", i, end=', ')
    print("Numbers =", end=' ')
    numbers = generator(6, 0, 11, i)
    print(numbers)

print()
print("a = 3, b = 0, m = 11:")
for i in range(0, 11):
    print("seed =", i, end=', ')
    print("Numbers =", end=' ')
    numbers = generator(3, 0, 11, i)
    print(numbers)