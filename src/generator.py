import os
from dotenv import load_dotenv
from groq import Groq
from src.config import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def stream_generate(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in response:
        token = chunk.choices[0].delta.content
        if token:
            yield token