import streamlit as st
import plotly.express as px
import pandas as pd


def soc_map_container(df: pd.DataFrame):

    with st.container():
        st.plotly_chart(
            px.scatter_mapbox(
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
        )
