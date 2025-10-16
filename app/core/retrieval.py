import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI

model = SentenceTransformer("all-MiniLM-L6-v2")
client = OpenAI()

# Example FAISS setup
index = faiss.IndexFlatL2(384)
docs = ["Margin call thresholds", "Liquidity risk policies"]
embeddings = model.encode(docs)
index.add(np.array(embeddings).astype("float32"))

def retrieve_and_generate(query: str):
    query_vector = model.encode([query]).astype("float32")
    D, I = index.search(query_vector, k=2)
    context = [docs[i] for i in I[0]]

    prompt = f"Based on the following financial context:\n{context}\n\nAnswer the query: {query}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
