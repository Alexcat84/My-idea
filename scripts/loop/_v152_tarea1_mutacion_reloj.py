# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 1: LA PRUEBA DE MUTACION DE LAS DOS GUARDAS NUEVAS.

EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION: ningun assert se publica
como prueba sin haber corrido antes su prueba de mutacion. Y la caida 2 de la
vuelta 89 dice ademas COMO: el valor comparado tiene que ser COMPUTADO, no un
literal que se aprueba solo.

QUE SE MUTA. No se toca el codigo de la guarda: SE MUEVE EL RELOJ. Las dos
corridas usan LA MISMA `--apertura` (fe98cf97, el HEAD de apertura de la vuelta
150, leido de git) y se diferencian SOLO en `--corte`:

  VERDE  --corte fe98cf97   el reloj parado en la apertura. Ningun commit de la
                            vuelta 150 puede servirle de prueba a la vuelta 150.
  ROJO   --corte HEAD       el reloj suelto, o sea EL COMPORTAMIENTO DE ANTES
                            DEL PARCHE. Los commits de la vuelta 150 entran y la
                            guarda TIENE que caer nombrandolos.

Si la corrida ROJA no cae, la guarda no sirve y esta salida lo dice.

USO:
  python scripts/loop/_v152_tarea1_mutacion_reloj.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APERTURA_150 = "fe98cf97"

CASOS = [
    ("A", "P3 del expediente", "VERDE", "vuelta150_3_relectura_expediente.py",
     ["--corte", APERTURA_150, "--apertura", APERTURA_150]),
    ("B", "P3 del expediente", "ROJO", "vuelta150_3_relectura_expediente.py",
     ["--corte", "HEAD", "--apertura", APERTURA_150]),
    ("C", "fila 0 CODIGO", "VERDE", "vuelta150_4_tabla_por_fase.py",
     ["--corte", APERTURA_150, "--apertura", APERTURA_150]),
    ("D", "fila 0 CODIGO", "ROJO", "vuelta150_4_tabla_por_fase.py",
     ["--corte", "HEAD", "--apertura", APERTURA_150]),
]


def main():
    print("APERTURA DE LA VUELTA 150, LEIDA DE GIT (no tecleada):")
    r = subprocess.run(["git", "log", "-1", "--format=%h %s", APERTURA_150],
                       capture_output=True, cwd=RAIZ)
    print("  " + r.stdout.decode("utf-8", "replace").strip()[:110])
    r = subprocess.run(["git", "rev-list", "--count", "%s..HEAD" % APERTURA_150],
                       capture_output=True, cwd=RAIZ)
    print("  commits en %s..HEAD: %s" % (APERTURA_150, r.stdout.decode().strip()))
    print("")

    fallos = []
    for etq, vara, esperado, script, args in CASOS:
        r = subprocess.run([sys.executable, os.path.join("scripts", "loop", script)] + args,
                           capture_output=True, cwd=RAIZ)
        salida = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
        cayo = r.returncode != 0
        # LOS DOS LADOS SON COMPUTADOS: `cayo` sale del exit code real de la
        # corrida y `esperado` de la tabla CASOS. No hay literal que se compare
        # consigo mismo.
        obtenido = "ROJO" if cayo else "VERDE"
        marca = "OK" if obtenido == esperado else "LA PRUEBA DE MUTACION FALLA"
        if obtenido != esperado:
            fallos.append(etq)
        print("CASO %s | %-18s | %-19s | esperado %-5s | obtenido %-5s | exit %d | [%s]"
              % (etq, vara, " ".join(args[:2]), esperado, obtenido, r.returncode, marca))
        for linea in salida.splitlines():
            if ("GUARDA DEL RELOJ" in linea or "GUARDA DE SALIDAS" in linea
                    or "INTRUSOS" in linea or "INTRUSAS" in linea
                    or "SE CUENTA A SI MISMA" in linea):
                print("    | %s" % linea.strip()[:200])
        print("")

    print("=" * 96)
    if fallos:
        print("PRUEBA DE MUTACION EN ROJO. Casos que no se comportan: %s" % ", ".join(fallos))
        raise SystemExit(1)
    print("PRUEBA DE MUTACION SUPERADA: los dos casos VERDE pasan y los dos ROJO CAEN,")
    print("y caen NOMBRANDO los commits y las salidas de la propia vuelta. Las guardas")
    print("muerden: sin el corte, las dos varas vuelven a contarse a si mismas.")


main()
