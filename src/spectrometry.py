import plotly.express as px
import pandas as pd

WAVELENGTH_IDENTIFIERS = {
    "Visible Light / Near Infrared (W)": "W",
    "Medium Infrared (M)": "M",
    "Gamma (G)": "G",
    "Hyperspectral (H)": "H",
}


def plot_spectrometry(
    df: pd.DataFrame, key_col: str, wavelength_col_id: str, plot_title="Spectrometry"
):

    df = df[
        [key_col, *filter(lambda x: x.startswith(wavelength_col_id), df.columns.values)]
    ]

    df_melt = df.melt(id_vars=[key_col])

    return px.line(
        df_melt,
        x="variable",
        y="value",
        color=key_col,
        labels={"variable": "wavelength", "value": "reflectance"},
        title=plot_title,
    )
