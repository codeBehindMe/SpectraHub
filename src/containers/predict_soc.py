import streamlit as st
from src.spectrometry import WAVELENGTH_IDENTIFIERS, plot_spectrometry
import pandas as pd
import plotly.express as px
from src.models.soc import spectrometry_based_soc_model


def predict_soc_container():

    with st.container():
        st.header("Upload your own data for SOC predictions")
        col1, col2 = st.columns(2)
        with col1:
            st.caption("Upload your own spectrometry data to predic soc")
            spec_data = st.file_uploader("Upload")

        if spec_data != None:
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

    st.plotly_chart(
        plot_spectrometry(
            uploaded_df[uploaded_df[id_col_name] == selected_sample_id],
            id_col_name,
            WAVELENGTH_IDENTIFIERS[wavelength_identifier],
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
