# -*- coding: utf-8 -*-
"""vuelta52_marcador_por_git.py . EL MARCADOR DE UN ESTADO PASADO DEL ARBOL,
LEIDO DEL PROPIO GIT Y NO DE UN ACTA.

POR QUE EXISTE, y lo manda el encargo de la vuelta 52 (TAREA 1.4.b) con estas
palabras: "ANTES de fechar, verifica por git la cifra de su corrida: checkout
del cierre de la vuelta 19 y de la 20, recomputa el marcador de cada estado, y
compara con la PRIMERA cifra de cada cadena". Una tabla que dice "medido hoy" y
publica una cifra que nadie ha vuelto a mirar no se puede fechar sin saber si
esa cifra fue cierta ALGUNA VEZ: si no calza ni con su propia corrida, no es un
rotulo envejecido, es una cifra que nacio mal, y las dos especies se tratan
distinto (acta de la vuelta 50, pregunta 5).

NO HACE CHECKOUT y por eso no puede ensuciar el arbol: lee el fichero de
veredictos del objeto de git con `git show <commit>:<ruta>` y cuenta. La
aritmetica es la MISMA que la de scripts/recomputar_marcador.py: se filtra por
`puesto_intra <= corte` y se cuenta el campo `clase`.

DE SOLO LECTURA sobre el arbol de trabajo. No escribe ningun fichero: imprime.

Uso:
  python scripts/loop/vuelta52_marcador_por_git.py 7b21a8d0 1bfab1c4 --corte 3388
"""
import argparse
import collections
import json
import subprocess
import sys

RUTA = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"


def marcador(commit, corte):
    crudo = subprocess.run(
        ["git", "show", "%s:%s" % (commit, RUTA)],
        capture_output=True, check=True,
    ).stdout.decode("utf-8")
    filas = [json.loads(l) for l in crudo.splitlines() if l.strip()]
    filas = [p for p in filas if p["puesto_intra"] <= corte]
    cnt = collections.Counter(p["clase"] for p in filas)
    return len(filas), cnt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("commits", nargs="+")
    ap.add_argument("--corte", type=int, default=3388)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("EL MARCADOR DE CADA ESTADO, LEIDO DE GIT (corte %d)" % a.corte)
    print("fichero: %s" % RUTA)
    print("=" * 78)
    print()
    print("%-12s %-46s %6s %6s %5s %5s %6s" % ("commit", "asunto", "n", "A", "B", "C", "D"))
    for c in a.commits:
        asunto = subprocess.run(
            ["git", "log", "-1", "--format=%s", c],
            capture_output=True, check=True,
        ).stdout.decode("utf-8", "replace").strip()
        n, cnt = marcador(c, a.corte)
        print("%-12s %-46s %6d %6d %5d %5d %6d" % (
            c, asunto[:46], n, cnt["A"], cnt["B"], cnt["C"], cnt["D"]))
    print()
    print("FIN")


if __name__ == "__main__":
    main()
