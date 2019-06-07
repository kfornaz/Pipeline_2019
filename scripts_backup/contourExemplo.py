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
import stats
import setupcov

def getArq(i,prefix):
    return prefix+str(i)+ext



def generateGraph(title,nomeArq,sb1,sb2,sb3,start,end):
    matrixf=open("B_ellTotal1234.txt") 
    matrixfbase=matrixf.readlines()
    matrix=np.array([i.split(",")[0] for i in (matrixfbase)])
    matrix_ell1=np.array([i.split(",")[1] for i in (matrixfbase)])
    matrix_ell2=np.array([i.split(",")[2] for i in (matrixfbase)])
    matrix_ell3=np.array([i.split(",")[3] for i in (matrixfbase)])
    matrix_ell23=np.array([abs(float(i.split(",")[2])-float(i.split(",")[3])) for i in (matrixfbase)])

    print(matrix_ell1)
    print(matrix_ell23)

    #ysize=matrix.shape[0]#get the x dimension form matrix shape
    #xsize=matrix.shape[1]#get the y dimension form matrix shape
   
    Y =matrix_ell1#matrix_ell1#set the x dimension form matrix shape   
    X =matrix_ell23#set the y dimension form matrix shape
    #xlen = len(X.size)
    #ylen = len(Y.size)    
    Z = matrix
    #print(matrix.shape)
  
    
    plt.subplot(sb1,sb2,sb3)    
    cp = plt.contourf(X, Y, Z,cmap=cm.YlOrRd)
    plt.colorbar(cp)
    plt.title(title)
    plt.xlabel('ell1')
    plt.ylabel('ell2-ell23')
    plt.set_zlim=(-6e-18,6e-18)
    
    
    mean=matrix.mean()
    std=matrix.std()
    max=np.amax(matrix)
    min=np.amin(matrix)
    print("Mean: "+str(mean))
    print("STD: "+str(std))
    print("Max: "+str(max))
    print("Min: "+str(min))
   
    


#load setup parameters
title='Bi Spectrum teste - Contours'

plt.figure(figsize=(21, 10))
generateGraph(title,"B_ellTotal1234.txt",1,1,1,0,1)
plt.show()






