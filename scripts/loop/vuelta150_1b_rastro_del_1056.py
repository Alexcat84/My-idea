# -*- coding: utf-8 -*-
"""vuelta150_1b_rastro_del_1056.py . EL RASTRO DE LA VERIFICACION 4 DE OP-S-12,
MEDIDO CON INSTRUMENTO PROPIO (TAREA 1.b de la vuelta 150).

La ficha de OP-S-12 exige "el numero total de entradas baja en exactamente
1.056" y la operacion de la vuelta 148 retiro 925. El acta 149 (adjudicacion
3.8) dice que no es contradiccion sino una cifra fiel a un corte que se movio, y
lo sostiene sobre un rastro. EJECUTOR.md 2 dice que un acta previa NUNCA es
fuente de una cifra nueva: se cita como contraste y, si discrepa de la medicion
de hoy, la discrepancia se DECLARA en vez de resolverse copiando. Asi que aqui
se vuelve a medir todo, version por version.

QUE MIDE, sobre docs/plan/ARISTAS_DUPLICADAS.jsonl y su historia en git:
  1. cuantas versiones tiene el fichero en git (git log --follow);
  2. de la PRIMERA version y de la de HEAD: grupos, nodos y entradas que sobran;
  3. de la de HEAD: cuantos de esos grupos viven sobre nodos que HOY estan
     deprecados, y cuantas entradas quedan sobre vivos;
  4. la serie entera de las treinta versiones, para ver si la bajada es monotona
     o no, que es lo que el acta afirma y aqui se comprueba.

NO ESCRIBE NADA en el repo: solo imprime.

USO:
  python scripts/loop/vuelta150_1b_rastro_del_1056.py
"""
import io
import json
import subprocess

RUTA = "docs/plan/ARISTAS_DUPLICADAS.jsonl"


def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: git " + " ".join(args))
    return r.stdout.decode("utf-8", "replace")


def filas_de(ref):
    if ref == "WORK":
        texto = io.open(RUTA, encoding="utf-8").read()
    else:
        texto = git("show", "%s:%s" % (ref, RUTA))
    out = []
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea:
            out.append(json.loads(linea))
    return out


def cuenta(filas):
    grupos = len(filas)
    nodos = len({f["nodo"] for f in filas})
    sobran = sum(int(f["sobran"]) for f in filas)
    return grupos, nodos, sobran


def main():
    versiones = [l.split()[0] for l in git(
        "log", "--follow", "--format=%H %s", "--", RUTA).splitlines() if l.strip()]
    print("VERSIONES DE %s EN GIT (git log --follow): %d" % (RUTA, len(versiones)))
    primera = versiones[-1]
    ultima = versiones[0]
    print("  la PRIMERA es %s" % primera[:8])
    print("  la de HEAD es %s" % ultima[:8])
    print("")

    g1, n1, s1 = cuenta(filas_de(primera))
    print("PRIMERA VERSION (%s): %d grupos / %d nodos / %d entradas que sobran"
          % (primera[:8], g1, n1, s1))
    gh, nh, sh = cuenta(filas_de(ultima))
    print("VERSION DE HEAD (%s): %d grupos / %d nodos / %d entradas que sobran"
          % (ultima[:8], gh, nh, sh))
    print("")

    # 3. cuantas de las de HEAD viven sobre nodos HOY deprecados
    N = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
    depre = {k for k, v in N.items() if v.get("deprecado")}
    filas_head = filas_de(ultima)
    sobre_depre = [f for f in filas_head if f["nodo"] in depre]
    sobran_depre = sum(int(f["sobran"]) for f in sobre_depre)
    sobre_fantasma = [f for f in filas_head if f["nodo"] not in N]
    sobran_vivos = sh - sobran_depre - sum(int(f["sobran"]) for f in sobre_fantasma)
    print("DE LAS %d DE HEAD, REPARTIDAS CONTRA EL GRAFO DE HOY:" % sh)
    print("  entradas que sobran sobre nodos HOY DEPRECADOS: %d (en %d grupo(s))"
          % (sobran_depre, len(sobre_depre)))
    print("  entradas que sobran sobre nodos QUE YA NO EXISTEN: %d (en %d grupo(s))"
          % (sum(int(f["sobran"]) for f in sobre_fantasma), len(sobre_fantasma)))
    print("  entradas que sobran sobre nodos VIVOS: %d" % sobran_vivos)
    for f in sobre_depre:
        print("    deprecado: %s.%s -> %s (sobran %s)"
              % (f["nodo"], f["campo"], f["destino"], f["sobran"]))
    print("")

    print("LA SERIE ENTERA, DE LA PRIMERA A LA DE HEAD (grupos / nodos / sobran):")
    serie = []
    for ref in reversed(versiones):
        g, n, s = cuenta(filas_de(ref))
        serie.append(s)
        print("  %s  %5d / %5d / %5d" % (ref[:8], g, n, s))
    monotona = all(serie[i] >= serie[i + 1] for i in range(len(serie) - 1))
    print("")
    print("BAJADA MONOTONA (ninguna version sube respecto de la anterior): %s" % monotona)
    print("PRIMERA %d, ULTIMA %d, DIFERENCIA %d" % (serie[0], serie[-1], serie[0] - serie[-1]))


main()
