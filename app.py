import streamlit as st
import os
from dotenv import load_dotenv
from components.sidebar import sidebar
from utils.openai_helper import generate_dalle_image, set_openai_api_key

st.set_page_config(page_title="Logo Design Chatbot", page_icon="🎨", layout="wide")

# Custom CSS to center content and add white space
st.markdown("""
    <style>
    .reportview-container {
        background-color: #ffffff;
    }
    .main > div {
        max-width: 900px;
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
        margin: 0 auto;
    }
    .stApp > header {
        background-color: transparent;
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .stAlert {
        background-color: #FFF9E6;
        color: #856404;
        border-color: #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

def load_api_key():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

def api_key_input():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown("# 🎨 Logo Design Chatbot")
        st.write("Enter your OpenAI API key:")
        api_key = st.text_input("OpenAI API Key", type="password", key="api_key_input", label_visibility="collapsed")
        
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            set_openai_api_key(api_key)
            st.success("API key set successfully!")
            if st.button("Continue to Logo Design"):
                st.session_state.api_key_entered = True
                st.experimental_rerun()
        else:
            st.warning("Please enter your OpenAI API key to continue.")

        st.markdown("---")
        st.info("Please enter your OpenAI API key to continue. "
                "This key will be used only for this session and will not be stored.")

def logo_design_chatbot():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.markdown("# 🎨 Logo Design Chatbot")

        # Sidebar options (you might want to integrate these differently)
        logo_type, model, image_size, quality, n = sidebar()

        # Main content
        st.header(f"Design a {logo_type}")
        user_input = st.text_area("Describe your logo design requirements:", height=150)

        if st.button("Generate Logo"):
            if user_input:
                with st.spinner("Generating logo..."):
                    image_prompt = f"Create a {logo_type} logo based on the following description: {user_input}"
                    image_urls = generate_dalle_image(image_prompt, model, image_size, quality, n)
                    
                    if isinstance(image_urls, str) and image_urls.startswith("An error occurred"):
                        st.error(image_urls)
                    else:
                        st.subheader("Generated Logo Concept(s):")
                        for i, url in enumerate(image_urls):
                            st.image(url, caption=f"DALL-E Generated Logo Concept {i+1}")
            else:
                st.warning("Please provide some design requirements.")

def main():
    api_key = load_api_key()
    
    if api_key:
        set_openai_api_key(api_key)
        logo_design_chatbot()
    else:
        if "api_key_entered" not in st.session_state:
            st.session_state.api_key_entered = False

        if not st.session_state.api_key_entered:
            api_key_input()
        else:
            logo_design_chatbot()

if __name__ == "__main__":
    main()