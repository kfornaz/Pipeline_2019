########################################################################
##       This script is a test for summing up fits file             ####  
###                                                                 ####
### Author: K. Fornazier                                            ####
### DATE: October 2018                                              ####
########################################################################
########################################################################


import healpy as hp
from matplotlib import pyplot as plt
from astropy.io import fits as pyfits


#########################################################################
## total means here, the fits file with foreground fit  file + 21 cm fits
## file
#########################################################################
#total = pyfits.getdata('total.fits')

#########################################################################
## foreground  means fit file from  https://github.com/lolivari/foregrounds
#########################################################################

fore = pyfits.getdata('foreground_cube_21cm.fits')


#########################################################################
## below we have just a test to check if we can obtain the 21 cm fit file
#########################################################################

#recupera21= total - fore


#hp.mollview(recupera21[0, :], norm='hist')
#plt.show()


#########################################################################
## Get data from Flask File
#########################################################################

#flask1 = pyfits.getdata("map-f1z1.fits") # nf por npixels

#flask2 = pyfits.getdata("map-f1z2.fits") # nf por npixels

#flask3 = pyfits.getdata("map-f2z1.fits") # nf por npixels

flask4 = pyfits.getdata("map-f2z2.fits") # nf por npixels

#flask_total = flask1 + flask2 + flask3 + flask4


#hp.mollview(flask4[0, :], norm='hist')
#plt.show()

pyfits.writeto("fits", flask4)


#########################################################################
## summing up flask fits with foregrounds 
#########################################################################

total_fits = flask4 + fore

hp.mollview(total_fits[0, :], norm='hist')
plt.show()

pyfits.writeto("fits", total_fits)
