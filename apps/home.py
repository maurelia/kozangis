import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
import numpy as np
import geocoder
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation

def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')

    camaras = 'https://github.com/maurelia/kozangis/blob/e0794668c83123ef4e8fa5e2c60f386ba2ebf57d/data/CAMARAS.geojson'

    
    loc = get_geolocation()
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']

    m = leafmap.Map(center=[latitude, longitude], zoom=13, draw_control=False, measure_control=False, fullscreen_control=True, attribution_control=False)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras")
    m.add_marker([latitude, longitude], popup=None, tooltip=None, icon=folium.Icon(color='red',icon_color='white',icon='ban-circle',), draggable=False)     
    m.to_streamlit(width=600,height=700,add_layer_control=True)
    
    st.write(f"{latitude},{longitude}")


    st.write("Estas son las ubicaciones de las cámaras de registro del acueducto y relaveducto de Atacama Kozan")
    st.write("La aplicación le mostrará su ubicación y si hace click en la ubicación, le mostrara los datos mas relevantes a conocer")


