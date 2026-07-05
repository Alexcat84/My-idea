# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Prototipo CLI del motor de ruteo (Fase 2.1)

Entrevista guiada de texto libre: el usuario nunca elige de un menu. En cada
paso responde libremente y un modelo barato (Haiku) interpreta la respuesta
para decidir el siguiente concepto, acumular lo que el usuario revela en un
perfil de sesion, y detectar cuando quiere su plan o quiere salir.

Capa 1 (entrada): texto libre -> clasificado con Haiku hacia una de las 20
    puertas curadas (dataset/metadata/entry_seeds.json), generando un
    perfil_sesion inicial. Si la API falla, cae al cuestionario cerrado
    (engine/cuestionario_raiz.json) como respaldo.
Capa 2 (recorrido): la pregunta de cada nodo esta pregenerada y cacheada
    (engine/preguntas_cache.json, ver build_question_cache.py) porque
    depende de la topologia, no del usuario. La respuesta del usuario SI
    requiere una llamada por turno (Haiku), porque texto libre no se puede
    cachear ni resolver con un algoritmo interno. Si la API falla en un
    turno, cae a un menu numerado de emergencia para ese turno.
Capa 3 (plan final): Sonnet redacta el plan a partir de la entrada original,
    el perfil de sesion acumulado y la ruta completa.

