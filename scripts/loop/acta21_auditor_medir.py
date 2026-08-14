# acta21_auditor_medir.py . Instrumento PROPIO del auditor para el acta de la
# vuelta 21 (14 ago 2026). Solo lectura. Codigo distinto del de los
# instrumentos del ejecutor: los criterios se reimplementan, no se copian.
import json
import re
import subprocess
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
R = lambda p: open(p, encoding="utf-8")

# --- 1. El marcador, desde el archivo de veredictos -------------------------
veredictos = [json.loads(l) for l in R("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")]
n = len(veredictos)
clases = Counter(v["clase"] for v in veredictos)
puestos = [v["puesto_intra"] for v in veredictos]
huecos = set(range(1, n + 1)) - set(puestos)
dups = [p for p, c in Counter(puestos).items() if c > 1]
print(f"veredictos: {n} lineas")
print("clases:", {k: clases[k] for k in "ABCD"},
      "| pct:", {k: round(100 * clases[k] / n, 1) for k in "ABCD"})
print(f"puestos 1..{n}: huecos={len(huecos)} duplicados={len(dups)}")
print("por dominio (pares, A, B, C, D, tasaA%):")
dom = {}
for v in veredictos:
    dom.setdefault(v["dominio"], Counter())[v["clase"]] += 1
for d in sorted(dom):
    c = dom[d]
    t = sum(c.values())
    print(f"  {d}: {t} | {c['A']} {c['B']} {c['C']} {c['D']} | "
          f"{round(100 * c['A'] / t, 1)}")

# --- 2. El grafo ------------------------------------------------------------
g = json.load(R("dataset/metadata/master_graph.json"))
nodos = g["nodos"]
dep = [nid for nid, nd in nodos.items() if "deprecado" in nd]
vivos = {nid: nd for nid, nd in nodos.items() if "deprecado" not in nd}
print(f"\ngrafo: {len(nodos)} nodos, {len(vivos)} vivos, {len(dep)} deprecado")

# --- 3. Operaciones, componentes, inventario --------------------------------
ops = [json.loads(l) for l in R("docs/plan/OPERACIONES.jsonl")]
estados = Counter(o["estado"] for o in ops)
print(f"operaciones: {len(ops)} | estados: {dict(estados)}")
comp = sum(1 for _ in R("docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl"))
inv = sum(1 for _ in R("docs/plan/INVENTARIO.jsonl"))
print(f"componentes: {comp} | inventario: {inv}")

# --- 4. Horowitz en segunda o posterior posicion (matcher propio) -----------
def segmentos(nd):
    f = nd.get("fuente") or ""
    return [s.strip() for s in f.split("|") if s.strip()]

HOR = re.compile(r"horowitz|hard thing", re.I)
hor2 = sorted(nid for nid, nd in vivos.items()
              if any(HOR.search(s) for s in segmentos(nd)[1:]))
print(f"\nHorowitz en 2a+ posicion (vivos): {len(hor2)}")
opf04 = next(o for o in ops if o["id_op"] == "OP-F-04-HOR")
n13 = set(opf04["nodos"])
print(f"OP-F-04-HOR campo nodos: {len(n13)}")
print("los 14 menos los 13:", sorted(set(hor2) - n13))
print("de los 13, fuera del grafo:", sorted(n13 - set(nodos)))

# --- 5. Cobertura de plan de principio_calidad_mvp --------------------------
sedes = [o["id_op"] for o in ops if "principio_calidad_mvp" in (o.get("nodos") or [])]
print(f"principio_calidad_mvp en campo nodos de: {sedes}")

# --- 6. Doble grafia del mismo libro en un nodo (criterio propio: dos
#        segmentos cuyo TITULO, separado del autor, es prefijo del otro).
#        El primer criterio del auditor comparaba el segmento entero con el
#        autor pegado y dio CERO: error propio, declarado en el acta. --------
def partes(seg):
    t, _, a = seg.rpartition(" - ")
    return (t or seg).strip().lower(), a.strip().lower()

dobles = []
for nid, nd in sorted(vivos.items()):
    ps = [partes(s) for s in segmentos(nd)]
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            corto, largo = sorted([ps[i][0], ps[j][0]], key=len)
            if corto and largo.startswith(corto):
                dobles.append((nid, ps[i][0], ps[j][0]))
