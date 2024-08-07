from common import models,qna_chain
import  streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
def app():
    try:
        Text=st.session_state.get('Text')
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        st.title("QNA")
        for message in st.session_state.chat_history:
            if isinstance(message,HumanMessage):
                with st.chat_message('Human'):
                    st.markdown(message.content)
            else:
                with st.chat_message('AI'):
                    st.markdown(message.content)
        user_qeury=st.chat_input('Your message')
        if user_qeury is not None and user_qeury!='':
            st.session_state.chat_history.append(HumanMessage(user_qeury))
            with st.chat_message('Human'):
                st.markdown(user_qeury)
            with st.chat_message('AI'):
                ai_response=qna_chain(models,Text,user_qeury)
                st.markdown(ai_response)

            st.session_state.chat_history.append(AIMessage(ai_response))
    except Exception as e:
        st.error('Please Fill the Input Page')
if __name__=='__main__':
    app.run()


            
