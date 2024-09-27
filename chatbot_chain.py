import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory 

def get_chatbot_chain():

    loader = CSVLoader(file_path="test-data.csv")
    documents = loader.load()

    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0, model=os.environ.get("CHAT_GPT_MODEL"), streaming=True), retriever=vectorstore.as_retriever(), memory=memory)
    
    return chain                                   
