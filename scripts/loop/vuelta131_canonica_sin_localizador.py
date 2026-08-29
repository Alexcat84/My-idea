# -*- coding: utf-8 -*-
"""vuelta131_canonica_sin_localizador.py . TAREA 3.b de la vuelta 131:
revoca "la canonica es la mas larga" (regla vieja de
vuelta130_grupos_mecanicos_fuente.py, `max(miembros, key=len)`), que
elige un LOCALIZADOR de capitulo/seccion/anexo como nombre de libro en
CUATRO de los trece grupos viejos, y en un quinto elige la forma con
punto y coma final. LA VARA ES LA LETRA DE LA PROPIA OPERACION (05_SANEO.md,
`OP-S-11`): cuenta LIBROS CANONICOS, no capitulos.

LA REGLA NUEVA: se recorta la cola de localizador (`, capitulo N`,
`, capitulos N y M`, `, Capitulo N: ...`, `, seccion X`, `, Anexo X`) y la
puntuacion final (`;`, `,`, `.`, `:`), y la canonica de un grupo es LA
FORMA MAS LARGA, ENTRE LOS MIEMBROS DEL GRUPO, QUE YA "SIGUE SIENDO UN
LIBRO": una grafia cuyo recorte (`recortar()`) no le cambia NI UN
CARACTER (no tenia cola de localizador ni puntuacion colgando). Si
NINGUN miembro cumple eso, se cae al viejo criterio (mas larga en crudo)
como resguardo, caso que esta vuelta no deberia disparar.

RAMAL (xiii): la regla se prueba contra los CINCO casos que la propia
vuelta ya midio (acta 130 mas la relectura de esta) ANTES de aplicarla:

  CASO POSITIVO: los cinco grupos documentados cambian de canonica.
    Lindstrom: vieja `..., Anexo de aviso de no participacion` -> nueva
    `Diana L. Lindstrom, Procurement Project Management Success (J. Ross,
    2014)`.
    FedEx: vieja `..., seccion Packaging Flowers and Plants` -> nueva
    `Guia de empaque para envios (FedEx)`.
    Max Muller: vieja `..., capitulos 1 y 2` -> nueva `Max Muller,
    Essentials of Inventory Management`.
    Rushton: vieja `..., capitulo 25` -> nueva `Rushton, Croucher y Baker,
    The Handbook of Logistics and Distribution Management`.
    Dekker: vieja `The Field Guide to Understandin - Dekker, Sidney;`
    (con punto y coma final) -> nueva `The Field Guide to Understandin -
    Dekker, Sidney` (sin el punto y coma).

  CASO NEGATIVO: una grafia SIN cola de localizador y sin puntuacion
  colgando no se toca ni un caracter: `recortar(g) == g`.

Salida: docs/loop/SALIDA_V131_3B_CANONICAS_SIN_LOCALIZADOR.txt

Uso:
  python scripts/loop/vuelta131_canonica_sin_localizador.py
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
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V131_3B_CANONICAS_SIN_LOCALIZADOR.txt")

LOCALIZADORES = [
    re.compile(r",\s*capitulo\s+\d+\s*:\s*.+$", re.IGNORECASE),  # "Capitulo N: ..."
    re.compile(r",\s*capitulos?\s+\d+(\s*(y|,)\s*\d+)*$", re.IGNORECASE),  # "capitulo N" / "capitulos N y M"
    re.compile(r",\s*seccion\s+.+$", re.IGNORECASE),  # "seccion X"
    re.compile(r",\s*anexo\s+.+$", re.IGNORECASE),  # "Anexo X"
]
PUNTUACION_FINAL = re.compile(r"[;,:\.\s]+$")


def recortar(grafia):
    s = grafia
    for pat in LOCALIZADORES:
        s2 = pat.sub("", s)
        if s2 != s:
            s = s2
            break
    s = PUNTUACION_FINAL.sub("", s)
    return s


def elegir_canonica(miembros):
    candidatos = [m for m in miembros if recortar(m) == m]
    base = candidatos if candidatos else miembros
    return max(base, key=len)


def calcular_grupos():
    censo = cargar_censo()
    grafias = sorted(censo.keys())
    uf = UnionFind(grafias)
    for a in grafias:
        for b in grafias:
            if prefijo_cadena_entera_une(a, b):
                uf.une(a, b)
            if prefijo_titulo_une(a, b):
                uf.une(a, b)
    grupos = {}
    for g in grafias:
        grupos.setdefault(uf.find(g), []).append(g)
    return censo, {r: m for r, m in grupos.items() if len(m) > 1}


def correr_casos_de_prueba(grupos_multi):
    esperado = {
        "Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014)": None,
        "Guia de empaque para envios (FedEx)": None,
        "Max Muller, Essentials of Inventory Management": None,
        "Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management": None,
        "The Field Guide to Understandin - Dekker, Sidney": None,
    }
    resultados = []
    for miembros in grupos_multi.values():
        for base_esperada in list(esperado.keys()):
            if base_esperada in miembros:
                vieja = max(miembros, key=len)
                nueva = elegir_canonica(miembros)
                cambia = nueva != vieja
                acierta = nueva == base_esperada
                resultados.append((base_esperada, vieja, nueva, cambia, acierta))
                assert cambia, "CASO POSITIVO FALLO (no cambia): %s" % base_esperada
                assert acierta, "CASO POSITIVO FALLO (canonica incorrecta): %s -> %s" % (base_esperada, nueva)
    assert len(resultados) == 5, "se esperaban los CINCO casos documentados, se encontraron %d" % len(resultados)

    negativo = "Essentials of Supply Chain Management - Michael H. Hugos"
    assert recortar(negativo) == negativo, "CASO NEGATIVO FALLO: recorto una grafia sin cola de localizador"

    return resultados, negativo


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo, grupos_multi = calcular_grupos()
    resultados, negativo = correr_casos_de_prueba(grupos_multi)

    cambios = []
    for r, miembros in grupos_multi.items():
        vieja = max(miembros, key=len)
        nueva = elegir_canonica(miembros)
        if nueva != vieja:
            cambios.append((vieja, nueva, miembros))

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("CASO NEGATIVO: recortar(%r) == grafia sin cambios: %s\n\n" % (negativo, recortar(negativo) == negativo))
        fh.write("CASO POSITIVO, LOS CINCO DOCUMENTADOS (vieja canonica -> nueva canonica):\n")
        for base_esperada, vieja, nueva, cambia, acierta in resultados:
            fh.write("  %s\n    VIEJA: %s\n    NUEVA: %s\n" % (base_esperada, vieja, nueva))
        fh.write("\nTODOS LOS GRUPOS QUE CAMBIAN DE CANONICA CON LA REGLA NUEVA (%d de %d grupos con 2+ miembros):\n" % (len(cambios), len(grupos_multi)))
        for vieja, nueva, miembros in sorted(cambios, key=lambda t: -sum(censo[m] for m in t[2])):
            fh.write("  VIEJA: %s\n  NUEVA: %s\n" % (vieja, nueva))
            for m in sorted(miembros, key=len):
                fh.write("    %d\t%s\n" % (censo[m], m))
        fh.write("\nTOTAL grupos con 2 o mas miembros: %d\n" % len(grupos_multi))
        fh.write("TOTAL grupos que cambian de canonica: %d\n" % len(cambios))

    print("caso negativo (recortar no toca una grafia limpia): %s" % (recortar(negativo) == negativo))
    print("caso positivo: los cinco documentados cambian de canonica y aciertan la esperada: OK")
    print("grupos con 2+ miembros: %d" % len(grupos_multi))
    print("grupos que cambian de canonica: %d" % len(cambios))
    print("EXITCODE: 0")


if __name__ == "__main__":
    raise SystemExit(main())
