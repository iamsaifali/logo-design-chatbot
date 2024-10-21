# import streamlit as st

# def sidebar():
#     with st.sidebar:
#         st.header("Logo Type")
#         logo_type = st.selectbox(
#             "Choose a logo type:",
#             [
#                 "Wordmark (Logotype)",
#                 "Lettermark (Monogram)",
#                 "Pictorial Mark (Brandmark or Symbol)",
#                 "Abstract Mark",
#                 "Mascot Logo",
#                 "Combination Mark",
#                 "Emblem Logo",
#                 "Dynamic Logo"
#             ]
#         )
#     return logo_type

import streamlit as st

def sidebar():
    with st.sidebar:
        st.header("Logo Type")
        logo_type = st.selectbox(
            "Choose a logo type:",
            [
                "Wordmark (Logotype)",
                "Lettermark (Monogram)",
                "Pictorial Mark (Brandmark or Symbol)",
                "Abstract Mark",
                "Mascot Logo",
                "Combination Mark",
                "Emblem Logo",
                "Dynamic Logo"
            ]
        )
        
        st.header("Image Generation Settings")
        model = st.selectbox(
            "Choose DALL-E model:",
            ["dall-e-3", "dall-e-2"]
        )
        
        image_size = st.selectbox(
            "Choose image size:",
            ["1024x1024", "512x512", "256x256"]
        )
        
        quality = st.selectbox(
            "Choose image quality:",
            ["standard", "hd"]
        )
        
        n = st.slider("Number of images to generate:", min_value=1, max_value=4, value=1)
        
    return logo_type, model, image_size, quality, n