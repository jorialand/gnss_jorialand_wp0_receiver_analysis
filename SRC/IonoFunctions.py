"""
Functions for plotting the IONOSPHERE related figures, WP0.
Author: Horia Ghionoiu Martínez, GNSS Academy
23/7/2021
"""

import sys, os
from SRC.interfaces import LOS_IDX
from SRC.COMMON import GnssConstants
from SRC.COMMON.Plots import generatePlot

def plotIono_STEC_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "Ionosphere Klobuchar STEC vs Time vs Elev from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "STEC[m]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 0.75

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "Elevation [deg]"
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = LosData[LOS_IDX["STEC[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_STEC_Vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)


def plotIono_PRN_Time_STEC():
    pass

def plotIono_VTEC_Time_Elev():
    pass

def plotIono_PRN_Time_VTEC():
    pass