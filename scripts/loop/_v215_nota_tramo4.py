# -*- coding: utf-8 -*-
r"""_v215_nota_tramo4.py . LA NOTA DEL TRAMO 4, INSERTADA POR SUSTITUCION
DECLARADA EN LA SECCION 8 DEL REPORTE YA CERRADO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE, Y LO DIGO ANTES DE QUE LO MIDA NADIE. La salida sellada de
cerrar_reporte.py publica, en su bloque B, esta linea:

    tramo 4   -> vuelta None

y esta otra:

    CIFRA tramos sellados EN LA VUELTA 215: 10 [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

DIEZ DE ONCE, Y EL QUE FALTA ES MIO. El lector de cerrar_reporte.py atribuye un
tramo a su vuelta leyendo EL ASUNTO de su ultimo commit, o sea su PRIMERA LINEA.
El commit del tramo 4 NO empieza por "VUELTA 215, BATERIA TRAMO 4": empieza por
mi correccion declarada del mensaje del tramo 3, que meti delante. El fichero
del tramo 4 SI cambio en un commit de la 215; lo que no calza es donde mira el
lector.

NO SE ARREGLA EL LECTOR (moratoria, y ademas el lector no esta roto: mide lo que
dice medir). SE DECLARA EN EL REPORTE, que es mi sede.

LA GUARDA: el ancla tiene que aparecer EXACTAMENTE UNA VEZ, la insercion no
puede borrar ninguna linea, y las secciones del reporte tienen que seguir siendo
las mismas antes y despues.

USO:  python scripts/loop/_v215_nota_tramo4.py [--escribir]
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

sys.path.insert(0, AQUI)
from cerrar_reporte import cifras_sin_pareja, secciones_del_reporte  # noqa: E402

ANCLA = """**Y UNA TERCERA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE"""

NOTA = """- **`C.2` MI PROPIA CORRECCION DECLARADA LE TAPO EL ASUNTO AL COMMIT DEL TRAMO
  4, Y LO DIGO ANTES DE QUE LO MIDA NADIE.** La salida sellada de
  `scripts/loop/cerrar_reporte.py` publica *"tramo 4 a vuelta None"* y
  *"CIFRA tramos sellados EN LA VUELTA 215: 10"*, **diez de once**. **El que
  falta es el 4 y la causa es mia:** ese lector atribuye cada tramo a su vuelta
  leyendo **el asunto de su ultimo commit**, o sea su primera linea, y el commit
  del tramo 4 **no empieza por el titulo del tramo**: empieza por la correccion
  declarada del mensaje del tramo 3, que meti delante. **El fichero del tramo 4
  SI cambio en un commit de la 215**, y su medicion esta sellada como los otros
  diez. **NO TOCO EL LECTOR:** rige la moratoria y ademas **no esta roto, mide lo
  que dice medir**. **La rama de la seccion 9 sale CORRIDA igual**, porque le
  basta con que al menos un tramo se sellara en esta vuelta, y se sellaron diez.

"""


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")


def main():
    escribir = "--escribir" in sys.argv
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)

    fallos = 0
    veces = texto.count(ANCLA)
    print("CIFRA veces que aparece el ancla: %d (se exige 1)" % veces)
    if veces != 1:
        print("ROJO: el ancla no es unica. No se escribe nada.")
        return 1

    nuevo = texto.replace(ANCLA, NOTA + ANCLA)

    viejas, nuevas = texto.split(NL), nuevo.split(NL)
    print("CIFRA lineas ANTES: %d | DESPUES: %d" % (len(viejas), len(nuevas)))
    anadidas = len(nuevas) - len(viejas)
    print("CIFRA lineas anadidas: %d | CIFRA lineas BORRADAS: %d (se exigen 0)"
          % (anadidas, max(0, len(viejas) - len(nuevas))))
    if len(nuevas) < len(viejas):
        fallos += 1
    desaparecidas = [l for l in viejas if l.strip() and l not in nuevas]
    print("CIFRA lineas viejas que DESAPARECEN del fichero: %d (se exigen 0)"
          % len(desaparecidas))
    if desaparecidas:
        fallos += 1

    sec_antes = secciones_del_reporte(texto)
    sec_despues = secciones_del_reporte(nuevo)
    print("CIFRA secciones ANTES: %d | DESPUES: %d (se exige que calcen)"
          % (len(sec_antes), len(sec_despues)))
    if sorted(sec_antes) != sorted(sec_despues):
        fallos += 1
    dup = [k for k, v in sec_despues.items() if len(v) > 1]
    print("CIFRA secciones DUPLICADAS despues: %d %s (se exigen 0)"
          % (len(dup), dup))
    if dup:
        fallos += 1

    huerfanas = cifras_sin_pareja(nuevo)
    print("CIFRA cifras sin su pareja DESPUES: %d (se exigen 0)" % len(huerfanas))
    if huerfanas:
        fallos += 1
    print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
          % (nuevo.count(chr(8212)), nuevo.count(chr(8211))))
    if nuevo.count(chr(8212)) or nuevo.count(chr(8211)):
        fallos += 1

    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe nada.")
        return 1
    if not escribir:
        print("VERDE EN SIMULACION. No se ha escrito nada: falta --escribir.")
        return 0
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
    de_nuevo = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    print("ESCRITO docs/loop/REPORTE.md -> %d bytes"
          % len(nuevo.encode("utf-8")))
    print("RELECTURA DEL DISCO: identico a lo juzgado: %s"
          % ("SI" if de_nuevo == nuevo else "NO"))
    return 0 if de_nuevo == nuevo else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
