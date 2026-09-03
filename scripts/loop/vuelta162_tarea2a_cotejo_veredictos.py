# -*- coding: utf-8 -*-
r"""vuelta162_tarea2a_cotejo_veredictos.py . TAREA 2.a de la vuelta 162.

LA PRUEBA DE QUE NINGUN VEREDICTO VIEJO SE MUEVE, Y NO ES ALEGATO: coteja
MECANICAMENTE, vuelta por vuelta, la salida de la guarda VIEJA
(`scripts/loop/_v162_apertura_vieja_copia.py`, copia byte a byte hecha ANTES de
tocar nada) contra la de la guarda NUEVA, sobre las vueltas que el encargo
nombra mas las dos que la adjudicacion 6.5 tiene que mover.

QUE COTEJA, Y POR QUE ASI. No compara las salidas enteras: la guarda nueva
IMPRIME MAS (la firma de la parada, el portador del encargo), y eso es lo que se
le pidio. Compara LO QUE ES EL VEREDICTO:
  - la palabra VERDE o ROJO,
  - el codigo de salida,
  - y el conjunto de lineas de FALLO, entero y literal.
Si esas tres cosas calzan, el veredicto no se movio, por mucho que la cabecera
diga mas cosas.

USO:
  python scripts/loop/vuelta162_tarea2a_cotejo_veredictos.py \
      docs/loop/SALIDA_V162_T2A_VIEJA.txt docs/loop/SALIDA_V162_T2A_NUEVA.txt \
      --debe-moverse 161

`--debe-moverse` es la lista de vueltas que la adjudicacion SI cambia. Sale ROJO
en los dos sentidos: si una vuelta que no esta en la lista se mueve, Y si una
vuelta que esta en la lista NO se mueve (una adjudicacion que no muerde tampoco
sirve).
"""
import argparse
import io
import re

CABECERA = re.compile(r"^#{10} VUELTA (\d+) #{10}$")


def bloques(ruta):
    """Parte el fichero en bloques por vuelta. Devuelve {vuelta: [lineas]}."""
    d, actual = {}, None
    for linea in io.open(ruta, encoding="utf-8", errors="replace").read().splitlines():
        m = CABECERA.match(linea.strip())
        if m:
            actual = int(m.group(1))
            d[actual] = []
        elif actual is not None:
            d[actual].append(linea)
    return d


def veredicto(lineas):
    """(palabra, exitcode, fallos). `fallos` son las lineas indentadas que
    siguen a la cabecera ROJA, literales y en orden."""
    palabra, codigo, fallos, dentro = None, None, [], False
    for linea in lineas:
        if linea.startswith("VERDE"):
            palabra, dentro = "VERDE", False
        elif linea.startswith("ROJO"):
            palabra, dentro = "ROJO", True
        elif linea.startswith("EXITCODE:"):
            codigo = linea.split(":", 1)[1].strip()
            dentro = False
        elif dentro and linea.startswith("   "):
            fallos.append(linea.strip())
    return palabra, codigo, fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vieja")
    ap.add_argument("nueva")
    ap.add_argument("--debe-moverse", type=int, nargs="*", default=[])
    a = ap.parse_args()

    v, n = bloques(a.vieja), bloques(a.nueva)
    if sorted(v) != sorted(n):
        print("ROJO: las dos corridas no cubren las mismas vueltas: %s contra %s"
              % (sorted(v), sorted(n)))
        return 1

    movidas, quietas, rotos = [], [], []
    print("COTEJO DE VEREDICTOS, guarda VIEJA contra guarda NUEVA")
    print("  vieja: %s" % a.vieja)
    print("  nueva: %s" % a.nueva)
    print("")
    for vuelta in sorted(v):
        pv, cv, fv = veredicto(v[vuelta])
        pn, cn, fn = veredicto(n[vuelta])
        igual = (pv, cv, fv) == (pn, cn, fn)
        (quietas if igual else movidas).append(vuelta)
        print("  VUELTA %d: vieja %s exit %s con %d fallo(s) | nueva %s exit %s con %d "
              "fallo(s) | %s" % (vuelta, pv, cv, len(fv), pn, cn, len(fn),
                                 "IDENTICO" if igual else "MOVIDO"))
        if not igual:
            for x in fv:
                if x not in fn:
                    print("      solo en la VIEJA: %s" % x)
            for x in fn:
                if x not in fv:
                    print("      solo en la NUEVA: %s" % x)

    esperadas = set(a.debe_moverse)
    print("")
    print("  quietas: %s" % (quietas or "ninguna"))
    print("  movidas: %s" % (movidas or "ninguna"))
    print("  se esperaba que se movieran: %s" % (sorted(esperadas) or "ninguna"))

    de_mas = sorted(set(movidas) - esperadas)
    de_menos = sorted(esperadas - set(movidas))
    if de_mas:
        rotos.append("SE MOVIERON VEREDICTOS QUE NO DEBIAN: %s" % de_mas)
    if de_menos:
        rotos.append("NO SE MOVIERON VEREDICTOS QUE SI DEBIAN (una adjudicacion que no "
                     "muerde tampoco sirve): %s" % de_menos)
    print("")
    if rotos:
        print("ROJO:")
        for x in rotos:
            print("   %s" % x)
        return 1
    print("VERDE: ningun veredicto viejo se movio, y el unico que se mueve es el que la "
          "adjudicacion 6.5 del acta 161 manda mover.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
