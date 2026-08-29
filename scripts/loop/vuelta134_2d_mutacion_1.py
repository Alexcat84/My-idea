# -*- coding: utf-8 -*-
"""vuelta134_2d_mutacion_1.py . TAREA 2.d, MUTACION 1 de la vuelta 134.

Copia el REPORTE.md REAL que hay en el arbol (no uno fabricado), cambia una
cifra COTEJABLE ("0 pares", linea de cifras del plan) por un numero distinto
y comprueba que verificar_cifras_del_reporte.py cae en ROJO EXIT 1 nombrando
la linea, la cifra escrita y la contada.

USO:
  python scripts/loop/vuelta134_2d_mutacion_1.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE_REAL = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")


def main():
    with io_open(REPORTE_REAL) as f:
        texto = f.read()
    if "cifras del plan (0 pares)" not in texto:
        print("ROJO PREVIO: no encuentro 'cifras del plan (0 pares)' en el reporte real, cambia el anclaje.")
        return 1
    mutado = texto.replace("cifras del plan (0 pares)", "cifras del plan (5 pares)")

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_134_MUTADO_2D1_")
    os.close(fd)
    with io_open(ruta_tmp, "w") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_tmp],
                            capture_output=True, text=True)
        print("--- copia mutada: '0 pares' -> '5 pares', esperado ROJO nombrando 5 contra 0 ---")
        print(r.stdout)
        print(r.stderr)
        print("EXITCODE proceso: %d" % r.returncode)
        if r.returncode == 1 and "5 pares" in r.stdout and "0" in r.stdout:
            print("MUTACION 1 VERIFICADA: la guarda cae en ROJO nombrando la cifra mutada, como se esperaba.")
            return 0
        print("MUTACION 1 NO VERIFICADA: la guarda no cayo como se esperaba.")
        return 1
    finally:
        os.remove(ruta_tmp)


def io_open(ruta, modo="r"):
    import io
    return io.open(ruta, modo, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
