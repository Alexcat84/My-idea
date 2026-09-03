# AUDITOR VUELTA 160: relectura CIEGA. Imprime SOLO titulo, fuente, entregable y
# pasos accionables de los dos nodos. Sin clase, sin via, sin cita y sin razon.
import json, re, sys, pathlib
R = pathlib.Path(".")
g = json.loads((R/"dataset/metadata/master_graph.json").read_text(encoding="utf-8"))["nodos"]
reg = [json.loads(l) for l in (R/"docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
por_ld = {}
for e in reg:
    m = re.match(r"(LD-OPC05-\d+)", e["cita"])
    if m: por_ld[m.group(1)] = e

def pinta(nid):
    n = g.get(nid)
    if not n:
        print(f"  [NODO AUSENTE: {nid}]"); return
    print(f"  NODO: {nid}")
    print(f"  titulo   : {n.get('titulo_concepto')}")
    print(f"  fuente   : {n.get('fuente')}")
    print(f"  entregable: {n.get('entregable_esperado')}")
    print("  pasos:")
    for i, p in enumerate(n.get("pasos_accionables") or [], 1):
        print(f"     {i}. {p}")

for ld in sys.argv[1:]:
    e = por_ld[ld]
    print("=" * 78)
    print(ld)
    print("=" * 78)
    pinta(e["nodo_a_leido"]); print("  " + "-"*70); pinta(e["nodo_b_leido"])
    print()
