# -*- coding: utf-8 -*-
"""AUDITOR vuelta 88. Vara propia de la TAREA 5 (re-base de OP-E-06) y de la
TAREA 4 (guarda OP-C-05). Nada se teclea: todo se lee de los ficheros.
"""
import collections
import json
import re

nodos = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


COS = filas("docs/plan/COSECHA_RAZONES_D.jsonl")
print("=" * 78)
print("A. LA COSECHA, TALLADA POR MI")
print("=" * 78)
print("filas totales: %d" % len(COS))
print("campos de la primera fila: %s" % sorted(COS[0].keys()))
nuevos = [r for r in COS if r.get("nuevo") is True]
print("nuevo=true: %d" % len(nuevos))
e06 = [r for r in nuevos if r.get("senales") != ["continua por la vara"]]
e07 = [r for r in nuevos if r.get("senales") == ["continua por la vara"]]
print("candidatos OP-E-06 (senales distintas de ['continua por la vara']): %d" % len(e06))
print("candidatos OP-E-07 (senal exacta): %d" % len(e07))
print("reparto por dominio de los OP-E-06: %s" % dict(
    collections.Counter(r.get("dominio") for r in e06).most_common()))
print("reparto por dominio de los OP-E-07: %s" % dict(
    collections.Counter(r.get("dominio") for r in e07).most_common()))


def alias_resuelve(nid):
    """resuelve un id por alias hasta un nodo del grafo, si lo hay"""
    return nid if nid in nodos else None


def hay_arista(a, b):
    va, vb = nodos.get(a) or {}, nodos.get(b) or {}
    return (b in (va.get("nodos_siguientes") or []) or
            a in (vb.get("nodos_previos") or []) or
            a in (vb.get("nodos_siguientes") or []) or
            b in (va.get("nodos_previos") or []))


print()
print("=" * 78)
print("B. MEDICION DE CONTRASTE SOBRE LOS 192 COMPLETOS (definicion estricta, sin alias)")
print("=" * 78)
ya, depre, inex = 0, 0, 0
for r in e06:
    a, b = r.get("nodo_a"), r.get("nodo_b")
    if a not in nodos or b not in nodos:
        inex += 1
        continue
    if (nodos[a].get("deprecado")) or (nodos[b].get("deprecado")):
        depre += 1
    if hay_arista(a, b):
        ya += 1
print("ya tienen arista (alguna direccion, SIN alias): %d" % ya)
print("tocan un nodo DEPRECADO: %d" % depre)
print("tocan un id inexistente: %d" % inex)

print()
print("=" * 78)
print("C. LA BOLSA RE-BASADA DEL EJECUTOR")
print("=" * 78)
reb = filas("docs/plan/OP_E_06_REBASE_V88.jsonl")
print("filas de docs/plan/OP_E_06_REBASE_V88.jsonl: %d" % len(reb))
print("campos: %s" % sorted(reb[0].keys()))
pares = set()
for r in reb:
    pares.add((r.get("nodo_a"), r.get("nodo_b")))
print("pares unicos: %d" % len(pares))
en_cosecha = set((r.get("nodo_a"), r.get("nodo_b")) for r in e06)
print("filas de la bolsa QUE NO ESTAN en los 192 de la cosecha: %d" % len(pares - en_cosecha))
d = collections.Counter(r.get("dominio") for r in reb)
print("reparto por dominio de la bolsa: %s" % dict(d.most_common()))
conarista = sum(1 for a, b in pares if a in nodos and b in nodos and hay_arista(a, b))
print("pares de la bolsa que YA tienen arista hoy (estricto): %d" % conarista)
condepre = sum(1 for a, b in pares if a in nodos and b in nodos and
               ((nodos[a].get("deprecado")) or (nodos[b].get("deprecado"))))
print("pares de la bolsa que tocan un DEPRECADO: %d" % condepre)

print()
print("=" * 78)
print("D. LA DIRECCION, CON LA LISTA DE PALABRAS DEL ENCARGO (vara propia)")
print("=" * 78)
PAL = ["madre", "hijo", "padre", "desarrolla", "detalla", "en una linea",
       "procedimiento", "cuelga", "enumera", "menciona", "nombra"]


def tiene_direccion(txt):
    t = (txt or "").lower()
    return any(p in t for p in PAL)


campo = "frase"
con = sum(1 for r in e06 if tiene_direccion(r.get(campo)))
print("campo de frase usado: %s" % campo)
print("de los 192: CON alguna palabra %d, SIN ninguna %d" % (con, len(e06) - con))
lit = sum(1 for r in e06 if "ninguno enlaza al otro" in (r.get(campo) or "").lower())
print("frases literales 'Ninguno enlaza al otro.': %d" % lit)
