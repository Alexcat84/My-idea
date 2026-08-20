# -*- coding: utf-8 -*-
"""vuelta50_supervivientes_viables.py . PARA CADA ACTO MIXTO, QUE SUPERVIVIENTES
DEJAN QUE LA RECETA DE `P.12` SE EJECUTE SIN VIOLAR UN VEREDICTO.

POR QUE EXISTE, y el motivo se levanto leyendo los dos primeros actos de esta
vuelta: la receta del encargo ("elige el superviviente de la PARTE A, lee el
MIXTO contra ese superviviente") esta bien escrita pero no dice QUE ES la parte A
cuando las aristas `A` del acto no forman una clique. Medido en esta vuelta:
24 de los 26 mixtos pendientes tienen forma de ESTRELLA y no de clique
(docs/loop/SALIDA_V50_FORMA_MIXTOS.txt). Sin una definicion operativa, "la parte
A" es una decision disfrazada de dato.

LA DEFINICION OPERATIVA, sacada del UNICO acto ya resuelto (el del SPIN, vuelta
49) y no inventada: alli el superviviente fue `modelo_spin_preguntas`, LA PARTE A
fueron los nodos con arista `A` CONTRA EL SUPERVIVIENTE, y EL MIXTO fue el unico
miembro SIN arista `A` contra el (tenia `A` con un nodo que moria y `D` con el
superviviente). Generalizada:

    dado un superviviente S,
      PARTE A = {S} mas los miembros con arista A contra S
      MIXTOS  = los miembros SIN arista A contra S

Y DE AHI SALE LA CONDICION DE VIABILIDAD, que es lo unico que este instrumento
anade y que es pura comprobacion, no criterio:

  (a) LA PARTE A TIENE QUE SER UNA CLIQUE `A`. Si dos miembros de la parte A
      tienen entre si un par que NO es `A`, fundirlos junta dos nodos que el
      archivo declaro DISTINTOS, y eso es exactamente lo que `P.12` prohibe
      ("el cierre transitivo CONVOCA, la lectura DECIDE; ni transitividad
      automatica ni mayoria").
  (b) TIENE QUE QUEDAR AL MENOS UN MIXTO FUERA. Si no queda ninguno, no hay
      lectura `P.12` que hacer y el acto no es mixto por este superviviente:
      seria una fusion entera, que es justo lo que la figura del acto desmiente.

RESULTADOS POSIBLES, y los tres se imprimen sin forzar ninguno:
  UN SOLO VIABLE     : la estructura fuerza el superviviente. El contenido lo
                       confirma o lo discute, pero no hay eleccion que inventar.
  VARIOS VIABLES     : el contenido decide, que es la regla de la pagina
                       (sobrevive por CONTENIDO; a contenido empatado, `P.8`).
  NINGUNO VIABLE     : la receta NO alcanza para este acto sin decidir algo que
                       ninguna regla escrita decide. Se DECLARA, no se improvisa.

Y ADEMAS SE IMPRIME, porque es el dato que mas discusion levanta: a quien nombra
como superviviente cada veredicto `A` del acto, buscando la formula "Sobrevive X"
en su razon. UN VEREDICTO PUEDE NOMBRAR A UN NODO QUE NO ES VIABLE, y cuando pasa
se dice: es un choque real entre la letra de un veredicto y la estructura del
acto, y no se resuelve en silencio.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta50_supervivientes_viables.py \
      --hoy docs/loop/RECOMPUTO_V50_APERTURA.jsonl --hasta 35
"""
import argparse
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

