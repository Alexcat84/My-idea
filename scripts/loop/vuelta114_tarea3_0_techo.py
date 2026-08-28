# -*- coding: utf-8 -*-
r"""vuelta114_tarea3_0_techo.py . EL TECHO DE LA TAREA 3 DE LA VUELTA 114,
DECLARADO Y SELLADO EN SU PROPIO COMMIT ANTES DE LA PRIMERA MEDICION (mismo
patron que vuelta113_tarea3_1_censo_territorio.py: el fichero nace solo, con
su script, en un commit propio, y la lectura/medicion real llega despues).

QUE DECLARA. El ALCANCE EXACTO de lo que esta vuelta va a medir en la TAREA
3, contado de sus ficheros de origen, SIN todavia calcular quien bloquea a
quien ni que arista falta (eso es la medicion, no el techo):

  (a) FASE 04_ENLACES: cuantas filas trae en docs/plan/OPERACIONES.jsonl.
  (b) OP-E-01: cuantas filas trae docs/plan/OP_E_01_DECIDIDAS.jsonl (sus
      pares "decididos").
  (c) FASE 05_SANEO: cuantas filas trae en docs/plan/OPERACIONES.jsonl.

USO:
  python scripts/loop/vuelta114_tarea3_0_techo.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def leer_jsonl(rel):
    ruta = os.path.join(RAIZ, rel)
    filas = []
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            filas.append(json.loads(linea))
    return filas


def main():
    ops = leer_jsonl("docs/plan/OPERACIONES.jsonl")
    fase04 = [r for r in ops if r.get("fase") == "04_ENLACES"]
    fase05 = [r for r in ops if r.get("fase") == "05_SANEO"]
    opE01 = leer_jsonl("docs/plan/OP_E_01_DECIDIDAS.jsonl")

    print("TECHO DE LA TAREA 3, VUELTA 114, DECLARADO ANTES DE MEDIR.")
    print("=" * 78)
    print()
    print("(a) FASE 04_ENLACES en docs/plan/OPERACIONES.jsonl: %d fila(s)." % len(fase04))
    for r in sorted(fase04, key=lambda r: r.get("id_op", "")):
        print("    %s" % r.get("id_op"))
    print()
    print("(b) docs/plan/OP_E_01_DECIDIDAS.jsonl: %d fila(s) decididas." % len(opE01))
    print()
    print("(c) FASE 05_SANEO en docs/plan/OPERACIONES.jsonl: %d fila(s)." % len(fase05))
    for r in sorted(fase05, key=lambda r: r.get("id_op", "")):
        print("    %s" % r.get("id_op"))
    print()
    print("TOTAL OPERACIONES.jsonl (contraste, no techo de lectura): %d fila(s)." % len(ops))
    print()
    print("Este techo se mide EN LOS COMMITS SIGUIENTES (3.1 censo fase 04, 3.2 OP-E-01")
    print("contra el grafo, 3.3 registro aditivo en 04_ENLACES.md, 3.4 censo fase 05).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
