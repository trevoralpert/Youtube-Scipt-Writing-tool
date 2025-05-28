import streamlit as st
from utils2 import generate_script
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Applying Styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color: #ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color: #FFFFFF;
}
</style>""", unsafe_allow_html=True)

st.title('😎 YouTube Script Writing Tool')

# Sidebar image only
st.sidebar.image('./Youtube.jpg', use_container_width=True)

# Captures User Inputs
prompt = st.text_input('Please provide the topic of the video', key="prompt")  # The box for the text prompt
video_length = st.text_input('Expected Video Length ⏱️ (in minutes)', key="video_length")  # The box for the video length
creativity = st.slider("Creativity Level 🧑‍🎨 - (0 LOW || 1 HIGH)", 0.0, 1.0, 0.2, step=0.1)

submit = st.button("Generate Script for me")

if submit:
    if OPENAI_API_KEY and SERPAPI_API_KEY:
        try:
            search_result, title, script = generate_script(prompt, video_length, creativity, OPENAI_API_KEY, SERPAPI_API_KEY)

            st.success('Hope you like this script 🥲')

            # Display Title
            st.subheader("Title: 🔥")
            st.write(title)

            # Display Video Script
            st.subheader("Your Video Script: 📝")
            st.write(script)

            # Display Search Engine Result
            st.subheader("Check Out - Google Search: 🔍")
            with st.expander('Show me 👀'):
                st.info(search_result)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please set your OpenAI and SerpAPI keys in the .env file.")
