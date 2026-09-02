# -*- coding: utf-8 -*-
"""Las tres barandas del alias en el Gate 0, y el filtro en los escritores.

EL ORIGEN (cirugia de metadata, ago 2026). Ocho nodos llevaban su propio id
dentro de su `ids_alias`, y uno de esos auto-alias competia con el dueno real
por la misma cadena (`jerarquia_controles`, reclamado por su propio nodo
deprecado Y por `prevencion_control_peligros`). El mapa se construye
recorriendo los nodos y el ULTIMO gana, asi que la resolucion dependia del
ORDEN de serializacion: ganaba el correcto por estar en el indice 2877 contra
el 2217 del otro.

    "Un dato que esta bien de suerte es un dato que esta mal."

Y la tercera baranda nace del mismo trabajo: 71 `etiqueta_arbol` vivieron
divergentes entre las dos copias del grafo durante toda una serie de commits,
porque cada copia era valida por su cuenta y NINGUN guardian las comparaba.
"""
import os
import json
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from run_phase1 import (alias_auto, alias_con_dos_duenos,  # noqa: E402
                        gemelos_divergentes)

LIMPIO = {
    "superviviente": {"ids_alias": ["absorbido_2", "absorbido_3"], "titulo_concepto": "A"},
    "absorbido_2": {"deprecado": True, "titulo_concepto": "B"},
    "otro": {"ids_alias": ["viejo_id"], "titulo_concepto": "C"},
}


def test_FIXTURE_LIMPIO_pasa_las_tres():
    assert alias_auto(LIMPIO) == []
    assert alias_con_dos_duenos(LIMPIO) == {}
    assert gemelos_divergentes(LIMPIO, json.loads(json.dumps(LIMPIO))) == {}
    print("  ok: el grafo limpio pasa las tres barandas")


def test_VIOLA_AUTO_ALIAS():
    """(a) un nodo con su propio id dentro de su ids_alias. Es la forma exacta
    que tenian los ocho: [base, base_2] en el nodo llamado `base`."""
    sucio = json.loads(json.dumps(LIMPIO))
    sucio["superviviente"]["ids_alias"] = ["superviviente", "absorbido_2"]
    assert alias_auto(sucio) == ["superviviente"], alias_auto(sucio)
    # y no confunde: el limpio sigue limpio
    assert alias_auto(LIMPIO) == []
    print("  ok: caza el auto-alias y no marca al limpio")


def test_VIOLA_ALIAS_CON_DOS_DUENOS():
    """(b) la misma cadena reclamada por dos nodos. La averia real: quien gana
    lo decide el orden de iteracion, no una regla."""
    sucio = json.loads(json.dumps(LIMPIO))
    sucio["otro"]["ids_alias"] = ["absorbido_2"]  # ya lo reclama `superviviente`
    dos = alias_con_dos_duenos(sucio)
    assert dos == {"absorbido_2": ["otro", "superviviente"]}, dos
    assert alias_con_dos_duenos(LIMPIO) == {}
    print("  ok: caza el alias con dos duenos, con los dos nombres")


def test_VIOLA_GEMELOS_DIVERGENTES():
    """(c) las dos copias del grafo diciendo cosas distintas. El caso real fue
    `etiqueta_arbol`: estructura valida en las dos, voz distinta."""
    web = json.loads(json.dumps(LIMPIO))
    web["superviviente"]["etiqueta_arbol"] = "Forma Curada"
    dif = gemelos_divergentes(LIMPIO, web)
    assert dif == {"superviviente": "etiqueta_arbol"}, dif
    # un nodo que solo existe en un lado tambien es divergencia
    solo = json.loads(json.dumps(LIMPIO))
    del solo["otro"]
    assert gemelos_divergentes(LIMPIO, solo) == {"otro": "solo en dataset"}
    assert gemelos_divergentes(solo, LIMPIO) == {"otro": "solo en web"}
    print("  ok: caza la divergencia de campo y la de nodo ausente")


