from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents_in_batches(uploaded_files, batch_size=1):
    """Loads documents from uploaded files in batches to avoid memory spikes."""
    for i in range(0, len(uploaded_files), batch_size):
        batch_files = uploaded_files[i:i+batch_size]
        docs = []
        for file in batch_files:
            loader = PyPDFLoader(file.name)
            docs.extend(loader.load())
        yield docs  # yields one batch of docs at a time

def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)
