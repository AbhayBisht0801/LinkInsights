import streamlit as st
from common import report_creation,models,add_html_to_docx,html_content_parser,displayPDF,doc_to_pdf
from streamlit import session_state
from docx import Document
from bs4 import BeautifulSoup
from markdown import markdown
from doc2pdf import convert
def app():
    try:
        Text=session_state.get('Text')
        Report_type =st.text_input('Enter the kind of report u want to generate')
        report_format=st.text_input("Enter the required report format with a , ")
        if st.button('Generate_report'):
            if Report_type!="" and report_format!="":
                doc = Document()
                result=report_creation(models,text=Text,format=report_format,type_of_report=Report_type)
                html_content=html_content_parser(result)
                
                print('hello')
                print(html_content)
    # Add the parsed HTML content to the Word document
                add_html_to_docx(html_content, doc)
                doc.save("report.docx")
                
            else:
                st.error('Please Fill the Following text')
        

            
            
    except KeyError:
        st.error('Please Fill the Input Page')
if __name__=='__main__':
    app.run()

    


