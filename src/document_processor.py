import re
from pypdf import PdfReader
from nltk.tokenize import sent_tokenize

def load_pdf(path):
    """
    Load text from a document.
    Currently supports PDF and TXT files.
    """
    import fitz

    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text() or ""
        return text

    """Make a exception to handle the error of not able to read the pdf file """
    except Exception as e:
        print(f"PDF parsing failed: {e}")
        return ""

def clean_text(text):
    """
    Clean extra spaces and normalize text.
    Helps improve embedding quality.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, chunk_size=200):

    """
    Split text into smaller chunks.

    Why?
    - LLMs cannot process very large text at once
    - Smaller chunks improve retrieval accuracy
    """
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

    """
    Full preprocessing pipeline:
    Load → Clean → Chunk
    """

    raw = load_pdf(path)
    clean = clean_text(raw)
    return chunk_text(clean)