RE_SOBREVIVE = re.compile(r"[Ss]obrevive\s+([a-z0-9_]+)")


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hoy", required=True)
    ap.add_argument("--hasta", type=int, default=0)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            todos[d["node_id"]] = d
    alias = {}
    for nid, d in todos.items():
        if not (d.get("deprecado") or d.get("deprecated")):
            for x in (d.get("ids_alias") or []):
                alias[x] = nid

    def res(x):
        s = set()
        while x in alias and x not in s:
            s.add(x)
            x = alias[x]
        return x

    porpar = {}
    for v in cargar_jsonl(VER):
        porpar.setdefault(frozenset((res(v["nodo_a"]), res(v["nodo_b"]))), []).append(v)

    cerrados = [c for c in cargar_jsonl(a.hoy) if c["estado"] == "CERRADO"]
    if a.hasta:
        cerrados = cerrados[:a.hasta]

    print("=" * 78)
    print("SUPERVIVIENTES VIABLES POR ACTO MIXTO, medidos hoy")
    print("nomina: %s" % a.hoy)
    print("=" * 78)
    print()

    resumen = {"UN SOLO VIABLE": [], "VARIOS VIABLES": [], "NINGUNO VIABLE": []}
    choques = []

    for n, c in enumerate(cerrados, 1):
        ms = sorted(set(res(m) for m in c["miembros"]))
        clase, puestos = {}, {}
        for x, y in itertools.combinations(ms, 2):
            vs = porpar.get(frozenset((x, y))) or []
            clase[frozenset((x, y))] = sorted(set(v["clase"] for v in vs))
            puestos[frozenset((x, y))] = vs
        es_a = {k: ("A" in v) for k, v in clase.items()}
        if not any(es_a.values()) or all(es_a.values()):
            continue  # no es mixto

        print("--- ACTO %d  tam %d" % (n, len(ms)))
        print("      miembros: %s" % ", ".join(ms))
        for k in sorted(clase, key=lambda z: sorted(z)):
            x, y = sorted(k)
            print("        %-46s %-46s %-6s %s"
                  % (x, y, ",".join(clase[k]) or "SIN",
                     ",".join(str(v["puesto_intra"]) for v in puestos[k])))

        # A quien nombra cada veredicto A como superviviente.
        nombrados = {}
        for k, vs in puestos.items():
            for v in vs:
                if v["clase"] != "A":
                    continue
                for m in RE_SOBREVIVE.findall(v["razon"]):
                    if res(m) in ms:
                        nombrados.setdefault(res(m), []).append(v["puesto_intra"])
        print("      LOS VEREDICTOS A NOMBRAN SUPERVIVIENTE: %s"
              % (", ".join("%s (puestos %s)" % (k, ",".join(str(p) for p in v))
                           for k, v in sorted(nombrados.items()))
                 or "ninguno lo escribe con la formula 'Sobrevive X'"))

        viables = []
        for s in ms:
            parte = [s] + [m for m in ms if m != s and es_a[frozenset((s, m))]]
            mixtos = [m for m in ms if m not in parte]
            if not mixtos:
                razon = "no deja ningun mixto fuera: seria fusion entera"
            elif not all(es_a[frozenset(p)] for p in itertools.combinations(parte, 2)):
                malos = [sorted(p) for p in itertools.combinations(parte, 2)
                         if not es_a[frozenset(p)]]
                razon = ("la parte A no es clique: %s no es A"
                         % " y ".join("%s con %s" % (x, y) for x, y in malos))
            else:
                viables.append((s, parte, mixtos))
                razon = None
            if razon:
                print("      %-46s NO VIABLE: %s" % (s, razon))
        for s, parte, mixtos in viables:
            print("      %-46s VIABLE   parte A = %s   MIXTO(S) = %s"
                  % (s, ", ".join(sorted(parte)), ", ".join(mixtos)))

        if len(viables) == 1:
            k = "UN SOLO VIABLE"
        elif viables:
            k = "VARIOS VIABLES"
        else:
            k = "NINGUNO VIABLE"
        resumen[k].append(n)
        print("      VEREDICTO DEL INSTRUMENTO: %s" % k)

        ids_viables = set(s for s, _, _ in viables)
        for nm, ps in nombrados.items():
            if nm not in ids_viables:
                choques.append((n, nm, ps))
                print("      CHOQUE: los veredictos %s nombran superviviente a %s,"
                      % (",".join(str(p) for p in ps), nm))
                print("              que NO es viable por la estructura del acto.")
        print()

    print("=" * 78)
    print("RESUMEN")
    for k in ("UN SOLO VIABLE", "VARIOS VIABLES", "NINGUNO VIABLE"):
        print("  %-16s %2d   actos %s"
              % (k, len(resumen[k]), ", ".join(str(x) for x in resumen[k]) or "ninguno"))
    print("  CHOQUES letra del veredicto contra estructura: %d" % len(choques))
    for n, nm, ps in choques:
        print("     acto %d: %s nombrado en %s" % (n, nm, ",".join(str(p) for p in ps)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
