import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd
import numpy as np
import geocoder

def get_current_gps_coordinates():
    g = geocoder.ip('me')#this function is used to find the current information using our IP Add
    if g.latlng is not None: #g.latlng tells if the coordiates are found or not
        return g.latlng
    else:
        return None

if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates
        print(f"Your current GPS coordinates are:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Unable to retrieve your GPS coordinates.")


def app():
    st.title('Ubicación de las cámaras del Acueducto y Relaveducto KOZAN')

    get_current_gps_coordinates()

    camaras = 'https://github.com/maurelia/kozangis/blob/e0794668c83123ef4e8fa5e2c60f386ba2ebf57d/data/CAMARAS.geojson'

    m = leafmap.Map(center=[-27.42581110601346, -70.26855756942263], zoom=13)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras")
    m.to_streamlit(width=700,height=500,add_layer_control=True)
    
    st.write("Estas son las ubicaciones de las cámaras de registro del acueducto y relaveducto de Atacama Kozan")
    st.write("La aplicación le mostrará su ubicación y si hace click en la ubicación, le mostrara los datos mas relevantes a conocer")


