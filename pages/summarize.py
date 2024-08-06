import streamlit as st
from common import summarize_video,models,add_html_to_docx
Text=st.session_state['Text']
genre=st.session_state['Genre']
result=summarize_video(Text,models,genre)
formating=add_html_to_docx(result)
with st.container():
    st.write(formating)

