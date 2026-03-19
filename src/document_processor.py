import re
from pypdf import PdfReader
from nltk.tokenize import sent_tokenize

def load_pdf(path):
    import fitz

    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text() or ""
        return text
    except Exception as e:
        print(f"PDF parsing failed: {e}")
        return ""

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, chunk_size=200):
    sentences = sent_tokenize(text)

    chunks = []
    current = []
    length = 0

    for sentence in sentences:
        words = sentence.split()

        if length + len(words) <= chunk_size:
            current.append(sentence)
            length += len(words)
        else:
            chunks.append(" ".join(current))
            current = [sentence]
            length = len(words)

    if current:
        chunks.append(" ".join(current))

    return chunks

def process_document(path):
    raw = load_pdf(path)
    clean = clean_text(raw)
    return chunk_text(clean)