# -*- coding: utf-8 -*-
r"""_v215_arreglar_parejas.py . LAS CUATRO CIFRAS DE BYTES QUE PUBLIQUE SIN SU
PAREJA, CORREGIDAS POR SUSTITUCION DECLARADA Y MEDIDA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE. La guarda de cerrar_reporte.py que exige las DOS CONVENCIONES
(bytes en disco y bytes normalizado a LF) me cazo CUATRO cifras publicadas con
una sola. Tiene razon: una cifra de bytes sin decir de que convencion es no se
puede cotejar contra el disco. El precedente de como se corrige sin rehacer el
esqueleto es _v214_arreglar_esqueleto.py y la sustitucion declarada de la 214.

QUE NO HACE: NO le da la vuelta a la guarda ni la afloja. Lo que hace es
MEDIR las dos convenciones de cada fichero y escribir LAS DOS.

QUE NO SE INVENTA: la lista de abajo dice, para cada cifra huerfana, DE QUE
FICHERO es, y las dos convenciones se miden de ese fichero con medir_en_disco(),
que es la sede unica de la casa. NINGUNA CIFRA SE TECLEA.

LA GUARDA QUE PUEDE CAER, Y ES LA QUE HACE AUDITABLE ESTO: se cuenta con la
PROPIA funcion de cerrar_reporte.py cuantas cifras huerfanas hay ANTES y
DESPUES, se exige que el DESPUES sea 0, y se mide el numstat para probar que no
cambia ni una linea fuera de las que la lista nombra.

USO:  python scripts/loop/_v215_arreglar_parejas.py [--escribir]
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
from cerrar_reporte import cifras_sin_pareja  # noqa: E402
from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402

# CADA CIFRA HUERFANA, CON EL FICHERO DEL QUE ES. El trozo de texto es el ancla
# EXACTA que hay que encontrar UNA SOLA VEZ en el reporte; si aparece cero veces
# o mas de una, esto cae en rojo y no escribe.
ARREGLOS = [
    ("SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt (912 bytes, sellada por el "
     "propio ciclo)",
     "docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt",
     "912 bytes"),
    ("(`docs/loop/SALIDA_V183_BATERIA.txt`, 93498 bytes, 1433 lineas)",
     "docs/loop/SALIDA_V183_BATERIA.txt",
     "93498 bytes"),
    ("**Sus 34258 bytes de hoy son de esa fecha.**",
     "docs/plan/10_INVENTARIO.md",
     "34258 bytes"),
    ("existe, mide **912 bytes**",
     "docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt",
     "**912 bytes**"),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.stdout.decode("utf-8", errors="replace")


def main():
    escribir = "--escribir" in sys.argv
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)

    antes = cifras_sin_pareja(texto)
    print("EL ANTES, CONTADO CON LA PROPIA FUNCION DE cerrar_reporte.py")
    print("CIFRA cifras publicadas sin su pareja ANTES: %d" % len(antes))
    for n, especie, muestra, linea in antes:
        print("   HUERFANA> linea %d, especie %s, muestra %s: %s"
              % (n, especie, muestra, linea[:100]))
    print("")

    print("LAS DOS CONVENCIONES DE CADA FICHERO, MEDIDAS Y NO TECLEADAS")
    fallos = 0
    nuevo = texto
    tocadas = 0
    for ancla, ruta, viejo in ARREGLOS:
        m = medir_en_disco(RAIZ, ruta)
        if m is None:
            print("ROJO: %s no existe en disco." % ruta)
            return 1
        disco, lf = m
        print("   %s -> %d bytes en disco y %d bytes normalizado a LF (%s)"
              % (ruta, disco, lf, "COINCIDEN" if disco == lf else "NO COINCIDEN"))
        veces = nuevo.count(ancla)
        print("      el ancla aparece %d vez(ces) (se exige 1)" % veces)
        if veces != 1:
            fallos += 1
            continue
        # LA CIFRA QUE HAY ESCRITA TIENE QUE SER LA DEL DISCO, o el remedio
        # estaria tapando ademas una cifra falsa.
        n_escrita = re.search(r"(\d+)", viejo)
        if not n_escrita or int(n_escrita.group(1)) != disco:
            print("      ROJO: la cifra escrita %s no es la del disco %d, y eso "
                  "no es una pareja que falta: es una cifra falsa."
                  % (n_escrita.group(1) if n_escrita else "(ninguna)", disco))
            fallos += 1
            continue
        estrellas = viejo.startswith("**")
        par = ("**%d bytes en disco y %d bytes normalizado a LF**"
               % (disco, lf)) if estrellas else (
            "%d bytes en disco y %d bytes normalizado a LF" % (disco, lf))
        ancla_nueva = ancla.replace(viejo, par)
        nuevo = nuevo.replace(ancla, ancla_nueva)
        tocadas += 1
        print("      SUSTITUIDO: %r -> %r" % (viejo, par))
    print("")
    print("CIFRA anclas sustituidas: %d | CIFRA que deberia haber: %d"
          % (tocadas, len(ARREGLOS)))
    if tocadas != len(ARREGLOS):
        fallos += 1

    despues = cifras_sin_pareja(nuevo)
    print("CIFRA cifras publicadas sin su pareja DESPUES: %d" % len(despues))
    for n, especie, muestra, linea in despues:
        print("   HUERFANA> linea %d, especie %s, muestra %s: %s"
              % (n, especie, muestra, linea[:100]))
    if despues:
        fallos += 1
    print("")

    viejas = texto.split(NL)
    nuevas = nuevo.split(NL)
    print("CIFRA lineas del reporte ANTES: %d | DESPUES: %d (se exige que "
          "calcen)" % (len(viejas), len(nuevas)))
    if len(viejas) != len(nuevas):
        fallos += 1
    distintas = [i + 1 for i, (a, b) in enumerate(zip(viejas, nuevas)) if a != b]
    print("CIFRA lineas que cambian: %d (se exigen %d)"
          % (len(distintas), len(ARREGLOS)))
    for i in distintas:
        print("   CAMBIA> linea %d" % i)
    if len(distintas) != len(ARREGLOS):
        fallos += 1
    print("")
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        print("ROJO: no se escribe nada. docs/loop/REPORTE.md queda intacto.")
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
    ns = [l for l in git(["diff", "--numstat", "--",
                          "docs/loop/REPORTE.md"]).split(NL) if l.strip()]
    print("numstat sobre el reporte: %s" % (ns[0] if ns else "(sin cambios)"))
    return 0 if de_nuevo == nuevo else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
