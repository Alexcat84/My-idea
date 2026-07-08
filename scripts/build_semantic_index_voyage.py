# -*- coding: utf-8 -*-
"""
build_semantic_index_voyage.py - Fase 3.0: re-embebe los 1266 nodos del
grafo con Voyage AI (voyage-4-lite) en vez de sentence-transformers
(Python-only, no viaja a la web). Genera web/lib/assets/semantic_index.json
para que web/lib/compass.ts haga similitud coseno en memoria, en runtime,
sin dependencias nativas.

Por que voyage-4-lite: el prompt de Fase 3.0 pedia "voyage-3-lite o
equivalente vigente" -- Voyage AI lanzo la serie 4 en enero de 2026,
sucediendo a la 3; voyage-4-lite es el equivalente directo (mismo tier
"lite", optimizado a costo/latencia). Precio: $0.02 por millon de tokens,
con 200 millones de tokens gratis al mes por cuenta -- embeber 1266 nodos
(~200-300 tokens cada uno) cae comodo dentro de la franja gratuita.

output_dimension=512 (no el default 1024): el dataset tiene 1266 nodos,
no millones -- 512 dimensiones da separacion mas que suficiente y reduce
a la mitad el tamano del archivo committeado.

Uso: python scripts/build_semantic_index_voyage.py
Requiere VOYAGE_API_KEY en el .env de la raiz.
"""
import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
OUT_PATH = BASE / "web" / "lib" / "assets" / "semantic_index.json"

load_dotenv(BASE / ".env")
VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY", "").strip()
VOYAGE_MODEL = "voyage-4-lite"
OUTPUT_DIMENSION = 512
BATCH_SIZE = 500  # bajo el limite de 1000 textos/llamada; menos llamadas = menos riesgo de 429
VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"
MAX_REINTENTOS = 5

# Los 2 casos de referencia de la Fase 2.9 (calibracion original de
# MIN_SCORE_SALTO=0.42 con sentence-transformers): se reverifican al final
# de este script contra los embeddings NUEVOS, porque el espacio de
# similitud cambia con el proveedor -- el prompt de Fase 3.0 pide
# explicitamente "re-verificar los scores... y ajustar el umbral si el
# espacio cambio".
QUERY_POSITIVA = "no he calculado bien cuanto me cuesta cada pieza"
NODO_ESPERADO_POSITIVO = "hoja_estimacion_costos"
QUERY_NEGATIVA = "mi resina hace burbujas y mi QR grabado con laser se borra"
NODO_ESPERADO_EXCLUIDO = "alfabetizacion_en_materiales_maliciosos"


def texto_nodo(n):
    partes = [
        n.get("titulo_concepto", ""),
        n.get("resumen_teorico", ""),
        " ".join(n.get("condiciones_activacion", []) or []),
    ]
    return " ".join(p for p in partes if p).strip()


def _embeber(textos, input_type):
    """Una llamada a Voyage para un batch de textos (<=1000). Devuelve la
    lista de vectores en el MISMO orden que los textos de entrada.
    Reintenta con backoff exponencial ante 429 (rate limit) -- encontrado
    en vivo corriendo esto la primera vez: 10 llamadas seguidas sin pausa
    disparaban 429 en una cuenta nueva."""
    for intento in range(MAX_REINTENTOS):
        resp = requests.post(
            VOYAGE_URL,
            headers={"Authorization": f"Bearer {VOYAGE_API_KEY}", "Content-Type": "application/json"},
            json={
                "input": textos,
                "model": VOYAGE_MODEL,
                "input_type": input_type,
                "output_dimension": OUTPUT_DIMENSION,
            },
            timeout=120,
        )
        if resp.status_code == 429 and intento < MAX_REINTENTOS - 1:
            espera = 2 ** intento * 2  # 2, 4, 8, 16, 32 segundos
            print(f"  (429 rate limit, reintentando en {espera}s...)")
            time.sleep(espera)
            continue
        resp.raise_for_status()
        data = resp.json()
        # Voyage devuelve "data" en el mismo orden que "input", cada item con
        # "embedding" e "index" -- pero por si el orden no viniera garantizado,
        # se reordena explicitamente por "index".
        items = sorted(data["data"], key=lambda d: d["index"])
        return [item["embedding"] for item in items], data.get("usage", {})
    raise RuntimeError("no se pudo completar el embebido tras varios reintentos")


def _coseno(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norma_a = sum(x * x for x in a) ** 0.5
    norma_b = sum(y * y for y in b) ** 0.5
    return dot / (norma_a * norma_b) if norma_a and norma_b else 0.0


def main():
    if not VOYAGE_API_KEY:
        print("ERROR: falta VOYAGE_API_KEY en el .env de la raiz.")
        raise SystemExit(1)

    print(f"Cargando grafo desde {GRAPH_PATH}...")
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]
    ids = list(graph.keys())
    textos = [texto_nodo(graph[nid]) for nid in ids]
    print(f"{len(ids)} nodos a embeber con {VOYAGE_MODEL} (dim={OUTPUT_DIMENSION}).")

    embeddings = []
    total_tokens = 0
    for i in range(0, len(textos), BATCH_SIZE):
        batch = textos[i : i + BATCH_SIZE]
        vectores, usage = _embeber(batch, input_type="document")
        embeddings.extend(vectores)
        total_tokens += usage.get("total_tokens", 0)
        print(f"  batch {i}-{i + len(batch)}: {len(vectores)} vectores (tokens acumulados: {total_tokens})")
        if i + BATCH_SIZE < len(textos):
            time.sleep(3)  # margen entre llamadas para no rozar el rate limit

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    contenido = {"model": VOYAGE_MODEL, "dimension": OUTPUT_DIMENSION, "ids": ids, "embeddings": embeddings}
    OUT_PATH.write_bytes((json.dumps(contenido, ensure_ascii=False) + "\n").encode("utf-8"))
    print(f"\nGuardado: {OUT_PATH} ({len(ids)} nodos, dim={OUTPUT_DIMENSION}, ~{total_tokens} tokens totales)")

    # Recalibracion (obligatoria por el prompt de Fase 3.0): re-verificar
    # los 2 casos de referencia de la Fase 2.9 contra el espacio nuevo.
    print("\n--- Recalibracion de MIN_SCORE_SALTO contra los embeddings de Voyage ---")
    vectores_pos, _ = _embeber([QUERY_POSITIVA], input_type="query")
    vec_pos = vectores_pos[0]
    vectores_neg, _ = _embeber([QUERY_NEGATIVA], input_type="query")
    vec_neg = vectores_neg[0]
    idx_pos = ids.index(NODO_ESPERADO_POSITIVO)
    idx_neg = ids.index(NODO_ESPERADO_EXCLUIDO)
    score_pos = _coseno(vec_pos, embeddings[idx_pos])
    score_neg = _coseno(vec_neg, embeddings[idx_neg])
    print(f"  '{QUERY_POSITIVA}' -> {NODO_ESPERADO_POSITIVO}: score={score_pos:.4f} (debe PASAR el umbral)")
    print(f"  '{QUERY_NEGATIVA}' -> {NODO_ESPERADO_EXCLUIDO}: score={score_neg:.4f} (debe quedar EXCLUIDO)")
    print(f"\n  Umbral original (sentence-transformers): 0.42")
    print(f"  Con estos dos puntos, un umbral candidato para Voyage seria el punto medio: "
          f"{(score_pos + score_neg) / 2:.4f}")
    print("  Ajustar MIN_SCORE_SALTO en web/lib/compass.ts segun este resultado antes de usarlo en produccion.")


if __name__ == "__main__":
    main()
