"""
Functions for plotting the POS related figures, WP0.
Author: Horia Ghionoiu Martínez, GNSS Academy
Friday, 29/7/2021
"""

import sys, os
from pandas import unique
from SRC.interfaces import POS_IDX
from SRC.COMMON import GnssConstants
from SRC.COMMON.Plots import generatePlot

def PLOT_SATS_vs_TIME(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "N. SATS in PVT vs TIME from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "Number of Satellites"
    # PlotConf["yLim"] = [2522.25, 2522.28]
    # PlotConf['yticklabel_format'] = 'plain'  # Avoid scientific notation.

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    PlotConf["LineWidth"] = 1

    # PlotConf["ColorBar"] = "gnuplot"
    # PlotConf["ColorBarLabel"] = "PRN"
    # PlotConf["ColorBarMin"] = 0
    # PlotConf["ColorBarMax"] = max(unique(LosData[LOS_IDX["PRN"]])) + 1
    # PlotConf["zTicks"] = sorted(unique(LosData[LOS_IDX["PRN"]]))
    # PlotConf["zTicksLabels"] = sorted(unique(LosData[LOS_IDX["PRN"]]))

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}
    Label = 0
    PlotConf["xData"][Label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = PosData[POS_IDX["NSATS"]]
    # PlotConf["zData"][Label] = LosData[LOS_IDX["ELEV"]]                                    - CLK + LosData[LOS_IDX["STEC[m]"]] + LosData[LOS_IDX["TROPO[m]"]])

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/' + 'POS_SATS_Vs_TIME_TLSA_D006Y15.png'

    generatePlot(PlotConf)

def PLOT_POS_DOP_vs_TIME(PosData):
    pass

def PLOT_OS_HVDOP_vs_TIME(PosData):
    pass

def PLOT_POS_ENU_PE_vs_TIME(PosData):
    pass

def PLOT_POS_HVPE_vs_TIME(PosData):
    pass

def PLOT_POS_NPE_vs_EPE(PosData):
    pass