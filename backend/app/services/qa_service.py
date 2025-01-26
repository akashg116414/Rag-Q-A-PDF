from typing import List

async def generate_answer(question: str, documents: List[str]):
    # Mocked RAG logic: In a real-world app, you'd query embeddings and use a model like GPT.
    context = " ".join(documents)
    return {"answer": f"Based on context: {context[:50]}... for question: {question}"}
