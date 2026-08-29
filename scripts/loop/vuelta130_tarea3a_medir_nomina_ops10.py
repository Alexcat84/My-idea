#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vuelta130_tarea3a_medir_nomina_ops10.py . MIDE, NO ESCRIBE.

Resuelve los 31 ids del campo `nodos` de OP-S-10 (docs/plan/OPERACIONES.jsonl)
por el resolutor de la historia (P.1, docs/plan/BANCO_DEL_PLAN.md:11), espejo
del mismo resolutor de scripts/reanclar_por_resolutor.py: camina `ids_alias`
leido de dataset/nodos/*.json, y si la cadena entera se deprecara, se queda en
el ultimo eslabon vivo o, si no hay ninguno vivo, en el ultimo eslabon visto.

Sobre los ids VIVOS DISTINTOS que resulten, mira cuales NO nombran el pais
("Estados Unidos") en `condiciones_activacion`.

USO:
  python scripts/loop/vuelta130_tarea3a_medir_nomina_ops10.py
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
NODOS = BASE / "dataset" / "nodos"
OPERACIONES = BASE / "docs" / "plan" / "OPERACIONES.jsonl"


def cargar_resolutor():
    g = {}
    for p in NODOS.glob("*.json"):
        n = json.loads(p.read_text(encoding="utf-8"))
        g[n["node_id"]] = n
    alias = {}
    for nid, v in g.items():
        for a in v.get("ids_alias") or []:
            if a != nid:
                alias[a] = nid

    def resolver(n):
        v = g.get(n)
        if v and not v.get("deprecado"):
            return n
        visto, cur = {n}, n
        ultimo = n if v else None
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = g.get(cur)
            if not c:
                continue
            ultimo = cur
            if not c.get("deprecado"):
                return cur
        return ultimo

    return resolver, g


def main():
    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    ops10 = next(o for o in ops if o["id_op"] == "OP-S-10")
    nomina = ops10["nodos"]
    print(f"NOMINA OP-S-10: {len(nomina)} ids")

    resolver, g = cargar_resolutor()
    resueltos = []
    for nid in nomina:
        r = resolver(nid)
        resueltos.append((nid, r))

    vivos = []
    vistos = set()
    for orig, r in resueltos:
        if r and r in g and not g[r].get("deprecado"):
            if r not in vistos:
                vistos.add(r)
                vivos.append(r)

    print(f"RESUELTOS A VIVOS DISTINTOS: {len(vivos)}")
    movidos = [(o, r) for o, r in resueltos if o != r]
    print(f"IDS QUE EL RESOLUTOR MUEVE ({len(movidos)}):")
    for o, r in movidos:
        print(f"  {o} -> {r}")

    print()
    print("SOBRE LOS VIVOS, QUIEN NOMBRA 'Estados Unidos' EN condiciones_activacion:")
    cubiertos = []
    no_cubiertos = []
    for nid in vivos:
        n = g[nid]
        cond = n.get("condiciones_activacion") or []
        nombra = any("Estados Unidos" in c for c in cond)
        (cubiertos if nombra else no_cubiertos).append(nid)

    print(f"CUBIERTOS (nombran el pais en condiciones_activacion): {len(cubiertos)}")
    for nid in cubiertos:
        print(f"  {nid}")
    print(f"NO CUBIERTOS: {len(no_cubiertos)}")
    for nid in no_cubiertos:
        n = g[nid]
        print(f"  {nid}")
        print(f"    condiciones_activacion actuales: {n.get('condiciones_activacion')}")

    print()
    print(f"RESUMEN: nomina {len(nomina)}, vivos distintos {len(vivos)}, "
          f"cubiertos {len(cubiertos)}, no_cubiertos {len(no_cubiertos)}")


if __name__ == "__main__":
    raise SystemExit(main())
