from langchain_community.document_loaders import YoutubeLoader
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from bs4 import BeautifulSoups
load_dotenv()
def youtubetranscript(links):
    text=[]
    for i in links.split(','):
        loader=YoutubeLoader.from_youtube_url(i,language=['en','hi'],translation='en')
        Transcript=loader.load()
        text+=Transcript[0].page_content
    return text
def videogenre(models,transcript):
    
    prompt = '''
    Based on the provided YouTube video transcript, classify the genre into one of the following categories:
    - Case Study
    - Educational/Tutorial
    - Documentary
    - Podcast/Interview/Debate
    - News/Current Affairs
    - Other

    Please provide only the genre from the list above.

    Input Transcript:
    {Transcript}
    '''
    template = PromptTemplate(input_variables=['Transcript'], template=prompt)
    content_genre=models.invoke(template.format(Transcript=transcript)).content
    return content_genre
def web_data(link):
    loader=WebBaseLoader(link)
    data=loader.load()
    return data
def add_html_to_docx(html, doc):
    for element in html:
        if element.name == "h1":
            run = doc.add_heading(level=1).add_run(element.text)
            run.font.size = Pt(24)
        elif element.name == "p":
            p = doc.add_paragraph()
            run = p.add_run(element.text)
        elif element.name == "ul":
            for li in element.find_all("li"):
                p = doc.add_paragraph(style='List Bullet')
                run = p.add_run(li.text)