def test_COMPARA_CAMPOS_Y_NO_BYTES():
    """El orden de las claves y el formato son cosa del serializador. Si el
    chequeo mirara bytes, cualquier re-volcado lo pondria rojo y acabaria
    desactivado, que es como mueren las barandas."""
    a = {"n": {"x": 1, "y": [1, 2], "z": "hola"}}
    b = {"n": {"z": "hola", "y": [1, 2], "x": 1}}  # mismas parejas, otro orden
    assert gemelos_divergentes(a, b) == {}
    print("  ok: compara campos, no bytes ni orden de claves")


def test_EL_ESCRITOR_QUE_SEMBRABA_YA_NO_SIEMBRA():
    """La huella de los ocho se rastreo hasta scripts/hseq/_renombrar_cosmetico
    .py: el nodo llega con la BASE ya en su ids_alias (la absorbio en el dedup)
    y acto seguido se guarda CON ESE MISMO NOMBRE. Su tabla RENOMBRES tiene
    exactamente los ocho.

    Se custodian los CINCO puntos de escritura de ids_alias del repo, no solo
    el culpable: la misma regla escrita en un solo sitio falla en el que
    alguien olvido."""
    escritores = {
        "scripts/hseq/_renombrar_cosmetico.py": 'a != nuevo',
        "scripts/hseq/paso1_ascii.py": 'a != nuevo',
        "scripts/consolidar_pack.py": 'a != gana',
        "scripts/hseq/paso2_dedup.py": 'viejo != keeper',
        "scripts/expansion/tejer_ola1.py": 'otro != keeper',
    }
    faltan = []
    for ruta, guarda in escritores.items():
        src = (BASE / ruta).read_text(encoding="utf-8")
        if guarda not in src:
            faltan.append(f"{ruta} (falta `{guarda}`)")
    assert not faltan, f"puntos de escritura sin filtro de auto-alias: {faltan}"
    print(f"  ok: los {len(escritores)} puntos de escritura filtran el auto-alias")


def test_EL_CATALOGO_REAL_ESTA_LIMPIO():
    """La pasada sobre el grafo de verdad. Si esto falla, alguien sembro."""
    g = json.loads((BASE / "dataset" / "metadata" / "master_graph.json")
                   .read_text(encoding="utf-8"))["nodos"]
    assert alias_auto(g) == [], alias_auto(g)
    assert alias_con_dos_duenos(g) == {}, alias_con_dos_duenos(g)
    web = json.loads((BASE / "web" / "lib" / "assets" / "master_graph.json")
                     .read_text(encoding="utf-8"))["nodos"]
    dif = gemelos_divergentes(g, web)
    # EL FALSO ROJO SE DELATA SOLO (TAREA 5 de la vuelta 150). Esta linea es la
    # que cuatro actas seguidas leyeron como un rojo del catalogo cuando era el
    # ciclo de Gate 0 a medias. El assert NO se afloja: lo que se anade es el
    # diagnostico que dice, en una linea, cual de las dos cosas es, y nombra el
    # comando que falta cuando falta.
    if dif:
        sys.path.insert(0, str(BASE / "scripts" / "loop"))
        from diagnostico_ciclo_a_medias import diagnosticar
        diag = diagnosticar(dif, g, web)
    else:
        diag = ""
    assert not dif, (f"{len(dif)} nodos divergentes entre las dos copias: "
                     + str(list(dif)[:3]) + os.linesep + diag)
    print(f"  ok: los {len(g)} nodos del master real, sin auto-alias, sin dos "
          f"duenos, y las dos copias identicas")


def main():
    for f in (test_FIXTURE_LIMPIO_pasa_las_tres,
              test_VIOLA_AUTO_ALIAS,
              test_VIOLA_ALIAS_CON_DOS_DUENOS,
              test_VIOLA_GEMELOS_DIVERGENTES,
              test_COMPARA_CAMPOS_Y_NO_BYTES,
              test_EL_ESCRITOR_QUE_SEMBRABA_YA_NO_SIEMBRA,
              test_EL_CATALOGO_REAL_ESTA_LIMPIO):
        f()
    print("OK: las tres barandas del alias, y los cinco escritores filtrados.")


if __name__ == "__main__":
    main()
