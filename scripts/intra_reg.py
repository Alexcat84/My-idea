# -*- coding: utf-8 -*-
"""intra_reg.py archivo.txt - registra veredictos del cribado intra-dominio.

Cada linea del archivo de entrada es: PUESTO CLASE razon

Comprueba antes de escribir que el puesto existe en la cola, que no estaba ya
registrado, que la clase es A, B, C o D y que la razon no esta vacia. Falla
RUIDOSO en cualquiera de los cuatro casos: un veredicto mal registrado es peor
que uno no registrado, porque el archivo es la unica prueba de que un par se
leyo.

Vive en scripts/ y no en un temporal porque el cribado se reanuda entre
sesiones.

Uso:
  python scripts/intra_reg.py lote.txt
"""
import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
SAL = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
P = {p["puesto_intra"]: p for p in (json.loads(l) for l in open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip())}
ya = {}
if os.path.exists(SAL):
    ya = {v["puesto_intra"]: v for v in (json.loads(l) for l in open(SAL, encoding="utf-8") if l.strip())}

nuevas = []
for ln, linea in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    linea = linea.strip()
    if not linea:
        continue
    a, b, razon = linea.split(" ", 2)
    pu, clase = int(a), b.upper()
    assert pu in P, "linea %d: el puesto %d no esta en la cola" % (ln, pu)
    assert pu not in ya, "linea %d: el puesto %d YA esta registrado" % (ln, pu)
    assert clase in ("A", "B", "C", "D"), "linea %d: clase %r invalida" % (ln, clase)
    assert len(razon.strip()) > 15, "linea %d: razon demasiado corta" % ln
    p = P[pu]
    nuevas.append({
        "puesto_intra": pu, "dominio": p["dominio"],
        "nodo_a": p["nodo_a"], "nodo_b": p["nodo_b"],
        "clave": round(max(p["sim_semantica"], p["sim_titulo"] / 100), 4),
        "banda_078_080": p["banda_078_080"],
        "clase": clase, "razon": razon.strip(),
    })
    ya[pu] = True

with open(SAL, "a", encoding="utf-8", newline="\n") as fh:
    for v in nuevas:
        fh.write(json.dumps(v, ensure_ascii=False) + "\n")
tot = sum(1 for _ in open(SAL, encoding="utf-8"))
print("registradas %d | total %d de %d" % (len(nuevas), tot, len(P)))
