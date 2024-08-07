import streamlit as st
from streamlit_option_menu import option_menu
import report
import summarize
import qna
import Intro



class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:        
            app = option_menu(
                menu_title='Menu ',
                options=['Input Page','QNA','Report','Summary'],
                icons=['Input Page','QNA','Report','Summary'],
                menu_icon='menu-button',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        
        if app == 'Input Page':
            Intro.app()
        elif app == "QNA":
            qna.app()
        elif app == "Report":
            report.app()
        elif app =='Summary':
            summarize.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()