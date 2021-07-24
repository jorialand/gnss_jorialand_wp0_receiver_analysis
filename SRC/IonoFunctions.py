"""
Functions for plotting the IONOSPHERE related figures, WP0.
Author: Horia Ghionoiu Martínez, GNSS Academy
Friday, 23/7/2021
"""

import sys, os
from pandas import unique
from SRC.interfaces import LOS_IDX
from SRC.COMMON import GnssConstants
from SRC.COMMON.Plots import generatePlot

def plotIono_STEC_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "Ionosphere Klobuchar STEC vs Time (Elev) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "STEC[m]"
    # PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["STEC[m]"]]))
    # PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["STEC[m]"]]))
    # PlotConf["yLim"] = [min(unique(LosData[LOS_IDX["STEC[m]"]])) - 1, max(unique(LosData[LOS_IDX["STEC[m]"]])) + 1]

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

def plotIono_PRN_Time_STEC(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,6.6)
    PlotConf["Title"] = "Satellite Visibility vs TIME (STEC) from TLSA on Year 2015"\
        " DoY 006"

    PlotConf["yLabel"] = "GPS-PRN"
    PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yLim"] = [0, max(unique(LosData[LOS_IDX["PRN"]])) + 1]

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'
    PlotConf["LineWidth"] = 15

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "STEC [m]"
    PlotConf["ColorBarMin"] = round(min(unique(LosData[LOS_IDX["STEC[m]"]]))) - 1
    PlotConf["ColorBarMax"] = round(max(unique(LosData[LOS_IDX["STEC[m]"]]))) + 1

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    for prn in sorted(unique(LosData[LOS_IDX["PRN"]])):
        Label = "G" + ("%02d" % prn)
        FilterCond = LosData[LOS_IDX["PRN"]] == prn
        PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]][FilterCond] / GnssConstants.S_IN_H
        PlotConf["yData"][Label] = LosData[LOS_IDX["PRN"]][FilterCond]
        PlotConf["zData"][Label] = LosData[LOS_IDX["STEC[m]"]][FilterCond]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_STEC_Vs_PRN_TLSA_D006Y15.png'

    generatePlot(PlotConf)

def plotIono_VTEC_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "Ionosphere Klobuchar VTEC vs Time (Elev) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "VTEC[m]"
    # PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    # PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    PlotConf["yLim"] = [round(min(unique(LosData[LOS_IDX["VTEC[m]"]]))) - 1, round(max(unique(LosData[LOS_IDX["VTEC[m]"]])) + 1)]

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
    PlotConf["yData"][Label] = LosData[LOS_IDX["VTEC[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_VTEC_Vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

def plotIono_PRN_Time_VTEC(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "Satellite Visibility vs Time (VTEC) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "GPS-PRN"
    PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["yLim"] = [0, max(unique(LosData[LOS_IDX["PRN"]])) + 1]

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'
    PlotConf["LineWidth"] = 15

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "VTEC [m]"
    PlotConf["ColorBarMin"] = round(min(unique(LosData[LOS_IDX["VTEC[m]"]]))) - 1
    PlotConf["ColorBarMax"] = round(max(unique(LosData[LOS_IDX["VTEC[m]"]]))) + 1

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    for prn in sorted(unique(LosData[LOS_IDX["PRN"]])):
        Label = "G" + ("%02d" % prn)
        FilterCond = LosData[LOS_IDX["PRN"]] == prn
        PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]][FilterCond] / GnssConstants.S_IN_H
        PlotConf["yData"][Label] = LosData[LOS_IDX["PRN"]][FilterCond]
        PlotConf["zData"][Label] = LosData[LOS_IDX["VTEC[m]"]][FilterCond]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/ION/' + 'IONO_VTEC_Vs_PRN_TLSA_D006Y15.png'

    generatePlot(PlotConf)