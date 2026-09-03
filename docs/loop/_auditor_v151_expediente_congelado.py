# -*- coding: utf-8 -*-
"""Auditor v151: LA MISMA VARA DEL EJECUTOR, CON EL RELOJ DE GIT PARADO.

Importa scripts/loop/vuelta150_3_relectura_expediente.py sin tocarlo y solo le
sustituye la pierna P3 por una identica cuyo `git log` va cortado en
`c9c6ea40~1`, o sea el arbol de justo ANTES del commit de la TAREA 3 de la
vuelta 150.

POR QUE EXISTE. La P3 pide "un commit que NOMBRA el id_op y ademas toca
dataset/, scripts/, engine/ o web/". El commit c9c6ea40 nombra a OP-V-01 y a
OP-L-01 en su cuerpo y toca scripts/loop/, asi que a partir de el la vara se
cuenta a si misma: el acto de publicar que esas dos fichas no tienen prueba de
ejecucion ES la prueba que les faltaba. Congelando el reloj se comprueba si las
cifras que el reporte publica eran fieles al instrumento en el momento de
correrlo. Lo son: reproducen las siete al digito.

Salida commiteada en docs/loop/_auditor_v151_expediente_congelado.txt.
"""
import json
import re
import subprocess
import sys

sys.path.insert(0, "scripts/loop")
import vuelta150_3_relectura_expediente as V  # noqa: E402

CORTE = "c9c6ea40~1"


def p3_congelado(ids):
    hits = {}
    for i in ids:
        r = subprocess.run(["git", "log", CORTE, "--format=%H", "-E", "--grep",
                            re.escape(i) + "([^A-Za-z0-9_-]|$)"],
                           capture_output=True, cwd=V.RAIZ)
        commits = [c for c in r.stdout.decode().split() if c]
        con = []
        for c in commits:
            n = subprocess.run(["git", "show", "--name-only", "--format=", c],
                               capture_output=True, cwd=V.RAIZ).stdout.decode("utf-8", "replace")
            if any(x.startswith(("dataset/", "scripts/", "engine/", "web/"))
                   for x in n.splitlines() if x.strip()):
                con.append(c[:8])
        hits[i] = (len(commits), con)
    return hits


def main():
    F = V.fichas()
    ids = [f["id_op"] for f in F]
    p1 = V.p1_vara_de_grafo()
    p2 = V.p2_vara_de_codigo(ids)
    p3 = p3_congelado(ids)

    n1 = sum(1 for i in ids if p1.get(i, (False,))[0])
    n2 = sum(1 for i in ids if p2[i])
    n3 = sum(1 for i in ids if p3[i][1])

    noc, dec, sil, hsin, sinprueba = [], 0, 0, 0, []
    for f in F:
        i = f["id_op"]
        a = p1.get(i, (False,))[0]
        b = bool(p2[i])
        c = bool(p3[i][1])
        e = a or b or c
        if f["estado"] == "HECHA" and not e:
            hsin += 1
        if f["estado"] == "LISTA" and e:
            noc.append(i)
            d, _ = V.declara_su_estado(f)
            dec += 1 if d else 0
            sil += 0 if d else 1
        if f["estado"] == "LISTA" and not e:
            sinprueba.append(i)

    print("CORTE DE GIT:", CORTE)
    print("cobertura: P1 %d / P2 %d / P3 %d" % (n1, n2, n3))
    print("no calzan %d | calzan %d | DECLARADAS %d | EN SILENCIO %d | HECHA sin prueba %d"
          % (len(noc), len(F) - len(noc), dec, sil, hsin))
    print("LISTA sin ninguna prueba:", sinprueba)


if __name__ == "__main__":
    main()
