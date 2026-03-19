def build_prompt(context, query):
    return f"""
You are an AI assistant.

Answer ONLY using the context.
If not found, say "Not found in document".

Context:
{context}

Question:
{query}

Answer:
"""