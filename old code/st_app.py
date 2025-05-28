import streamlit as st
from utils import generate_script

#Applying Styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
    }
</style>""", unsafe_allow_html=True)


#Creating Session State Variable
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''


st.title('😎 Youtube Script Writing Tool')

#Sidebar to capture the OpenAI API key
st.sidebar.title("🗝️")
st.session_state['API_Key'] = st.sidebar.text_input("What's your API key?", type="password")
st.sidebar.image('./Youtube.jpg', use_container_width=True)

#Captures User Inputs
prompt = st.text_input('Please provide the topic of the video', key="prompt") #The box for the text prompt
video_length = st.text_input('Expected Video Length ⏱️ (in minutes)',key="video_lenght") #The box for the text prompt
creativity = st.slider("Creativity Level 🧑‍🎨 - (0 LOW || 1 HIGH)", 0.0, 1.0,0.2,step=0.1)


submit = st.button("Generate Script for me")


if submit:
    if st.session_state['API_Key']:
        try:
            search_result, title, script = generate_script(prompt, video_length, creativity, st.session_state['API_Key'])
            
            st.success('Hope you like this script 🥲')

            # Display Title
            st.subheader("Title: 🔥")
            st.write(title)

            # Display Video Script
            st.subheader("Your Video Script: 📝")
            st.write(script)

            # Display Search Engine Result
            st.subheader("Check Out - DuckDuckGo Search: 🔍")
            with st.expander('Show me 👀'):
                st.info(search_result)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Oops! Nice try but no free lunch around here 😏 Please provide API key.....")


