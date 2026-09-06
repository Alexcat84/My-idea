# -*- coding: utf-8 -*-
r"""vuelta192_racha_de_cierres.py . LA RACHA DE VUELTAS QUE CIERRAN SU PROPIO
REPORTE, CONTADA DEL INVENTARIO ENTERO Y NO DE UNA VENTANA ELEGIDA A MANO.

POR QUE EXISTE, Y ES UNA CAIDA MIA CAZADA ANTES DE PUBLICAR. El bloque `B.2` del
sello de apertura de esta vuelta miro una VENTANA TECLEADA (185 a 191) y publico
"racha 7". Esa cifra no es de la racha: es del borde inferior de mi ventana. El
inventario de disco tiene ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt` mas atras, y
una racha que se corta justo donde acaba la ventana que uno eligio NO ES UNA
MEDICION DE LA RACHA. Este fichero la mide del inventario ENTERO: descubre los
numeros de vuelta del propio directorio, no de una lista.

QUE CUENTA, ESCRITO ANTES DE CONTAR:
  . UN FICHERO ENTRA en el inventario si su nombre casa
    `SALIDA_V<n>_CERRAR_REPORTE.txt`. El numero sale del nombre.
  . UN FICHERO ESTA EN VERDE si trae una linea `CIFRA piezas que faltan: 0`.
  . LA RACHA es la cuenta de vueltas CONSECUTIVAS en verde hacia atras desde la
    mas alta del inventario. Un numero que falta CORTA la racha, y se nombra.

LO QUE ESTA MEDICION NO PUEDE HACER, DICHO ANTES DE SU CIFRA: no prueba que la
vuelta corriera `cerrar_reporte.py`, solo que su fichero de salida existe y dice
que no le falta ninguna pieza. Para eso el bloque `B.2` mira ademas `git log`, y
las dos cifras se publican por separado.

USO:
  python scripts/loop/vuelta192_racha_de_cierres.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V192_RACHA_DE_CIERRES.txt")
PAT = re.compile(r"^SALIDA_V(\d+)_CERRAR_REPORTE\.txt$")
AGUJA = "CIFRA piezas que faltan"


def inventario(directorio=None):
    """{vuelta: (nombre, bytes_disco, en_verde, linea)}. Semi-pura: lo unico que
    toca disco es leer el directorio y los ficheros, y `directorio` va por
    parametro para que el caso positivo por mutacion la apunte a uno fabricado."""
    base = directorio or LOOP
    salida = {}
    for nombre in sorted(os.listdir(base)):
        m = PAT.match(nombre)
        if not m:
            continue
        ruta = os.path.join(base, nombre)
        t = io.open(ruta, encoding="utf-8", errors="replace").read().replace(
            chr(13) + NL, NL)
        lineas = [l.strip() for l in t.split(NL) if AGUJA in l]
        verde = bool(lineas) and lineas[0].endswith("0")
        salida[int(m.group(1))] = (nombre, os.path.getsize(ruta), verde,
                                   lineas[0] if lineas else "(sin la linea)")
    return salida


def racha(inv):
    """(tope, cuenta, corte). PURA sobre el diccionario del inventario.

    `tope` es la vuelta mas alta; `cuenta` las consecutivas en verde hacia atras;
    `corte` la primera vuelta que rompe la racha y por que."""
    if not inv:
        return None, 0, "el inventario esta vacio"
    tope = max(inv)
    n = 0
    v = tope
    while True:
        if v not in inv:
            return tope, n, "la vuelta %d no tiene fichero de cierre" % v
        if not inv[v][2]:
            return tope, n, "la vuelta %d tiene fichero pero no esta en verde" % v
        n += 1
        v -= 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 192: LA RACHA DE CIERRES, CONTADA DEL INVENTARIO ENTERO")
    w("=" * 78)
    w("")
    w("LA REGLA, ESCRITA ANTES DE CONTAR:")
    w("   ENTRA: todo fichero de docs/loop/ que case %r" % PAT.pattern)
    w("   VERDE: el que trae una linea %r terminada en 0" % AGUJA)
    w("   RACHA: consecutivas en verde hacia atras desde la mas alta. Un numero")
    w("          que falta CORTA la racha y se nombra.")
    w("")
    inv = inventario()
    w("A) EL INVENTARIO ENTERO, VUELTA A VUELTA")
    w("   CIFRA ficheros de cierre en disco: %d" % len(inv))
    for v in sorted(inv):
        nombre, bs, verde, linea = inv[v]
        w("   %-40s %6d bytes | %-5s | %s"
          % (nombre, bs, "VERDE" if verde else "ROJO", linea))
    w("   CIFRA en VERDE: %d" % len([1 for v in inv if inv[v][2]]))
    w("")
    w("B) LOS HUECOS DEL INVENTARIO, NOMBRADOS")
    faltan = [v for v in range(min(inv), max(inv) + 1) if v not in inv]
    w("   rango mirado: %d a %d" % (min(inv), max(inv)))
    w("   CIFRA vueltas del rango SIN fichero de cierre: %d (%s)"
      % (len(faltan), ", ".join(str(x) for x in faltan) or "ninguna"))
    w("")
    w("C) LA RACHA")
    tope, n, corte = racha(inv)
    w("   tope del inventario: %s" % tope)
    w("   CIFRA vueltas CONSECUTIVAS en verde hacia atras: %d" % n)
    w("   las vueltas de la racha: %s"
      % ", ".join(str(x) for x in range(tope - n + 1, tope + 1)))
    w("   que la corta: %s" % corte)
    w("")
    w("D) LAS TRES CIFRAS QUE ANDAN DANDO VUELTAS, PUBLICADAS JUNTAS")
    w("   el acta 191 venia contando CINCO (187 a 191)")
    w("   el encargo de la 192 dice SEIS (186 a 191) y manda contarlo del")
    w("   instrumento en vez de heredarlo")
    w("   el bloque B.2 de mi sello de apertura, sobre una VENTANA TECLEADA de")
    w("   185 a 191, dice 7, que es el borde de MI ventana y no la racha")
    w("   ESTE INSTRUMENTO, sobre el inventario ENTERO, dice %d" % n)
    w("   LAS CUATRO SE PUBLICAN Y NINGUNA SE RESUELVE COPIANDO.")
    w("")
    w("FIN")
    texto = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V192_RACHA_DE_CIERRES.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
