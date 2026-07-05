# -*- coding: utf-8 -*-
"""
build_question_cache.py - Construye engine/preguntas_cache.json (Fase 2.1)

Para cada nodo del grafo con nodos_siguientes validos, genera UNA pregunta
ABIERTA en espanol comun (sin opciones), disenada para que la respuesta libre
del usuario discrimine entre esos caminos. La pregunta depende solo de la
topologia del grafo (no del usuario), asi que se genera una vez y se cachea:
{node_id: {"pregunta": str, "candidatos": [ids]}}

Uso:
    python engine/build_question_cache.py --sample 20   # prueba barata, no toca el cache real
    python engine/build_question_cache.py --yes         # corrida completa, sobrescribe engine/preguntas_cache.json
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
CACHE_PATH = BASE / "engine" / "preguntas_cache.json"
SAMPLE_CACHE_PATH = BASE / "engine" / "preguntas_cache.sample.json"

MODEL = "claude-haiku-4-5"
PRICE_INPUT_PER_MTOK = 1.00
PRICE_OUTPUT_PER_MTOK = 5.00

SYSTEM_PREGUNTA = (
    "Eres un disenador de entrevistas para una app de emprendimiento. Se te da un "
    "concepto actual (que la persona acaba de leer) y una lista de conceptos "
    "siguientes posibles, cada uno con sus condiciones de activacion (cuando ese "
    "camino aplica). Tu tarea: redactar UNA sola pregunta ABIERTA, en espanol "
    "comun, sin jerga, sin mencionar autores, libros ni la palabra 'nodo', "
    "hablando siempre de la IDEA o el PROYECTO de la persona (nunca de su "
    "'empresa' o 'negocio', salvo que el concepto actual sea explicitamente de "
    "viabilidad economica), disenada para que la respuesta libre de la persona "
    "revele naturalmente cual de los caminos siguientes le corresponde. NO "
    "ofrezcas opciones ni menciones "
    "los caminos por nombre; la pregunta debe sonar como algo que preguntaria un "
    "buen mentor, no un formulario. Responde SOLO un JSON: {\"pregunta\": str}."
)


def cargar_grafo():
    return json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]


def nodos_elegibles(graph):
    elegibles = {}
    for nid, n in graph.items():
        candidatos = [s for s in n.get("nodos_siguientes", []) if s in graph and s != nid]
        if candidatos:
            elegibles[nid] = candidatos
    return elegibles


def generar_pregunta(client, actual, candidatos_ids, graph):
    ctx = {
        "concepto_actual": {
            "titulo": actual["titulo_concepto"],
            "resumen": actual["resumen_teorico"][:400],
        },
        "conceptos_siguientes": [
            {
                "titulo": graph[c]["titulo_concepto"],
                "condiciones_activacion": graph[c].get("condiciones_activacion", [])[:3],
            }
            for c in candidatos_ids
        ],
    }
    msg = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=[{"type": "text", "text": SYSTEM_PREGUNTA, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": json.dumps(ctx, ensure_ascii=False)}],
    )
    raw = "".join(b.text for b in msg.content if b.type == "text")
    data = json.loads(raw.strip().removeprefix("```json").removesuffix("```").strip())
    return data["pregunta"], msg.usage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=None,
                     help="Procesa solo N nodos de prueba (muestreados) y reporta costo extrapolado")
    ap.add_argument("--yes", action="store_true",
                     help="Confirma la corrida completa sobre todos los nodos elegibles (sin --sample)")
    ap.add_argument("--patch", nargs="+", metavar="NODE_ID", default=None,
                     help="Regenera solo estos node_id puntuales y los fusiona en el cache real existente")
    args = ap.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY no esta configurada (revisa .env).")
        sys.exit(1)

    import anthropic
    client = anthropic.Anthropic()

    graph = cargar_grafo()
    elegibles = nodos_elegibles(graph)
    total = len(elegibles)
    print(f"Nodos elegibles (con nodos_siguientes validos): {total}")

    if args.patch:
        cache = json.load(open(CACHE_PATH, encoding="utf-8")) if CACHE_PATH.exists() else {}
        for nid in args.patch:
            if nid not in elegibles:
                print(f"  omitido (no elegible o no existe): {nid}")
                continue
            pregunta, usage = generar_pregunta(client, graph[nid], elegibles[nid], graph)
            cache[nid] = {"pregunta": pregunta, "candidatos": elegibles[nid]}
            costo = usage.input_tokens / 1_000_000 * PRICE_INPUT_PER_MTOK + usage.output_tokens / 1_000_000 * PRICE_OUTPUT_PER_MTOK
            print(f"  parchado: {nid} -> {pregunta[:70]}  (${costo:.4f})")
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nGuardado: {CACHE_PATH}  ({len(cache)} preguntas totales)")
        return

    if args.sample is None and not args.yes:
        print(f"\nEsto ejecutaria la corrida COMPLETA sobre {total} nodos y gastaria dinero real.")
        print("Corre primero con --sample 20 para ver el costo extrapolado,")
        print("o pasa --yes si ya confirmaste el costo y quieres proceder con todo.")
        sys.exit(1)

    if args.sample is not None:
        ids = list(elegibles.keys())
        step = max(1, len(ids) // args.sample)
        trabajo = ids[::step][:args.sample]
        out_path = SAMPLE_CACHE_PATH
        print(f"Modo muestra: procesando {len(trabajo)} de {total} nodos (espaciados uniformemente).\n")
    else:
        trabajo = list(elegibles.keys())
        out_path = CACHE_PATH
        print(f"Modo completo: procesando los {len(trabajo)} nodos elegibles.\n")

    cache = {}
    total_in, total_out = 0, 0
    t0 = time.time()
    for i, nid in enumerate(trabajo, 1):
        actual = graph[nid]
        candidatos = elegibles[nid]
        try:
            pregunta, usage = generar_pregunta(client, actual, candidatos, graph)
        except Exception as e:
            print(f"  [{i}/{len(trabajo)}] FALLO en {nid}: {e}")
            continue
        cache[nid] = {"pregunta": pregunta, "candidatos": candidatos}
        total_in += usage.input_tokens
        total_out += usage.output_tokens
        if i % 20 == 0 or i == len(trabajo):
            print(f"  [{i}/{len(trabajo)}] {nid} -> {pregunta[:70]}")

    elapsed = time.time() - t0
    cost = (total_in / 1_000_000) * PRICE_INPUT_PER_MTOK + (total_out / 1_000_000) * PRICE_OUTPUT_PER_MTOK

    out_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nGuardado: {out_path}  ({len(cache)} preguntas)")
    print(f"Tokens reales: {total_in} in / {total_out} out | Costo real: ${cost:.4f} | Tiempo: {elapsed:.1f}s")

    if args.sample is not None:
        factor = total / len(trabajo)
        print(f"\nExtrapolado a los {total} nodos elegibles (factor {factor:.1f}x):")
        print(f"  Tokens estimados: {int(total_in * factor)} in / {int(total_out * factor)} out")
        print(f"  Costo estimado de la corrida completa: ${cost * factor:.2f}")
        print("\nPara la corrida completa: python engine/build_question_cache.py --yes")


if __name__ == "__main__":
    main()
