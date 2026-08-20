"""Vuelta 47, TAREA 3.1: EL ORDEN DE LA FASE 03, MEDIDO ANTES DE ADJUDICARLO.

El encargo manda adjudicar por criterio CITABLE del plan, con el precedente de
CONGELADOS LIBERADOS delante, y PARAR si no lo hay. Este instrumento no adjudica:
MIDE las tres cosas que la adjudicacion necesita, para que la decision se tome con
las cifras delante y no con un recuerdo.

  1. LA VARA DE LA FASE 02, APLICADA LITERAL A LA FASE 03: cuantos congelados libera
     cada operacion de la fase 03. Si la respuesta es CERO para todas, se dice.
  2. LA MISMA VARA EN SU FORMA GENERAL (docs/PENDIENTES.md linea 2596: el criterio de
     orden es CUANTOS PARES DESBLOQUEA): cuantas operaciones del plan espera cada
     una, leido del campo depende_de, que es texto sellado del plan.
  3. SI CADA CANDIDATA ESTA DESBLOQUEADA: todas sus dependencias en una fase con
     cierre declarado.

De solo lectura.

Uso: python scripts/loop/vuelta47_orden_fase03.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

FASE = "03_FUSIONES"
MARCA = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)

# Las fases con cierre DECLARADO y su cita, leidas hoy. No se dan por cerradas: se
# nombra donde esta escrito el cierre, para que el lector lo pueda comprobar.
CIERRES = {
    "00_CODIGO": "acta de la vuelta 21, seccion 4 punto 5 (la fase 0 cierra con "
                 "OP-C-05 DIFERIDA Y DECLARADA)",
    "01_FUENTES": "docs/plan/01_FUENTES.md linea 1139 (LA FASE 01 QUEDA CERRADA, "
                  "14 ago 2026, vuelta 31)",
    "02_DESTEJIDOS": "docs/plan/02_DESTEJIDOS.md, EL CIERRE DE LA FASE 02 DECLARADO "
                     "MIDIENDO (19 ago 2026), hoy 9 de 9 con registro",
    "06_MESAS": "docs/plan/00_INDICE.md, EL ORDEN: 06 MESAS ya no espera, las cinco "
                "estan adjudicadas; sus operaciones hijas viven en las fases 3 y 4",
}


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    ops = []
    for l in io.open(OPS, encoding="utf-8"):
        l = l.strip()
        if l:
            ops.append(json.loads(l))
    por_id = {o["id_op"]: o for o in ops}
    dela = [o for o in ops if o["fase"] == FASE]

    sep("0. LAS CANDIDATAS: EL EMPATE DEL CAMPO orden, CONTADO")
    minimo = min(o["orden"] for o in dela)
    empatadas = sorted([o["id_op"] for o in dela if o["orden"] == minimo])
    print("  operaciones de la fase %s : %d" % (FASE, len(dela)))
    print("  orden minimo del campo      : %d" % minimo)
    print("  EMPATADAS EN ESE ORDEN      : %d  %s" % (len(empatadas), empatadas))

    sep("1. LA VARA DE LA FASE 02, APLICADA LITERAL: CONGELADOS QUE LIBERA CADA UNA")
    congelados = []
    for l in io.open(VER, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        v = json.loads(l)
        if MARCA.match((v.get("razon") or "").strip()):
            congelados.append(v)
    print("  congelados abiertos en el archivo entero, contados hoy: %d"
          % len(congelados))
    for v in congelados:
        print("    puesto %s  clase %s  %s contra %s"
              % (v.get("puesto_intra"), v.get("clase"),
                 v.get("nodo_a"), v.get("nodo_b")))
    print()
    print("  quien nombra a esos nodos, buscado en TODAS las operaciones del plan:")
    for v in congelados:
        duenos = []
        for o in ops:
            blob = json.dumps(o, ensure_ascii=False)
            if v.get("nodo_a") in blob and v.get("nodo_b") in blob:
                duenos.append("%s (%s)" % (o["id_op"], o["fase"]))
        print("    puesto %s -> %s" % (v.get("puesto_intra"), duenos or "nadie"))
    print()
    print("  %-20s %s" % ("operacion de la fase 03", "congelados que libera"))
    for oid in empatadas:
        o = por_id[oid]
        blob = json.dumps(o, ensure_ascii=False)
        n = sum(1 for v in congelados
                if v.get("nodo_a") in blob and v.get("nodo_b") in blob)
        print("  %-20s %d" % (oid, n))
    print()
    print("  LECTURA: si las tres dan CERO, la vara de la fase 02 aplicada LITERAL")
    print("  no rompe el empate, y hay que leerla en su forma general.")

    sep("2. LA MISMA VARA EN SU FORMA GENERAL: CUANTO DESBLOQUEA CADA UNA")
    print("  docs/PENDIENTES.md linea 2596, adjudicado el 14 ago 2026: el criterio de")
    print("  orden no es el tamano ni lo averiado, es CUANTOS PARES DESBLOQUEA. Aqui")
    print("  lo desbloqueado se lee del campo depende_de, que es texto sellado del")
    print("  plan y no una lectura mia.")
    print()
    print("  %-20s %-8s %s" % ("operacion", "espera a", "quien la espera a ella"))
    for oid in sorted([o["id_op"] for o in dela],
                      key=lambda i: (-len([x for x in ops if i in x["depende_de"]]),
                                     por_id[i]["orden"], i)):
        esperan = sorted(x["id_op"] for x in ops if oid in x["depende_de"])
        marca = "  <== EMPATADA" if oid in empatadas else ""
        print("  %-20s %-8d %d  %s%s"
              % (oid, len(por_id[oid]["depende_de"]), len(esperan), esperan, marca))

    print()
    print("  SOLO LAS EMPATADAS, que es donde el criterio tiene que decidir:")
    filas = []
    for oid in empatadas:
        esperan = sorted(x["id_op"] for x in ops if oid in x["depende_de"])
        filas.append((len(esperan), oid, esperan))
    for n, oid, esperan in sorted(filas, reverse=True):
        print("    %-20s desbloquea %d  %s" % (oid, n, esperan))

    sep("3. SI CADA EMPATADA ESTA DESBLOQUEADA HOY")
    for oid in empatadas:
        o = por_id[oid]
        print()
        print("  %s  depende de %d operacion(es)" % (oid, len(o["depende_de"])))
        fases = {}
        for d in o["depende_de"]:
            f = por_id[d]["fase"] if d in por_id else "ID QUE NO EXISTE"
            fases.setdefault(f, []).append(d)
        listo = True
        for f in sorted(fases):
            cita = CIERRES.get(f)
            if cita is None:
                listo = False
            print("    %-16s %-2d  %s"
                  % (f, len(fases[f]), cita or "SIN CIERRE DECLARADO QUE CITAR"))
        print("    DESBLOQUEADA: %s" % ("SI" if listo else "NO"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
