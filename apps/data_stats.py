import folium
import streamlit as st
import numpy as np
import pandas as pd
import leafmap

from data.create_data import create_table

def app():
    st.title('Data Stats')

    st.write("This is a sample data stats in the mutliapp.")
    st.write("See `apps/data_stats.py` to know how to use it.")

    st.markdown("### Plot Data")
    m = leafmap.Map()
    m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
    )
    m
