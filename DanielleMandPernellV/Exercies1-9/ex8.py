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

#Output = <dd>:<mm>:<ss.sss>
Degrees = 95.41805
dd = int(Degrees)
mm = int((Degrees - dd) * 60)
ss = (Degrees - dd - (float(mm)/60)) * 3600


print str(Degrees) + " = " + str(dd) + ":" + str(mm) + ":" + "{:.3f}".format(ss)