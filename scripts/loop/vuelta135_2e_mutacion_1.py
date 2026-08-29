# -*- coding: utf-8 -*-
"""vuelta135_2e_mutacion_1.py . MUTACION 1 de TAREA 2.e de la vuelta 135
(acta 134, 4.1): sobre una COPIA del REPORTE REAL de la vuelta 134
(docs/loop/REPORTE.md tal como esta en el arbol al abrir esta vuelta,
antes de reescribirlo), `118 grafias` pasa a `999 grafias`, dejando el
literal `(sin instrumento)` y la cita de `SALIDA_V134_4A_CENSO_COLA.txt`
exactamente donde estan. Con la exencion (iii) vieja esto daba VERDE EXIT
0 (la caida que prueba el auditor, mutacion (A) de su acta 134). Con la
regla nueva de 2.b tiene que caer ROJO EXIT 1, nombrando la cifra y el
fichero.

Salida: docs/loop/SALIDA_V135_2E_MUTACION_1.txt

USO:
  python scripts/loop/vuelta135_2e_mutacion_1.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE_REAL = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_2E_MUTACION_1.txt")

VIEJO = "118 grafias (sin instrumento)"
NUEVO = "999 grafias (sin instrumento)"


def main():
    with io.open(REPORTE_REAL, encoding="utf-8") as f:
        texto = f.read()
    if texto.count(VIEJO) != 1:
        print("ROJO PREVIO: '%s' no aparece exactamente una vez en el reporte real." % VIEJO)
        return 1
    mutado = texto.replace(VIEJO, NUEVO)

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_134_MUTACION1_")
    os.close(fd)
    with io.open(ruta_tmp, "w", encoding="utf-8") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_tmp],
                            capture_output=True, text=True)
        salida_txt = (
            "MUTACION 1: '%s' -> '%s' sobre copia de REPORTE.md (vuelta 134 real).\n"
            "--- salida de verificar_cifras_del_reporte.py ---\n%s\n%s\n"
            "EXITCODE proceso: %d\n" % (VIEJO, NUEVO, r.stdout, r.stderr, r.returncode)
        )
        verificada = (r.returncode == 1 and "999 grafias" in r.stdout)
        salida_txt += ("MUTACION VERIFICADA: cayo ROJO nombrando la cifra mutada, como se esperaba.\n"
                        if verificada else
                        "MUTACION NO VERIFICADA: no cayo como se esperaba.\n")
        salida_txt += "EXITCODE: %d\n" % (0 if verificada else 1)
    finally:
        os.remove(ruta_tmp)

    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(salida_txt)
    print(salida_txt)
    return 0 if verificada else 1


if __name__ == "__main__":
    raise SystemExit(main())
