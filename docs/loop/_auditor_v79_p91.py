"""Auditor v79: re-corrida propia del filtro P.9.1 ensanchado sobre la bolsa de 259."""
import json, sys

ops = [json.loads(l) for l in open("docs/plan/OPERACIONES.jsonl", encoding="utf-8") if l.strip()]
no_ej = [o for o in ops if o.get("estado") != "HECHA"]
elim, surv, ren = set(), set(), set()
for o in no_ej:
    for x in (o.get("eliminar") or []): elim.add(x)
    s = o.get("superviviente")
    if s: surv.add(s)
    if o.get("tipo") == "RENOMBRE_CON_ALIAS":
        for x in (o.get("nodos") or []): ren.add(x)
print(f"operaciones totales {len(ops)} | NO EJECUTADAS {len(no_ej)}")
print(f"ids en eliminar: {len(elim)} | en superviviente: {len(surv)} | en nodos de RENOMBRE_CON_ALIAS: {len(ren)}")

G = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
vivo = lambda n: n in G and not G[n].get("deprecado")

paresA = set()
for l in open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8"):
    l = l.strip()
    if not l: continue
    o = json.loads(l)
    if o["clase"] == "A" and vivo(o["nodo_a"]) and vivo(o["nodo_b"]):
        paresA.add(o["nodo_a"]); paresA.add(o["nodo_b"])
print(f"nodos VIVOS en al menos un veredicto A vivo: {len(paresA)}")

bolsa = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
sinA = [f for f in bolsa if not f.get("arista")]
print(f"bolsa reducida {len(bolsa)} | sin arista {len(sinA)}")

op_ids = elim | surv | ren
apart, solo_op, con_A, limpios = 0, 0, 0, []
for f in sinA:
    m, h = f["madre"], f["hijo"]
    por_op = (m in op_ids) or (h in op_ids)
    por_A = (m in paresA) or (h in paresA)
    if por_op or por_A:
        apart += 1
        if por_A: con_A += 1
        else: solo_op += 1
    else:
        limpios.append((m, h, f.get("paso_n")))
print(f"APARTADOS por P.9.1 ensanchado: {apart} | solo por operacion: {solo_op} | con motivo de la vara de los A: {con_A}")
print(f"LIMPIOS: {len(limpios)}")

fich = [json.loads(l) for l in open("docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl", encoding="utf-8") if l.strip()]
mio = set((a, b) for a, b, _ in limpios)
suyo = set((f["madre"], f["hijo"]) for f in fich)
print(f"\nCOTEJO FILA A FILA contra PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl ({len(fich)} filas)")
print(f"  mias de mas: {len(mio - suyo)} {sorted(mio - suyo)[:5]}")
print(f"  suyas de mas: {len(suyo - mio)} {sorted(suyo - mio)[:5]}")
print(f"  COINCIDEN: {len(mio & suyo)} de {len(mio)}")

# guarda del par no dirigido sobre las limpias
from collections import Counter
nd = Counter(frozenset((a, b)) for a, b, _ in limpios)
par = [k for k, v in nd.items() if v > 1]
print(f"\nGUARDA DEL PAR NO DIRIGIDO sobre las limpias: {len(par)} pareja(s) {[sorted(p) for p in par]}")
