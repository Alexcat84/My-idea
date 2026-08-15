# -*- coding: utf-8 -*-
"""EL DEPRECADO ES ARCHIVO, TAMBIEN EN EL RECIPROCADO.

EL ORIGEN, medido en la vuelta 33 de la campana del bucle (15 ago 2026). Una
fusion depreca al absorbido CONSERVANDO su cableado, que es justo lo que la hace
auditable, y redirige a los nodos vivos que lo nombraban. El paso 5 del Gate 0
leia entonces las listas del absorbido, veia aristas "sin vista reciproca" y
DEVOLVIA el id del muerto a los tres vivos de los que se acababa de quitar. El
caso positivo de la fusion pasaba 23 de 23 antes de correr el Gate y 22 de 23
despues.

    "Un verde que dura hasta la proxima corrida es un verde y mal."

La decision del fundador (15 ago 2026, opcion a de
docs/loop/paradas/2026-08-15-cableado-deprecado-y-costuras.md) es que el
deprecado conserva su cableado como ARCHIVO y el Gate deja de reciprocar las
aristas que nacen en el. Esta prueba custodia esa regla, y la custodia EN ROJO Y
EN VERDE: la regla vieja vive aqui dentro, copiada literal, y se exige que
FALLE. Una prueba que solo mira la version nueva no distingue entre "la regla
esta puesta" y "la averia nunca existio".
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from run_phase1 import aristas_a_simetrizar, count_asymmetric_edges  # noqa: E402

# LA FIGURA EXACTA DE LA AVERIA, con los papeles de la fusion de OP-D-02:
#   `superviviente` absorbe a `absorbido`, que queda deprecado con su cableado
#   INTACTO, y `vivo_1` y `vivo_2` ya fueron redirigidos al superviviente.
TRAS_UNA_FUSION = {
    "superviviente": {
        "ids_alias": ["absorbido"],
        "nodos_previos": ["vivo_2"],
        "nodos_siguientes": ["vivo_1"],
    },
    "absorbido": {
        "deprecado": True,
        # su cableado historico, tal como estaba antes de morir
        "nodos_previos": ["vivo_2"],
        "nodos_siguientes": ["vivo_1"],
    },
    "vivo_1": {"nodos_previos": ["superviviente"], "nodos_siguientes": []},
    "vivo_2": {"nodos_previos": [], "nodos_siguientes": ["superviviente"]},
}


def regla_vieja(nodes):
    """LA REGLA DE ANTES, copiada literal de `step5_symmetrize` tal como vivia
    en `scripts/run_phase1.py` hasta el commit 270ef4ea. Se conserva aqui para
    poder exigir que FALLE, no para usarla."""
    existing_ids = set(nodes)
    edges = set()
    for node_id, data in nodes.items():
        for after in data.get("nodos_siguientes") or []:
            if after in existing_ids and after != node_id:
                edges.add((node_id, after))
        for before in data.get("nodos_previos") or []:
            if before in existing_ids and before != node_id:
                edges.add((before, node_id))
    return edges


def aristas_que_tocarian_a_un_vivo(edges, nodes, muerto):
    """Las que escribirian el id del muerto DENTRO de un nodo vivo."""
    fuera = set()
    for antes, despues in edges:
        if antes == muerto and not nodes[despues].get("deprecado"):
            fuera.add((antes, despues))
        if despues == muerto and not nodes[antes].get("deprecado"):
            fuera.add((antes, despues))
    return fuera


def test_LA_REGLA_VIEJA_DEVUELVE_EL_MUERTO_A_LOS_VIVOS():
    """EN ROJO. Con la regla de antes, las dos aristas del absorbido vuelven, y
    son exactamente las que el caso positivo de la fusion vio caer."""
    vuelven = aristas_que_tocarian_a_un_vivo(
        regla_vieja(TRAS_UNA_FUSION), TRAS_UNA_FUSION, "absorbido")
    assert vuelven == {("absorbido", "vivo_1"), ("vivo_2", "absorbido")}, vuelven
    print("  ok (rojo): la regla vieja devolveria %d aristas del muerto a los vivos"
          % len(vuelven))


def test_LA_REGLA_NUEVA_NO_LO_DEVUELVE():
    """EN VERDE. Con la regla de hoy no queda ninguna: el deprecado conserva su
    cableado y no se lo escribe a nadie."""
    vuelven = aristas_que_tocarian_a_un_vivo(
        aristas_a_simetrizar(TRAS_UNA_FUSION), TRAS_UNA_FUSION, "absorbido")
    assert vuelven == set(), vuelven
    print("  ok (verde): la regla nueva no devuelve ninguna")


def test_LO_QUE_DECLARA_UN_VIVO_SIGUE_SIENDO_SIMETRIZABLE():
    """LA GUARDA DE LA GUARDA. Quitar de mas seria peor que no quitar: si un
    nodo VIVO nombra a un deprecado, esa arista la declara el vivo y sigue
    entrando. Solo se exime lo que UNICAMENTE dice un muerto."""
    g = json.loads(json.dumps(TRAS_UNA_FUSION))
    g["vivo_1"]["nodos_previos"].append("absorbido")  # lo declara un VIVO
    edges = aristas_a_simetrizar(g)
    assert ("absorbido", "vivo_1") in edges, sorted(edges)
    # y la otra, que solo dice el muerto, sigue fuera
    assert ("vivo_2", "absorbido") not in edges, sorted(edges)
    print("  ok: entra lo que declara un vivo, no entra lo que solo dice un muerto")


def test_EL_CHEQUEO_MIDE_LO_MISMO_QUE_EL_PASO_5():
    """Un Gate que exigiera simetria en aristas que el paso 5 ya no simetriza se
    pondria rojo por su propia politica. Las dos leen la misma funcion, y aqui
    se comprueba sobre el fixture: cero asimetrias, sin tocar el absorbido."""
    assert count_asymmetric_edges(TRAS_UNA_FUSION) == (0, 0), \
        count_asymmetric_edges(TRAS_UNA_FUSION)
    # y sigue cazando la asimetria de verdad, la que declara un vivo
    roto = json.loads(json.dumps(TRAS_UNA_FUSION))
    roto["vivo_1"]["nodos_previos"] = []          # el vivo pierde la vista
    assert count_asymmetric_edges(roto) == (1, 0), count_asymmetric_edges(roto)
    print("  ok: el chequeo no exige lo eximido y sigue cazando lo real")


def test_EL_CATALOGO_REAL_ESTA_SIMETRICO():
    """La pasada sobre el grafo de verdad, con la definicion de hoy."""
    g = json.loads((BASE / "dataset" / "metadata" / "master_graph.json")
                   .read_text(encoding="utf-8"))["nodos"]
    faltan = count_asymmetric_edges(g)
    assert faltan == (0, 0), faltan
    print("  ok: %d aristas declaradas por vivos en el catalogo real, todas con "
          "sus dos vistas" % len(aristas_a_simetrizar(g)))


def main():
    for f in (test_LA_REGLA_VIEJA_DEVUELVE_EL_MUERTO_A_LOS_VIVOS,
              test_LA_REGLA_NUEVA_NO_LO_DEVUELVE,
              test_LO_QUE_DECLARA_UN_VIVO_SIGUE_SIENDO_SIMETRIZABLE,
              test_EL_CHEQUEO_MIDE_LO_MISMO_QUE_EL_PASO_5,
              test_EL_CATALOGO_REAL_ESTA_SIMETRICO):
        f()
    print("OK: el deprecado es archivo tambien en el reciprocado.")


if __name__ == "__main__":
    main()
