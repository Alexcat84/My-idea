# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Prototipo CLI del motor de ruteo (Fase 2.3)

Entrevista guiada de texto libre con travesia silenciosa multi-salto: el
usuario nunca elige de un menu, y el intérprete puede atravesar varios nodos
en silencio cuando lo que el usuario ya conto (entrada original, perfil de
sesion, respuestas previas) responde lo que esos nodos preguntarian. Se
detiene a preguntar solo en el primer punto donde el contexto no alcanza
para decidir entre ramas.

Capa 1 (entrada): texto libre -> clasificado con Haiku hacia una de las 20
    puertas curadas (dataset/metadata/entry_seeds.json), generando un
    perfil_sesion inicial. Si la API falla, cae al cuestionario cerrado
    (engine/cuestionario_raiz.json) como respaldo.
Capa 2 (recorrido, travesia silenciosa): en cada punto de decision, el
    interprete (Haiku) recibe el nodo actual, sus sucesores (nivel 1) Y los
    sucesores de esos sucesores (nivel 2), mas todo el contexto acumulado.
    Devuelve un camino de 1 a 3 nodos: los que el contexto ya responde se
    atraviesan en silencio (cuentan para el plan y las familias del
    medidor, pero no se preguntan), y se detiene a preguntar solo en el
    ultimo nodo del camino si pregunta_necesaria=true. La pregunta de cada
    nodo esta pregenerada y cacheada (engine/preguntas_cache.json) porque
    depende de la topologia, no del usuario. Si la API falla en un turno,
    cae a un menu numerado de emergencia (un solo salto). El interprete
    ademas pondera senales de miedo/riesgo/duda hacia candidatos de
    validacion con clientes (ver engine/plan_readiness.py).
Medidor de completitud: antes de redactar el plan, se evalua si la ruta toca
    al menos una familia de accion con clientes y una de viabilidad
    economica (engine/plan_readiness.py). Si no, se ofrece UNA vez la
    opcion de continuar ("go deeper") o recibir un plan inicial honesto. La
    sesion se persiste en engine/sessions/{id}.json (incluyendo que nodos
    fueron conversados vs. cubiertos en silencio) y se puede retomar con
    --continuar {id}.
Capa 3 (plan final): Sonnet redacta el plan en modo imperativo (tareas, no
    preguntas) a partir de la entrada original, el perfil de sesion
    acumulado y la ruta completa, marcando si es un plan inicial o completo.
    El lenguaje de cara al usuario habla de "idea/proyecto", no de
    "negocio", salvo que el analisis economico o el propio usuario lo
    traigan a la conversacion.

Uso:  python engine/prototipo_motor.py
      python engine/prototipo_motor.py --continuar SESSION_ID
Guardrails: profundidad maxima 15 (cuenta todos los nodos, conversados y
silenciosos), maximo 3 nodos silenciosos por llamada al interprete, maximo 1
repregunta por punto de decision antes de forzar el camino mas probable, el
medidor de completitud solo se ofrece una vez por sesion.
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
MAX_SUCESORES_NIVEL2 = 4
MAX_SALTOS_SILENCIOSOS_POR_LLAMADA = 3
MAX_REPREGUNTAS_POR_PUNTO = 1

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
    "usuario describe su idea o su situacion en texto libre. Debes: 1) elegir "
    "la puerta de entrada que mejor corresponde a su fase y necesidad actual, "
    "de una lista fija de puertas (cada una con id, fase y una breve "
    "descripcion), y 2) redactar un perfil_sesion: un resumen breve (2 a 4 "
    "frases) de lo que el usuario revelo sobre su idea o situacion, para que "
    "las etapas posteriores no pierdan ese contexto. Responde SOLO un JSON: "
    "{\"puerta_id\": str, \"perfil_sesion\": str}. El puerta_id DEBE ser "
    "exactamente uno de los ids de la lista dada."
)

