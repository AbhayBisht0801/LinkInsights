from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from nltk.corpus import word_tokenizer
from streamlit import session_state
from common import youtubetranscript,WebBaseLoader,videogenre
st.title("EasySummary")
youtube_url = st.text_input('YouTube URL (can enter multiple links separated by a space or delimiter)')
language = st.text_input('Language spoken in the video')
website_url = st.text_input('Enter the website URL')

btn1 = st.button('QNA')
btn2 = st.button('Summarized Result')
btn3=st.button('Generate Report')
