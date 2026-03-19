from src.embedding import embed
from src.config import TOP_K

def retrieve(query, vectordb):
    """
    Convert query into embedding and retrieve relevant chunks.
    """
    q_emb = embed([query])[0]
    return vectordb.search(q_emb, k=TOP_K)