# -*- coding: utf-8 -*-
# Cuadro de varas PROPIO del auditor, vuelta 58, tramo 5. Codigo independiente
# del instrumento del ejecutor: pasos y condiciones por conteo de listas, cab
# por vecinos resueltos distintos de si mismo, forma por las flechas.
import json, io

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
ALIAS = {}
for k, v in G.items():
    for x in (v.get("ids_alias") or []):
        ALIAS[x] = k

def res(x):
    vistos = set()
    while x in ALIAS and x not in vistos:
        vistos.add(x)
        x = ALIAS[x]
    return x

filas = [json.loads(l) for l in io.open("docs/loop/TRAMO5_V58.jsonl", encoding="utf-8")]
formas = {}
out = io.open("docs/loop/_auditor_v58_varas_tramo5_propio.txt", "w", encoding="utf-8")
for f in filas:
    mi = sorted(f["miembros"])
    d = []
    for x in mi:
        o = json.load(io.open("dataset/nodos/%s.json" % x, encoding="utf-8"))
        cab = {res(y) for c in ("nodos_previos", "nodos_siguientes") for y in (o.get(c) or [])} - {res(x)}
        d.append((len(o.get("pasos_accionables") or []), len(o.get("condiciones_activacion") or []), len(cab)))

    def fl(i):
        if d[0][i] > d[1][i]:
            return 1
        if d[1][i] > d[0][i]:
            return 2
        return 0

    fp, fc, fk = fl(0), fl(1), fl(2)
    conte = [x for x in (fp, fc) if x]
    if not conte:
        forma = "CONTENIDO EMPATA" if fk else "EMPATE SIN VARA"
    elif len(set(conte)) == 2:
        forma = "CHOCAN"
    elif len(conte) == 1:
        forma = "UNA SOLA VARA"
    else:
        forma = "TODAS DE ACUERDO"
    formas[forma] = formas.get(forma, 0) + 1
    out.write("%d|%s|%s|%r|%r|%s\n" % (f["orden_tramo5"], mi[0], mi[1], d[0], d[1], forma))
out.write("POR FORMA: %r\n" % formas)
out.close()
print("POR FORMA (mio):", formas)
