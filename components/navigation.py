import streamlit as st

def navigate_to(page):
    """Function to change pages"""
    st.session_state.page = page

def render_navigation():
    """Render the main navigation bar"""
    # Enhanced 4-button navigation
    st.markdown('<div class="navigation">', unsafe_allow_html=True)
    col1, col2, col3= st.columns([1, 1, 1])

    with col1:
        st.markdown('<div class="nav-button-container">', unsafe_allow_html=True)
        if st.button("HOME", key="home_btn"):
            navigate_to('home')
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="nav-button-container">', unsafe_allow_html=True)
        if st.button("EXPLORE", key="explore_btn"):
            navigate_to('explore')
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="nav-button-container">', unsafe_allow_html=True)
        if st.button("ART", key="art_btn"):
            navigate_to('art')
        st.markdown('</div>', unsafe_allow_html=True)
