#!/usr/bin/env python

## Copyright (C) GNSS ACADEMY 
##
## Name          : receiver_analysis.py
## Purpose       : WP0 Takss: Plot Receiver SPP Analyses
## Project       : WP0-JSNP
## Component     : 
## Author        : GNSS Academy
## Creation date : 2021
## File Version  : 1.0
##

import sys, os
from collections import OrderedDict
from pandas import read_csv
# from yaml import dump

from SRC.interfaces import LOS_IDX
import SRC.SatFunctions as SatFunctions
import SRC.IonoFunctions as IonoFunctions

#######################################################
# INTERNAL FUNCTIONS 
#######################################################

def displayUsage():
    sys.stderr.write("ERROR: Please provide path to SCENARIO as a unique \nargument\n")

def readConf(CfgFile):
    Conf = OrderedDict({})
    with open(CfgFile, 'r') as f:
        # Read file
        Lines = f.readlines()

        # Read each configuration parameter which is compound of a key and a value
        for Line in Lines:
            if "#" in Line: continue
            LineSplit = Line.split('=')
            try:
                LineSplit = list(filter(None, LineSplit))
                Conf[LineSplit[0].strip()] = LineSplit[1].strip()

            except:
                sys.stderr.write("ERROR: Bad line in conf: %s\n" % Line)

    return Conf

#######################################################
# MAIN PROCESSING
#######################################################

print( '-----------------------------')
print( 'RUNNING RECEIVER ANALYSES ...')
print( '-----------------------------')

if len(sys.argv) != 2:
    displayUsage()
    sys.exit()

# Take the arguments
Scen = sys.argv[1]

# Path to conf
CfgFile = Scen + '/CFG/receiver_analysis.cfg'

# Read conf file
Conf = readConf(CfgFile)

# Print 
print('Reading Configuration file',CfgFile)

#print(dump(Conf))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>> LOS FILE ANALYSES
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get LOS file full path
LosFile = Scen + 'OUT/LOS/' + Conf["LOS_FILE"]

#-----------------------------------------------------------------------
# PLOT SATELLITE ANALYSES
#-----------------------------------------------------------------------

# Plot Satellite Visibility figure
if(Conf["PLOT_SATVIS"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["PRN"],LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Visibility Periods ...')

    # Configure plot and call plot generation function
    SatFunctions.plotSatVisibility(LosData)

# Plot Satellite Geometrical Ranges figure
if(Conf["PLOT_SATRNG"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],LOS_IDX["RANGE[m]"],LOS_IDX["ELEV"]])

    print( 'Plot Satellite Geometrical Ranges ...')
    
    # Configure plot and call plot generation function
    SatFunctions.plotSatGeomRnge(LosData)

# Plot Satellite Tracks figure
if(Conf["PLOT_SATTRK"] == '1'):
    # Read the cols we need from LOS file
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[LOS_IDX["SOD"],
    LOS_IDX["SAT-X[m]"],
    LOS_IDX["SAT-Y[m]"],
    LOS_IDX["SAT-Z[m]"],
    LOS_IDX["ELEV"]])
    
    print( 'Plot Satellite Tracks ...')    

    # Configure plot and call plot generation function
    SatFunctions.plotSatTracks(LosData)

# Plot Satellite Velocity figure
if(Conf['PLOT_SATVEL'] == '1'):
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None, \
                       usecols=[LOS_IDX["SOD"], LOS_IDX["PRN"],
                                LOS_IDX['VEL-X[m/s]'], LOS_IDX['VEL-Y[m/s]'], LOS_IDX['VEL-Z[m/s]'],
                                LOS_IDX["ELEV"]])

    print('Plot Satellite Velocities ...')
    SatFunctions.plotSatVel(LosData)

# Plot Satellite Clock figure
if(Conf['PLOT_SATCLK'] == '1'):
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None, \
                       usecols=[LOS_IDX["SOD"],
                                LOS_IDX['SV-CLK[m]'],
                                LOS_IDX['TGD[m]'],
                                LOS_IDX['DTR[m]'],
                                LOS_IDX["PRN"],
                                ])

    print('Plot Satellite Clocks ...')
    SatFunctions.plotSatClk(LosData)

# Plot Satellite Clock Total Group Delay figure
if(Conf['PLOT_SATTGD'] == '1'):
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None, \
                       usecols=[LOS_IDX["SOD"],
                                LOS_IDX['TGD[m]'],
                                LOS_IDX["PRN"],
                                ])

    print('Plot Satellite Clock Total Group Delay (TGD) ...')
    SatFunctions.plotSatTGD(LosData)

# Plot Satellite Clock Total Group Delay figure
if(Conf['PLOT_SATDTR'] == '1'):
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None, \
                       usecols=[LOS_IDX["SOD"],
                                LOS_IDX['DTR[m]'],
                                LOS_IDX["ELEV"],
                                ])

    print('Plot Satellite Clock Delay Total Room (DTR) ...')
    SatFunctions.plotSatDTR(LosData)

# Plot of slant ionospheric delays (STEC in meters) from Klobuchar model for all satellites
# as a function of the hour of the day. Color: satellite elevation.
if(Conf['PLOT_IONO_STEC_TIME_ELEV'] == '1'):
    LosData = read_csv(LosFile, delim_whitespace=True, skiprows=1, header=None, \
                       usecols=[LOS_IDX["STEC[m]"],
                                LOS_IDX['SOD'],
                                LOS_IDX["ELEV"],
                                ])

    print('Plot Satellite STEC Vs TIME (ELEV) ...')
    IonoFunctions.plotIono_STEC_Time_Elev(LosData)
