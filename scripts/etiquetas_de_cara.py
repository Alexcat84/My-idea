"""etiquetas_de_cara.py — aplica la lista CURADA de etiquetas de cara.

Decision del fundador (jul 2026): el usuario jamas ve titulos tecnicos ni
jerga; ve etiquetas naturales, cortas y familiares. Los nodos NO se tocan:
solo se reescribe `etiqueta_arbol`. `titulo_concepto`, `resumen_teorico` y
`fuente` quedan intactos (ahi viven la PI y la paridad con los libros).

La lista vive en dataset/metadata/etiquetas_de_cara_v1.json: es curada y
versionada, NO se genera al vuelo con el modelo (cero costo en runtime).

Parchea las DOS copias del grafo (la del dataset y el espejo que lee la web)
para que no puedan divergir. Es idempotente: correrlo dos veces no cambia
nada la segunda vez.

Uso:
    python scripts/etiquetas_de_cara.py            # muestra el diff, no escribe
    python scripts/etiquetas_de_cara.py --aplicar  # escribe las dos copias
"""

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
# Tres fuentes con procedencia SEPARADA a proposito, y EN ORDEN: la ultima
# manda sobre las anteriores.
#  1. la lista curada del auditor (la vara),
#  2. las que el diccionario de la casa (§C) prescribe palabra por palabra y la
#     lista no cubrio (nunca se inventa: lo que el diccionario no resuelve se
#     reporta, no se parchea),
#  3. la curaduria FINAL del auditor, que resuelve las colisiones que la lista
#     D introdujo y los anglicismos que no cubria.
#  4. las correcciones de FIDELIDAD del fundador (25 sep 2026): etiquetas que
#     decian lo contrario o algo distinto del concepto de su nodo, cada una con
#     su motivo escrito en `_motivos`.
LISTAS = [
    RAIZ / "dataset" / "metadata" / "etiquetas_de_cara_v1.json",
    RAIZ / "dataset" / "metadata" / "etiquetas_de_cara_v1_casa.json",
    RAIZ / "dataset" / "metadata" / "etiquetas_de_cara_v1_curaduria_final.json",
    #  la ORTOGRAFIA (saneamiento, nivel 1, criterio 16, 27 sep 2026): solo tildes, erratas y enie, cada una con su
    #  motivo en `_motivos`. Va ANTES de la de fidelidad, que sigue siendo la ultima (engine/test_etiquetas_fidelidad.py):
    #  no comparten ninguna etiqueta.
    RAIZ / "dataset" / "metadata" / "etiquetas_de_cara_v1_ortografia.json",
    RAIZ / "dataset" / "metadata" / "etiquetas_de_cara_v1_fidelidad.json",
]
GRAFOS = [
    RAIZ / "dataset" / "metadata" / "master_graph.json",
    RAIZ / "web" / "lib" / "assets" / "master_graph.json",
]


def cargar(ruta: Path) -> dict:
    with ruta.open(encoding="utf-8") as f:
        return json.load(f)


def lista_curada(verbose: bool = False) -> dict:
    """El mapa node_id -> etiqueta que manda la curaduria. La ultima lista gana."""
    lista = {}
    for ruta_lista in LISTAS:
        parcial = {k: v for k, v in cargar(ruta_lista).items() if not k.startswith("_")}
        if verbose:
            print(f"{ruta_lista.name}: {len(parcial)} etiquetas")
        lista.update(parcial)
    return lista


def curar_nodos(nodos: dict, lista: dict) -> tuple:
    """Pone en `nodos` la etiqueta curada. Devuelve (cambios, huerfanos): los
    huerfanos son ids de la lista que no estan en `nodos`, y con alguno el que
    llama no debe escribir. La usan este script y el paso 6 de run_phase1
    (decision del fundador, 7 oct 2026): la fuente sigue siendo una sola."""
    cambios, huerfanos = [], []
    for node_id, nueva in lista.items():
        nodo = nodos.get(node_id)
        if nodo is None:
            huerfanos.append(node_id)
            continue
        vieja = nodo.get("etiqueta_arbol")
        if vieja != nueva:
            cambios.append((node_id, vieja, nueva))
            nodo["etiqueta_arbol"] = nueva
    return cambios, huerfanos


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aplicar", action="store_true", help="escribe los cambios en disco")
    args = parser.parse_args()

    lista = lista_curada(verbose=True)
    print(f"total a aplicar: {len(lista)}\n")

    huerfanos = []
    cambios_por_grafo = []
    for ruta in GRAFOS:
        grafo = cargar(ruta)
        cambios, faltan = curar_nodos(grafo["nodos"], lista)
        huerfanos += [(ruta.name, node_id) for node_id in faltan]
        cambios_por_grafo.append((ruta, grafo, cambios))

    if huerfanos:
        # Fallar ruidoso: una lista que nombra nodos inexistentes esta
        # desalineada con el grafo, y aplicarla a medias es peor que no
        # aplicarla (quedaria la mitad en jerga sin que nadie lo note).
        print("ERROR: la lista nombra node_id que no existen en el grafo:", file=sys.stderr)
        for archivo, node_id in huerfanos:
            print(f"  {archivo}: {node_id}", file=sys.stderr)
        return 1

    # El diff completo, para que el commit lo pueda listar entero.
    ruta_ref, _, cambios_ref = cambios_por_grafo[0]
    for node_id, vieja, nueva in cambios_ref:
        print(f"  {node_id}\n      - {vieja}\n      + {nueva}")
    print(f"\n{len(cambios_ref)} etiquetas cambian; {len(lista) - len(cambios_ref)} ya estaban en su forma final.")

    if not args.aplicar:
        print("\n(dry run: nada escrito. Corre con --aplicar para escribir.)")
        return 0

    for ruta, grafo, cambios in cambios_por_grafo:
        with ruta.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(grafo, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"escrito: {ruta.relative_to(RAIZ)} ({len(cambios)} etiquetas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
