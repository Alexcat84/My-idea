# -*- coding: utf-8 -*-
r"""vuelta118_tarea2_6_mutacion_dd.py . TAREA 2.6 de la vuelta 118: MUTACION
DD, LADO ROJO, sobre la lista PALABRAS_CIERRE de
vuelta118_tarea2_2_censo_ejecucion_fase04_reparado.py.

QUE HACE. Escribe una COPIA del censo reparado con la palabra "CIERRE"
QUITADA de PALABRAS_CIERRE (sin tocar nada mas), la corre, y verifica que:
  (a) la cabecera imprime una lista MENOR (4 palabras en vez de 5);
  (b) se pierde al menos una celda de "registro en pagina" (OP-E-03 vuelve a
      NO, como en la vuelta 117).
Una lista declarada que nunca fallo no esta probada (EJECUTOR.md, "EL CASO
ROJO SE PRUEBA POR MUTACION").

Pega la salida de ANTES (censo reparado, lista de 5) y la de DESPUES (esta
mutacion, lista de 4) en dos ficheros aparte, y el veredicto en un tercero.

USO:
  python scripts/loop/vuelta118_tarea2_6_mutacion_dd.py
"""
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = sys.executable
ORIGINAL = os.path.join(RAIZ, "scripts", "loop", "vuelta118_tarea2_2_censo_ejecucion_fase04_reparado.py")
MUTADO = os.path.join(RAIZ, "scripts", "loop", "_v118_mut_dd_censo2_sin_cierre.py")


def construir_mutado():
    with open(ORIGINAL, encoding="utf-8") as f:
        texto = f.read()
    vieja = 'PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO", "CIERRE")'
    nueva = 'PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO")  # MUTACION DD: "CIERRE" quitada a proposito'
    assert vieja in texto, "el marcador de PALABRAS_CIERRE no caso: revisar el original"
    nuevo = texto.replace(vieja, nueva)
    with open(MUTADO, "w", encoding="utf-8") as f:
        f.write(nuevo)


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([PY, ruta], cwd=RAIZ, capture_output=True, env=env)
    return r.returncode, r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")


def fila_ope03(salida):
    for l in salida.splitlines():
        if l.strip().startswith("| OP-E-03 |"):
            return l.strip()
    return None


def cabecera_criterio(salida):
    for l in salida.splitlines():
        if l.strip().startswith("CRITERIO IMPRESO"):
            return l.strip()
    return None


def main():
    construir_mutado()

    _cod_antes, out_antes = correr(ORIGINAL)
    _cod_despues, out_despues = correr(MUTADO)

    ruta_antes = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_6_MUTACION_DD_ANTES.txt")
    ruta_despues = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_6_MUTACION_DD_DESPUES.txt")
    ruta_veredicto = os.path.join(RAIZ, "docs", "loop", "SALIDA_V118_TAREA2_6_MUTACION_DD_VEREDICTO.txt")

    with open(ruta_antes, "w", encoding="utf-8") as f:
        f.write(out_antes)
    with open(ruta_despues, "w", encoding="utf-8") as f:
        f.write(out_despues)

    cab_antes = cabecera_criterio(out_antes)
    cab_despues = cabecera_criterio(out_despues)
    fila_antes = fila_ope03(out_antes)
    fila_despues = fila_ope03(out_despues)

    print("ANTES  (lista de 5): %s" % cab_antes)
    print("        %s" % fila_antes)
    print("DESPUES (lista de 4, mutacion DD): %s" % cab_despues)
    print("        %s" % fila_despues)

    lista_menor = ("5 palabra(s)" in (cab_antes or "")) and ("4 palabra(s)" in (cab_despues or ""))
    celda_perdida = (fila_antes == "| OP-E-03 | LISTA | SI | SI | 0/0 |") and (fila_despues == "| OP-E-03 | LISTA | SI | NO | 0/0 |")

    ok = lista_menor and celda_perdida
    veredicto = ("PASA EXIT 0: la mutacion DD imprime una lista menor Y pierde la celda de OP-E-03: la lista "
                 "declarada esta probada.") if ok else "FALLA: la mutacion no se comporto como se esperaba, revisar."

    with open(ruta_veredicto, "w", encoding="utf-8") as f:
        f.write("%s\nANTES: %s | %s\nDESPUES: %s | %s\n" % (veredicto, cab_antes, fila_antes, cab_despues, fila_despues))

    print(veredicto)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
