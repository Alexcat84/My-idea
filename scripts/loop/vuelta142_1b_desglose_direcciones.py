# -*- coding: utf-8 -*-
r"""vuelta142_1b_desglose_direcciones.py . EL DESGLOSE DE DIRECCIONES DE LA
FASE 06, COMPUTADO Y NO TECLEADO (TAREA 1.b de la vuelta 142, acta de la vuelta
141, caidas 4.1 del ejecutor y 4.4 del auditor).

POR QUE NACE. El acta 140, adjudicacion 3.4, publico "el total de la fase es 18
direcciones (2+9+4+2+1)" en la misma adjudicacion en que fijo que LA UNIDAD ES
LA DIRECCION. El 9 son FILAS DE FICHA de OP-E-04; en direcciones son 8. El
reporte de la 141 publico otro 18 (8+4+2+1+2+1) sobre SEIS operaciones, con
OP-M-05-APERTURA dentro, y declaro concordancia con el 18 del acta: DOS 18
DISTINTOS que coinciden por casualidad. La CORRECCION 15 registra las tres
cifras sin borrar la vieja, y esta es la que las computa.

QUE COMPUTA, todo desde tallar_estado_de_fase (mismo parser, mismo resolutor,
misma nomina de catalogo; ninguna nomina se teclea aqui):

  - por operacion del catalogo con `aristas_nuevas`: FILAS DE FICHA (los pares
    que el parser saca) y DIRECCIONES DISTINTAS tras resolver por alias (P.1);
  - el TOTAL sobre LAS CINCO REMITIDAS por la tabla de docs/plan/04_ENLACES.md
    (seccion "SEGUNDA MITAD, LAS CINCO REMITIDAS A LAS MESAS DE LA FASE 06"),
    que es el universo que el acta 140 conto;
  - el TOTAL sobre TODAS las del catalogo que tienen direcciones, que es el
    universo que el instrumento de la vuelta 141 conto;
  - y la NOMINA de las que estan en el segundo universo y no en el primero, que
    es exactamente lo que explica la diferencia.

LA MEMBRESIA NO SE TECLEA: "remitida por 04_ENLACES" se decide porque
leer_remisiones() devuelve para ese id una `fuente` que apunta a
docs/plan/04_ENLACES.md, y esa fuente sale del fichero parseado.

USO:
  python scripts/loop/vuelta142_1b_desglose_direcciones.py --fase 06_MESAS
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default="06_MESAS")
    ap.add_argument("--ref", default="WORK")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = T.cargar_ops(a.ref)
    nodos = T.cargar_grafo(a.ref)
    resolver = T.resolver_de(nodos)
    remisiones = T.leer_remisiones(a.fase, a.ref)
    fallos = []
    catalogo, por_id = T.construir_catalogo(a.fase, ops, remisiones, fallos)

    print("=" * 78)
    print("DESGLOSE DE DIRECCIONES | FASE %s | REF: %s" % (a.fase, a.ref))
    print("Unidad adjudicada: LA DIRECCION (acta 140, adjudicacion 3.4).")
    print("Las filas de ficha se publican SIEMPRE nombradas como tales.")
    print("=" * 78)
    print("")
    print("| operacion | remitida por | filas de ficha | direcciones distintas |")
    print("|---|---|---:|---:|")

    filas_cinco, dirs_cinco, nombres_cinco = 0, 0, []
    filas_todas, dirs_todas, nombres_todas = 0, 0, []
    for x in sorted(catalogo):
        op = por_id[x]
        pares = T.pares_de_aristas(op, fallos)
        if not pares:
            continue
        dirs = T.direcciones_de(pares, resolver)
        meta = remisiones.get(x) or {}
        fuente = meta.get("fuente") or ""
        por_enlaces = T.REL_ENLACES in fuente
        etiqueta = fuente if fuente else "no remitida (fase propia)"
        print("| %s | %s | %d | %d |" % (x, etiqueta, len(pares), len(dirs)))
        filas_todas += len(pares)
        dirs_todas += len(dirs)
        nombres_todas.append(x)
        if por_enlaces:
            filas_cinco += len(pares)
            dirs_cinco += len(dirs)
            nombres_cinco.append(x)

    fuera = [x for x in nombres_todas if x not in nombres_cinco]

    print("")
    print("UNIVERSO 1, LAS REMITIDAS POR %s (el que conto el acta 140):" % T.REL_ENLACES)
    print("   operaciones: %d (%s)" % (len(nombres_cinco), ", ".join(nombres_cinco) or "ninguna"))
    print("   FILAS DE FICHA: %d" % filas_cinco)
    print("   DIRECCIONES DISTINTAS: %d" % dirs_cinco)
    print("")
    print("UNIVERSO 2, TODAS LAS DEL CATALOGO CON DIRECCIONES (el que conto la vuelta 141):")
    print("   operaciones: %d (%s)" % (len(nombres_todas), ", ".join(nombres_todas) or "ninguna"))
    print("   FILAS DE FICHA: %d" % filas_todas)
    print("   DIRECCIONES DISTINTAS: %d" % dirs_todas)
    print("")
    print("EN EL UNIVERSO 2 Y NO EN EL 1 (%d): %s" % (len(fuera), ", ".join(fuera) or "ninguna"))
    print("DIFERENCIA DE DIRECCIONES ENTRE LOS DOS UNIVERSOS: %d" % (dirs_todas - dirs_cinco))

    if fallos:
        print("")
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
