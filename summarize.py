import streamlit as st
from common import summarize_video, models, add_html_to_docx, markdown_result, summarize_web_and_vid_or_web

def app():
    try:
        # Get the session state values safely
        
        content = st.session_state.get('content')
        Text = st.session_state.get('Text')
       
        if content is None or Text is None:
            raise KeyError

        # Process based on the 'content' type
        if content == 'Youtube_Only':
            genre = st.session_state.get('Genre', None)
            output = summarize_video(Text, models, genre)
            with st.container():
                st.write(output)
            
        elif content == 'web' or content == 'Youtube_and_web':
            output = summarize_web_and_vid_or_web(Text, models)
            with st.container():
                st.write(output)
        
    except KeyError:
        st.error('Please Enter all required fields on the Input Page')
        
if __name__ == '__main__':
    app()
