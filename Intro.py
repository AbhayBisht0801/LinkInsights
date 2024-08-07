from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from nltk.tokenize import word_tokenize
from common import youtubetranscript,WebBaseLoader,videogenre,models
def app():
    st.title("EasySummary")
    youtube_url = st.text_input("YouTube URL (can enter multiple links separated by a , ")
    language = st.text_input('Language spoken in the video(Default English)')
    translate_video_language_to=st.text_input('Language you want the transcript to be in.(Default English)')
    website_url = st.text_input('Enter the website URL')
    if st.button('Submit'):
        genre=None
        
        
        if website_url=='' and youtube_url!="":
            Text=''
            Text+=youtubetranscript(youtube_url,language=language,translation=translate_video_language_to)
            genre=videogenre(models=models,transcript=Text)
        elif website_url!='' and youtube_url!="":
            Text=''
            Text+=youtubetranscript(youtube_url,language=language,translation=translate_video_language_to)
            Text+=WebBaseLoader(website_url)
        if Text!="":
            st.session_state['Text']=Text
        if genre!=None:
            st.session_state['Genre']=genre

    print(st.session_state.get('Genre'))
if __name__=='__main__':
    app.run()

        