SYSTEM_INTERPRETE_MULTI = (
    "Eres el interprete de una entrevista guiada de emprendimiento que puede "
    "avanzar varios pasos del grafo en silencio cuando el contexto del "
    "usuario ya responde lo que esos nodos preguntarian, y se detiene a "
    "preguntar solo en el primer punto donde el contexto no alcanza para "
    "decidir entre ramas.\n\n"
    "Recibes: la entrada original del usuario, el perfil de sesion "
    "acumulado, el nodo actual, sus sucesores inmediatos (nivel 1) con sus "
    "condiciones_activacion, y los sucesores de esos sucesores (nivel 2, "
    "resumidos). Tambien, si aplica, la ultima pregunta hecha y la "
    "respuesta libre del usuario a esa pregunta (puede ser null si aun no "
    "se ha hecho ninguna pregunta en este punto y solo cuentas con el "
    "contexto acumulado).\n\n"
    "Tu trabajo es construir un camino: la secuencia de nodos (1 a 3, en "
    "orden, empezando por un sucesor de nivel 1) que el usuario deberia "
    "atravesar dado lo que ya se sabe de el. Un nodo se atraviesa EN "
    "SILENCIO (sin preguntarlo) solo si el contexto acumulado responde con "
    "claridad razonable lo que ese nodo necesitaria saber para elegir su "
    "propio siguiente paso. Detente en el primer nodo donde el contexto NO "
    "alcance para decidir entre sus propios sucesores: ese es el ultimo "
    "nodo del camino, y marca pregunta_necesaria=true porque ahi hace falta "
    "preguntarle al usuario.\n\n"
    "Reglas:\n"
    "- Maximo 3 nodos en el camino por llamada. Si el contexto alcanzaria "
    "para seguir mas alla del tercero, detente igual en el tercero y marca "
    "pregunta_necesaria=false (se continuara en la siguiente llamada, sin "
    "preguntar, mientras el contexto siga alcanzando).\n"
    "- Si la respuesta del usuario a la ultima pregunta no discrimina entre "
    "los sucesores inmediatos y repreguntas_disponibles=true, usa "
    "accion='repreguntar' con UNA pregunta de seguimiento especifica y "
    "breve.\n"
    "- Si repreguntas_disponibles=false, NUNCA repreguntes: elige el camino "
    "mas probable con lo que tienes y usa accion='avanzar'.\n"
    "- Si en cualquier punto el usuario expresa que quiere su plan final "
    "(aunque no use un comando exacto, p.ej. 'dame mi plan', 'ya tengo "
    "suficiente'), usa accion='generar_plan'. Si quiere salir sin plan "
    "(p.ej. 'no quiero seguir', 'olvidalo'), usa accion='salir'.\n"
    "- Si la respuesta o el contexto expresa un miedo, riesgo o duda no "
    "resuelta (p.ej. 'que nadie lo use', 'no se si pagarian'), da "
    "preferencia en el camino a los nodos cuyas condiciones_activacion "
    "atienden esa senal (validacion con clientes reales, pruebas baratas, "
    "MVP) por encima de una continuacion puramente teorica.\n"
    "- Si la respuesta o el contexto revela informacion nueva y relevante "
    "sobre la idea o la situacion del usuario, resumela en 1 o 2 frases en "
    "perfil_update. Si no hay nada nuevo que agregar, perfil_update debe "
    "ser null.\n"
    "- 'camino' es la cadena LITERAL completa, sin saltos: el primer id "
    "SIEMPRE debe ser uno de los sucesores de nivel 1 dados. Si el nodo que "
    "te interesa es de nivel 2 (aparece dentro de 'sucesores' de un nodo de "
    "nivel 1), DEBES incluir primero ese nodo de nivel 1 como paso previo en "
    "'camino', y el de nivel 2 despues, en ese orden. Nunca pongas un nodo "
    "de nivel 2 sin su padre de nivel 1 inmediatamente antes en el mismo "
    "camino. Cada id debe ser un sucesor real del nodo anterior en la "
    "cadena, nunca un id repetido ni inventado.\n"
    "- 'repregunta' debe tener texto solo cuando accion='repreguntar'; si "
    "no, null.\n\n"
    "Responde SOLO un JSON: {\"accion\": \"avanzar\"|\"repreguntar\"|"
    "\"generar_plan\"|\"salir\", \"camino\": [ids en orden], "
    "\"pregunta_necesaria\": bool, \"repregunta\": str|null, "
    "\"perfil_update\": str|null}."
)

