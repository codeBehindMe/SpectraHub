from typing import Optional
import pandas as pd
from scipy.spatial import distance


def filter_wavelength_columns(
    df: pd.DataFrame, wl_col_id: Optional[str] = "m"
) -> pd.DataFrame:
    return df[filter(lambda x: x.startswith(wl_col_id), df.columns.values)]


def get_k_closest(
    selected_df: pd.DataFrame, lib_df: pd.DataFrame, key_col: str, wl_identifier: str
):

    target_vector = filter_wavelength_columns(selected_df, wl_identifier)
    lib_vectors = filter_wavelength_columns(lib_df, wl_identifier)

    lib_df["SCORES"] = lib_vectors.apply(
        lambda x: distance.euclidean(x.to_numpy().flatten(), target_vector), axis=1
    )

    return lib_df.sort_values("SCORES", ascending=False).head(5)
