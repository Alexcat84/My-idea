# -*- coding: utf-8 -*-
"""Auditor v129: resuelve la nomina de OP-S-10 por el resolutor (P.1) y mide
la verificacion 1 sobre el arbol de HOY. Codigo propio del auditor."""
import glob, io, json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LIT = "Solo aplica si vendes o piensas vender franquicias en Estados Unidos"

m = {}
for f in glob.glob(os.path.join(NODOS, "*.json")):
    o = json.load(io.open(f, encoding="utf-8"))
    nid = os.path.basename(f)[:-5]
    for a in (o.get("ids_alias") or []):
        m[a] = nid
print("ALIAS EN EL RESOLUTOR:", len(m))

def res(x):
    visto = set()
    while x in m and x not in visto:
        visto.add(x); x = m[x]
    return x

G = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]

nomina = None
for l in io.open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"), encoding="utf-8"):
    if not l.strip(): continue
    o = json.loads(l)
    if o.get("id_op") == "OP-S-10":
        nomina = o["nodos"]
print("NOMINA (campo nodos):", len(nomina), "unicos:", len(set(nomina)))

cambian = []
for nid in nomina:
    r = res(nid)
    if r != nid:
        cambian.append((nid, r))
print("IDS QUE EL RESOLUTOR MUEVE:", len(cambian))
for a, b in cambian: print("   ", a, "->", b)

resueltos = sorted({res(x) for x in nomina})
print("RESUELVEN A", len(resueltos), "IDS DISTINTOS")
ausentes = [x for x in resueltos if x not in G]
vivos = [x for x in resueltos if x in G and not G[x].get("deprecado")]
depre = [x for x in resueltos if x in G and G[x].get("deprecado")]
print("  vivos:", len(vivos), " deprecados:", len(depre), " ausentes:", ausentes or "ninguno")
if depre: print("  DEPRECADOS TRAS RESOLVER:", depre)

def nombra_pais(n):
    return any("Estados Unidos" in c for c in (n.get("condiciones_activacion") or []))
def literal_primero(n):
    ca = n.get("condiciones_activacion") or []
    return bool(ca) and ca[0].strip() == LIT

sin = [x for x in vivos if not nombra_pais(G[x])]
print("\nVERIFICACION 1 (todo vivo de la nomina resuelta nombra el pais):")
print("  CUBIERTOS:", len(vivos) - len(sin), "de", len(vivos))
print("  SIN CUBRIR:", sin or "NINGUNO")
print("  con el literal exacto en PRIMERA posicion:", sum(1 for x in vivos if literal_primero(G[x])))
for x in sin:
    print("\n  --- ", x, "---")
    n = G[x]
    print("   titulo:", n.get("titulo"))
    print("   dominio:", n.get("dominio"), "| fuente:", str(n.get("fuente"))[:120])
    print("   deprecado:", n.get("deprecado"))
    print("   condiciones_activacion:", n.get("condiciones_activacion"))
