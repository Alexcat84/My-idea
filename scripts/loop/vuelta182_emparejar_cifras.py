# -*- coding: utf-8 -*-
r"""vuelta182_emparejar_cifras.py . LAS CIFRAS DE BYTES DEL REPORTE, PUBLICADAS
POR LAS DOS CONVENCIONES, PARA QUE `cifras_sin_pareja()` LAS PUEDA COTEJAR.

POR QUE EXISTE, Y ES UNA GUARDA QUE ME MORDIO A MI. `cerrar_reporte.py` cierra el
reporte y despues corre `cifras_sin_pareja()`, cuya regla esta escrita en su
propio docstring: *"una cifra esta emparejada si en su MISMA LINEA hay dos o mas
apariciones de su especie, o si la linea nombra al menos DOS marcas de
convencion"*. Sobre el reporte de la 182 recien cerrado dio **27**, y el acta 180
punto 6.7 midio **0** sobre el reporte de la 180. **La diferencia es mia**: publique
un solo numero por fichero, el de disco, y la casa publica los dos mientras la
convencion del fundador no este fijada (`P.2`, novena vuelta que sube).

QUE HACE, Y NO TOCA NINGUNA CIFRA: **no cambia ningun numero**. Busca cada cifra
que la guarda senala, **localiza el fichero del que habla** en su misma linea o en
las dos de encima, **lo mide con `os.path.getsize` y con el conteo normalizado a
LF**, y reescribe la frase para que lleve las dos. Si no encuentra el fichero, **NO
inventa una segunda cifra**: deja la linea como esta y la publica en su salida como
no emparejable, que es una medicion y no un fallo tapado.

USO:
  python scripts/loop/vuelta182_emparejar_cifras.py --simular
  python scripts/loop/vuelta182_emparejar_cifras.py
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REPORTE = os.path.join(LOOP, "REPORTE.md")
NL = chr(10)

PAT_RUTA = re.compile(r"`([A-Za-z0-9_./-]+\.(?:txt|json|py|md|jsonl))`")


def medidas(nombre):
    """(disco, lf) de un fichero nombrado en el reporte, o None si no se
    encuentra. Prueba la ruta tal cual desde la raiz y, si es un nombre suelto,
    dentro de docs/loop/."""
    for cand in (os.path.join(RAIZ, nombre.replace("/", os.sep)),
                 os.path.join(LOOP, os.path.basename(nombre))):
        if os.path.isfile(cand):
            t = io.open(cand, encoding="utf-8", errors="replace").read()
            return (os.path.getsize(cand),
                    len(t.replace(chr(13) + NL, NL).encode("utf-8")))
    return None


def con_puntos(n):
    s = str(n)
    fuera = []
    while len(s) > 3:
        fuera.insert(0, s[-3:])
        s = s[:-3]
    return ".".join([s] + fuera)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    antes = CR.cifras_sin_pareja(texto)
    w("VUELTA 182: LAS CIFRAS DE BYTES, EMPAREJADAS POR LAS DOS CONVENCIONES")
    w("   docs/loop/REPORTE.md -> %d bytes | %d lineas"
      % (len(texto.encode("utf-8")), len(lineas)))
    w("   cifras_sin_pareja() ANTES: %d" % len(antes))
    w("")

    arregladas = 0
    sin_fichero = []
    for n, especie, muestra, _l in antes:
        if especie != "bytes":
            sin_fichero.append((n, "no es una cifra de bytes"))
            continue
        idx = n - 1
        rutas = []
        for k in (idx, idx - 1, idx - 2):
            if 0 <= k < len(lineas):
                rutas += PAT_RUTA.findall(lineas[k])
        med = None
        elegida = None
        for r in rutas:
            m = medidas(r)
            if m and con_puntos(m[0]) == muestra:
                med, elegida = m, r
                break
        if med is None:
            sin_fichero.append((n, "no se encontro el fichero de %s bytes en su "
                                   "linea ni en las dos de encima" % muestra))
            continue
        viejo = "%s bytes" % muestra
        nuevo = ("%s bytes en disco y %s normalizados a LF"
                 % (muestra, con_puntos(med[1])))
        if viejo not in lineas[idx]:
            sin_fichero.append((n, "la frase %r ya no esta en su linea" % viejo))
            continue
        lineas[idx] = lineas[idx].replace(viejo, nuevo, 1)
        arregladas += 1
        w("   LINEA %-4d %-52s disco %s | LF %s"
          % (n, elegida, con_puntos(med[0]), con_puntos(med[1])))

    nuevo_texto = NL.join(lineas)
    despues = CR.cifras_sin_pareja(nuevo_texto)
    w("")
    w("   CIFRA lineas emparejadas: %d" % arregladas)
    w("   CIFRA que NO se pudieron emparejar: %d" % len(sin_fichero))
    for n, motivo in sin_fichero:
        w("      LINEA %-4d %s" % (n, motivo))
        w("         | %s" % lineas[n - 1].strip()[:120])
    w("   cifras_sin_pareja() DESPUES: %d" % len(despues))
    for n, _e, muestra, l in despues:
        w("      QUEDA LINEA %-4d %s | %s" % (n, muestra, l[:100]))
    w("")

    if a.simular:
        w("MODO --simular: NO se escribe el reporte.")
    else:
        io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo_texto)
        rele = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("ESCRITO docs/loop/REPORTE.md -> %d bytes | %d lineas"
          % (os.path.getsize(REPORTE), rele.count(NL)))
        w("   RELEIDO: cifras_sin_pareja() = %d" % len(CR.cifras_sin_pareja(rele)))
        w("   guiones largos o medios: %d"
          % (rele.count(chr(8212)) + rele.count(chr(8211))))

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_EMPAREJAR_CIFRAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
