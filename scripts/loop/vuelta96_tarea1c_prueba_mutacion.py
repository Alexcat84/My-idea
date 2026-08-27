# -*- coding: utf-8 -*-
r"""vuelta96_tarea1c_prueba_mutacion.py . LA PRUEBA DE MUTACION de la mecanica
de ROJO de scripts/loop/vuelta96_tarea1c_etiqueta_grupo_c.py.

POR QUE NACE (EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION", 29 ago
2026, nacida de la caida 2 de la vuelta 89: un caso rojo cuya variable de
veredicto era una CONSTANTE LITERAL y por tanto no podia fallar nunca). Aqui la
mutacion se hace SOBRE DATO REAL EN MEMORIA y sobre el PARAMETRO REAL que
gobierna la guarda; no hay ninguna cadena tecleada haciendo de veredicto.

LAS DOS GUARDAS QUE SI SE PRUEBAN:
  (i)  una fila de OP_E_07_DIRECCION_V94.jsonl sin su puesto_intra en
       INTRA_DOMINIO_VEREDICTOS.jsonl. MUTACION: se borra de una COPIA EN
       MEMORIA del fichero de veredictos la entrada de un puesto que si existe,
       y la guarda tiene que CAER.
  (ii) el grupo C no trae exactamente 18 filas. MUTACION: se le pide a medir()
       un tamano esperado de 17 sobre el dato REAL sin tocar, y la guarda tiene
       que CAER.

LA GUARDA QUE NO TIENE CASO ROJO AUTOMATICO, Y SE DECLARA EN VEZ DE FABRICARLO:
la guarda (iii) ("una fila del grupo C que ademas casa el patron A del acta")
es una TAUTOLOGIA mientras el mismo clasifica_razon() alimente las dos cosas:
una fila que casa PATRONES_A nunca sale clasificada como C, asi que la guarda
no puede dispararse por ningun dato. No se le fabrica una mutacion que la
apruebe sola: SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO PARA ELLA, y queda
como asercion de auto consistencia, util solo si alguien separa las dos piezas
en el futuro.

USO:
  python scripts/loop/vuelta96_tarea1c_prueba_mutacion.py
"""
import copy
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta96_tarea1c_etiqueta_grupo_c as mod  # noqa: E402


def main():
    salida = []
    ok = True

    # --- CONTROL: el dato real, sin tocar, tiene que dar VERDE ---
    filas, fallos = mod.medir()
    verde = (not fallos) and len(filas) == 18
    salida.append("CONTROL (dato real, sin mutar): filas %d, fallos %d -> %s"
                  % (len(filas), len(fallos), "VERDE" if verde else "ROJO"))
    ok = ok and verde

    # --- MUTACION (ii): el tamano esperado, que es PARAMETRO REAL de la guarda ---
    filas_m, fallos_m = mod.medir(tamano_esperado_c=17)
    cayo_ii = any("se esperaban 17" in f for f in fallos_m)
    salida.append("MUTACION (ii) tamano esperado 17 sobre dato real: fallos %d -> %s"
                  % (len(fallos_m), "CAE (correcto)" if cayo_ii else "NO CAE (la guarda no sirve)"))
    for f in fallos_m:
        salida.append("    %s" % f)
    ok = ok and cayo_ii

    # --- MUTACION (i): copia EN MEMORIA del fichero de veredictos, sin una entrada ---
    original = mod.cargar_jsonl
    entrada_real = original(mod.ENTRADA)
    veredictos_real = original(mod.VEREDICTOS)
    puesto_victima = entrada_real[0]["puesto"]

    def cargar_mutado(ruta):
        if ruta == mod.VEREDICTOS:
            copia = copy.deepcopy(veredictos_real)
            return [v for v in copia if int(v["puesto_intra"]) != puesto_victima]
        return copy.deepcopy(entrada_real)

    mod.cargar_jsonl = cargar_mutado
    try:
        _, fallos_i = mod.medir()
    finally:
        mod.cargar_jsonl = original

    cayo_i = any("puesto %s no tiene puesto_intra" % puesto_victima in f for f in fallos_i)
    salida.append("MUTACION (i) copia en memoria sin el veredicto del puesto %s: fallos %d -> %s"
                  % (puesto_victima, len(fallos_i), "CAE (correcto)" if cayo_i else "NO CAE (la guarda no sirve)"))
    for f in fallos_i:
        salida.append("    %s" % f)
    ok = ok and cayo_i

    # --- LA QUE NO SE PRUEBA, DICHA ---
    salida.append("GUARDA (iii) 'esta en C y casa el patron A': NO HAY CASO ROJO AUTOMATICO.")
    salida.append("    Es tautologia mientras clasifica_razon() alimente las dos piezas:")
    salida.append("    una razon que casa PATRONES_A no sale clasificada C. No se le fabrica")
    salida.append("    una mutacion que la apruebe sola; se declara.")

    # --- EL CONTROL VUELVE A VERDE tras deshacer la mutacion (que no quede pegada) ---
    filas_v, fallos_v = mod.medir()
    vuelve = (not fallos_v) and len(filas_v) == 18
    salida.append("CONTROL DE VUELTA (mutacion deshecha): filas %d, fallos %d -> %s"
                  % (len(filas_v), len(fallos_v), "VERDE" if vuelve else "ROJO"))
    ok = ok and vuelve

    print("=" * 90)
    print("PRUEBA DE MUTACION DE LA MECANICA DE ROJO (vuelta 96, TAREA 1.c)")
    print("=" * 90)
    print()
    for l in salida:
        print(l)
    print()
    print("VEREDICTO: %s" % ("VERDE, las dos guardas probadas CAEN al mutarlas y el control sigue verde"
                             if ok else "ROJO, alguna guarda no se comporta"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
