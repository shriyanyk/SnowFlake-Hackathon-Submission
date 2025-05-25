import streamlit as st

def render_gallery_page():
    """Render the gallery page with image collections"""
    # Gallery page
    st.title("Gallery")
    st.write("Explore the visual richness of Indian culture through our curated gallery.")
    
    # Create a simple gallery layout with placeholders
    render_gallery_grid()

def render_gallery_grid():
    """Render the main gallery grid layout"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_gallery_column_1()
        
    with col2:
        render_gallery_column_2()
        
    with col3:
        render_gallery_column_3()

def render_gallery_column_1():
    """Render the first column of gallery images"""
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Festival", use_column_width=True)
    st.write("Festival of Colors")
    
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Architecture", use_column_width=True)
    st.write("Ancient Temples")

def render_gallery_column_2():
    """Render the second column of gallery images"""
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Dance", use_column_width=True)
    st.write("Classical Dance Forms")
    
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Art", use_column_width=True)
    st.write("Traditional Paintings")

def render_gallery_column_3():
    """Render the third column of gallery images"""
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Food", use_column_width=True)
    st.write("Culinary Delights")
    
    st.image("https://via.placeholder.com/300x200.png?text=Indian+Textiles", use_column_width=True)
    st.write("Handcrafted Textiles")