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
    PlotConf["Title"] = "N. SATS in PVT from TLSA on Year 2015" \
                        " DoY 006"

    PlotConf["yLabel"] = "Number of Satellites"


    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    PlotConf["LineWidth"] = 1

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    Label = 0
    PlotConf["xData"][Label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"][Label] = PosData[POS_IDX["NSATS"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/' + 'POS_SATS_Vs_TIME_TLSA_D006Y15.png'

    generatePlot(PlotConf)

def PLOT_POS_DOP_vs_TIME(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "Dilution of Precision from TLSA on Year 2015" \
                        " DoY 006"
    PlotConf['Legend'] = True

    PlotConf["yLabel"] = "DOP"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    PlotConf["LineWidth"] = 1

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    PlotConf["xData"]['GDOP'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['GDOP'] = PosData[POS_IDX["GDOP"]]
    PlotConf["xData"]['PDOP'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['PDOP'] = PosData[POS_IDX["PDOP"]]
    PlotConf["xData"]['TDOP'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['TDOP'] = PosData[POS_IDX["TDOP"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/' + 'POS_DOP_Vs_TIME_TLSA_D006Y15.png'

    generatePlot(PlotConf)

def PLOT_OS_HVDOP_vs_TIME(PosData):
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "Dilution of Precision from TLSA on Year 2015" \
                        " DoY 006"
    PlotConf['Legend'] = True

    PlotConf["yLabel"] = "HDOP/VDOP"
    PlotConf["SecondYAxis"] = "NSATS"
    PlotConf["SecondYAxisLabel"] = "Number of Satellites"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    PlotConf["LineWidth"] = 1

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    PlotConf["xData"]['HDOP'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['HDOP'] = PosData[POS_IDX["HDOP"]]
    PlotConf["xData"]['VDOP'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['VDOP'] = PosData[POS_IDX["VDOP"]]
    PlotConf["xData"]['NSATS'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['NSATS'] = PosData[POS_IDX["NSATS"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/' + 'POS_HVDOP_Vs_TIME_TLSA_D006Y15.png'

    generatePlot(PlotConf)

def PLOT_POS_ENU_PE_vs_TIME(PosData):

    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4, 6.6)
    PlotConf["Title"] = "ENU Position Error from TLSA on Year 2015" \
                        " DoY 006"
    PlotConf['Legend'] = True

    PlotConf["yLabel"] = "ENU-PE[m]"

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '-'
    PlotConf["LineWidth"] = .5

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    PlotConf["xData"]['EPE[m]'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['EPE[m]'] = PosData[POS_IDX["EPE[m]"]]
    PlotConf["xData"]['NPE[m]'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['NPE[m]'] = PosData[POS_IDX["NPE[m]"]]
    PlotConf["xData"]['UPE[m]'] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H
    PlotConf["yData"]['UPE[m]'] = PosData[POS_IDX["UPE[m]"]]

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/' + 'POS_ENU_PE_Vs_TIME_TLSA_D006Y15_EPE.png'

    generatePlot(PlotConf)

def PLOT_POS_HVPE_vs_TIME(PosData):
    pass

def PLOT_POS_NPE_vs_EPE(PosData):
    pass