# -*- coding: utf-8 -*-
"""vuelta49_guarda_defectos.py . LA GUARDA DE DUPLICADAS TRAS RESOLVER Y
AUTO-ARISTAS, SACADA DEL INSTRUMENTO DE FUNDIR PARA PODER CORRERLA SOLA.

DE DONDE SALE, literal: es la funcion censo_defectos de
scripts/loop/vuelta48_fundir_tramo.py, con la MISMA vara y por el mismo motivo,
puesta en un fichero propio porque el encargo de la vuelta 49 (TAREA 1.1) pide
re-correr la guarda sobre el resultado de una operacion que NO es una fusion y
que por tanto no pasa por aquel instrumento.

LA VARA, y va escrita porque ya se corrigio una vez (vuelta 48, correccion 3 del
reporte): SOLO CUENTAN LAS NUEVAS. El catalogo arrastra un pasivo historico de
duplicadas que OP-S-12 tiene encargado; una guarda que suma el pasivo ajeno al
propio se cae siempre y deja de ser guarda. Por eso este instrumento no publica
un semaforo sobre el total: publica un SNAPSHOT, y el semaforo sale de comparar
dos snapshots con --contra.

P.1 DEL BANCO DEL PLAN: todo conteo que toque ids pasa por el resolutor antes de
contar. La cadena de alias se camina con proteccion de ciclo, igual que alli.

ESTRICTAMENTE DE SOLO LECTURA sobre dataset/. Solo escribe el fichero de
snapshot que se le pida por --snapshot.

Uso:
  python scripts/loop/vuelta49_guarda_defectos.py --snapshot docs/loop/X.json
  python scripts/loop/vuelta49_guarda_defectos.py --snapshot docs/loop/Y.json --contra docs/loop/X.json
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--contra")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        todos[d["node_id"]] = d

    alias = {}
    for nid, d in todos.items():
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for x in (d.get("ids_alias") or []):
            alias[x] = nid

    def r(x):
        v = set()
        while x in alias and x not in v:
            v.add(x)
            x = alias[x]
        return x

    dups, autos = set(), set()
    vivos = 0
    for nid, d in todos.items():
        if d.get("deprecado") or d.get("deprecated"):
            continue
        vivos += 1
        for campo in CAMPOS:
            lista = d.get(campo) or []
            if nid in lista:
                autos.add((nid, campo))
            vistos = set()
            for x in lista:
                y = r(x)
                if y == nid:
                    continue
                if y in vistos:
                    dups.add((nid, campo, y))
                vistos.add(y)

    print("=" * 78)
    print("GUARDA DE DEFECTOS, medida HOY sobre el catalogo entero")
    print("=" * 78)
    print("  ficheros                       : %d" % len(todos))
    print("  vivos revisados                : %d" % vivos)
    print("  cadenas de alias vivas         : %d" % len(alias))
    print("  DUPLICADAS TRAS RESOLVER       : %d" % len(dups))
    print("  AUTO-ARISTAS                   : %d" % len(autos))

    snap = {"duplicadas": sorted("|".join(x) for x in dups),
            "auto_aristas": sorted("|".join(x) for x in autos),
            "ficheros": len(todos), "vivos": vivos}
    io.open(a.snapshot, "w", encoding="utf-8", newline="\n").write(
        json.dumps(snap, ensure_ascii=False, indent=1) + "\n")
    print("  snapshot escrito               : %s" % a.snapshot)

    if not a.contra:
        print()
        print("SIN --contra: esto es una MEDICION, no un semaforo. La guarda es la")
        print("comparacion de dos snapshots, y sin base no hay guarda que dar por verde.")
        return 0

    base = json.load(io.open(a.contra, encoding="utf-8"))
    nd = sorted(set(snap["duplicadas"]) - set(base["duplicadas"]))
    na = sorted(set(snap["auto_aristas"]) - set(base["auto_aristas"]))
    idas_d = len(set(base["duplicadas"]) - set(snap["duplicadas"]))
    idas_a = len(set(base["auto_aristas"]) - set(snap["auto_aristas"]))
    print()
    print("=" * 78)
    print("CONTRA LA BASE %s" % a.contra)
    print("=" * 78)
    print("  duplicadas   base %d  ->  hoy %d   (nuevas %d, retiradas %d)"
          % (len(base["duplicadas"]), len(snap["duplicadas"]), len(nd), idas_d))
    print("  auto-aristas base %d  ->  hoy %d   (nuevas %d, retiradas %d)"
          % (len(base["auto_aristas"]), len(snap["auto_aristas"]), len(na), idas_a))
    for x in nd:
        print("     [ROJO] DUPLICADA NUEVA: %s" % x)
    for x in na:
        print("     [ROJO] AUTO-ARISTA NUEVA: %s" % x)
    print()
    print("guarda A, cero AUTO-ARISTAS nuevas             : %s (%d)"
          % ("OK" if not na else "ROJO", len(na)))
    print("guarda B, cero DUPLICADAS nuevas tras resolver : %s (%d)"
          % ("OK" if not nd else "ROJO", len(nd)))
    return 1 if (nd or na) else 0


if __name__ == "__main__":
    sys.exit(main())
