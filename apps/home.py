import leafmap
import streamlit-leaflet
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Home')
    m = leafmap.Map()

    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")
    st.markdown("### Sample Data")

    streamlit-leaflet(m)
    st.write('Navigate to `Data Stats` page to visualize the data')


