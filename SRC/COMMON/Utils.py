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

