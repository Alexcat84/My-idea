# -*- coding: utf-8 -*-
"""vuelta113_tarea2_mutacion_tsc.py . MUTACION V (verde) y MUTACION W (rojo)
de la TAREA 2.1/2.2/2.3 de la vuelta 113: prueba que
tallar_cabecera_reporte.interpretar_tsc() distingue un tsc LIMPIO (solo el
marcador EXIT=0) de un tsc SUCIO (una linea de error real mas EXIT=1), y que
las dos celdas salen DISTINTAS.

Ver el docstring de tallar_cabecera_reporte.py, seccion "TAREA 2.1", para el
porque de la caida que esto repara (acta de la vuelta 112, "TU CAIDA GRANDE
ES DE GUARDA CEGADA").

USO:
  python scripts/loop/vuelta113_tarea2_mutacion_tsc.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tallar_cabecera_reporte import interpretar_tsc

MUTACION_V = "EXIT=0\n"
MUTACION_W = "web/lib/x.ts(3,5): error TS2304: Cannot find name 'foo'.\nEXIT=1\n"


def main():
    celda_v = interpretar_tsc(MUTACION_V)
    celda_w = interpretar_tsc(MUTACION_W)

    print("MUTACION V (solo el marcador EXIT=0):")
    print("  contenido: %r" % MUTACION_V)
    print("  celda tallada: %s" % celda_v)
    print()
    print("MUTACION W (una linea de error real mas EXIT=1):")
    print("  contenido: %r" % MUTACION_W)
    print("  celda tallada: %s" % celda_w)
    print()

    fallos = []
    if celda_v != "EXITCODE 0, cero lineas":
        fallos.append("MUTACION V: se esperaba 'EXITCODE 0, cero lineas' (tsc LIMPIO), salio %r" % celda_v)
    if "error TS2304" not in celda_w:
        fallos.append("MUTACION W: la celda no nombra la linea de error: %r" % celda_w)
    if celda_v == celda_w:
        fallos.append("MUTACION V y W dieron la MISMA celda: la guarda no distingue limpio de sucio")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: V da tsc LIMPIO, W da una celda DISTINTA que nombra la linea de error.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
