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

PRINCIPIO 2 (decision del fundador, 28 sep 2026, docs/REGLAS_DE_LA_CASA.md): nada se elimina ni se cambia. Las
preguntas de la cache son PREGUNTAS BASE y se quedan EXACTAMENTE como estan. Dos modos que solo AÑADEN:
    --faltantes --yes   # la pregunta de los nodos con siguientes que aun no la tienen (los 40); nunca pisa una base
    --neutrales --yes   # la version NEUTRAL de cada base (sin roles supuestos, tuteo neutro), en el campo aparte
                        # pregunta_neutral; es la salida segura del adaptador (web/lib/engine/adaptadorPregunta.ts)
Los dos corren en la CORRIDA FINAL (regla del fundador: ninguna llamada a la API real antes), y se pueden reanudar:
lo que ya esta hecho no se vuelve a pagar.
"""
import argparse
import json
import os
import re
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
    "PROHIBIDO usar guiones largos o medios (— o –) en cualquier texto que escribas: usa comas, dos puntos o parentesis. "
    "Eres un disenador de entrevistas para una app de emprendimiento. Se te da un "
    "concepto actual (que la persona acaba de leer) y una lista de conceptos "
    "siguientes posibles, cada uno con sus condiciones de activacion (cuando ese "
    "camino aplica). Tu tarea: redactar UNA sola pregunta ABIERTA, en espanol "
    "comun, sin jerga, sin mencionar autores, libros ni la palabra 'nodo', "
    "hablando siempre de la IDEA o el PROYECTO de la persona (nunca de su "
    "'empresa' o 'negocio', salvo que el concepto actual sea explicitamente de "
    "viabilidad economica), disenada para que la respuesta libre de la persona "
    "revele naturalmente cual de los caminos siguientes le corresponde. Habla "
    "SIEMPRE de tu (singular): la persona suele estar sola al inicio. NO asumas "
    "que tiene cofundadores, equipo, empleados, empresa constituida, "
    "distribuidores ni clientes corporativos; si el concepto trata de esos "
    "temas, pregunta en condicional (por ejemplo 'si llegas a traer socios...') "
    "o pregunta primero si esa realidad existe. NO "
    "ofrezcas opciones ni menciones "
    "los caminos por nombre; la pregunta debe sonar como algo que preguntaria un "
    "buen mentor, no un formulario. Responde SOLO un JSON: {\"pregunta\": str}."
)

# La REGLA UNICA del contexto del usuario (docs/REGLAS_DE_LA_CASA.md, regla 1). Copia literal de
# web/lib/reglaContextoUsuario.ts; test_generador_neutrales.py comprueba que son la misma letra.
REGLA_CONTEXTO_USUARIO = (
    "CONTEXTO REAL DE LA PERSONA: no supongas roles ni estructuras que la persona no mencionó. Muchos conceptos del "
    "material vienen de libros escritos para empresas grandes y suponen un jefe por encima, un departamento de "
    "recursos humanos, directivos o varios departamentos. Mira la ficha de contexto de la persona (su papel, si tiene "
    "jefe, su equipo, su sector y su etapa) y habla de su situación real: si es dueña de su negocio no tiene jefe, y si "
    "trabaja sola no tiene equipo. Si el concepto supone uno de esos roles, adáptalo a quien lo cumple en su caso (un "
    "socio, un asesor, ella misma) o pregúntalo en condicional ('si tienes a alguien por "
    "encima...'). Adaptar cambia la forma, nunca el fondo: lo que preguntas o propones busca lo mismo que el material. "
    "Nunca des por hecho lo que la persona no dijo."
)

# El generador de preguntas base lleva tambien la regla unica (las 40 nuevas nacen con ella).
SYSTEM_PREGUNTA_CON_REGLA = SYSTEM_PREGUNTA + "\n\n" + REGLA_CONTEXTO_USUARIO

SYSTEM_NEUTRAL = (
    "PROHIBIDO usar guiones largos o medios (— o –) en cualquier texto que escribas: usa comas, dos puntos o parentesis. "
    "Recibes la PREGUNTA BASE de un concepto de una entrevista de emprendimiento, el concepto y los temas siguientes "
    "entre los que la respuesta ayuda a elegir. Escribe su VERSION NEUTRAL: la que se le puede hacer a CUALQUIER "
    "persona sin saber nada de ella (puede estar sola, ser dueña de su negocio, tener un equipo o trabajar para "
    "otro). Cambia la FORMA, nunca el FONDO: busca averiguar exactamente lo mismo que la base y su respuesta sirve "
    "para elegir entre los mismos temas. Quita todo rol o estructura que la base da por hecho (un jefe, un equipo, "
    "empleados, recursos humanos, directivos, departamentos, una empresa grande): si el concepto lo necesita, "
    "preguntalo en condicional ('si tienes a alguien por encima...') o habla de quien lo cumpla. Tutea en espanol "
    "neutro, nada de voseo (tienes, quieres, puedes; nunca tenes, queres, podes, vos). UNA sola pregunta, abierta, "
    "calida, sin jerga, sin autores ni libros. Si la base ya es neutral, devuelvela igual. "
    "Responde SOLO un JSON: {\"pregunta_neutral\": str}."
    "\n\n" + REGLA_CONTEXTO_USUARIO
)

# Voseo que la neutral no puede traer (la base puede: no se toca). Donde el tuteo se escribe igual salvo la tilde
# (sabes/sabés, buscas/buscás, mira/mirá) se exige la tilde; donde el tuteo diptonga (tienes/tenés), basta la raiz.
VOSEO = re.compile(
    r"\b(vos|sos|ten[eé]s|quer[eé]s|pod[eé]s|sabés|hacés|decís|pensás|necesitás|buscás|"
    r"cont[aá]me|dec[ií]me|contanos|pensá|mirá|contá)\b",
    re.IGNORECASE,
)


def comprobar_neutral(base, texto):
    """None si la neutral sirve; si no, el motivo. El fondo lo mide el juez de la prueba de coherencia."""
    t = (texto or "").strip()
    if not t:
        return "vacia"
    if "?" in base and "?" not in t:
        return "no_es_pregunta"
    if "—" in t or "–" in t:
        return "guion_largo"
    if len(t) > max(2 * len(base), len(base) + 200):
        return "demasiado_larga"
    if VOSEO.search(t):
        return "voseo"
    return None


def _json_de(raw):
    raw = raw.strip()
    ini, fin = raw.find("{"), raw.rfind("}")
    if ini < 0 or fin < ini:
        raise ValueError("sin objeto JSON")
    return json.loads(raw[ini:fin + 1])


class SalidaFallida(ValueError):
    """Una salida que no sirve, pero que YA se pago: lleva su uso para que el coste reportado sea el real."""

    def __init__(self, motivo, usage):
        super().__init__(motivo)
        self.usage = usage


def generar_neutral(client, nid, base, candidatos_ids, graph):
    """La version neutral de UNA base. Devuelve (texto, usage); lanza SalidaFallida (con su uso) si no sirve."""
    n = graph[nid]
    ctx = {
        "pregunta_base": base,
        "concepto": {"etiqueta": n.get("etiqueta_arbol") or n["titulo_concepto"], "resumen": n.get("resumen_teorico", "")[:400]},
        "temas_siguientes": [graph[c].get("etiqueta_arbol") or graph[c]["titulo_concepto"] for c in candidatos_ids if c in graph][:6],
    }
    msg = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=[{"type": "text", "text": SYSTEM_NEUTRAL, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": json.dumps(ctx, ensure_ascii=False)}],
    )
    if getattr(msg, "stop_reason", None) == "max_tokens":
        raise SalidaFallida("respuesta cortada por tope de tokens", msg.usage)
    raw = "".join(b.text for b in msg.content if b.type == "text")
    try:
        texto = str(_json_de(raw).get("pregunta_neutral", "")).strip()
    except ValueError as e:
        raise SalidaFallida(f"no es JSON: {e}", msg.usage) from e
    motivo = comprobar_neutral(base, texto)
    if motivo:
        raise SalidaFallida(f"la neutral no pasa: {motivo}", msg.usage)
    return texto, msg.usage


def objetivos_neutrales(cache, graph):
    """Las bases que necesitan neutral: nodo vivo (existe y no esta deprecado), con pregunta y sin neutral aun."""
    return [
        nid for nid, e in cache.items()
        if e.get("pregunta") and not e.get("pregunta_neutral") and nid in graph and not graph[nid].get("deprecado")
    ]


def correr_neutrales(client, cache, graph, limite=None, guardar=None, reintentos=1):
    """Añade pregunta_neutral a cada base que la necesita. La base NO se toca. Reanudable: solo trabaja lo que falta.
    Devuelve {'hechas', 'fallidas': [(nid, motivo)], 'tokens_in', 'tokens_out'}."""
    trabajo = objetivos_neutrales(cache, graph)
    if limite is not None:
        trabajo = trabajo[:limite]
    hechas, fallidas, t_in, t_out = 0, [], 0, 0
    for i, nid in enumerate(trabajo, 1):
        base = cache[nid]["pregunta"]
        ultimo = None
        for _ in range(1 + reintentos):
            try:
                texto, usage = generar_neutral(client, nid, base, cache[nid].get("candidatos", []), graph)
                t_in += usage.input_tokens
                t_out += usage.output_tokens
                cache[nid] = {**cache[nid], "pregunta_neutral": texto}
                assert cache[nid]["pregunta"] == base  # la base queda intacta
                hechas += 1
                ultimo = None
                break
            except Exception as e:  # noqa: BLE001 - se reporta, no se calla
                ultimo = str(e)
                usage = getattr(e, "usage", None)
                if usage is not None:  # lo pagado cuenta aunque la salida no sirva
                    t_in += usage.input_tokens
                    t_out += usage.output_tokens
        if ultimo:
            fallidas.append((nid, ultimo))
        if guardar and i % 50 == 0:
            guardar(cache)
    if guardar:
        guardar(cache)
    return {"hechas": hechas, "fallidas": fallidas, "tokens_in": t_in, "tokens_out": t_out}


def faltantes(cache, graph):
    """Los nodos con siguientes validos que aun no tienen pregunta en la cache."""
    return [nid for nid in nodos_elegibles(graph) if not (cache.get(nid) or {}).get("pregunta")]


def correr_faltantes(client, cache, graph, guardar=None):
    """Añade la pregunta de los nodos que no la tienen. Jamas pisa una base existente."""
    elegibles = nodos_elegibles(graph)
    hechas, fallidas, t_in, t_out = 0, [], 0, 0
    for nid in faltantes(cache, graph):
        try:
            pregunta, usage = generar_pregunta(client, graph[nid], elegibles[nid], graph, system=SYSTEM_PREGUNTA_CON_REGLA)
        except Exception as e:  # noqa: BLE001
            fallidas.append((nid, str(e)))
            continue
        assert not (cache.get(nid) or {}).get("pregunta")  # nunca pisa una base
        cache[nid] = {**(cache.get(nid) or {}), "pregunta": pregunta, "candidatos": elegibles[nid]}
        hechas += 1
        t_in += usage.input_tokens
        t_out += usage.output_tokens
    if guardar:
        guardar(cache)
    return {"hechas": hechas, "fallidas": fallidas, "tokens_in": t_in, "tokens_out": t_out}


def cargar_grafo():
    return json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]


def nodos_elegibles(graph):
    """Los nodos para los que vale la pena generar pregunta.

    Los DEPRECADOS quedan fuera: no se les ofrece al usuario, asi que gastar API
    en sus preguntas seria pagar por algo que nadie va a ver. Tampoco pueden ser
    CANDIDATOS de la pregunta de otro, por lo mismo.

    Pero la poda es HACIA ADELANTE, jamas hacia atras: las preguntas ya
    cacheadas de un nodo deprecado NO se borran. Son lectura historica potencial
    y guardadas no cuestan nada (palabra del fundador, ago 2026). Esta funcion
    decide a quien se le GENERA, no a quien se le borra.
    """
    elegibles = {}
    for nid, n in graph.items():
        if n.get("deprecado"):
            continue
        candidatos = [s for s in n.get("nodos_siguientes", [])
                      if s in graph and s != nid and not graph[s].get("deprecado")]
        if candidatos:
            elegibles[nid] = candidatos
    return elegibles


def generar_pregunta(client, actual, candidatos_ids, graph, system=SYSTEM_PREGUNTA):
    ctx = {
        # La condicion y el entregable del nodo actual (integracion del mundo 11,
        # 28 sep 2026): sin ellos la pregunta no podia partir de la situacion
        # del nodo y la verificacion a ciegas la daba por floja.
        "concepto_actual": {
            "titulo": actual["titulo_concepto"],
            "resumen": actual["resumen_teorico"][:400],
            "condicion": (actual.get("condiciones_activacion") or [""])[0],
            "entregable": actual.get("entregable_esperado") or "",
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
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": json.dumps(ctx, ensure_ascii=False)}],
    )
    if getattr(msg, "stop_reason", None) == "max_tokens":
        raise ValueError("respuesta cortada por tope de tokens")
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
    ap.add_argument("--patch-file", metavar="RUTA", default=None,
                     help="Como --patch pero lee los node_id de un archivo (uno por linea); "
                          "evita el limite de linea de comandos de Windows con listas grandes")
    ap.add_argument("--faltantes", action="store_true",
                     help="Principio 2: genera la pregunta SOLO de los nodos con siguientes que no la tienen (exige --yes)")
    ap.add_argument("--neutrales", action="store_true",
                     help="Principio 2: añade pregunta_neutral a cada base que no la tiene; la base no se toca (exige --yes)")
    ap.add_argument("--limite", type=int, default=None, help="Con --neutrales: como mucho N nodos en esta pasada")
    args = ap.parse_args()

    if args.patch_file:
        ids = [l.strip() for l in Path(args.patch_file).read_text(encoding="utf-8").splitlines() if l.strip()]
        args.patch = (args.patch or []) + ids

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

    if args.faltantes or args.neutrales:
        cache = json.load(open(CACHE_PATH, encoding="utf-8"))
        pendientes = faltantes(cache, graph) if args.faltantes else objetivos_neutrales(cache, graph)
        modo = "faltantes" if args.faltantes else "neutrales"
        if not args.yes:
            print(f"\n--{modo}: {len(pendientes)} nodos por hacer. Gasta dinero real: pasa --yes para correrlo.")
            sys.exit(1)

        def guardar(c):
            CACHE_PATH.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8")

        t0 = time.time()
        if args.faltantes:
            r = correr_faltantes(client, cache, graph, guardar=guardar)
        else:
            r = correr_neutrales(client, cache, graph, limite=args.limite, guardar=guardar)
        cost = (r["tokens_in"] / 1_000_000) * PRICE_INPUT_PER_MTOK + (r["tokens_out"] / 1_000_000) * PRICE_OUTPUT_PER_MTOK
        print(f"\n--{modo}: hechas {r['hechas']}, fallidas {len(r['fallidas'])}")
        for nid, motivo in r["fallidas"][:30]:
            print(f"  FALLO {nid}: {motivo}")
        print(f"Tokens reales: {r['tokens_in']} in / {r['tokens_out']} out | Costo real aprox: ${cost:.4f} | {time.time() - t0:.1f}s")
        print("Despues: python scripts/sync_assets_web.py")
        # fallar ruidoso: si algo quedo sin hacer, el codigo de salida lo dice
        sys.exit(1 if r["fallidas"] else 0)

    if args.patch:
        cache = json.load(open(CACHE_PATH, encoding="utf-8")) if CACHE_PATH.exists() else {}
        total_in, total_out, parchados, omitidos = 0, 0, 0, 0
        t0 = time.time()
        for i, nid in enumerate(args.patch, 1):
            if nid not in elegibles:
                omitidos += 1
                if omitidos <= 20:
                    print(f"  omitido (no elegible o no existe): {nid}")
                continue
            if (cache.get(nid) or {}).get("pregunta"):
                # Principio 2 (28 sep 2026): una pregunta base no se regenera ni se cambia.
                omitidos += 1
                print(f"  omitido (ya tiene su pregunta base; no se toca): {nid}")
                continue
            pregunta, usage = generar_pregunta(client, graph[nid], elegibles[nid], graph)
            # conserva los campos aparte (pregunta_neutral, pregunta_entrada) si el nodo ya los tenia
            cache[nid] = {**(cache.get(nid) or {}), "pregunta": pregunta, "candidatos": elegibles[nid]}
            total_in += usage.input_tokens
            total_out += usage.output_tokens
            parchados += 1
            if parchados % 20 == 0:
                print(f"  [{i}/{len(args.patch)}] parchado: {nid} -> {pregunta[:60]}")
            # guardado incremental: una falla a mitad de lista no pierde lo hecho
            if parchados % 50 == 0:
                CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        elapsed = time.time() - t0
        cost = (total_in / 1_000_000) * PRICE_INPUT_PER_MTOK + (total_out / 1_000_000) * PRICE_OUTPUT_PER_MTOK
        print(f"\nGuardado: {CACHE_PATH}  ({len(cache)} preguntas totales)")
        print(f"Parchados: {parchados} | Omitidos (sin sucesores validos): {omitidos}")
        print(f"Tokens reales: {total_in} in / {total_out} out | Costo real: ${cost:.4f} | Tiempo: {elapsed:.1f}s")
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
