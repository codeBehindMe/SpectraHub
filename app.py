import pandas as pd
import streamlit as st
import plotly.express as px
import os
from src.spectrometry import plot_spectrometry, WAVELENGTH_IDENTIFIERS
from src.containers.predict_soc import predict_soc_container

mapbox_token = os.environ["MAPBOX_TOKEN"]
px.set_mapbox_access_token(mapbox_token)

st.set_page_config(layout="wide")
st.title("spectral hub (demo)")


def soc_map():
    return px.scatter_mapbox(
        df,
        lat="LAT",
        lon="LON",
        color="SOC",
        size="SOC",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=10,
        zoom=2,
        title="National SOC Data Map",
    )


if __name__ == "__main__":
    df = pd.read_csv("visnir_soc.csv")
    with st.container():
        st.plotly_chart(soc_map())

    predict_soc_container()