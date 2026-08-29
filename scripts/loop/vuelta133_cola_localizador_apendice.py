# -*- coding: utf-8 -*-
"""vuelta133_cola_localizador_apendice.py . TAREA 4.a de la vuelta 133
(adjudicacion del auditor, acta 132, seccion 3.1). EXTIENDE la cola de
localizador de `vuelta132_grupos_por_localizador.py` con `Apendice`, sin
borrar ese fichero: importa su `cargar_censo`, `prefijo_cadena_entera_une`
y `prefijo_titulo_une` (via `vuelta131_grupos_por_titulo`), y repite la
misma mecanica de union-find con la cola EXTENDIDA.

EFECTO NOMBRADO (ramal xiv): AGRUPA, igual que el resto de la cola. La
cola pasa a recortar tambien `, Apendice X`, `, Apendices X y Z` (plural)
y `, Anexos X` (plural del que ya estaba en la 132). ADJUDICADO Y NO
DISCUTIBLE (acta 132, 3.1): `Apendice` es el mismo localizador que `Anexo`
escrito en la otra grafia, y las dos formas conviven en la MISMA familia
del censo (medido: las TRES grafias del censo con Anexo o Apendice son
las TRES de la familia Lindstrom), asi que la extension es por cita, no
doctrina nueva.

RAMAL (xiii), sus dos casos, corridos ANTES de aplicarla sobre el censo:

  CASO POSITIVO: la grafia
  `Diana L. Lindstrom, Procurement Project Management Success, Apendice B
  (RFPS)` recorta a `Diana L. Lindstrom, Procurement Project Management
  Success` (deja de traer el Apendice) y DEJA DE SER un grupo LIBRO propio:
  con la cola vieja (solo Anexo) esa grafia no recortaba nada y quedaba
  singleton fuera de la familia; con la cola extendida cae en el mismo
  grupo que las otras dos grafias de capitulo de Lindstrom.

  CASO NEGATIVO: una grafia SIN cola de localizador no se toca ni un
  caracter (recortar(g) == g).

Salida: docs/loop/SALIDA_V133_4A_COLA_CON_APENDICE.txt

Uso:
  python scripts/loop/vuelta133_cola_localizador_apendice.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import (  # noqa: E402
    cargar_censo,
    prefijo_cadena_entera_une,
    prefijo_titulo_une,
    UnionFind,
)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V133_4A_COLA_CON_APENDICE.txt")

# EXTENSION (TAREA 4.a): se anade "apendice(s)" a la alternativa de "anexo(s)".
# El resto (capitulo(s), seccion) queda IDENTICO a vuelta132_grupos_por_localizador.py.
LOC = re.compile(r",\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|[Aa]nexos?\s+.*|[Aa]p[eé]ndices?\s+.*)$",
                  re.IGNORECASE)
PUNTUACION_FINAL = re.compile(r"[;,:\.\s]+$")


def recortar_localizador_con_apendice(grafia):
    x = grafia
    while True:
        y = LOC.sub("", x)
        y = PUNTUACION_FINAL.sub("", y)
        if y == x:
            return x
        x = y


def correr_casos_de_prueba():
    positivo = ("Diana L. Lindstrom, Procurement Project Management Success, "
                "Apendice B (RFPS)")
    esperada = "Diana L. Lindstrom, Procurement Project Management Success"
    recortada = recortar_localizador_con_apendice(positivo)
    assert recortada == esperada, (
        "CASO POSITIVO FALLO: '%s' recorto a '%s', se esperaba '%s'" %
        (positivo, recortada, esperada))

    negativo = "Essentials of Supply Chain Management - Michael H. Hugos"
    assert recortar_localizador_con_apendice(negativo) == negativo, (
        "CASO NEGATIVO FALLO: recorto una grafia sin cola de localizador")

    return positivo, esperada, negativo


def agrupar(censo, recortador):
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
        buck.setdefault(recortador(g), []).append(g)
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            uf.une(base, m)
    return uf, grafias


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    positivo, esperada, negativo = correr_casos_de_prueba()

    censo = cargar_censo()

    # LADO VIEJO (cola vigente, solo Anexo): para reportar el ANTES exacto.
    from vuelta132_grupos_por_localizador import recortar_localizador as recortar_vieja
    uf_vieja, grafias = agrupar(censo, recortar_vieja)
    n_vieja = len({uf_vieja.find(g) for g in grafias})

    # LADO NUEVO (cola con Apendice).
    uf_nueva, _ = agrupar(censo, recortar_localizador_con_apendice)
    n_nueva = len({uf_nueva.find(g) for g in grafias})

    assert uf_nueva.find(positivo) == uf_nueva.find(
        "Diana L. Lindstrom, Procurement Project Management Success, capitulo 11"
    ), "CASO POSITIVO FALLO (post): el Apendice B no cayo en la familia Lindstrom"
    assert recortar_localizador_con_apendice(negativo) == negativo, "CASO NEGATIVO FALLO (post)"

    grupos_nueva = {}
    for g in grafias:
        grupos_nueva.setdefault(uf_nueva.find(g), []).append(g)
    multi = {r: m for r, m in grupos_nueva.items() if len(m) > 1}
    solos = [m[0] for m in grupos_nueva.values() if len(m) == 1]

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO POSITIVO: '%s' recorta a '%s' y entra a la familia Lindstrom: OK\n" %
                 (positivo, esperada))
        fh.write("CASO NEGATIVO (grafia sin cola de localizador, recortar(g) == g): OK\n\n")
        fh.write("GRUPOS con cola VIEJA (solo Anexo, vuelta 132 3.a): %d\n" % n_vieja)
        fh.write("GRUPOS con cola EXTENDIDA (mas Apendice, esta TAREA 4.a): %d\n" % n_nueva)
        fh.write("COLAPSOS GANADOS POR LA EXTENSION: %d\n\n" % (n_vieja - n_nueva))
        fh.write("GRUPOS CON 2 O MAS MIEMBROS (%d grupos, %d grafias):\n" % (len(multi), sum(len(m) for m in multi.values())))
        for r in sorted(multi, key=lambda r: -sum(censo[m] for m in multi[r])):
            miembros = multi[r]
            fh.write("  GRUPO (%d nodos):\n" % sum(censo[m] for m in miembros))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grafias: %d\n" % len(grafias))
        fh.write("TOTAL grupos (incluye singletons): %d\n" % n_nueva)
        fh.write("TOTAL grupos con 2 o mas miembros: %d (%d grafias)\n" % (len(multi), sum(len(m) for m in multi.values())))
        fh.write("TOTAL sin agrupar: %d\n" % len(solos))
    print("caso positivo (Apendice B entra a la familia Lindstrom): OK")
    print("caso negativo (grafia sin cola, no cambia): OK")
    print("grupos cola vieja (solo Anexo): %d" % n_vieja)
    print("grupos cola extendida (mas Apendice): %d" % n_nueva)
    print("grupos con 2+ miembros: %d (%d grafias)" % (len(multi), sum(len(m) for m in multi.values())))
    print("sin agrupar: %d" % len(solos))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
