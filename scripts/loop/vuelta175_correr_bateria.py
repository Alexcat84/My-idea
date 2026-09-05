# -*- coding: utf-8 -*-
r"""vuelta175_correr_bateria.py . CORRE LA BATERIA ENTERA Y SELLA SU SALIDA SIN
QUE PUEDA QUEDARSE EN CERO BYTES.

POR QUE NACE, Y LA CAUSA ESTA MEDIDA Y NO SUPUESTA. El bloque H.7 de
`docs/loop/SALIDA_V175_APERTURA.txt`, corrido antes de la primera operacion de
esta vuelta, cuenta 51 ficheros de bateria en `docs/loop/` y NUEVE DE ELLOS CON
CERO BYTES, entre ellos `SALIDA_V171_BATERIA.txt`, `SALIDA_V172_BATERIA.txt`,
`SALIDA_V173_BATERIA.txt` y las dos del auditor de la 172 y la 173. La regla del
5 sep 2026 dice que UNA RUTA QUE PROMETE PRUEBA ES CIFRA y que un fichero de
cero bytes es CAIDA DE CIFRA, asi que esas rutas, publicadas como prueba, eran
cifras caidas.

LA CAUSA MECANICA DEL CERO, dicha entera: un `> fichero` de shell crea el
fichero VACIO en el instante en que se lanza el comando, y el interprete de
Python bufferiza su salida. Si la corrida se corta (y esta bateria tarda mas de
media hora), lo que queda en disco es el fichero de cero bytes que el shell creo
al principio. El cero no es que la bateria no dijera nada: es que nunca llego a
vaciarse su buffer.

QUE HACE ESTE FICHERO, Y ES LO UNICO QUE HACE:

  1. Lanza `scripts/loop/verificar_mutaciones_viejas.py` con `-u` (sin buffer) y
     va ESCRIBIENDO CADA LINEA AL VUELO en un fichero de trabajo, con `flush()`
     linea a linea. Si esto se corta a la mitad, en disco queda la mitad, que es
     lo que la casa pide: una vuelta cortada deja parcial, nunca vacio.
  2. EL FICHERO DE TRABAJO VIVE FUERA DE `docs/loop/`, en un temporal del
     sistema. NO ES UN CAPRICHO: la bateria mira `docs/loop/` entero antes y
     despues de cada arnes y publica como RUIDO DE CONCURRENCIA todo `.txt` que
     cambie sin ser de nadie. Un fichero de salida creciendo dentro de
     `docs/loop/` durante la corrida saldria como ruido en las 87 entradas, y
     seria ruido fabricado por el propio instrumento que mide.
  3. Al terminar, copia el fichero de trabajo a `docs/loop/SALIDA_V175_BATERIA.txt`
     y LO MIDE: bytes, lineas y sha256. **NO NOMBRA LA RUTA COMO PRUEBA SI MIDE
     CERO BYTES**: en ese caso sale en ROJO diciendo que la ruta no se puede
     publicar, que es exactamente lo que la regla de la casa manda.
  4. Publica el reloj de pared por los dos extremos (inicio y fin en UTC) al
     lado del cronometro monotono que la propia bateria ya imprime. Los dos, no
     uno: el monotono es el que mide, y el de pared es el que deja constancia de
     que la corrida ocurrio hoy.

LO QUE NO HACE: no toca la nomina, no cambia ninguna guarda, no interpreta el
veredicto y no lo reescribe. El exit code de la bateria se PROPAGA tal cual, y
si la bateria sale en rojo este fichero sale en rojo con ella.

USO:
  python scripts/loop/vuelta175_correr_bateria.py
  python scripts/loop/vuelta175_correr_bateria.py --sufijo SEGUNDA
"""
import argparse
import datetime
import hashlib
import io
import os
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
BATERIA = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
NL = chr(10)


