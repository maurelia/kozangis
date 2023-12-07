import leafmap
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')
    m = leafmap.Map()
    m.add_basemap('ROADMAP')
    m.to_streamlit()
    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")
    st.markdown("### Sample Data")
    st.write('Navigate to `Data Stats` page to visualize the data')