SYSTEM_PROFUNDIZAR = (
    "Interpretas la respuesta de un usuario a la pregunta de si quiere su "
    "plan ahora mismo (aunque le falten algunas partes) o prefiere "
    "responder unas preguntas mas para tener un plan mas completo. "
    "Responde SOLO un JSON: {\"decision\": \"generar_ya\"|\"continuar\"}."
)

SYSTEM_PLAN = (
    "Eres el redactor final de una app de emprendimiento. Recibes un JSON con "
    "entrada_original (el texto libre con el que la persona empezo), "
    "perfil_sesion (lo que revelo sobre su idea a lo largo del recorrido) "
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
    "agrega al final una seccion '## ¿Puede sostenerse tu idea? Los numeros "
    "en simple' que sintetice esos conceptos en palabras comunes, usando "
    "solo lo que esta en el material. Si NINGUNA etapa lo tiene, NO "
    "agregues esa seccion ni inventes cifras.\n"
    "4. Prohibido cerrar el plan con preguntas para el usuario. El plan "
    "cierra con la primera accion concreta del lunes, no con una pregunta.\n"
    "5. Titulo breve especifico al proyecto (no generico), un parrafo de "
    "contexto que conecte entrada_original y perfil_sesion con lo que va a "
    "lograr.\n"
    "6. Habla siempre de la IDEA o el PROYECTO del usuario. Usa la palabra "
    "'negocio' unicamente si el analisis economico forma parte del "
    "material recibido, o si el propio usuario ya la uso en su entrada o "
    "perfil_sesion.\n\n"
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


def guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido):
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "ruta": ruta,
        "modos": modos,
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
    texto = raw.strip().removeprefix("```json").removesuffix("```").strip()
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        # El modelo a veces agrega texto despues del primer objeto JSON valido
        # (p.ej. una nota o una repeticion); raw_decode toma solo el primero.
        obj, _ = json.JSONDecoder().raw_decode(texto)
        return obj


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
        "donde estas parado ahora mismo con tu idea y que es lo que mas "
        "te preocupa o te entusiasma."
    )


def sucesores_nivel(nid, graph, visitados, limite=MAX_OPCIONES):
    return [c for c in graph[nid].get("nodos_siguientes", []) if c in graph and c not in visitados][:limite]


def resumen_nodo(nid, graph):
    n = graph[nid]
    return {
        "id": nid,
        "titulo": n["titulo_concepto"],
        "condiciones_activacion": n.get("condiciones_activacion", [])[:2],
    }


def _validar_camino(actual_id, camino, graph, visitados):
    if not camino or len(camino) > MAX_SALTOS_SILENCIOSOS_POR_LLAMADA:
        raise ValueError(f"camino invalido (vacio o excede {MAX_SALTOS_SILENCIOSOS_POR_LLAMADA}): {camino}")
    prev = actual_id
    vistos_en_camino = set()
    for nid in camino:
        if nid not in graph or nid in visitados or nid in vistos_en_camino:
            raise ValueError(f"nodo invalido o repetido en camino: {nid}")
        if nid not in graph[prev].get("nodos_siguientes", []):
            raise ValueError(f"{nid} no es sucesor de {prev}")
        vistos_en_camino.add(nid)
        prev = nid


