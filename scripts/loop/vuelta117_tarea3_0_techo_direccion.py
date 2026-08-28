# -*- coding: utf-8 -*-
r"""vuelta117_tarea3_0_techo_direccion.py . EL TECHO NUEVO DE LA TAREA 3.0 DE
LA VUELTA 117, DECLARADO Y SELLADO EN SU PROPIO COMMIT ANTES DE MEDIR NADA
(mismo patron que vuelta114_tarea3_0_techo.py, que esta vuelta re-corre tal
cual sobre OPERACIONES.jsonl y OP_E_01_DECIDIDAS.jsonl).

QUE DECLARA. El ALCANCE EXACTO de las filas de los ficheros de DIRECCION de
OP-E-06 y de OP-E-07 (los addenda de ejecucion de las vueltas 90 y 91-94),
que la TAREA 3.1 de esta vuelta va a resolver por alias contra el grafo, SIN
todavia resolver nada:

  (a) docs/plan/OP_E_06_DIRECCION_V90.jsonl: cuantas filas trae (unico
      fichero de direccion de OP-E-06, no hay V91, V92... para esta
      operacion).
  (b) docs/plan/OP_E_07_DIRECCION_V9*.jsonl: CUANTOS ficheros hay con este
      patron y CUAL ES EL ULTIMO (el de version mas alta), porque la nomina
      de verdad es la del ULTIMO, no la del primero (encargo de la vuelta
      117, TAREA 3.0). Se listan TODOS con su cuenta de filas, y se declara
      cual es el elegido.

USO:
  python scripts/loop/vuelta117_tarea3_0_techo_direccion.py
"""
import glob
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def leer_jsonl(ruta_abs):
    filas = []
    with open(ruta_abs, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            filas.append(json.loads(linea))
    return filas


def main():
    print("TECHO NUEVO DE LA TAREA 3.0, VUELTA 117, DECLARADO ANTES DE MEDIR.")
    print("=" * 78)
    print()

    ruta_e06 = os.path.join(RAIZ, "docs", "plan", "OP_E_06_DIRECCION_V90.jsonl")
    filas_e06 = leer_jsonl(ruta_e06)
    print("(a) docs/plan/OP_E_06_DIRECCION_V90.jsonl: %d fila(s)." % len(filas_e06))
    print()

    patron = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V9*.jsonl")
    candidatos = sorted(glob.glob(patron))
    print("(b) docs/plan/OP_E_07_DIRECCION_V9*.jsonl: %d fichero(s) encontrados:" % len(candidatos))
    versiones = []
    for ruta in candidatos:
        nombre = os.path.basename(ruta)
        m = re.search(r"_V(\d+)\.jsonl$", nombre)
        version = int(m.group(1)) if m else -1
        filas = leer_jsonl(ruta)
        versiones.append((version, nombre, len(filas)))
        print("    %s: %d fila(s) (version V%d)" % (nombre, len(filas), version))

    if not versiones:
        print("    NINGUNO encontrado.")
        print()
        print("ROJO: no hay ningun OP_E_07_DIRECCION_V9*.jsonl que elegir.")
        return 1

    version_max, nombre_ultimo, filas_ultimo = max(versiones, key=lambda t: t[0])
    print()
    print("EL ULTIMO (version mas alta): %s, %d fila(s)." % (nombre_ultimo, filas_ultimo))
    print()
    print("TECHO PARA LA TAREA 3.1: OP-E-06 direccion %d fila(s) (V90); OP-E-07 direccion "
          "%d fila(s) (%s, el ultimo de %d ficheros)."
          % (len(filas_e06), filas_ultimo, nombre_ultimo, len(versiones)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
