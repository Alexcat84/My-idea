# -*- coding: utf-8 -*-
"""vuelta107_contar_tres_vias.py . TALLA LA CIFRA DE LA TAREA 4.3 (vuelta 107)
CONTANDO docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md, no tecleandola
(EJECUTOR.md, "LA TABLA SE CUENTA DE SU FICHERO").

QUE MIDE: cada linea de datos del fichero (empieza con `puesto | `) trae un
veredicto OBJETO, SATELITE o NO_OBJETO inmediatamente despues del ultimo
`| hijo | ` de la linea. Cuenta cuantas de cada clase hay y las imprime.

USO:
  python scripts/loop/vuelta107_contar_tres_vias.py
"""
import re

RUTA = "docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md"
RE_FILA = re.compile(r"^(\d+) \|.*\| (OBJETO|SATELITE|NO_OBJETO)\b")


def main():
    with open(RUTA, encoding="utf-8") as f:
        lineas = f.readlines()

    veredictos = {}
    for l in lineas:
        m = RE_FILA.match(l)
        if m:
            veredictos[int(m.group(1))] = m.group(2)

    n = len(veredictos)
    objeto = sum(1 for v in veredictos.values() if v == "OBJETO")
    satelite = sum(1 for v in veredictos.values() if v == "SATELITE")
    no_objeto = sum(1 for v in veredictos.values() if v == "NO_OBJETO")

    print("n=%d puestos" % n)
    print("OBJETO: %d" % objeto)
    print("SATELITE: %d -- %s" % (satelite, sorted(p for p, v in veredictos.items() if v == "SATELITE")))
    print("NO_OBJETO: %d -- %s" % (no_objeto, sorted(p for p, v in veredictos.items() if v == "NO_OBJETO")))
    assert n == objeto + satelite + no_objeto


if __name__ == "__main__":
    main()
