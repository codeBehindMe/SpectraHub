import pandas as pd
import streamlit as st
import plotly.express as px
import os
from src.containers.header import header_container
from src.containers.soc_map import soc_map_container
from src.spectrometry import plot_spectrometry, WAVELENGTH_IDENTIFIERS
from src.containers.predict_soc import predict_soc_container

mapbox_token = os.environ["MAPBOX_TOKEN"]
px.set_mapbox_access_token(mapbox_token)

st.set_page_config(layout="wide")


if __name__ == "__main__":
    df = pd.read_csv("visnir_soc.csv")
    header_container()

    soc_map_container(df)

    predict_soc_container()
