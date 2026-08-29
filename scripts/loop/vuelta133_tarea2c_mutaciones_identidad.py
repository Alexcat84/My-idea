# -*- coding: utf-8 -*-
"""vuelta133_tarea2c_mutaciones_identidad.py . LAS DOS PRUEBAS POR MUTACION DE
tallar_identidad_reporte.py --comparar (TAREA 2.c de la vuelta 133), sobre
COPIAS temporales, nunca sobre docs/loop/REPORTE.md real.

MUTACION A: se toma el parrafo de identidad REAL de la vuelta 132 (el que hoy
vive en docs/loop/REPORTE.md, YA CONOCIDO como la caida: publica en el rotulo
"commit de nacimiento" el mismo hash que "HEAD sellado de apertura", 5eb04ca5,
cuando el medido es 3a5fd829) y se comprueba que --comparar --vuelta 132 cae en
ROJO nombrando ESE rotulo. Es, literalmente, la caida real, no una fabricada.

MUTACION B: se toma un parrafo de identidad CORRECTO (el que tallar_identidad_
reporte.py --vuelta 132 produce de verdad) y se le cambia UN CARACTER del hash
del tercer rotulo (HEAD sellado de cierre), y se comprueba que --comparar
--vuelta 132 tambien cae en ROJO nombrando ese rotulo.

USO:
  python scripts/loop/vuelta133_tarea2c_mutaciones_identidad.py
"""
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TALLADOR = os.path.join(RAIZ, "scripts", "loop", "tallar_identidad_reporte.py")


def correr(args):
    r = subprocess.run([sys.executable, TALLADOR] + args, cwd=RAIZ,
                        capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout + r.stderr


def escribir_temp(contenido):
    fd, ruta = tempfile.mkstemp(suffix=".md", prefix="REPORTE_132_MUTADO_")
    os.close(fd)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return ruta


def mutacion_a():
    print("--- MUTACION A: caida real de la 132 (nacimiento == apertura, 5eb04ca5) ---")
    contenido = (
        "Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `5eb04ca5`\n"
        "(acta 131), commit de nacimiento de las salidas de apertura `5eb04ca5`,\n"
        "HEAD sellado de cierre `3a5fd829` (`SALIDA_V132_HEAD_CIERRE.txt`, sellado\n"
    )
    ruta = escribir_temp(contenido)
    try:
        ec, salida = correr(["--vuelta", "132", "--comparar", ruta])
        print(salida)
        ok = ec == 1 and "commit de nacimiento de las salidas de apertura" in salida
        print("MUTACION A %s: exit %d, %s" %
              ("VERIFICADA" if ok else "FALLIDA", ec,
               "cae en ROJO nombrando el rotulo mutado" if ok else "NO nombro el rotulo esperado"))
        return ok
    finally:
        os.remove(ruta)


def mutacion_b():
    print("--- MUTACION B: un caracter cambiado en HEAD sellado de cierre ---")
    ec0, correcto = correr(["--vuelta", "132"])
    if ec0 != 0:
        print("no se pudo tallar la vuelta 132 correcta: %s" % correcto)
        return False
    lineas = correcto.strip().splitlines()
    mutadas = []
    for l in lineas:
        if l.startswith("HEAD sellado de cierre"):
            partes = l.split("`")
            hash_ = partes[1]
            hash_mutado = ("f" if hash_[0] != "f" else "0") + hash_[1:]
            l = l.replace("`%s`" % hash_, "`%s`" % hash_mutado)
        mutadas.append(l)
    contenido = "\n".join(mutadas) + "\n"
    ruta = escribir_temp(contenido)
    try:
        ec, salida = correr(["--vuelta", "132", "--comparar", ruta])
        print(salida)
        ok = ec == 1 and "HEAD sellado de cierre" in salida
        print("MUTACION B %s: exit %d, %s" %
              ("VERIFICADA" if ok else "FALLIDA", ec,
               "cae en ROJO nombrando el rotulo mutado" if ok else "NO nombro el rotulo esperado"))
        return ok
    finally:
        os.remove(ruta)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=["a", "b"], default=None)
    a = ap.parse_args()

    if a.solo == "a":
        return 0 if mutacion_a() else 1
    if a.solo == "b":
        return 0 if mutacion_b() else 1

    a_ok = mutacion_a()
    print()
    b_ok = mutacion_b()
    print()
    if a_ok and b_ok:
        print("LAS DOS MUTACIONES VERIFICADAS: la guarda cae en ROJO en los dos casos, como se esperaba.")
        return 0
    print("ALGUNA MUTACION NO SE COMPORTO COMO SE ESPERABA.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
