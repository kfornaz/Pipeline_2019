from mpl_toolkits.mplot3d import Axes3D
from stats import getCovMatrix
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.stats import norm
import matplotlib
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from astropy.io import fits
from math import pi, sin, cos, sqrt, log, floor
from sympy.physics.wigner import gaunt
import sys


#load file and matrix
matrixf = np.loadtxt("B_ellTotal1234.txt", delimiter=',')
#print matrixf
matrix_Bell = matrixf[:,0]
matrix_ell1 = matrixf[:,1]
matrix_ell23 = matrixf[:,3]-matrixf[:,2]
print (matrix_ell23)

#matrix l1
Y =matrix_ell1#matrix_ell1#set the x dimension form matrix shape 
#print Y 
print (max(Y), min(Y))
a = Y.max()
b = np.min(Y)
print (a,b)
Yarr = np.arange(int(b),int(a)+1)
print (Yarr)

#matrix l2 - l3

X =matrix_ell23#matrix_ell1#set the x dimension form matrix shape 
#print X
print (max(X), min(X))
a = X.max()
b = np.min(X)
print (a,b)
Xarr = np.arange(int(b),int(a)+1)
print (Xarr)

sizex = Xarr.size
print (sizex)
print (Xarr.size)
Bellmatrix = np.zeros((Xarr.size,Yarr.size))
print (Bellmatrix)

for i in np.arange(matrix_Bell.size):    
    #print int(matrix_ell23[i]),int(matrix_ell1[i])
    Bellmatrix[int(matrix_ell1[i]),int(matrix_ell23[i])]=matrix_Bell[i]
    #Bellmatrix[]
#print (Bellmatrix)

cp = plt.contourf(Xarr, Yarr, Bellmatrix.T,cmap=cm.inferno )
print (Xarr.size, Bellmatrix[0,:].size)
#plt.colormap()
plt.colorbar(cp)
plt.title("Contour plot Bispectrum")
plt.xlabel('ell2-ell23')
plt.ylabel('ell1')
plt.set_zlim=(-6e-18,6e-18)
#plt.figure(figsize=(21, 10))
plt.show()
