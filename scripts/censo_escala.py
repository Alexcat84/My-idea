#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""censo_escala.py - Clasifica cada nodo ACTIVO contra la definicion de ESCALA.

ESTRICTAMENTE DE SOLO LECTURA sobre el catalogo. No escribe ni un campo de
ningun nodo, no toca la puerta, no toca el motor, no toca la web. Lo unico que
produce es su propio registro en packs/_core/poda/_censo_escala.jsonl y el
documento docs/CENSO_ESCALA.md.

LA DEFINICION, fijada antes del censo y no negociable durante el:

  Un nodo es de ESCALA CORPORATIVA si sus pasos_accionables son IMPOSIBLES sin
  al menos una de estas tres cosas:
    (a) personas a quienes delegar,
    (b) funciones o areas separadas,
    (c) una autoridad formal por encima del lector.
  Si los pasos se pueden hacer estando SOLO, el nodo es UNIVERSAL, aunque hable
  de empresas, mencione departamentos o cite una norma industrial.

  DECIDEN LOS PASOS. No decide el titulo, no decide el vocabulario, no decide la
  fuente, no deciden las condiciones_activacion.

POR QUE NO ES UNA EXPRESION REGULAR. La casa ya adjudico tres veces que se
detecta por lo que el nodo DESCRIBE, no por la cadena que menciona: la sigla de
OSHA en un nodo que dice "o el organismo equivalente en tu mercado", el comite
que se nombra para decir que no lo hay, el "equipo de proteccion personal" que
no es un equipo de trabajo. Un patron mide la palabra; aqui hay que medir la
posibilidad, y eso lo hace un lector.

EL REGISTRO ES INCREMENTAL, una linea por nodo. Un lote de 3.521 no cabe en una
ventana, y una corrida cortada que pierde la cuenta paga la API dos veces por el
mismo trabajo (aprendido dos veces en el ciclo de la curacion).

Uso:
  python scripts/censo_escala.py --tanda 400      # sigue donde quedo
  python scripts/censo_escala.py --reporte        # escribe el .md, sin API
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import libro_mayor  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
NODOS = BASE / "dataset" / "nodos"
REGISTRO = BASE / "packs" / "_core" / "poda" / "_censo_escala.jsonl"
REPORTE = BASE / "docs" / "CENSO_ESCALA.md"
MODEL = "claude-sonnet-5"
TECHOS = (16000, 32000, 64000)
PRECIO_IN, PRECIO_OUT = 2.00, 10.00
POR_LLAMADA = 25

SYSTEM = """Eres un lector que clasifica nodos de un catalogo de conocimiento
para emprendedores. Tu unico trabajo es decidir si cada nodo se puede EJECUTAR
ESTANDO SOLO.

LA DEFINICION, y no admite matices:

Un nodo es de ESCALA CORPORATIVA (C) si sus pasos_accionables son IMPOSIBLES sin
al menos una de estas tres cosas:
  (a) personas a quienes delegar,
  (b) funciones o areas separadas,
  (c) una autoridad formal por encima del lector.

Si los pasos se pueden hacer estando SOLO, el nodo es UNIVERSAL (U), AUNQUE
hable de empresas, mencione departamentos, cite una norma industrial o use
vocabulario corporativo.

DECIDEN LOS PASOS. No decide el titulo, no decide el vocabulario, no decide la
fuente. La pregunta unica es: una persona sola, con un telefono y su negocio,
¿puede HACER estos pasos?

EJEMPLOS DE LA FRONTERA:
- "Reune a los representantes de cada area" -> C, condicion (b): sin areas
  separadas no hay a quien reunir.
- "Define quien aprueba cada cambio" -> U: estando solo, lo apruebas tu, y el
  paso sigue teniendo sentido.
- "Presenta el caso al comite de direccion" -> C, condicion (c).
- "Capacita a las personas que trabajan contigo" -> C, condicion (a): sin nadie
  a quien capacitar el paso no se puede hacer.
- "Documenta tu procedimiento de calidad" -> U, aunque el titulo diga ISO.
- "Negocia la tarifa con el proveedor" -> U.
- "Delega el seguimiento diario" -> C, condicion (a).

MARCA DUDOSO (D) cuando la lectura sea defendible en las DOS direcciones. Se
prefieren veinte dudosos honestos a cero dudosos y tres errores escondidos. NO
fuerces un veredicto para evitar la D.

Devuelve EXCLUSIVAMENTE un arreglo JSON, sin markdown, un objeto por nodo, EN EL
MISMO ORDEN y con TODOS los nodos recibidos:
  {"id": "...", "v": "U"}
  {"id": "...", "v": "C", "cond": "a", "paso": "el paso textual que no se puede
   hacer solo", "razon": "una linea"}
  {"id": "...", "v": "D", "cond": "b", "paso": "...", "razon": "por que es
   defendible en las dos direcciones"}
El campo "cond" es una sola letra: a, b o c."""


def _texto(r):
    for b in r.content:
        if getattr(b, "type", "") == "text":
            return b.text
    return ""