def interpretar_multi_salto(actual_id, graph, visitados, perfil_sesion, texto_original,
                             pregunta_hecha, respuesta_usuario, repreguntas_disponibles):
    """Capa 2: decide un camino de 1-3 nodos (silenciosos + a lo sumo uno conversado).
    Devuelve None si la API falla o el resultado no es valido."""
    nivel1_ids = sucesores_nivel(actual_id, graph, visitados)
    nivel1 = []
    visitados_o_nivel1 = visitados | set(nivel1_ids)
    for nid in nivel1_ids:
        nivel2_ids = sucesores_nivel(nid, graph, visitados_o_nivel1, limite=MAX_SUCESORES_NIVEL2)
        entrada_nivel1 = resumen_nodo(nid, graph)
        entrada_nivel1["sucesores"] = [resumen_nodo(n2, graph) for n2 in nivel2_ids]
        nivel1.append(entrada_nivel1)

    ctx = {
        "entrada_original": texto_original,
        "perfil_sesion": perfil_sesion,
        "nodo_actual": resumen_nodo(actual_id, graph),
        "sucesores_nivel1_y_nivel2": nivel1,
        "pregunta_hecha": pregunta_hecha,
        "respuesta_usuario": respuesta_usuario,
        "repreguntas_disponibles": repreguntas_disponibles,
    }
    try:
        raw = llamar_claude(SYSTEM_INTERPRETE_MULTI, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=600)
        data = _parsear_json(raw)
        accion = data.get("accion")
        if accion not in ("avanzar", "repreguntar", "generar_plan", "salir"):
            raise ValueError(f"accion invalida: {accion}")
        if accion == "repreguntar" and not repreguntas_disponibles:
            raise ValueError("el modelo repregunto sin repreguntas disponibles")
        if accion == "avanzar":
            camino = data.get("camino") or []
            _validar_camino(actual_id, camino, graph, visitados)
            data["camino"] = camino
            data["pregunta_necesaria"] = bool(data.get("pregunta_necesaria", True))
        return data
    except Exception as e:
        print(f"  (fallo el interprete multi-salto, uso menu de emergencia: {e})")
        return None


def _menu_emergencia(nivel1_ids, graph):
    ops = []
    for c in nivel1_ids:
        cn = graph[c]
        cond = (cn.get("condiciones_activacion") or [""])[0]
        pista = f"  <- si: {cond[:70]}" if cond else ""
        ops.append(f"{cn['titulo_concepto']}{pista}")
    r = preguntar_opcion("¿Hacia dónde seguimos? (modo de emergencia, sin IA)", ops,
                         extra="P. Generar mi plan ahora   Q. Salir sin plan")
    if r == "Q":
        return {"accion": "salir", "camino": [], "pregunta_necesaria": True, "perfil_update": None}
    if r == "P":
        return {"accion": "generar_plan", "camino": [], "pregunta_necesaria": True, "perfil_update": None}
    return {"accion": "avanzar", "camino": [nivel1_ids[r]], "pregunta_necesaria": True, "perfil_update": None}


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
            out.append(f"Lo que sabemos de tu idea: {perfil_sesion}")
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


def _imprimir_nodo(idx, total, node, modo, con_resumen=False):
    etiqueta = f"[{modo}]"
    print("\n" + "-" * 60)
    print(f"[{idx}/{total}] {etiqueta} {node['titulo_concepto']}")
    if con_resumen:
        print(textwrap.fill(node["resumen_teorico"], 76)[:600])
    else:
        print("  (cubierto por lo que ya contaste; no hace falta preguntarlo)")


