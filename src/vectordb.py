import chromadb
from chromadb.config import Settings

class VectorStore:
    def __init__(self, persist_dir="vectordb"):
        self.persist_dir = persist_dir

        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=Settings(anonymized_telemetry=False)
        )

        self.collection = self.client.get_or_create_collection(
            name="docs"
        )

    def add(self, embeddings, texts):
        # Clear old data (IMPORTANT for rebuild)
        if self.collection.count() > 0:
            self.collection.delete(where={})

        ids = [str(i) for i in range(len(texts))]

        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=texts,
            ids=ids
        )

    def search(self, query_embedding, k=3):
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k
        )

        docs = []
        for i in range(len(results["documents"][0])):
            docs.append({
                "text": results["documents"][0][i],
                "score": results["distances"][0][i] if "distances" in results else 1.0
            })

        return docs

    def count(self):
        return self.collection.count()

    def save(self):
        pass

    @staticmethod
    def load(persist_dir="vectordb"):
        return VectorStore(persist_dir)