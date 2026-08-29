# -*- coding: utf-8 -*-
"""vuelta123_tarea2d_censo_alias.py . Remide, para la adjudicacion 2.d del
encargo de la vuelta 123, el censo de alias sobre la fuente canonica del
resolutor (ids_alias embebido en cada nodo de dataset/metadata/
master_graph.json, la misma fuente que mapaDeAlias en web/lib/engine/
graph.ts y su espejo scripts/reanclar_por_resolutor.py) y sobre los cuatro
alias_map_*.json de dataset/metadata/, POR CORRIDA PROPIA, no copiado del
acta de la vuelta 122.

USO:
  python scripts/loop/vuelta123_tarea2d_censo_alias.py
"""
import glob
import json
import os

RAIZ = "C:/Users/AlexDesk/Documents/I have an idea"


def censo_fuente_canonica():
    """CLASIFICA POR EL DUENO (nid), no por si la CLAVE del alias coincide con
    algun id de nodo: resolverId(alias) devuelve el id del nodo que RECLAMA
    ese alias en su propio ids_alias (el nid que itera el bucle de abajo), y
    ESE es el que puede ser vivo o deprecado. Clasificar por si la clave del
    alias coincide con un id de nodo cualquiera es una pregunta distinta y
    sin sentido para el resolutor (hallado al probar este script contra el
    acta de la vuelta 122: la primera version daba 0 a_vivo, 665 a_deprecado,
    77 huerfanas, y las tres estaban midiendo la cosa equivocada)."""
    with open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8") as f:
        master = json.load(f)
    nodos = master["nodos"] if isinstance(master, dict) and "nodos" in master else master
    vivos = {nid for nid, n in nodos.items() if not n.get("deprecado")}
    duenos = {}
    auto = 0
    entradas = 0
    for nid, n in nodos.items():
        for a in (n.get("ids_alias") or []):
            if a == nid:
                auto += 1
                continue
            entradas += 1
            duenos.setdefault(a, []).append(nid)
    colisiones = {a: d for a, d in duenos.items() if len(d) > 1}
    dueno_vivo = sum(1 for a, ds in duenos.items() for nid in ds if nid in vivos)
    dueno_deprecado = sum(1 for a, ds in duenos.items() for nid in ds if nid not in vivos)
    huerfanas = sum(1 for a, ds in duenos.items() for nid in ds if nid not in nodos)
    return {
        "entradas": entradas,
        "auto_alias_excluidos": auto,
        "colisiones": len(colisiones),
        "a_vivo": dueno_vivo,
        "a_deprecado": dueno_deprecado,
        "huerfanas": huerfanas,
        "huerfanas_lista": [],
    }


def censo_alias_map_files():
    with open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8") as f:
        master = json.load(f)
    nodos = master["nodos"] if isinstance(master, dict) and "nodos" in master else master
    vivos = {nid for nid, n in nodos.items() if not n.get("deprecado")}

    rutas = sorted(glob.glob(os.path.join(RAIZ, "dataset", "metadata", "alias_map_*.json")))
    union = {}
    for ruta in rutas:
        with open(ruta, encoding="utf-8") as f:
            d = json.load(f)
        for k, v in d.items():
            if k not in union:
                union[k] = v
    huerfanos = sorted(k for k, v in union.items() if v not in nodos)
    a_deprecado = sum(1 for k, v in union.items() if v in nodos and v not in vivos)
    return {
        "ficheros": [os.path.basename(r) for r in rutas],
        "claves_unicas": len(union),
        "huerfanos": len(huerfanos),
        "huerfanos_lista": huerfanos,
        "a_deprecado": a_deprecado,
    }


def main():
    print("=== FUENTE CANONICA (ids_alias embebido, resolutor real) ===")
    c = censo_fuente_canonica()
    print(json.dumps({k: v for k, v in c.items() if k != "huerfanas_lista"}, ensure_ascii=False, indent=2))
    print("huerfanas_lista:", c["huerfanas_lista"])

    print("\n=== ALIAS_MAP_*.json (union, primera ocurrencia gana) ===")
    m = censo_alias_map_files()
    print(json.dumps(m, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
