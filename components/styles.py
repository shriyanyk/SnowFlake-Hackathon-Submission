import streamlit as st

def load_styles():
    """Load all custom CSS styles for the application"""
    st.markdown(
        """
        <style>
        /* Set the entire app background to black */
        .stApp {
            background-color: #000000;
        }

        /* General text styling */
        h1, h2, h3, p, label {
            color: white !important;
        }

        /* Iframe styling */
        iframe {
            border-radius: 12px;
            border: none;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }

        /* Hide Streamlit header and footer */
        header, footer {
            visibility: hidden;
        }

        /* Remove padding around content */
        .block-container {
            padding: 0 !important;
        }

        /* Navigation bar styling */
        .navigation {
            display: flex;
            justify-content: center;
            padding: 20px 0;
            background-color: transparent;
            margin-bottom: 30px;
            position: relative;
        }

        .navigation:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 15%;
            right: 15%;
            height: 1px;
            background: rgba(255, 255, 255, 0.1);
        }

        .nav-button-container {
            width: 140px;
            padding: 0 15px;
        }

        /* Button styling */
        .stButton > button {
            width: 100%;
            background-color: transparent !important;
            color: rgba(255, 255, 255, 0.7) !important;
            border: none !important;
            border-radius: 0 !important;
            padding: 10px 16px !important;
            cursor: pointer;
            transition: all 0.2s ease;
            font-weight: 400;
            font-size: 14px;
            margin: 0;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .stButton > button:hover {
            color: rgba(255, 255, 255, 1) !important;
            background-color: transparent !important;
            transform: none;
            box-shadow: none !important;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 4px 4px 0px 0px;
            color: white;
            padding: 10px 20px;
        }

        .stTabs [aria-selected="true"] {
            background-color: rgba(76, 175, 80, 0.3);
            border-bottom: 2px solid #4CAF50;
            color: white;
        }

        /* Content area */
        .content-area {
            padding: 0 20px;
        }

        /* Video container */
        .video-container {
            width: 80%;
            max-width: 800px;
            margin: 0 auto;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0px 12px 35px rgba(0, 0, 0, 0.4);
            margin-bottom: 20px;
            background: linear-gradient(145deg, rgba(40, 40, 40, 0.3), rgba(60, 60, 60, 0.2));
            padding: 8px;
        }

        .stVideo > div {
            border-radius: 15px !important;
            overflow: hidden !important;
        }

        .stVideo video {
            border-radius: 15px !important;
            width: 100% !important;
            height: auto !important;
        }

        .custom-video {
            border-radius: 15px;
            width: 100%;
            height: auto;
            box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.3);
        }

        /* Explore section */
        .explore-section {
            background: linear-gradient(135deg, rgba(0, 0, 0, 0.8), rgba(20, 20, 20, 0.9));
            padding: 60px 20px;
            margin: 40px 0;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .explore-card {
            background: linear-gradient(135deg, rgba(40, 40, 40, 0.6), rgba(60, 60, 60, 0.4));
            padding: 30px;
            margin: 20px 0;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .explore-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.4);
        }

        .section-title {
            color: #4CAF50 !important;
            font-size: 2.5rem;
            font-weight: 300;
            text-align: center;
            margin-bottom: 30px;
            letter-spacing: 1px;
        }

        .feature-title {
            color: #81C784 !important;
            font-size: 1.5rem;
            margin-bottom: 15px;
            font-weight: 400;
        }

        .feature-description {
            color: rgba(255, 255, 255, 0.8) !important;
            line-height: 1.6;
            font-size: 1rem;
        }

        /* File uploader */
        .stFileUploader {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 2px dashed rgba(255, 255, 255, 0.2) !important;
            border-radius: 12px !important;
            padding: 20px !important;
        }

        .stFileUploader label {
            color: rgba(255, 255, 255, 0.8) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
