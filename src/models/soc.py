from typing import List
import pandas as pd
import numpy as np


def spectrometry_based_soc_model(df: pd.DataFrame, key_col: str):
    subset_key = pd.DataFrame(df[key_col])

    subset_key["PREDICTED_SOC_PERC"] = np.random.uniform(1, 100, df.shape[0])
    subset_key["PREDICTION_ERROR"] = np.random.uniform(5, 15, df.shape[0])

    return subset_key
