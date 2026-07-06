# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Prototipo CLI del motor de ruteo (Fase 2.5)

Entrevista guiada de texto libre con travesia silenciosa multi-salto: el
usuario nunca elige de un menu, y el interprete puede atravesar varios nodos
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
Cosecha de vecindario (Fase 2.4): antes de redactar, se expande en silencio
    desde la ruta (conversada + silenciosa) hacia sus nodos_siguientes y
    nodos_previos adyacentes (hasta 25, priorizados por familia faltante,
    fase mayoritaria y afinidad con el perfil_sesion). El redactor recibe
    material_principal (la ruta, manda estructura y cronologia) y
    material_de_apoyo (la cosecha, enriquece etapas existentes sin crear
    etapas propias). El plan reporta cuantos conceptos lo alimentaron. La
    etiqueta inicial/completo y la seccion "no cubre" se calculan sobre
    ruta+cosecha (lo que el plan realmente contiene), no solo la ruta.

Fase 2.5 - persistencia y proyectos de largo plazo:
    - Persistencia en Supabase (engine/db.py) con fallback a JSON local
      (--offline): proyectos, sesiones, nodos cubiertos y planes.
    - estado_vivo: al cerrar cada sesion (no en --gratis), se comprime el
      estado_vivo anterior + las novedades de la sesion en una sintesis
      nueva de 300-500 tokens que alimenta la siguiente sesion.
    - --gratis: una sola llamada Haiku ("organizador de tu idea"), sin
      interview, con la regla dura de organizar y senalar huecos, nunca
      instruir.
    - --seguir PROJECT_ID: sesion de seguimiento. Capa 1 avanzada elige
      cualquier nodo del grafo (no solo las 20 puertas) segun estado_vivo +
      cobertura por familia + mensaje nuevo. El recorrido y la cosecha
      excluyen automaticamente los nodos ya cubiertos (se siembran en
      visitados). El plan de seguimiento abre reconociendo el avance.
    - Presupuesto duro por sesion (PRESUPUESTO_SESION_USD, env var,
      default 0.30): si el costo acumulado alcanza el tope, las llamadas
      posteriores fallan a proposito y cada punto de la app ya sabe caer a
      su respaldo offline existente (menu de emergencia, cuestionario
      cerrado, plan ensamblado sin IA). El evento se registra en la sesion.

Uso:  python engine/prototipo_motor.py
      python engine/prototipo_motor.py --continuar SESSION_ID
      python engine/prototipo_motor.py --gratis
      python engine/prototipo_motor.py --seguir PROJECT_ID
      python engine/prototipo_motor.py --offline   (fuerza JSON local en vez de Supabase)
