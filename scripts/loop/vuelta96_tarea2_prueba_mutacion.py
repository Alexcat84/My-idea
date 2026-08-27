# -*- coding: utf-8 -*-
r"""vuelta96_tarea2_prueba_mutacion.py . LA PRUEBA DE MUTACION de
scripts/loop/vuelta96_tarea2_vara_de_la_mesa.py y de
scripts/loop/vuelta96_tarea2_mesa_de_formula.py.

POR QUE NACE (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION", nacida
de la caida 2 de la vuelta 89: un caso rojo cuya variable de veredicto era una
CONSTANTE LITERAL y no podia fallar nunca). Todo lo que se muta aqui es dato
real o parametro real; no hay ninguna cadena tecleada haciendo de veredicto.

LO QUE SE PRUEBA:
  (A) LA COMPARACION DE LA VARA NO ES TAUTOLOGIA, en las dos direcciones.
      Sobre el dato real ya da 3 CHOCAN de 19, o sea que sabe decir que NO;
      falta probar que sabe decir que SI donde hoy dice que no, y al reves.
      MUTACION A1: se le da un expediente EN MEMORIA donde el veredicto
      publicado de un par que hoy CALZA se voltea. Ese par tiene que pasar a
      CHOCAR.
      MUTACION A2: se le da un expediente EN MEMORIA donde el veredicto
      publicado de un par que hoy CHOCA se voltea. Ese par tiene que pasar a
      CALZAR.
  (B) LA MECANICA DE ROJO de la vara: un puesto del expediente sin veredicto.
      MUTACION B: expediente EN MEMORIA con un puesto inventado que no existe
      en INTRA_DOMINIO_VEREDICTOS.jsonl. Tiene que CAER.
  (C) LA MECANICA DE ROJO de la mesa: un nodo del par que, ya resuelto, no
      existe en el grafo. MUTACION C: se le pasa una lista de ejemplares EN
      MEMORIA con un puesto que no tiene veredicto. Tiene que CAER.

USO:
  python scripts/loop/vuelta96_tarea2_prueba_mutacion.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta96_tarea2_vara_de_la_mesa as vara  # noqa: E402
import vuelta96_tarea2_mesa_de_formula as mesa  # noqa: E402

VOLTEA = {"QUEDA": "SALE", "SALE": "QUEDA"}


def main():
    lineas = []
    ok = True

    # --- CONTROL: el expediente real, sin tocar ---
    exp, vivos, fallos = vara.medir()
    calzan = [f for f in exp if f["calza"]]
    chocan = [f for f in exp if not f["calza"]]
    lineas.append("CONTROL (expediente real): %d filas, CALZAN %d, CHOCAN %d, fallos %d"
                  % (len(exp), len(calzan), len(chocan), len(fallos)))
    lineas.append("    CHOCAN nominal: %s" % ", ".join(str(f["puesto"]) for f in chocan))
    control_ok = (not fallos) and len(exp) == 19 and len(chocan) == 3
    ok = ok and control_ok
    lineas.append("    -> %s" % ("VERDE" if control_ok else "ROJO"))

    # --- MUTACION A1: voltear el publicado de uno que hoy CALZA ---
    victima_calza = calzan[0]["puesto"]
    exp_mut = [(p, VOLTEA[v] if p == victima_calza else v, s) for p, v, s in vara.EXPEDIENTE]
    exp_a1, _, _ = vara.medir(expediente=exp_mut)
    fila_a1 = [f for f in exp_a1 if f["puesto"] == victima_calza][0]
    cayo_a1 = not fila_a1["calza"]
    lineas.append("MUTACION A1 (puesto %d, que hoy CALZA, con su publicado volteado): calza=%s -> %s"
                  % (victima_calza, fila_a1["calza"], "CAE (correcto)" if cayo_a1 else "NO CAE (la comparacion no sirve)"))
    ok = ok and cayo_a1

    # --- MUTACION A2: voltear el publicado de uno que hoy CHOCA ---
    victima_choca = chocan[0]["puesto"]
    exp_mut2 = [(p, VOLTEA[v] if p == victima_choca else v, s) for p, v, s in vara.EXPEDIENTE]
    exp_a2, _, _ = vara.medir(expediente=exp_mut2)
    fila_a2 = [f for f in exp_a2 if f["puesto"] == victima_choca][0]
    subio_a2 = fila_a2["calza"]
    lineas.append("MUTACION A2 (puesto %d, que hoy CHOCA, con su publicado volteado): calza=%s -> %s"
                  % (victima_choca, fila_a2["calza"], "PASA A CALZAR (correcto)" if subio_a2 else "SIGUE CHOCANDO (la comparacion no sirve)"))
    ok = ok and subio_a2

    # --- MUTACION B: un puesto que no existe en los veredictos ---
    exp_mut3 = list(vara.EXPEDIENTE) + [(999999, "QUEDA", "puesto inventado por la prueba de mutacion")]
    _, _, fallos_b = vara.medir(expediente=exp_mut3)
    cayo_b = any("999999" in f for f in fallos_b)
    lineas.append("MUTACION B (expediente con el puesto inventado 999999): fallos %d -> %s"
                  % (len(fallos_b), "CAE (correcto)" if cayo_b else "NO CAE (la guarda no sirve)"))
    for f in fallos_b:
        lineas.append("    %s" % f)
    ok = ok and cayo_b

    # --- MUTACION C: la mecanica de rojo de la mesa ---
    cinco_original = mesa.LOS_CINCO
    mesa.LOS_CINCO = list(cinco_original) + [(999998, "INVENTADO", "puesto inventado por la prueba de mutacion")]
    try:
        _, fallos_c = mesa.reunir()
    finally:
        mesa.LOS_CINCO = cinco_original
    cayo_c = any("999998" in f for f in fallos_c)
    lineas.append("MUTACION C (mesa con el puesto inventado 999998): fallos %d -> %s"
                  % (len(fallos_c), "CAE (correcto)" if cayo_c else "NO CAE (la guarda no sirve)"))
    for f in fallos_c:
        lineas.append("    %s" % f)
    ok = ok and cayo_c

    # --- CONTROL DE VUELTA: nada quedo pegado ---
    exp_v, _, fallos_v = vara.medir()
    fichas_v, fallos_mv = mesa.reunir()
    vuelve = (not fallos_v) and len(exp_v) == 19 and (not fallos_mv) and len(fichas_v) == 5
    lineas.append("CONTROL DE VUELTA (mutaciones deshechas): vara %d filas / %d fallos, mesa %d fichas / %d fallos -> %s"
                  % (len(exp_v), len(fallos_v), len(fichas_v), len(fallos_mv), "VERDE" if vuelve else "ROJO"))
    ok = ok and vuelve

    print("=" * 100)
    print("PRUEBA DE MUTACION DE LA MESA Y DE SU VARA (vuelta 96, TAREA 2)")
    print("=" * 100)
    print()
    for l in lineas:
        print(l)
    print()
    print("VEREDICTO: %s" % ("VERDE, las cuatro mutaciones se comportan y el control vuelve a verde"
                             if ok else "ROJO, alguna guarda o comparacion no se comporta"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
