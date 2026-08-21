# -*- coding: utf-8 -*-
"""vuelta64_puesto2.py . TALLA LA TABLA DE DESBLOQUEOS DEL PUESTO 2 DE LA FASE
03, QUE ES LA VARA GENERAL DE LA VUELTA 47, Y LA MIDE POR CAMINO PROPIO.

LA TABLA SE IMPRIME, NO SE TECLEA (regla 1). El registro de la TAREA 1.a pega la
salida de tabla_markdown() entera en vez de reteclear las celdas, que es
exactamente la especie de caida de las vueltas 31, 32, 54, 55 y 56.

QUE SE MIDE, todo de docs/plan/OPERACIONES.jsonl y nada de un acta:
  a) las operaciones de fase 03_FUSIONES con campo orden == 2, que son las
     empatadas en el puesto;
  b) para cada una, CUANTAS operaciones la nombran en su depende_de, que es lo
     que la vara de la vuelta 47 llama DESBLOQUEAR;
  c) si la operacion esta CONSUMIDA hoy (su par resuelve a un solo vivo por
     P.1), leido de la misma medicion de scripts/loop/vuelta64_consumidas.py
     para las cinco que le tocan, y medido aqui para las demas.

Uso: python scripts/loop/vuelta64_puesto2.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def medir():
    ops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    nodos = {}
    for f in os.listdir(NODOS):
        if f.endswith(".json"):
            j = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
            nodos[j.get("node_id") or f[:-5]] = j
    alias = {}
    for nid, j in nodos.items():
        for a in (j.get("ids_alias") or []):
            alias.setdefault(a, nid)

    def resolver(n):
        visto = set()
        while n in alias and n not in visto:
            visto.add(n)
            n = alias[n]
        return n

    cand = [o for o in ops
            if o.get("fase") == "03_FUSIONES" and o.get("orden") == 2]
    filas = []
    for c in cand:
        dep = [o["id_op"] for o in ops if c["id_op"] in (o.get("depende_de") or [])]
        ns = [n for n in (c.get("nodos") or []) if n in nodos]
        res = sorted({resolver(n) for n in ns})
        filas.append({
            "id_op": c["id_op"],
            "desbloquea": len(dep),
            "cuales": dep,
            "miembros": len(c.get("nodos") or []),
            "resueltos": len(res),
            "consumida": len(res) == 1 and len(c.get("nodos") or []) > 1,
        })
    filas.sort(key=lambda f: (-f["desbloquea"], f["id_op"]))
    return filas, len(ops)


def tabla_markdown(filas):
    nl = chr(10)
    out = ["| puesto | operacion | **desbloquea** | cuales, leidas de su `depende_de` | estado HOY |",
           "|---:|---|---:|---|---|"]
    for k, f in enumerate(filas, 1):
        out.append("| **%d.a** | `%s` | **%d** | %s | %s |"
                   % (k, f["id_op"], f["desbloquea"],
                      ", ".join("`%s`" % x for x in f["cuales"]) or "ninguna",
                      "**CONSUMIDA**, su par ya resuelve a un solo vivo"
                      if f["consumida"] else
                      ("ejecutable; **SIN nomina de nodos en su ficha**, su universo "
                       "se abre aparte" if not f["miembros"] else
                       "ejecutable, %d miembros a %d vivos"
                       % (f["miembros"], f["resueltos"]))))
    return nl.join(out)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas, n = medir()
    print("=" * 78)
    print("EL PUESTO 2 DE LA FASE 03, MEDIDO CON LA VARA GENERAL DE LA VUELTA 47")
    print("  fichas leidas de docs/plan/OPERACIONES.jsonl: %d" % n)
    print("  empatadas por el campo orden == 2 en fase 03_FUSIONES: %d" % len(filas))
    print("=" * 78)
    print()
    for f in filas:
        print("  %-18s desbloquea %d %s | %s"
              % (f["id_op"], f["desbloquea"], f["cuales"],
                 "CONSUMIDA" if f["consumida"] else
                 ("ejecutable, SIN nomina de nodos en su ficha" if not f["miembros"]
                  else "ejecutable, %d miembros a %d vivos"
                  % (f["miembros"], f["resueltos"]))))
    print()
    print("--- LA TABLA, PARA PEGARLA ENTERA ---")
    print(tabla_markdown(filas))
    print()
    ejecutables = [f for f in filas if not f["consumida"]]
    if not ejecutables:
        print("ROJO: no queda ninguna ejecutable en el puesto 2. PARADA.")
        return 1
    print("  LA PRIMERA EJECUTABLE DEL PUESTO: %s (desbloquea %d)"
          % (ejecutables[0]["id_op"], ejecutables[0]["desbloquea"]))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
