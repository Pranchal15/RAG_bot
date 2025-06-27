from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def get_qa_chain(vectorstore):
    print("qa chain coming up")
    llm = ChatOpenAI(
        model_name="./models/mistral",
        base_url="http://localhost:8000/v1",  # point to your vLLM server
        api_key="EMPTY"  # vLLM just needs a placeholder
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )
