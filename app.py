import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

st.title("ABDULLAH CHATBOT")
input_text = st.text_input("Search the topic you want")

# API Key from .env (not included in GitHub)
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.1-70b-versatile"
)

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond clearly and accurately."),
    ("user", "Question: {question}")
])

chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": input_text})
    st.write(response)
