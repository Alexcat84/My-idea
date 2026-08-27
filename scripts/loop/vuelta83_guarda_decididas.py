# -*- coding: utf-8 -*-
"""vuelta83_guarda_decididas.py . TAREA 2.b de la vuelta 83.

LA GUARDA DEL REGISTRO, ROJO con exit 1 (adjudicacion 5.2 del acta de la
vuelta 82). Cruza docs/plan/OP_E_01_DECIDIDAS.jsonl (o el registro que se
pase con --registro) contra una bolsa filtrada (--bolsa RUTA, en orden de
fichero, la misma cabeza que se lee): toda unidad de la bolsa que tenga
decision NO SE ENLAZA en el registro tiene que caer DENTRO del PREFIJO de
decididas (las primeras N unidades, sin huecos); si una unidad decidida
aparece POR DETRAS de una sin decidir, es ROJO, exit 1: una unidad se salto
sin leer.

USO:
  python scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl
  python scripts/loop/vuelta83_guarda_decididas.py --bolsa RUTA --registro RUTA_COPIA_ADULTERADA

SALIDA: VERDE (exit 0) con el prefijo y el primer indice sin decidir; ROJO
(exit 1) nombrando la unidad decidida que aparece detras de una sin decidir.
"""
import argparse
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def cargar_jsonl(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bolsa", required=True, help="bolsa filtrada jsonl, en orden de fichero")
    ap.add_argument("--registro", default="docs/plan/OP_E_01_DECIDIDAS.jsonl")
    a = ap.parse_args()

    ruta_bolsa = a.bolsa if os.path.isabs(a.bolsa) else os.path.join(RAIZ, a.bolsa)
    ruta_reg = a.registro if os.path.isabs(a.registro) else os.path.join(RAIZ, a.registro)

    bolsa = cargar_jsonl(ruta_bolsa)
    registro = cargar_jsonl(ruta_reg)

    decididas_no_enlaza = {}
    for r in registro:
        if r["decision"] == "NO SE ENLAZA":
            decididas_no_enlaza[(r["madre"], r["hijo"])] = r

    print("=" * 78)
    print("LA GUARDA DEL REGISTRO DE DECIDIDAS, TAREA 2.b vuelta 83")
    print("bolsa: %s (%d filas)" % (a.bolsa, len(bolsa)))
    print("registro: %s (%d filas, %d NO SE ENLAZA)" % (a.registro, len(registro), len(decididas_no_enlaza)))
    print("=" * 78)
    print()

    banderas = []
    for i, fila in enumerate(bolsa):
        clave = (fila["madre"], fila["hijo"])
        banderas.append(clave in decididas_no_enlaza)

    primer_sin_decidir = None
    for i, b in enumerate(banderas):
        if not b:
            primer_sin_decidir = i
            break

    if primer_sin_decidir is None:
        prefijo_len = len(banderas)
        rojos = []
    else:
        prefijo_len = primer_sin_decidir
        rojos = [i for i in range(primer_sin_decidir, len(banderas)) if banderas[i]]

    print("prefijo de decididas: indices 0 a %d (%d unidades)"
          % (prefijo_len - 1 if prefijo_len else -1, prefijo_len))
    if primer_sin_decidir is None:
        print("TODA LA BOLSA ESTA DECIDIDA.")
    else:
        fila = bolsa[primer_sin_decidir]
        print("primera unidad SIN DECIDIR: indice %d, %s -> %s (paso %s, dominio %s)"
              % (primer_sin_decidir, fila["madre"], fila["hijo"], fila.get("paso"), fila.get("dominio")))
    print()

    if rojos:
        print("ROJO: %d unidad(es) decidida(s) POR DETRAS de la primera sin decidir "
              "(indice %d): una unidad se salto sin leer" % (len(rojos), primer_sin_decidir))
        for i in rojos:
            fila = bolsa[i]
            r = decididas_no_enlaza[(fila["madre"], fila["hijo"])]
            print("   indice %d: %s -> %s | decidida en tramo %s (%s)"
                  % (i, fila["madre"], fila["hijo"], r["tramo"], r["fichero_origen"]))
        print("GUARDA: ROJO")
        return 1

    print("GUARDA: VERDE (ninguna unidad decidida aparece por detras de una sin decidir)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
