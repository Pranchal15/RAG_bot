import streamlit as st
from loaders.file_loader import load_file
from utils.text_splitter import split_documents
from utils.embedder import create_vectorstore
from rag.qa_pipeline import get_qa_chain
from dotenv import load_dotenv

load_dotenv()
st.title("📄 RAG Chatbot with File Upload")

uploaded_files = st.file_uploader("Upload documents", accept_multiple_files=True, type=["pdf", "docx", "txt"])

if uploaded_files:
    all_chunks = []
    for file in uploaded_files:
        print("got a file, processing it")
        with st.spinner(f"Processing {file.name}..."):
            docs = load_file(file)
            chunks = split_documents(docs)
            all_chunks.extend(chunks)
    print(all_chunks,"chunks")
    vectorstore = create_vectorstore(all_chunks)
    qa_chain = get_qa_chain(vectorstore)
    print("qa chain",qa_chain)
    st.success("✅ Files processed! Ask a question below:")

    query = st.text_input("🔍 Ask a question about your documents:")
    print(query, "what a qeury")

    if query:
        with st.spinner("Generating answer..."):
            response = qa_chain.invoke(query)
            st.markdown(f"**Answer:** {response}")
