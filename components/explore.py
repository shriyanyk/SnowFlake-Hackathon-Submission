import streamlit as st
import streamlit.components.v1 as components
import os
import base64

def render_explore_page():
    """Render the explore page with video and content sections"""

    # Inject custom CSS for h1.section-title
    st.markdown("""
        <style>
            .section-title {
                font-size: 4.5rem;
                text-align: center;
                margin-bottom: 20px;
                color: #222;
            }
        </style>
    """, unsafe_allow_html=True)

    # Explore page title
    st.markdown('<h1 class="section-title">Explore Incredible India</h1>', unsafe_allow_html=True)

    # Video display section with autoplay and rounded corners
    render_video_section()

    # Scrollable content sections
    render_best_places_carousel()

    # New festivals section
    render_festivals_section()


def render_video_section():
    """Render the video section with autoplay functionality"""
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    
    try:
        video_file_path = "video/India - Made with Clipchamp.mp4"
        
        if os.path.exists(video_file_path):
            # Read video file and encode to base64 for embedding
            with open(video_file_path, "rb") as video_file:
                video_bytes = video_file.read()
            
            # Create base64 encoded video
            import base64
            video_base64 = base64.b64encode(video_bytes).decode()
            
            # Embed video with full autoplay and no controls
            components.html(f"""
                <div style="width: 100%; text-align: center;">
                    <video 
                        width="100%" 
                        height="800"
                        autoplay 
                        muted 
                        loop
                        playsinline
                        preload="auto"
                        style="border-radius: 35px; box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.3); object-fit: cover;">
                        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                
                <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    const video = document.querySelector('video');
                    if (video) {{
                        video.muted = true;
                        video.play().catch(e => {{
                            console.log('Autoplay blocked by browser:', e);
                            // Fallback: try to play on user interaction
                            document.addEventListener('click', function() {{
                                video.play().catch(e => console.log('Play failed:', e));
                            }}, {{ once: true }});
                        }});
                        
                        // Ensure video keeps playing
                        video.addEventListener('pause', function() {{
                            setTimeout(() => {{
                                video.play().catch(e => console.log('Resume failed:', e));
                            }}, 100);
                        }});
                    }}
                }});
                </script>
            """, height=450)
        else:
            raise FileNotFoundError("Video file not found")
            
    except (FileNotFoundError, MemoryError):
        render_video_fallback()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_video_fallback():
    """Render fallback content when video is not available"""
    st.markdown("""
    <div style="background: linear-gradient(45deg, #1a1a1a, #2d2d2d); 
                height: 400px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                border-radius: 25px; 
                border: 2px solid rgba(255,100,100,0.3);">
        <div style="text-align: center; color: rgba(255,255,255,0.6);">
            <h3>⚠️ Video File Not Found</h3>
            <p>Please ensure your video file is in the correct location</p>
            <p style="font-size: 0.9rem; color: rgba(255,255,255,0.4);">
                Expected: video/India - Made with Clipchamp.mp4
            </p>
            <p style="font-size: 0.8rem; color: rgba(255,255,255,0.3); margin-top: 15px;">
                Note: When video is found, it will autoplay without controls
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show how it would work with a placeholder video URL (no controls)
    st.markdown("### Demo with Placeholder Video (Auto-playing):")
    components.html("""
        <div style="width: 100%; text-align: center;">
            <video 
                width="100%" 
                height="300" 
                autoplay 
                muted 
                loop 
                playsinline
                preload="auto"
                style="border-radius: 15px; box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.3); margin-top: 20px; object-fit: cover;">
                <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const video = document.querySelector('video');
            if (video) {
                video.muted = true;
                video.play().catch(e => {
                    console.log('Autoplay blocked by browser:', e);
                    // Show a subtle message if autoplay fails
                    const message = document.createElement('div');
                    message.innerHTML = '<p style="color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-top: 10px;">Click anywhere to start video</p>';
                    video.parentNode.appendChild(message);
                    
                    document.addEventListener('click', function() {
                        video.play().catch(e => console.log('Play failed:', e));
                        message.remove();
                    }, { once: true });
                });
                
                // Prevent pausing
                video.addEventListener('pause', function() {
                    setTimeout(() => {
                        video.play().catch(e => console.log('Resume failed:', e));
                    }, 100);
                });
            }
        });
        </script>
    """, height=350)


def render_best_places_carousel():
    """Render a horizontally scrollable image carousel with hover text about culture"""
    import os
    import base64
    import streamlit as st
    import streamlit.components.v1 as components

    image_folder = "images"
    place_images = [
        ("Shimla", "shimla.jpg", "Snowy escape with Himachali folk music"),
        ("Udaipur", "udaipur.jpeg", "City of Lakes & Mewar miniature art"),
        ("Varanasi", "varanasi.jpg", "Spiritual hub with Ganga Aarti rituals"),
        ("Leh", "leh.jpg", "Land of Lamas & Buddhist mask festivals"),
        ("Kutch", "kutch.jpeg", "Home to Rann Utsav & mirror embroidery")
    ]

    image_elements = ""
    for name, filename, description in place_images:
        image_path = os.path.join(image_folder, filename)
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                img_bytes = img_file.read()
                img_base64 = base64.b64encode(img_bytes).decode()
                image_elements += f"""
                    <div class="place-card">
                        <img src="data:image/jpeg;base64,{img_base64}" alt="{name}" title="{name}">
                        <div class="overlay">
                            <h4>{name}</h4>
                            <p>{description}</p>
                        </div>
                    </div>
                """

    html_code = f"""
    <style>
        .scroll-wrapper {{
            overflow-x: auto;
            white-space: nowrap;
            padding: 10px 0;
        }}
        .scroll-container {{
            display: flex;
            gap: 20px;
        }}
        .place-card {{
            position: relative;
            flex: 0 0 auto;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
            transition: transform 0.3s ease;
        }}
        .place-card:hover {{
            transform: scale(1.05);
        }}
        .place-card img {{
            width: 300px;
            height: 200px;
            object-fit: cover;
            border-radius: 20px;
        }}
        .overlay {{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 12px;
            background: rgba(0,0,0,0.6);
            color: #fff;
            font-family: sans-serif;
            transition: 0.3s ease;
            opacity: 0;
        }}
        .place-card:hover .overlay {{
            opacity: 1;
        }}
        .overlay h4 {{
            margin: 0 0 4px 0;
            font-size: 18px;
            font-weight: bold;
        }}
        .overlay p {{
            margin: 0;
            font-size: 14px;
        }}
        ::-webkit-scrollbar {{
            height: 12px;
            width: 12px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(60, 60, 60, 0.3);
            border-radius: 6px;
            margin: 0 10px;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(150, 150, 150, 0.6); 
            border-radius: 6px;
            border: 2px solid transparent;
            background-clip: content-box;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(180, 180, 180, 0.8);
            background-clip: content-box;
        }}
        ::-webkit-scrollbar-corner {{
            background: transparent;
        }}
    </style>
    <div class="scroll-wrapper">
        <div class="scroll-container">
            {image_elements}
        </div>
    </div>
    """

    st.markdown("""
    <div style="text-align: center; padding-top: 100px; margin-bottom: 10px;">
        <h2 style="font-size: 3.0rem; color: #FF6B35;"> Top Destinations for Cultural Travel</h2>
    </div>
    """, unsafe_allow_html=True)
    components.html(html_code, height=300, scrolling=True)


def render_festivals_section():
    """Render festivals and events section organized by months"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 30px;">
        <h2 style="font-size: 3.0rem; color: #FF6B35;">Festivals & Cultural Events Throughout the Year</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Festival data organized by months
    festivals_data = {
        "January": [
            ("Makar Sankranti", "Gujarat", "makar sankranti.jpg", "Kite flying festival celebrating harvest season", "Mid-January"),
            ("Republic Day Parade", "Delhi", "republic day.jpg", "Grand celebration of India's constitution", "26th January"),
            ("Desert Festival", "Rajasthan", "desert festival.jpg", "Cultural extravaganza in the Thar Desert", "January-February")
        ],
        "February": [
            ("Vasant Panchami", "Punjab", "vasant pachami.png", "Spring festival dedicated to Goddess Saraswati", "Late January/February"),
            ("Losar Festival", "Ladakh", "losar.jpg", "Tibetan New Year celebration", "February/March"),
            ("Surajkund Mela", "Haryana", "surajkund.jpg", "International crafts and cultural fair", "February")
        ],
        "March": [
            ("Holi", "Mathura, UP", "holi.jpg", "Festival of colors celebrating spring arrival", "March (Full Moon)"),
            ("Shigmo", "Goa", "shigmo.jpeg", "Goan spring festival with parades", "March"),
            ("Chapchar Kut", "Mizoram", "chapchar.jpg", "Harvest festival of the Mizo people", "March")
        ],
        "April": [
            ("Baisakhi", "Punjab", "baisakhi.jpg", "Harvest festival and Sikh New Year", "13th/14th April"),
            ("Ram Navami", "Ayodhya, UP", "ram_navami.jpg", "Celebration of Lord Rama's birth", "April"),
            ("Bohag Bihu", "Assam", "bohag_bihu.jpg", "Assamese New Year celebration", "Mid-April")
        ],
        "May": [
            ("Buddha Purnima", "Bodh Gaya, Bihar", "buddha_purnima.jpg", "Celebration of Buddha's birth", "May (Full Moon)"),
            ("Ratha Yatra", "Puri, Odisha", "ratha_yatra.jpg", "Chariot festival of Lord Jagannath", "June/July"),
            ("Thrissur Pooram", "Kerala", "thrissur_pooram.jpg", "Grand temple festival with elephants", "April/May")
        ],
        "June": [
            ("Rath Yatra", "Puri, Odisha", "rath_yatra_puri.jpg", "Famous chariot procession", "June/July"),
            ("Hemis Festival", "Ladakh", "hemis_festival.jpg", "Largest monastic festival in Ladakh", "June/July"),
            ("Ambubachi Mela", "Assam", "ambubachi.jpg", "Fertility festival at Kamakhya Temple", "June")
        ],
        "July": [
            ("Kanwar Yatra", "Uttarakhand", "kanwar_yatra.jpg", "Pilgrimage to collect Ganga water", "July/August"),
            ("Guru Purnima", "Nationwide", "guru_purnima.jpg", "Honoring spiritual teachers", "July"),
            ("Pushkar Fair", "Rajasthan", "pushkar_fair.jpg", "Camel fair and cultural celebration", "October/November")
        ],
        "August": [
            ("Independence Day", "Delhi", "independence_day.jpg", "National celebration of freedom", "15th August"),
            ("Raksha Bandhan", "Nationwide", "raksha_bandhan.jpg", "Festival celebrating sibling bond", "August"),
            ("Krishna Janmashtami", "Mathura, UP", "janmashtami.jpg", "Celebration of Lord Krishna's birth", "August/September")
        ],
        "September": [
            ("Ganesh Chaturthi", "Maharashtra", "ganesh_chaturthi.jpg", "Grand celebration of Lord Ganesha", "August/September"),
            ("Onam", "Kerala", "onam.jpg", "Harvest festival of Kerala with boat races", "August/September"),
            ("Navratri", "Gujarat", "navratri.jpg", "Nine nights of dance and devotion", "September/October")
        ],
        "October": [
            ("Durga Puja", "West Bengal", "durga_puja.jpg", "Grand celebration of Goddess Durga", "September/October"),
            ("Dussehra", "Karnataka", "dussehra.jpg", "Victory of good over evil", "September/October"),
            ("Karva Chauth", "North India", "karva_chauth.jpg", "Festival of married women", "October/November")
        ],
        "November": [
            ("Diwali", "Nationwide", "diwali.jpg", "Festival of lights and prosperity", "October/November"),
            ("Pushkar Fair", "Rajasthan", "pushkar_camel_fair.jpg", "World's largest camel fair", "November"),
            ("Bhai Dooj", "North India", "bhai_dooj.jpg", "Celebrating brother-sister bond", "November")
        ],
        "December": [
            ("Hornbill Festival", "Nagaland", "hornbill_festival.jpg", "Festival of festivals showcasing Naga culture", "1-10 December"),
            ("Christmas", "Goa", "christmas_goa.jpg", "Joyous celebration in India's Christian heartland", "25th December"),
            ("Rann Utsav", "Gujarat", "rann_utsav.jpg", "Cultural festival in the white desert", "December-February")
        ]
    }
    
    # Create month selector with custom styling
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        selected_month = st.selectbox(
            "Select Month to Explore Festivals:",
            list(festivals_data.keys()),
            index=0
        )
    
    # Render festival cards for selected month
    render_festival_cards(festivals_data[selected_month], selected_month)

