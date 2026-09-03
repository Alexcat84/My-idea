# -*- coding: utf-8 -*-
r"""vuelta163_tarea2_censo_arneses.py . TAREA 2 de la vuelta 163, PRIMERA MITAD:
EL CENSO Y LA CORRIDA DE LOS ARNESES QUE ESTAN FUERA DE LA NOMINA.

POR QUE NACE: adjudicacion 6.8 del acta 162, seccion 5.1. La nomina de
`scripts/loop/verificar_mutaciones_viejas.py` lleva quince vueltas congelada (su
ultima vuelta representada es la 147) y hay arneses de mutacion nacidos despues
que nunca entraron. La regla que lo prohibe esta escrita DENTRO de la propia
guarda, y la escribio el acta 144.

QUE HACE: censa, corre y MIDE. No escribe nomina: eso lo hace la segunda mitad
(`vuelta163_tarea2_poner_al_dia.py`). Aqui solo se produce la cifra con la que
se decide, con su cronometro y su primera linea util, para que ningun arnes
entre "en verde alegado".

EL CRITERIO DE CENSO ES EL DEL AUDITOR Y NO SE ESTRECHA: fichero de
`scripts/loop/` que case `vuelta<N>...mutacion...py`. Se reusa a proposito para
que la cifra sea comparable con la que el acta 162 publica.

USO:
  python scripts/loop/vuelta163_tarea2_censo_arneses.py            (los post 147)
  python scripts/loop/vuelta163_tarea2_censo_arneses.py --previos  (los 41 de la 5.b)
"""
import argparse
import os
import re
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
GUARDA = os.path.join(LOOP, "verificar_mutaciones_viejas.py")
MARCA_RECURSION = "LOOP_BATERIA_EN_CURSO"


def nomina_de_la_guarda():
    src = open(GUARDA, encoding="utf-8").read()
    return sorted(set(re.findall(r'\("(vuelta\d+[^"]*\.py)",\s*(?:True|False)\)', src)))


def arneses():
    return sorted(f for f in os.listdir(LOOP)
                  if re.match(r"vuelta\d+.*mutacion", f) and f.endswith(".py"))


def vuelta_de(f):
    return int(re.match(r"vuelta(\d+)", f).group(1))


def censo():
    nomina = nomina_de_la_guarda()
    todos = arneses()
    fuera = [f for f in todos if f not in nomina]
    ultima = max(vuelta_de(f) for f in nomina)
    post = [f for f in fuera if vuelta_de(f) > ultima]
    previos = [f for f in fuera if vuelta_de(f) <= ultima]
    return nomina, todos, fuera, ultima, post, previos


def correr(script):
    entorno = dict(os.environ)
    entorno[MARCA_RECURSION] = "1"
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(LOOP, script)],
                       capture_output=True, text=True, cwd=RAIZ, env=entorno,
                       encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or ""), time.time() - t0


def primera_linea_util(salida):
    for l in salida.splitlines():
        if l.strip():
            return l.strip()[:150]
    return "(sin salida)"


def ultima_linea_util(salida):
    for l in reversed(salida.splitlines()):
        if l.strip():
            return l.strip()[:200]
    return "(sin salida)"


def main(previos=False):
    nomina, todos, fuera, ultima, post, prev = censo()
    lote = prev if previos else post
    titulo = ("LOS %d ARNESES ANTERIORES A LA VUELTA %d QUE ESTAN FUERA DE LA NOMINA"
              % (len(prev), ultima + 1)) if previos else \
             ("LOS %d ARNESES POSTERIORES A LA VUELTA %d QUE ESTAN FUERA DE LA NOMINA"
              % (len(post), ultima))
    print("=" * 78)
    print("VUELTA 163, TAREA %s: %s" % ("5.b" if previos else "2", titulo))
    print("=" * 78)
    print("")
    print("A) EL CENSO, RECOMPUTADO HOY")
    print("   CIFRA nomina de verificar_mutaciones_viejas.py: %d" % len(nomina))
    print("   CIFRA arneses de mutacion en scripts/loop: %d" % len(todos))
    print("   CIFRA fuera de la nomina: %d" % len(fuera))
    print("   CIFRA ultima vuelta representada en la nomina: %d" % ultima)
    print("   CIFRA fuera y POSTERIORES a esa vuelta: %d" % len(post))
    print("   CIFRA fuera y ANTERIORES o iguales a esa vuelta: %d" % len(prev))
    print("")
    print("B) EL LOTE DE ESTA CORRIDA, NOMBRE A NOMBRE Y SIN RESUMIR")
    for f in lote:
        print("   vuelta %-4d %s" % (vuelta_de(f), f))
    print("   CIFRA del lote: %d" % len(lote))
    print("")
    print("C) LA CORRIDA, CON SU CRONOMETRO")
    verdes, rojos = [], []
    total = 0.0
    for f in lote:
        codigo, salida, seg = correr(f)
        total += seg
        (verdes if codigo == 0 else rojos).append((f, codigo))
        print("   %-46s exit %-3d %6.1fs" % (f, codigo, seg))
        if codigo != 0:
            print("      primera linea: %s" % primera_linea_util(salida))
            print("      ultima  linea: %s" % ultima_linea_util(salida))
    print("")
    print("D) LA CUENTA")
    print("   CIFRA corridos: %d" % len(lote))
    print("   CIFRA exit 0: %d (%s)" % (len(verdes), ", ".join(f for f, _c in verdes) or "ninguno"))
    print("   CIFRA en rojo: %d (%s)" % (len(rojos), ", ".join(f for f, _c in rojos) or "ninguno"))
    print("   CRONOMETRO total del lote: %.1fs" % total)
    print("")
    if previos:
        print("ES UNA MEDICION Y SE PARA AHI: NINGUNO DE ESTOS ENTRA EN LA BATERIA.")
        print("La regla de la bateria nace en la vuelta 144 y no dice si es")
        print("retroactiva; con esta cifra delante se decide, que es lo que la 6.7 del")
        print("acta 156 hizo con las nueve salidas de la P3b.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--previos", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(previos=a.previos))
