from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def embed(texts):
    """
    Convert text chunks into vector embeddings.

    Why embeddings?
    - Enables semantic search instead of keyword matching
    - Helps retrieve meaning-based relevant chunks
    """

    return model.encode(texts, normalize_embeddings=True)