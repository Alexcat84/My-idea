# -*- coding: utf-8 -*-
"""Vuelta 48: CUANTAS PUERTAS HAY DENTRO DEL LOTE DE `OP-U-01`.

ESTRICTAMENTE DE SOLO LECTURA.

POR QUE EXISTE, y no es una idea: la primera corrida --ejecutar del tramo 1 de
esta vuelta depreco
investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor y GATE 0 SALIO
EN ROJO por DOS chequeos a la vez, porque ese nodo es SEMILLA DE ENTRADA del
mundo compras y ademas DESTINO DE UN PUENTE APROBADO. El dataset se restauro
con git checkout y el acto salio del lote.

La pregunta que eso deja no es del acto 36: es de la operacion entera. Un nodo
PROTEGIDO (semilla de entrada o extremo de puente aprobado) es una PUERTA por
la que se entra a un mundo. Si muere, la puerta no abre. Este instrumento
cuenta cuantos actos del lote tienen una puerta dentro, y separa los dos casos,
que son muy distintos:

  a) UN SOLO miembro protegido: el acto SE SALVA si la lectura elige a ese nodo
     como superviviente. La regla de la pagina (sobrevive por CONTENIDO) puede
     apuntar al otro, y entonces hay choque y se declara.
  b) TODOS los miembros protegidos: NO HAY FUSION POSIBLE sin cerrar una
     puerta, porque alguien tiene que morir. Ese acto no se funde con las
     reglas escritas.

Las fuentes son las MISMAS que lee scripts/run_phase1.py en su Gate 0.

Uso: python scripts/loop/vuelta48_puertas_en_el_lote.py --nomina docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    n_core = len(sem)
    packs = os.path.join(RAIZ, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    pue = {}
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    pue.setdefault(x[extremo], set()).add(d)
    prot = sem | set(pue)

    print("=" * 78)
    print("LAS PUERTAS DENTRO DEL LOTE DE OP-U-01")
    print("=" * 78)
    print("  semillas de entrada core                     : %d" % n_core)
    print("  semillas de entrada con las de los mundos    : %d" % len(sem))
    print("  nodos que son extremo de puente aprobado     : %d" % len(pue))
    print("  UNION, el universo PROTEGIDO                 : %d" % len(prot))

    R = [json.loads(l) for l in io.open(a.nomina, encoding="utf-8") if l.strip()]
    C = [r for r in R if r["estado"] == "CERRADO"]
    salvables, imposibles = [], []
    for i, r in enumerate(C, 1):
        p = [x for x in r["miembros"] if x in prot]
        if not p:
            continue
        (imposibles if len(p) == len(r["miembros"]) else salvables).append((i, r, p))

    print()
    print("SOBRE LOS %d ACTOS CERRADOS:" % len(C))
    print("  actos con al menos una puerta dentro: %d" % (len(salvables) + len(imposibles)))
    print("    SALVABLES (una sola puerta; el acto se funde SI la puerta sobrevive): %d"
          % len(salvables))
    print("    IMPOSIBLES (todos sus miembros son puerta; alguien tendria que morir): %d"
          % len(imposibles))
    print()
    print("  LOS IMPOSIBLES, uno por uno:")
    for i, r, p in imposibles:
        print("    acto %3d tam %d | %s" % (i, r["tamano"], ", ".join(r["miembros"])))
    print()
    print("  LOS SALVABLES, uno por uno (puerta que TIENE que sobrevivir):")
    for i, r, p in salvables:
        print("    acto %3d tam %d | puerta: %s" % (i, r["tamano"], ", ".join(p)))
        print("               resto: %s" % ", ".join(x for x in r["miembros"] if x not in p))
    print()
    print("LO QUE ESTO DEJA ESCRITO PARA LOS TRAMOS QUE VIENEN: la eleccion de")
    print("superviviente de esos %d actos NO es libre. La regla de la pagina dice"
          % (len(salvables) + len(imposibles)))
    print("que sobrevive por CONTENIDO; si el contenido apunta al que NO es puerta,")
    print("hay choque entre la vara de la fase y el Gate 0, y eso no lo resuelve")
    print("ninguna regla escrita hoy. Va como pregunta al auditor, no como decision.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
