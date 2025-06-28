
import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def get_qa_chain(vectorstore):
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base="https://api.together.xyz/v1",
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7,  # Controls randomness            
        max_tokens=1024
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
