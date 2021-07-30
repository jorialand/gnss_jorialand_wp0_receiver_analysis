"""
Functions for plotting the MEASUREMENTS related figures, WP0.
Author: Horia Ghionoiu Martínez, GNSS Academy
Monday, 26/7/2021
"""

import sys, os
from pandas import unique
from SRC.interfaces import LOS_IDX
from SRC.COMMON import GnssConstants
from SRC.COMMON.Plots import generatePlot

def plotMeas_PSR_Time_Elev(LosData):
    # Configure the figure
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 7.6)
    PlotConf["Title"] = "PseudoRange C1C vs Time (Elev) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "STD[m]"
    # PlotConf["yTicks"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    # PlotConf["yTicksLabels"] = sorted(unique(LosData[LOS_IDX["VTEC[m]"]]))
    PlotConf["yLim"] = [round(min(unique(LosData[LOS_IDX["MEAS[m]"]]))) - 1,
                        round(max(unique(LosData[LOS_IDX["MEAS[m]"]])) + 1)]

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
    PlotConf["yData"][Label] = LosData[LOS_IDX["MEAS[m]"]]
    PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_CODES_Vs_TIME_TLSA_D006Y15.png'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

def plotMeas_ResidualsC1(LosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "Residuals C1 vs Time (PRN) from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "Residuals[km]"
    PlotConf["yLim"] = [2522.25, 2522.28]
    PlotConf['yticklabel_format'] = 'plain'  # Avoid scientific notation.


    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]


    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 0.01

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = "PRN"
    PlotConf["ColorBarMin"] = 0
    PlotConf["ColorBarMax"] = max(unique(LosData[LOS_IDX["PRN"]])) + 1
    PlotConf["zTicks"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    PlotConf["zTicksLabels"] = sorted(unique(LosData[LOS_IDX["PRN"]]))


    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    CLK = LosData[LOS_IDX["SV-CLK[m]"]] + LosData[LOS_IDX["DTR[m]"]] - LosData[LOS_IDX["TGD[m]"]]
    RES = LosData[LOS_IDX["MEAS[m]"]] - (LosData[LOS_IDX["RANGE[m]"]]
                                         - CLK + LosData[LOS_IDX["STEC[m]"]] + LosData[LOS_IDX["TROPO[m]"]])
    for prn in sorted(unique(LosData[LOS_IDX["PRN"]])):
        Label = "G" + ("%02d" % prn)
        FilterCond = LosData[LOS_IDX["PRN"]] == prn
        PlotConf["xData"][Label] = LosData[LOS_IDX["SOD"]][FilterCond] / GnssConstants.S_IN_H
        PlotConf["yData"][Label] = RES[FilterCond] / GnssConstants.M_IN_KM
        PlotConf["zData"][Label] = LosData[LOS_IDX["PRN"]][FilterCond]

    PlotConf["Path"] = sys.argv[1] + '/OUT/LOS/MSR/' + 'MEAS_RESIDUALS_Vs_TIME_TLSA_D006Y15.png'

    generatePlot(PlotConf)
