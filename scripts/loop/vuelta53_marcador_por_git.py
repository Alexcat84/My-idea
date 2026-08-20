# -*- coding: utf-8 -*-
"""vuelta53_marcador_por_git.py . EL MARCADOR DE UN ESTADO PASADO DEL ARBOL,
LEIDO DEL PROPIO GIT Y NO DE UN ACTA, CON SUS PORCENTAJES.

SUCESOR DECLARADO de scripts/loop/vuelta52_marcador_por_git.py, al que NO
reemplaza. La aritmetica del marcador es LA MISMA, digito a digito, para que
las dos corridas sigan siendo comparables.

EL UNICO CAMBIO, declarado con su motivo, porque cambiar un instrumento sin
declararlo es lo que la regla 2 del EJECUTOR.md prohibe: SE ANADEN LAS CUATRO
COLUMNAS DE PORCENTAJE. El motivo lo trae el encargo de la vuelta 53 (TAREA
1.2): la tabla del cierre de la vuelta 20 en docs/plan/RECOMPUTO_3388.md no
publica solo el marcador, publica tambien "(17,0 / 2,4 / 0,2 / 80,3 por
ciento)", y esos cuatro porcentajes son los del 575, es decir los del
MANTENIMIENTO MUERTO que esta vuelta tacha. Al dejar VISIBLE el 583 hay que
dejar visibles TAMBIEN sus porcentajes, y la regla 1 del EJECUTOR (cuarto
renglon, LA TABLA SE IMPRIME, NO SE TECLEA) prohibe teclearlos: se leen de la
salida de un instrumento corrido en esta vuelta.

EL REDONDEO ES EL DE scripts/recomputar_marcador.py, no otro: round(x/n*100, 1).
Se dice porque un redondeo distinto fabricaria una discrepancia que no existe.

NO HACE CHECKOUT y por eso no puede ensuciar el arbol: lee el fichero de
veredictos del objeto de git con `git show <commit>:<ruta>` y cuenta.

DE SOLO LECTURA sobre el arbol de trabajo. No escribe ningun fichero: imprime.

Uso:
  python scripts/loop/vuelta53_marcador_por_git.py 7b21a8d0 1bfab1c4 --corte 3388
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

    print("=" * 96)
    print("EL MARCADOR DE CADA ESTADO, LEIDO DE GIT, CON PORCENTAJES (corte %d)" % a.corte)
    print("fichero: %s" % RUTA)
    print("redondeo: el mismo de scripts/recomputar_marcador.py, round(x/n*100, 1)")
    print("=" * 96)
    print()
    print("%-12s %-40s %6s %6s %5s %5s %6s | %6s %5s %5s %6s" % (
        "commit", "asunto", "n", "A", "B", "C", "D", "%A", "%B", "%C", "%D"))
    for c in a.commits:
        asunto = subprocess.run(
            ["git", "log", "-1", "--format=%s", c],
            capture_output=True, check=True,
        ).stdout.decode("utf-8", "replace").strip()
        n, cnt = marcador(c, a.corte)
        pct = [round(cnt[k] / n * 100, 1) for k in ("A", "B", "C", "D")]
        print("%-12s %-40s %6d %6d %5d %5d %6d | %6s %5s %5s %6s" % (
            c, asunto[:40], n, cnt["A"], cnt["B"], cnt["C"], cnt["D"],
            pct[0], pct[1], pct[2], pct[3]))
    print()
    print("FIN")


if __name__ == "__main__":
    main()
