""" 
Kindly install these libraries before executing this code:
  1. numpy
  2. matplotlib
  3. scipy
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath 
import math 
from scipy import stats
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# if using a Jupyter notebook, kindly uncomment following line:
%matplotlib inline



def genRandomNumbers(a):
  Z1 = np.random.normal(0, 1, 1000)
  Z2 = np.random.normal(0, 1, 1000)

  X1 = []
  for idx in range(0, len(Z1)):
    X1.append(5 + Z1[idx])

  X2 = []
  for idx in range(0, len(Z1)):
    X2.append(8 + 2*a*Z1[idx] + math.sqrt(1 - a*a)*2*Z2[idx])

  return X1, X2



def plot3D(X1, X2, a):
  x = np.array(X1)  
  y = np.array(X2)

  fig = plt.figure()          
  ax = fig.add_subplot(111, projection='3d')

  hist, xedges, yedges = np.histogram2d(x, y, bins = (30, 30))
  xpos, ypos = np.meshgrid(xedges[:-1] + xedges[1:], yedges[:-1] + yedges[1:])

  xpos = xpos.flatten()/2.
  ypos = ypos.flatten()/2.
  zpos = np.zeros_like (xpos)

  dx = xedges [1] - xedges [0]
  dy = yedges [1] - yedges [0]
  dz = hist.flatten()

  cmap = cm.get_cmap('jet') 
  max_height = np.max(dz) 
  min_height = np.min(dz)
 
  col = [cmap((k-min_height)/max_height) for k in dz] 

  ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color = col, zsort = 'average')
  plt.title("Frequency of Generated values for a = {}".format(a))
  plt.xlabel("Z1")
  plt.ylabel("Z2")
  plt.show()
 
  

def actualDensity(mu_x, mu_y, variance_x, variance_y, cov):
  x = np.linspace(2, 8, 1000)
  y = np.linspace(2, 14, 1000)
  X, Y = np.meshgrid(x, y)
  pos = np.empty(X.shape + (2,))
  pos[:, :, 0] = X; pos[:, :, 1] = Y
  rv = multivariate_normal([mu_x, mu_y], [[variance_x, cov], [cov, variance_y]])


  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.plot_surface(X, Y, rv.pdf(pos), cmap = 'viridis', linewidth = 0)
  ax.set_xlabel('X1')
  ax.set_ylabel('X2')
  ax.set_zlabel('f(X)')
  plt.title('Actual Density for a = {}'.format(cov/2))
  plt.show()

  plt.contour(X, Y, rv.pdf(pos))
  plt.title('Contour plot of Multivariate Normal for a = {}'.format(cov/2))
  plt.xlim([2, 8])
  plt.ylim([3, 13])
  plt.xlabel('X axis')
  plt.ylabel('Y axis')
  plt.show()



def simulatedDensity(X1, X2, a):
  Z = []
  cov = np.array( [[1, 2*a], [2*a, 4]])
  u = np.array([5, 8])
  det = np.linalg.det(cov)

  for idx in range(0, len(X1)):
    x = np.array([X1[idx], X2[idx]])
    Z.append(1/(2*math.pi*math.sqrt(det)) * math.exp(-0.5*np.dot( np.dot(np.transpose(x - u), np.linalg.inv(cov)), (x - u))))

  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')
  ax.scatter(X1, X2, Z)
  ax.set_xlabel('X1')
  ax.set_ylabel('X2')
  ax.set_zlabel('f(X)')
  plt.title('Simulated Density for a = {}'.format(a))
  plt.show()

  

def marginalDensity(X, mean, var, rho, idx):
  x = np.arange(mean - 5, mean + 5, 0.1)
  y = stats.norm.pdf(x, mean, math.sqrt(var))
  plt.plot(x, y, color = 'red', label = 'Theoretical PDF')

  counts, bin_edges = np.histogram(X, bins = 150, density = 1)
  plt.title('Marginal Density - X{} for a = {}'.format(idx, rho))
  plt.ylabel('f(X)')
  plt.xlabel('X (generated values)')
  plt.plot(bin_edges[1:], counts, color = 'blue', label = "generated PDF")
  plt.legend(loc = "upper left")
  plt.show() 



def main(): 
  a = [-0.5, 0, 0.5, 1]
  num = 1

  for rho in a:
    X1, X2 = genRandomNumbers(rho)
    print('********************** Case {}: a = {} **********************\n'.format(num, rho))
    print('X1 : ')
    print(X1)
    print('Total no of Random numbers in X1 = {}'.format(len(X1)))
    print()
    print('X2 : ')
    print(X2)
    print('Total no of Random numbers in X2 = {}'.format(len(X2)))
    print()
    
    if rho != 1:
      plot3D(X1, X2, rho)
      simulatedDensity(X1, X2, rho)
      actualDensity(5, 8, 1, 4, 2*rho)  

    marginalDensity(X1, 5, 1, rho, 1)
    marginalDensity(X2, 8, 4, rho, 2)
    num += 1


if __name__ == "__main__": 
    main() 