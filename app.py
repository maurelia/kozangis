import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Cámaras del acueducto/relaveducto", home.app)
app.add_app("Construcción Tercer Dren", data_stats.app)

# The main app
app.run()
