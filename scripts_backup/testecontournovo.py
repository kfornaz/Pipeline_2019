# encoding: utf-8
###########################################################################

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
import csv

def anuncio(msg):
    print(msg)
    print("\n")

Bell=[]
l1=[]
l2=[]
l3=[]
ls=[]
file= csv.reader("l_ell1_saida_loops2.txt")
print("li file arquivo")
reader=csv.reader(file, delimiter=',')
print("coloquei delimiter")

for i in range(0, 91):
       l1 =float(row[0])  
       anuncio(l1)                                                                                                                                                                               
       l2 =float(row[1])
       anuncio(l2)
       l3=float(row[2])
       anuncio(l3)
       Bell=float(row[3])                                                                                                                                                                                     
       anuncio(Bell)
       