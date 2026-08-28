# -*- coding: utf-8 -*-
"""vuelta111_tarea3_1_censo_satelite_no_resuelta.py . TAREA 3.1 de la vuelta
111 (encargo del auditor, acta de la vuelta 110, TAREA 3: "LOS CINCO
SATELITE QUE NADIE HA VUELTO A LEER").

QUE HACE. Cruza las NO RESUELTA de hoy (`contar_cierre_efectivo.cifras()`,
campo `sin_dir`) contra los puestos que SI recibieron la pregunta de tres
vias (misma extraccion que usa `verificar_cobertura_bolsa_tres_vias.py`
sobre `FICHEROS_VEREDICTO`), y de esos, cuales dieron SATELITE. RECUENTA
PRIMERO, ANTES DE LEER NINGUN PAR: la letra del encargo pide declarar la
cifra antes de leer, y pararse si la nomina no calza con la que trae el
encargo (109 NO RESUELTA, 104 SIN VEREDICTO, 5 SATELITE: 20, 21, 38, 66, 93).

USO: python scripts/loop/vuelta111_tarea3_1_censo_satelite_no_resuelta.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce  # noqa: E402
import verificar_cobertura_bolsa_tres_vias as vcb  # noqa: E402

CIFRA_ESPERADA_NO_RESUELTA = 109
CIFRA_ESPERADA_SATELITE = {20, 21, 38, 66, 93}


def veredicto_de(puesto, ficheros, fallos):
    """Devuelve el veredicto (OBJETO/SATELITE/NO_OBJETO) de `puesto` en el
    PRIMER fichero de FICHEROS_VEREDICTO (en orden) que lo mencione, igual
    orden que usa verificar_vuelco_de_veredicto para 'el mas viejo'."""
    for nombre, formato in ficheros:
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        if formato == "bloque":
            for linea in texto.splitlines():
                m = vcb.RE_BLOQUE_CABECERA.match(linea)
                if m and int(m.group(1)) == puesto:
                    idx = texto.splitlines().index(linea)
                    for sig in texto.splitlines()[idx + 1:]:
                        if sig.strip() == "" or vcb.RE_BLOQUE_CABECERA.match(sig):
                            break
                        vm = vcb.RE_BLOQUE_VEREDICTO.search(sig)
                        if vm:
                            return vm.group(1), nombre
        elif formato == "tabla":
            for linea in texto.splitlines():
                m = vcb.RE_TABLA_FILA.match(linea)
                if m and int(m.group(1)) == puesto:
                    return m.group(2), nombre
    return None, None


def main():
    fallos = []
    d, f = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if f:
        print("ROJO:", f)
        return 1
    no_resuelta = sorted(d["sin_dir"])
    print("NO RESUELTA de hoy (contar_cierre_efectivo.cifras, sin_dir): %d" % len(no_resuelta))

    ficheros = list(vcb.FICHEROS_VEREDICTO)
    con_pregunta_todos = vcb.puestos_con_pregunta(ficheros, fallos)
    if fallos:
        print("ROJO:", fallos)
        return 1

    no_resuelta_con_pregunta = sorted(set(no_resuelta) & con_pregunta_todos)
    no_resuelta_sin_pregunta = sorted(set(no_resuelta) - con_pregunta_todos)
    print("de esas, con veredicto de tres vias: %d" % len(no_resuelta_con_pregunta))
    print("de esas, SIN veredicto de tres vias: %d" % len(no_resuelta_sin_pregunta))

    satelite = []
    for p in no_resuelta_con_pregunta:
        v, nombre = veredicto_de(p, ficheros, fallos)
        print("   puesto %d: %s (%s)" % (p, v, nombre))
        if v == "SATELITE":
            satelite.append(p)

    print()
    print("SATELITE entre las NO RESUELTA con pregunta: %d -- %s" % (len(satelite), satelite))

    ok = True
    if len(no_resuelta) != CIFRA_ESPERADA_NO_RESUELTA:
        print("PARA Y LO TRAE: NO RESUELTA es %d, el encargo dice %d" %
              (len(no_resuelta), CIFRA_ESPERADA_NO_RESUELTA))
        ok = False
    if set(satelite) != CIFRA_ESPERADA_SATELITE:
        print("PARA Y LO TRAE: SATELITE es %s, el encargo dice %s" %
              (sorted(satelite), sorted(CIFRA_ESPERADA_SATELITE)))
        ok = False

    if not ok:
        return 1
    print("\nVERDE: la nomina calza con la del encargo (109 NO RESUELTA, 5 SATELITE: %s)." %
          sorted(CIFRA_ESPERADA_SATELITE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
