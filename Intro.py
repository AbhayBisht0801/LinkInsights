import streamlit as st
from common import summarize_video,models,add_html_to_docx,markdown_result
def app():
    try:
        Text=st.session_state.get('Text')
        print(Text)
        genre=st.session_state.get('Genre')
        
        print(genre)
        output=summarize_video(Text,models,genre)
        print(output)
        
        with st.container():
            st.write(output)
    except  KeyError:
        st.error('Please Enter in the Input Page')
if __name__=='__main__':
    app.run()