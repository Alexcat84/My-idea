"""Auditor v81 (Opus 5): cruza las 10 unidades frescas del tramo 6 de la
vuelta 80 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN DIRECCION (el par
no dirigido {a,b}), que es la vara que la TAREA 4 del encargo de la vuelta 81
pedia y que nunca se corrio porque la vuelta no entrego.
Ademas cruza contra la bolsa filtrada de la vuelta 80 buscando la reciproca.
Nada tecleado: los pares se leen de la salida del filtro de la vuelta 80.
"""
import io, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILTRO = os.path.join(RAIZ, "docs", "loop",
                      "SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
BOLSA = os.path.join(RAIZ, "docs", "plan", "PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl")

RE_U = re.compile(r"^\s*(\d+):\s*(.+?)\s*->\s*(.+?)\s*\(paso\s*(.+?),\s*dominio\s*(.+?)\)\s*\|")

unidades = []
for l in io.open(FILTRO, encoding="utf-8"):
    m = RE_U.match(l)
    if m:
        idx, a, b, paso, dom = m.groups()
        unidades.append((int(idx), a, b, paso, dom))
frescas = [u for u in unidades if u[0] >= 20]
print("unidades leidas del filtro: %d | frescas (20..29): %d" % (len(unidades), len(frescas)))
assert len(frescas) == 10, "no son 10 frescas"

ver = {}
n = 0
for l in io.open(VER, encoding="utf-8"):
    l = l.strip()
    if not l:
        continue
    d = json.loads(l)
    n += 1
    ver[frozenset((d["nodo_a"], d["nodo_b"]))] = d
print("veredictos leidos: %d | pares no dirigidos unicos: %d" % (n, len(ver)))

bolsa = []
if os.path.exists(BOLSA):
    for l in io.open(BOLSA, encoding="utf-8"):
        l = l.strip()
        if l:
            bolsa.append(json.loads(l))
print("bolsa filtrada V80: %d unidades" % len(bolsa))
campos = sorted(bolsa[0].keys()) if bolsa else []
print("campos de la bolsa: %s" % campos)

def par_de(d):
    for ka, kb in (("madre", "hijo"), ("nodo_a", "nodo_b"), ("origen", "destino"),
                   ("desde", "hasta"), ("a", "b")):
        if ka in d and kb in d:
            return d[ka], d[kb]
    return None

pares_bolsa = set()
for d in bolsa:
    p = par_de(d)
    if p:
        pares_bolsa.add(p)

print()
print("| # | par | veredicto sin direccion | reciproca en la bolsa V80 |")
print("|---:|---|---|---|")
for idx, a, b, paso, dom in frescas:
    v = ver.get(frozenset((a, b)))
    if v:
        cel = "**%s** puesto %d (%s), dirigido %s -> %s" % (
            v["clase"], v["puesto_intra"], v["dominio"], v["nodo_a"], v["nodo_b"])
    else:
        cel = "sin veredicto"
    rec = "SI" if (b, a) in pares_bolsa else "no"
    print("| %d | `%s -> %s` | %s | %s |" % (idx, a, b, cel, rec))
