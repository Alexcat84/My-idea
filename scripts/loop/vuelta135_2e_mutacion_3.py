# -*- coding: utf-8 -*-
"""vuelta135_2e_mutacion_3.py . MUTACION 3 de TAREA 2.e de la vuelta 135,
EL CASO NEGATIVO que importa tanto como los otros dos (encargo): una
cifra con su fichero citado, con su linea `CIFRA` puesta (2.c) y con el
numero CORRECTO tiene que dar VERDE. Una guarda que siempre cae en rojo
no mide mas que una que nunca cae.

Sobre una COPIA del REPORTE REAL de la vuelta 134, las DOS cifras que la
vieja exencion (iii) dejaba pasar sin cotejar (`118 grafias` y
`54 grupos`) DEJAN de marcarse `(sin instrumento)` y pasan a citar
`docs/loop/SALIDA_V135_2E_APOYO.txt` (fichero real, commiteado esta misma
vuelta, con sus dos lineas `CIFRA ...: 118 grafias` y `CIFRA ...: 54
grupos`). La tercera cifra exenta del reporte (`0 pares`) NO se toca: su
ventana amplia no cita ningun SALIDA_V134_*.txt, sigue siendo una
exencion LEGAL bajo la regla nueva de 2.b, y el conjunto entero tiene que
dar VERDE EXIT 0.

Salida: docs/loop/SALIDA_V135_2E_MUTACION_3.txt

USO:
  python scripts/loop/vuelta135_2e_mutacion_3.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE_REAL = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
APOYO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_2E_APOYO.txt")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_2E_MUTACION_3.txt")

CITA = "`SALIDA_V135_2E_APOYO.txt`"
PARES = [
    ("118 grafias (sin instrumento)", "118 grafias (%s)" % CITA),
    ("54 grupos (sin instrumento)", "54 grupos (%s)" % CITA),
    # Neutraliza las citas VIEJAS de 4.a/4.b: sin esto, la ventana forward
    # de "118 grafias" (frases i, i+1, i+2) alcanza igual la cita vieja de
    # 4.b (una frase mas adelante) y `citas[0]` (orden alfabetico) prefiere
    # SALIDA_V134_... sobre SALIDA_V135_..., cotejando contra el fichero
    # equivocado. Se neutralizan las DOS para que la unica cita viva en la
    # ventana de las dos cifras mutadas sea la nueva.
    ("`SALIDA_V134_4A_CENSO_COLA.txt`", "(fichero historico 4A, ya no citado aqui)"),
    ("`SALIDA_V134_4B_EFECTO_CAP.txt`", "(fichero historico 4B, ya no citado aqui)"),
]


def main():
    if not os.path.exists(APOYO):
        print("ROJO PREVIO: no existe %s (tiene que estar commiteado antes de esta prueba)." % APOYO)
        return 1

    with io.open(REPORTE_REAL, encoding="utf-8") as f:
        texto = f.read()

    mutado = texto
    for viejo, nuevo in PARES:
        if texto.count(viejo) != 1:
            print("ROJO PREVIO: '%s' no aparece exactamente una vez en el reporte real." % viejo)
            return 1
        mutado = mutado.replace(viejo, nuevo)

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_134_MUTACION3_")
    os.close(fd)
    with io.open(ruta_tmp, "w", encoding="utf-8") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_tmp],
                            capture_output=True, text=True)
        salida_txt = (
            "MUTACION 3 (CASO NEGATIVO): '118 grafias (sin instrumento)' y "
            "'54 grupos (sin instrumento)' pasan a citar %s, que trae sus dos "
            "lineas CIFRA con el numero CORRECTO, sobre copia de REPORTE.md "
            "(vuelta 134 real).\n"
            "--- salida de verificar_cifras_del_reporte.py ---\n%s\n%s\n"
            "EXITCODE proceso: %d\n" % (CITA, r.stdout, r.stderr, r.returncode)
        )
        verificada = (r.returncode == 0)
        salida_txt += ("MUTACION VERIFICADA: el caso negativo da VERDE, como se esperaba.\n"
                        if verificada else
                        "MUTACION NO VERIFICADA: no dio VERDE como se esperaba.\n")
        salida_txt += "EXITCODE: %d\n" % (0 if verificada else 1)
    finally:
        os.remove(ruta_tmp)

    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(salida_txt)
    print(salida_txt)
    return 0 if verificada else 1


if __name__ == "__main__":
    raise SystemExit(main())
