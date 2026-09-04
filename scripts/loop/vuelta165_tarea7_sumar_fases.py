# -*- coding: utf-8 -*-
r"""vuelta165_tarea7_sumar_fases.py . SUMA LAS ONCE FASES CONTANDO SU PROPIO
FICHERO DE SALIDA (vuelta 165).

POR QUE: `EJECUTOR.md` 1, "LA TABLA SE CUENTA DE SU FICHERO". Las once corridas
de `tallar_estado_de_fase.py --fase` imprimen una linea `CIFRA` por fase, pero
NINGUNA imprime el TOTAL. Sumarlo a mano seria teclear una celda que ningun
instrumento valida. Esto lo suma leyendo `docs/loop/SALIDA_V165_T7_FASES.txt` y
APENDA sus lineas `CIFRA` al mismo fichero, para que el reporte pueda citarlo.

USO:  python scripts/loop/vuelta165_tarea7_sumar_fases.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V165_T7_FASES.txt")
MARCA = "SUMA DE LAS ONCE FASES, CONTADA DE ESTE MISMO FICHERO"

PAT = re.compile(
    r"CIFRA: operaciones del catalogo: (\d+) \| con destino cumplido: (\d+) \| "
    r"sin cumplir: (\d+) \| de ellas, sin vara escrita: (\d+) \| de ellas, "
    r"consumidas con superviviente divergente: (\d+)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    texto = io.open(RUTA, encoding="utf-8").read()
    if MARCA in texto:
        texto = texto.split("\n" + "=" * 78 + "\n" + MARCA)[0]
    filas = PAT.findall(texto)
    fases = re.findall(r"^########## (\S+)$", texto, re.M)
    if len(filas) != len(fases):
        raise SystemExit("ROJO: %d fases y %d lineas CIFRA. No cuadra."
                         % (len(fases), len(filas)))
    tot = [sum(int(f[i]) for f in filas) for i in range(5)]
    bloque = [
        "",
        "=" * 78,
        MARCA,
        "=" * 78,
        "  CIFRA fases sumadas: %d" % len(filas),
        "  CIFRA operaciones del catalogo: %d" % tot[0],
        "  CIFRA con destino cumplido: %d" % tot[1],
        "  CIFRA sin cumplir: %d" % tot[2],
        "  CIFRA sin vara escrita: %d" % tot[3],
        "  CIFRA consumidas con superviviente divergente: %d" % tot[4],
        "  COMPROBACION: cumplidas mas sin cumplir es %d, y el catalogo es %d: %s"
        % (tot[1] + tot[2], tot[0], "CUADRA" if tot[1] + tot[2] == tot[0] else "NO CUADRA"),
        "",
    ]
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(
        texto.rstrip("\n") + "\n" + "\n".join(bloque))
    for l in bloque:
        if l.strip():
            print(l)
    return 0 if tot[1] + tot[2] == tot[0] else 1


if __name__ == "__main__":
    raise SystemExit(main())
