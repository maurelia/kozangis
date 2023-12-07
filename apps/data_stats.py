import folium
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_folium import st_folium

from data.create_data import create_table

def app():
    st.title('Data Stats')

    st.write("This is a sample data stats in the mutliapp.")
    st.write("See `apps/data_stats.py` to know how to use it.")
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)    
    st.markdown("### Plot Data")
    st_data = st_folium(m, width=725)
    #df = create_table()

    st.line_chart(df)
