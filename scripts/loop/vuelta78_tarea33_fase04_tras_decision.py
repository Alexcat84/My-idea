"""VUELTA 78, TAREA 3.3: tras la decision de 3.2 (10 se quedan, 1 se
revierte), deja registrado cuantas de las aristas de la fase 04 quedan
tocadas por la vara de los A. Fase 04 entera: 79 menos 1 revertida = 78.
Reusa el mismo instrumento de conteo que el auditor (comparacion contra
62d4f28e, primer commit de la fase 04) via docs/loop/_auditor_v77_diff.py
no esta pensado para esto; en vez de eso, recorre TODOS los nodos VIVOS del
grafo de HOY y toma como "aristas de la fase 04" las que aparecen en
docs/loop/SALIDA_V77_TRAMO3_ESCRIBIR.txt mas los tramos 1 y 2 (importados de
los scripts que las escribieron), menos la revertida en esta vuelta.
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta77_tramo3_escribir import PARES_SANOS as TRAMO3  # noqa: E402
from vuelta76_op_e01_tramo2_escribir import PARES_SANOS as TRAMO2  # noqa: E402

# Tramo 1 no dejo un modulo con PARES_SANOS reusable por nombre estandar;
# se toma la lista completa de la fase 04 restando tramo 2 y tramo 3 del
# fichero de diff del auditor (docs/loop/_auditor_v77_diff.txt no lista los
# pares uno a uno). En su lugar, la fase 04 completa se mide EN EL GRAFO:
# toda arista nueva desde el commit 62d4f28e (primer commit de la fase 04)
# citado por el propio auditor en su acta 77 seccion 2.


def cargar_grafo(ref):
    import subprocess
    if ref == "WORK":
        return json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", f"{ref}:dataset/metadata/master_graph.json"],
                        capture_output=True)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def main():
    antes = cargar_grafo("62d4f28e")
    ahora = cargar_grafo("WORK")

    aristas_antes = set()
    for nid, n in antes.items():
        for h in (n.get("nodos_siguientes") or []):
            aristas_antes.add((nid, h))
    aristas_ahora = set()
    for nid, n in ahora.items():
        for h in (n.get("nodos_siguientes") or []):
            aristas_ahora.add((nid, h))

    fase04 = sorted(aristas_ahora - aristas_antes)
    print(f"ARISTAS DE LA FASE 04 (HOY menos {list(aristas_antes)[:0]}62d4f28e): {len(fase04)}")

    veredictos = [json.loads(l) for l in VEREDICTOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    vivos = {nid for nid, n in ahora.items() if not n.get("deprecado")}
    condenado_por_a = {}
    for v in veredictos:
        if v.get("clase") != "A":
            continue
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a not in vivos or b not in vivos:
            continue
        condenado_por_a.setdefault(a, []).append((v["puesto_intra"], b))
        condenado_por_a.setdefault(b, []).append((v["puesto_intra"], a))

    tocadas = [(m, h) for m, h in fase04 if m in condenado_por_a or h in condenado_por_a]
    print(f"DE ESAS, TOCADAS POR LA VARA DE LOS A (tras la decision de 3.2): {len(tocadas)}")
    for m, h in tocadas:
        print(f"  {m} -> {h}")


if __name__ == "__main__":
    main()
