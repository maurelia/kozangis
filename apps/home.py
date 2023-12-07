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
    
    camaras = 'https://github.com/maurelia/kozangis/blob/edacf98a91f516740f0e16801fc58d82c5c3b4e2/data/CAMARAS.geojson'

    m = leafmap.Map(center=[-27.42581110601346, -70.26855756942263], zoom=13)
    m.add_basemap("HYBRID")
    m.add_geojson(camaras, layer_name="Camaras")
    m.to_streamlit(width=700,height=500,add_layer_control=False)
    
    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")
    st.markdown("### Sample Data")
    st.write('Navigate to `Data Stats` page to visualize the data')


