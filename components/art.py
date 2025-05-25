import streamlit as st 
import os
 
def render_art_page(): 
    """Render the art page with Indian art information""" 
    # Art page 
    st.title("Indian Art") 
    st.write(""" 
    India has a rich tradition of art spanning thousands of years. From ancient cave paintings to modern contemporary art, 
    the artistic heritage of India is diverse and vibrant. 
    """) 
     
    # Art categories 
    tab1, tab2, tab3 = st.tabs(["Classical", "Folk", "Contemporary"]) 
     
    with tab1: 
        render_classical_art_section() 
         
    with tab2: 
        render_folk_art_section() 
         
    with tab3: 
        render_contemporary_art_section() 

def get_image_path(filename):
    """Helper function to get image path"""
    return os.path.join("images", filename)

def display_image_safely(image_path, caption, description, use_column_width=True):
    """Display image with hover effect if it exists, otherwise show a message"""
    if os.path.exists(image_path):
        # Create HTML with CSS for curved edges and hover effect
        image_html = f"""
        <div style="position: relative; display: inline-block; width: 100%;">
            <img src="data:image/png;base64,{get_image_base64(image_path)}" 
                 style="width: 100%; height: 350px; object-fit: cover; border-radius: 15px; 
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'; 
                            document.getElementById('tooltip-{caption.replace(' ', '-').replace(',', '').replace(':', '').lower()}').style.display='block';"
                 onmouseout="this.style.transform='scale(1)'; 
                           document.getElementById('tooltip-{caption.replace(' ', '-').replace(',', '').replace(':', '').lower()}').style.display='none';"
            />
            <div id="tooltip-{caption.replace(' ', '-').replace(',', '').replace(':', '').lower()}" 
                 style="display: none; position: absolute; background: rgba(0,0,0,0.9); color: white; 
                        padding: 12px; border-radius: 8px; top: 260px; left: 0; width: calc(100% - 24px); 
                        font-size: 14px; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                <strong>{caption}</strong><br><br>
                {description}
            </div>
        </div>
        """
        st.markdown(image_html, unsafe_allow_html=True)
    else:
        st.info(f"Image not found: {image_path}")
        st.write(f"Caption: {caption}")

def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    import base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
 
def render_classical_art_section(): 
    """Render the classical art section""" 
    st.header("Classical Art") 
    st.write(""" 
    Classical Indian art forms represent the pinnacle of artistic achievement in ancient and medieval India. 
    These art forms are characterized by their spiritual themes, technical precision, and adherence to traditional 
    aesthetic principles outlined in ancient texts like the Natya Shastra. 
    """) 
    
    # Ajanta Cave Paintings
    st.subheader("🎨 Pattachitra Paintings")
    st.write("""
    In Raghurajpur, every house is a museum, every artist a storyteller. Pattachitra artists spend weeks crafting tales on cloth, using intricate lines and bold natural colors. The devotion is evident in every stroke, especially when narrating the story of Lord Jagannath and his siblings. These scrolls were once carried from village to village, unrolled as traveling theaters. Today, they whisper to us across time: gods once walked among us, and art was their language.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("pattachitra2.jpg"), 
                           "Bodhisattva Padmapani - Cave 1",
                           "This magnificent fresco from Cave 1 depicts Bodhisattva Padmapani (Avalokiteshvara) in serene meditation. The painting showcases the sophisticated artistic techniques of ancient Indian artists, with delicate shading and emotional depth that has captivated viewers for centuries.")
    with col2:
        display_image_safely(get_image_path("pattachitra1.jpg"), 
                           "Buddha's Life Scenes - Cave 17",
                           "Cave 17 houses some of the most elaborate narrative paintings depicting scenes from Buddha's life and Jataka tales. These paintings demonstrate the mastery of perspective, composition, and storytelling through visual art in ancient India.")
    
    st.divider()
    
    # Tanjore Paintings
    st.subheader("🖼️ Tanjore Paintings")
    st.write("""
    In the temple town of Thanjavur, art meets devotion. Tanjore paintings are not just wall hangings—they’re spiritual icons. Richly colored and embellished with gold foil and glass stones, they bring deities like Lakshmi, Vishnu, and Krishna to life with divine regality. Created originally for temple altars, these paintings are considered sacred. As the gold catches sunlight, it’s said to reflect not just light, but blessings.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("tanjore1.jpg"), 
                           "Lord Krishna - Traditional Tanjore Style",
                           "This exquisite Tanjore painting depicts Lord Krishna in his divine glory, adorned with gold foil work and precious stones. The rich colors and intricate details exemplify the opulent style of Thanjavur court paintings from the Maratha period.")
    with col2:
        display_image_safely(get_image_path("tanjore2.jpg"), 
                           "Goddess Saraswati with Gold Work",
                           "Goddess Saraswati, the deity of knowledge and arts, is portrayed with traditional iconography enhanced by gold leaf application. The painting demonstrates the characteristic Tanjore technique of relief work and vibrant color palette.")
 
