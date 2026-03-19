import json
from src.document_processor import process_document
from src.embedding import embed
from src.vectordb import VectorStore

DOC_PATH = "data/document.pdf"
CHUNK_PATH = "chunks/chunks.json"

# Step 1: Process document
chunks = process_document(DOC_PATH)

# Step 2: Save chunks
with open(CHUNK_PATH, "w") as f:
    json.dump(chunks, f, indent=2)

if not chunks:
    print("Error: No text could be extracted from the PDF. The file might be corrupted or scanned.")
    exit(1)

# Step 3: Create embeddings
embeddings = embed(chunks)

# Step 4: Create vector DB (NO dimension needed)
db = VectorStore()

# Step 5: Add data
db.add(embeddings, chunks)

# Step 6: Save DB (Chroma persists internally)
db.save()

print(f"Chunks created: {len(chunks)}")
print("Vector DB stored in /vectordb successfully!")