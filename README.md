# 🔍 Information Retrieval RAG System

## Overview  
This project implements a **Retrieval-Augmented Generation (RAG)** system using **LangChain**, **Hugging Face Inference API**, and **ChromaDB**. It allows users to upload PDF documents and interact with them through a **Streamlit chatbot interface**. The chatbot supports multi-turn conversations and context-aware question rewriting.

---

## 💡 Key Features

- ✅ **PDF ingestion** and plain-text extraction  
- ✅ **Text chunking** using `RecursiveCharacterTextSplitter`  
- ✅ **Vector store** with `ChromaDB` and HF `BAAI/bge-small-en-v1.5` embeddings  
- ✅ **Conversational model** using `google/gemma-2-2b-it` via Hugging Face Inference API  
- ✅ **History-aware retriever and QA chain**  
- ✅ **Web interface** built with Streamlit  
- ✅ **Chat history persistence** across user sessions  

---

## 🧱 Architecture

```text
              ┌─────────────┐
              │  PDF Upload │◄───────────────┐
              └────┬────────┘                │
                   ▼                         │
         ┌────────────────────┐              │
         │ Extract Plain Text │              │
         └────────┬───────────┘              │
                  ▼                          │
       ┌─────────────────────────┐           │
       │ Chunk Text into Vectors │           │
       └────────┬────────────────┘           │
                ▼                            │
       ┌────────────────────────────┐        │
       │ Store in Chroma Vector DB │        │
       └────────┬───────────────────┘        │
                ▼                            │
     ┌───────────────────────────────┐       │
     │ History-Aware Retriever + QA  │◄──────┘
     └───────────────────────────────┘
                ▼
         ┌─────────────┐
         │ Chat Output │
         └─────────────┘
```

---

## 🧰 Tech Stack

| Component         | Technology / Tool                           |
|------------------|----------------------------------------------|
| Web UI           | Streamlit                                   |
| LLM              | `google/gemma-2-2b-it` via Hugging Face API |
| Embeddings       | `BAAI/bge-small-en-v1.5`                     |
| Vector Store     | `Chroma` + `LangChain`                      |
| Prompting        | `ChatPromptTemplate`, `MessagesPlaceholder` |
| Backend          | LangChain RAG chain (retrieval + generation)|
| Deployment       | `streamlit run app.py`                      |

---

## 📦 Installation

```bash
git clone https://github.com/your-user/Information_RAG.git
cd Information_RAG
pip install -e .
```

Or, with `pyproject.toml` (PEP 621):

```bash
pip install .
```

### ⚠️ Requirements
- Python ≥ 3.8
- Hugging Face token stored in `.env` as `HF_TOKEN`

Example `.env`:

```env
HF_TOKEN=your_huggingface_api_token_here
```

---

## 🚀 Usage

### Run the app:

```bash
streamlit run app.py
```

Then, go to [http://localhost:8501](http://localhost:8501) in your browser.

### Workflow:

1. Upload one or more PDFs in the sidebar
2. Click “Process” to:
   - Extract text
   - Chunk and embed
   - Initialize vector DB
   - Set up conversational chain
3. Start chatting with your documents in natural language

---

## 🧪 Example Prompt

> “What are the key responsibilities outlined in this document?”

The system will:
- Rewrite the question with context
- Retrieve relevant passages
- Answer using the LLM

---

## 📁 Project Structure

| File                  | Description                           |
|-----------------------|---------------------------------------|
| `app.py`              | Streamlit app and chat interface      |
| `helper.py`           | Logic for PDF parsing, embeddings, and RAG chain building:contentReference[oaicite:0]{index=0}  
| `pyproject.toml`      | Project metadata and dependencies:contentReference[oaicite:1]{index=1}  
| `trials.ipynb`        | Local testing / experimentation       |

---

## 📝 License

MIT License

---
