# -*- coding: utf-8 -*-
r"""vuelta143_1c_tres_unidades.py . LAS TRES UNIDADES QUE CONVIVEN, MEDIDAS Y
NO TECLEADAS (TAREA 1.c de la vuelta 143, acta de la vuelta 142, seccion 2).

POR QUE NACE. El auditor de la vuelta 142 releyo a ciegas el desglose de la
fase 06 con instrumento propio y coincidio en DIRECCIONES (17 sobre las cinco
remitidas, 18 sobre las seis) pero NO en "filas": conto 16 donde el ejecutor
conto 18. La causa no era un error de nadie: contaban UNIDADES DISTINTAS. El
auditor contaba ENTRADAS DEL ARRAY `aristas_nuevas`; el ejecutor y
tallar_estado_de_fase.py cuentan FILAS DE FICHA, que es la direccion escrita
ANTES de resolver, y una sola entrada del array puede escribir dos.

LAS TRES UNIDADES, nombradas de una vez para que no vuelvan a mezclarse:
  ENTRADA  = un elemento del array JSON `aristas_nuevas` de la ficha.
  FILA     = un par "A -> B" tal como esta ESCRITO, antes de resolver alias.
             Es lo que `pares_de_aristas()` devuelve y lo que
             tallar_estado_de_fase.py llama fila y publica desde la vuelta 141.
  DIRECCION= el par (A, B) DESPUES de resolver por alias (P.1). Es la unidad
             adjudicada por el acta 140.

QUE COMPUTA. Las tres cifras por operacion y los tres totales, sobre los DOS
universos que las actas han usado: LAS CINCO REMITIDAS por
docs/plan/04_ENLACES.md (membresia leida del fichero, nunca tecleada, igual que
en vuelta142_1b_desglose_direcciones.py) y LAS SEIS del catalogo de la fase con
direcciones, que anade OP-M-05-APERTURA.

USO:
  python scripts/loop/vuelta143_1c_tres_unidades.py --fase 06_MESAS
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
    print("LAS TRES UNIDADES | FASE %s | REF: %s" % (a.fase, a.ref))
    print("ENTRADA = elemento del array JSON aristas_nuevas")
    print("FILA    = 'A -> B' escrito, ANTES de resolver (lo que el tallador llama fila)")
    print("DIRECCION = (A, B) DESPUES de resolver por alias (P.1), unidad del acta 140")
    print("=" * 78)
    print("")
    print("| operacion | remitida por | entradas | filas | direcciones |")
    print("|---|---|---:|---:|---:|")

    tot5 = [0, 0, 0]
    tot6 = [0, 0, 0]
    n5, n6 = [], []
    for x in sorted(catalogo):
        op = por_id[x]
        entradas = len(op.get("aristas_nuevas") or [])
        pares = T.pares_de_aristas(op, fallos)
        if not pares:
            continue
        dirs = T.direcciones_de(pares, resolver)
        meta = remisiones.get(x) or {}
        fuente = meta.get("fuente") or ""
        etiqueta = fuente if fuente else "no remitida (fase propia)"
        print("| %s | %s | %d | %d | %d |" % (x, etiqueta, entradas, len(pares), len(dirs)))
        tot6[0] += entradas; tot6[1] += len(pares); tot6[2] += len(dirs)
        n6.append(x)
        if T.REL_ENLACES in fuente:
            tot5[0] += entradas; tot5[1] += len(pares); tot5[2] += len(dirs)
            n5.append(x)

    print("")
    # LINEAS `CIFRA <etiqueta>: <n> <unidad>` para que verificar_cifras_del_reporte.py
    # pueda COTEJAR estas cifras contra este fichero. `fila` y `direccion` no
    # tienen convencion mecanica de conteo: solo cotejan contra una linea CIFRA.
    print("CIFRA filas sobre las cinco remitidas: %d filas" % tot5[1])
    print("CIFRA direcciones sobre las cinco remitidas: %d direcciones" % tot5[2])
    print("CIFRA filas sobre las seis del catalogo: %d filas" % tot6[1])
    print("CIFRA direcciones sobre las seis del catalogo: %d direcciones" % tot6[2])
    print("")
    print("UNIVERSO 1, LAS REMITIDAS POR %s: %d operaciones (%s)"
          % (T.REL_ENLACES, len(n5), ", ".join(n5)))
    print("   ENTRADAS %d | FILAS %d | DIRECCIONES %d" % tuple(tot5))
    print("")
    print("UNIVERSO 2, TODAS LAS DEL CATALOGO CON DIRECCIONES: %d operaciones (%s)"
          % (len(n6), ", ".join(n6)))
    print("   ENTRADAS %d | FILAS %d | DIRECCIONES %d" % tuple(tot6))
    print("")
    fuera = [x for x in n6 if x not in n5]
    print("EN EL UNIVERSO 2 Y NO EN EL 1: %s" % (", ".join(fuera) or "ninguna"))
    print("")
    print("LOS DOS EJEMPLARES DEL SALTO, cada uno con sus tres cifras:")
    for x in ("OP-E-05", "OP-M-05-APERTURA"):
        if x not in por_id:
            print("   %s: NO esta en el catalogo de la fase %s" % (x, a.fase))
            continue
        op = por_id[x]
        entradas = len(op.get("aristas_nuevas") or [])
        pares = T.pares_de_aristas(op, fallos)
        dirs = T.direcciones_de(pares, resolver)
        print("   %s: %d entrada(s), %d fila(s), %d direccion(es)"
              % (x, entradas, len(pares), len(dirs)))
        for i, s in enumerate(op.get("aristas_nuevas") or []):
            print("      entrada [%d]: %s" % (i, s))
        for o, d in pares:
            print("      fila escrita: %s -> %s   (resuelve a %s -> %s)"
                  % (o, d, resolver(o), resolver(d)))
        for ro, rd in dirs:
            print("      direccion resuelta: %s -> %s" % (ro, rd))

    if fallos:
        print("")
        print("FALLOS DEL PARSER (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
    return 0


if __name__ == "__main__":
    sys.exit(main())
