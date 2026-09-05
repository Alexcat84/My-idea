# -*- coding: utf-8 -*-
"""vuelta135_2e_mutacion_2.py . MUTACION 2 de TAREA 2.e de la vuelta 135
(acta 134, 4.1): sobre una COPIA del REPORTE REAL de la vuelta 134,
`54 grupos` pasa a `77 grupos`, dejando el literal `(sin instrumento)` y la
cita de `SALIDA_V134_4B_EFECTO_CAP.txt` donde estan (mutacion (B) del
auditor, que hoy pasa VERDE con la exencion vieja). Con la regla nueva de
2.b tiene que caer ROJO EXIT 1.

Salida: docs/loop/SALIDA_V135_2E_MUTACION_2.txt

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
  python scripts/loop/vuelta135_2e_mutacion_2.py
SUJETO CONGELADO (declarado en la vuelta 180, TAREA 2.a): este arnes lee `REPORTE.md` de un BLOB DE GIT CLAVADO por su sha, no del fichero vivo (1 lectura(s) de blob clavado y 0 del fichero vivo, medidas fila a fila en docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl), asi que su resultado no depende de lo que ese fichero diga hoy.
"""
import argparse
import hashlib
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUJETO_FIJO = os.path.join(RAIZ, "docs", "loop",
                           "SUJETO_FIJO_V135_2E_REPORTE_134.md")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V135_2E_MUTACION_2.txt")

VIEJO = "54 grupos (sin instrumento)"
NUEVO = "77 grupos (sin instrumento)"


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
    texto, motivo = abrir_sujeto()
    if texto is None:
        print(motivo)
        return 1
    if texto.count(VIEJO) != 1:
        print("ROJO PREVIO: '%s' no aparece exactamente una vez en el reporte real." % VIEJO)
        return 1
    mutado = texto.replace(VIEJO, NUEVO)

    fd, ruta_tmp = tempfile.mkstemp(suffix=".md", prefix="REPORTE_134_MUTACION2_")
    os.close(fd)
    with io.open(ruta_tmp, "w", encoding="utf-8") as f:
        f.write(mutado)

    try:
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta_tmp],
                            capture_output=True, text=True)
        salida_txt = (
            "MUTACION 2: '%s' -> '%s' sobre copia de REPORTE.md (vuelta 134 real).\n"
            "--- salida de verificar_cifras_del_reporte.py ---\n%s\n%s\n"
            "EXITCODE proceso: %d\n" % (VIEJO, NUEVO, r.stdout, r.stderr, r.returncode)
        )
        verificada = (r.returncode == 1 and "77 grupos" in r.stdout)
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
