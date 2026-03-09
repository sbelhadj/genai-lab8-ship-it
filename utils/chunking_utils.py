"""
Chunking Utilities for Lab 6 — RAG Pipeline

Provides functions to split documents into retrievable chunks.
"""

import os
import re


def chunk_by_paragraphs(text, min_length=50):
    """
    Split text into chunks by paragraph boundaries (double newline).
    Merges very short paragraphs with the next one.

    Args:
        text: Full document text.
        min_length: Minimum chunk length in characters.

    Returns:
        List of chunk strings.
    """
    # Split on double newlines (paragraph boundaries)
    raw_paragraphs = re.split(r'\n\s*\n', text.strip())

    chunks = []
    buffer = ""

    for para in raw_paragraphs:
        para = para.strip()
        if not para:
            continue

        # Skip very short lines that are just headers or blanks
        if buffer:
            buffer += "\n\n" + para
        else:
            buffer = para

        if len(buffer) >= min_length:
            chunks.append(buffer)
            buffer = ""

    if buffer:
        if chunks:
            chunks[-1] += "\n\n" + buffer
        else:
            chunks.append(buffer)

    return chunks


def chunk_by_sections(text, heading_pattern=r'^#{1,3}\s+'):
    """
    Split markdown text by heading boundaries.

    Each chunk starts with a heading and includes all content until
    the next heading of equal or higher level.

    Args:
        text: Markdown document text.
        heading_pattern: Regex pattern for headings.

    Returns:
        List of (heading, content) tuples.
    """
    lines = text.split('\n')
    sections = []
    current_heading = "Introduction"
    current_lines = []

    for line in lines:
        if re.match(heading_pattern, line):
            if current_lines:
                content = '\n'.join(current_lines).strip()
                if content:
                    sections.append({"heading": current_heading, "text": content})
            current_heading = line.strip().lstrip('#').strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        content = '\n'.join(current_lines).strip()
        if content:
            sections.append({"heading": current_heading, "text": content})

    return sections


def load_and_chunk_corpus(corpus_dir, strategy="paragraphs", min_length=80):
    """
    Load all markdown files from corpus directory and chunk them.

    Args:
        corpus_dir: Path to directory containing .md files.
        strategy: "paragraphs" or "sections".
        min_length: Minimum chunk length.

    Returns:
        List of dicts: {text, source_file, section, chunk_index}
    """
    all_chunks = []
    chunk_idx = 0

    for filename in sorted(os.listdir(corpus_dir)):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(corpus_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        if strategy == "sections":
            sections = chunk_by_sections(text)
            for sec in sections:
                if len(sec["text"]) >= min_length:
                    all_chunks.append({
                        "text": sec["text"],
                        "source_file": filename,
                        "section": sec["heading"],
                        "chunk_index": chunk_idx,
                    })
                    chunk_idx += 1
        else:
            paragraphs = chunk_by_paragraphs(text, min_length)
            for para in paragraphs:
                all_chunks.append({
                    "text": para,
                    "source_file": filename,
                    "section": "",
                    "chunk_index": chunk_idx,
                })
                chunk_idx += 1

    return all_chunks
