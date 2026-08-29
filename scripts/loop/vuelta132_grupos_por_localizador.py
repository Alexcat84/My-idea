# -*- coding: utf-8 -*-
"""vuelta132_grupos_por_localizador.py . TAREA 3.a de la vuelta 132: anade
una TERCERA regla mecanica de agrupacion a las dos de la 131 (cadena
entera, titulo). EFECTO NOMBRADO (ramal xiv): AGRUPA, no solo corona.

LA REGLA. Se recorta de cada grafia la cola de localizador (`, capitulo N`,
`, capitulos N y M`, `, Capitulo N: ...`, `, seccion X`, `, Anexo X`) y la
puntuacion final (`;`, `,`, `.`, `:`). Dos grafias cuya forma recortada
queda IDENTICA (igualdad exacta, NO prefijo: el prefijo sobre la recortada
es otra cosa, 3.d) van al mismo grupo.

RAMAL (xiii): sus dos casos, corridos ANTES de aplicarla sobre el censo:

  CASO POSITIVO: las TRES grafias de Diana L. Lindstrom (capitulo 11,
  capitulo 3 y Apendice C, capitulo 6) recortan todas a la misma forma
  ('Diana L. Lindstrom, Procurement Project Management Success') y hoy son
  TRES grupos de uno (la forma sin cola no existe como grafia en el censo,
  asi que ni la cadena entera ni el titulo las unen). Con la regla del
  localizador, las tres caen en UN SOLO grupo.

  CASO NEGATIVO: una grafia SIN cola de localizador no se toca ni un
  caracter (recortar(g) == g) y no cambia de grupo respecto de R1+R2.

Salida: docs/loop/SALIDA_V132_3A_GRUPOS_POR_LOCALIZADOR.txt

Uso:
  python scripts/loop/vuelta132_grupos_por_localizador.py
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
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V132_3A_GRUPOS_POR_LOCALIZADOR.txt")

LOC = re.compile(r",\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|[Aa]nexo\s+.*)$", re.IGNORECASE)
PUNTUACION_FINAL = re.compile(r"[;,:\.\s]+$")


def recortar_localizador(grafia):
    x = grafia
    while True:
        y = LOC.sub("", x)
        y = PUNTUACION_FINAL.sub("", y)
        if y == x:
            return x
        x = y


def correr_casos_de_prueba():
    positivos = [
        "Diana L. Lindstrom, Procurement Project Management Success, capitulo 11",
        "Diana L. Lindstrom, Procurement Project Management Success, capitulo 3 y Apendice C",
        "Diana L. Lindstrom, Procurement Project Management Success, capitulo 6",
    ]
    recortadas = {recortar_localizador(g) for g in positivos}
    assert len(recortadas) == 1, "CASO POSITIVO FALLO: las tres grafias de Lindstrom no recortan igual: %s" % recortadas
    esperada = "Diana L. Lindstrom, Procurement Project Management Success"
    assert recortadas.pop() == esperada, "CASO POSITIVO FALLO: la forma recortada no es la esperada"

    negativo = "Essentials of Supply Chain Management - Michael H. Hugos"
    assert recortar_localizador(negativo) == negativo, "CASO NEGATIVO FALLO: recorto una grafia sin cola de localizador"

    return positivos, negativo


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    positivos, negativo = correr_casos_de_prueba()

    censo = cargar_censo()
    grafias = sorted(censo.keys())

    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
    n_cadena = len({uf.find(g) for g in grafias})

    for a in grafias:
        for b in grafias:
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    n_titulo = len({uf.find(g) for g in grafias})

    for a in positivos:
        assert uf.find(a) != uf.find(positivos[0]) or a == positivos[0], "precondicion rota"
    assert len({uf.find(g) for g in positivos}) == 3, (
        "precondicion rota: los tres Lindstrom ya estaban agrupados antes de la regla del localizador"
    )

    buck = {}
    for g in grafias:
        buck.setdefault(recortar_localizador(g), []).append(g)
    pares_localizador_nuevos = []
    for _, miembros in buck.items():
        base = miembros[0]
        for m in miembros[1:]:
            if uf.find(base) != uf.find(m):
                pares_localizador_nuevos.append((base, m))
            uf.une(base, m)
    n_localizador = len({uf.find(g) for g in grafias})

    assert len({uf.find(g) for g in positivos}) == 1, "CASO POSITIVO FALLO: los tres Lindstrom no quedaron en un solo grupo"
    assert recortar_localizador(negativo) == negativo, "CASO NEGATIVO FALLO (post)"

    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)
    multi = {r: m for r, m in grupos.items() if len(m) > 1}
    solos = [m[0] for m in grupos.values() if len(m) == 1]

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO POSITIVO (Lindstrom, tres grafias con cola de capitulo): recortan las tres a "
                 "'Diana L. Lindstrom, Procurement Project Management Success' y quedan en UN grupo: OK\n")
        fh.write("CASO NEGATIVO (grafia sin cola de localizador, recortar(g) == g): OK\n\n")
        fh.write("GRUPOS con R1 (cadena entera): %d\n" % n_cadena)
        fh.write("GRUPOS con R1+R2 (cadena entera + titulo): %d\n" % n_titulo)
        fh.write("GRUPOS con R1+R2+R3 (+ localizador, AGRUPA): %d\n" % n_localizador)
        fh.write("COLAPSOS ADICIONALES QUE GANA R3 SOLA: %d\n\n" % (n_titulo - n_localizador))
        fh.write("PARES NUEVOS QUE SOLO R3 (LOCALIZADOR) UNE (no unidos por R1 ni R2):\n")
        for a, b in pares_localizador_nuevos:
            fh.write("  %s  <->  %s\n" % (a, b))
        fh.write("\nGRUPOS CON 2 O MAS MIEMBROS (%d grupos, %d grafias):\n" % (len(multi), sum(len(m) for m in multi.values())))
        for r in sorted(multi, key=lambda r: -sum(censo[m] for m in multi[r])):
            miembros = multi[r]
            fh.write("  GRUPO (%d nodos):\n" % sum(censo[m] for m in miembros))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grafias: %d\n" % len(grafias))
        fh.write("TOTAL grupos (incluye singletons): %d\n" % n_localizador)
        fh.write("TOTAL grupos con 2 o mas miembros: %d (%d grafias)\n" % (len(multi), sum(len(m) for m in multi.values())))
        fh.write("TOTAL sin agrupar: %d\n" % len(solos))

    print("caso positivo (Lindstrom, tres grafias -> un grupo): OK")
    print("caso negativo (grafia sin cola de localizador, no cambia): OK")
    print("grupos R1 (cadena entera): %d" % n_cadena)
    print("grupos R1+R2 (titulo): %d" % n_titulo)
    print("grupos R1+R2+R3 (localizador, AGRUPA): %d" % n_localizador)
    print("grupos con 2+ miembros: %d (%d grafias)" % (len(multi), sum(len(m) for m in multi.values())))
    print("sin agrupar: %d" % len(solos))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
