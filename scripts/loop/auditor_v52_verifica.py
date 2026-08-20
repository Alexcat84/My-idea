"""Auditor, vuelta 52: verificacion completa por corrida propia.

SOLO LECTURA sobre el repo. Todo se mide HOY, nada se copia de actas ni
reportes: las cifras del reporte se pasan como contraste al final.

Mide: marcador global y por dominio, grafo, familias, retrato de las A con
resolutor por cadena, colisiones de clase vigentes por par resuelto,
auto-aristas tras resolver, grupos de duplicadas tras resolver (conteo
propio sobre el grafo, no el jsonl), cola de costuras, operaciones,
inventario, y el marcador al corte 2.900.

Uso: python scripts/loop/auditor_v52_verifica.py
"""
import io
import json
import os
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COLA = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")
DUP = os.path.join(RAIZ, "docs", "plan", "ARISTAS_DUPLICADAS.jsonl")


def leer_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


V = leer_jsonl(VER)
n = len(V)
puestos = [p["puesto_intra"] for p in V]
cnt = Counter(p["clase"] for p in V)
print("=== MARCADOR (codigo propio) ===")
print("n=%d huecos=%d dups=%d" % (
    n,
    len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
    n - len(set(puestos))))
for k in "ABCD":
    print("  %s %5d  %.1f" % (k, cnt[k], 100.0 * cnt[k] / n))
print("fuera de ABCD:", sorted(set(cnt) - set("ABCD")) or "ninguna")

byd = defaultdict(Counter)
for p in V:
    byd[p["dominio"]][p["clase"]] += 1
print("\n=== POR DOMINIO (A, n, tasa) ===")
for dom in sorted(byd):
    c = byd[dom]
    nd = sum(c.values())
    print("  %-16s A=%4d n=%5d  %.1f" % (dom, c["A"], nd, 100.0 * c["A"] / nd))

print("\n=== MARCADOR AL CORTE 2900 ===")
c29 = Counter(p["clase"] for p in V if p["puesto_intra"] <= 2900)
print("  " + " / ".join("%s %d" % (k, c29[k]) for k in "ABCD"))

nodos = {}
for f in sorted(os.listdir(NODOS)):
    if f.endswith(".json"):
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        nodos[d["node_id"]] = d


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


dep = [k for k, d in nodos.items() if not vivo(d)]
enl = sum(len(d.get("nodos_previos") or []) + len(d.get("nodos_siguientes") or [])
          for d in nodos.values())
print("\n=== GRAFO ===")
print("ficheros=%d ids=%d vivos=%d deprecados=%d enlaces=%d" % (
    len([f for f in os.listdir(NODOS) if f.endswith(".json")]),
    len(nodos), len(nodos) - len(dep), len(dep), enl))

print("\n=== FAMILIAS ===")
for nombre, trozo in [("Weinberg", "Traction"), ("Horowitz", "Hard Thing"),
                      ("Hugos", "Hugos"), ("Coleman", "Coleman"),
                      ("Rackham", "Rackham")]:
    sel = [d for d in nodos.values()
           if trozo.lower() in (d.get("fuente") or "").lower() and vivo(d)]
    unica = [d for d in sel if len(str(d.get("fuente", "")).split("|")) == 1]
    print("  %-10s vivos=%d unicos=%d" % (nombre, len(sel), len(unica)))

# resolutor por cadena: absorbido -> superviviente, siguiendo cadenas
alias = {}
for nid, d in nodos.items():
    for a in d.get("ids_alias") or []:
        alias[a] = nid


def resolver(x):
    visto = set()
    while x in alias and x not in visto:
        visto.add(x)
        x = alias[x]
    return x


print("\n=== RETRATO DE LAS A (resolutor por cadena) ===")
crudas = [p for p in V if p["clase"] == "A"]
colapsos = 0
pares = set()
for p in crudas:
    ra, rb = resolver(p["nodo_a"]), resolver(p["nodo_b"])
    if ra == rb:
        colapsos += 1
    else:
        pares.add(frozenset((ra, rb)))
print("crudas=%d colapsos=%d pares_distintos=%d" % (len(crudas), colapsos, len(pares)))

print("\n=== COLISIONES DE CLASE VIGENTES (par resuelto, 2+ clases) ===")
porpar = defaultdict(set)
for p in V:
    ra, rb = resolver(p["nodo_a"]), resolver(p["nodo_b"])
    if ra != rb:
        porpar[frozenset((ra, rb))].add(p["clase"])
col = [k for k, cl in porpar.items() if len(cl) > 1]
print("colisiones=%d %s" % (len(col), [sorted(k) for k in col[:10]]))

print("\n=== AUTO-ARISTAS TRAS RESOLVER (vivos) ===")
auto = 0
for nid, d in nodos.items():
    if not vivo(d):
        continue
    for e in (d.get("nodos_previos") or []) + (d.get("nodos_siguientes") or []):
        if resolver(e) == nid:
            auto += 1
print("auto-aristas=%d" % auto)

print("\n=== DUPLICADAS TRAS RESOLVER (grupos, conteo propio) ===")
# una arista dirigida (origen, destino, sentido) que tras resolver aparece
# mas de una vez dentro del mismo nodo vivo forma un grupo
grupos = 0
for nid, d in nodos.items():
    if not vivo(d):
        continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        c = Counter(resolver(e) for e in d.get(campo) or [])
        grupos += sum(1 for k, v in c.items() if v > 1)
print("grupos propios=%d" % grupos)
if os.path.exists(DUP):
    dup = leer_jsonl(DUP)
    print("lineas de ARISTAS_DUPLICADAS.jsonl=%d" % len(dup))
    if dup and isinstance(dup[0], dict):
        print("claves ejemplo:", sorted(dup[0].keys()))

print("\n=== COLA DE COSTURAS ===")
print("lineas=%d" % len(leer_jsonl(COLA)))

print("\n=== OPERACIONES E INVENTARIO ===")
ops = leer_jsonl(OPS)
ids = set(o["id_op"] for o in ops)
rotas = [(o["id_op"], d) for o in ops
         for d in (o.get("depende_de") or []) + (o.get("bloquea_a") or [])
         if d not in ids]
print("operaciones=%d estados=%s rotas=%d" % (
    len(ops), dict(Counter(o["estado"] for o in ops)), len(rotas)))
print("inventario=%d" % len(leer_jsonl(INV)))
