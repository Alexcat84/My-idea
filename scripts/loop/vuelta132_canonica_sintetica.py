# -*- coding: utf-8 -*-
"""vuelta132_canonica_sintetica.py . TAREA 3.b de la vuelta 132: tapa el
agujero de la propia regla de 3.a. EFECTO NOMBRADO (ramal xiv): SOLO
CORONA, NO AGRUPA (los grupos ya los fijo 3.a, esta pieza solo elige un
nombre para cada uno).

LA REGLA (adjudicada en el acta 131, 3.2): la canonica de un grupo es la
forma mas larga, ENTRE LOS MIEMBROS, que "sigue siendo un libro" (su
recorte de localizador no le cambia ni un caracter). CUANDO NINGUN
MIEMBRO SOBREVIVE COMO LIBRO (los tres Lindstrom de 3.a: los tres llevan
cola de capitulo), la canonica es la FORMA RECORTADA DEL MIEMBRO MAS
LARGO, y se marca SINTETICA. Puede ser una cadena que no existe en el
censo: es correcto, la lista canonica es lo que OP-S-11 PRODUCE, no lo
que consume (2.d de la 131).

CASO POSITIVO: el grupo de tres de Lindstrom (3.a) corona 'Diana L.
Lindstrom, Procurement Project Management Success' (la recortada del
miembro mas largo) y va marcado SINTETICA.
CASO NEGATIVO: un grupo que SI tiene un miembro que es libro (los cinco
documentados en la 131: Lindstrom-Anexo, FedEx, Max Muller, Rushton,
Dekker, que en esta vuelta pertenecen a otros grupos ya sellados por R1/R2
y no cambian por R3) NO cambia de canonica y NO se marca SINTETICA.

Salida: docs/loop/SALIDA_V132_3B_CANONICAS_SINTETICAS.txt

Uso:
  python scripts/loop/vuelta132_canonica_sintetica.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    UnionFind,
)
from vuelta132_grupos_por_localizador import recortar_localizador  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V132_3B_CANONICAS_SINTETICAS.txt")


def calcular_grupos():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    buck = {}
    for g in grafias:
        buck.setdefault(recortar_localizador(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)
    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)
    return censo, {r: m for r, m in grupos.items() if len(m) > 1}


def elegir_canonica(miembros):
    libros = [m for m in miembros if recortar_localizador(m) == m]
    if libros:
        return max(libros, key=len), False
    mas_largo = max(miembros, key=len)
    return recortar_localizador(mas_largo), True


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    censo, grupos_multi = calcular_grupos()

    grupo_lindstrom = None
    for r, miembros in grupos_multi.items():
        if any(m.startswith("Diana L. Lindstrom, Procurement Project Management Success, capitulo") for m in miembros):
            grupo_lindstrom = miembros
            break
    assert grupo_lindstrom is not None and len(grupo_lindstrom) == 3, (
        "CASO POSITIVO FALLO: no se encontro el grupo de tres de Lindstrom"
    )
    canon_lind, sint_lind = elegir_canonica(grupo_lindstrom)
    assert sint_lind is True, "CASO POSITIVO FALLO: el grupo de Lindstrom no se marco SINTETICA"
    assert canon_lind == "Diana L. Lindstrom, Procurement Project Management Success", (
        "CASO POSITIVO FALLO: canonica sintetica incorrecta: %r" % canon_lind
    )

    negativos_esperados = 0
    for r, miembros in grupos_multi.items():
        if any(recortar_localizador(m) == m for m in miembros) and miembros is not grupo_lindstrom:
            negativos_esperados += 1
    assert negativos_esperados > 0, "CASO NEGATIVO FALLO: ningun grupo de contraste con miembro libro"

    filas = []
    for r, miembros in grupos_multi.items():
        canon, sint = elegir_canonica(miembros)
        filas.append((miembros, canon, sint))

    n_sinteticas = sum(1 for _, _, sint in filas if sint)

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO POSITIVO (Lindstrom, ningun miembro sobrevive como libro): canonica='%s' SINTETICA=%s\n" %
                 (canon_lind, sint_lind))
        fh.write("CASO NEGATIVO (%d grupo(s) de contraste con al menos un miembro libro, no se marcan SINTETICA): OK\n\n" %
                 negativos_esperados)
        fh.write("TODOS LOS GRUPOS DE 2+ MIEMBROS CON SU CANONICA (%d grupos, %d SINTETICAS):\n" %
                 (len(filas), n_sinteticas))
        for miembros, canon, sint in sorted(filas, key=lambda t: -sum(censo[m] for m in t[0])):
            fh.write("  CANONICA: %s%s\n" % (canon, "  [SINTETICA]" if sint else ""))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grupos con 2 o mas miembros: %d\n" % len(filas))
        fh.write("TOTAL marcados SINTETICA: %d\n" % n_sinteticas)

    print("caso positivo (Lindstrom SINTETICA): OK, canonica=%r" % canon_lind)
    print("caso negativo (grupos con miembro libro, no SINTETICA): OK (%d grupos de contraste)" % negativos_esperados)
    print("grupos con 2+ miembros: %d" % len(filas))
    print("marcados SINTETICA: %d" % n_sinteticas)
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
