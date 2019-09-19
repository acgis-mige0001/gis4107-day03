#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      elle.migeon
#
# Created:     17-09-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Converter
reload(Converter)

mi = 10
km = Converter.miles_to_km(mi)

print str(mi) + "{} mi = {:.4} km".format(mi, km)

km_per_hr = 100
m_per_s = Converter.kmPerHr_to_mPerSec(km_per_hr)
print "{} km/hr = {:.3} m/s".format(km_per_hr, m_per_s)

sq_m = 10000
hctr = Converter.sqmetres_to_hectares(sq_m)
print "{} sq.m = {} hectares".format(sq_m, hctr)

sq_m = 10000
acres = Converter.sqmetres_to_acres(sq_m)
print "{} sq.m = {:.3} acres".format(sq_m, acres)

acres = 2
edge_of_square = Converter.acres_to_edge_of_square(acres)
print "{} acres = {:.5} metres".format(acres, edge_of_square)

area_sq_m = 10000000
bear_per_sqkm = 4
bears = Converter.get_bear_count(area_sq_m)
print "{} bears".format(bears)

deg = 95
mins = 25
secs = 5
dd = Converter.dms_to_dd(deg, mins, secs)
print "{:.5f}".format(dd)

Degrees = 95.41805
dd, mm, ss = Converter.dd_to_dms(Degrees)
print "{} degrees, {} minutes, {:.3} seconds = {}".format(dd,mm,ss,Degrees)

km = 100
miPerGal = 35
kmPerL = 14.88
DolPerL = 1.30
cost = Converter.get_fuel_cost(km)
print "{} km = {:.3}$".format(km,cost)


