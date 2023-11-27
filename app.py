import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="Q&A Chatbot")
st.header("Hello, What do you want to talk about")

from dotenv import load_dotenv
load_dotenv()

chat=ChatOpenAI(temperature=0.6)

if 'flowmessages' not in st.session_state:  #If no content given then the AI will have this as default system message content
    st.session_state['flowmessages']=[SystemMessage(content="You are a chatbot")]

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask")

if submit: #If submit button clicked
    st.subheader("The response is")
    st.write(response)