def _arreglo(t):
    t = t.strip()
    for v in ("```json", "```"):
        if t.startswith(v):
            t = t[len(v):]
    if t.endswith("```"):
        t = t[:-3]
    i, j = t.find("["), t.rfind("]")
    return t[i:j + 1] if i != -1 and j > i else t


def llamar(cli, prompt, uso):
    ultimo = None
    for techo in TECHOS:
        for intento in range(3):
            try:
                with cli.messages.stream(model=MODEL, max_tokens=techo, system=SYSTEM,
                                         messages=[{"role": "user", "content": prompt}]) as s:
                    r = s.get_final_message()
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                if r.stop_reason == "max_tokens":
                    ultimo = "cortada"
                    break
                return json.loads(_arreglo(_texto(r))), None
            except json.JSONDecodeError as e:
                ultimo = f"JSON invalido: {e}"
            except Exception as e:
                ultimo = str(e)
                time.sleep(5 * (intento + 1))
    return None, ultimo or "fallo"


def cargar_activos():
    out = {}
    for p in sorted(NODOS.glob("*.json")):
        n = json.loads(p.read_text(encoding="utf-8"))
        if not n.get("deprecado"):
            out[n["node_id"]] = n
    return out


def ya_juzgados():
    if not REGISTRO.exists():
        return {}
    d = {}
    for linea in REGISTRO.read_text(encoding="utf-8").splitlines():
        if linea.strip():
            x = json.loads(linea)
            d[x["id"]] = x
    return d


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tanda", type=int, default=400)
    ap.add_argument("--reporte", action="store_true", help="solo escribe el .md")
    args = ap.parse_args()

    activos = cargar_activos()
    hechos = ya_juzgados()
    print(f"  activos: {len(activos)} | ya juzgados: {len(hechos)}")
    if args.reporte:
        escribir_reporte(activos, hechos)
        return 0

    pendientes = [n for n in activos if n not in hechos][:args.tanda]
    if not pendientes:
        print("  nada pendiente. Corre con --reporte.")
        return 0

    from dotenv import load_dotenv
    import anthropic
    load_dotenv(BASE / ".env")
    cli = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    uso = {"in": 0, "out": 0}

    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    for k in range(0, len(pendientes), POR_LLAMADA):
        trozo = pendientes[k:k + POR_LLAMADA]
        bloques = []
        for nid in trozo:
            n = activos[nid]
            bloques.append(json.dumps({
                "id": nid,
                "titulo": n.get("titulo_concepto"),
                "pasos_accionables": n.get("pasos_accionables") or [],
                "entregable_esperado": n.get("entregable_esperado") or "",
            }, ensure_ascii=False))
        datos, err = llamar(cli, "\n".join(bloques), uso)
        if err or not isinstance(datos, list):
            print(f"    [fallo] {err}")
            continue
        por_id = {d.get("id"): d for d in datos if isinstance(d, dict)}
        with open(REGISTRO, "a", encoding="utf-8") as fh:
            for nid in trozo:
                d = por_id.get(nid)
                if not d or d.get("v") not in ("U", "C", "D"):
                    continue
                d["dominio"] = activos[nid].get("dominio", "core")
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        print(f"    [{k + len(trozo)}/{len(pendientes)}] {len(por_id)} juzgados")

    costo = uso["in"] / 1e6 * PRECIO_IN + uso["out"] / 1e6 * PRECIO_OUT
    libro_mayor.anotar(None, "censo-de-escala", costo, nodos=len(pendientes), tokens=uso)
    print(f"  Costo de la tanda: ${costo:.2f}")
    print(f"  Total juzgados: {len(ya_juzgados())}/{len(activos)}")
    return 0


