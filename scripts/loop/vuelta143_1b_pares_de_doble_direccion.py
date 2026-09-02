# -*- coding: utf-8 -*-
r"""vuelta143_1b_pares_de_doble_direccion.py . LOS PARES DEL PLAN QUE LLEVAN
SUS DOS DIRECCIONES ESCRITAS EN SU PROPIO aristas_nuevas, COMPUTADOS Y NO
TECLEADOS (TAREA 1.b de la vuelta 143, acta de la vuelta 142, adjudicacion 3.4).

POR QUE NACE. docs/plan/00_INDICE.md:478 dice literal: "Los dos enlaces mutuos
del banco 9.22 son las UNICAS aristas del plan que van en las dos direcciones a
proposito." La frase se escribio cuando OP-E-05 era el unico sitio donde las dos
direcciones estaban en la MISMA fila. Hoy hay pares cuyas dos direcciones estan
en DOS FILAS DISTINTAS de la misma ficha, y solo se ven tras resolver por alias
(P.1), que es justamente lo que la frase no mira.

QUE COMPUTA. Recorre TODAS las fichas de docs/plan/OPERACIONES.jsonl (no solo
las de una fase), saca los pares del parser de tallar_estado_de_fase
(pares_de_aristas), los RESUELVE por alias con el mismo resolutor del grafo
(P.1, EJECUTOR.md regla 9) y busca los pares no ordenados {A,B} para los que la
MISMA ficha escribe A -> B y B -> A. De cada uno publica: la operacion, las dos
direcciones resueltas, las filas de ficha de origen con su LD leido de la propia
cadena, y si las dos direcciones vienen de UNA fila o de DOS.

EL LD NO SE TECLEA: sale de la cadena de aristas_nuevas con la expresion
"por LD-<n>", y si una fila no lo trae se publica "sin LD en la cadena", nunca
se inventa.

USO:
  python scripts/loop/vuelta143_1b_pares_de_doble_direccion.py
  python scripts/loop/vuelta143_1b_pares_de_doble_direccion.py --ref 62d4f28e
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

PATRON_LD = re.compile(r"\bLD-(\d+)\b")


def filas_con_ld(op):
    """[(cadena, [(origen, destino), ...], [LD, ...])] por cada cadena de
    aristas_nuevas, con sus pares crudos y los LD que la cadena nombra."""
    salida = []
    for s in (op.get("aristas_nuevas") or []):
        pares = T.PATRON_ARISTA.findall(s)
        lds = ["LD-%s" % m for m in PATRON_LD.findall(s)]
        salida.append((s, pares, lds))
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    lista_ops = T.cargar_ops(a.ref)
    ops = {o["id_op"]: o for o in lista_ops}
    nodos = T.cargar_grafo(a.ref)
    resolver = T.resolver_de(nodos)

    print("=" * 78)
    print("PARES DEL PLAN CON LAS DOS DIRECCIONES EN SU PROPIO aristas_nuevas")
    print("REF: %s | fichas leidas de %s: %d" % (a.ref, T.REL_OPS, len(lista_ops)))
    print("Direcciones RESUELTAS por alias (P.1) antes de emparejar.")
    print("=" * 78)
    print("")

    hallados = []
    fichas_con_aristas = 0
    total_filas = 0
    total_direcciones = 0
    for id_op in sorted(ops):
        op = ops[id_op]
        filas = filas_con_ld(op)
        if not any(p for _, p, _ in filas):
            continue
        fichas_con_aristas += 1
        # direccion resuelta -> lista de (indice de fila, LDs de esa fila)
        procedencia = {}
        for i, (_, pares, lds) in enumerate(filas):
            total_filas += len(pares)
            for o, d in pares:
                clave = (resolver(o), resolver(d))
                procedencia.setdefault(clave, []).append((i, lds))
        total_direcciones += len(procedencia)
        vistos = set()
        for (ro, rd) in procedencia:
            if ro == rd:
                continue
            par = tuple(sorted((ro, rd)))
            if par in vistos:
                continue
            if (rd, ro) in procedencia:
                vistos.add(par)
                hallados.append((id_op, (ro, rd), (rd, ro),
                                 procedencia[(ro, rd)], procedencia[(rd, ro)], filas))

    print("| # | operacion | par (resuelto) | LD de la ida | LD de la vuelta | filas de ficha |")
    print("|---:|---|---|---|---|---|")
    for n, (id_op, ida, vuelta, proc_i, proc_v, filas) in enumerate(hallados, 1):
        ld_i = ", ".join(sorted({x for _, lds in proc_i for x in lds})) or "sin LD en la cadena"
        ld_v = ", ".join(sorted({x for _, lds in proc_v for x in lds})) or "sin LD en la cadena"
        idx_i = sorted({i for i, _ in proc_i})
        idx_v = sorted({i for i, _ in proc_v})
        forma = "UNA fila" if idx_i == idx_v and len(idx_i) == 1 else "DOS filas"
        print("| %d | %s | %s <-> %s | %s | %s | %s (indices %s y %s) |"
              % (n, id_op, ida[0], ida[1], ld_i, ld_v, forma,
                 ",".join(str(x) for x in idx_i), ",".join(str(x) for x in idx_v)))

    print("")
    print("PARES CON LAS DOS DIRECCIONES: %d" % len(hallados))
    print("ARISTAS QUE ESO SUPONE (2 por par): %d" % (2 * len(hallados)))
    print("FICHAS DEL PLAN CON aristas_nuevas NO VACIO: %d de %d" % (fichas_con_aristas, len(ops)))
    print("FILAS DE FICHA TOTALES EN EL PLAN: %d" % total_filas)
    print("DIRECCIONES DISTINTAS TOTALES EN EL PLAN (tras resolver): %d" % total_direcciones)
    print("")
    print("DESGLOSE POR OPERACION:")
    por_op = {}
    for id_op, _, _, _, _, _ in hallados:
        por_op[id_op] = por_op.get(id_op, 0) + 1
    for id_op in sorted(por_op):
        print("   %s: %d par(es)" % (id_op, por_op[id_op]))
    print("")
    print("LAS CADENAS DE ORIGEN, ENTERAS Y SIN RECORTAR:")
    for id_op, ida, vuelta, proc_i, proc_v, filas in hallados:
        idx = sorted({i for i, _ in proc_i} | {i for i, _ in proc_v})
        print("   %s | %s <-> %s" % (id_op, ida[0], ida[1]))
        for i in idx:
            print("      [%d] %s" % (i, filas[i][0]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
