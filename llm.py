from langchain_groq import ChatGroq
from config import groq_api_key

def get_llm():
    llm=ChatGroq(
        api_key=groq_api_key,
        model="openai/gpt-oss-20b",
        temperature=0.3
    )

    return llm