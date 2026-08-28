# -*- coding: utf-8 -*-
r"""vuelta117_tarea2_3_mutacion_bb.py . MUTACION BB (TAREA 2.3 de la vuelta
117): prueba, DEL LADO ROJO, que el numero de instrumentos que
vuelta117_guardas_cierre.py imprime SI se mueve cuando la lista INSTRUMENTOS
se mueve (la caida D.1 del acta 116 era exactamente lo contrario: un numero
tecleado que NUNCA se movia, aunque la lista tuviera ocho en vez de nueve).

QUE HACE. Escribe una COPIA de vuelta117_guardas_cierre.py
(scripts/loop/_v117_mut_bb_copia.py, commiteada como pieza historica) con UNA
sola edicion: se quita la entrada "9. tallar_cifras_de_antes.py (sobre el
propio REPORTE.md)" de INSTRUMENTOS, y NADA MAS. No se toca ninguna otra
lista, ningun CASO, ninguna ancla.

LA VARA. La copia mutada tiene que imprimir un numero MENOR de instrumentos,
en su linea de apertura Y en su linea de cierre, que la version real (8 en
vez de 9); no puede seguir diciendo 9 como si nada. Se corren las DOS
versiones (el fichero real de hoy, sin mutar, y la copia mutada) y se pegan
las dos salidas completas, cada una en su fichero nombrado:
  docs/loop/SALIDA_V117_TAREA2_3_MUTACION_BB_ANTES.txt (el real, dice 9)
  docs/loop/SALIDA_V117_TAREA2_3_MUTACION_BB_DESPUES.txt (la copia mutada,
    dice 8)

USO:
  python scripts/loop/vuelta117_tarea2_3_mutacion_bb.py
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable
ORIGINAL = os.path.join(RAIZ, "scripts", "loop", "vuelta117_guardas_cierre.py")
COPIA = os.path.join(RAIZ, "scripts", "loop", "_v117_mut_bb_copia.py")

ENTRADA_A_QUITAR = (
    '    ("9. tallar_cifras_de_antes.py (sobre el propio REPORTE.md)",\n'
    '     ["scripts/loop/tallar_cifras_de_antes.py"], 0),\n'
)


def escribir_copia_mutada():
    with open(ORIGINAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(ENTRADA_A_QUITAR) != 1:
        raise SystemExit("ROJO: la entrada 9 de INSTRUMENTOS a quitar no aparece EXACTAMENTE "
                          "una vez en %s (aparece %d veces). NO SE MUTA NADA."
                          % (ORIGINAL, texto.count(ENTRADA_A_QUITAR)))
    mutado = texto.replace(ENTRADA_A_QUITAR, "", 1)
    with open(COPIA, "w", encoding="utf-8") as f:
        f.write(mutado)


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, ruta], cwd=RAIZ, capture_output=True, env=env)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def numero_de_instrumentos(out, patron):
    m = re.search(patron, out)
    return int(m.group(1)) if m else None


def main():
    escribir_copia_mutada()

    cod_antes, out_antes = correr(ORIGINAL)
    cod_despues, out_despues = correr(COPIA)

    # La linea "LOS N INSTRUMENTOS:" se imprime SIEMPRE, calce o no calce
    # cada instrumento (a diferencia de la linea VERDE de cierre, que solo
    # sale si TODO calza). Es la que se usa para las dos mediciones, apertura
    # y cierre, para que la vara no dependa de que el resto de la guarda de
    # VERDE.
    n_apertura_antes = numero_de_instrumentos(out_antes, r"VUELTA 117: (\d+) INSTRUMENTOS")
    n_apertura_despues = numero_de_instrumentos(out_despues, r"VUELTA 117: (\d+) INSTRUMENTOS")
    n_cierre_antes = numero_de_instrumentos(out_antes, r"LOS (\d+) INSTRUMENTOS:")
    n_cierre_despues = numero_de_instrumentos(out_despues, r"LOS (\d+) INSTRUMENTOS:")

    print("=== ANTES (fichero real, sin mutar) ===")
    print("EXIT guarda entera: %d" % cod_antes)
    print("instrumentos en la apertura: %s" % n_apertura_antes)
    print("instrumentos en el bloque 'LOS N INSTRUMENTOS': %s" % n_cierre_antes)
    print()
    print("=== DESPUES (copia mutada, entrada 9 de INSTRUMENTOS quitada) ===")
    print("EXIT guarda entera: %d" % cod_despues)
    print("instrumentos en la apertura: %s" % n_apertura_despues)
    print("instrumentos en el bloque 'LOS N INSTRUMENTOS': %s" % n_cierre_despues)
    print()

    ok_antes = n_apertura_antes == 9 and n_cierre_antes == 9
    ok_despues = (n_apertura_despues == 8 and n_cierre_despues == 8
                  and n_apertura_despues < n_apertura_antes)

    print("VARA: ANTES dice 9 en las dos lineas (%s); DESPUES de quitar una entrada dice 8 en "
          "las dos, un numero MENOR que antes, no el mismo (%s)." % (ok_antes, ok_despues))
    if ok_antes and ok_despues:
        print("PASA: el conteo de instrumentos SI se mueve cuando la lista se mueve; no queda "
              "tecleado.")
        return 0
    print("NO PASA: la mutacion BB no se comporto como se esperaba.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
