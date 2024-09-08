from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from nltk.tokenize import word_tokenize
from common import youtubetranscript,web_data,videogenre,models,languages,match_back_language
def app():
    st.title("EasySummary")
    youtube_url = st.text_input("YouTube URL (can enter multiple links separated by a , ")
    all_language=[]
    for value in languages.values():
        all_language.append(value)
    all_language=tuple(all_language)
    default_language='English'

    video_language = st.selectbox('select the language in the video',all_language,index=all_language.index('English'))
    translate_video_language_to = st.selectbox(
    'The Video Transcript is in:', 
    [default_language], 
    index=0, 
    disabled=True
)
    website_url = st.text_input('Enter the website URL')
    if st.button('Submit'):
        with st.spinner('Processing'):
            genre=None
            language_in=None
            
            if website_url=='' and youtube_url!="":
                Text=''
                Text+=youtubetranscript(youtube_url,language=match_back_language(video_language))
                genre=videogenre(models=models,transcript=Text)
                if Text!="":
                    st.session_state['Text']=Text
                if genre!=None:
                    st.session_state['Genre']=genre
                if language_in!=None:
                    st.session_state['language_in']=translate_video_language_to
                    st.session_state['content']='Youtube_Only'
            elif website_url!='' and youtube_url!="":
                Text=''
                Text+=youtubetranscript(youtube_url,language=match_back_language(video_language))
                Text+=web_data(website_url)
                if Text!="":
                    st.session_state['Text']=Text
                if language_in!=None:
                    st.session_state['language_in']=translate_video_language_to
                st.session_state['content']='Youtube_and_web'
            else:
                Text=''
                Text+=web_data(website_url)
                if Text!="":
                    st.session_state['Text']=Text
                st.session_state['content']='web'
        
if __name__=='__main__':
    app.run()

        


