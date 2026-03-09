"""
Retrieval Utilities for Lab 6 — RAG Pipeline

Provides helpers for building and querying a ChromaDB vector store.
"""


def format_context(retrieved_passages, max_passages=5):
    """
    Format retrieved passages into a numbered context block for the prompt.

    Args:
        retrieved_passages: List of dicts with 'text' and 'source'.
        max_passages: Maximum passages to include.

    Returns:
        Formatted context string with source labels.
    """
    lines = []
    for i, passage in enumerate(retrieved_passages[:max_passages]):
        source = passage.get("source", "Unknown")
        text = passage["text"].strip()
        lines.append(f"[Source {i+1}] ({source}):\n{text}")
    return "\n\n".join(lines)


def query_collection(collection, embedding_model, question, top_k=3):
    """
    Query a ChromaDB collection with a natural language question.

    Args:
        collection: ChromaDB collection.
        embedding_model: SentenceTransformer model.
        question: Query string.
        top_k: Number of results.

    Returns:
        List of dicts: {text, source, similarity}
    """
    query_embedding = embedding_model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    passages = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        source = meta.get("source_file", "unknown")
        section = meta.get("section", "")
        if section:
            source = f"{source}, {section}"
        passages.append({
            "text": doc,
            "source": source,
            "similarity": round(1 - dist, 4),
        })

    return passages
