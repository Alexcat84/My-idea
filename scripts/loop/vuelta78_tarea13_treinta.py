"""VUELTA 78, TAREA 1.3: recuenta por corrida propia cuantos de los 30
candidatos del tramo 3 (28 escritas + 2 pendientes, vuelta 77) tenian
veredicto propio en docs/INTRA_DOMINIO_VEREDICTOS.jsonl, para corregir la
cifra "4 de 30" del REPORTE.md seccion 3.3 (caida de reporte, acta 77
seccion 4.1). Importa la lista de pares directo de
scripts/loop/vuelta77_tramo3_escribir.py, sin retranscribirla a mano
(EJECUTOR.md regla 1, LA TABLA SE CUENTA DE SU FICHERO).

El cribado lee PARES, no aristas dirigidas: por eso el conteo principal
empareja SIN DIRECCION (igual que hace el auditor en su acta 77 seccion
4.1), y se publica ademas el conteo en direccion madre->hijo solamente,
como contraste.
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta77_tramo3_escribir import PARES_SANOS, PARES_DESCARTADOS  # noqa: E402

TREINTA = [(m, h) for m, h, _ in PARES_SANOS] + [(m, h) for m, h, _ in PARES_DESCARTADOS]
assert len(TREINTA) == 30, f"esperaba 30 candidatos, hay {len(TREINTA)}"


def main():
    veredictos_sin_direccion = {}
    veredictos_dirigidos = {}
    with open(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") as f:
        for l in f:
            if not l.strip():
                continue
            d = json.loads(l)
            a, b = d.get("nodo_a"), d.get("nodo_b")
            veredictos_sin_direccion.setdefault(frozenset((a, b)), []).append(d)
            veredictos_dirigidos.setdefault((a, b), []).append(d)

    sin_direccion = []
    dirigido = []
    for madre, hijo in TREINTA:
        vs = veredictos_sin_direccion.get(frozenset((madre, hijo)))
        if vs:
            sin_direccion.append((madre, hijo, vs))
        vd = veredictos_dirigidos.get((madre, hijo))
        if vd:
            dirigido.append((madre, hijo, vd))

    print(f"CANDIDATOS DEL TRAMO 3: {len(TREINTA)} (28 escritas + 2 pendientes)")
    print()
    print(f"CON VEREDICTO PROPIO, SIN DIRECCION (como lee el cribado): {len(sin_direccion)} de 30")
    for m, h, vs in sin_direccion:
        for v in vs:
            print(f"  puesto_intra {v['puesto_intra']:>5}  clase {v['clase']}  {m} -> {h}")
    print()
    print(f"CON VEREDICTO PROPIO, SOLO DIRECCION MADRE->HIJO: {len(dirigido)} de 30")
    for m, h, vs in dirigido:
        for v in vs:
            print(f"  puesto_intra {v['puesto_intra']:>5}  clase {v['clase']}  {m} -> {h}")
    print()
    clases = [v["clase"] for _, _, vs in sin_direccion for v in vs]
    print(f"clases (sin direccion): {sorted(clases)}")
    print(f"clase A entre ellos: {clases.count('A')}")


if __name__ == "__main__":
    main()
