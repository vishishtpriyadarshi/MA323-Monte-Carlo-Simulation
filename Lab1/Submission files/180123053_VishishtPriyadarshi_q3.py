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

    print("length =", len(xi))
    return ui


x = generator(1229, 1, 2048, 1)
y = generator(1229, 1, 2048, 1)

del x[len(x) - 1]
del y[0]
print("x = ", end=' ')
print(x)
print("y = ", end=' ')
print(y)
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Question 3: Two Dimensional plot")
plt.show()