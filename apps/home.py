import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')
    
    m = leafmap.Map(center=[-27.37763794313421, -70.2559825011241], zoom=10)    
    m.add_basemap("HYBRID")
    m.to_streamlit(width=700,height=500,add_layer_control=True)
    
    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")
    st.markdown("### Sample Data")
    st.write('Navigate to `Data Stats` page to visualize the data')


