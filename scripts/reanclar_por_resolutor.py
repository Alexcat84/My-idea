#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-ancla por el RESOLUTOR DE LA HISTORIA lo que apunta a un nodo absorbido.

POR QUE EXISTE. Al fundir el nucleo (Fase 3 de la curacion, ago 2026) el primer
lote rompio un puente aprobado de franquicias: su ancla en el nucleo se habia
fusionado. El Gate 0 lo cazo, que para eso esta, pero arreglarlo a mano lote por
lote es como cazar el mismo pez cuatro veces.

QUE TOCA, y solo esto:
  1. las anclas de los puentes aprobados de cada pack (packs/*/metadata/
     bridges_aprobados.json),
  2. las anclas del banco de rumbos (scripts/rumbos/banco_rumbos.json).

QUE NO TOCA: los nodos. Ni uno. Esto mueve REFERENCIAS, no contenido.

LA REGLA: se apunta al SUPERVIVIENTE, que es el mismo concepto con las piezas de
los dos. El id viejo queda anotado (`ancla_original`) para que la historia siga
contando de donde venia. Es la misma ley que ya se aplico a 22 puentes en el
ciclo del censo, ahora hecha herramienta en vez de faena.

Uso:
  python scripts/reanclar_por_resolutor.py --dry-run
  python scripts/reanclar_por_resolutor.py
"""
import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
# SE LEE DE dataset/nodos/, NO del master_graph compilado. El compilado lo
# regenera run_phase1, asi que dependiendo de el esta herramienta solo funciona
# si alguien la corre en el orden correcto -- y la primera vez se corrio en el
# orden equivocado, leyo un grafo viejo y dijo "nada que re-anclar" con dos
# puentes rotos delante. La verdad de si un nodo esta deprecado vive en su
# archivo; leerla ahi hace la herramienta inmune al orden.
NODOS = BASE / "dataset" / "nodos"
BANCO = BASE / "scripts" / "rumbos" / "banco_rumbos.json"


def cargar_resolutor():
    """Devuelve resolver(id) -> id vigente. Espejo exacto de resolverId en
    web/lib/engine/graph.ts: se camina la cadena, y si la cadena entera se
    retiro de la seleccion, el eslabon mas RECIENTE que exista."""
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
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    resolver, g = cargar_resolutor()
    cambios = []

    for p in sorted((BASE / "packs").glob("*/metadata/bridges_aprobados.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        tocado = False
        for x in d.get("aprobados", []):
            r = resolver(x["core"])
            if r and r != x["core"]:
                cambios.append(("puente", p.parts[-3], x["core"], r, g[r]["titulo_concepto"]))
                if not args.dry_run:
                    x.setdefault("ancla_original", x["core"])
                    x["core"] = r
                    tocado = True
        if tocado:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")

    b = json.loads(BANCO.read_text(encoding="utf-8"))
    tocado = False
    for r_ in b["rumbos"]:
        for campo in ("ancla", "ancla_conjunto"):
            for i, a in enumerate(r_.get(campo) or []):
                nuevo = resolver(a)
                if nuevo and nuevo != a:
                    cambios.append(("rumbo", r_["id"], a, nuevo, g[nuevo]["titulo_concepto"]))
                    if not args.dry_run:
                        r_[campo][i] = nuevo
                        tocado = True
    if tocado:
        BANCO.write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if not cambios:
        print("  nada que re-anclar: ninguna referencia apunta a un absorbido.")
        return 0
    for tipo, quien, viejo, nuevo, titulo in cambios:
        print(f"  [{tipo}] {quien}: {viejo} -> {nuevo}  ({titulo})")
    print(f"  {len(cambios)} referencias re-ancladas"
          f"{' (DRY RUN: no se escribio nada)' if args.dry_run else ''}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
