# 🤖 Loan RAG Chatbot

A powerful Retrieval-Augmented Generation (RAG) chatbot that lets you chat with your **loan dataset** in `.csv` or `.zip` format. Built using **Streamlit**, **LangChain**, **FAISS**, and **HuggingFace Transformers**, the chatbot allows users to ask natural language questions and get meaningful answers based on the dataset.

---

## 🧠 Overview

This app enables users to:
- Upload structured data files (CSV or ZIP containing CSVs)
- Process and embed the data using HuggingFace models
- Ask any natural language question about the data
- Get accurate, contextual answers without relying on OpenAI APIs

It’s **completely local** and suitable for offline use!

---

## 🛠️ Tech Stack

| Component         | Library / Tool              |
|------------------|-----------------------------|
| Web Interface     | [Streamlit](https://streamlit.io)       |
| RAG Chain         | [LangChain](https://www.langchain.com) |
| Embeddings        | HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store      | FAISS                       |
| Language Model    | `google/flan-t5-base` (via HuggingFace Transformers) |
| Data Processing   | `pandas`, `scikit-learn`, `torch`        |

---

## 🚀 How to Run It Locally

### 1️⃣ Clone the Repository
git clone https://github.com/DivyanshuCh07/loan-rag-chatbot
cd loan-rag-chatbot

### 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Launch the App
streamlit run main.py

### ❓ Sample Questions to Try
What are the common reasons for loan rejection?
What is the most common purpose for applying for a loan?
How many applicants are self-employed?
List the applicants with poor credit scores.
What is the average loan amount requested?


👨‍💻 Author
Built with ❤️ by Divyanshu Choudhary
