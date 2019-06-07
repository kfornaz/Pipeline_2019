# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D
#from stats import getCovMatrix
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

#load file and matrix - usou loadtxt para evitar problemas com int ou qq outra coisa nos numeros
#matrixf = np.loadtxt("B_ellTotal1234.txt", delimiter=',')
matrixf = np.loadtxt("B_ellTotalForegrounds18.txt", delimiter=',')
#carregou a matriz com os valores de Bell
matrix_Bell = matrixf[:,0] 
matrix_Bella = matrixf[:,0]
matrix_Bellt=np.concatenate((matrix_Bell, matrix_Bella), axis=0)
matrix_Bellt=matrix_Bellt.T #gambi que fiz... nao tem razao logica...


#carregou a matriz com os valores de l1
matrix_ell1 = matrixf[:,1]
matrix_ell1a = matrixf[:,1]
matrix_ell1t=np.concatenate((matrix_ell1, matrix_ell1a), axis=0)


#carregou a matriz com os valores de l2  e  l3 
matrix_ell2 = matrixf[:,2]
matrix_ell3 = matrixf[:,3]
matrixeq    = matrixf[:,3]
matrixeq1   = matrixf[:,2]

print matrix_ell2

print matrix_ell3

for i in range (len(matrix_ell2)):
    if matrix_ell2[i]== matrix_ell3[i]:
        matrixeq= matrix_ell2[i]
        matrixeq1= matrix_ell3[i]

        print matrixeq
        print matrixeq1


print matrixeq
print matrixeq1


matrix_equal=np.concatenate((matrixeq, matrixeq1), axis=0)
