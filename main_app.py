import streamlit as st
from components.home import render_home_page
from components.art import render_art_page
from components.explore import render_explore_page
from components.navigation import render_navigation
from components.styles import load_styles

# Set page configuration for wide layout
st.set_page_config(layout="wide", page_title="Incredible India", page_icon="🇮🇳")

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Load custom styles
load_styles()

# Render navigation
render_navigation()

# Content area
st.markdown("<div class='content-area'></div>", unsafe_allow_html=True)

# Main content based on selected page
if st.session_state.page == 'home':
    render_home_page()
elif st.session_state.page == 'art':
    render_art_page()
elif st.session_state.page == 'explore':
    render_explore_page()