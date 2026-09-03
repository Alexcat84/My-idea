# -*- coding: utf-8 -*-
r"""vuelta163_tarea2_flake_154.py . TAREA 2 de la vuelta 163, LA MEDICION DEL
FLAKE QUE NADIE PIDIO PERO QUE SALIO SOLO.

QUE PASO, CON SUS DOS FICHEROS DELANTE. El acta 162 (seccion 5.1) publica que
CUATRO de los veintidos arneses post 147 dan rojo. En MI PRIMERA corrida del
lote salieron **CINCO**: los cuatro suyos mas
`vuelta154_tarea2d_mutacion_guarda.py`, con
`AssertionError: la guarda VIEJA sale roja: la mutacion no ataca el punto ciego`.
En la SEGUNDA corrida del MISMO lote, sobre el MISMO arbol, salieron CUATRO y
ese arnes dio exit 0.

  - corrida 1: `docs/loop/SALIDA_V163_T2_CENSO_POST147.txt` (5 en rojo)
  - corrida 2: `docs/loop/SALIDA_V163_T2_CENSO_POST147_SEGUNDA.txt` (4 en rojo)

NO SE ELIGE LA CORRIDA QUE CONVIENE. Las dos salidas se sellan y se publican, y
este instrumento mide cuantas veces de N el arnes se comporta, para que la
diferencia sea una CIFRA y no una impresion.

LO QUE YA ESTA MEDIDO Y VA AQUI PARA NO REPETIRLO A MANO:
  - corrido SOLO en el arbol de trabajo: exit 0 (cuatro veces seguidas);
  - corrido SOLO en un `git worktree` sobre `3386680e` (el acta 162, que es el
    HEAD de apertura de esta vuelta): exit 0;
  - corrido con `LOOP_BATERIA_EN_CURSO=1`, que es como lo invoca la bateria:
    exit 0;
  - corrido detras de los seis arneses de la 148 y detras del de la 150: exit 0.
  NINGUNA de esas reproducciones lo pone rojo. **NO SE HA REPRODUCIDO, Y SE
  DICE ASI EN VEZ DE DECLARARLO SANO.**

POR QUE IMPORTA Y NO ES UN DETALLE: este arnes ENTRA en la bateria por la
adjudicacion 6.8, y la bateria corre cada script DOS VECES SEGUIDAS. Un arnes
que falla una de cada N corridas convierte la bateria entera en intermitente, y
eso es peor que un rojo fijo, porque un rojo fijo se arregla y un intermitente
se ignora. Entra igual, porque esconderlo seria lo contrario del banco 9, y
entra CON ESTA MEDICION AL LADO.

USO:
  python scripts/loop/vuelta163_tarea2_flake_154.py --repeticiones 3
"""
import argparse
import os
import subprocess
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
ARNES = "vuelta154_tarea2d_mutacion_guarda.py"
MARCA_RECURSION = "LOOP_BATERIA_EN_CURSO"

# LAS DOS SALIDAS SELLADAS DE LAS DOS CORRIDAS DEL LOTE, que son la evidencia.
SALIDAS = [
    ("corrida 1 del lote", "docs/loop/SALIDA_V163_T2_CENSO_POST147.txt"),
    ("corrida 2 del lote", "docs/loop/SALIDA_V163_T2_CENSO_POST147_SEGUNDA.txt"),
]


def veredicto_en(ruta):
    """El exit que la salida sellada publica PARA ESTE ARNES, parseado del
    fichero y no recordado."""
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.exists(p):
        return None
    for l in open(p, encoding="utf-8", errors="replace"):
        if l.strip().startswith(ARNES):
            partes = l.split("exit")
            if len(partes) > 1:
                return int(partes[1].split()[0])
    return None


def correr():
    entorno = dict(os.environ)
    entorno[MARCA_RECURSION] = "1"
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(LOOP, ARNES)],
                       capture_output=True, text=True, cwd=RAIZ, env=entorno,
                       encoding="utf-8", errors="replace")
    return r.returncode, time.time() - t0


def main(repeticiones):
    print("=" * 78)
    print("VUELTA 163, TAREA 2: EL FLAKE DE %s, MEDIDO" % ARNES)
    print("=" * 78)
    print("")
    print("A) LAS DOS CORRIDAS DEL LOTE, PARSEADAS DE SUS SALIDAS SELLADAS")
    veredictos = []
    for etiqueta, ruta in SALIDAS:
        v = veredicto_en(ruta)
        veredictos.append(v)
        print("   %-20s %-52s exit %s" % (etiqueta, ruta, v))
    distintos = len(set(v for v in veredictos if v is not None)) > 1
    print("   CIFRA corridas del lote parseadas: %d" % len([v for v in veredictos if v is not None]))
    print("   LAS DOS DAN LO MISMO: %s" % ("NO, Y ESO ES EL FLAKE" if distintos else "SI"))
    print("")

    print("B) N CORRIDAS SOLITARIAS DE HOY, CON SU CRONOMETRO")
    codigos = []
    for i in range(1, repeticiones + 1):
        c, seg = correr()
        codigos.append(c)
        print("   corrida solitaria %d  exit %-3d %6.1fs" % (i, c, seg))
    print("")

    print("C) LA CUENTA, Y NO SE REDONDEA A SANO")
    verdes = sum(1 for c in codigos if c == 0)
    print("   CIFRA corridas solitarias: %d" % len(codigos))
    print("   CIFRA en exit 0: %d" % verdes)
    print("   CIFRA en rojo: %d" % (len(codigos) - verdes))
    print("   CIFRA veces que se ha visto en rojo, contando el lote: %d"
          % (sum(1 for v in veredictos if v not in (None, 0)) + (len(codigos) - verdes)))
    print("")
    print("   VEREDICTO DE ESTA MEDICION: el rojo EXISTE y esta sellado en")
    print("   docs/loop/SALIDA_V163_T2_CENSO_POST147.txt, y NO SE HA REPRODUCIDO en")
    print("   ninguna de las reconstrucciones. Se declara INTERMITENTE NO REPRODUCIDO,")
    print("   que no es lo mismo que sano, y entra en la bateria con esta nota.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeticiones", type=int, default=3)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(a.repeticiones))
