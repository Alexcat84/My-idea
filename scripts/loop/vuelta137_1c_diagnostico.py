# -*- coding: utf-8 -*-
"""vuelta137_1c_diagnostico.py . TAREA 1.c de la vuelta 137: REPRODUCE, con
ficheros de salida REALES ya commiteados, los DOS defectos de
verificar_cifras_del_reporte.py que el acta 136 nombra (parada del 29 ago 2026,
punto 4). Se corre ANTES de la reparacion para medirlos, y DESPUES para
comprobar que se cerraron.

EJECUTOR regla 2, EL INSTRUMENTO MANDA: los dos casos no se describen de
palabra, se corren.

DEFECTO 1, NO SABE CONTAR LA UNIDAD `grafia`.
  docs/loop/SALIDA_V135_4B_PELDANOS.txt trae DOS lineas CIFRA de unidad
  `grafias`: "grafias en grupo: 92" y "grafias sin agrupar: 37".
  contar_por_cifra_etiquetada() devuelve la PRIMERA que encuentra, o sea 92
  SIEMPRE. Una cifra CORRECTA escrita con el vocabulario de la casa ("37
  grafias sin agrupar") cae en ROJO contra su propio fichero.
  La prueba de que el defecto ya deformaba el trabajo esta en la cabecera de
  ese mismo fichero de salida, que explica que el peldano 6 se pone PRIMERO
  "porque el cotejo toma la PRIMERA linea CIFRA de la unidad pedida": un
  instrumento doblado alrededor del defecto de la guarda.

DEFECTO 2, EMPAREJA LA CIFRA CON EL FICHERO ALFABETICAMENTE PRIMERO.
  La linea 388 hacia `sorted(set(...))` y la 395 tomaba `citas[0]`, o sea el
  primero por ORDEN ALFABETICO de la ventana y no el que corresponde a esa
  cifra. Con una cifra que cita su fichero y una frase vecina que cita otro
  alfabeticamente anterior, la guarda coteja contra EL DEL VECINO.

Salida: docs/loop/SALIDA_V137_1C_DIAGNOSTICO.txt

USO:
  python scripts/loop/vuelta137_1c_diagnostico.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
SALIDA = os.path.join(LOOP, "SALIDA_V137_1C_DIAGNOSTICO.txt")

# Ficheros REALES, ya commiteados. El primero trae DOS lineas CIFRA de unidad
# `grafias` (92 en grupo, 37 sin agrupar) y el segundo es alfabeticamente
# ANTERIOR, que es lo que hace visible el defecto 2.
FICHERO_PROPIO = "SALIDA_V135_4B_PELDANOS.txt"
FICHERO_VECINO = "SALIDA_V133_2E_MUTACION.txt"

CASO_1 = """# Reporte de prueba, caso del defecto 1

La tabla de peldanos (`%s`) deja 37 grafias sin agrupar al cerrar la
cadena de seis reglas.
""" % FICHERO_PROPIO

CASO_2 = """# Reporte de prueba, caso del defecto 2

La tabla de peldanos (`%s`) deja 92 grafias en grupo.
La mutacion de la vuelta 133 (`%s`) quedo verificada aparte.
""" % (FICHERO_PROPIO, FICHERO_VECINO)


def correr_guarda(texto, lineas, titulo, espera):
    fd, tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_V137_1C_")
    os.close(fd)
    try:
        with io.open(tmp, "w", encoding="utf-8") as f:
            f.write(texto)
        r = subprocess.run([sys.executable, GUARDA, "--reporte", tmp],
                           capture_output=True, text=True, cwd=RAIZ)
    finally:
        os.remove(tmp)
    lineas.append("=== %s" % titulo)
    lineas.append("cifra escrita y CORRECTA segun su propio fichero: %s" % espera)
    lineas.append("--- salida de verificar_cifras_del_reporte.py ---")
    lineas.append(r.stdout.rstrip())
    if r.stderr.strip():
        lineas.append(r.stderr.rstrip())
    lineas.append("EXITCODE proceso: %d" % r.returncode)
    lineas.append("")
    return r.returncode, r.stdout


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lineas = ["DIAGNOSTICO 1.c (vuelta 137): los dos defectos de "
              "verificar_cifras_del_reporte.py, con ficheros REALES", ""]

    # Se deja constancia de lo que los ficheros reales dicen, contado ahora.
    for nombre in (FICHERO_PROPIO, FICHERO_VECINO):
        with io.open(os.path.join(LOOP, nombre), encoding="utf-8") as f:
            cifras = [l.strip() for l in f if l.startswith("CIFRA")]
        lineas.append("lineas CIFRA de `%s`:" % nombre)
        for c in cifras:
            lineas.append("  %s" % c)
        if not cifras:
            lineas.append("  (ninguna)")
    lineas.append("")

    rc1, out1 = correr_guarda(
        CASO_1, lineas,
        "DEFECTO 1, la unidad `grafia`: el fichero trae DOS lineas CIFRA de "
        "esa unidad y la guarda toma la PRIMERA.",
        "37 grafias sin agrupar, que es literalmente la linea "
        "'CIFRA grafias sin agrupar: 37 grafias' de %s" % FICHERO_PROPIO)

    rc2, out2 = correr_guarda(
        CASO_2, lineas,
        "DEFECTO 2, el emparejamiento: la cifra cita SU fichero y la frase "
        "siguiente cita otro alfabeticamente ANTERIOR.",
        "92 grafias en grupo, que es literalmente la linea "
        "'CIFRA grafias en grupo: 92 grafias' de %s" % FICHERO_PROPIO)

    lineas.append("RESUMEN: defecto 1 %s / defecto 2 %s" % (
        "REPRODUCIDO (ROJO sobre cifra correcta)" if rc1 == 1 else "NO reproducido (EXIT %d)" % rc1,
        "REPRODUCIDO (ROJO sobre cifra correcta)" if rc2 == 1 else "NO reproducido (EXIT %d)" % rc2))
    lineas.append("EXITCODE: %d" % (0 if (rc1 == 1 and rc2 == 1) else 1))

    texto = "\n".join(lineas) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)
    return 0 if (rc1 == 1 and rc2 == 1) else 1


if __name__ == "__main__":
    raise SystemExit(main())
