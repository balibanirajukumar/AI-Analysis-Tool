import os
import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory 
import pandas as pd


def get_chatbot_chain():
    st.title("CSV Document Loader")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file as a pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Convert DataFrame to CSV and save to a temporary file
        temp_file_path = "temp.csv"
        df.to_csv(temp_file_path, index=False)

        # Load the CSV file using CSVLoader
        loader = CSVLoader(file_path=temp_file_path)
        documents = loader.load()

        # Display the documents
        st.write(documents)
        vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0, model=os.environ.get("CHAT_GPT_MODEL"), streaming=True), retriever=vectorstore.as_retriever(), memory=memory)
        return chain
    else:
        st.write("Please upload a CSV file.")
    
    return None                                  
