#!/usr/bin/env python3
"""
DevAssist — AI-Powered Documentation Assistant for TaskFlow

Usage:
    python devassist.py "How do I authenticate with the TaskFlow API?"
    python devassist.py --no-rag "What are the task states?"
    python devassist.py --verbose "How do I install TaskFlow?"
"""

import argparse
import json
import sys
import time
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.generation_utils import generate, is_ollama_available
from utils.chunking_utils import load_and_chunk_corpus
from utils.retrieval_utils import format_context, query_collection
from utils.security_utils import (
    sanitize_input, validate_output,
    HARDENED_SYSTEM_PROMPT, ORIGINAL_SYSTEM_PROMPT,
)


def build_index():
    """Build the ChromaDB index from the corpus."""
    from sentence_transformers import SentenceTransformer
    import chromadb

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.Client()
    try:
        client.delete_collection("taskflow_docs")
    except Exception:
        pass
    collection = client.create_collection("taskflow_docs", metadata={"hnsw:space": "cosine"})

    corpus_dir = os.path.join(os.path.dirname(__file__), "corpus", "docs")
    all_chunks = load_and_chunk_corpus(corpus_dir, strategy="sections", min_length=80)
    chunk_texts = [c["text"] for c in all_chunks]
    chunk_ids = [f"chunk_{i}" for i in range(len(all_chunks))]
    chunk_metas = [{"source_file": c["source_file"], "section": c.get("section", "")} for c in all_chunks]
    chunk_embs = embedding_model.encode(chunk_texts).tolist()
    collection.add(ids=chunk_ids, documents=chunk_texts, embeddings=chunk_embs, metadatas=chunk_metas)

    return embedding_model, collection


def query(question, embedding_model, collection, use_rag=True, verbose=False):
    """Execute a query through the full pipeline."""
    result = {"question": question, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

    # Layer 1: Input sanitization
    sanitization = sanitize_input(question)
    result["sanitization"] = sanitization
    if sanitization["blocked"]:
        result["response"] = (
            "Your query was flagged by our safety system. "
            "Please rephrase your question about TaskFlow documentation."
        )
        result["blocked"] = True
        return result

    # Layer 2: Retrieval + generation
    if use_rag:
        passages = query_collection(collection, embedding_model, question, top_k=3)
        context_block = format_context(passages)
        prompt = HARDENED_SYSTEM_PROMPT.format(context=context_block, user_question=question)
        result["retrieved_passages"] = passages
    else:
        prompt = f"Answer this question about TaskFlow:\n\n{question}\n\nAnswer:"
        passages = []

    start = time.time()
    raw_response = generate(prompt, temperature=0.2)
    result["latency_ms"] = round((time.time() - start) * 1000)
    result["raw_response"] = raw_response

    # Layer 3: Output validation
    validation = validate_output(raw_response, passages)
    result["validation"] = validation
    result["response"] = validation["filtered_response"]
    result["blocked"] = not validation["passed"]

    return result


def main():
    parser = argparse.ArgumentParser(description="DevAssist — TaskFlow Documentation Assistant")
    parser.add_argument("question", nargs="?", help="Question about TaskFlow")
    parser.add_argument("--no-rag", action="store_true", help="Disable RAG (baseline mode)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show retrieval details + timing")
    parser.add_argument("--json", action="store_true", help="Output raw JSON result")
    args = parser.parse_args()

    if not args.question:
        parser.print_help()
        return

    if not is_ollama_available():
        print("Error: Ollama is not running. Start with: ollama serve")
        sys.exit(1)

    print("Loading index...", end=" ", flush=True)
    embedding_model, collection = build_index()
    print("done.")

    result = query(args.question, embedding_model, collection, use_rag=not args.no_rag, verbose=args.verbose)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
        return

    if result.get("blocked") and result.get("sanitization", {}).get("blocked"):
        print(f"\n🛑 Query blocked by input sanitizer.")
        print(f"   Flags: {result['sanitization']['flags']}")
        print(f"   Response: {result['response']}")
        return

    print(f"\n📝 Question: {args.question}")
    print(f"\n💬 Answer:\n{result['response']}")

    if args.verbose and "retrieved_passages" in result:
        print(f"\n📚 Retrieved passages:")
        for i, p in enumerate(result["retrieved_passages"]):
            print(f"  [{i+1}] {p['source']} (sim: {p['similarity']:.3f})")
            print(f"      {p['text'][:120]}...")
        print(f"\n⏱  Latency: {result.get('latency_ms', '?')} ms")

    if not result.get("validation", {}).get("passed", True):
        print(f"\n⚠️  Output validation issues:")
        for issue in result["validation"]["issues"]:
            print(f"   [{issue['severity']}] {issue['detail']}")


if __name__ == "__main__":
    main()
