# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 88. Mediciones propias de la seccion 1 del acta.
Los pares y los ids se LEEN de los ficheros; ninguno se teclea a mano.

  python docs/loop/_auditor_v88_mediciones.py > docs/loop/_auditor_v88_mediciones.txt
"""
import collections
import hashlib
import json
import os
import subprocess

GRAFO = "dataset/metadata/master_graph.json"
CAL = "docs/plan/PASO_NODO_CALIBRADO.jsonl"
REG = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
REBASE = "docs/plan/OP_E_06_REBASE_V88.jsonl"
COSECHA = "docs/plan/COSECHA_RAZONES_D.jsonl"

REFS = [("e6dc63a0", "apertura, acta 87"),
        ("970713d6", "TAREA 2"),
        ("e6402ea2", "TAREA 3"),
        ("dfe9650a", "TAREAS 4 y 5"),
        ("e7b0d21f", "cierre, HEAD")]


def filas(ruta):
    return [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]


def bytes_de(ref, ruta):
    return subprocess.run(["git", "show", "%s:%s" % (ref, ruta)],
                          capture_output=True, check=True).stdout


def grafo_de(ref):
    return json.loads(bytes_de(ref, GRAFO).decode("utf-8"))["nodos"]


def cifras(nodos):
    total = len(nodos)
    vivos = sum(1 for v in nodos.values() if not v.get("deprecado"))
    sig = sum(len(v.get("nodos_siguientes") or []) for v in nodos.values())
    prev = sum(len(v.get("nodos_previos") or []) for v in nodos.values())
    union, auto, dup = set(), 0, 0
    for k, v in nodos.items():
        s = v.get("nodos_siguientes") or []
        p = v.get("nodos_previos") or []
        if len(s) != len(set(s)) or len(p) != len(set(p)):
            dup += 1
        if k in s or k in p:
            auto += 1
        for d in s:
            union.add((k, d))
        for o in p:
            union.add((o, k))
    return dict(nodos=total, vivos=vivos, depre=total - vivos, sig=sig,
                prev=prev, suma=sig + prev, union=len(union), auto=auto, dup=dup)


print("=" * 78)
print("1. LAS CIFRAS DEL GRAFO EN CINCO REFS MAS EL ARBOL")
print("=" * 78)
print("%-28s %6s %6s %5s %7s %7s %7s %7s %5s %5s" % (
    "ref", "nodos", "vivos", "depre", "sig", "prev", "suma", "union", "auto", "dup"))
for ref, que in REFS:
    c = cifras(grafo_de(ref))
    sha = hashlib.sha256(bytes_de(ref, GRAFO)).hexdigest()
    print("%-28s %6d %6d %5d %7d %7d %7d %7d %5d %5d" % (
        "%s (%s)" % (ref, que), c["nodos"], c["vivos"], c["depre"], c["sig"],
        c["prev"], c["suma"], c["union"], c["auto"], c["dup"]))
    print("    sha256 master_graph: %s" % sha)

nodos = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
c = cifras(nodos)
print("%-28s %6d %6d %5d %7d %7d %7d %7d %5d %5d" % (
    "arbol de trabajo", c["nodos"], c["vivos"], c["depre"], c["sig"],
    c["prev"], c["suma"], c["union"], c["auto"], c["dup"]))
print("    sha256 master_graph: %s" % hashlib.sha256(open(GRAFO, "rb").read()).hexdigest())

print()
print("=" * 78)
print("2. EL MARCADOR DEL CRIBADO")
print("=" * 78)
vs = filas(VER)
cl = collections.Counter(v.get("clase") or v.get("veredicto") for v in vs)
puestos = sorted(v["puesto"] for v in vs if "puesto" in v)
print("n=%d  clases=%s" % (len(vs), dict(cl)))
if puestos:
    huecos = [p for p in range(puestos[0], puestos[-1] + 1) if p not in set(puestos)]
    print("puestos %d..%d, unicos %d, huecos %d" % (
        puestos[0], puestos[-1], len(set(puestos)), len(huecos)))

print()
print("=" * 78)
print("3. EL REGISTRO OP_E_01_DECIDIDAS, CRUZADO CONTRA EL GRAFO DE HOY")
print("=" * 78)
reg = filas(REG)
dec = collections.Counter(r.get("decision") for r in reg)
print("filas=%d  decisiones=%s" % (len(reg), dict(dec)))
malas = []
for r in reg:
    m, h = r.get("madre"), r.get("hijo")
    a = nodos.get(m) or {}
    b = nodos.get(h) or {}
    hay = h in (a.get("nodos_siguientes") or []) or m in (b.get("nodos_previos") or [])
    esperado = (r.get("decision") == "ESCRITA")
    if hay != esperado:
        malas.append((m, h, r.get("decision"), hay))
print("filas cuya decision NO calza con el grafo de hoy: %d" % len(malas))
for x in malas[:10]:
    print("   ", x)

print()
print("=" * 78)
print("4. EL DESFASE DEL CALIBRADO (bolsa distinta del grafo)")
print("=" * 78)
cal = filas(CAL)
print("filas de la bolsa: %d" % len(cal))
desf = []
for r in cal:
    m, h = r.get("madre"), r.get("hijo")
    a = nodos.get(m) or {}
    b = nodos.get(h) or {}
    hay = h in (a.get("nodos_siguientes") or []) or m in (b.get("nodos_previos") or [])
    if hay:
        desf.append("%s -> %s" % (m, h))
print("pares de la bolsa CON arista en el grafo de hoy: %d" % len(desf))
for x in desf:
    print("   ", x)