def main():
    args = parse_args()
    graph = cargar_grafo()
    entry_seeds = cargar_entry_seeds()
    preguntas_cache = cargar_preguntas_cache()
    families = plan_readiness.cargar_families(graph)

    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo (travesia silenciosa)")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'} | "
          f"preguntas cacheadas: {len(preguntas_cache)}")
    print("=" * 60)

    pregunta_hecha, respuesta_usuario = None, None

    if args.continuar:
        sesion = cargar_sesion(args.continuar)
        session_id = args.continuar
        ruta = sesion["ruta"]
        modos = sesion.get("modos", ["conversado"] * len(ruta))
        visitados = set(ruta)
        actual_id = ruta[-1]
        perfil_sesion = sesion["perfil_sesion"]
        texto_original = sesion["entrada_original"]
        profundizar_ofrecido = sesion.get("profundizar_ofrecido", False)
        print(f"\nRetomando sesion {session_id} desde: {graph[actual_id]['titulo_concepto']}")
    else:
        session_id = uuid.uuid4().hex[:8]
        texto_original = input("\nCuéntame tu idea, o en qué punto estás con ella:\n> ")
        actual_id, perfil_sesion = clasificar_entrada(texto_original, entry_seeds, graph)
        visitados, ruta, modos = {actual_id}, [actual_id], ["conversado"]
        profundizar_ofrecido = False
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido)
        _imprimir_nodo(1, MAX_DEPTH, graph[actual_id], "puerta de entrada", con_resumen=True)

    repreguntas_usadas = 0
    while True:
        nivel1_ids = sucesores_nivel(actual_id, graph, visitados)
        if not nivel1_ids or len(ruta) >= MAX_DEPTH:
            motivo = "llegaste a un punto de cierre" if not nivel1_ids else "recorrido completo"
            print(f"\n({motivo}: generamos tu plan)")
            break

        resultado = interpretar_multi_salto(
            actual_id, graph, visitados, perfil_sesion, texto_original,
            pregunta_hecha, respuesta_usuario,
            repreguntas_disponibles=(repreguntas_usadas < MAX_REPREGUNTAS_POR_PUNTO),
        )
        if resultado is None:
            resultado = _menu_emergencia(nivel1_ids, graph)

        if resultado.get("perfil_update"):
            perfil_sesion = (perfil_sesion + "\n" + resultado["perfil_update"]).strip() if perfil_sesion else resultado["perfil_update"]

        if resultado["accion"] == "salir":
            print("\nHasta pronto.")
            reportar_costo()
            return

        if resultado["accion"] == "repreguntar":
            repreguntas_usadas += 1
            pregunta_hecha = resultado["repregunta"]
            print("\n" + "-" * 60)
            print(f"[{len(ruta)}/{MAX_DEPTH}] [conversado] {graph[actual_id]['titulo_concepto']}")
            respuesta_usuario = input("\n" + pregunta_hecha + "\n> ")
            continue

        if resultado["accion"] == "generar_plan":
            evaluacion = plan_readiness.evaluar_ruta(ruta, families)
            if not evaluacion["es_completa"] and not profundizar_ofrecido:
                profundizar_ofrecido = True
                guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido)
                if preguntar_profundizar(evaluacion["familias_faltantes"]) == "continuar":
                    print("\nPerfecto, sigamos un poco mas.")
                    pregunta_hecha, respuesta_usuario = None, None
                    repreguntas_usadas = 0
                    continue
            break

        # accion == "avanzar": camino de 1-3 nodos, algunos silenciosos + a lo sumo uno conversado al final
        camino = resultado["camino"]
        pregunta_necesaria = resultado["pregunta_necesaria"]
        for idx, nid in enumerate(camino):
            es_ultimo = idx == len(camino) - 1
            modo = "conversado" if (es_ultimo and pregunta_necesaria) else "silencioso"
            visitados.add(nid)
            ruta.append(nid)
            modos.append(modo)
            if modo == "silencioso":
                _imprimir_nodo(len(ruta), MAX_DEPTH, graph[nid], "silencioso", con_resumen=False)
        actual_id = camino[-1]
        repreguntas_usadas = 0
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido)

        if pregunta_necesaria:
            n = graph[actual_id]
            _imprimir_nodo(len(ruta), MAX_DEPTH, n, "conversado", con_resumen=True)
            pregunta_hecha = obtener_pregunta(actual_id, n, preguntas_cache)
            respuesta_usuario = input("\n" + pregunta_hecha + "\n> ")
        else:
            pregunta_hecha, respuesta_usuario = None, None

    evaluacion = plan_readiness.evaluar_ruta(ruta, families)
    print("\nEnsamblando tu plan...\n")
    plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id)
    print(plan)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    ruta_txt = " -> ".join(f"[{m[0]}]{nid}" for nid, m in zip(ruta, modos))
    print(f"Ruta recorrida ({len(ruta)}): {ruta_txt}")
    reportar_costo()


if __name__ == "__main__":
    main()
