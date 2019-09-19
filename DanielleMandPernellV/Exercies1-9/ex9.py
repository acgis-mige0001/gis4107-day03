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

km = 100
miPerGal = 35
kmPerL = 14.88
DolPerL = 1.30
cost = (km/kmPerL) * (DolPerL)


print (str(km) + " km at " + str(miPerGal) + " mi/gal" + " and $"
+ "{:.2f}".format(DolPerL) + " per L will cost $" + "{:.2f}".format(cost))