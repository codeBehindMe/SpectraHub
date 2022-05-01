from distutils.command.upload import upload
import streamlit as st
from src.spectrometry import WAVELENGTH_IDENTIFIERS, plot_spectrometry
import pandas as pd
import plotly.express as px
from src.models.soc import spectrometry_based_soc_model
from src.models.spec_sim import get_k_closest
from src.database.database import visnir_lib


def predict_soc_container():

    with st.container():
        st.header("Upload your own data for SOC predictions")

        st.markdown(
            """
          This platform allows you to upload your own spectrometry data which 
          can give you a prediction of the soil organic carbon content value.

          >Note this is a demo and the predictions are not real

          ## How to use
          We currently only support VIS-NIR spectrometry data for predictions. 
          Click to upload button to upload of the CSV spectrometry data. See 
          your spectrometry tool documentation how to exctract this data.

          >In this demo, we expect the data to be organised in a specific way, 
          >but in a real client, we'd auto detect most of the fields for you.
        
          Currently, we expect the data to contain the following columns at a
          minimum:
          1. ID column - ID column for individual samples
          2. lattitude - column specifying the sample location's lattitude named LAT
          3. longitude - column specifying the sample location's longitude name LON
          4. absorbption x wavelength - set of columns with a prefix 'W' containing 
              absorption at each wavelength in nm.

          ### Try it with a sample
          We have set up a sample file which conforms to the above requirements
          for you to try using the UI. You can download a sample set of data from
          [here](https://storage.googleapis.com/soil_raw_landing/spectra_hub_sample.csv)."""
        )

        col1, col2 = st.columns(2)
        with col1:
            st.caption("Upload your own spectrometry data to predic soc")
            spec_data = st.file_uploader("Upload")

        if spec_data is not None:
            with col2:
                st.subheader("Your data")
                uploaded_df = pd.read_csv(spec_data)
                st.write(uploaded_df)

            with col1:
                id_col_name: str = st.selectbox(
                    "My Sample ID column is", uploaded_df.columns.values.tolist()
                )
                wavelength_identifier = st.selectbox(
                    "My measurements are", WAVELENGTH_IDENTIFIERS.keys()
                )

                predict_botton = st.button("Predict SOC")
                if predict_botton:
                    st.write("Predictions for your data")
                    st.write(spectrometry_based_soc_model(uploaded_df, id_col_name))

            with col2:
                plot_user_data_on_loc(uploaded_df, id_col_name)

            explore_individual_samples_container(
                uploaded_df, id_col_name, wavelength_identifier
            )


def explore_individual_samples_container(
    uploaded_df: pd.DataFrame, id_col_name: str, wavelength_identifier: str
):

    st.header("Explore individual samples")
    selected_sample_id = st.selectbox(
        "Select a sample", uploaded_df[uploaded_df.columns.values[0]].to_list()
    )

    selected_data: pd.DataFrame = uploaded_df[
        uploaded_df[id_col_name] == selected_sample_id
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.plotly_chart(
            plot_spectrometry(
                selected_data,
                id_col_name,
                WAVELENGTH_IDENTIFIERS[wavelength_identifier],
            )
        )

        k_closest = get_k_closest(
            selected_data,
            visnir_lib,
            id_col_name,
            WAVELENGTH_IDENTIFIERS[wavelength_identifier],
        )

    with col2:
        st.plotly_chart(
            plot_spectrometry(
                k_closest, id_col_name, WAVELENGTH_IDENTIFIERS[wavelength_identifier]
            )
        )

    with col3:
        st.plotly_chart(
            px.scatter_mapbox(
                k_closest,
                lat="LAT",
                lon="LON",
                color="SOC",
                size_max=10,
                zoom=2,
                title="Nearest neighbour locations",
            )
        )


def plot_user_data_on_loc(
    user_df: pd.DataFrame, id_col_name: str, lat_col="LAT", lon_col="LON"
):
    return st.plotly_chart(
        px.scatter_mapbox(
            user_df,
            lat=lat_col,
            lon=lon_col,
            hover_data=[id_col_name],
            size_max=10,
            zoom=2,
            title="Your sample locations",
        )
    )
