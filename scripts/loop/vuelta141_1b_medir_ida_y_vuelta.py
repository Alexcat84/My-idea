# -*- coding: utf-8 -*-
r"""vuelta141_1b_medir_ida_y_vuelta.py . LA CUENTA DE FILAS DE OP-E-04 EN
VIOLACION DE SU PROPIA VERIFICACION 0, MEDIDA CON IDA Y VUELTA A LA VEZ
(TAREA 1.b de la vuelta 141, acta de la vuelta 140, caida 4.1).

POR QUE NACE. El reporte de la vuelta 140 publico TRES filas de OP-E-04 en
violacion de su verificacion 0 ("LA VUELTA NO DEBE EXISTIR NI LITERAL NI
RESUELTA"): LD-42, LD-48 y LD-53. El acta 140, caida 4.1, midio CINCO:
LD-35, LD-42, LD-48, LD-49 y LD-51. La discrepancia tiene causa nombrada:
la vara del ejecutor solo miro las filas que aun NO estaban presentes, y a
las tres que ya lo estaban las dio por "YA PRESENTE" sin medir su vuelta.

QUE MIDE, Y NO DECIDE NADA. Para cada fila de `aristas_nuevas` de una
operacion, imprime: la lectura dirigida que la cita, los dos extremos
RESUELTOS por el resolutor de la casa (P.1), si la IDA esta presente y si la
VUELTA esta presente, las dos medidas en LAS DOS VISTAS (nodos_siguientes
del origen y nodos_previos del destino). No escribe nada en disco.

EJECUTOR.md regla 2: la cifra que la CORRECCION 13 publica como "de hoy" sale
de esta corrida y no de la prosa del acta.

USO:
  python scripts/loop/vuelta141_1b_medir_ida_y_vuelta.py --op OP-E-04
  python scripts/loop/vuelta141_1b_medir_ida_y_vuelta.py --op OP-E-04 --ref <commit>
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

PATRON_LD = re.compile(r"\bLD-\d+\b")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", required=True)
    ap.add_argument("--ref", default="WORK")
    a = ap.parse_args()

    ops = T.cargar_ops(a.ref)
    por_id = {o.get("id_op"): o for o in ops}
    if a.op not in por_id:
        print("ROJO: %s no existe en %s (%s)" % (a.op, T.REL_OPS, a.ref))
        return 1
    op = por_id[a.op]
    nodos = T.cargar_grafo(a.ref)
    resolver = T.resolver_de(nodos)

    print("IDA Y VUELTA DE %s | REF: %s" % (a.op, a.ref))
    print("Verificacion 0 de la ficha, literal: %s" % (op.get("verificacion") or ["(sin verificacion)"])[0])
    print("")
    print("| lectura | fila cruda (origen -> destino) | origen resuelto | destino resuelto | IDA presente | VUELTA presente |")
    print("|---|---|---|---|---|---|")

    filas = []
    for s in (op.get("aristas_nuevas") or []):
        for o, d in T.PATRON_ARISTA.findall(s):
            ld = PATRON_LD.search(s)
            ida, ro, rd = T.arista_presente(nodos, resolver, o, d)
            vuelta, _, _ = T.arista_presente(nodos, resolver, d, o)
            filas.append(dict(ld=ld.group(0) if ld else "(sin LD)", o=o, d=d,
                              ro=ro, rd=rd, ida=ida, vuelta=vuelta))
            print("| %s | %s -> %s | %s | %s | %s | %s |" % (
                filas[-1]["ld"], o, d, ro, rd,
                "SI" if ida else "no", "SI" if vuelta else "no"))

    direcciones = sorted({(f["ro"], f["rd"]) for f in filas})
    con_vuelta = sorted({f["ld"] for f in filas if f["vuelta"]})
    sin_ida = sorted({f["ld"] for f in filas if not f["ida"]})
    print("")
    print("FILAS DE FICHA: %d | DIRECCIONES DISTINTAS TRAS RESOLVER: %d"
          % (len(filas), len(direcciones)))
    print("FILAS CON LA IDA PRESENTE: %d | FILAS CON LA VUELTA PRESENTE: %d"
          % (sum(1 for f in filas if f["ida"]), sum(1 for f in filas if f["vuelta"])))
    print("EN VIOLACION DE LA VERIFICACION 0 (la vuelta existe hoy), %d fila(s): %s"
          % (len(con_vuelta), ", ".join(con_vuelta) or "ninguna"))
    print("FILAS SIN LA IDA PUESTA, %d: %s" % (len(sin_ida), ", ".join(sin_ida) or "ninguna"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
