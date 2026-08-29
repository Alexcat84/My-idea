# -*- coding: utf-8 -*-
"""vuelta135_cola_localizador_cap.py . TAREA 4.a de la vuelta 135
(adjudicacion del auditor, acta 134, 3.3 y 3.b/4.1 punto (3)). EXTIENDE la
cola de localizador de `vuelta133_cola_localizador_apendice.py` con la
abreviatura `Cap.`/`Caps.` (con punto), SIN borrar ese fichero: importa su
`LOC` (la cola VIEJA, para reportar el ANTES exacto),
`recortar_localizador_con_apendice` y, via `vuelta131_grupos_por_titulo`,
`cargar_censo`, `prefijo_cadena_entera_une`, `prefijo_titulo_une` y
`UnionFind`. No reimplementa el union-find.

EFECTO NOMBRADO (ramal xiv): AGRUPA, igual que el resto de la cola. La
cola pasa a recortar tambien `, Cap. X`, `, Caps. X y Z` y sus variantes
con minuscula (`re.IGNORECASE`, ya vigente en la cola vieja).

RAMAL (xiii), sus dos casos, corridos ANTES de aplicarla sobre el censo:

  CASO POSITIVO: `Edwards et al., Managing Project Risks, Cap. 9 (Risk
  Transfer)` recorta a `Edwards et al., Managing Project Risks` y cae en
  el MISMO grupo que `Edwards et al., Managing Project Risks, Cap. 2
  (Classifying Risk)`.

  CASO NEGATIVO: una grafia SIN cola de localizador no se toca ni un
  caracter (recortar(g) == g). Usa la misma que uso la 133,
  `Essentials of Supply Chain Management - Michael H. Hugos`.

Salida: docs/loop/SALIDA_V135_4A_COLA_CON_CAP.txt, con su linea CIFRA.

USO:
  python scripts/loop/vuelta135_cola_localizador_cap.py
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
from vuelta133_cola_localizador_apendice import (  # noqa: E402
    LOC as LOC_VIEJA,
    PUNTUACION_FINAL,
    recortar_localizador_con_apendice,
)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_4A_COLA_CON_CAP.txt")

# EXTENSION (TAREA 4.a): se anade "caps?\." (con punto, abreviatura) a la
# alternativa de la cola VIEJA (capitulos?, seccion, anexos?, apendices?),
# que ya viene con re.IGNORECASE puesto: "Cap." y "cap." casan igual, sin
# alternativa aparte para minuscula.
LOC_CON_CAP = re.compile(
    r",\s*(cap[ií]tulos?\s+.*|caps?\.\s*.*|secci[oó]n\s+.*|[Aa]nexos?\s+.*|[Aa]p[eé]ndices?\s+.*)$",
    re.IGNORECASE)


def recortar_localizador_con_cap(grafia):
    x = grafia
    while True:
        y = LOC_CON_CAP.sub("", x)
        y = PUNTUACION_FINAL.sub("", y)
        if y == x:
            return x
        x = y


def correr_casos_de_prueba():
    positivo = "Edwards et al., Managing Project Risks, Cap. 9 (Risk Transfer)"
    esperada = "Edwards et al., Managing Project Risks"

    assert LOC_VIEJA.search(positivo) is None, (
        "la cola VIEJA (133) ya reconocia 'Cap.': la extension no aporta nada")

    recortada = recortar_localizador_con_cap(positivo)
    assert recortada == esperada, (
        "CASO POSITIVO FALLO: '%s' recorto a '%s', se esperaba '%s'" %
        (positivo, recortada, esperada))

    negativo = "Essentials of Supply Chain Management - Michael H. Hugos"
    assert recortar_localizador_con_cap(negativo) == negativo, (
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

    # LADO VIEJO (cola de la 133, con Apendice pero sin Cap.): para
    # reportar el ANTES exacto.
    uf_vieja, grafias = agrupar(censo, recortar_localizador_con_apendice)
    n_vieja = len({uf_vieja.find(g) for g in grafias})

    # LADO NUEVO (cola con Caps?.).
    uf_nueva, _ = agrupar(censo, recortar_localizador_con_cap)
    n_nueva = len({uf_nueva.find(g) for g in grafias})

    assert uf_nueva.find(positivo) == uf_nueva.find(
        "Edwards et al., Managing Project Risks, Cap. 2 (Classifying Risk)"
    ), "CASO POSITIVO FALLO (post): el Cap. 9 no cayo en la familia Edwards"
    assert recortar_localizador_con_cap(negativo) == negativo, "CASO NEGATIVO FALLO (post)"

    grupos_nueva = {}
    for g in grafias:
        grupos_nueva.setdefault(uf_nueva.find(g), []).append(g)
    multi = {r: m for r, m in grupos_nueva.items() if len(m) > 1}
    solos = [m[0] for m in grupos_nueva.values() if len(m) == 1]

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO POSITIVO: '%s' recorta a '%s' y entra a la familia Edwards: OK\n" %
                 (positivo, esperada))
        fh.write("CASO NEGATIVO (grafia sin cola de localizador, recortar(g) == g): OK\n\n")
        fh.write("GRUPOS con cola VIEJA (133, con Apendice, sin Cap.): %d\n" % n_vieja)
        fh.write("GRUPOS con cola EXTENDIDA (mas Caps?., esta TAREA 4.a): %d\n" % n_nueva)
        fh.write("CIFRA grupos con cola extendida a Caps?.: %d grupos\n" % n_nueva)
        fh.write("COLAPSOS GANADOS POR LA EXTENSION: %d\n\n" % (n_vieja - n_nueva))
        fh.write("GRUPOS CON 2 O MAS MIEMBROS (%d grupos, %d grafias):\n" % (len(multi), sum(len(m) for m in multi.values())))
        for r in sorted(multi, key=lambda r: -sum(censo[m] for m in multi[r])):
            miembros = multi[r]
            fh.write("  GRUPO (%d nodos):\n" % sum(censo[m] for m in miembros))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grafias: %d\n" % len(grafias))
        fh.write("CIFRA grafias del censo: %d grafias\n" % len(grafias))
        fh.write("TOTAL grupos (incluye singletons): %d\n" % n_nueva)
        fh.write("TOTAL grupos con 2 o mas miembros: %d (%d grafias)\n" % (len(multi), sum(len(m) for m in multi.values())))
        fh.write("TOTAL sin agrupar: %d\n" % len(solos))
    print("caso positivo (Cap. 9 entra a la familia Edwards): OK")
    print("caso negativo (grafia sin cola, no cambia): OK")
    print("grupos cola vieja (133, con Apendice): %d" % n_vieja)
    print("grupos cola extendida (mas Caps?.): %d" % n_nueva)
    print("grupos con 2+ miembros: %d (%d grafias)" % (len(multi), sum(len(m) for m in multi.values())))
    print("sin agrupar: %d" % len(solos))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
