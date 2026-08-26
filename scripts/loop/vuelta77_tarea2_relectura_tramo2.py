"""VUELTA 77, TAREA 2: relectura al doble del tramo 2 de OP-E-01 (AUDITOR.md
seccion 1.2, disparada porque la segunda caida de la vuelta 76 cayo FUERA
del marcado), con la vara que la parada del 26 ago 2026 encontro: cruzar
las 26 aristas del tramo 2 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl
(fuente de verdad por AUDITOR.md seccion 0) y publicar, par a par, si el
cribado ya habia leido ese par y con que clase. Cualquier par que el
cribado haya fallado A y este escrito se revierte con correccion declarada.

Los 26 pares vienen de PARES_SANOS en
scripts/loop/vuelta76_op_e01_tramo2_escribir.py (import directo, no se
retranscribe la lista a mano).
"""
import json
import importlib.util
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"

spec = importlib.util.spec_from_file_location(
    "vuelta76_op_e01_tramo2_escribir",
    RAIZ / "scripts" / "loop" / "vuelta76_op_e01_tramo2_escribir.py",
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
PARES_SANOS = mod.PARES_SANOS


def main():
    veredictos_por_par = {}
    with open(VEREDICTOS, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            v = json.loads(linea)
            a, b = v["nodo_a"], v["nodo_b"]
            veredictos_por_par[frozenset((a, b))] = v

    print(f"PARES DEL TRAMO 2: {len(PARES_SANOS)}")
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
    print(f"CLASE A del cribado y escritos como enlace (A REVERTIR): {len(revertir)}")
    for m, h, v in revertir:
        print(f"  {m} -> {h} (puesto {v['puesto_intra']}, razon: {v['razon']})")


if __name__ == "__main__":
    main()
