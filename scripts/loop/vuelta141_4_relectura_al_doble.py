# -*- coding: utf-8 -*-
r"""vuelta141_4_relectura_al_doble.py . LA RELECTURA AL DOBLE DEL TRAMO
(TAREA 4 de la vuelta 141).

EL TRAMO QUE SE RELEE, y va nombrado en el encargo: "TODA ARISTA ESCRITA O
DECLARADA CUMPLIDA SIN HABER MEDIDO SU VUELTA". El credito de la tanda esta
roto por vigesimoprimera vuelta porque el hallazgo del auditor (acta 140, 4.1)
salio FUERA de los discutibles marcados: la vara de enlace media si la arista
estaba y nunca miraba si la vuelta estaba.

"YA PRESENTE" NO ES UN VEREDICTO: ES MEDIA MEDICION.

QUE HACE. Recorre TODAS las operaciones del catalogo de una fase que tienen
`aristas_nuevas`, y para CADA DIRECCION suya (resuelta por alias, P.1, y medida
en LAS DOS VISTAS) publica: si la IDA esta presente, si la VUELTA esta presente,
y el REGIMEN DE VUELTA que la ficha declara. No se salta ninguna direccion por
estar ya puesta: esa es justamente la que la caida 4.1 dejo sin mirar.

Cierra con la CIFRA del tramo: cuantas direcciones se relen, cuantas tienen la
vuelta presente, y cuantas de esas viven en una ficha que la PROHIBE.

USO:
  python scripts/loop/vuelta141_4_relectura_al_doble.py --fase 06_MESAS
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
    print("RELECTURA AL DOBLE DEL TRAMO | FASE %s | REF: %s" % (a.fase, a.ref))
    print("El tramo: toda arista escrita o declarada cumplida SIN haber medido su vuelta.")
    print("Ninguna direccion se salta por estar YA PRESENTE: esa es la que la caida 4.1")
    print("del acta 140 dejo sin mirar.")
    print("=" * 78)
    print("")
    print("| operacion | regimen de vuelta (de la ficha) | direccion resuelta | lectura | IDA | VUELTA |")
    print("|---|---|---|---|---|---|")

    total_dir = 0
    con_vuelta = []
    con_vuelta_prohibida = []
    for x in catalogo:
        op = por_id[x]
        pares = T.pares_de_aristas(op, fallos)
        if not pares:
            continue
        regimen, cita = T.regimen_de_vuelta(op, fallos)
        # La lectura dirigida de cada fila, para poder nombrarla en la tabla.
        ld_por_par = {}
        for s in (op.get("aristas_nuevas") or []):
            m = PATRON_LD.search(s)
            for o, d in T.PATRON_ARISTA.findall(s):
                ld_por_par.setdefault((resolver(o), resolver(d)), []).append(
                    m.group(0) if m else "(sin LD)")
        for ro, rd in T.direcciones_de(pares, resolver):
            total_dir += 1
            ida, _, _ = T.arista_presente(nodos, resolver, ro, rd)
            vuelta, _, _ = T.arista_presente(nodos, resolver, rd, ro)
            lds = ", ".join(sorted(set(ld_por_par.get((ro, rd)) or ["(sin LD)"])))
            print("| %s | %s | %s -> %s | %s | %s | %s |"
                  % (x, regimen, ro, rd, lds,
                     "SI" if ida else "no", "SI" if vuelta else "no"))
            if vuelta:
                con_vuelta.append((x, "%s -> %s" % (rd, ro), lds))
                if regimen == "PROHIBE":
                    con_vuelta_prohibida.append((x, "%s -> %s" % (rd, ro), lds))

    print("")
    print("CIFRA DEL TRAMO RELEIDO AL DOBLE:")
    print("   direcciones releidas con IDA Y VUELTA a la vez: %d" % total_dir)
    print("   direcciones con LA VUELTA PRESENTE: %d" % len(con_vuelta))
    for x, d, lds in con_vuelta:
        print("      %s | %s | por %s" % (x, d, lds))
    print("   de esas, en una ficha que PROHIBE la vuelta: %d" % len(con_vuelta_prohibida))
    for x, d, lds in con_vuelta_prohibida:
        print("      %s | %s | por %s" % (x, d, lds))
    if fallos:
        print("")
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
