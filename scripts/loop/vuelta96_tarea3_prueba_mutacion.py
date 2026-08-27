# -*- coding: utf-8 -*-
r"""vuelta96_tarea3_prueba_mutacion.py . LA PRUEBA DE MUTACION de las guardas de
scripts/loop/vuelta96_tarea3_tramo1_opE03.py y
scripts/loop/vuelta96_tarea3_veredictos_tramo1.py.

LO PRIMERO, Y ES UNA DECLARACION, NO UNA PRUEBA (EJECUTOR.md regla 1, "EL CASO
ROJO SE PRUEBA POR MUTACION", parrafo final): la CLASE A/B/C/D de cada uno de
los 40 pares la pone LA LECTURA del ejecutor y vive en una TABLA A MANO. NO HAY
NADA QUE MUTAR AHI y por tanto NO HAY CASO ROJO AUTOMATICO PARA LA CLASE. Se
declara en vez de fabricar una asercion que se apruebe sola, que es exactamente
la caida 2 de la vuelta 89.

LO QUE SI SE PRUEBA, porque es mecanico y gobierna lo que se publica:
  (A) UNA FILA DE LA BOLSA QUE YA ESTA EN LA COLA tiene que CAER. Es la guarda
      que sostiene la adjudicacion del 11 ago 2026 de OP-E-03 ("una lectura que
      entra por dos puertas se cuenta dos veces"). MUTACION: se le da al
      instrumento del material una bolsa EN MEMORIA cuya primera fila es un par
      sacado de docs/INTRA_DOMINIO_PARES.jsonl, o sea que SI esta en la cola.
  (B) EL CRIBADO NO CERRADO tiene que CAER. MUTACION: se le pide el corte 3389
      sobre el dato real.
  (C) UNA CLASE FUERA DE {A,B,C,D} tiene que CAER.
  (D) UN VEREDICTO QUE NO CORRESPONDE A NINGUNA FILA del tramo tiene que CAER.
  (E) UNA DIRECCION QUE NOMBRA UN NODO AJENO a esa fila tiene que CAER. Es la
      guarda que impide publicar una direccion inventada.
  (F) UN VEREDICTO QUE FALTA tiene que CAER.

USO:
  python scripts/loop/vuelta96_tarea3_prueba_mutacion.py
"""
import copy
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta96_tarea3_tramo1_opE03 as mat  # noqa: E402
import vuelta96_tarea3_veredictos_tramo1 as ver  # noqa: E402


