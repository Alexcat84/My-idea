# -*- coding: utf-8 -*-
"""Instrumento de solo lectura de la VUELTA 18.

No escribe nada. Mide, sobre los archivos del repo en esta vuelta:
  1. el plan de operaciones (cuantas, cuantas LISTAS, ids unicos)
  2. el marcador del cribado recomputado desde el archivo de veredictos
  3. la tasa por dominio
  4. las figuras del inventario y cuales nombran ejemplares

Todo lo que imprime sale de leer los archivos AHORA, no de ninguna nota previa.
"""
import json
import re
import sys
from collections import Counter, defaultdict

RAIZ = "."
OPS = "docs/plan/OPERACIONES.jsonl"
INV = "docs/plan/INVENTARIO.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


def cargar(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for n, linea in enumerate(fh, 1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                filas.append(json.loads(linea))
            except json.JSONDecodeError as exc:
                print("LINEA MALA %s:%d %s" % (ruta, n, exc))
                sys.exit(1)
    return filas


def medir_operaciones():
    ops = cargar(OPS)
    estados = Counter(o.get("estado") for o in ops)
    ids = [o.get("id_op") for o in ops]
    print("== OPERACIONES ==")
    print("total          : %d" % len(ops))
    print("por estado     : %s" % dict(estados))
    print("ids unicos     : %d de %d" % (len(set(ids)), len(ids)))
    print("sin id_op      : %d" % sum(1 for i in ids if not i))
    fases = Counter(o.get("fase") for o in ops)
    print("por fase       :")
    for f in sorted(fases, key=lambda x: str(x)):
        listas = sum(1 for o in ops if o.get("fase") == f and o.get("estado") == "LISTA")
        print("   %-24s %3d  LISTAS %3d" % (f, fases[f], listas))
    return ops


def medir_marcador():
    filas = cargar(VER)
    print("\n== MARCADOR DEL CRIBADO ==")
    print("lineas del archivo : %d" % len(filas))
    clases = Counter(f.get("clase") for f in filas)
    n = len(filas)
    for c in ("A", "B", "C", "D"):
        v = clases.get(c, 0)
        print("   %s %5d  (%.1f%%)" % (c, v, 100.0 * v / n if n else 0))
    otras = {k: v for k, v in clases.items() if k not in ("A", "B", "C", "D")}
    if otras:
        print("   OTRAS CLASES: %s" % otras)
    puestos = [f.get("puesto_intra") for f in filas]
    print("puestos unicos     : %d" % len(set(puestos)))
    print("min / max          : %s / %s" % (min(puestos), max(puestos)))
    faltan = sorted(set(range(min(puestos), max(puestos) + 1)) - set(puestos))
    print("huecos             : %d %s" % (len(faltan), faltan[:10]))
    dup = [p for p, c in Counter(puestos).items() if c > 1]
    print("duplicados         : %d %s" % (len(dup), dup[:10]))

    print("\n== TASA POR DOMINIO ==")
    por_dom = defaultdict(lambda: Counter())
    for f in filas:
        por_dom[f.get("dominio")][f.get("clase")] += 1
    print("%-18s %6s %6s %6s" % ("dominio", "pares", "A", "tasa"))
    for d in sorted(por_dom):
        c = por_dom[d]
        tot = sum(c.values())
        a = c.get("A", 0)
        print("%-18s %6d %6d %5.1f%%" % (d, tot, a, 100.0 * a / tot if tot else 0))
    return filas


# criterio de forma de la vuelta 17, reproducido tal cual antes de medir nada nuevo
RE_ID = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){2,}\b")
RE_PUESTO = re.compile(r"\bpuestos?\s+\d{2,4}\b", re.IGNORECASE)
RE_LD = re.compile(r"\bLD-\d+\b")


def medir_figuras():
    inv = cargar(INV)
    figs = [e for e in inv if e.get("tipo") == "figura"]
    print("\n== FIGURAS ==")
    print("total figuras : %d" % len(figs))
    nombran, no_nombran = [], []
    for f in figs:
        nota = f.get("nota", "") or ""
        # criterio de la vuelta 17: la nota trae id de nodo, puesto citado o id de LD
        tiene = bool(RE_LD.search(nota) or RE_ID.search(nota) or RE_PUESTO.search(nota))
        (nombran if tiene else no_nombran).append(f.get("nombre"))
    print("nombran       : %d" % len(nombran))
    print("no nombran    : %d" % len(no_nombran))
    for nb in no_nombran:
        e = [x for x in figs if x.get("nombre") == nb][0]
        print("   - %-46s cobertura: %s" % (nb, e.get("cobertura")))
    return figs


if __name__ == "__main__":
    medir_operaciones()
    medir_marcador()
    medir_figuras()
