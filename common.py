from langchain_community.document_loaders import YoutubeLoader,WebBaseLoader
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
models=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
def tokenize(lang):
    return word_tokenize(lang)
def youtubetranscript(links,language,translation):
    text=[]
    if language=="" and translation=="":
    
        for i in links.split(','):
            loader=YoutubeLoader.from_youtube_url(i)
            Transcript=loader.load()
            text+=Transcript[0].page_content
        return text
    elif language !="":
        for i in links.split(','):
            loader=YoutubeLoader.from_youtube_url(i,language=language)
            Transcript=loader.load()
            text+=Transcript[0].page_content
        return text
    else:
        for i in links.split(','):
            loader=YoutubeLoader.from_youtube_url(i,language=language,translation=translation)
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
    text=''
    for i in link.split(','):
        loader=WebBaseLoader(i)
        text+=loader.load()
    return text
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
def split_text(text):
    text_split=RecursiveCharacterTextSplitter(chunk_size=4000,chunk_overlap=500)
    return text_split.split_text(text)
def qna_chain(models,text,question):
    chain=load_summarize_chain(models,chain_type='map_rerank',return_intermediate_steps=True)
    result=chain({'input_documents':text,'question':question},return_only_outputs=True)
    return result.stream
def report_creation(models,text,format):
    report_template="""Your Have to generate a  Report based following data Below:
    '{text}'
    The Format for the Report is as Follows:
    '{Format}'"""
    models.get_
    prompt=PromptTemplate(template=report_template,input_variables=['text','Format'])
    result=models.invoke(prompt.format(text=text,Format=format))
    return result
def summarize_video(Transcript,models,content_genre):
    if content_genre.replace('\n','').strip()=='Educational/Tutorial':
        prompt='''Summarize the Transcript in points and breifly describe the
        following transcript if the video involves with respect to coding tutorial then write the piece of code for  the following:
        {Transcript}'''
        template = PromptTemplate(input_variables=['Transcript'], template=prompt)
        result=models.invoke(template.format(Transcript=Transcript)).content
    elif content_genre.replace('\n','').strip()=='Case Study':
        prompt='''Summarize the Transcript in points and breifly describe the
        following transcript:
        {Transcript}'''
        template = PromptTemplate(input_variables=['Transcript'], template=prompt)
        result=models.invoke(template.format(Transcript=Transcript)).content
    elif content_genre.replace('\n','').strip()=='Podcast/Interview/Debate':
        prompt='''Give the point of Discussion and give the summary of them with respect to the  following Transcript:
        {Transcript}'''
        template = PromptTemplate(input_variables=['Transcript'], template=prompt)
        result=models.invoke(template.format(Transcript=Transcript)).content
    return result
def summarize_web_and_vid(Text):
    prompt="""Write the concise summary of the following:
    "{text}" 
    CONCISE SUMMARY:
    """
    combine_prompt="""
    Write a concise summaru of the following text delimited by triple backqoutes,
    Return your response in bullet points which covers the key points of the text.
    ```{text}```
    BULLET POINT SUMMARY:
    """
    combine_prompt_template=PromptTemplate(template=combine_prompt_template,input_variables=['text'])
    summary_prompt=PromptTemplate(template=prompt,input_variables=['text'])
    summary_chain=load_summarize_chain(llm=models,chain_type='map_reduce',map_prompt=summary_prompt,combine_prompt=combine_prompt_template)
    output=summary_chain(Text)
    return output






