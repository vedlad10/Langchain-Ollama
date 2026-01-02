from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Prompt Template (LCEL supports tuple messages)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("LangChain Demo with Local LLM (Ollama)")
input_text = st.text_input("Search the topic you want")

# Local Ollama LLM (8GB-safe model)
llm = Ollama(model="llama3.2:3b")
output_parser = StrOutputParser()

# LCEL chain (NO LLMChain)
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
