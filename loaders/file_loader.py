import os
import tempfile
# from langchain.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader
from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader

def load_file(file):
    suffix = os.path.splitext(file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    if suffix == ".pdf":
        print("hi, i am a pdf")
        return PyMuPDFLoader(tmp_path).load()
    elif suffix == ".docx":
        return Docx2txtLoader(tmp_path).load()
    elif suffix == ".txt":
        return TextLoader(tmp_path).load()
    else:
        raise ValueError("Unsupported file format")
