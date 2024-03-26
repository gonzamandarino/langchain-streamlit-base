import streamlit as st
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

st.title('🦜🔗 Quickstart App')


with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.info(llm(text))
