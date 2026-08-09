# -*- coding: utf-8 -*-
"""
build_semantic_index.py - FOSIL VIGILADO. Indice de embeddings para la brujula
semantica del MOTOR DE CLI (engine/prototipo_motor.py), y de nada mas.

    ESTE ARCHIVO NO FORMA PARTE DE NINGUN FLUJO DE LA LINEA DE ENSAMBLAJE.

Nadie lo llama: ni run_phase1, ni integrar_packs, ni sync_assets_web, ni la web.
Su salida, engine/semantic_index.npz, se genero por ULTIMA VEZ el 2026-07-08 y
desde entonces envejece sola con cada cambio del catalogo.

LA WEB USA OTRO INDICE Y OTRO PROVEEDOR: web/lib/assets/semantic_index.json, que
genera scripts/build_semantic_index_voyage.py con Voyage en 512 dimensiones.
Este de aqui usa sentence-transformers en 384. Los dos espacios NO son
comparables: no es que uno este desactualizado respecto del otro, son dos
brujulas distintas.

QUE PASA SI NO SE REGENERA (auditoria del segundo indice, ago 2026): la brujula
del CLI se APAGA SOLA. _cargar_brujula compara los ids del .npz contra los nodos
activos del grafo maestro y, si falta uno solo, no busca: devuelve vacio y avisa
con este comando. El motor sigue con navegacion local. El antidoto se anclo en
el punto de exposicion, que es el momento en que alguien corre el CLI y se cree
el resultado.

La condicion de retiro de este archivo y del .npz esta fijada por adelantado en
docs/PENDIENTES.md.

Genera embeddings locales (sentence-transformers, sin llamadas a la API, costo
cero por sesion) del texto de cada nodo (titulo + resumen +
condiciones_activacion) y los guarda en engine/semantic_index.npz junto con la
lista de ids en el mismo orden.

Uso: python engine/build_semantic_index.py
"""
import datetime
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

    # LA FECHA VA DENTRO DEL ARTEFACTO, no se deduce del sistema de archivos.
    # Git no guarda tiempos de modificacion: en cualquier clon nuevo el .npz
    # nace con la fecha del checkout, y el aviso de la brujula diria "generado
    # hoy" mientras explica que el indice esta desfasado. Un dato dentro de un
    # aviso que no es lo que dice ser es exactamente lo que estos avisos vienen
    # a curar.
    generado = datetime.datetime.now().replace(microsecond=0).isoformat()
    np.savez_compressed(INDEX_PATH, ids=np.array(ids), embeddings=embeddings,
                        generado_iso=np.array(generado))
    print(f"Guardado: {INDEX_PATH} ({embeddings.shape[0]} nodos, dim={embeddings.shape[1]})")


if __name__ == "__main__":
    main()