print(f"\nnodos con el mismo libro dos veces (titulos, prefijo): {len(dobles)}")
for nid, a, b in dobles:
    print(f"  {nid}: [{a}] / [{b}]")

# --- 7. metas_vs_proposito: posicion del bloque -----------------------------
segs = segmentos(nodos["metas_vs_proposito"])
print(f"\nmetas_vs_proposito: {len(segs)} segmentos; Horowitz en posiciones "
      f"{[i + 1 for i, s in enumerate(segs) if HOR.search(s)]}; "
      f"ultimo = {segs[-1]}")
enmedio = [nid for nid in n13
           if (lambda ss: any(HOR.search(s) for s in ss)
               and not HOR.search(ss[-1]))(segmentos(nodos[nid]))]
print(f"de los 13, con Horowitz declarado y NO ultimo: {enmedio}")

# --- 8. Los pasos de los tres casos (HEAD y blob del 11 ago) ----------------
for nid in ["decision_de_vender_startup", "viral_loop_marketing",
            "coeficiente_viral"]:
    print(f"{nid}: {len(nodos[nid]['pasos_accionables'])} pasos (HEAD)")
blob = subprocess.run(
    ["git", "show", "23f9ac32:dataset/metadata/master_graph.json"],
    capture_output=True).stdout.decode("utf-8")
g11 = json.loads(blob)["nodos"]
print("decision_de_vender_startup en blob 23f9ac32:",
      len(g11["decision_de_vender_startup"]["pasos_accionables"]), "pasos")

# --- 9. Guiones largos y medios en las rutas tocadas ------------------------
rutas = ["docs/plan/01_FUENTES.md", "docs/plan/OPERACIONES.jsonl",
         "docs/plan/RECOMPUTO_3388.md", "scripts/loop/vuelta21_registros.py",
         "scripts/loop/vuelta21_tarea1.py",
         "scripts/loop/vuelta21_fase0_sitios.py"]
print()
for r in rutas:
    t = open(r, encoding="utf-8").read()
    print(f"guiones {r}: largos={t.count(chr(0x2014))} medios={t.count(chr(0x2013))}")

# --- 10. LO QUE OP-C-04 ENCONTRARIA HOY. Auto-aristas tras resolver, con el
#         mecanismo real del motor (ids_alias, reimplementado de graph.ts) ---
alias = {}
for nid, nd in nodos.items():
    for a in nd.get("ids_alias") or []:
        if a != nid:
            alias[a] = nid

def resolver(nid):
    nd = nodos.get(nid)
    if nd is not None and not nd.get("deprecado"):
        return nid
    visto = {nid}
    cur = nid
    ultimo = nid if nd is not None else None
    while cur in alias:
        cur = alias[cur]
        if cur in visto:
            break
        visto.add(cur)
        c = nodos.get(cur)
        if c is None:
            continue
        ultimo = cur
        if not c.get("deprecado"):
            return cur
    return ultimo

auto = []
for nid, nd in nodos.items():
    if nd.get("deprecado"):
        continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        for d in nd.get(campo) or []:
            if resolver(d) == nid:
                auto.append((nid, campo, d))
peor = Counter(n for n, _, _ in auto)
print(f"\nauto-aristas tras resolver, HOY, en vivos: {len(auto)} aristas "
      f"sobre {len(peor)} nodos; el peor: {peor.most_common(1)}")
directas = sum(1 for nid, _, d in auto if d == nid)
print(f"de ellas, directas (id igual a id): {directas}")

# --- 11. LO QUE LA LISTA BLANCA DE CLAVES ENCONTRARIA HOY -------------------
STD = {"node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
       "resumen_teorico", "pasos_accionables", "entregable_esperado",
       "nodos_previos", "nodos_siguientes", "condiciones_activacion",
       "etiqueta_arbol", "ids_alias", "deprecado"}
raras = {}
for nid, nd in nodos.items():
    for k in set(nd) - STD:
        raras.setdefault(k, []).append(nid)
print("claves fuera del esquema estandar de doce mas ids_alias/deprecado:")
for k, quien in sorted(raras.items(), key=lambda x: -len(x[1])):
    print(f"  {k}: {len(quien)} nodos -> {sorted(quien)[:4]}"
          f"{' ...' if len(quien) > 4 else ''}")
