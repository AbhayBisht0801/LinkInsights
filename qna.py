from common import models,qna_chain

import  streamlit as st

from langchain_core.messages import HumanMessage,AIMessage

def app():
    if 'Text'  in st.session_state:
        Text=st.session_state.get('Text')
        st.header('Chat with the Input Data')
        
        if "chat_history" not in st.session_state:
                st.session_state.chat_history = []
                initial_message = AIMessage("Hi, how can I help you?")
                st.session_state.chat_history.append(initial_message)
        for message in st.session_state.chat_history:
                if isinstance(message, HumanMessage):
                    with st.chat_message('Human'):
                        st.markdown(message.content)
                else:
                    with st.chat_message('AI'):
                        st.markdown(message.content)
        user_query = st.chat_input('Ask Question based on your input website or youtube video')
        if user_query:
            st.session_state.chat_history.append(HumanMessage(user_query))
            with st.chat_message('Human'):
                st.markdown(user_query)

            ai_response = qna_chain(models=models,text=Text,question=user_query)
            with st.chat_message('AI'):
                st.markdown(ai_response)

            st.session_state.chat_history.append(AIMessage(ai_response))
    else:
         st.error('Please Fill the Input Page First')
    



if __name__=='__main__':
    app.run()


            