Uso:  python engine/prototipo_motor.py
Guardrails: profundidad maxima 15, sin ciclos (nodos visitados no se
reofrecen), maximo 1 repregunta por nodo antes de forzar el candidato mas
probable.
"""
import json
import os
import sys
import textwrap
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# En consolas de Windows, stdout suele quedar en cp1252 (o el codepage local),
# que no puede representar caracteres como flechas (->) o comillas tipograficas
# presentes en el contenido de algunos nodos. Sin esto, print() lanza
# UnicodeEncodeError y el programa se cae a mitad de un recorrido.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
QUIZ_PATH = BASE / "engine" / "cuestionario_raiz.json"
ENTRY_SEEDS_PATH = BASE / "dataset" / "metadata" / "entry_seeds.json"
PREGUNTAS_CACHE_PATH = BASE / "engine" / "preguntas_cache.json"

MAX_DEPTH = 15
MAX_OPCIONES = 6
MAX_REPREGUNTAS_POR_NODO = 1

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
MODEL = "claude-sonnet-4-6"
MODEL_HAIKU = "claude-haiku-4-5"

PRECIOS = {
    MODEL: (3.00, 15.00),
    MODEL_HAIKU: (1.00, 5.00),
}
USO = {}

SYSTEM_CLASIFICACION = (
    "Eres el clasificador de entrada de una app de guia de emprendimiento. El "
    "usuario describe su situacion en texto libre. Debes: 1) elegir la puerta "
    "de entrada que mejor corresponde a su fase y necesidad actual, de una "
    "lista fija de puertas (cada una con id, fase y una breve descripcion), y "
    "2) redactar un perfil_sesion: un resumen breve (2 a 4 frases) de lo que "
    "el usuario revelo sobre su proyecto o situacion, para que las etapas "
    "posteriores no pierdan ese contexto. Responde SOLO un JSON: "
    "{\"puerta_id\": str, \"perfil_sesion\": str}. El puerta_id DEBE ser "
    "exactamente uno de los ids de la lista dada."
)

SYSTEM_INTERPRETE = (
    "Eres el interprete de turno de una entrevista guiada de emprendimiento. "
    "El usuario esta en un concepto actual y acaba de responder libremente a "
    "una pregunta abierta. Tu trabajo es interpretar su respuesta para decidir "
    "que pasa despues. Recibes el concepto actual, una lista de conceptos "
    "candidatos siguientes con sus condiciones_activacion, el perfil de sesion "
    "acumulado, la pregunta que se hizo, la respuesta del usuario, y si quedan "
    "repreguntas disponibles en este nodo.\n\n"
    "Reglas:\n"
    "- Si la respuesta indica que el usuario quiere su plan final (aunque no "
    "use un comando exacto, p.ej. 'dame mi plan', 'ya tengo suficiente', "
    "'terminemos'), usa accion='generar_plan'.\n"
    "- Si la respuesta indica que el usuario quiere salir sin plan (p.ej. 'no "
    "quiero seguir', 'olvidalo', 'dejalo asi'), usa accion='salir'.\n"
    "- Si la respuesta discrimina con claridad hacia uno de los candidatos, "
    "usa accion='avanzar' y siguiente=el id exacto de ese candidato.\n"
    "- Si la respuesta NO discrimina entre los candidatos y "
    "repreguntas_disponibles=true, usa accion='repreguntar' con UNA pregunta "
    "de seguimiento especifica y breve que ayude a distinguir.\n"
    "- Si repreguntas_disponibles=false, NUNCA uses accion='repreguntar': "
    "elige el candidato mas probable con la informacion que tienes y usa "
    "accion='avanzar'.\n"
    "- Si la respuesta revela informacion nueva y relevante sobre el proyecto "
    "o la situacion del usuario (mas alla de solo elegir camino), resumela en "
    "1 o 2 frases en perfil_update. Si no hay nada nuevo que agregar, "
    "perfil_update debe ser null.\n"
    "- 'siguiente' DEBE ser exactamente uno de los ids de los candidatos "
    "cuando accion='avanzar', y null en cualquier otro caso.\n"
    "- 'repregunta' debe tener texto solo cuando accion='repreguntar'; si no, "
    "null.\n\n"
    "Responde SOLO un JSON: {\"accion\": \"avanzar\"|\"repreguntar\"|"
    "\"generar_plan\"|\"salir\", \"siguiente\": str|null, \"repregunta\": "
    "str|null, \"perfil_update\": str|null}."
)

SYSTEM_PLAN = (
    "Eres el redactor final de una app de emprendimiento. Recibes un JSON con "
    "entrada_original (el texto libre con el que la persona empezo), "
    "perfil_sesion (lo que revelo sobre su proyecto a lo largo del recorrido) "
    "y recorrido (los conceptos que visito en orden, cada uno con pasos "
    "accionables y un entregable esperado). Redacta un plan de accion en "
    "espanol comun, claro y poderoso, como un project manager excelente que "
    "habla simple: un titulo breve que refleje el proyecto especifico de la "
    "persona (no generico), un parrafo de contexto que conecte su entrada "
    "original y su perfil con lo que va a lograr, y una secuencia numerada de "
    "pasos concretos agrupados por etapas, con el entregable de cada etapa "
    "como punto de control. Sin jerga sin explicar, sin autores, sin relleno "
    "motivacional. Todo lo que escribas debe salir del material recibido; no "
    "inventes tecnicas nuevas."
)


def cargar_grafo():
    return json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]


def cargar_quiz():
    return json.load(open(QUIZ_PATH, encoding="utf-8"))


def cargar_entry_seeds():
    return json.load(open(ENTRY_SEEDS_PATH, encoding="utf-8"))["seeds"]


def cargar_preguntas_cache():
    if PREGUNTAS_CACHE_PATH.exists():
        return json.load(open(PREGUNTAS_CACHE_PATH, encoding="utf-8"))
    return {}


def preguntar_opcion(texto, opciones, extra=""):
    """Menu numerado de emergencia. Devuelve indice elegido, o 'P'/'Q' si extra los permite."""
    print("\n" + texto)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    if extra:
        print(f"  {extra}")
    while True:
        r = input("> ").strip().upper()
        if r in ("P", "Q") and extra:
            return r
        if r.isdigit() and 1 <= int(r) <= len(opciones):
            return int(r) - 1
        print("Opcion no valida, intenta de nuevo.")


def _parsear_json(raw):
    return json.loads(raw.strip().removeprefix("```json").removesuffix("```").strip())


def llamar_claude(system, user_text, model, max_tokens=1500):
    import anthropic
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=model, max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_text}],
    )
    stats = USO.setdefault(model, {"in": 0, "out": 0, "llamadas": 0, "cache_read": 0})
    stats["in"] += msg.usage.input_tokens
    stats["out"] += msg.usage.output_tokens
    stats["cache_read"] += getattr(msg.usage, "cache_read_input_tokens", 0) or 0
    stats["llamadas"] += 1
    return "".join(b.text for b in msg.content if b.type == "text")


def reportar_costo():
    print("\n" + "=" * 60)
    print("  Costo real de la sesion (tokens)")
    print("=" * 60)
    total = 0.0
    for model, s in USO.items():
        pin, pout = PRECIOS.get(model, (0.0, 0.0))
        costo = s["in"] / 1_000_000 * pin + s["out"] / 1_000_000 * pout
        total += costo
        print(f"  {model}: {s['llamadas']} llamadas | {s['in']} in / {s['out']} out "
              f"(cache_read {s['cache_read']}) | ${costo:.4f}")
    print(f"  TOTAL: ${total:.4f}")


def clasificar_entrada(texto, entry_seeds, graph):
    """Capa 1: texto libre -> (puerta_id, perfil_sesion). Fallback: cuestionario cerrado."""
    if API_KEY:
        puertas = [
            {
                "id": s,
                "fase": graph[s]["fase_proyecto"],
                "titulo": graph[s]["titulo_concepto"],
                "resumen": graph[s]["resumen_teorico"][:200],
            }
            for s in entry_seeds
        ]
        ctx = {"texto_usuario": texto, "puertas": puertas}
        try:
            raw = llamar_claude(SYSTEM_CLASIFICACION, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=400)
            data = _parsear_json(raw)
            if data["puerta_id"] in entry_seeds:
                return data["puerta_id"], (data.get("perfil_sesion") or "").strip()
            raise ValueError(f"puerta_id fuera de las 20 puertas: {data.get('puerta_id')}")
        except Exception as e:
            print(f"  (fallo la clasificacion con IA, uso cuestionario cerrado: {e})")
    quiz = cargar_quiz()
    pf = quiz["pregunta_fase"]
    i = preguntar_opcion(pf["texto"], [o["texto"] for o in pf["opciones"]])
    fase = pf["opciones"][i]["fase"]
    pp = quiz["pregunta_puerta"][fase]
    i = preguntar_opcion(pp["texto"], [o["texto"] for o in pp["opciones"]])
    return pp["opciones"][i]["nodo"], ""


def obtener_pregunta(node_id, node, cache):
    """Pregunta abierta pregenerada para este nodo, o una generica si no esta en el cache."""
    entry = cache.get(node_id)
    if entry and entry.get("pregunta"):
        return entry["pregunta"]
    return (
        f"Pensando en \"{node['titulo_concepto']}\", cuentame en tus palabras "
        "donde estas parado ahora mismo con tu proyecto y que es lo que mas "
        "te preocupa o te entusiasma."
    )


def interpretar_turno(node, candidatos_ids, graph, perfil_sesion, pregunta_hecha, respuesta, repreguntas_disponibles):
    """Capa 2, por turno: interpreta la respuesta libre. Devuelve None si la API falla."""
    ctx = {
        "concepto_actual": {"titulo": node["titulo_concepto"], "resumen": node["resumen_teorico"][:400]},
        "candidatos": [
            {
                "id": c,
                "titulo": graph[c]["titulo_concepto"],
                "condiciones_activacion": graph[c].get("condiciones_activacion", [])[:3],
            }
            for c in candidatos_ids
        ],
        "perfil_sesion": perfil_sesion,
        "pregunta_hecha": pregunta_hecha,
        "respuesta_usuario": respuesta,
        "repreguntas_disponibles": repreguntas_disponibles,
    }
    try:
        raw = llamar_claude(SYSTEM_INTERPRETE, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=500)
        data = _parsear_json(raw)
        accion = data.get("accion")
        if accion not in ("avanzar", "repreguntar", "generar_plan", "salir"):
            raise ValueError(f"accion invalida: {accion}")
        if accion == "avanzar" and data.get("siguiente") not in candidatos_ids:
            raise ValueError(f"siguiente invalido: {data.get('siguiente')}")
        if accion == "repreguntar" and not repreguntas_disponibles:
            raise ValueError("el modelo repregunto sin repreguntas disponibles")
        return data
    except Exception as e:
        print(f"  (fallo el interprete con IA, uso menu de emergencia: {e})")
        return None


def _menu_emergencia(candidatos, graph):
    ops = []
    for c in candidatos:
        cn = graph[c]
        cond = (cn.get("condiciones_activacion") or [""])[0]
        pista = f"  <- si: {cond[:70]}" if cond else ""
        ops.append(f"{cn['titulo_concepto']}{pista}")
    r = preguntar_opcion("¿Hacia dónde seguimos? (modo de emergencia, sin IA)", ops,
                         extra="P. Generar mi plan ahora   Q. Salir sin plan")
    if r == "Q":
        return {"accion": "salir", "siguiente": None, "perfil_update": None}
    if r == "P":
        return {"accion": "generar_plan", "siguiente": None, "perfil_update": None}
    return {"accion": "avanzar", "siguiente": candidatos[r], "perfil_update": None}


def ensamblar_plan(ruta, graph, perfil_sesion, texto_original):
    material = []
    for nid in ruta:
        n = graph[nid]
        material.append({
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
        })
    if API_KEY:
        payload = {"entrada_original": texto_original, "perfil_sesion": perfil_sesion, "recorrido": material}
        try:
            return llamar_claude(SYSTEM_PLAN, json.dumps(payload, ensure_ascii=False), MODEL, max_tokens=2000)
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
    out = ["# Tu plan de accion", ""]
    if texto_original or perfil_sesion:
        out.append("## Contexto")
        if texto_original:
            out.append(f"Punto de partida: {texto_original}")
        if perfil_sesion:
            out.append(f"Lo que sabemos de tu proyecto: {perfil_sesion}")
        out.append("")
    for i, m in enumerate(material, 1):
        out.append(f"## Etapa {i}: {m['concepto']}")
        for j, p in enumerate(m["pasos"], 1):
            out.append(f"  {i}.{j} {p}")
        if m["entregable"]:
            out.append(f"  Punto de control: {m['entregable']}")
        out.append("")
    return "\n".join(out)


def main():
    graph = cargar_grafo()
    entry_seeds = cargar_entry_seeds()
    preguntas_cache = cargar_preguntas_cache()

    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo (entrevista guiada)")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'} | "
          f"preguntas cacheadas: {len(preguntas_cache)}")
    print("=" * 60)

    texto_original = input("\nCuentame tu idea o tu situacion actual, con tus palabras:\n> ")
    actual_id, perfil_sesion = clasificar_entrada(texto_original, entry_seeds, graph)

    visitados, ruta = {actual_id}, [actual_id]
    while True:
        n = graph[actual_id]
        print("\n" + "-" * 60)
        print(f"[{len(ruta)}/{MAX_DEPTH}] {n['titulo_concepto']}")
        print(textwrap.fill(n["resumen_teorico"], 76)[:600])
        candidatos = [t for t in n.get("nodos_siguientes", []) if t in graph and t not in visitados][:MAX_OPCIONES]
        if not candidatos or len(ruta) >= MAX_DEPTH:
            motivo = "llegaste a un punto de cierre" if not candidatos else "recorrido completo"
            print(f"\n({motivo}: generamos tu plan)")
            break

        pregunta_actual = obtener_pregunta(actual_id, n, preguntas_cache)
        repreguntas_usadas = 0
        resultado = None
        while resultado is None:
            respuesta = input("\n" + pregunta_actual + "\n> ")
            resultado = interpretar_turno(
                n, candidatos, graph, perfil_sesion, pregunta_actual, respuesta,
                repreguntas_disponibles=(repreguntas_usadas < MAX_REPREGUNTAS_POR_NODO),
            )
            if resultado is None:
                resultado = _menu_emergencia(candidatos, graph)
            elif resultado["accion"] == "repreguntar":
                repreguntas_usadas += 1
                pregunta_actual = resultado["repregunta"]
                resultado = None

        if resultado.get("perfil_update"):
            perfil_sesion = (perfil_sesion + "\n" + resultado["perfil_update"]).strip() if perfil_sesion else resultado["perfil_update"]

        if resultado["accion"] == "salir":
            print("\nHasta pronto.")
            reportar_costo()
            return
        if resultado["accion"] == "generar_plan":
            break
        actual_id = resultado["siguiente"]
        visitados.add(actual_id)
        ruta.append(actual_id)

    print("\nEnsamblando tu plan...\n")
    plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original)
    print(plan)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    print(f"Ruta recorrida ({len(ruta)}): {' -> '.join(ruta)}")
    reportar_costo()


if __name__ == "__main__":
    main()
