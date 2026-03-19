import streamlit as st
from src.vectordb import VectorStore
from src.rag_pipeline import run_rag

DB_PATH = "vectordb"

@st.cache_resource
def load_db():
    return VectorStore.load(DB_PATH)

db = load_db()

st.set_page_config(page_title="RAG Chatbot")

st.title("📚 AI Document Chatbot")

# Sidebar
st.sidebar.write("Model: LLaMA3 (Groq)")
st.sidebar.write(f"Chunks: {db.count()}")
query = st.text_input("Ask your question:")

if query:
    stream, sources = run_rag(query, db)

    st.subheader("Answer")
    st.write_stream(stream)

    st.subheader("Sources")
    for s in sources:
        st.markdown(f"**Score: {s['score']:.2f}**")
        st.info(s["text"])