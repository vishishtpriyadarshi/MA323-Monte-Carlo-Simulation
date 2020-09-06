# ***************************Question 1***********************
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
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


print("a = 6, b = 0, c = 11:")
for i in range(0, 11):
    print("seed =", i, end=', ')
    print("Numbers =", end=' ')
    numbers = generator(6, 0, 11, i)
    print(numbers)

print()
print("a = 3, b = 0, c = 11:")
for i in range(0, 11):
    print("seed =", i, end=', ')
    print("Numbers =", end=' ')
    numbers = generator(3, 0, 11, i)
    print(numbers)


# ***************************Question 2***********************
import numpy as np 
import matplotlib.pyplot as plt  
from collections import OrderedDict

# if using a Jupyter notebook, include:
# %matplotlib inline


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
        # print(len(ui), end = ' ')

    return hashmap


for i in range(0, 5):
    hashmap = generator(1597, 5, 4944, i)
    # print("Total random numbers = ", len(numbers))
    hashmap = OrderedDict(sorted(hashmap.items())) 
    oldKeys = list(hashmap.keys())
    hashmap = dict((round(key*0.05, 2), value) for (key, value) in hashmap.items())

    x = list(hashmap.keys())
    y = list(hashmap.values())

    labels = ['0 - 0.05', '0.05 - 0.10', '0.10 - 0.15', '0.15 - 0.20', '0.20 - 0.25', '0.25 - 0.30', '0.30 - 0.35', '0.35 - 0.40', '0.40 - 0.45', '0.45 - 0.50', '0.50 - 0.55', '0.55 - 0.60', '0.60 - 0.65', '0.65 - 0.70', '0.70 - 0.75', '0.75 - 0.80', '0.80 - 0.85', ' 0.85 - 0.90', '0.90 - 0.95', '0.95 - 1']
    plt.figure(figsize=(18, 5))
    width = np.min(np.diff(oldKeys))/3
    plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

    hashmap = generator(51749, 5, 4944, i)
    # print("Total random numbers = ", len(numbers))
    hashmap = OrderedDict(sorted(hashmap.items())) 
    oldKeys = list(hashmap.keys())
    hashmap = dict((round(key*0.05, 2), value) for (key, value) in hashmap.items())

    x = list(hashmap.keys())
    y = list(hashmap.values())

    plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
    plt.xticks(oldKeys, labels, rotation='vertical')
    plt.legend(framealpha=1, frameon=True, loc='upper right')
    plt.xlabel("Ranges")
    plt.ylabel("Frequency")
    plt.title("Question 2 - Value of seed(x0) = {}".format(i))
    plt.show()


# ***************************Question 3***********************
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
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
print(x)
print(y)
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Question 3: Two Dimensional plot")
plt.show()
