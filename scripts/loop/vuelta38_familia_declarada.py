# -*- coding: utf-8 -*-
"""vuelta38_familia_declarada.py - EL CHOQUE ENTRE LA REGLA FAMILIA DECLARADA Y LAS TRES LECTURAS.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo, ni en un nodo, ni en el plan.

POR QUE EXISTE. La REGLA FAMILIA DECLARADA (docs/INTRA_DOMINIO_INFORME.md, linea
26, generalizada el 11 ago 2026 a TODO racimo declarado) dice que un par cuyos DOS
nodos pertenecen a un racimo ya declarado NO PELEA LA CLASE, y da el motivo: la
decision ya esta tomada EN OTRO SITIO. Las tres lecturas que el encargo del 19 ago
2026 manda hacer (LD-96 a LD-98) son, las tres, pares de DOS miembros de la misma
nomina censada. O sea que la regla las alcanza.

Este instrumento no resuelve el choque: lo MIDE, que es lo que el ejecutor puede
hacer con el (EJECUTOR.md, regla 5: si contradice una regla vigente, se escribe
como PARADA y no se arregla).

QUE MIDE, todo hoy:
  1. LA NOMINA del racimo, leida de docs/RACIMOS_MIEMBROS.jsonl.
  2. SI LOS TRES PARES SON INTRA NOMINA, uno por uno.
  3. SI EXISTE EL OTRO SITIO donde la decision estaria tomada: se barren las 71
     operaciones de docs/plan/OPERACIONES.jsonl buscando cual nombra a alguno de
     los cuatro, y en que fase.
  4. LAS CLASES YA ESCRITAS entre miembros de la nomina, para ver que hizo el
     archivo cuando la regla si tenia donde apoyarse.

Uso: python scripts/loop/vuelta38_familia_declarada.py
"""
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RACIMOS = os.path.join(RAIZ, "docs", "RACIMOS_MIEMBROS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

RACIMO = "Las reglas del brainstorming"
CUARTO = "brainstorming"
TALLER = ["brainstorming_divergente", "brainstorming_efectivo", "reglas_brainstorming"]


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    bloque("1. LA NOMINA DEL RACIMO, leida hoy de docs/RACIMOS_MIEMBROS.jsonl")
    R = [json.loads(l) for l in io.open(RACIMOS, encoding="utf-8") if l.strip()]
    print("  racimos censados en el fichero: %d" % len(R))
    fila = next((r for r in R if r.get("racimo") == RACIMO), None)
    if fila is None:
        print("  ABORTA: no existe el racimo %r en el censo" % RACIMO)
        return 1
    print("  racimo            : %s" % fila["racimo"])
    print("  dominio_censado   : %s" % fila["dominio_censado"])
    print("  tamano_censado    : %s" % fila["tamano_censado"])
    print("  origen            : %s" % fila["origen"])
    nomina = [m["node_id"] for m in fila["miembros"]]
    for m in fila["miembros"]:
        print("     %-38s %-10s %s" % (m["node_id"], m["dominio"], m["fuente"]))

    bloque("2. LOS TRES PARES DE LD-96 A LD-98, son intra nomina?")
    for b in TALLER:
        dentro = CUARTO in nomina and b in nomina
        print("  %-14s contra %-38s los dos en la nomina: %s"
              % (CUARTO, b, "SI" if dentro else "no"))
    print("")
    print("  LA REGLA FAMILIA DECLARADA ALCANZA A LOS TRES: %s"
          % ("SI" if all(CUARTO in nomina and b in nomina for b in TALLER) else "no"))

    bloque("3. EXISTE EL OTRO SITIO? las 71 operaciones barridas por los cuatro nombres")
    O = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    print("  operaciones en docs/plan/OPERACIONES.jsonl: %d" % len(O))
    print("")
    hallazgos = 0
    for o in O:
        toca = [n for n in (o.get("nodos") or []) if n in nomina]
        if toca:
            hallazgos += 1
            print("  %-14s fase %-18s nodos de la nomina que nombra: %s"
                  % (o["id_op"], o["fase"], ", ".join(toca)))
    print("")
    print("  operaciones que nombran a algun miembro: %d" % hallazgos)
    fases = sorted(set(o["fase"] for o in O
                       if any(n in nomina for n in (o.get("nodos") or []))))
    print("  fases en que aparecen: %s" % (", ".join(fases) if fases else "ninguna"))
    print("  operaciones de fase 06_MESAS que nombran a algun miembro: %d"
          % sum(1 for o in O if o["fase"].startswith("06")
                and any(n in nomina for n in (o.get("nodos") or []))))
    print("")
    print("  LECTURA: la regla se apoya en que LA DECISION YA ESTA TOMADA EN OTRO SITIO.")
    print("  Si ninguna operacion de mesa nombra a estos nodos, ese otro sitio no existe")
    print("  todavia, y es exactamente el hueco que la autorizacion del fundador llena.")

    bloque("4. LAS CLASES YA ESCRITAS ENTRE MIEMBROS DE LA NOMINA")
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v
    print("  los 6 pares posibles de una nomina de 4:")
    for a, b in itertools.combinations(nomina, 2):
        v = por_par.get((a, b))
        if v is None:
            print("     %-38s %-38s SIN VEREDICTO" % (a, b))
        else:
            cita = "familia declarada" in (v.get("razon") or "").lower() \
                or "FAMILIA DECLARADA" in (v.get("razon") or "")
            print("     %-38s %-38s %s  puesto %-5s cita la regla: %s"
                  % (a, b, v["clase"], v["puesto_intra"], "SI" if cita else "no"))

    bloque("VEREDICTO DE LA MEDICION")
    print("la nomina tiene %d miembros; los tres pares de la tanda son intra nomina;" % len(nomina))
    print("el barrido de las 71 operaciones esta impreso arriba. EL CHOQUE NO SE RESUELVE")
    print("AQUI: se mide y se lleva al reporte como PARADA DE DOCTRINA.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
