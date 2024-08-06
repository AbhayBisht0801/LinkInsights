import streamlit as st
from common import report_creation,models,add_html_to_docx
from streamlit import session_state
Text=session_state['Text']
report_format=st.text_input('Enter the required report format')
if st.button('Submit'):
    result=report_creation(models,text=Text,report_creation=report_format)
    formating=add_html_to_docx(result)
    with st.container():
        st.write(formating)
    