def render_festival_cards(festivals, month):
    """Render festival cards for the selected month"""
    image_folder = "images"
    
    festival_cards_html = ""
    for festival_name, location, image_file, description, timing in festivals:
        image_path = os.path.join(image_folder, image_file)
        
        # Try to load image, use placeholder if not found
        if os.path.exists(image_path):
            try:
                with open(image_path, "rb") as img_file:
                    img_bytes = img_file.read()
                    img_base64 = base64.b64encode(img_bytes).decode()
                    image_src = f"data:image/jpeg;base64,{img_base64}"
            except:
                image_src = "https://via.placeholder.com/400x250/FF6B35/FFFFFF?text=Festival+Image"
        else:
            image_src = "https://via.placeholder.com/400x250/FF6B35/FFFFFF?text=Festival+Image"
        
        festival_cards_html += f"""
            <div class="festival-card">
                <div class="festival-image">
                    <img src="{image_src}" alt="{festival_name}">
                    <div class="festival-timing">{timing}</div>
                </div>
                <div class="festival-content">
                    <h3 class="festival-title">{festival_name}</h3>
                    <div class="festival-location">
                        <span class="location-icon">📍</span>
                        <span>{location}</span>
                    </div>
                    <p class="festival-description">{description}</p>
                    <div class="best-time">
                        <span class="time-icon">🗓️</span>
                        <span>Best Time: {timing}</span>
                    </div>
                </div>
            </div>
        """
    
    html_code = f"""
    <style>
        .festivals-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            padding: 20px 0;
        }}
        
        .festival-card {{
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }}
        
        .festival-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}
        
        .festival-image {{
            position: relative;
            height: 200px;
            overflow: hidden;
        }}
        
        .festival-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }}
        
        .festival-card:hover .festival-image img {{
            transform: scale(1.1);
        }}
        
        .festival-timing {{
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255,107,53,0.9);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            backdrop-filter: blur(10px);
        }}
        
        .festival-content {{
            padding: 20px;
        }}
        
        .festival-title {{
            color: #FF6B35;
            font-size: 22px;
            font-weight: bold;
            margin: 0 0 10px 0;
            font-family: 'Arial', sans-serif;
        }}
        
        .festival-location {{
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            color: rgba(255,255,255,0.8);
            font-size: 14px;
        }}
        
        .location-icon {{
            margin-right: 8px;
            font-size: 16px;
        }}
        
        .festival-description {{
            color: rgba(255,255,255,0.9);
            font-size: 14px;
            line-height: 1.6;
            margin: 0 0 15px 0;
        }}
        
        .best-time {{
            display: flex;
            align-items: center;
            color: #4CAF50;
            font-size: 13px;
            font-weight: 500;
            background: rgba(76,175,80,0.1);
            padding: 8px 12px;
            border-radius: 15px;
            border: 1px solid rgba(76,175,80,0.3);
        }}
        
        .time-icon {{
            margin-right: 8px;
            font-size: 14px;
        }}
        
        .month-header {{
            text-align: center;
            margin: 30px 0 20px 0;
            color: #FF6B35;
            font-size: 24px;
            font-weight: bold;
        }}
        
        @media (max-width: 768px) {{
            .festivals-container {{
                grid-template-columns: 1fr;
                gap: 20px;
            }}
            
            .festival-card {{
                margin: 0 10px;
            }}
        }}
    </style>
    
    <div class="month-header"> {month} Festivals & Events</div>
    <div class="festivals-container">
        {festival_cards_html}
    </div>
    """
    
    components.html(html_code, height=len(festivals) * 180 + 100, scrolling=True)

