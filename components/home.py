import streamlit as st
import streamlit.components.v1 as components

def render_home_page():
    """Render the home page with Spline 3D component"""
    # Home page with Spline component
    components.html(
        """
        <iframe 
            src="https://my.spline.design/particleplanet-SZJcrtMsBA4ppoXCk1QuAvSP/" 
            frameborder="0" 
            width="100%" 
            height="1000px">
        </iframe>
        """,
        height=1000,
        scrolling=False
    )