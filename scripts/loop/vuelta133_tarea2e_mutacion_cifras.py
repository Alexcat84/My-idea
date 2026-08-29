# -*- coding: utf-8 -*-
"""vuelta133_tarea2e_mutacion_cifras.py . PRUEBA DE MUTACION obligatoria de
verificar_cifras_del_reporte.py (TAREA 2.e de la vuelta 133), sobre una COPIA
de un reporte fabricado, nunca sobre docs/loop/REPORTE.md real.

Usa docs/loop/SALIDA_V133_CONTEO_APERTURA.txt, que hoy trae 2 lineas no vacias
(la linea WORK y la linea EXITCODE: 0). Un reporte que cite
"2 lineas (docs/loop/SALIDA_V133_CONTEO_APERTURA.txt)" tiene que cotejar VERDE
(2 == 2); el mismo reporte con "3 lineas" en vez de "2 lineas" tiene que caer
en ROJO nombrando esa cifra.

USO:
  python scripts/loop/vuelta133_tarea2e_mutacion_cifras.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
FICHERO_CITADO = "docs/loop/SALIDA_V133_CONTEO_APERTURA.txt"


def correr(ruta_reporte):
    r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_reporte], cwd=RAIZ,
                        capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout + r.stderr


def escribir_temp(contenido):
    fd, ruta = tempfile.mkstemp(suffix=".md", prefix="REPORTE_133_MUTADO_TAREA2E_")
    os.close(fd)
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    return ruta


def main():
    print("--- (1) reporte fabricado, cifra CORRECTA: 2 lineas ---")
    correcto = ("El conteo de la apertura trae 2 lineas (`%s`), medido hoy.\n" % FICHERO_CITADO)
    ruta = escribir_temp(correcto)
    try:
        ec, salida = correr(ruta)
        print(salida)
        ok1 = ec == 0 and "2 lineas == 2 contados" in salida
        print("CASO (1) %s" % ("VERDE, como se esperaba" if ok1 else "NO SE COMPORTO COMO SE ESPERABA"))
    finally:
        os.remove(ruta)

    print()
    print("--- (2) MUTADO: 3 lineas (deberia caer en ROJO) ---")
    mutado = ("El conteo de la apertura trae 3 lineas (`%s`), medido hoy.\n" % FICHERO_CITADO)
    ruta = escribir_temp(mutado)
    try:
        ec, salida = correr(ruta)
        print(salida)
        ok2 = ec == 1 and "3 linea" in salida
        print("CASO (2) %s" % ("ROJO, como se esperaba" if ok2 else "NO SE COMPORTO COMO SE ESPERABA"))
    finally:
        os.remove(ruta)

    print()
    if ok1 and ok2:
        print("MUTACION VERIFICADA: (1) VERDE 2==2, (2) ROJO nombrando 3 lineas mutadas.")
        return 0
    print("MUTACION NO VERIFICADA.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
