# -*- coding: utf-8 -*-
"""
build_semantic_index.py - Fase 2.8: indice de embeddings de los 1265 nodos
(brujula semantica) para navegacion libre por toda la telaraña.

Genera embeddings locales (sentence-transformers, sin llamadas a la API,
costo cero por sesion) del texto de cada nodo (titulo + resumen +
condiciones_activacion) y los guarda en engine/semantic_index.npz junto
con la lista de ids en el mismo orden. Se corre UNA vez (o cuando el grafo
cambie); prototipo_motor.py carga ese archivo en tiempo de ejecucion.

Uso: python engine/build_semantic_index.py
"""
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent.parent
GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
INDEX_PATH = BASE / "engine" / "semantic_index.npz"

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


def texto_nodo(n):
    partes = [
        n.get("titulo_concepto", ""),
        n.get("resumen_teorico", ""),
        " ".join(n.get("condiciones_activacion", []) or []),
    ]
    return " ".join(p for p in partes if p).strip()


def main():
    print(f"Cargando grafo desde {GRAPH_PATH}...")
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]
    ids = list(graph.keys())
    textos = [texto_nodo(graph[nid]) for nid in ids]
    print(f"{len(ids)} nodos a embeber.")

    print(f"Cargando modelo {MODEL_NAME} (local, primera vez descarga de HuggingFace)...")
    from sentence_transformers import SentenceTransformer
    modelo = SentenceTransformer(MODEL_NAME)

    print("Generando embeddings (esto puede tardar unos minutos)...")
    embeddings = modelo.encode(
        textos, normalize_embeddings=True, show_progress_bar=True, batch_size=64,
    ).astype("float32")

    np.savez_compressed(INDEX_PATH, ids=np.array(ids), embeddings=embeddings)
    print(f"Guardado: {INDEX_PATH} ({embeddings.shape[0]} nodos, dim={embeddings.shape[1]})")


if __name__ == "__main__":
    main()
