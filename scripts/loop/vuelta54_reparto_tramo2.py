# -*- coding: utf-8 -*-
"""vuelta54_reparto_tramo2.py . EL REPARTO PIEZA A PIEZA DE UN LOTE DEL TRAMO 2,
CON EL TEXTO VERBATIM DE LAS DOS PARTES Y EL SOLAPE MEDIDO AL LADO.

DE SOLO LECTURA. Imprime; no toca nada.

POR QUE EXISTE: el contrato de scripts/loop/vuelta48_fundir_tramo.py pide que
el plan marque CADA paso y CADA condicion del absorbido como APPEND, CUBIERTO:n
o INCISO. Esa marca se decide LEYENDO, y para leer hace falta tener las dos
listas delante y verbatim. Este instrumento las pone una al lado de la otra y
anade, por cada pieza del absorbido, EL PASO DEL SUPERVIVIENTE QUE MAS SE LE
PARECE con su solape medido.

EL SOLAPE ES UN CONTRASTE DE MAQUINA Y NO ES LA MARCA. Un solape alto no
prueba que la pieza este cubierta y uno bajo no prueba que no lo este: la marca
la pone la lectura. La cifra esta para que la lectura no se apoye en el
recuerdo.

Uso:
  python scripts/loop/vuelta54_reparto_tramo2.py --tramo docs/loop/TRAMO2_V54.jsonl
        --actos 2,3,5 --superviviente-de docs/loop/ELECCIONES_V54.json
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PALABRA = re.compile(r"[a-záéíóúñü0-9]+", re.IGNORECASE)
VACIAS = set("""el la los las un una unos unas de del al a en y o con por para que se su sus lo
como mas mai si no es son ser esta este esa ese estos esos cada cuando donde desde sobre entre
sin hasta tu tus te le les nos ya muy todo toda todos todas otro otra""".split())


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def bolsa(t):
    return {w.lower() for w in PALABRA.findall(t or "")} - VACIAS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    ap.add_argument("--actos", required=True, help="ordinales del tramo 2, separados por coma")
    ap.add_argument("--elecciones", required=True,
                    help="json {ordinal: superviviente} con la eleccion ya tomada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    tramo = {r["orden_tramo2"]: r for r in cargar(a.tramo)}
    elec = json.load(io.open(a.elecciones, encoding="utf-8"))
    quiere = [int(x) for x in a.actos.split(",") if x.strip()]

    for n in quiere:
        act = tramo[n]
        mi = sorted(act["miembros"])
        sup = elec[str(n)]
        if sup not in mi:
            raise SystemExit("ROJO: el superviviente %s no es miembro del acto %d" % (sup, n))
        ab = [x for x in mi if x != sup][0]
        os_ = json.load(io.open(os.path.join(NODOS, sup + ".json"), encoding="utf-8"))
        oa = json.load(io.open(os.path.join(NODOS, ab + ".json"), encoding="utf-8"))

        print("#" * 100)
        print("# ACTO %d del tramo 2" % n)
        print("# SOBREVIVE : %s" % sup)
        print("# ABSORBIDO : %s" % ab)
        print("#" * 100)
        print()
        print("--- LOS PASOS DEL SUPERVIVIENTE (%d), verbatim ---" % len(os_.get("pasos_accionables") or []))
        for i, p in enumerate(os_.get("pasos_accionables") or [], 1):
            print("  S%d. %s" % (i, p))
        print()
        print("--- LAS CONDICIONES DEL SUPERVIVIENTE (%d), verbatim ---"
              % len(os_.get("condiciones_activacion") or []))
        for i, c in enumerate(os_.get("condiciones_activacion") or [], 1):
            print("  SC%d. %s" % (i, c))
        print()
        print("--- LOS PASOS DEL ABSORBIDO (%d), con el mas parecido del superviviente ---"
              % len(oa.get("pasos_accionables") or []))
        for i, p in enumerate(oa.get("pasos_accionables") or [], 1):
            bp = bolsa(p)
            mejor, cuanto = 0, 0.0
            for j, q in enumerate(os_.get("pasos_accionables") or [], 1):
                bq = bolsa(q)
                if not bp:
                    continue
                v = len(bp & bq) / float(len(bp))
                if v > cuanto:
                    mejor, cuanto = j, v
            print("  A%d. %s" % (i, p))
            print("      mas parecido: S%s con solape %.0f%%" % (mejor or "-", cuanto * 100))
        print()
        print("--- LAS CONDICIONES DEL ABSORBIDO (%d), con la mas parecida ---"
              % len(oa.get("condiciones_activacion") or []))
        for i, c in enumerate(oa.get("condiciones_activacion") or [], 1):
            bc = bolsa(c)
            mejor, cuanto = 0, 0.0
            for j, q in enumerate(os_.get("condiciones_activacion") or [], 1):
                bq = bolsa(q)
                if not bc:
                    continue
                v = len(bc & bq) / float(len(bc))
                if v > cuanto:
                    mejor, cuanto = j, v
            print("  AC%d. %s" % (i, c))
            print("       mas parecida: SC%s con solape %.0f%%" % (mejor or "-", cuanto * 100))
        print()

    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
