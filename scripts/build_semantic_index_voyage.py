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

RUTA_ENV = BASE / ".env"
load_dotenv(RUTA_ENV)
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


def embeber_textos(textos, input_type):
    """Una llamada a Voyage para un batch de textos (<=1000). Devuelve la
    lista de vectores en el MISMO orden que los textos de entrada.

    NOMBRE PUBLICO DESDE LA VUELTA 148, y el cambio es de rotulo y nada mas:
    el cuerpo no se toco. Nacio como `_embeber`, o sea declarada privada del
    modulo, y desde la vuelta 148 `scripts/integrar_packs.py` la usa para
    embeber un candidato de pack ANTES de insertarlo (decision del fundador
    del 2 sep 2026, PREGUNTA 1 por el camino 1). Importar un nombre privado
    desde otro modulo es acordar una costura sin declararla: el guion bajo
    dice "puedo cambiar sin avisar" y el que la importa no se entera. Se
    renombra en vez de duplicar la llamada HTTP, que es lo unico que no se
    puede hacer: dos versiones de la misma llamada serian dos varas.
    `_embeber` sobrevive como alias mas abajo para no romper a nadie.

    NO LEE EL GRAFO. Toma una lista de textos sueltos, y por eso sirve para un
    candidato que todavia no esta en `master_graph.json`: la dependencia
    circular que la vuelta 147 midio (el vector se fabrica leyendo el grafo, y
    el grafo solo conoce al candidato tras la copia) vive en `main()`, no
    aqui.
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


# Alias de compatibilidad: el nombre viejo sigue apuntando a la MISMA funcion,
# no a una copia. Cualquiera que aun escriba `_embeber` obtiene lo mismo.
_embeber = embeber_textos


def credencial_ausente(clave=None, ruta_env=None):
    """PURA A PROPOSITO, Y NO SALE A LA RED (vuelta 148). Devuelve el MOTIVO
    escrito de que falte la credencial, o None si esta. No lanza y no imprime:
    quien llama decide como fallar, y asi el motivo se puede probar sin gastar
    un token ni tocar el disco.

    Recibe la clave por parametro (con el global como defecto) para que la
    prueba de mutacion pueda darle una clave computada y una copia mutada de
    esa misma clave, en vez de compararse contra un literal (EJECUTOR 1, "EL
    CASO ROJO SE PRUEBA POR MUTACION").

    NOMBRA LO QUE FALTA: la variable Y el fichero donde vive. Un "falta la
    configuracion" no le dice a nadie que escribir ni donde (banco 9, fallar
    ruidoso)."""
    clave = VOYAGE_API_KEY if clave is None else clave
    ruta_env = RUTA_ENV if ruta_env is None else ruta_env
    if (clave or "").strip():
        return None
    return ("falta la credencial VOYAGE_API_KEY. Es una variable de entorno que se "
            "lee del fichero '%s' (la raiz del repo). Ese fichero esta FUERA del repo "
            "a proposito, asi que esta herramienta solo puede correr en una sesion con "
            "humano presente que lo tenga puesto. Sin ella no se puede embeber el "
            "candidato, y sin vector la aduana semantica A2.6 bloquea la insercion: "
            "no hay forma de seguir a medias." % ruta_env)


def _coseno(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norma_a = sum(x * x for x in a) ** 0.5
    norma_b = sum(y * y for y in b) ** 0.5
    return dot / (norma_a * norma_b) if norma_a and norma_b else 0.0


def main():
    motivo = credencial_ausente()
    if motivo:
        print("ERROR: %s" % motivo)
        raise SystemExit(1)

    print(f"Cargando grafo desde {GRAPH_PATH}...")
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]
    # Los DEPRECADOS no se embeben. Sin esto la deprecacion seria decorativa: el
    # nodo saldria de la seleccion del motor y el buscador semantico lo seguiria
    # proponiendo, que es el mismo nodo entrando por la otra puerta.
    deprecados = [k for k, n in graph.items() if n.get("deprecado")]
    ids = [k for k in graph.keys() if not graph[k].get("deprecado")]
    if deprecados:
        print(f"  {len(deprecados)} deprecados fuera del indice (siguen en el grafo).")
    textos = [texto_nodo(graph[nid]) for nid in ids]
    print(f"{len(ids)} nodos a embeber con {VOYAGE_MODEL} (dim={OUTPUT_DIMENSION}).")

    embeddings = []
    total_tokens = 0
    for i in range(0, len(textos), BATCH_SIZE):
        batch = textos[i : i + BATCH_SIZE]
        vectores, usage = embeber_textos(batch, input_type="document")
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
    vectores_pos, _ = embeber_textos([QUERY_POSITIVA], input_type="query")
    vec_pos = vectores_pos[0]
    vectores_neg, _ = embeber_textos([QUERY_NEGATIVA], input_type="query")
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
