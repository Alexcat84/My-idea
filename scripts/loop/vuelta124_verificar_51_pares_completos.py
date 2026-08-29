# -*- coding: utf-8 -*-
"""vuelta124_verificar_51_pares_completos.py . GUARDA de la TAREA 3.a/3.b de
la vuelta 124: confirma que los 51 pares del racimo de OP-S-09 (39 de la
vuelta 123 + 12 de la vuelta 124) estan LEIDOS Y REGISTRADOS antes de que la
ejecucion de OP-S-09 (TAREA 3.b) pueda empezar.

Compara, familia por familia, los pares de
docs/loop/SALIDA_V123_OPS09_LECTURA.jsonl + SALIDA_V124_OPS09_LECTURA_RESTO.jsonl
contra la suma de C(n,2) sobre los miembros de cada familia. ROJO EXIT 1 si
falta algun par o sobra alguno (duplicado entre los dos ficheros).

USO:
  python scripts/loop/vuelta124_verificar_51_pares_completos.py
"""
import itertools
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_39 = os.path.join(RAIZ, "docs", "loop", "SALIDA_V123_OPS09_LECTURA.jsonl")
RUTA_12 = os.path.join(RAIZ, "docs", "loop", "SALIDA_V124_OPS09_LECTURA_RESTO.jsonl")


def leer(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def main():
    filas_39 = leer(RUTA_39)
    filas_12 = leer(RUTA_12)

    miembros_por_familia = {f["familia"]: f["miembros"] for f in filas_39}
    for f in filas_12:
        if f["familia"] not in miembros_por_familia:
            raise SystemExit("ROJO: familia %s del RESTO no esta en el registro de 39" % f["familia"])
        if sorted(f["miembros"]) != sorted(miembros_por_familia[f["familia"]]):
            raise SystemExit("ROJO: miembros de %s difieren entre los dos registros" % f["familia"])

    pares_por_familia = {f["familia"]: set() for f in filas_39}
    for f in filas_39:
        for p in f["pares"]:
            pares_por_familia[f["familia"]].add(tuple(sorted((p["a"], p["b"]))))
    for f in filas_12:
        for p in f["pares"]:
            par = tuple(sorted((p["a"], p["b"])))
            if par in pares_por_familia[f["familia"]]:
                raise SystemExit("ROJO: par %s duplicado entre los dos registros" % (par,))
            pares_por_familia[f["familia"]].add(par)

    total_registrado = sum(len(v) for v in pares_por_familia.values())
    total_esperado = 0
    faltan = []
    for familia, miembros in miembros_por_familia.items():
        n = len(miembros)
        c_n_2 = n * (n - 1) // 2
        total_esperado += c_n_2
        for a, b in itertools.combinations(sorted(miembros), 2):
            if tuple(sorted((a, b))) not in pares_por_familia[familia]:
                faltan.append((familia, a, b))

    if faltan:
        print("ROJO EXIT 1: %d par(es) del racimo SIN leer:" % len(faltan))
        for familia, a, b in faltan:
            print("  %s: %s <-> %s" % (familia, a, b))
        return 1

    print("VERDE EXIT 0: %d familias, %d pares TOTALES del racimo, %d registrados en los dos ficheros. "
          "TODOS leidos, cero faltantes, cero duplicados entre ficheros."
          % (len(miembros_por_familia), total_esperado, total_registrado))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