Guardrails: profundidad maxima 15 (cuenta todos los nodos, conversados y
silenciosos), maximo 3 nodos silenciosos por llamada al interprete, maximo 1
repregunta por punto de decision antes de forzar el camino mas probable, el
medidor de completitud solo se ofrece una vez por sesion, presupuesto duro
por sesion con degradacion elegante a modo offline.
"""
import argparse
import json
import os
import re
import sys
import textwrap
import unicodedata
import uuid
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

import db
import plan_readiness

# En consolas de Windows, stdout suele quedar en cp1252 (o el codepage local),
# que no puede representar caracteres como flechas (->) o comillas tipograficas
# presentes en el contenido de algunos nodos. Sin esto, print() lanza
# UnicodeEncodeError y el programa se cae a mitad de un recorrido.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

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

PRESUPUESTO_SESION_USD = float(os.environ.get("PRESUPUESTO_SESION_USD", "0.30"))
PRESUPUESTO_EXCEDIDO = False

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

SYSTEM_PUERTA_AVANZADA = (
    "Eres el clasificador de seguimiento de un proyecto de emprendimiento ya "
    "en marcha. Recibes el estado_vivo del proyecto (sintesis acumulada de "
    "sesiones previas, puede ser null si es la primera vez que se comprime), "
    "un mensaje nuevo del usuario contando que ha pasado desde la ultima "
    "sesion, y una lista de conceptos candidatos (id, titulo, resumen corto, "
    "fase, condiciones_activacion) que el proyecto TODAVIA NO ha cubierto. "
    "Elige el candidato que mejor sirva como punto de entrada para retomar "
    "la conversacion ahora mismo, dado el momento real del proyecto. Tambien "
    "redacta un perfil_sesion actualizado (2 a 4 frases) que combine lo que "
    "ya se sabia (estado_vivo) con lo nuevo que cuenta el mensaje. Responde "
    "SOLO un JSON: {\"puerta_id\": str, \"perfil_sesion\": str}. El "
    "puerta_id DEBE ser exactamente uno de los candidatos dados."
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
    "entrada_original (el texto libre con el que la persona empezo o el "
    "mensaje nuevo de esta sesion si es un seguimiento), "
    "perfil_sesion (lo que revelo sobre su idea a lo largo del recorrido), "
    "material_principal: la ruta conversada (lista ordenada de conceptos, "
    "cada uno con titulo, pasos, entregable esperado, y "
    "es_viabilidad_economica), material_de_apoyo: conceptos vecinos del "
    "grafo (mismo formato) que NO fueron conversados con el usuario pero son "
    "relevantes a su perfil, y opcionalmente es_seguimiento + "
    "estado_vivo_previo si esta sesion continua un proyecto ya en marcha.\n\n"
    "Reglas obligatorias:\n"
    "1. Modo imperativo SIEMPRE. Convierte cada paso reflexivo o pregunta del "
    "material en una tarea concreta con verbo, sujeto y criterio de exito. "
    "Ejemplo: el material dice '¿has validado con clientes reales?' y tu "
    "escribes 'Entrevista a 5 personas de tu publico objetivo esta semana y "
    "anota como resuelven el problema hoy'.\n"
    "2. material_principal manda la estructura y la cronologia del plan: "
    "sus conceptos, en su orden, definen las etapas. material_de_apoyo NUNCA "
    "crea etapas propias; solo enriquece las etapas ya definidas por "
    "material_principal con acciones y consideraciones adicionales, donde el "
    "concepto de apoyo sea relevante a esa etapa. Si un concepto de apoyo no "
    "encaja con claridad en ninguna etapa existente, omitelo — no fuerces su "
    "inclusion.\n"
    "3. Cada etapa termina con una linea 'Esta semana:' seguida de UNA accion "
    "ejecutable en 7 dias, concreta y especifica al proyecto de la persona.\n"
    "4. Si al menos un concepto (de material_principal o material_de_apoyo) "
    "tiene es_viabilidad_economica=true, agrega al final una seccion "
    "'## ¿Puede sostenerse tu idea? Los numeros en simple' que sintetice "
    "esos conceptos en palabras comunes, usando solo lo que esta en el "
    "material. Si NINGUNO lo tiene, NO agregues esa seccion ni inventes "
    "cifras.\n"
    "5. Prohibido cerrar el plan con preguntas para el usuario. El plan "
    "cierra con la primera accion concreta del lunes, no con una pregunta.\n"
    "6. Titulo breve especifico al proyecto (no generico), un parrafo de "
    "contexto que conecte entrada_original y perfil_sesion con lo que va a "
    "lograr.\n"
    "7. Habla siempre de la IDEA o el PROYECTO del usuario. Usa la palabra "
    "'negocio' unicamente si el analisis economico forma parte del "
    "material recibido, o si el propio usuario ya la uso en su entrada o "
    "perfil_sesion.\n"
    "8. Si recibes es_seguimiento=true, abre el plan con UNA linea (justo "
    "despues del titulo) que reconozca el avance del proyecto desde la "
    "ultima sesion, basada en estado_vivo_previo. No repitas acciones ya "
    "cubiertas antes: el material que recibes ya excluye lo cubierto en "
    "sesiones previas, asi que basta con no asumir que el usuario empieza "
    "de cero.\n\n"
    "Espanol comun, sin jerga sin explicar, sin autores, sin relleno "
    "motivacional. Todo debe salir del material recibido; no inventes "
    "tecnicas nuevas."
)

SYSTEM_ESTADO_VIVO = (
    "Comprimes el estado de un proyecto de emprendimiento en una sintesis de "
    "300 a 500 tokens que sirve como memoria para la siguiente sesion. "
    "Recibes el estado_vivo anterior (puede ser null si es la primera "
    "sesion), el perfil de sesion acumulado en la sesion que acaba de "
    "cerrar, y los titulos de los conceptos nuevos que se cubrieron. "
    "Combina todo en un solo estado_vivo nuevo: que sabemos del proyecto, "
    "que se ha validado o decidido, que sigue sin resolver. Prosa densa, "
    "sin listas, en espanol comun, sin jerga. No repitas informacion ya "
    "dicha, sintetiza. Responde SOLO el texto del estado_vivo nuevo, sin "
    "JSON, sin comillas, sin titulo."
)

SYSTEM_ORGANIZADOR = (
    "Organizas la idea de un usuario en un resumen honesto, SIN instruir. "
    "Recibes texto_usuario (su idea o situacion en texto libre) y una lista "
    "de puertas curadas del grafo (fase + titulo + resumen corto) para que "
    "sepas el mapa de temas disponible. Responde SOLO un JSON: "
    "{\"idea_en_una_frase\": str, \"etapa_detectada\": "
    "\"ideacion\"|\"validacion\"|\"planificacion\"|\"ejecucion\", "
    "\"lo_que_ya_tienes_claro\": [str, ...], "
    "\"lo_que_estas_asumiendo_sin_saberlo\": [str, ...], "
    "\"areas_que_cubriria_tu_plan_completo\": [str, ...]}.\n\n"
    "REGLA DURA: organiza y senala huecos; PROHIBIDO instruir, dar pasos, "
    "recomendar acciones o usar verbos en modo imperativo en ningun campo. "
    "'areas_que_cubriria_tu_plan_completo' son solo NOMBRES de temas (3 a "
    "6), nunca acciones, nunca el 'como' hacerlo."
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


def guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                    project_id=None, db_session_id=None, es_seguimiento=False, estado_vivo_previo=None):
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "ruta": ruta,
        "modos": modos,
        "perfil_sesion": perfil_sesion,
        "entrada_original": texto_original,
        "profundizar_ofrecido": profundizar_ofrecido,
        "project_id": project_id,
        "db_session_id": db_session_id,
        "es_seguimiento": es_seguimiento,
        "estado_vivo_previo": estado_vivo_previo,
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


def costo_acumulado_usd():
    total = 0.0
    for model, s in USO.items():
        pin, pout = PRECIOS.get(model, (0.0, 0.0))
        total += s["in"] / 1_000_000 * pin + s["out"] / 1_000_000 * pout
    return total


def llamar_claude(system, user_text, model, max_tokens=1500):
    global PRESUPUESTO_EXCEDIDO
    if costo_acumulado_usd() >= PRESUPUESTO_SESION_USD:
        if not PRESUPUESTO_EXCEDIDO:
            PRESUPUESTO_EXCEDIDO = True
            print(f"  (presupuesto de ${PRESUPUESTO_SESION_USD:.2f} alcanzado; "
                  f"el resto de la sesion corre en modo offline)")
        raise RuntimeError("presupuesto de sesion excedido")
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
    print(f"  TOTAL: ${total:.4f}" + (" (presupuesto excedido, se degrado a offline)" if PRESUPUESTO_EXCEDIDO else ""))


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


def _reparar_camino_cadena(actual_id, camino, graph, visitados):
    """Reparo 1 (cadena estricta): si un id del camino no es sucesor directo
    del anterior pero SI es sucesor de alguno de los sucesores directos de
    ese anterior (el modelo omitio el padre de nivel 1 intermedio), inserta
    ese padre automaticamente. Solo repara "hacia adelante" dentro de la
    MISMA rama que el elemento previo ya aceptado; si el modelo empezo por
    la rama equivocada, este reparo falla (ver _reparar_camino_desde_objetivo)."""
    reparado = []
    prev = actual_id
    vistos = set()
    for nid in camino:
        if nid in graph.get(prev, {}).get("nodos_siguientes", []):
            reparado.append(nid)
            vistos.add(nid)
            prev = nid
            continue
        padre = next(
            (c for c in graph.get(prev, {}).get("nodos_siguientes", [])
             if c not in visitados and c not in vistos and nid in graph.get(c, {}).get("nodos_siguientes", [])),
            None,
        )
        if padre is None:
            raise ValueError(f"{nid} no es sucesor de {prev} ni de ninguno de sus sucesores directos")
        reparado.append(padre)
        vistos.add(padre)
        reparado.append(nid)
        vistos.add(nid)
        prev = nid
    return reparado


def _reparar_camino_desde_objetivo(camino, nivel1_pool, visitados):
    """Reparo 2 (reconstruccion desde el objetivo): ignora los pasos
    intermedios que el modelo propuso (a veces atribuye un nodo de nivel 2 a
    la rama de nivel 1 equivocada, confundiendo hermanos) y reconstruye el
    camino minimo real hacia el ULTIMO id que el modelo indico, buscando su
    padre correcto en el MISMO pool de nivel1+nivel2 que se le mostro."""
    if not camino:
        raise ValueError("camino vacio")
    objetivo = camino[-1]
    if objetivo in visitados:
        raise ValueError(f"objetivo {objetivo} ya fue visitado")
    nivel1_ids = {n["id"] for n in nivel1_pool}
    if objetivo in nivel1_ids:
        return [objetivo]
    for n in nivel1_pool:
        hijos = {h["id"] for h in n.get("sucesores", [])}
        if objetivo in hijos and n["id"] not in visitados:
            return [n["id"], objetivo]
    raise ValueError(f"{objetivo} no es sucesor de nivel 1 ni de nivel 2 conocido")


def _validar_camino(actual_id, camino, graph, visitados, nivel1_pool=None):
    if not camino:
        raise ValueError("camino vacio")
    try:
        camino_reparado = _reparar_camino_cadena(actual_id, camino, graph, visitados)
        if len(camino_reparado) > MAX_SALTOS_SILENCIOSOS_POR_LLAMADA:
            raise ValueError(f"camino excede {MAX_SALTOS_SILENCIOSOS_POR_LLAMADA} nodos tras reparacion en cadena")
    except Exception:
        if nivel1_pool is None:
            raise
        camino_reparado = _reparar_camino_desde_objetivo(camino, nivel1_pool, visitados)

    prev = actual_id
    vistos_en_camino = set()
    for nid in camino_reparado:
        if nid not in graph or nid in visitados or nid in vistos_en_camino:
            raise ValueError(f"nodo invalido o repetido en camino: {nid}")
        if nid not in graph[prev].get("nodos_siguientes", []):
            raise ValueError(f"{nid} no es sucesor de {prev}")
        vistos_en_camino.add(nid)
        prev = nid
    return camino_reparado


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
            data["camino"] = _validar_camino(actual_id, camino, graph, visitados, nivel1_pool=nivel1)
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


MAX_COSECHA = 25
_STOPWORDS_COSECHA = set(
    "de la el en y a los las que para con su sus un una como al del por se es "
    "son o u e no ya mas tu tus este esta estos estas".split()
)


def _tokens_cosecha(texto):
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    ascii_txt = "".join(c for c in nfkd if not unicodedata.combining(c))
    return set(w for w in re.findall(r"[a-z0-9]+", ascii_txt) if w not in _STOPWORDS_COSECHA and len(w) > 2)


def cosechar_vecindario(ruta, graph, families, evaluacion, perfil_sesion, tope=MAX_COSECHA):
    """Expande desde la ruta (conversada + silenciosa) hacia nodos_siguientes y
    nodos_previos adyacentes, sin preguntar nada, y devuelve hasta `tope`
    priorizados por: familia que le falte a la ruta, fase mayoritaria de la
    ruta, y afinidad de palabras clave con el perfil_sesion."""
    ruta_set = set(ruta)
    candidatos = set()
    for nid in ruta:
        n = graph[nid]
        for vecino in n.get("nodos_siguientes", []) + n.get("nodos_previos", []):
            if vecino in graph and vecino not in ruta_set:
                candidatos.add(vecino)

    fases_ruta = [graph[nid].get("fase_proyecto") for nid in ruta if nid in graph]
    fase_mayoritaria = max(set(fases_ruta), key=fases_ruta.count) if fases_ruta else None

    familias_faltantes = set()
    if not evaluacion["tiene_accion_clientes"]:
        familias_faltantes.add("accion_clientes")
    if not evaluacion["tiene_viabilidad_economica"]:
        familias_faltantes.add("viabilidad_economica")

    perfil_tokens = _tokens_cosecha(perfil_sesion) if perfil_sesion else set()

    def puntaje(nid):
        n = graph[nid]
        p = 0
        if families.get(nid) in familias_faltantes:
            p += 10
        if n.get("fase_proyecto") == fase_mayoritaria:
            p += 3
        if perfil_tokens:
            texto_nodo = n.get("titulo_concepto", "") + " " + " ".join(n.get("condiciones_activacion", []))
            p += len(perfil_tokens & _tokens_cosecha(texto_nodo))
        return p

    return sorted(candidatos, key=puntaje, reverse=True)[:tope]


def ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion, session_id,
                    es_seguimiento=False, estado_vivo_previo=None):
    """`evaluacion` (ruta-solo) decide QUE cosechar (familia faltante como
    prioridad). La etiqueta inicial/completo y la seccion "no cubre" se
    recalculan sobre ruta+cosecha, porque eso es lo que el plan realmente
    contiene: si la cosecha trajo la familia que la ruta no toco, el plan
    ya la cubre y no puede declarar lo contrario. Devuelve un dict con el
    markdown y los metadatos de cosecha/cobertura, para persistencia."""
    def a_material(nid):
        n = graph[nid]
        return {
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
            "es_viabilidad_economica": families.get(nid) == "viabilidad_economica",
        }

    material_principal = [a_material(nid) for nid in ruta]
    cosecha_ids = cosechar_vecindario(ruta, graph, families, evaluacion, perfil_sesion)
    material_de_apoyo = [a_material(nid) for nid in cosecha_ids]
    evaluacion_cobertura = plan_readiness.evaluar_ruta(ruta + cosecha_ids, families)

    if API_KEY:
        payload = {
            "entrada_original": texto_original,
            "perfil_sesion": perfil_sesion,
            "material_principal": material_principal,
            "material_de_apoyo": material_de_apoyo,
        }
        if es_seguimiento:
            payload["es_seguimiento"] = True
            payload["estado_vivo_previo"] = estado_vivo_previo
        try:
            cuerpo = llamar_claude(SYSTEM_PLAN, json.dumps(payload, ensure_ascii=False), MODEL, max_tokens=8192)
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
            cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)
    else:
        cuerpo = _ensamblar_offline(material_principal, perfil_sesion, texto_original)

    etiqueta = "Plan completo" if evaluacion_cobertura["es_completa"] else "Plan inicial"
    total_conceptos = len(ruta) + len(cosecha_ids)
    partes = [f"_{etiqueta}_", "", cuerpo]
    partes += ["", "---", f"_Este plan se alimento de {total_conceptos} conceptos: "
                          f"{len(ruta)} de tu recorrido conversado y {len(cosecha_ids)} "
                          f"del vecindario relacionado del grafo._"]
    if not evaluacion_cobertura["es_completa"]:
        partes += ["", "## Lo que este plan aun no cubre", ""]
        for f in evaluacion_cobertura["familias_faltantes"]:
            partes.append(f"- {f}")
        partes += ["", f"Para profundizar, continua la sesion: "
                        f"`python engine/prototipo_motor.py --continuar {session_id}`"]
    return {
        "markdown": "\n".join(partes),
        "cosecha_ids": cosecha_ids,
        "evaluacion_cobertura": evaluacion_cobertura,
    }


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


def comprimir_estado_vivo(estado_anterior, perfil_sesion_nueva, conceptos_nuevos_titulos):
    """Comprime estado_anterior + novedades de la sesion en un estado_vivo
    nuevo de 300-500 tokens. Respaldo offline: concatena sin comprimir."""
    if API_KEY:
        ctx = {
            "estado_vivo_anterior": estado_anterior,
            "perfil_actualizado_esta_sesion": perfil_sesion_nueva,
            "conceptos_nuevos_cubiertos": conceptos_nuevos_titulos,
        }
        try:
            return llamar_claude(SYSTEM_ESTADO_VIVO, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=700).strip()
        except Exception as e:
            print(f"  (fallo comprimir estado_vivo, uso respaldo sin comprimir: {e})")
    return (estado_anterior + "\n" + perfil_sesion_nueva).strip() if estado_anterior else perfil_sesion_nueva


def organizador_gratuito(texto_original, entry_seeds, graph):
    """Capa gratuita: UNA llamada Haiku que organiza sin instruir.
    Devuelve (markdown, data_dict) o (None, mensaje_error)."""
    puertas = [
        {"id": s, "fase": graph[s]["fase_proyecto"], "titulo": graph[s]["titulo_concepto"],
         "resumen": graph[s]["resumen_teorico"][:150]}
        for s in entry_seeds
    ]
    ctx = {"texto_usuario": texto_original, "puertas": puertas}
    try:
        raw = llamar_claude(SYSTEM_ORGANIZADOR, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=600)
        data = _parsear_json(raw)
    except Exception as e:
        return None, f"  (fallo el organizador con IA: {e})"

    out = [
        "# Organizador de tu idea", "",
        f"**En una frase:** {data.get('idea_en_una_frase', '')}", "",
        f"**Etapa detectada:** {data.get('etapa_detectada', '')}", "",
        "## Lo que ya tienes claro",
    ]
    for b in data.get("lo_que_ya_tienes_claro", []) or []:
        out.append(f"- {b}")
    out += ["", "## Lo que estás asumiendo sin saberlo"]
    for b in data.get("lo_que_estas_asumiendo_sin_saberlo", []) or []:
        out.append(f"- {b}")
    out += ["", "## Áreas que cubriría tu plan completo"]
    for b in data.get("areas_que_cubriria_tu_plan_completo", []) or []:
        out.append(f"- {b}")
    return "\n".join(out), data


def candidatos_seguimiento(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos, tope=30):
    """Candidatos de CUALQUIER parte del grafo (no solo las 20 puertas) que el
    proyecto aun no cubrio, priorizados por fase, familia sin cubrir y
    afinidad de palabras clave con el mensaje nuevo + estado_vivo."""
    orden = {"ideacion": 0, "validacion": 1, "planificacion": 2, "ejecucion": 3}
    fase_idx = orden.get(fase_actual, 0)
    conteo_fam = {}
    for nid in cubiertos:
        f = families.get(nid, "general")
        conteo_fam[f] = conteo_fam.get(f, 0) + 1
    contexto_tokens = _tokens_cosecha((mensaje_nuevo or "") + " " + (estado_vivo or ""))

    def puntaje(nid):
        n = graph[nid]
        p = 0
        f_nodo = orden.get(n.get("fase_proyecto"), 0)
        if f_nodo == fase_idx:
            p += 5
        elif f_nodo == fase_idx + 1:
            p += 3
        fam = families.get(nid, "general")
        if fam != "general" and conteo_fam.get(fam, 0) == 0:
            p += 6
        if contexto_tokens:
            texto_nodo = n.get("titulo_concepto", "") + " " + " ".join(n.get("condiciones_activacion", []))
            p += len(contexto_tokens & _tokens_cosecha(texto_nodo))
        return p

    candidatos = [nid for nid in graph if nid not in cubiertos]
    return sorted(candidatos, key=puntaje, reverse=True)[:tope]


def seleccionar_puerta_avanzada(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos, entry_seeds):
    """Capa 1 avanzada (--seguir): elige cualquier nodo del grafo aun no
    cubierto como punto de entrada de la sesion de seguimiento."""
    candidatos_ids = candidatos_seguimiento(mensaje_nuevo, estado_vivo, fase_actual, families, graph, cubiertos)
    if API_KEY and candidatos_ids:
        opciones = []
        for nid in candidatos_ids:
            n = graph[nid]
            opciones.append({
                "id": nid, "titulo": n["titulo_concepto"], "fase": n.get("fase_proyecto"),
                "resumen": n.get("resumen_teorico", "")[:150],
                "condiciones_activacion": n.get("condiciones_activacion", [])[:2],
            })
        ctx = {"estado_vivo": estado_vivo, "mensaje_nuevo": mensaje_nuevo, "candidatos": opciones}
        try:
            raw = llamar_claude(SYSTEM_PUERTA_AVANZADA, json.dumps(ctx, ensure_ascii=False), MODEL_HAIKU, max_tokens=400)
            data = _parsear_json(raw)
            if data["puerta_id"] in candidatos_ids:
                return data["puerta_id"], (data.get("perfil_sesion") or "").strip()
            raise ValueError(f"puerta_id fuera de los candidatos: {data.get('puerta_id')}")
        except Exception as e:
            print(f"  (fallo la clasificacion avanzada, uso el candidato de mayor puntaje: {e})")
    if candidatos_ids:
        return candidatos_ids[0], (estado_vivo or "")
    return next(iter(entry_seeds)), (estado_vivo or "")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--continuar", metavar="SESSION_ID", default=None,
                    help="Retoma una sesion previa desde su ultimo nodo (engine/sessions/{id}.json)")
    ap.add_argument("--gratis", action="store_true",
                    help="Organizador gratuito: una sola llamada, sin entrevista")
    ap.add_argument("--seguir", metavar="PROJECT_ID", default=None,
                    help="Sesion de seguimiento de un proyecto existente")
    ap.add_argument("--offline", action="store_true",
                    help="Fuerza persistencia JSON local en engine/projects_local/ en vez de Supabase")
    return ap.parse_args()


def _imprimir_nodo(idx, total, node, modo, con_resumen=False):
    etiqueta = f"[{modo}]"
    print("\n" + "-" * 60)
    print(f"[{idx}/{total}] {etiqueta} {node['titulo_concepto']}")
    if con_resumen:
        print(textwrap.fill(node["resumen_teorico"], 76)[:600])
    else:
        print("  (cubierto por lo que ya contaste; no hace falta preguntarlo)")


def _extraer_titulo(plan_md):
    for line in plan_md.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None


def ejecutar_recorrido(graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
                       perfil_sesion, texto_original, session_id, project_id, db_session_id,
                       profundizar_ofrecido=False, pregunta_hecha=None, respuesta_usuario=None,
                       es_seguimiento=False, estado_vivo_previo=None):
    """Corre el bucle de entrevista (comun a proyecto nuevo y --seguir) hasta
    salir sin plan o ensamblar uno. Devuelve un dict con el resultado."""
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
            return {"tipo": "salio", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion}

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
                guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                               project_id, db_session_id, es_seguimiento, estado_vivo_previo)
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
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                       project_id, db_session_id, es_seguimiento, estado_vivo_previo)

        if pregunta_necesaria:
            n = graph[actual_id]
            _imprimir_nodo(len(ruta), MAX_DEPTH, n, "conversado", con_resumen=True)
            pregunta_hecha = obtener_pregunta(actual_id, n, preguntas_cache)
            respuesta_usuario = input("\n" + pregunta_hecha + "\n> ")
        else:
            pregunta_hecha, respuesta_usuario = None, None

    evaluacion = plan_readiness.evaluar_ruta(ruta, families)
    print("\nEnsamblando tu plan...\n")
    resultado_plan = ensamblar_plan(ruta, graph, perfil_sesion, texto_original, families, evaluacion,
                                     session_id, es_seguimiento=es_seguimiento,
                                     estado_vivo_previo=estado_vivo_previo)
    plan_md = resultado_plan["markdown"]
    print(plan_md)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan_md, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    ruta_txt = " -> ".join(f"[{m[0]}]{nid}" for nid, m in zip(ruta, modos))
    print(f"Ruta recorrida ({len(ruta)}): {ruta_txt}")

    return {
        "tipo": "plan", "ruta": ruta, "modos": modos, "perfil_sesion": perfil_sesion,
        "cosecha_ids": resultado_plan["cosecha_ids"],
        "evaluacion_cobertura": resultado_plan["evaluacion_cobertura"],
        "plan_md": plan_md, "plan_fname": fname,
    }


def _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=False):
    """Escribe en Supabase (o JSON local) el resultado de una sesion: nodos
    cubiertos, cierre de sesion, plan, y el estado_vivo comprimido."""
    if project_id is None or db_session_id is None:
        return  # --continuar de un scratch file anterior sin project_id: nada que persistir

    ruta = resultado["ruta"]
    modos = resultado["modos"]

    if resultado["tipo"] == "salio":
        db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO)
        return

    cosecha_ids = resultado["cosecha_ids"]
    evaluacion_cobertura = resultado["evaluacion_cobertura"]

    nodos_con_tipo = list(zip(ruta, modos)) + [(nid, "cosechado") for nid in cosecha_ids]
    db.registrar_nodos(project_id, db_session_id, nodos_con_tipo)

    ruta_con_modos_json = [{"node_id": nid, "tipo": modo} for nid, modo in zip(ruta, modos)]
    db.cerrar_sesion(project_id, db_session_id, ruta_con_modos_json, costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO)

    etiqueta_db = "seguimiento" if es_seguimiento else ("completo" if evaluacion_cobertura["es_completa"] else "inicial")
    total_conceptos = len(ruta) + len(cosecha_ids)
    familias_presentes = sorted({families.get(nid, "general") for nid in ruta + cosecha_ids} - {"general"})
    db.guardar_plan(project_id, db_session_id, etiqueta_db, resultado["plan_md"], total_conceptos, familias_presentes)

    proyecto = db.obtener_proyecto(project_id)
    estado_anterior = proyecto.get("estado_vivo") if proyecto else None
    conceptos_titulos = [graph[nid]["titulo_concepto"] for nid in ruta + cosecha_ids if nid in graph]
    estado_nuevo = comprimir_estado_vivo(estado_anterior, resultado["perfil_sesion"], conceptos_titulos)

    fase_final = graph[ruta[-1]].get("fase_proyecto", "ideacion") if ruta else "ideacion"
    campos = {"estado_vivo": estado_nuevo, "fase_actual": fase_final}
    titulo = _extraer_titulo(resultado["plan_md"])
    if titulo and (not proyecto or not proyecto.get("titulo")):
        campos["titulo"] = titulo
    db.actualizar_proyecto(project_id, **campos)


def modo_nuevo_proyecto(graph, families, entry_seeds, preguntas_cache, args):
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
        project_id = sesion.get("project_id")
        db_session_id = sesion.get("db_session_id")
        es_seguimiento = sesion.get("es_seguimiento", False)
        estado_vivo_previo = sesion.get("estado_vivo_previo")
        print(f"\nRetomando sesion {session_id} desde: {graph[actual_id]['titulo_concepto']}")
    else:
        session_id = uuid.uuid4().hex[:8]
        texto_original = input("\nCuéntame tu idea, o en qué punto estás con ella:\n> ")
        project_id = db.crear_proyecto(texto_original)
        db_session_id = db.crear_sesion(project_id, "inicial", texto_original)
        actual_id, perfil_sesion = clasificar_entrada(texto_original, entry_seeds, graph)
        visitados, ruta, modos = {actual_id}, [actual_id], ["conversado"]
        profundizar_ofrecido = False
        es_seguimiento, estado_vivo_previo = False, None
        guardar_sesion(session_id, ruta, modos, perfil_sesion, texto_original, profundizar_ofrecido,
                       project_id, db_session_id)
        _imprimir_nodo(1, MAX_DEPTH, graph[actual_id], "puerta de entrada", con_resumen=True)
        print(f"\n(proyecto: {project_id})")

    resultado = ejecutar_recorrido(
        graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
        perfil_sesion, texto_original, session_id, project_id, db_session_id,
        profundizar_ofrecido, pregunta_hecha, respuesta_usuario,
        es_seguimiento=es_seguimiento, estado_vivo_previo=estado_vivo_previo,
    )
    _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=es_seguimiento)
    if project_id:
        print(f"\nPara continuar mas adelante: python engine/prototipo_motor.py --seguir {project_id}")
    reportar_costo()


def modo_seguir(project_id, graph, families, entry_seeds, preguntas_cache):
    proyecto = db.obtener_proyecto(project_id)
    if proyecto is None:
        print(f"ERROR: no existe el proyecto {project_id}")
        sys.exit(1)

    cubiertos = db.nodos_cubiertos(project_id)
    print(f"\nRetomando proyecto {project_id} (fase actual: {proyecto.get('fase_actual')}, "
          f"{len(cubiertos)} conceptos ya cubiertos).")
    mensaje_nuevo = input("\nCuéntame qué ha pasado desde la última vez:\n> ")

    db_session_id = db.crear_sesion(project_id, "seguimiento", mensaje_nuevo)
    estado_vivo_previo = proyecto.get("estado_vivo")

    actual_id, perfil_sesion = seleccionar_puerta_avanzada(
        mensaje_nuevo, estado_vivo_previo, proyecto.get("fase_actual", "ideacion"),
        families, graph, cubiertos, entry_seeds,
    )
    visitados = set(cubiertos) | {actual_id}
    ruta, modos = [actual_id], ["conversado"]
    session_id = uuid.uuid4().hex[:8]
    guardar_sesion(session_id, ruta, modos, perfil_sesion, mensaje_nuevo, False, project_id, db_session_id,
                   es_seguimiento=True, estado_vivo_previo=estado_vivo_previo)
    _imprimir_nodo(1, MAX_DEPTH, graph[actual_id], "puerta de seguimiento", con_resumen=True)

    resultado = ejecutar_recorrido(
        graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
        perfil_sesion, mensaje_nuevo, session_id, project_id, db_session_id,
        profundizar_ofrecido=False, es_seguimiento=True, estado_vivo_previo=estado_vivo_previo,
    )
    _persistir_resultado(project_id, db_session_id, resultado, graph, families, es_seguimiento=True)
    reportar_costo()


def modo_gratis(graph, entry_seeds):
    print("\n--- Modo gratuito: organizador de tu idea (sin entrevista) ---")
    texto_original = input("\nCuéntame tu idea, o en qué punto estás con ella:\n> ")
    project_id = db.crear_proyecto(texto_original)
    db_session_id = db.crear_sesion(project_id, "gratuito", texto_original)

    markdown, data = organizador_gratuito(texto_original, entry_seeds, graph)
    if markdown is None:
        print(data)
        reportar_costo()
        return

    print("\n" + markdown)
    fname = BASE / f"plan_gratis_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(markdown, encoding="utf-8")
    print(f"\nGuardado en: {fname}")

    db.guardar_plan(project_id, db_session_id, "organizador", markdown, 0, [])
    db.cerrar_sesion(project_id, db_session_id, [], costo_acumulado_usd(), PRESUPUESTO_EXCEDIDO)
    if isinstance(data, dict) and data.get("etapa_detectada") in db.FASES:
        db.actualizar_proyecto(project_id, fase_actual=data["etapa_detectada"])

    print(f"\nProyecto: {project_id}")
    print(f"Para continuar mas adelante: python engine/prototipo_motor.py --seguir {project_id}")
    reportar_costo()


def main():
    args = parse_args()
    if args.offline:
        db.forzar_offline(True)

    graph = cargar_grafo()
    entry_seeds = cargar_entry_seeds()
    preguntas_cache = cargar_preguntas_cache()
    families = plan_readiness.cargar_families(graph)

    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo (travesia silenciosa)")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'} | "
          f"preguntas cacheadas: {len(preguntas_cache)} | persistencia: "
          f"{'Supabase' if db.disponible() else 'JSON local'}")
    print("=" * 60)

    if args.gratis:
        modo_gratis(graph, entry_seeds)
        return
    if args.seguir:
        modo_seguir(args.seguir, graph, families, entry_seeds, preguntas_cache)
        return
    modo_nuevo_proyecto(graph, families, entry_seeds, preguntas_cache, args)


if __name__ == "__main__":
    main()
