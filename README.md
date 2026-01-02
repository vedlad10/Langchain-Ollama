# Local AI Assistant using LangChain and Ollama

This project is a simple AI-powered question-answering application built using **LangChain**, **Ollama**, and **Streamlit**. It runs entirely on a local machine, making it cost-free and suitable for experimentation with LLM-based applications.

## 🚀 Features
- Uses a **locally hosted LLM** via Ollama (no API keys required)
- Built with **LangChain LCEL** (LangChain Expression Language)
- Interactive **Streamlit web interface**
- Clean prompt structuring using chat-based templates
- Lightweight and beginner-friendly setup

## 🛠 Tech Stack
- **Python**
- **LangChain**
- **Ollama**
- **Streamlit**
- **dotenv**

## ⚙️ How It Works
1. User enters a question in the Streamlit UI.
2. The input is formatted using a chat-based prompt template.
3. The formatted prompt is passed to a local LLM running via Ollama.
4. The model generates a response, which is parsed and displayed in the UI.

## 📦 Installation

```bash
pip install langchain langchain-community streamlit python-dotenv
⚠️ Note: This application is intended to run locally. Streamlit Cloud does not support local LLM servers such as Ollama.

