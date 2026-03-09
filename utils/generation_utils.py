"""Generation Utilities for Lab 6."""
import requests

def generate(prompt, model="llama3.2:3b", temperature=0.2, max_tokens=500, timeout=120):
    try:
        r = requests.post("http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False,
                  "options": {"temperature": temperature, "num_predict": max_tokens}},
            timeout=timeout)
        r.raise_for_status()
        return r.json()["response"]
    except Exception as e:
        return f"[Generation failed: {e}]"

def is_ollama_available():
    try:
        return requests.get("http://localhost:11434/api/tags", timeout=5).status_code == 200
    except Exception:
        return False
