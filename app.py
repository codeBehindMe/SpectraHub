import pandas as pd
import streamlit as st
import plotly.express as px
import os
from src.spectrometry import plot_spectrometry

mapbox_token = os.environ["MAPBOX_TOKEN"]
px.set_mapbox_access_token(mapbox_token)

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

    with st.container():
      st.header("Predict SOC")
      st.caption("Upload your own spectrometry data to predic soc")
      spec_data = st.file_uploader("Upload")

      if spec_data != None:
        uploaded_df = pd.read_csv(spec_data)
        st.write(uploaded_df)
        st.button("Predict SOC")

        st.header("Explore individual samples")
        st.selectbox("Select a sample", uploaded_df[uploaded_df.columns.values[0]].to_list())