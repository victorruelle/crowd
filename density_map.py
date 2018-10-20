import numpy as np
from global_variables import walls
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

dx=0.1
Obs1b = [ [ (4.5/dx,5/dx) , 0.7/dx] , [ (4.5/dx,2.5/dx) , 0.7/dx ] ]

walls_dx = []
for wall in walls:
    walls_dx.append([])
    for point in wall:
        point_dx = ( point[0]/dx , point[1]/dx )
        walls_dx[-1].append(point_dx)


def adaptX(X):
    A=[]
    B=[]
    for i in range(len(X)):
        p=X[i][0]
        x,y=p.position()
        y+=1
        A.append(x)
        B.append(y)
    return np.array(A),np.array(B)
    
def dMap(X):
    x,y=adaptX(X)
   
    # Calculate the point density
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)
    
    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    
    fig, ax = plt.subplots()
    ax.scatter(x, y, c=z, s=50, edgecolor='')
    plt.show()