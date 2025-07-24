import streamlit as st
import os
from rag_chain import load_data_as_documents, build_vector_store, build_rag_chain
from utils import extract_zip, cleanup_data_folder

st.set_page_config(page_title="RAG Q&A Chatbot")

st.title("🤖 RAG Q&A Chatbot")
st.markdown("Upload a `.zip` or `.csv` file or share a GitHub repo to chat with your data.")

uploaded_file = st.file_uploader("Upload .zip or .csv file", type=["zip", "csv"])

if uploaded_file:
    cleanup_data_folder()

    if uploaded_file.name.endswith(".zip"):
        extract_zip(uploaded_file, extract_to="data")
        data_files = [f for f in os.listdir("data") if f.endswith(".csv")]
        if not data_files:
            st.error("No .csv found inside the zip.")
            st.stop()
        file_path = os.path.join("data", data_files[0])
    elif uploaded_file.name.endswith(".csv"):
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    else:
        st.error("Unsupported file type.")
        st.stop()

    with st.spinner("Processing documents..."):
        docs = load_data_as_documents(file_path)
        vs = build_vector_store(docs)
        qa_chain = build_rag_chain(vs)

    st.success("Ready to chat with your data!")

    query = st.text_input("Ask a question about the data:")

    if query:
        with st.spinner("Generating answer..."):
            result = qa_chain.run(query)
            st.markdown(f"**Answer:** {result}")
else:
    st.info("Awaiting file upload...")
