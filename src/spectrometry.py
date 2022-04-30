import plotly.express as px
import pandas as pd

def plot_spectrometry(df: pd.DataFrame, key_col : str, wavelength_col_id: str):

    df = df[[key_col , *filter(lambda x: x.startswith(wavelength_col_id), df.columns.values)]]

    df_melt = df.melt(id_vars=[key_col])

    return px.line(
        df_melt,
        x="variable",
        y="value",
        color=key_col,
        labels={"variable": "wavelength", "value": "reflectance"},
        title="Spectrograph",
    )