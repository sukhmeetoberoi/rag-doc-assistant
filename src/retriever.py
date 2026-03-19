from src.embedding import embed
from src.config import TOP_K

def retrieve(query, vectordb):
    q_emb = embed([query])[0]
    return vectordb.search(q_emb, k=TOP_K)