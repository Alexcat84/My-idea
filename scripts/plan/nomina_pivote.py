# -*- coding: utf-8 -*-
"""NOMINA DEL RACIMO DEL PIVOTE, con los DOS instrumentos que manda el estandar:
   1. EL CONTADOR: levanta candidatos POR EL NOMBRE (id y titulo).
   2. EL BARRIDO DE LAS A: levanta candidatos POR EL ARCHIVO (toda A vigente).
   Los dos levantan; la lectura decide. Corte: el maximo puesto del archivo."""
import json, io, sys, re, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
VIV = {k: v for k, v in G.items() if not v.get("deprecado")}
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
P = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
CORTE = max(r["puesto_intra"] for r in V)
leido = {frozenset((r["nodo_a"], r["nodo_b"])): r for r in V}
encola = {frozenset((p["nodo_a"], p["nodo_b"])) for p in P}

# --- 1. EL CONTADOR: por el nombre ---
RX = re.compile(r"pivot|perseverar|proceed", re.I)
contador = sorted(k for k, v in VIV.items()
                  if RX.search(k) or RX.search(v.get("titulo_concepto") or ""))
print("### 1. EL CONTADOR (por el nombre): %d candidatos" % len(contador))
for k in contador: print("   ", k, "|", VIV[k].get("titulo_concepto"))

# --- 2. EL BARRIDO DE LAS A: por el archivo ---
ady = collections.defaultdict(set)
for r in V:
    if r["clase"] == "A":
        ady[r["nodo_a"]].add(r["nodo_b"]); ady[r["nodo_b"]].add(r["nodo_a"])
def comp(n):
    pila = [n]; c = set()
    while pila:
        x = pila.pop()
        if x in c: continue
        c.add(x); pila.extend(ady[x] - c)
    return c
barrido = set()
for k in contador: barrido |= comp(k)
print()
print("### 2. EL BARRIDO DE LAS A (por el archivo): %d nodos" % len(barrido))
for k in sorted(barrido):
    marca = "" if k in contador else "   <== SOLO POR EL BARRIDO, el contador no lo ve"
    print("   ", k, "|", (VIV.get(k) or {}).get("titulo_concepto"), marca)

# --- 3. LA UNION y su cobertura ---
nom = sorted(set(contador) | barrido)
pos = len(nom) * (len(nom) - 1) // 2
ley = [(a, b) for a, b in itertools.combinations(nom, 2) if frozenset((a, b)) in leido]
col = [(a, b) for a, b in itertools.combinations(nom, 2) if frozenset((a, b)) in encola and frozenset((a, b)) not in leido]
fue = [(a, b) for a, b in itertools.combinations(nom, 2) if frozenset((a, b)) not in encola and frozenset((a, b)) not in leido]
cl = collections.Counter(leido[frozenset(p)]["clase"] for p in ley)
print()
print("### 3. LA NOMINA UNIDA, corte puesto %d" % CORTE)
print("   miembros: %d | pares posibles: %d | leidos: %d | en cola: %d | fuera de cola: %d"
      % (len(nom), pos, len(ley), len(col), len(fue)))
print("   clases de los leidos:", dict(cl))
forma = "PURO" if cl.get("A", 0) == len(ley) and len(ley) == pos else ("SUB-PURO" if cl.get("A",0)==len(ley) else "MEZCLADO")
print("   FORMA:", forma, "| COBERTURA: %d de %d" % (len(ley), pos))
print()
print("   pares leidos:")
for a, b in ley: print("      [%s] %s | %s  (puesto %d)" % (leido[frozenset((a,b))]["clase"], a, b, leido[frozenset((a,b))]["puesto_intra"]))
if col:
    print("   pares EN COLA sin leer:")
    for a, b in col: print("      ", a, "|", b)
if fue:
    print("   pares FUERA DE COLA:")
    for a, b in fue: print("      ", a, "|", b)
