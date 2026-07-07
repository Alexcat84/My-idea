#!/usr/bin/env python3
"""
hotfix_v2_1_1_add_dominio.py - Groundwork de dominios (Hotfix motor-v2.1.1).

Agrega "dominio": "core" a todos los nodos de dataset/nodos/ que aun no
tengan ese campo. Es un cambio puramente aditivo (no toca titulo_concepto,
resumen_teorico, pasos_accionables, ni las referencias nodos_previos/
nodos_siguientes) - preparacion para filtrar por dominios desbloqueados en
el ruteador, la brujula y la cosecha en fases futuras. Hoy todos los
proyectos tienen ["core"] desbloqueado por defecto, asi que este cambio no
altera ningun comportamiento observable.

Correr una sola vez, luego scripts/run_phase1.py para recompilar
master_graph.json y validar Gate 0 (que ahora exige "dominio" valido en
todos los nodos).

Uso: python scripts/hotfix_v2_1_1_add_dominio.py
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NODOS_DIR = BASE / "dataset" / "nodos"

DOMINIO_POR_DEFECTO = "core"


def main():
    actualizados = 0
    ya_tenian = 0
    for path in sorted(NODOS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if "dominio" in data:
            ya_tenian += 1
            continue
        # "dominio" va justo despues de "fase_proyecto" para mantener el
        # mismo orden de lectura que el resto de los archivos del dataset.
        nuevo = {}
        insertado = False
        for k, v in data.items():
            nuevo[k] = v
            if k == "fase_proyecto":
                nuevo["dominio"] = DOMINIO_POR_DEFECTO
                insertado = True
        if not insertado:
            nuevo["dominio"] = DOMINIO_POR_DEFECTO
        path.write_text(json.dumps(nuevo, ensure_ascii=False, indent=2), encoding="utf-8")
        actualizados += 1

    print(f"Nodos actualizados con dominio='{DOMINIO_POR_DEFECTO}': {actualizados}")
    print(f"Nodos que ya tenian dominio: {ya_tenian}")
    print(f"Total: {actualizados + ya_tenian}")


if __name__ == "__main__":
    main()