def ahora_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sufijo", default="",
                    help="sufijo del nombre de la salida, para una segunda corrida")
    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true",
                    help="pasa --mutar-ancla a la bateria (la prueba del ancla)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    nombre = "SALIDA_V175_BATERIA%s.txt" % (("_" + a.sufijo) if a.sufijo else "")
    destino = os.path.join(LOOP, nombre)

    tmpdir = tempfile.mkdtemp(prefix="v175_bateria_")
    trabajo = os.path.join(tmpdir, "bateria_en_curso.txt")

    cmd = [sys.executable, "-u", BATERIA] + (["--mutar-ancla"] if a.mutar else [])
    entorno = dict(os.environ)
    entorno["PYTHONIOENCODING"] = "utf-8"

    inicio_pared = ahora_utc()
    t0 = time.perf_counter()
    print("LANZANDO LA BATERIA. inicio (UTC): %s" % inicio_pared)
    print("   comando: %s" % " ".join(cmd[1:]))
    print("   fichero de trabajo, FUERA de docs/loop/: %s" % trabajo)
    print("   destino final: docs/loop/%s" % nombre)
    print("")

    codigo = None
    with io.open(trabajo, "w", encoding="utf-8", newline=NL) as f:
        f.write("CORRIDA DE LA BATERIA DE LA VUELTA 175" + NL)
        f.write("lanzada por scripts/loop/vuelta175_correr_bateria.py" + NL)
        f.write("INICIO (reloj de pared, UTC): %s" % inicio_pared + NL)
        f.write(("=" * 78) + NL)
        f.flush()
        p = subprocess.Popen(cmd, cwd=RAIZ, env=entorno, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for linea in io.TextIOWrapper(p.stdout, encoding="utf-8", errors="replace"):
            f.write(linea.replace(chr(13) + NL, NL).rstrip(chr(13) + NL) + NL)
            f.flush()
        codigo = p.wait()
        fin_pared = ahora_utc()
        segundos = time.perf_counter() - t0
        f.write(("=" * 78) + NL)
        f.write("EXITCODE DE LA BATERIA: %d" % codigo + NL)
        f.write("FIN (reloj de pared, UTC): %s" % fin_pared + NL)
        f.write("DURACION MEDIDA POR EL LANZADOR (monotona, segundos): %.1f" % segundos + NL)
        f.write("DURACION MEDIDA POR EL LANZADOR (monotona, minutos): %.1f" % (segundos / 60.0) + NL)
        f.flush()

    datos = io.open(trabajo, "rb").read()
    io.open(destino, "wb").write(datos)

    bytes_disco = os.path.getsize(destino)
    texto = datos.decode("utf-8", errors="replace")
    lineas = texto.count(NL)
    sha = hashlib.sha256(datos.replace(b"\r\n", b"\n")).hexdigest()

    print("")
    print("LA SALIDA, MEDIDA ANTES DE NOMBRARLA EN NINGUN SITIO")
    print("   (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA)")
    print("   docs/loop/%s" % nombre)
    print("   CIFRA bytes en disco: %d" % bytes_disco)
    print("   CIFRA lineas: %d" % lineas)
    print("   CIFRA sha256 (normalizado a LF): %s" % sha[:16])
    print("   CIFRA exitcode de la bateria: %d" % codigo)
    print("   CIFRA duracion en minutos (monotona): %.1f" % (segundos / 60.0))
    print("   inicio (UTC): %s | fin (UTC): %s" % (inicio_pared, fin_pared))

    if bytes_disco == 0:
        print("")
        print("ROJO: la salida mide CERO BYTES. Esa ruta NO SE PUEDE PUBLICAR como")
        print("      prueba de nada, y por eso este lanzador no la da por buena.")
        return 1

    print("")
    print("LA RUTA SE PUEDE NOMBRAR: existe y mide %d bytes." % bytes_disco)
    print("EL VEREDICTO DE LA BATERIA SE PROPAGA TAL CUAL, exitcode %d." % codigo)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
