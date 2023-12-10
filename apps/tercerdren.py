import leafmap
import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Visor de la construcción del Tercer Dren')

    m = leafmap.Map(center=[-27.42581110601346, -70.26855756942263], zoom=13)
    m.add_basemap("HYBRID")
    m.to_streamlit(width=700,height=500,add_layer_control=True)
    
    st.write("")
    st.write("")
