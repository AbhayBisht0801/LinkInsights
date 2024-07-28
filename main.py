from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from streamlit import session_state
st.title("EasySummary")
youtube_url = st.text_input('YouTube URL (can enter multiple links separated by a space or delimiter)')
language = st.text_input('Language spoken in the video other than English.(else default English)')
st.markdown("If multiple videos, enter the language for each in a list.")
website_url = st.text_input('Enter the website URL')
btn1 = st.button('QNA')
if btn1:
    
    st.session_state.runpage = "app1"

btn2 = st.button('Summarized Result')
btn3=st.button('Generate Report')
