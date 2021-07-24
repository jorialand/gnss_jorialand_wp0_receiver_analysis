"""
Functions for plotting the TROPOSPHERE related figures, WP0.
Author: Horia Ghionoiu Martínez, GNSS Academy
Saturday, 24/7/2021
"""

import sys, os
from pandas import unique
from SRC.interfaces import LOS_IDX
from SRC.COMMON import GnssConstants
from SRC.COMMON.Plots import generatePlot
from SRC.COMMON.Utils import compute_tropo_ztd

def plotTropo_STD_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "Slant Tropospheric Delay STD vs Time (Elev) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "STD[m]"
    # PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    # PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    PlotConf["yLim"] = [round(min(unique(LosData[LOS_IDX["TROPO[m]"]]))) - 1, round(max(unique(LosData[LOS_IDX["TROPO[m]"]])) + 1)]

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
    PlotConf["yData"][Label] = LosData[LOS_IDX["TROPO[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/TRO/' + 'TROPO_STD_Vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

def plotTropo_ZTD_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "Zenith Tropospheric Delay ZTD vs Time (Elev) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "ZTD[m]"
    # PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    # PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    # PlotConf["yLim"] = [round(min(unique(LosData[LOS_IDX["TROPO[m]"]]))) - 1, round(max(unique(LosData[LOS_IDX["TROPO[m]"]])) + 1)]
    PlotConf["yLim"] = [2.3156, 2.3172]

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
    PlotConf["yData"][Label] = compute_tropo_ztd(LosData[LOS_IDX["TROPO[m]"]], LosData[LOS_IDX["ELEV"]])
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/TRO/' + 'TROPO_ZTD_Vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)
