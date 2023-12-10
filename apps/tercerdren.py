import leafmap
import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Visor de la construcción del Tercer Dren')

    m = leafmap.Map(center=[-27.42581110601346, -70.26855756942263], zoom=13)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras")
    m.to_streamlit(width=700,height=500,add_layer_control=True)
    
    st.write("Estas son las ubicaciones de las cámaras de registro del acueducto y relaveducto de Atacama Kozan")
    st.write("La aplicación le mostrará su ubicación y si hace click en la ubicación, le mostrara los datos mas relevantes a conocer")
