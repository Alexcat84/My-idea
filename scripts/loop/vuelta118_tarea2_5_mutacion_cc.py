# -*- coding: utf-8 -*-
r"""vuelta118_tarea2_5_mutacion_cc.py . TAREA 2.5 de la vuelta 118: MUTACION
CC, LADO ROJO, sobre la guarda de negacion de
vuelta118_tarea2_1_censo_tres_superficies_reparado.py.

QUE HACE. Escribe una COPIA del censo reparado con `negacion_delante()`
forzada a devolver siempre None (sin tocar nada mas: mismas DEPENDENCIAS,
mismo FRASE_C, mismo MARCAS_NEGACION declarado en la salida), la corre, y
verifica que OP-D-07 superficie (C) VUELVE a dar SI: una guarda que nunca
fallo no esta probada (EJECUTOR.md, "EL CASO ROJO SE PRUEBA POR MUTACION").

Pega la salida de ANTES (censo reparado, con guarda) y la de DESPUES (esta
mutacion, sin guarda) en dos ficheros aparte, y el veredicto en un tercero.

USO:
  python scripts/loop/vuelta118_tarea2_5_mutacion_cc.py
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable
ORIGINAL = os.path.join(RAIZ, "scripts", "loop", "vuelta118_tarea2_1_censo_tres_superficies_reparado.py")
MUTADO = os.path.join(RAIZ, "scripts", "loop", "_v118_mut_cc_censo1_sin_guarda.py")


def construir_mutado():
    with open(ORIGINAL, encoding="utf-8") as f:
        texto = f.read()
    marca = "def negacion_delante(texto, idx):"
    idx = texto.index(marca)
    fin_doc = texto.index('"""', texto.index('"""', idx) + 3) + 3
    cuerpo_mutado = (
        "def negacion_delante(texto, idx):\n"
        "    \"\"\"MUTACION CC: guarda de negacion DESACTIVADA a proposito, sin tocar nada mas.\"\"\"\n"
        "    return None\n"
    )
    nuevo = texto[:idx] + cuerpo_mutado + texto[fin_doc:]
    assert nuevo != texto, "la mutacion no cambio nada: el marcador no caso"
    with open(MUTADO, "w", encoding="utf-8") as f:
        f.write(nuevo)


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, ruta], cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")


def fila_opd07(salida):
    for l in salida.splitlines():
        if l.strip().startswith("| OP-D-07 |"):
            return l.strip()
    return None


def main():
    construir_mutado()

    _cod_antes, out_antes = correr(ORIGINAL)
    _cod_despues, out_despues = correr(MUTADO)

    ruta_antes = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_5_MUTACION_CC_ANTES.txt")
    ruta_despues = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_5_MUTACION_CC_DESPUES.txt")
    ruta_veredicto = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_5_MUTACION_CC_VEREDICTO.txt")

    with open(ruta_antes, "w", encoding="utf-8") as f:
        f.write(out_antes)
    with open(ruta_despues, "w", encoding="utf-8") as f:
        f.write(out_despues)

    fila_antes = fila_opd07(out_antes)
    fila_despues = fila_opd07(out_despues)

    print("ANTES  (con guarda de negacion): %s" % fila_antes)
    print("DESPUES (SIN guarda, mutacion CC): %s" % fila_despues)

    ok = (fila_antes == "| OP-D-07 | SI | SI | NO |") and (fila_despues == "| OP-D-07 | SI | SI | SI |")
    veredicto = "PASA EXIT 0: la mutacion CC vuelve a dar SI en OP-D-07 (C), la guarda esta probada." if ok else \
                "FALLA: la mutacion no se comporto como se esperaba, revisar."

    with open(ruta_veredicto, "w", encoding="utf-8") as f:
        f.write("%s\nANTES: %s\nDESPUES: %s\n" % (veredicto, fila_antes, fila_despues))

    print(veredicto)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
