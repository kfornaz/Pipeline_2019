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
#import stats
#import setupcov

#def getArq(i,prefix):
    #return prefix+str(i)+ext



def generateGraph(title,nomeArq,sb1,sb2,sb3,start,end):
    matrixf=open("B_ellTotal1234.txt")#open file 
    matrixfbase=matrixf.readlines()#reads file line by line
    matrix_Bell=np.array([i.split(",")[0] for i in (matrixfbase)])#extract bells
    matrix_ell1=np.array([i.split(",")[1] for i in (matrixfbase)])#extracts ell1
    matrix_ell2=np.array([i.split(",")[2] for i in (matrixfbase)])#extracts ell2
    matrix_ell3=np.array([i.split(",")[3] for i in (matrixfbase)])#extracts ell3
    matrix_ell23=np.array([abs(float(i.split(",")[2])-float(i.split(",")[3])) for i in (matrixfbase)]) #subtracts l2-l3

       
   
    Y =matrix_ell1#matrix_ell1#set the x dimension form matrix shape 
    print(Y.max(), Y.min())  
    X =matrix_ell23#set the y dimension form matrix shape      
    print(X.max(), X.min())
    Z = matrix_Bell
    
  
    
    plt.subplot(sb1,sb2,sb3)    
    cp = plt.contourf(X, Y, Z,cmap=cm.inferno)
    plt.colorbar(cp)
    plt.title(title)
    plt.xlabel('ell1')
    plt.ylabel('ell2-ell23')
    plt.set_zlim=(-6e-18,6e-18)
    
    
    mean=matrix_Bell.mean()
    std=matrix_Bell.std()
    max=np.amax(matrix_Bell)
    min=np.amin(matrix_Bell)
    print("Mean: "+str(mean))
    print("STD: "+str(std))
    print("Max: "+str(max))
    print("Min: "+str(min))
   
    


#load setup parameters
title='Bi Spectrum teste - Contours'

#plt.figure(figsize=(21, 10))
#generateGraph(title,"B_ellTotal1234.txt",1,1,1,0,1)
#plt.show()






