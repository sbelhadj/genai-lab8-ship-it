"""
Embedding Utilities for Lab 6 — RAG Pipeline

Provides helpers for sentence embeddings and similarity computation.
"""

import numpy as np


def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors."""
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))


def cosine_similarity_matrix(query_embeddings, doc_embeddings):
    """
    Compute a similarity matrix (queries × documents).

    Args:
        query_embeddings: (n_queries, dim) array.
        doc_embeddings: (n_docs, dim) array.

    Returns:
        (n_queries, n_docs) similarity matrix.
    """
    q = np.array(query_embeddings)
    d = np.array(doc_embeddings)
    # Normalize
    q_norm = q / (np.linalg.norm(q, axis=1, keepdims=True) + 1e-10)
    d_norm = d / (np.linalg.norm(d, axis=1, keepdims=True) + 1e-10)
    return q_norm @ d_norm.T


def plot_similarity_heatmap(sim_matrix, row_labels, col_labels, title="Similarity Matrix"):
    """Plot a similarity heatmap with matplotlib."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(max(10, len(col_labels) * 1.2), max(4, len(row_labels) * 0.8)))
    im = ax.imshow(sim_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label='Cosine Similarity')

    ax.set_xticks(range(len(col_labels)))
    ax.set_yticks(range(len(row_labels)))
    ax.set_xticklabels([c[:40] + '...' if len(c) > 40 else c for c in col_labels],
                       rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels([r[:50] + '...' if len(r) > 50 else r for r in row_labels], fontsize=9)

    for i in range(len(row_labels)):
        for j in range(len(col_labels)):
            ax.text(j, i, f'{sim_matrix[i, j]:.2f}', ha='center', va='center', fontsize=7,
                    color='white' if sim_matrix[i, j] > 0.6 else 'black')

    ax.set_title(title, fontsize=13)
    plt.tight_layout()
    plt.show()