def render_folk_art_section(): 
    """Render the folk art section""" 
    st.header("Folk Art") 
    
    # Madhubani Art
    st.subheader("Madhubani Art")
    st.write("""In the quiet villages of Bihar, the walls speak in color. Generations of women have etched their emotions, rituals, and divine tales into their homes through Madhubani paintings—using twigs, fingers, and natural dyes. One can still see Sita’s wedding or Krishna playing the flute, captured in symmetrical frames and fish motifs, believed to bring prosperity. What began as a form of domestic devotion now graces galleries worldwide, yet its essence still lies in village courtyards under neem trees.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("madhubani1.jpg"), 
                           "Tree of Life - Traditional Madhubani",
                           "The Tree of Life is a central motif in Madhubani art, symbolizing fertility, growth, and the connection between earth and heaven. This painting showcases the characteristic geometric patterns and natural pigments used by women artists of Mithila region.")
    with col2:
        display_image_safely(get_image_path("madhubani2.jpg"), 
                           "Fish Motifs - Symbol of Fertility",
                           "Fish are auspicious symbols in Madhubani art, representing fertility, abundance, and marital bliss. This artwork demonstrates the intricate line work and vibrant colors that make Madhubani paintings instantly recognizable worldwide.")
    
    st.divider()
    
    # Blue Pottery
    st.subheader("Blue Pottery")
    st.write("""
    A traditional craft from Jaipur, Rajasthan, distinguished by striking blue and white colors. 
    Made from quartz and raw glaze without clay, colored with cobalt oxide.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("blue.jpg"), 
                           "Traditional Blue Pottery Vase",
                           "This elegant vase showcases the distinctive blue and white aesthetic of Jaipur's blue pottery tradition. Made without clay, using quartz and raw glaze, these pieces are fired at high temperatures to achieve their characteristic durability and lustrous finish.")
    with col2:
        display_image_safely(get_image_path("blue pottery 1.jpg"), 
                           "Decorative Plates with Floral Motifs",
                           "These decorative plates feature traditional Persian-influenced floral patterns painted in cobalt blue. The intricate designs reflect the Mughal influence on Rajasthani craftsmanship, creating pieces that are both functional and artistic.")
    
    st.divider()
    
    # Warli Art
    st.subheader("Warli Art")
    st.write("""
    In the tribal pockets of Maharashtra, art lives in rhythm—with life and nature. Warli art, using just white pigment on mud walls, captures weddings, harvests, and festivals with geometric simplicity. To outsiders, it may look abstract, but for the Warli people, it’s a living archive of their cultural identity. Each dot and triangle celebrates harmony—between humans, animals, and spirits. It’s art that doesn’t decorate but documents.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("warli1.jpg"), 
                           "Traditional Warli Dance Circle",
                           "This painting depicts the famous Warli dance circle, where tribal communities gather to celebrate harvests and festivals. The simple stick figures and geometric forms capture the essence of community life and spiritual connection with nature.")
    with col2:
        display_image_safely(get_image_path("warli2.jpg"), 
                           "Village Life and Daily Activities",
                           "Warli paintings serve as visual narratives of tribal life, showing daily activities like farming, hunting, and family gatherings. The minimalist style using white pigment on mud walls creates a timeless quality that speaks to universal human experiences.")
 
def render_contemporary_art_section(): 
    """Render the contemporary art section""" 
    st.header("Contemporary Art") 
    
    # Progressive Artists Group Era
    st.subheader("M.F. Hussain Paintings")
    st.write("""
    Maqbool Fida Husain was an Indian painter and film director who painted narrative paintings in a modified Cubist style. He was one of the founding members of Bombay Progressive Artists' Group. M.F. Husain is associated with Indian modernism in the 1940s.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("mf2.jpeg"), 
                           "Abstract Composition - Modern Indian Style",
                           "This abstract composition represents the fusion of traditional Indian spiritual themes with modernist techniques. The bold colors and geometric forms reflect the influence of European modernism while maintaining distinctly Indian sensibilities and symbolism.")
    with col2:
        display_image_safely(get_image_path("mf1.jpg"), 
                           "Contemporary Figurative Painting",
                           "Contemporary Indian figurative art explores themes of identity, tradition, and modernity. This piece demonstrates how contemporary artists navigate between preserving cultural heritage and expressing contemporary urban experiences.")
    
    st.divider()
    
    # Digital and Mixed Media
    st.subheader("S. H. Raza")
    st.write("""
   Sayed Haider Raza LH was an Indian painter who lived and worked in France for most of his career. Born on 22 February 1922 in Kakkaiya, Central Provinces, British India, Raza moved to France in 1950, marrying the French artist Janine Mongillat in 1959.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        display_image_safely(get_image_path("sh1.jpg"), 
                           "Digital Art Installation",
                           "This digital installation represents the new frontier of Indian contemporary art, where technology meets traditional narratives. Interactive elements and multimedia components create immersive experiences that engage viewers in dialogue about cultural identity in the digital age.")
    with col2:
        display_image_safely(get_image_path("sh2.jpg"), 
                           "Contemporary Mixed Media Sculpture",
                           "This mixed media sculpture combines traditional materials with contemporary forms, reflecting the complexity of modern Indian identity. The piece addresses themes of urbanization, globalization, and cultural preservation through innovative artistic expression.")

# Main function to run the app
def main():
    st.set_page_config(
        page_title="Indian Art Gallery",
        page_icon="🎨",
        layout="wide"
    )
    render_art_page()

if __name__ == "__main__":
    main()