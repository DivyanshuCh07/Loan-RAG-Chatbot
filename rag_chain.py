import os
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.docstore.document import Document
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def load_data_as_documents(file_path):
    df = pd.read_csv(file_path)
    docs = []
    for _, row in df.iterrows():
        content = "\n".join([f"{col}: {row[col]}" for col in df.columns])
        docs.append(Document(page_content=content))
    return docs

def build_vector_store(docs):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore

def build_rag_chain(vectorstore):
    # Load Hugging Face local model
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=256,
        do_sample=True,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
