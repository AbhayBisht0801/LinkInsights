from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from nltk.tokenize import word_tokenize
from common import youtubetranscript,WebBaseLoader,videogenre

st.title("EasySummary")
youtube_url = st.text_input("YouTube URL (can enter multiple links separated by a , ")
language = st.text_input('Language spoken in the video(Default English)')
translate_video_language_to=st.text_input('Language you want the transcript to be in.(Default English)')
website_url = st.text_input('Enter the website URL')
if st.button('Submit'):
    if website_url=='' and youtube_url!="":
        Text=''
        Text+=youtubetranscript(youtube_url,language=language,translation=translate_video_language_to)
        genre=videogenre(Text)
    elif website_url!='' and youtube_url!="":
        Text=''
        Text+=youtubetranscript(youtube_url,language=language,translation=translate_video_language_to)
        Text+=WebBaseLoader(website_url)
    if 'Text' not in st.session_state:
        st.session_state.Text=Text
    if genre!="":
        if 'Genre' not in st.session_state:
            st.session_state.Genre=genre
if st.button('QNA'):
    st.switch_page('qna.py')
if st.button('Report'):
    st.switch_page('report.py')
if st.button('Summarize'):
    st.switch_page('summarize.py')

        


