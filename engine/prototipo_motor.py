# -*- coding: utf-8 -*-
"""
prototipo_motor.py - Prototipo CLI del motor de ruteo (Fase 2)

Flujo: cuestionario raiz (2 preguntas) -> puerta de entrada -> recorrido guiado
por el grafo -> ensamblado del plan final ("receta de cafe").

Dos modos:
  - CON ANTHROPIC_API_KEY: Claude genera la pregunta de cada paso en lenguaje
    natural y redacta el plan final en una sola voz clara.
  - SIN API key (modo offline): menus numerados usando condiciones_activacion
    como pista, y plan final ensamblado estructuralmente. Sirve para probar la
    topologia y la experiencia sin gastar tokens.

Uso:  python3 engine/prototipo_motor.py
Guardrails: profundidad maxima 15, sin ciclos (nodos visitados no se reofrecen),
opcion permanente [P] generar plan / [Q] salir.
"""
import json
import os
import sys
import textwrap
from datetime import datetime
from pathlib import Path

# En consolas de Windows, stdout suele quedar en cp1252 (o el codepage local),
# que no puede representar caracteres como flechas (->) o comillas tipograficas
# presentes en el contenido de algunos nodos. Sin esto, print() lanza
# UnicodeEncodeError y el programa se cae a mitad de un recorrido.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent.parent
GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
QUIZ_PATH = BASE / "engine" / "cuestionario_raiz.json"
MAX_DEPTH = 15
MAX_OPCIONES = 6

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
MODEL = "claude-sonnet-4-6"

SYSTEM_RUTEO = (
    "Eres el guia de una app que convierte conocimiento de emprendimiento en un "
    "camino personalizado. Recibes el concepto actual que el usuario acaba de ver "
    "y una lista de conceptos siguientes posibles con sus condiciones de activacion. "
    "Tu trabajo: formular UNA sola pregunta breve y calida en espanol comun (sin "
    "jerga, sin mencionar autores ni libros ni la palabra 'nodo') cuyas opciones de "
    "respuesta correspondan exactamente, en orden, a los conceptos siguientes dados. "
    "Responde SOLO un JSON: {\"pregunta\": str, \"opciones\": [str, ...]} con tantas "
    "opciones como conceptos recibiste, cada una de maximo 15 palabras, en segunda "
    "persona, orientada a la situacion del usuario y no al titulo teorico."
)

SYSTEM_PLAN = (
    "Eres el redactor final de una app de emprendimiento. Recibes, en orden, los "
    "conceptos que una persona recorrio, cada uno con pasos accionables y un "
    "entregable esperado. Redacta un plan de accion en espanol comun, claro y "
    "poderoso, como un project manager excelente que habla simple: titulo breve, "
    "un parrafo de contexto (que va a lograr la persona), y una secuencia numerada "
    "de pasos concretos agrupados por etapas, con el entregable de cada etapa como "
    "punto de control. Sin jerga sin explicar, sin autores, sin relleno motivacional. "
    "Todo lo que escribas debe salir del material recibido; no inventes tecnicas nuevas."
)


def cargar():
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]
    quiz = json.load(open(QUIZ_PATH, encoding="utf-8"))
    return graph, quiz


def preguntar_opcion(texto, opciones, extra=""):
    """Menu numerado. Devuelve indice elegido, o 'P'/'Q' si extra los permite."""
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


def llamar_claude(system, user_text):
    import anthropic
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL, max_tokens=1500,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_text}],
    )
    return "".join(b.text for b in msg.content if b.type == "text")


def pregunta_paso(actual, candidatos, graph):
    """Genera la pregunta del paso. Devuelve (texto_pregunta, [textos_opciones])."""
    if API_KEY:
        ctx = {
            "concepto_actual": {
                "titulo": actual["titulo_concepto"],
                "resumen": actual["resumen_teorico"][:400],
            },
            "conceptos_siguientes": [
                {"titulo": graph[c]["titulo_concepto"],
                 "condiciones_activacion": graph[c].get("condiciones_activacion", [])[:3]}
                for c in candidatos
            ],
        }
        try:
            raw = llamar_claude(SYSTEM_RUTEO, json.dumps(ctx, ensure_ascii=False))
            data = json.loads(raw.strip().removeprefix("```json").removesuffix("```").strip())
            if len(data["opciones"]) == len(candidatos):
                return data["pregunta"], data["opciones"]
        except Exception as e:
            print(f"  (fallo la generacion con IA, uso modo offline: {e})")
    # Offline: titulo + primera condicion de activacion como pista
    ops = []
    for c in candidatos:
        n = graph[c]
        cond = (n.get("condiciones_activacion") or [""])[0]
        pista = f"  <- si: {cond[:70]}" if cond else ""
        ops.append(f"{n['titulo_concepto']}{pista}")
    return "¿Hacia dónde seguimos?", ops


def ensamblar_plan(ruta, graph):
    material = []
    for nid in ruta:
        n = graph[nid]
        material.append({
            "concepto": n["titulo_concepto"],
            "pasos": n.get("pasos_accionables", []),
            "entregable": n.get("entregable_esperado", ""),
        })
    if API_KEY:
        try:
            return llamar_claude(SYSTEM_PLAN, json.dumps(material, ensure_ascii=False))
        except Exception as e:
            print(f"  (fallo el redactor con IA, ensamblo offline: {e})")
    # Offline: ensamblado estructural
    out = ["# Tu plan de accion", ""]
    for i, m in enumerate(material, 1):
        out.append(f"## Etapa {i}: {m['concepto']}")
        for j, p in enumerate(m["pasos"], 1):
            out.append(f"  {i}.{j} {p}")
        if m["entregable"]:
            out.append(f"  Punto de control: {m['entregable']}")
        out.append("")
    return "\n".join(out)


def main():
    graph, quiz = cargar()
    print("=" * 60)
    print("  MY IDEA - prototipo del motor de ruteo")
    print(f"  Grafo: {len(graph)} conceptos | modo: {'IA' if API_KEY else 'offline'}")
    print("=" * 60)

    # Cuestionario raiz
    pf = quiz["pregunta_fase"]
    i = preguntar_opcion(pf["texto"], [o["texto"] for o in pf["opciones"]])
    fase = pf["opciones"][i]["fase"]
    pp = quiz["pregunta_puerta"][fase]
    i = preguntar_opcion(pp["texto"], [o["texto"] for o in pp["opciones"]])
    actual_id = pp["opciones"][i]["nodo"]

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
        texto, ops = pregunta_paso(n, candidatos, graph)
        r = preguntar_opcion(texto, ops, extra="P. Generar mi plan ahora   Q. Salir sin plan")
        if r == "Q":
            print("Hasta pronto."); return
        if r == "P":
            break
        actual_id = candidatos[r]
        visitados.add(actual_id); ruta.append(actual_id)

    print("\nEnsamblando tu plan...\n")
    plan = ensamblar_plan(ruta, graph)
    print(plan)
    fname = BASE / f"plan_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    fname.write_text(plan, encoding="utf-8")
    print(f"\nPlan guardado en: {fname}")
    print(f"Ruta recorrida ({len(ruta)}): {' -> '.join(ruta)}")


if __name__ == "__main__":
    main()
