# 🧠 Fine-Tuned RAG Chatbot with Streaming Responses

An end-to-end **Retrieval-Augmented Generation (RAG)** chatbot that answers user queries based on a legal document using **LLaMA 3.1 8B Instant**, **ChromaDB**, and a **Streamlit UI with real-time streaming responses**.

---

## 🚀 Demo

🔗 **Project Links**
* 🎬 Demo Video: [Watch Demo](https://drive.google.com/file/d/1xCNzkKOy78amtJdVeCA8helMRRlKJAKc/view?usp=sharing)
  

---

## 📌 Overview

This project demonstrates how to build a **context-aware AI chatbot** that generates **accurate and grounded responses** by retrieving relevant information from documents before generating answers.

Unlike traditional chatbots, this system:

* ❌ Avoids hallucinations
* ✅ Uses **retrieved context**
* ⚡ Streams responses in real-time

---

## 🏗️ System Architecture

### 🔹 Document Processing Pipeline

* Document Ingestion
* Text Cleaning
* Chunking (100–300 words)
* Embedding Generation
* Storage in ChromaDB

### 🔹 Query Processing Pipeline

* User Query
* Query Embedding
* Similarity Search
* Top-K Retrieval
* Prompt Construction
* LLM Response (Streaming)

---

## 🔄 RAG Pipeline

1. **Document Chunking**

   * Sentence-aware splitting
   * 100–300 word chunks with overlap

2. **Embedding**

   * Model: `all-MiniLM-L6-v2`

3. **Vector Database**

   * **ChromaDB** for efficient semantic retrieval

4. **Retriever**

   * Cosine similarity
   * Top-K relevant chunks

5. **Generator**

   * **LLaMA 3.1 8B Instant**
   * Generates grounded answers

---

## 🧾 Prompt Template

```text
You are a helpful AI assistant. Answer strictly based on the context.

Context:
{retrieved_chunks}

Question:
{user_query}

Answer:
```

---

## ⚡ Streaming Responses

* Token-by-token output
* Implemented using generator functions
* Enhances user experience with real-time interaction

---

## 🖥️ Streamlit Features

* 💬 Chat interface
* ⚡ Real-time streaming responses
* 📄 Source chunk display
* 📊 Sidebar:

  * Model used (LLaMA 3.1 8B Instant)
  * Number of chunks indexed
* 🔄 Reset chat functionality

---

## 📁 Project Structure

```
rag-doc-assistant/
│
├── data/
│   └── document.pdf              # Input document
│
├── chunks/
│   └── chunks.json              # Processed text chunks
│
├── vectordb/                    # Stored Chroma vector database
│
├── notebooks/
│   └── preprocessing.ipynb      # Data preprocessing experiments
│
├── src/
│   ├── config.py                # Configuration settings
│   ├── document_processor.py    # Text extraction & cleaning
│   ├── embedding.py             # Embedding generation logic
│   ├── vectordb.py              # ChromaDB operations
│   ├── retriever.py             # Semantic search logic
│   ├── prompt.py                # Prompt template
│   ├── generator.py             # LLM response generation
│   └── rag_pipeline.py          # End-to-end pipeline
│
├── app.py                       # Streamlit chatbot UI
├── build_vectordb.py            # Script to create vector DB
├── requirements.txt             # Dependencies
├── .env                         # API keys (not committed)
└── README.md                    # Project documentation
```


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_LINK
cd your-repo-name
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Build Vector Database (IMPORTANT ⚠️)

Before running the chatbot, you must process the document and create embeddings:

```bash
python build_vectordb.py
```

This step will:

* 📄 Load and clean the document
* ✂️ Chunk the text
* 🧠 Generate embeddings
* 🗂️ Store them in **ChromaDB**

---

### 4️⃣ Run the Chatbot

```bash
streamlit run app.py
```

---

### ⚠️ Note

If you skip the vector database step, the chatbot will not return meaningful responses.


---

## 📊 Example Queries

* "What happens if a user violates eBay policies?"
* "Does eBay guarantee product quality?"
* "How are disputes resolved?"

---

## ⚠️ Challenges

* 🔸 Hallucination (reduced via RAG)
* 🔸 Latency due to LLM inference
* 🔸 Retrieval errors if chunking is weak

---

## 🚀 Future Improvements

* Use **bge-large embeddings**
* Add **reranking model**
* Implement **hybrid search (BM25 + vector)**
* Fine-tune LLM on domain-specific data

---

## 💡 Key Highlight

> This system ensures grounded responses by conditioning the LLM strictly on retrieved document context, significantly reducing hallucination.

---

## 📜 License

This project is developed as part of an AI engineering assignment and is intended for educational purposes.

---

## 👨‍💻 Author

**Sukhmeet Singh Oberoi**

* 📧 [sukhmeetoberoi@gmail.com](mailto:sukhmeetoberoi@gmail.com)
* 🔗 GitHub: https://github.com/sukhmeetoberoi

---
