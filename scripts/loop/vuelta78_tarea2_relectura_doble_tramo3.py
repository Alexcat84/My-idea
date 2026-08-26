"""VUELTA 78, TAREA 2: LA RELECTURA AL DOBLE DEL TRAMO 3 (credito rebajado,
AUDITOR.md seccion 1.2, disparado porque las dos caidas de reporte de la
vuelta 77 cayeron FUERA de los discutibles marcados). Cruza las 28 aristas
del tramo 3 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl y publica, par a
par, si el cribado ya habia leido ese par y con que clase. Cualquier par
fallado A y escrito se revierte con correccion declarada.

Los 28 pares vienen de PARES_SANOS en scripts/loop/vuelta77_tramo3_escribir.py
(import directo, no se retranscribe la lista a mano).
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta77_tramo3_escribir import PARES_SANOS  # noqa: E402


def main():
    assert len(PARES_SANOS) == 28, f"esperaba 28 pares, hay {len(PARES_SANOS)}"

    veredictos_por_par = {}
    with open(VEREDICTOS, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            v = json.loads(linea)
            a, b = v["nodo_a"], v["nodo_b"]
            veredictos_por_par[frozenset((a, b))] = v

    print(f"PARES DEL TRAMO 3: {len(PARES_SANOS)}")
    print()

    leidos = []
    no_leidos = []
    revertir = []
    for madre, hijo, _razon in PARES_SANOS:
        clave = frozenset((madre, hijo))
        v = veredictos_por_par.get(clave)
        if v is None:
            no_leidos.append((madre, hijo))
            print(f"{madre} -> {hijo}: NUNCA LEIDO por el cribado")
            continue
        leidos.append((madre, hijo, v))
        print(f"{madre} -> {hijo}: LEIDO, puesto {v['puesto_intra']}, clase {v['clase']}")
        if v["clase"] == "A":
            revertir.append((madre, hijo, v))

    print()
    print(f"LEIDOS por el cribado: {len(leidos)} de {len(PARES_SANOS)}")
    print(f"NUNCA LEIDOS por el cribado: {len(no_leidos)} de {len(PARES_SANOS)}")
    print(f"clase D (de los leidos): {sum(1 for _,_,v in leidos if v['clase']=='D')}")
    print(f"clase A (de los leidos): {sum(1 for _,_,v in leidos if v['clase']=='A')}")
    print(f"CLASE A del cribado y escritos como enlace (A REVERTIR): {len(revertir)}")
    for m, h, v in revertir:
        print(f"  {m} -> {h} (puesto {v['puesto_intra']}, razon: {v['razon']})")


if __name__ == "__main__":
    main()
