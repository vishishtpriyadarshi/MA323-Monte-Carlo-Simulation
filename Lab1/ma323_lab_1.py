# -*- coding: utf-8 -*-
"""MA323 - Lab_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-MrB530qXsJD0Ja65gALBsqBM0pLvCPR

# Question - 1
"""

# Commented out IPython magic to ensure Python compatibility.
# import numpy as np
# import matplotlib.pyplot as plt
# # if using a Jupyter notebook, include:
# # %matplotlib inline

# def generator(a, b, m, seed):
#     x = seed
#     g = list()
#     while True:
#         x = (a * x + b) % m
#         if x in g:
#             break
#         g.append(x)

#     return g


# for i in range(0, 10):
#     numbers = generator(6, 0, 11, i)
#     print(numbers)
    # x = [*range(1, len(numbers) + 1, 1)] 
    # fig, ax = plt.subplots()
    # ax.scatter(x, numbers)
    # plt.show()

"""# Question 2"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np 
import matplotlib.pyplot as plt  
from collections import OrderedDict

# # if using a Jupyter notebook, include:
# # %matplotlib inline


def generator(a, b, m, seed):
    x = seed
    ui = list()
    xi = list()

    hashmap = dict()
    for i in range(0, 20):
        hashmap[i] = 0

    while True:
        x = (a * x + b) % m
        u = x/m
        if x in xi:
            break
        ui.append(u)
        xi.append(x)

        key = round(u*20) % 20
        hashmap[key] += 1
        print(len(ui), end = ' ')
    
    hashmap = OrderedDict(sorted(hashmap.items())) 
    oldKeys = list(hashmap.keys())
    hashmap = dict((round(key*0.05, 2), value) for (key, value) in hashmap.items())

    # x = list(hashmap.keys())
    x = list(hashmap.keys())
    y = list(hashmap.values())

    print(x)
    print(oldKeys)
    plt.bar(oldKeys, y, color ='blue', width = 0.6, ec = "black") 
  
    plt.xlabel("Ranges (Multiply by 0.05)") 
    plt.ylabel("Frequency") 
    plt.title("Question 2") 
    plt.show() 

    return ui

for i in range(4, 5):
  numbers = generator(1597, 51749, 244944, i)
  print("Total random numbers = ", len(numbers))


"""# Question 3
**Issues:**
1. Spectral test - multiple lines
2. Overflow issue causing period to increase
"""
# import numpy as np
# import matplotlib.pyplot as plt
# # if using a Jupyter notebook, include:
# # %matplotlib inline

# def generator(a, b, m, seed):
#     x = seed
#     ui = list()
#     xi = list()
#     while True:
#         x = (a * x + b) % m
#         u = x/m
#         if x in xi or u in ui:
#             break

#         if(x == 0):
#           continue
#         xi.append(x)
#         ui.append(u)

#     print("length = ", len(xi))
#     return ui


# x = generator(1229, 1, 2048, 1)
# y = generator(1229, 1, 2048, 1)

# del x[len(x) - 1] 
# del y[0]
# print(len(x), len(y))

# fig, ax = plt.subplots()
# ax.scatter(x, y, alpha = 0.5)
# plt.xlabel("X axis") 
# plt.ylabel("Y axis") 
# plt.title("Question 3") 
# plt.show()

                                        