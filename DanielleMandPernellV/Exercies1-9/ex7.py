#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pernell
#
# Created:     12-09-2019
# Copyright:   (c) Pernell 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

deg = 95
mins = 25
secs = 5
dd = (deg) + (float(mins)/60) + (float(secs)/3600)

# print(str(int(deg)) + ":" + str(int(mins)) + ":" + str(int(secs)) + " = " +
    #"{:.5f}".format(dd))
#(str(deg + float(mins)/60 + float(secs)/3600)))

print(str(deg) + ":" + str(mins) + ":" + str(secs) + " = " + "{:.5f}".format(dd))
