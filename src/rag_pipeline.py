from src.retriever import retrieve
from src.prompt import build_prompt
from src.generator import stream_generate

def run_rag(query, vectordb):
    docs = retrieve(query, vectordb)

    context = "\n\n".join([d["text"] for d in docs])

    prompt = build_prompt(context, query)

    return stream_generate(prompt), docs