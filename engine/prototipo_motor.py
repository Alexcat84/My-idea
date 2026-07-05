# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Prototipo CLI del motor de ruteo (Fase 2.2)

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
    turno, cae a un menu numerado de emergencia para ese turno. El
    interprete ademas pondera senales de miedo/riesgo/duda hacia candidatos
    de validacion con clientes (ver engine/plan_readiness.py).
Medidor de completitud: antes de redactar el plan, se evalua si la ruta toca
    al menos una familia de accion con clientes y una de viabilidad
    economica (engine/plan_readiness.py). Si no, se ofrece UNA vez la
    opcion de continuar ("go deeper") o recibir un plan inicial honesto. La
    sesion se persiste en engine/sessions/{id}.json y se puede retomar con
    --continuar {id}.
Capa 3 (plan final): Sonnet redacta el plan en modo imperativo (tareas, no
    preguntas) a partir de la entrada original, el perfil de sesion
    acumulado y la ruta completa, marcando si es un plan inicial o completo.

Uso:  python engine/prototipo_motor.py
      python engine/prototipo_motor.py --continuar SESSION_ID
Guardrails: profundidad maxima 15, sin ciclos (nodos visitados no se
reofrecen), maximo 1 repregunta por nodo antes de forzar el candidato mas
probable, el medidor de completitud solo se ofrece una vez por sesion.
"""
import argparse
import json
import os
import sys
import textwrap
import uuid
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

import plan_readiness

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
SESSIONS_DIR = BASE / "engine" / "sessions"

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
    "- Si la respuesta expresa un miedo, riesgo o duda no resuelta (p.ej. "
    "'que nadie lo use', 'no se si pagarian', 'me preocupa que...'), da "
    "preferencia a los candidatos cuyas condiciones_activacion atienden esa "
    "senal (validacion con clientes reales, pruebas baratas, MVP) por encima "
    "de una continuacion puramente teorica, aunque otro candidato parezca "
    "tematicamente mas cercano.\n"
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

SYSTEM_PROFUNDIZAR = (
    "Interpretas la respuesta de un usuario a la pregunta de si quiere su "
    "plan de negocio ahora mismo (aunque le falten algunas partes) o "
    "prefiere responder unas preguntas mas para tener un plan mas completo. "
    "Responde SOLO un JSON: {\"decision\": \"generar_ya\"|\"continuar\"}."
)

SYSTEM_PLAN = (
    "Eres el redactor final de una app de emprendimiento. Recibes un JSON con "
    "entrada_original (el texto libre con el que la persona empezo), "
    "perfil_sesion (lo que revelo sobre su proyecto a lo largo del recorrido) "
    "y recorrido: una lista ordenada de conceptos, cada uno con titulo, pasos "
    "(el material original, a menudo en forma de preguntas o pasos "
    "reflexivos), entregable esperado, y es_viabilidad_economica (si el "
    "concepto trata de costos, precios o numeros del negocio).\n\n"
    "Reglas obligatorias:\n"
    "1. Modo imperativo SIEMPRE. Convierte cada paso reflexivo o pregunta del "
    "material en una tarea concreta con verbo, sujeto y criterio de exito. "
    "Ejemplo: el material dice '¿has validado con clientes reales?' y tu "
    "escribes 'Entrevista a 5 personas de tu publico objetivo esta semana y "
    "anota como resuelven el problema hoy'.\n"
    "2. Cada etapa termina con una linea 'Esta semana:' seguida de UNA accion "
    "ejecutable en 7 dias, concreta y especifica al proyecto de la persona.\n"
    "3. Si al menos una etapa del recorrido tiene es_viabilidad_economica=true, "
    "agrega al final una seccion '## ¿Es negocio? Los numeros en simple' que "
    "sintetice esos conceptos en palabras comunes, usando solo lo que esta en "
    "el material. Si NINGUNA etapa lo tiene, NO agregues esa seccion ni "
    "inventes cifras.\n"
    "4. Prohibido cerrar el plan con preguntas para el usuario. El plan "
    "cierra con la primera accion concreta del lunes, no con una pregunta.\n"
    "5. Titulo breve especifico al proyecto (no generico), un parrafo de "
    "contexto que conecte entrada_original y perfil_sesion con lo que va a "
    "lograr.\n\n"
    "Espanol comun, sin jerga sin explicar, sin autores, sin relleno "
    "motivacional. Todo debe salir del material recibido; no inventes "
    "tecnicas nuevas."
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


def guardar_sesion(session_id, ruta, perfil_sesion, texto_original, profundizar_ofrecido):
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "ruta": ruta,
        "perfil_sesion": perfil_sesion,
        "entrada_original": texto_original,
        "profundizar_ofrecido": profundizar_ofrecido,
        "timestamp": datetime.now().isoformat(),
    }
    (SESSIONS_DIR / f"{session_id}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_sesion(session_id):
    path = SESSIONS_DIR / f"{session_id}.json"
    if not path.exists():
        print(f"ERROR: no existe la sesion {session_id} en {SESSIONS_DIR}")
        sys.exit(1)
    return json.load(open(path, encoding="utf-8"))


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


def preguntar_profundizar(familias_faltantes):
    """Ofrece UNA vez la disyuntiva plan-inicial-ya vs. seguir profundizando."""
    faltan_txt = "; ".join(familias_faltantes)
    mensaje = (
        f"Puedo darte tu plan ahora mismo. Eso si: con algunas preguntas mas "
        f"incluiria {faltan_txt}. ¿Seguimos un poco o lo quieres ya?"
    )
    respuesta = input("\n" + mensaje + "\n> ")
    if API_KEY:
        try:
            raw = llamar_claude(SYSTEM_PROFUNDIZAR, respuesta, MODEL_HAIKU, max_tokens=100)
            data = _parsear_json(raw)
            if data.get("decision") in ("generar_ya", "continuar"):
                return data["decision"]
        except Exception as e:
            print(f"  (fallo la interpretacion, uso deteccion simple: {e})")
    low = respuesta.strip().lower()
    if any(p in low for p in ("ya", "ahora", "dame", "listo", "asi esta bien", "así está bien")):
        return "generar_ya"
    return "continuar"


def ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id):
    material = []
    for nid in ruta:
        n = graph[nid]
        material.append({
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
            "es_viabilidad_economica": families.get(nid) == "viabilidad_economica",
        })
    if API_KEY:
        payload = {"entrada_original": texto_original, "perfil_sesion": perfil_sesion, "recorrido": material}
        try:
            cuerpo = llamar_claude(SYSTEM_PLAN, json.dumps(payload, ensure_ascii=False), MODEL, max_tokens=4096)
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
            cuerpo = _ensamblar_offline(material, perfil_sesion, texto_original)
    else:
        cuerpo = _ensamblar_offline(material, perfil_sesion, texto_original)

    etiqueta = "Plan completo" if evaluacion["es_completa"] else "Plan inicial"
    partes = [f"_{etiqueta}_", "", cuerpo]
    if not evaluacion["es_completa"]:
        partes += ["", "---", "", "## Lo que este plan aun no cubre", ""]
        for f in evaluacion["familias_faltantes"]:
            partes.append(f"- {f}")
        partes += ["", f"Para profundizar, continua la sesion: "
                        f"`python engine/prototipo_motor.py --continuar {session_id}`"]
    return "\n".join(partes)


def _ensamblar_offline(material, perfil_sesion, texto_original):
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


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--continuar", metavar="SESSION_ID", default=None,
                    help="Retoma una sesion previa desde su ultimo nodo (engine/sessions/{id}.json)")
    return ap.parse_args()


def main():
    args = parse_args()
    graph = cargar_grafo()
    entry_seeds = cargar_entry_seeds()
    preguntas_cache = cargar_preguntas_cache()
    families = plan_readiness.cargar_families(graph)

    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo (entrevista guiada)")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'} | "
          f"preguntas cacheadas: {len(preguntas_cache)}")
    print("=" * 60)

    if args.continuar:
        sesion = cargar_sesion(args.continuar)
        session_id = args.continuar
        ruta = sesion["ruta"]
        visitados = set(ruta)
        actual_id = ruta[-1]
        perfil_sesion = sesion["perfil_sesion"]
        texto_original = sesion["entrada_original"]
        profundizar_ofrecido = sesion.get("profundizar_ofrecido", False)
        print(f"\nRetomando sesion {session_id} desde: {graph[actual_id]['titulo_concepto']}")
    else:
        session_id = uuid.uuid4().hex[:8]
        texto_original = input("\nCuentame tu idea o tu situacion actual, con tus palabras:\n> ")
        actual_id, perfil_sesion = clasificar_entrada(texto_original, entry_seeds, graph)
        visitados, ruta = {actual_id}, [actual_id]
        profundizar_ofrecido = False
        guardar_sesion(session_id, ruta, perfil_sesion, texto_original, profundizar_ofrecido)

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
            evaluacion = plan_readiness.evaluar_ruta(ruta, families)
            if not evaluacion["es_completa"] and not profundizar_ofrecido:
                profundizar_ofrecido = True
                guardar_sesion(session_id, ruta, perfil_sesion, texto_original, profundizar_ofrecido)
                if preguntar_profundizar(evaluacion["familias_faltantes"]) == "continuar":
                    print("\nPerfecto, sigamos un poco mas.")
                    continue
            break

        actual_id = resultado["siguiente"]
        visitados.add(actual_id)
        ruta.append(actual_id)
        guardar_sesion(session_id, ruta, perfil_sesion, texto_original, profundizar_ofrecido)

    evaluacion = plan_readiness.evaluar_ruta(ruta, families)
    print("\nEnsamblando tu plan...\n")
    plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id)
    print(plan)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    print(f"Ruta recorrida ({len(ruta)}): {' -> '.join(ruta)}")
    reportar_costo()


if __name__ == "__main__":
    main()
