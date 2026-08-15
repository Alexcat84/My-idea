# -*- coding: utf-8 -*-
"""vuelta34_ld_opd03.py - LECTURA PURA del acto de OP-D-03, DESPUES del destejido.

DE SOLO LECTURA: no decide, no clasifica, no escribe en ningun documento.

SUCESOR DECLARADO de scripts/loop/vuelta33_ld_opd02.py, y lo que cambia va dicho
(EJECUTOR.md regla 2): aquel leia la nomina de OP-D-02 y este la de OP-D-03, y se
le anaden DOS guardas que alli no hicieron falta:

  - EL RELOJ DE P.5: comprueba que el destejido de este acto YA ESTA HECHO antes
    de imprimir nada. P.5 manda leer DESPUES del destejido, y la decision 3 del
    fundador (15 ago 2026) lo confirmo por su letra. Si el nodo destejido no
    tiene los pasos que el plan sellado deja, este script ABORTA: leer antes
    seria leer texto que va a cambiar.
  - EL SIGUIENTE NUMERO DE LECTURA DIRIGIDA, medido sobre docs/ ENTERO y no
    recordado. La vuelta 33 casi acuna tres numeros ya tomados y lo cazo su
    propio guard; aqui la medicion va de serie.

Imprime los SEIS nodos enteros, los pares ya leidos con su razon, y los que
faltan con su arista buscada en los DOS sentidos y su prueba de que no estan en
la cola del cribado (lo que los hace lectura dirigida y no par saltado: n no se
mueve).

Uso: python scripts/loop/vuelta34_ld_opd03.py
"""
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PARES = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_PARES.jsonl")
DOCS = os.path.join(RAIZ, "docs")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V34_OPD03_AB.json")

OPERACION = "OP-D-03"
RE_LD = re.compile(r"\bLD-(\d+)\b")


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def imprimir_nodo(nid):
    d = nodo(nid)
    print("-" * 78)
    if d is None:
        print("NODO %s: AUSENTE DEL GRAFO" % nid)
        return
    print("NODO: %s" % nid)
    print("  titulo    : %s" % d.get("titulo_concepto"))
    print("  fuente    : %s" % d.get("fuente"))
    print("  dominio   : %s   fase: %s   vivo: %s"
          % (d.get("dominio"), d.get("fase_proyecto"),
             not (d.get("deprecado") or d.get("deprecated"))))
    print("  entregable: %s" % d.get("entregable_esperado"))
    print("  resumen   : %s" % d.get("resumen_teorico"))
    print("  PASOS (%d):" % len(d.get("pasos_accionables") or []))
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print("    %2d. %s" % (i, p))
    print("  CONDICIONES (%d):" % len(d.get("condiciones_activacion") or []))
    for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
        print("    %2d. %s" % (i, c))
    print("  previos   : %s" % (d.get("nodos_previos") or []))
    print("  siguientes: %s" % (d.get("nodos_siguientes") or []))


def arista(a, b):
    da, db = nodo(a) or {}, nodo(b) or {}
    ab = b in (da.get("nodos_previos") or []) + (da.get("nodos_siguientes") or [])
    ba = a in (db.get("nodos_previos") or []) + (db.get("nodos_siguientes") or [])
    return ab, ba


def maximo_ld():
    """El mayor LD-N escrito en docs/ entero. Se mide, no se recuerda."""
    mayor, donde = 0, None
    for raiz, _dirs, ficheros in os.walk(DOCS):
        for f in ficheros:
            if not f.endswith((".md", ".jsonl", ".json", ".txt")):
                continue
            ruta = os.path.join(raiz, f)
            try:
                texto = io.open(ruta, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for m in RE_LD.finditer(texto):
                n = int(m.group(1))
                if n > mayor:
                    mayor, donde = n, os.path.relpath(ruta, RAIZ)
    return mayor, donde


def main():
    ops = {}
    for linea in io.open(OPS, encoding="utf-8"):
        if linea.strip():
            o = json.loads(linea)
            ops[o["id_op"]] = o
    nomina = ops[OPERACION]["nodos"]

    # GUARDA DEL RELOJ DE P.5: el destejido tiene que estar HECHO.
    plan = json.load(io.open(PLAN, encoding="utf-8"))
    f = plan["nodos"][0]
    d = nodo(f["nodo"]) or {}
    pasos = d.get("pasos_accionables") or []
    if pasos != f["pasos_finales"]:
        print("ABORTA (reloj de P.5): %s no tiene todavia los pasos que el plan sellado "
              "deja (%d contra %d). Leer ahora seria leer texto que va a cambiar."
              % (f["nodo"], len(pasos), len(f["pasos_finales"])))
        return 1
    print("GUARDA DEL RELOJ DE P.5: el destejido de %s ESTA HECHO (%d pasos, los del "
          "plan sellado). Se puede leer." % (f["nodo"], len(pasos)))

    mayor, donde = maximo_ld()
    print("SIGUIENTE NUMERO DE LECTURA DIRIGIDA: LD-%d (el mayor escrito en docs/ es "
          "LD-%d, en %s)" % (mayor + 1, mayor, donde))

    vs = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {frozenset((v["nodo_a"], v["nodo_b"])): v for v in vs}
    en_cola = set()
    for linea in io.open(PARES, encoding="utf-8"):
        if linea.strip():
            p = json.loads(linea)
            en_cola.add(frozenset((p["nodo_a"], p["nodo_b"])))

    print()
    print("=" * 78)
    print("LECTURA DIRIGIDA DEL ACTO DE %s (P.5). LOS SEIS NODOS, ENTEROS" % OPERACION)
    print("=" * 78)
    print("NOMINA, leida hoy de OPERACIONES.jsonl: %d nodos" % len(nomina))
    print()
    for nid in sorted(nomina):
        imprimir_nodo(nid)

    print()
    print("=" * 78)
    print("LOS PARES DEL ACTO YA LEIDOS, con su clase y su razon entera")
    print("=" * 78)
    leidos = 0
    for a, b in itertools.combinations(sorted(nomina), 2):
        v = por_par.get(frozenset((a, b)))
        if v is None:
            continue
        leidos += 1
        print()
        print("PUESTO %d, clase %s, clave %s: %s contra %s"
              % (v["puesto_intra"], v["clase"], v["clave"], v["nodo_a"], v["nodo_b"]))
        for i in range(0, len(v["razon"]), 96):
            print("    %s" % v["razon"][i:i + 96])

    total = len(list(itertools.combinations(sorted(nomina), 2)))
    print()
    print("=" * 78)
    print("LOS PARES POR LEER: %d de %d. Con su arista y su prueba de que NO estan en la cola"
          % (total - leidos, total))
    print("=" * 78)
    for a, b in itertools.combinations(sorted(nomina), 2):
        if por_par.get(frozenset((a, b))) is not None:
            continue
        ab, ba = arista(a, b)
        print()
        print("PAR: %s contra %s" % (a, b))
        print("  veredicto en el archivo        : NINGUNO")
        print("  esta en la cola del cribado    : %s"
              % ("SI, ojo: NO seria lectura dirigida"
                 if frozenset((a, b)) in en_cola else "NO, o sea LECTURA DIRIGIDA legitima"))
        print("  %s nombra a %s: %s" % (a, b, ab))
        print("  %s nombra a %s: %s" % (b, a, ba))
        print("  HAY ARISTA: %s" % (ab or ba))
    print()
    print("=" * 78)
    print("FIN DE LA LECTURA. Nada se clasifico y nada se escribio.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
