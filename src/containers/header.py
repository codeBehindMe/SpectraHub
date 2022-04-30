import streamlit as st


def header_container():

    st.title("Spectral Hub (demo)")
    st.caption(
        "Spectral hub is a place where you can share your spectral data and get predictions of Soil Organic Carbon"
    )

    st.markdown(
        """ 
  > This demo uses a mix of sample and computer generated data.
  """
    )
