# -*- coding: utf-8 -*-
"""vuelta109_tarea2_4_prueba_mutacion.py . CASO ROJO POR MUTACION de
verificar_vuelco_de_veredicto.py (TAREA 2.4 de la vuelta 109).

Sobre una COPIA de docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md
(docs/loop/_v109_mut/TRAMO3_SIN_DECLARACION_123.md) con las DOS menciones
que declaran el vuelco del 123 borradas (la de su propia fila, "ya barrido
SATELITE en la vuelta 106 y SOSTENIDO tras lectura entera", y la de la
linea de resumen del mismo fichero, "123 sostenido en la vuelta 106"),
puesta EN EL LUGAR del fichero real via `verificar(overrides=...)`: el 123
tiene que pasar de DECLARADO a MUDO. El fichero real (sin mutar) sigue
dando DECLARADO. Si el mutado tambien diera DECLARADO, el instrumento no
estaria leyendo la declaracion de verdad.

USO: python scripts/loop/vuelta109_tarea2_4_prueba_mutacion.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_vuelco_de_veredicto as m  # noqa: E402

RUTA_MUTADA = os.path.join(RAIZ, "docs", "loop", "_v109_mut", "TRAMO3_SIN_DECLARACION_123.md")


def veredicto_del_123(vuelcos):
    for v in vuelcos:
        if v["puesto"] == 123:
            return v["declarado"]
    raise SystemExit("el 123 no aparece como vuelco: la prueba no mide nada")


def main():
    fallos_real, vuelcos_real = m.verificar()
    if fallos_real:
        print("ROJO inesperado sobre el fichero REAL:", fallos_real)
        return 1
    declarado_real = veredicto_del_123(vuelcos_real)
    print("CONTROL (fichero real, sin mutar): 123 -> %s" % ("DECLARADO" if declarado_real else "MUDO"))

    overrides = {"SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md": RUTA_MUTADA}
    fallos_mut, vuelcos_mut = m.verificar(overrides=overrides)
    if fallos_mut:
        print("ROJO inesperado sobre el fichero MUTADO:", fallos_mut)
        return 1
    declarado_mut = veredicto_del_123(vuelcos_mut)
    print("MUTADO (declaracion del 123 borrada): 123 -> %s" % ("DECLARADO" if declarado_mut else "MUDO"))

    if declarado_real and not declarado_mut:
        print("\nVERDE: la guarda MUERDE. Con la declaracion borrada, el 123 cae a MUDO; "
              "con el fichero real, sigue DECLARADO.")
        return 0
    print("\nROJO: la mutacion no cambio el veredicto del 123 (real=%s, mutado=%s): "
          "la guarda no esta leyendo la declaracion de verdad." % (declarado_real, declarado_mut))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
