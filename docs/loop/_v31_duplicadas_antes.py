# Un solo uso: mide las MISMAS duplicadas tras resolver sobre la version de HEAD
# de los nodos tocados, para separar lo que esta vuelta creo de lo que ya venia.
# La guarda de vuelta31_guardas_col.py cayo en 9 duplicadas: la pregunta es de
# quien son.
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V31_OPF04_COL.json")

g = json.load(open(MASTER, encoding="utf-8"))["nodos"]
ALIAS = {a: k for k, v in g.items() for a in (v.get("ids_alias") or [])}


def res(x):
    visto = set()
    while x in ALIAS and x not in visto:
        visto.add(x)
        x = ALIAS[x]
    return x


def head(nid):
    p = subprocess.run(["git", "show", "HEAD:dataset/nodos/%s.json" % nid],
                       cwd=RAIZ, capture_output=True)
    if p.returncode != 0:
        return None
    return json.loads(p.stdout.decode("utf-8"))


plan = json.load(open(PLAN, encoding="utf-8"))
tocados = set()
for c in plan["cortes"]:
    tocados.add(c["origen"])
    tocados.add(c["destino"].get("nodo") or c["destino"]["nuevo"]["node_id"])

print("DUPLICADAS TRAS RESOLVER, en la version de HEAD (antes del corte de hoy)")
print("=" * 78)
total = 0
for nid in sorted(tocados):
    d = head(nid)
    if d is None:
        print("  %-42s NO EXISTIA EN HEAD (nodo propio de hoy)" % nid)
        continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        v = [res(x) for x in (d.get(campo) or [])]
        sobran = len(v) - len(set(v))
        propias = sum(1 for x in v if x == res(nid))
        if sobran or propias:
            total += sobran
            print("  %-42s %-17s duplicadas %d  auto %d" % (nid, campo, sobran, propias))
            vistos = {}
            for original in (d.get(campo) or []):
                r = res(original)
                vistos.setdefault(r, []).append(original)
            for r, orig in vistos.items():
                if len(orig) > 1:
                    print("       %s  <-  %s" % (r, orig))
print("=" * 78)
print("TOTAL DUPLICADAS EN HEAD, sobre los nodos tocados: %d" % total)
