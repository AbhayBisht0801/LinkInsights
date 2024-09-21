import streamlit as st
from common import report_creation,models,add_html_to_docx,html_content_parser,displayPDF,doc_to_pdf
from streamlit import session_state
from docx import Document
from bs4 import BeautifulSoup
from markdown import markdown
from doc2pdf import convert
def app():
    Text=session_state.get('Text')
    
    if Text!="":
        Report_type =st.text_input('Enter the kind of report u want to generate')
        report_format=st.text_input("Enter the required report format with a , ")
        st.session_state['Report_type']=Report_type
        st.session_state['report_format']=report_format
        if st.button('Generate_report'):
            report_format=st.session_state.get('report_format')
            Report_type=st.session_state.get('Report_type')
            
            if Report_type=="" and report_format=="":
                st.error('Please fill the required fields')
                
            else:
                doc = Document()
                result=report_creation(models,text=Text,format=report_format,type_of_report=Report_type)
                html_content=html_content_parser(result)
                print(html_content)
                print(Report_type,report_format)
                add_html_to_docx(html_content, doc)
                doc.save("report.docx")
                
        

            
            
    else:
        st.error('Please Fill the Input Page')
if __name__=='__main__':
    app.run()

    


