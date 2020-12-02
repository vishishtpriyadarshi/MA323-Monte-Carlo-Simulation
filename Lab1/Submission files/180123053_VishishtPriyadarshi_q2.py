""" 
Kindly install these libraries before executing this code:
    1. numpy
    2. matplotlib
"""

import numpy as np 
import matplotlib.pyplot as plt  
from collections import OrderedDict
# if using a Jupyter notebook, kindly uncomment following line:
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


labels = ['0 - 0.05', '0.05 - 0.10', '0.10 - 0.15', '0.15 - 0.20', '0.20 - 0.25', '0.25 - 0.30', '0.30 - 0.35', '0.35 - 0.40', '0.40 - 0.45', '0.45 - 0.50', '0.50 - 0.55', '0.55 - 0.60', '0.60 - 0.65', '0.65 - 0.70', '0.70 - 0.75', '0.75 - 0.80', '0.80 - 0.85', ' 0.85 - 0.90', '0.90 - 0.95', '0.95 - 1']




#           Case (i):  Seed (x0) = 1

hashmap1 = generator(1597, 1, 244944, 1)
# print("Total random numbers = ", len(numbers))
hashmap1 = OrderedDict(sorted(hashmap1.items())) 
oldKeys = list(hashmap1.keys())
hashmap1 = dict((round(key*0.05, 2), value) for (key, value) in hashmap1.items())

x = list(hashmap1.keys())
y = list(hashmap1.values())

plt.figure(figsize=(18, 5))
width = np.min(np.diff(oldKeys))/3
plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

hashmap2 = generator(51749, 1, 244944, 1)
# print("Total random numbers = ", len(numbers))
hashmap2 = OrderedDict(sorted(hashmap2.items())) 
oldKeys = list(hashmap2.keys())
hashmap2 = dict((round(key*0.05, 2), value) for (key, value) in hashmap2.items())

x = list(hashmap2.keys())
y = list(hashmap2.values())

plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
plt.xticks(oldKeys, labels, rotation='vertical')
plt.legend(framealpha=1, frameon=True, loc='upper right')
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.title("Question 2 - Value of seed(x0) = 1")
plt.show()
print()
print("a = 1597, hashmap1 : ")
for key, value in hashmap1.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)
print()
print("a = 51749, hashmap2 = ")
for key, value in hashmap2.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)




#           Case (ii):  Seed (x0) = 2

hashmap1 = generator(1597, 0, 244944, 2)
# print("Total random numbers = ", len(numbers))
hashmap1 = OrderedDict(sorted(hashmap1.items())) 
oldKeys = list(hashmap1.keys())
hashmap1 = dict((round(key*0.05, 2), value) for (key, value) in hashmap1.items())

x = list(hashmap1.keys())
y = list(hashmap1.values())

plt.figure(figsize=(18, 5))
width = np.min(np.diff(oldKeys))/3
plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

hashmap2 = generator(51749, 0, 244944, 2)
# print("Total random numbers = ", len(numbers))
hashmap2 = OrderedDict(sorted(hashmap2.items())) 
oldKeys = list(hashmap2.keys())
hashmap2 = dict((round(key*0.05, 2), value) for (key, value) in hashmap2.items())

x = list(hashmap2.keys())
y = list(hashmap2.values())

plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
plt.xticks(oldKeys, labels, rotation='vertical')
plt.legend(framealpha=1, frameon=True, loc='upper right')
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.title("Question 2 - Value of seed(x0) = 2")
plt.show()
print()
print("a = 1597, hashmap1 : ")
for key, value in hashmap1.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)
print()
print("a = 51749, hashmap2 = ")
for key, value in hashmap2.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)




#           Case (iii):  Seed (x0) = 3

hashmap1 = generator(1597, 1, 244944, 3)
# print("Total random numbers = ", len(numbers))
hashmap1 = OrderedDict(sorted(hashmap1.items())) 
oldKeys = list(hashmap1.keys())
hashmap1 = dict((round(key*0.05, 2), value) for (key, value) in hashmap1.items())

