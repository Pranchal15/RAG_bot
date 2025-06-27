from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

def get_embedder():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def create_vectorstore(chunks, batch_size=32):
    embedder = get_embedder()
    vectorstore = FAISS.from_documents(chunks, embedder)
    return vectorstore
