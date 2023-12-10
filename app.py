import streamlit as st
from multiapp import MultiApp
from apps import home, tercerdren # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Cámaras del acueducto/relaveducto", home.app)
app.add_app("Construcción Tercer Dren", tercerdren.app)

# The main app
app.run()
