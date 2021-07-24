import pandas as pd
import numpy as np

def compute_three_vectors_module(x, y, z):
    data = {'x': x,
            'y': y,
            'z': z}
    df = pd.DataFrame(data)
    res = np.zeros((df.shape[0]))

    for row in range(df.shape[0]):
        # print(row)
        res[row] = np.linalg.norm(df.iloc[row])
    return res

def compute_sat_clk_correction(SV_CLK, DTR, TGD):
    return SV_CLK + DTR - TGD

def compute_tropo_ztd(STD, ELEV):
    ZTD = np.zeros((STD.size))

    for i in range(ZTD.size):
        ZTD[i] = STD[i] / ( 1.001 / np.sqrt(0.002001 + np.sin(ELEV[i]) ** 2) )

    return ZTD