def render_content_sections():
    """Render all content sections for the explore page"""
    st.markdown('<div class="explore-section">', unsafe_allow_html=True)
    
    # Heritage section
    render_heritage_section()
    
    # Culture section
    render_culture_section()
    
    # Adventure section
    render_adventure_section()
    
    # Cuisine section
    render_cuisine_section()
    
    # Spirituality section
    render_spirituality_section()
    
    # Crafts section
    render_crafts_section()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_heritage_section():
    """Render heritage and monuments section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🏛️ Heritage & Monuments</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            Discover India's magnificent architectural heritage spanning over 5000 years. From the iconic Taj Mahal 
            to ancient cave temples, every monument tells a story of India's glorious past. Explore UNESCO World 
            Heritage Sites that showcase the country's rich cultural tapestry.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_culture_section():
    """Render arts and culture section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🎭 Arts & Culture</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            Immerse yourself in India's vibrant cultural landscape. From classical dance forms like Bharatanatyam 
            and Kathak to folk traditions that vary from state to state. Experience colorful festivals, traditional 
            music, and age-old customs that continue to thrive in modern India.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_adventure_section():
    """Render adventure and nature section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🏔️ Adventure & Nature</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            From the snow-capped peaks of the Himalayas to the pristine beaches of Goa, India offers diverse 
            landscapes for every adventure seeker. Trek through dense forests, spot wildlife in national parks, 
            or find serenity in the backwaters of Kerala.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_cuisine_section():
    """Render culinary journey section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🍛 Culinary Journey</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            Embark on a gastronomic adventure through India's diverse culinary landscape. Each region offers 
            unique flavors, spices, and cooking techniques. From street food delights to royal feasts, 
            Indian cuisine is a celebration of taste, tradition, and hospitality.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_spirituality_section():
    """Render spiritual experiences section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🕉️ Spiritual Experiences</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            India is the birthplace of major religions and spiritual practices. Visit ancient temples, 
            participate in yoga retreats, witness the evening aarti at Varanasi ghats, or find inner peace 
            in mountain monasteries. Discover the spiritual dimension that defines India's soul.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_crafts_section():
    """Render handicrafts and textiles section"""
    st.markdown("""
    <div style="text-align: center; padding-top: 50px; margin-bottom: 20px;">
        <h2 style="font-size: 2.5rem; font-weight: bold; color: #FF6B35;">🎨 Handicrafts & Textiles</h2>
    </div>
    <div class="explore-card">
        <p class="feature-description">
            Marvel at India's incredible handicraft traditions passed down through generations. From intricate 
            embroidery and handwoven textiles to pottery, jewelry, and woodwork. Each region specializes in 
            unique crafts that reflect local culture and artistic excellence.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_call_to_action():
    """Render the call to action section"""
    st.markdown("""
    <div style="text-align: center; padding: 40px 20px; 
                background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(76, 175, 80, 0.1)); 
                border-radius: 15px; margin: 40px 0;">
        <h2 style="color: #4CAF50; margin-bottom: 20px;">Ready to Explore?</h2>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
            Plan your journey to experience the incredible diversity, rich heritage, and warm hospitality 
            that makes India truly incredible. Every visit reveals new wonders and creates lasting memories.
        </p>
    </div>
    """, unsafe_allow_html=True)