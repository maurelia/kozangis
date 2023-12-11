import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_js_eval import get_geolocation
import folium

def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')

    camaras = 'https://github.com/maurelia/kozangis/blob/e0794668c83123ef4e8fa5e2c60f386ba2ebf57d/data/CAMARAS.geojson'

    
    loc = get_geolocation()
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']


    m = leafmap.Map(center=[latitude, longitude], zoom=18, draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=False)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras",zoom_to_layer=False)
    m.add_marker([latitude, longitude], popup=None, tooltip=None, icon=folium.Icon(color="red", icon="", prefix='fa'), draggable=False,zoom_to_layer=True)     
    m.to_streamlit(width=600,height=700,add_layer_control=True)
    
    st.write(f"{latitude},{longitude}")


    st.write("Estas son las ubicaciones de las cámaras de registro del acueducto y relaveducto de Atacama Kozan")
    st.write("La aplicación le mostrará su ubicación y si hace click en la ubicación de las cámaras, le mostrara los datos mas relevantes")


