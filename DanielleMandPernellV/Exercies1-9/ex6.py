#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      elle.migeon
#
# Created:     10-09-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
bear_per_sqkm = 4
area_sq_m = 10000000
area_sq_km = area_sq_m / 1000
bears = bear_per_sqkm * area_sq_km
print "When bear density is " + str(bear_per_sqkm) + " bears / sq. km and area is " + str(area_sq_m) + " sq m, the probable number of bears is " + str(bears)

