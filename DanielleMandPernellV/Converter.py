"""Various unit conversions for GIS4107 - Exercises for Week 3"""
#-------------------------------------------------------------------------------
# Name:        converter.py
# Purpose:     Various unit conversions for GIS4107 - Exercises for Week 3
#
# Author:      elle.migeon
#
# Created:     17-09-2019
# Copyright:   (c) elle.migeon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def miles_to_km (mi):
    """This function converts miles to kilometers."""
    miles_per_kilometer = mi * 1.60934
    #km =  mi * miles_per_kilometer [redundancy. don't need]
    return miles_per_kilometer

def kmPerHr_to_mPerSec (km_per_hr):
    """This function converts kilometers/hour to metres/second."""
    m_per_s = km_per_hr / 3.599997120002304
    return m_per_s

def sqmetres_to_hectares (sq_m):
    """This function converts square meters to hectares."""
    hctr = sq_m / 10000
    return hctr

def sqmetres_to_acres (sq_m):
    """This function converts square meters to acres."""
    acres = sq_m * 0.000247105
    return acres

def acres_to_edge_of_square (acres):
    """This function converts square acres to
        length of edge of square of in metres."""
    edge_of_square = acres * 63.614808
    return edge_of_square

def get_bear_count (area_sq_m):
    """This function converts bear density to the probable number of bears
        within a given area."""
    bear_per_sqkm = 4
    area_sq_km = area_sq_m / 1000
    bears = bear_per_sqkm * area_sq_km
    return bears

def dms_to_dd (deg, mins, secs):
   """This function converts degrees, minutes and seconds to decimal degrees."""
   deg = 95
   mins = 25
   secs = 5
   dd = (deg) + (float(mins)/60) + (float(secs)/3600)
   return dd

def dd_to_dms (Degrees):
    """This function converts decimal degrees to degrees, minutes, seconds
        coordinates."""
    dd = int(Degrees)
    mm = int((Degrees - dd) * 60)
    ss = (Degrees - dd - (float(mm)/60)) * 3600
    return dd, mm, ss

def get_fuel_cost (km):
    """This function converts kilometers to fuel cost in dollars."""
    km = 100
    miPerGal = 35
    kmPerL = 14.88
    DolPerL = 1.30
    cost = (km/kmPerL) * (DolPerL)
    return cost




