# -*- coding: utf-8 -*-
r"""vuelta181_correr_bateria.py . CORRE LA BATERIA ENTERA, DE UN SOLO BOCADO Y
SIN `--tramo`, Y SELLA SU SALIDA SIN QUE PUEDA QUEDARSE EN CERO BYTES.

CLON DECLARADO de scripts/loop/vuelta175_correr_bateria.py. Y LA AFIRMACION DE
CLON SE MIDE, NO SE AFIRMA: el cotejo lo hace
scripts/loop/cotejar_clon_declarado.py y su salida se pega en el reporte, que es
obligatorio desde la vuelta 178 por el docstring de aquel fichero. Este texto NO
publica ningun resultado de diff.

Y AQUI LA MAQUINA SI CAMBIA, ASI QUE SE DICE EN VEZ DE PROMETER QUE NO. El
numero de vuelta deja de estar tecleado dentro de dos literales y pasa a ser la
constante `VUELTA`, de la que salen el nombre de la salida y el prefijo del
temporal; se anade una linea que declara en la propia transcripcion que la
corrida va SIN `--tramo`; y la medicion final publica DOS cifras mas, los bytes
normalizados a LF (por la convencion que sigue sin fijar) y el `sha256` entero en
vez de sus dieciseis primeros caracteres. Lo que NO cambia es el ORDEN de los
pasos ni ninguna de las tres precauciones de abajo. La cuenta exacta la da el
instrumento y va pegada en el reporte, no aqui.

POR QUE SIN `--tramo`, Y ES LA LETRA DEL ENCARGO: la 181 corre la nomina ENTERA
de una sola vez. El reparto en tramos de la vuelta 176 sigue existiendo y sigue
siendo legitimo (parte el bocado, no la bateria), pero el encargo de esta vuelta
pide la corrida entera y sin tramos para que EL RELOJ QUE SE PUBLIQUE SEA EL DE
UNA CORRIDA COMPLETA. El grano del tope de 10 minutos se MIDE aqui con ese reloj
y NO SE CAMBIA: es decision del fundador y esta vuelta solo le pone la medida
delante.

LAS TRES PRECAUCIONES QUE ESTE FICHERO HEREDA Y NO AFLOJA:

  1. LANZAMIENTO CON `-u` (sin buffer) y ESCRITURA LINEA A LINEA con `flush()`.
     Un `> fichero` de shell crea el fichero VACIO al lanzar el comando y el
     interprete bufferiza: si la corrida se corta, en disco queda el cero. Asi
     nacieron los ficheros de cero bytes de las vueltas 166, 167, 170, 171, 172 y
     173, que el bloque H.7 de la apertura de esta vuelta vuelve a contar.
  2. EL FICHERO DE TRABAJO VIVE FUERA DE `docs/loop/`, en un temporal del
     sistema, Y SE COPIA DENTRO AL FINAL. NO ES UN CAPRICHO: la bateria mira
     `docs/loop/` entero antes y despues de cada arnes y publica como RUIDO DE
     CONCURRENCIA todo `.txt` que cambie sin ser de nadie. Un fichero de salida
     creciendo dentro de `docs/loop/` durante la corrida saldria como ruido en
     las 108 entradas, y seria ruido fabricado por el propio instrumento que
     mide.
  3. LA SALIDA SE MIDE ANTES DE NOMBRARLA. Si midiera cero bytes, ROJO y la ruta
     NO se publica, porque UNA RUTA QUE PROMETE PRUEBA ES CIFRA (`AUDITOR.md` 4,
     letra del 5 sep 2026) y una ruta a un fichero vacio es CAIDA DE CIFRA.

LO QUE NO HACE: no toca la nomina, no cambia ninguna guarda, no interpreta el
veredicto y no lo reescribe. El exit code de la bateria se PROPAGA tal cual, y
si la bateria sale en rojo este fichero sale en rojo con ella. NADA SE PODA:
si la bateria destapa un arnes roto, se queda en rojo y se nombra.

USO:
  python scripts/loop/vuelta181_correr_bateria.py
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
VUELTA = 181


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

    nombre = "SALIDA_V%d_BATERIA%s.txt" % (VUELTA, ("_" + a.sufijo) if a.sufijo else "")
    destino = os.path.join(LOOP, nombre)

    tmpdir = tempfile.mkdtemp(prefix="v%d_bateria_" % VUELTA)
    trabajo = os.path.join(tmpdir, "bateria_en_curso.txt")

    cmd = [sys.executable, "-u", BATERIA] + (["--mutar-ancla"] if a.mutar else [])
    entorno = dict(os.environ)
    entorno["PYTHONIOENCODING"] = "utf-8"

    inicio_pared = ahora_utc()
    t0 = time.perf_counter()
    print("LANZANDO LA BATERIA. inicio (UTC): %s" % inicio_pared)
    print("   comando: %s" % " ".join(cmd[1:]))
    print("   SIN --tramo: la nomina ENTERA, de un solo bocado.")
    print("   fichero de trabajo, FUERA de docs/loop/: %s" % trabajo)
    print("   destino final: docs/loop/%s" % nombre)
    print("")

    codigo = None
    with io.open(trabajo, "w", encoding="utf-8", newline=NL) as f:
        f.write("CORRIDA DE LA BATERIA DE LA VUELTA %d" % VUELTA + NL)
        f.write("lanzada por scripts/loop/vuelta%d_correr_bateria.py" % VUELTA + NL)
        f.write("SIN --tramo: LA NOMINA ENTERA, DE UN SOLO BOCADO" + NL)
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
        f.write("DURACION MEDIDA POR EL LANZADOR (monotona, minutos): %.1f"
                % (segundos / 60.0) + NL)
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
    print("   CIFRA bytes normalizados a LF: %d"
          % len(datos.replace(b"\r\n", b"\n")))
    print("   CIFRA lineas: %d" % lineas)
    print("   CIFRA sha256 (normalizado a LF): %s" % sha)
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
