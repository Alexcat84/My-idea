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

--- RE-ANCLAJE, VUELTA 138, TAREA 2.b (ADJUDICADO EN EL ACTA 137, 3.3) ---

CORRECCION DECLARADA, y el texto de arriba se queda entero porque una correccion
que tapa lo que corrige no se puede auditar. Esta mutacion nacio anclada a
docs/loop/REPORTE.md, que SE SOBREESCRIBE CADA VUELTA: desde que el reporte de
la 134 dejo de ser el reporte de hoy, la mutacion cae con "ROJO PREVIO" y no
llega a probar nada. La vuelta 137 la midio y la declaro (mutacion D de
scripts/loop/vuelta137_1c_mutacion.py, "ANCLA PERDIDA"), y el acta 137 adjudico
que SE RE-ANCLAN, no que se declaren superadas: un EXIT 1 que no mide nada no es
una prueba, es un plato vacio (ramal xxi), y toda cifra se lee del instrumento
corrido HOY (EJECUTOR regla 2).

EL SUJETO NUEVO ES PROPIO Y CONGELADO: docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md,
que es el REPORTE.md de la vuelta 134 tal cual, copiado del blob del commit del
acta 134 (e12e4c36). No es una transcripcion ni un resumen: la identidad se
comprueba AQUI, en cada corrida, cotejando el sha256 normalizado del fichero de
hoy contra el sha256 del blob leido de git (EJECUTOR, "LA IDENTIDAD SE LEE DE
GIT"). Si alguien toca el sujeto fijo, esta mutacion cae en ROJO nombrandolo, en
vez de medir otra cosa en silencio. Es la misma figura de la guarda envejecida de
la vuelta 137, banco 9.10, solo que del lado del SUJETO en vez del ARBOL.

--sujeto RUTA apunta la mutacion a otro fichero. Solo lo usa
scripts/loop/verificar_mutaciones_viejas.py --mutar-ancla, que fabrica una copia
con el ancla arrancada para probar que ANCLA PERDIDA cae en ROJO. Con --sujeto la
comprobacion de identidad NO corre, y se dice.

USO:
  python scripts/loop/vuelta135_2e_mutacion_3.py
"""
import argparse
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUJETO_FIJO = os.path.join(RAIZ, "docs", "loop",
                           "SUJETO_FIJO_V135_2E_REPORTE_134.md")
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


BLOB_DEL_SUJETO = "e12e4c362fe734ff2aae0177fa47a3047b485b01:docs/loop/REPORTE.md"


def _normalizar(datos):
    return datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha256_normalizado(datos):
    return hashlib.sha256(_normalizar(datos)).hexdigest()


def identidad_del_sujeto(ruta):
    """El sujeto fijo tiene que ser, byte a byte, el blob del acta 134. Devuelve
    (iguales, sha_del_blob, sha_de_hoy), o (None, motivo, None) si no se pudo
    leer el blob."""
    r = subprocess.run(["git", "show", BLOB_DEL_SUJETO], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None, "no se pudo leer el blob %s de git" % BLOB_DEL_SUJETO, None
    with io.open(ruta, "rb") as f:
        hoy = f.read()
    a = sha256_normalizado(r.stdout)
    b = sha256_normalizado(hoy)
    return a == b, a, b


def sujeto_de_la_linea_de_ordenes():
    """--sujeto RUTA, o el sujeto fijo. Devuelve (ruta, es_el_fijo)."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--sujeto", default=None)
    a, _ = ap.parse_known_args()
    if a.sujeto:
        return a.sujeto, False
    return SUJETO_FIJO, True


def abrir_sujeto():
    """Devuelve (texto, None) o (None, motivo del ROJO PREVIO)."""
    ruta, es_el_fijo = sujeto_de_la_linea_de_ordenes()
    if not os.path.exists(ruta):
        return None, "ROJO PREVIO: no existe el sujeto %s." % ruta
    if es_el_fijo:
        iguales, a, b = identidad_del_sujeto(ruta)
        if iguales is None:
            return None, "ROJO PREVIO: %s" % a
        if not iguales:
            return None, ("ROJO PREVIO: el sujeto fijo %s NO es el blob del acta 134: "
                          "sha256 del blob %s, sha256 de hoy %s." % (ruta, a, b))
        print("SUJETO FIJO VERIFICADO: %s calza con el blob %s (sha256 %s)."
              % (os.path.basename(ruta), BLOB_DEL_SUJETO.split(":")[0][:8], a))
    else:
        print("SUJETO DADO A MANO (--sujeto %s): la comprobacion de identidad NO corre." % ruta)
    with io.open(ruta, encoding="utf-8") as f:
        return f.read(), None


def main():
    if not os.path.exists(APOYO):
        print("ROJO PREVIO: no existe %s (tiene que estar commiteado antes de esta prueba)." % APOYO)
        return 1

    texto, motivo = abrir_sujeto()
    if texto is None:
        print(motivo)
        return 1

    mutado = texto
    for viejo, nuevo in PARES:
        if texto.count(viejo) != 1:
            print("ROJO PREVIO: '%s' no aparece exactamente una vez en el reporte real." % viejo)
            return 1
        mutado = mutado.replace(viejo, nuevo)

    # EL TEMPORAL TIENE NOMBRE FIJO (TAREA 2.f de la vuelta 141, acta de la
    # vuelta 140, caida 4.2 del ejecutor).
    #
    # POR QUE CAMBIA. Aqui habia tempfile.mkstemp(prefix="REPORTE_134_MUTACION3_"),
    # que produce un sufijo ALEATORIO. La guarda que se corre abajo IMPRIME el
    # nombre del fichero que cuenta ("80 lineas == 80 contados en `wc -l
    # REPORTE_134_MUTACION3_xffen9vd.md`"), asi que ese nombre aleatorio entraba
    # en docs/loop/SALIDA_V135_2E_MUTACION_3.txt, que es una SALIDA SELLADA. El
    # fichero cambiaba SOLO en cada corrida sin que nadie tocara nada: el auditor
    # lo confirmo al correr la bateria de la vuelta 140 y verlo mutar de
    # _xffen9vd a _xv7o8hyj.
    #
    # EL ARREGLO: el nombre del fichero pasa a ser FIJO y la aleatoriedad se
    # mueve al DIRECTORIO temporal, que la guarda no imprime. La salida sellada
    # queda byte a byte identica entre corridas. P.16, QUIEN FABRICA LIMPIA: el
    # directorio se retira entero en el finally.
    dir_tmp = tempfile.mkdtemp(prefix="v135_2e_mut3_")
    ruta_tmp = os.path.join(dir_tmp, "REPORTE_134_MUTACION3.md")
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
        shutil.rmtree(dir_tmp, ignore_errors=True)

    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(salida_txt)
    print(salida_txt)
    return 0 if verificada else 1


if __name__ == "__main__":
    raise SystemExit(main())
