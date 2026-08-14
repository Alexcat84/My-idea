# -*- coding: utf-8 -*-
"""Instrumento del AUDITOR, vuelta 20. SOLO LECTURA.

Recomputa desde los archivos, sin copiar nada de reportes ni actas:
  1. el marcador A/B/C/D y los puestos (huecos y duplicados)
  2. la tasa por dominio
  3. el inventario: entradas, tipos, actos vigentes CERRADOS/ABIERTOS
  4. la deuda de P.5 por las dos rutas (nota y cobertura)
  5. el diff del inventario contra 5a7b7d60 se corre aparte con git
"""
import json, re, sys, io
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
INVENTARIO = "docs/plan/INVENTARIO.jsonl"

# 1 y 2: marcador y dominios
rows = []
with open(VEREDICTOS, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

print(f"veredictos: {len(rows)} lineas")
clases = Counter(r["clase"] for r in rows)
print("marcador:", dict(sorted(clases.items())))
puestos = [r["puesto_intra"] for r in rows]
setp = set(puestos)
print(f"puestos unicos: {len(setp)}; min {min(setp)}; max {max(setp)}; "
      f"huecos: {len(set(range(1, 3389)) - setp)}; duplicados: {len(puestos) - len(setp)}")

dom = {}
for r in rows:
    d = dom.setdefault(r["dominio"], [0, 0])
    d[0] += 1
    if r["clase"] == "A":
        d[1] += 1
for k in sorted(dom):
    n, a = dom[k]
    print(f"  {k:20s} {n:5d} pares  A={a:4d}  tasa={100.0*a/n:.1f}%")

# 3 y 4: inventario
inv = []
with open(INVENTARIO, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            inv.append(json.loads(line))
print(f"\ninventario: {len(inv)} entradas")
tipos = Counter(e.get("tipo") for e in inv)
print("tipos:", dict(sorted(tipos.items())))

actos = [e for e in inv if e.get("tipo") == "acto"]
sup = [e for e in actos if "SUPERADA" in json.dumps(e, ensure_ascii=False).upper()]
# estado de vigentes
vig = [e for e in actos if e not in sup]
est = Counter(e.get("estado") for e in vig)
print(f"actos: {len(actos)} total; superadas {len(sup)}; vigentes {len(vig)}")
print("estado de vigentes:", dict(sorted(est.items(), key=lambda x: str(x[0]))))

# deuda P.5 ruta A: campo cobertura "X en cola" / "X fuera de cola" -> pendientes
# La deuda son pares aun sin leer de actos vigentes; se extrae del campo cobertura
# con el patron "N de M pares leidos" -> M - N, mas lo que declare "fuera de cola".
deuda_cob = 0
sin_patron = 0
for e in vig:
    cob = e.get("cobertura", "") or ""
    m = re.search(r"(\d+)\s+de\s+(\d+)\s+pares\s+leidos", cob)
    if m:
        deuda_cob += int(m.group(2)) - int(m.group(1))
    else:
        sin_patron += 1
print(f"deuda P.5 via cobertura: {deuda_cob} pares  (entradas sin patron: {sin_patron})")

# deuda P.5 ruta B: campo nota con "quedan N" o "N pendientes" es fragil; en su lugar
# reusamos el patron de pares en el propio campo nota si existe
deuda_nota = 0
sin_patron_n = 0
for e in vig:
    nota = e.get("nota", "") or ""
    m = re.search(r"(\d+)\s+de\s+(\d+)\s+pares\s+leidos", nota)
    if m:
        deuda_nota += int(m.group(2)) - int(m.group(1))
    else:
        sin_patron_n += 1
print(f"deuda P.5 via nota:      {deuda_nota} pares  (entradas sin patron: {sin_patron_n})")

# figuras
figs = [e for e in inv if e.get("tipo") == "figura"]
print(f"\nfiguras: {len(figs)}")
con_tanda = [e for e in figs if re.search(r"nombrad[ao]s? en (?:la )?(?:tanda|vuelta)", json.dumps(e, ensure_ascii=False), re.I)]
print(f"figuras con marca 'nombrad* en tanda/vuelta': {len(con_tanda)}")

# el acto del sales roadmap y el racimo homonimo
for e in inv:
    txt = json.dumps(e, ensure_ascii=False)
    if "sales_roadmap" in txt.lower() or "sales roadmap" in txt.lower():
        print(f"\n[{e.get('tipo')}] {e.get('nombre', e.get('id', '?'))}: "
              f"estado={e.get('estado')!r} cobertura={str(e.get('cobertura'))[:120]!r}")