x = list(hashmap1.keys())
y = list(hashmap1.values())

plt.figure(figsize=(18, 5))
width = np.min(np.diff(oldKeys))/3
plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

hashmap2 = generator(51749, 1, 244944, 3)
# print("Total random numbers = ", len(numbers))
hashmap2 = OrderedDict(sorted(hashmap2.items())) 
oldKeys = list(hashmap2.keys())
hashmap2 = dict((round(key*0.05, 2), value) for (key, value) in hashmap2.items())

x = list(hashmap2.keys())
y = list(hashmap2.values())

plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
plt.xticks(oldKeys, labels, rotation='vertical')
plt.legend(framealpha=1, frameon=True, loc='upper right')
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.title("Question 2 - Value of seed(x0) = 3")
plt.show()
print()
print("a = 1597, hashmap1 : ")
for key, value in hashmap1.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)
print()
print("a = 51749, hashmap2 = ")
for key, value in hashmap2.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)




#           Case (iv):  Seed (x0) = 4

hashmap1 = generator(1597, 1, 244944, 4)
# print("Total random numbers = ", len(numbers))
hashmap1 = OrderedDict(sorted(hashmap1.items())) 
oldKeys = list(hashmap1.keys())
hashmap1 = dict((round(key*0.05, 2), value) for (key, value) in hashmap1.items())

x = list(hashmap1.keys())
y = list(hashmap1.values())

plt.figure(figsize=(18, 5))
width = np.min(np.diff(oldKeys))/3
plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

hashmap2 = generator(51749, 1, 244944, 4)
# print("Total random numbers = ", len(numbers))
hashmap2 = OrderedDict(sorted(hashmap2.items())) 
oldKeys = list(hashmap2.keys())
hashmap2 = dict((round(key*0.05, 2), value) for (key, value) in hashmap2.items())

x = list(hashmap2.keys())
y = list(hashmap2.values())

plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
plt.xticks(oldKeys, labels, rotation='vertical')
plt.legend(framealpha=1, frameon=True, loc='upper right')
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.title("Question 2 - Value of seed(x0) = 4")
plt.show()
print()
print("a = 1597, hashmap1 : ")
for key, value in hashmap1.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)
print()
print("a = 51749, hashmap2 = ")
for key, value in hashmap2.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)




#           Case (v):  Seed (x0) = 6

hashmap1 = generator(1597, 1, 244944, 6)
# print("Total random numbers = ", len(numbers))
hashmap1 = OrderedDict(sorted(hashmap1.items())) 
oldKeys = list(hashmap1.keys())
hashmap1 = dict((round(key*0.05, 2), value) for (key, value) in hashmap1.items())

x = list(hashmap1.keys())
y = list(hashmap1.values())

plt.figure(figsize=(18, 5))
width = np.min(np.diff(oldKeys))/3
plt.bar(oldKeys - 0.5*width, y, color='blue', width=0.3, ec='black', label='a = 1597') 

hashmap2 = generator(51749, 1, 244944, 6)
# print("Total random numbers = ", len(numbers))
hashmap2 = OrderedDict(sorted(hashmap2.items())) 
oldKeys = list(hashmap2.keys())
hashmap2 = dict((round(key*0.05, 2), value) for (key, value) in hashmap2.items())

x = list(hashmap2.keys())
y = list(hashmap2.values())

plt.bar(oldKeys + 0.5*width, y, color='green', width=0.3, ec='black', label='a = 51749') 
plt.xticks(oldKeys, labels, rotation='vertical')
plt.legend(framealpha=1, frameon=True, loc='upper right')
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.title("Question 2 - Value of seed(x0) = 6")
plt.show()
print()
print("a = 1597, hashmap1 : ")
for key, value in hashmap1.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)
print()
print("a = 51749, hashmap2 = ")
for key, value in hashmap2.items():
    print(key, ' - ', round(key + 0.05, 2) , ' = ', value)