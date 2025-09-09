import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings , ChatHuggingFace
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")  
#os.environ["HF_TOKEN"]


def get_pdf_text(pdf_docs):
    """Extract plain text from uploaded PDFs (simple first pass)."""
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=25)
    chunks = text_splitter.split_text(text)
    return chunks

def initialize_hf_llm():
            client = InferenceClient(token=HF_TOKEN, timeout=60)  # timeout here
            endpoint = HuggingFaceEndpoint(
                repo_id="google/gemma-2-2b-it",
                task="conversational",          # <-- change here
                client=client,
                temperature=0.1,
                top_p=0.95,
                max_new_tokens=256,
                repetition_penalty=1.05,
            )
            # Expose it as a ChatModel to LangChain
            return ChatHuggingFace(llm=endpoint)

def get_vector_store(text_chunks):
    """Build a Chroma vector store with HF Inference API embeddings (first pass)."""
    embeddings = HuggingFaceEndpointEmbeddings(
    model="BAAI/bge-small-en-v1.5",
    task="feature-extraction"
)
    return Chroma.from_texts(text_chunks, embedding=embeddings)

def build_history_aware_rag_chain(llm, vector_store):
    retriever = vector_store.as_retriever()
    cq_prompt = ChatPromptTemplate.from_messages([
        ("system", "Rewrite the user's question as a standalone question. Do not answer."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", "Use the context to answer concisely. If unknown, say you don't know.\n\n{context}"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    hist_retriever = create_history_aware_retriever(llm, retriever, cq_prompt)
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    return create_retrieval_chain(hist_retriever, qa_chain)