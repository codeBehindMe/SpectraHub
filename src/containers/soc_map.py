import streamlit as st
import plotly.express as px
import pandas as pd


def soc_map_container(df: pd.DataFrame):

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig = px.scatter_mapbox(
                    df,
                    lat="LAT",
                    lon="LON",
                    color="SOC",
                    color_continuous_scale=px.colors.cyclical.IceFire,
                    size_max=10,
                    zoom=2,
                    title="National Soil Carbon Data Map",
                )
            fig.update_layout(coloraxis_showscale=False)
            st.plotly_chart(
              fig
            )

        with col2:
            st.markdown(
                """
          # National Soil Carbon Map
          
          >Note this is computer generated data for purpose of demonstration

          The National Soil Carbon Map visualises the available soil organic
          carbon data. 
          The data is organised into a format which allows it to be easily used 
          in data analysis and machine based modelling techniques. 

          ## What data is available
          Spectral hub contains proximal sensing data; currently we have 
          spectral schemes of VIS-NIR, MIR, Hyperspectral and Gamma. 

          In the future we'll be integrating the remote sensing data too which
          will give a more complete picture of soil organic carbon stock.

          ## How can I get access to this dataset.

          We support 3 ways toget the data that is available in this repository.
          1. Click the download button below.
          2. The Rest API  - Documentation TBA
          3. The python sdk - Documentation TBA
          """
            )

            st.download_button("Download data", df.to_csv(), "soc_data.csv")