def escribir_reporte(activos, hechos):
    import collections
    U = [x for x in hechos.values() if x["v"] == "U"]
    C = [x for x in hechos.values() if x["v"] == "C"]
    D = [x for x in hechos.values() if x["v"] == "D"]

    # (5) semillas corporativas
    seeds = set()
    for p in [BASE / "dataset" / "metadata" / "entry_seeds.json"] + \
             list((BASE / "packs").glob("*/metadata/entry_seeds.json")):
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            seeds |= set(d["seeds"] if isinstance(d, dict) else d)
    semillas_corp = [x for x in C if x["id"] in seeds]

    # (6) simulacro de encierro: quien queda inalcanzable si los C no se ofrecen
    grafo = json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    apagados = {x["id"] for x in C}
    ofrecible = {k for k, n in grafo.items() if not n.get("deprecado")} - apagados
    alcanzables, frente = set(), [s for s in seeds if s in ofrecible]
    alcanzables.update(frente)
    while frente:
        nid = frente.pop()
        for s in (grafo.get(nid, {}).get("nodos_siguientes") or []):
            if s in ofrecible and s not in alcanzables:
                alcanzables.add(s)
                frente.append(s)
    huerfanos = sorted((ofrecible - alcanzables))
    # de esos, cuales son UNIVERSALES juzgados
    univ = {x["id"] for x in U}
    huerfanos_u = [h for h in huerfanos if h in univ]
    # por que camino colgaban: un padre apagado que los alcanzaba
    def padre_apagado(h):
        for k in apagados:
            if h in (grafo.get(k, {}).get("nodos_siguientes") or []):
                return k
        return None

    L = ["# Censo de escala corporativa (SOLO LECTURA)", "",
         "Clasificacion de los nodos ACTIVOS contra la definicion fijada antes del censo.",
         "**Cero campos escritos, cero puertas tocadas, cero motor.** Esto es una lista "
         "para adjudicar.", "",
         "## La definicion aplicada", "",
         "> Un nodo es de ESCALA CORPORATIVA si sus `pasos_accionables` son IMPOSIBLES sin "
         "al menos una de estas tres cosas: **(a)** personas a quienes delegar, **(b)** "
         "funciones o areas separadas, **(c)** una autoridad formal por encima del lector. "
         "Si los pasos se pueden hacer estando SOLO, el nodo es UNIVERSAL, aunque hable de "
         "empresas, mencione departamentos o cite una norma industrial.", "",
         "**Deciden los pasos.** No decide el titulo, ni el vocabulario, ni la fuente, ni "
         "las `condiciones_activacion`.", "",
         "## Los tres conteos", "",
         f"| | nodos | % |", "|---|---:|---:|",
         f"| UNIVERSALES | **{len(U)}** | {100*len(U)/max(1,len(hechos)):.1f}% |",
         f"| CORPORATIVOS | **{len(C)}** | {100*len(C)/max(1,len(hechos)):.1f}% |",
         f"| DUDOSOS | **{len(D)}** | {100*len(D)/max(1,len(hechos)):.1f}% |",
         f"| **juzgados** | **{len(hechos)}** de {len(activos)} activos | |", ""]

    por_dom = collections.defaultdict(lambda: collections.Counter())
    for x in hechos.values():
        por_dom[x.get("dominio", "core")][x["v"]] += 1
    L += ["### Por dominio", "", "| dominio | universales | corporativos | dudosos |",
          "|---|---:|---:|---:|"]
    for dom in sorted(por_dom):
        c = por_dom[dom]
        L.append(f"| {dom} | {c['U']} | {c['C']} | {c['D']} |")
    L.append("")

    L += ["## LAS SEMILLAS DE ENTRADA CORPORATIVAS", ""]
    if semillas_corp:
        L += ["**AVISO GRANDE.** Una semilla corporativa deja un mundo entero sin puerta de "
              "entrada para un usuario solo.", "",
              "| node_id | dominio | cond | razon |", "|---|---|---|---|"]
        for x in semillas_corp:
            L.append(f"| `{x['id']}` | {x.get('dominio')} | ({x.get('cond')}) | {x.get('razon','')} |")
    else:
        L.append("**NINGUNA.** Ninguno de los nodos marcados corporativos es semilla de "
                 "entrada de su mundo.")
    L.append("")

    L += ["## SIMULACRO DE ENCIERRO (solo calculo)", "",
          f"Si los **{len(C)}** corporativos dejaran de ser ofrecibles, quedarian "
          f"**{len(huerfanos)}** nodos inalcanzables desde las semillas, de los cuales "
          f"**{len(huerfanos_u)} son UNIVERSALES** (los otros son corporativos que se "
          f"apagan a si mismos y no cuentan).", ""]
    if huerfanos_u:
        L += ["**Este es el numero que decide si la compuerta se puede desplegar o si antes "
              "hay que reanclar.** Los primeros veinte:", "",
              "| universal que queda colgando | lo alcanzaba a traves de |", "|---|---|"]
        for h in huerfanos_u[:20]:
            L.append(f"| `{h}` | `{padre_apagado(h) or '(sin padre apagado directo)'}` |")
    else:
        L.append("**CERO universales quedarian colgando.** La compuerta se puede desplegar "
                 "sin reanclar nada.")
    L.append("")

    L += ["## LOS CANDIDATOS, uno por uno", "",
          "Los universales no se listan: basta el conteo de arriba.", "",
          "| node_id | dominio | veredicto | cond | razon (citando el paso) |",
          "|---|---|---|---|---|"]
    for x in sorted(C + D, key=lambda y: (y["v"], y.get("dominio", ""), y["id"])):
        paso = (x.get("paso") or "").replace("|", "/")
        razon = (x.get("razon") or "").replace("|", "/")
        L.append(f"| `{x['id']}` | {x.get('dominio')} | **{'CORPORATIVO' if x['v']=='C' else 'DUDOSO'}** "
                 f"| ({x.get('cond','?')}) | {razon} *Paso: \"{paso}\"* |")
    REPORTE.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"  escrito: {REPORTE}")
    print(f"  U={len(U)} C={len(C)} D={len(D)} | semillas corporativas: {len(semillas_corp)} "
          f"| universales colgando: {len(huerfanos_u)}")


if __name__ == "__main__":
    raise SystemExit(main())
