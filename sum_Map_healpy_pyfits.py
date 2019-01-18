#! /usr/bin/env python
# -*- coding: utf-8 -*-

#####################################################################################################################
#####################################################################################################################
###                                       Summing up Healpy Flask + Foregrounds                                 #####
###                                                                                                             ##### 
###     Script for summing up Flask files and Foregrounds files                                                 #####  
###                                                                                                             #####
### Author: K. Fornazier                                                                                        #####
### DATE: January 2019                                                                                          #####
#####################################################################################################################
#####################################################################################################################

import healpy as hp
import matplotlib.pyplot as plt
import sys
import numpy as np
from astropy.io import fits as pyfits


##############################################################################
# Read maps from Flask
#############################################################################
map_flask = hp.read_map("map-f1z1.fits")
hp.mollview(map_flask)
map_flask.shape
plt.show()
#plt.savefig('map_flask.png')
pyfits.writeto('output/map_flask.fits', map_flask)

##############################################################################
# Read maps from Foregrounds
#############################################################################

#map_foregrounds0 = pyfits.getdata("foreground_cube_21cm_fore.fits")
#hp.mollview(map_foregrounds0[0, :], "foregrounds[0]")
#plt.show()
#pyfits.writeto('output/map_foregrounds0.fits', map_foregrounds0[0,:])


#map_foregrounds1 = pyfits.getdata("foreground_cube_21cm_fore.fits")
#hp.mollview(map_foregrounds1[1, :])
#plt.show()
#plt.savefig('map_foregrounds1')
#pyfits.writeto('output/map_foregrounds1.fits', map_foregrounds1)

#map_foregrounds2 = pyfits.getdata("foreground_cube_21cm_fore.fits")
#hp.mollview(map_foregrounds1[2, :])
#plt.show()
#plt.savefig('map_foregrounds1')
#pyfits.writeto('output/map_foregrounds2.fits', map_foregrounds2)

#map_foregrounds3 = pyfits.getdata("foreground_cube_21cm_fore.fits")
#hp.mollview(map_foregrounds1[3, :])
#plt.show()
#plt.savefig('map_foregrounds1')
#pyfits.writeto('output/map_foregrounds3.fits', map_foregrounds3)

#map_foregrounds4 = pyfits.getdata("foreground_cube_21cm_fore.fits")
#hp.mollview(map_foregrounds1[4, :])
#plt.show()
#plt.savefig('map_foregrounds1')
#pyfits.writeto('output/map_foregrounds4.fits', map_foregrounds4)

############################################################################
# Adding maps
############################################################################
############################################################################

Map = []
MapFile = []
MapVar = []
MapCount = 0

Map = pyfits.getdata("foreground_cube_21cm_fore.fits")
for i in range(0,49):
    hp.mollview(Map[i, :], "Foregrounds")
    #plt.show()
    MapVar.append('Map[i,:]'.format(MapCount))
    MapCount = MapCount + 1

plt.show(MapVar, 'hist')

##############################################################################
# A partir daqui está ERRADO
#############################################################################
############################################################################3


#pyfits.writeto('output/map_total_50.fits', MapVar)

mtot = map_flask + MapVar
hp.mollview(mtot)
plt.show()
pyfits.writeto('output/maptot.fits', mtot)
