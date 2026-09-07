# -*- coding: utf-8 -*-
"""Repara los dos bloques del acta 201 que la shell mutilo comiendose los acentos
graves. NO toca nada mas y NO borra ni una linea: solo sustituye texto roto por el
texto que se quiso escribir. Se declara en el acta como lo que es: un arreglo mio.

Fichero de UN SOLO USO, con prefijo de guion bajo: queda FUERA del censo y FUERA de
la nomina congelada en 135, o sea que no fabrica maquinaria y no roza la moratoria
6.3."""
import io
import sys

NL = chr(10)
BT = chr(96)

ROTO = (
    "acta. Lo repare con un fichero de un solo uso, ," + NL
    + "que lleva **prefijo de guion bajo** y queda **fuera del censo y fuera de la nomina" + NL
    + "congelada en 135**, o sea que **no fabrica maquinaria** y no roza la moratoria ." + NL
)

BUENO = (
    "acta. Lo repare con un fichero de un solo uso," + NL
    + BT + "docs/loop/_auditor_v201_reparar_c3.py" + BT + ", que lleva **prefijo de guion bajo** y queda" + NL
    + "**fuera del censo y fuera de la nomina congelada en 135**, o sea que **no fabrica" + NL
    + "maquinaria** y no roza la moratoria " + BT + "6.3" + BT + "." + NL
)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for ruta in ("docs/loop/_auditor_v201_acta_seccion.md",
                 "docs/loop/ACTA_AUDITOR.md"):
        t = io.open(ruta, encoding="utf-8").read()
        antes = t.count(NL)
        n = t.count(ROTO)
        t = t.replace(ROTO, BUENO)
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        print("%-44s bloques reparados: %d | lineas %d -> %d"
              % (ruta, n, antes + 1, t.count(NL) + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
