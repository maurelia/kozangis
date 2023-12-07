import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')
    
    camaras = 'https://github.com/maurelia/kozangis/blob/edacf98a91f516740f0e16801fc58d82c5c3b4e2/data/CAMARAS.geojson'

    m = leafmap.Map(center=[-27.42581110601346, -70.26855756942263], zoom=13)
    leafmap.LocateControl().add_to(m)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras")
    m.to_streamlit(width=700,height=500,add_layer_control=True)
    
    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")
    st.markdown("### Sample Data")
    st.write('Navigate to `Data Stats` page to visualize the data')