def main():
    lineas = []
    ok = True

    # --- CONTROL ---
    filas_m, fallos_m, _, total, _ = mat.reunir()
    filas_v, fallos_v, _ = ver.construir_filas()
    control = (not fallos_m) and (not fallos_v) and len(filas_m) == 40 and len(filas_v) == 40
    lineas.append("CONTROL (dato real): material %d filas / %d fallos, veredictos %d filas / %d fallos -> %s"
                  % (len(filas_m), len(fallos_m), len(filas_v), len(fallos_v), "VERDE" if control else "ROJO"))
    ok = ok and control

    # --- MUTACION A: una fila que YA ESTA EN LA COLA ---
    original = mat.cargar_jsonl
    bolsa_real = original(mat.BOLSA)
    pares_real = original(mat.PARES)
    veredictos_real = original(mat.VEREDICTOS)
    intruso = pares_real[0]
    bolsa_mutada = ([{"dominio": intruso.get("dominio"), "madre": intruso["nodo_a"], "hijo": intruso["nodo_b"],
                      "paso": 1, "texto_paso": "fila inyectada por la prueba de mutacion"}]
                    + copy.deepcopy(bolsa_real))

    def cargar_mut_a(ruta):
        if ruta == mat.BOLSA:
            return copy.deepcopy(bolsa_mutada)
        return copy.deepcopy(original(ruta))

    mat.cargar_jsonl = cargar_mut_a
    try:
        _, fallos_a, _, _, _ = mat.reunir()
    finally:
        mat.cargar_jsonl = original
    cayo_a = any("YA ESTA EN LA COLA" in f for f in fallos_a)
    lineas.append("MUTACION A (bolsa en memoria con un par que SI esta en la cola, %s / %s): fallos %d -> %s"
                  % (intruso["nodo_a"], intruso["nodo_b"], len(fallos_a),
                     "CAE (correcto)" if cayo_a else "NO CAE (la guarda no sirve)"))
    for f in fallos_a[:3]:
        lineas.append("    %s" % f)
    ok = ok and cayo_a

    # --- MUTACION B: el cribado no cerrado ---
    _, fallos_b, _, _, _ = mat.reunir(corte=3389)
    cayo_b = any("no esta cerrado en 3389" in f for f in fallos_b)
    lineas.append("MUTACION B (corte esperado 3389 sobre el dato real): fallos %d -> %s"
                  % (len(fallos_b), "CAE (correcto)" if cayo_b else "NO CAE (la guarda no sirve)"))
    for f in fallos_b:
        lineas.append("    %s" % f)
    ok = ok and cayo_b

    # --- MUTACION C: una clase invalida ---
    v_mut = [(n, "Z" if n == 1 else c, d, r) for n, c, d, r in ver.VEREDICTOS]
    _, fallos_c, _ = ver.construir_filas(veredictos=v_mut)
    cayo_c = any("no es A, B, C ni D" in f for f in fallos_c)
    lineas.append("MUTACION C (clase 'Z' en el par 1): fallos %d -> %s"
                  % (len(fallos_c), "CAE (correcto)" if cayo_c else "NO CAE (la guarda no sirve)"))
    ok = ok and cayo_c

    # --- MUTACION D: un veredicto que no corresponde a ninguna fila ---
    v_mut2 = [(999 if n == 1 else n, c, d, r) for n, c, d, r in ver.VEREDICTOS]
    _, fallos_d, _ = ver.construir_filas(veredictos=v_mut2)
    cayo_d = any("no corresponde a ninguna fila" in f for f in fallos_d)
    lineas.append("MUTACION D (el par 1 renumerado a 999): fallos %d -> %s"
                  % (len(fallos_d), "CAE (correcto)" if cayo_d else "NO CAE (la guarda no sirve)"))
    ok = ok and cayo_d

    # --- MUTACION E: una direccion que nombra un nodo ajeno ---
    v_mut3 = [(n, c, "nodo_inventado -> get_out_of_the_building" if n == 1 else d, r)
              for n, c, d, r in ver.VEREDICTOS]
    _, fallos_e, _ = ver.construir_filas(veredictos=v_mut3)
    cayo_e = any("que no son los dos nodos" in f for f in fallos_e)
    lineas.append("MUTACION E (direccion del par 1 con un nodo ajeno): fallos %d -> %s"
                  % (len(fallos_e), "CAE (correcto)" if cayo_e else "NO CAE (la guarda no sirve)"))
    ok = ok and cayo_e

    # --- MUTACION F: un veredicto que falta ---
    v_mut4 = [t for t in ver.VEREDICTOS if t[0] != 40]
    _, fallos_f, _ = ver.construir_filas(veredictos=v_mut4)
    cayo_f = any("faltan veredictos para las filas" in f for f in fallos_f)
    lineas.append("MUTACION F (sin el veredicto del par 40): fallos %d -> %s"
                  % (len(fallos_f), "CAE (correcto)" if cayo_f else "NO CAE (la guarda no sirve)"))
    for f in fallos_f:
        lineas.append("    %s" % f)
    ok = ok and cayo_f

    # --- CONTROL DE VUELTA ---
    filas_m2, fallos_m2, _, _, _ = mat.reunir()
    filas_v2, fallos_v2, _ = ver.construir_filas()
    vuelve = (not fallos_m2) and (not fallos_v2) and len(filas_m2) == 40 and len(filas_v2) == 40
    lineas.append("CONTROL DE VUELTA (mutaciones deshechas): material %d/%d, veredictos %d/%d -> %s"
                  % (len(filas_m2), len(fallos_m2), len(filas_v2), len(fallos_v2), "VERDE" if vuelve else "ROJO"))
    ok = ok and vuelve

    print("=" * 100)
    print("PRUEBA DE MUTACION DE LAS GUARDAS DE OP-E-03, TRAMO 1 (vuelta 96, TAREA 3)")
    print("=" * 100)
    print()
    for l in lineas:
        print(l)
    print()
    print("LO QUE NO SE PRUEBA, Y SE DICE: la CLASE A/B/C/D de cada par es tabla a mano.")
    print("NO HAY CASO ROJO AUTOMATICO PARA ELLA. No se le fabrica uno que se apruebe solo.")
    print()
    print("VEREDICTO: %s" % ("VERDE, las seis mutaciones CAEN y el control vuelve a verde"
                             if ok else "ROJO, alguna guarda no se comporta"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
