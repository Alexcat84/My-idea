# -*- coding: utf-8 -*-
"""vuelta134_efecto_cap_abreviado.py . TAREA 4.b de la vuelta 134.

Repite la MISMA cadena de cuatro reglas de la 133
(vuelta133_tabla_mapeo_propuesto.py: cadena entera, titulo, localizador,
prefijo sobre recortada), pero con la cola de localizador EXTENDIDA a
`Caps?.` con punto (ademas de capitulo/seccion/anexo/apendice, que se quedan tal
cual). NO REIMPLEMENTA el union-find: importa
vuelta133_tabla_mapeo_propuesto como modulo y le SUSTITUYE su `recortar`
por la version extendida antes de llamar a su `calcular()`.

Publica, por el ramal (xvi) ("una regla se adjudica por su efecto sobre la
CANONICA, no solo por cuantos grupos colapsa"), LAS DOS COSAS AL LADO:
grupos resultantes Y canonicas resultantes, con las SINTETICAS listadas una
por una con su numero de grafias y de nodos.

Salida: docs/loop/SALIDA_V134_4B_EFECTO_CAP.txt

USO:
  python scripts/loop/vuelta134_efecto_cap_abreviado.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta133_tabla_mapeo_propuesto as vt133  # noqa: E402
from vuelta133_cola_localizador_apendice import PUNTUACION_FINAL  # noqa: E402

LOC_EXTENDIDA = re.compile(
    r",\s*(cap[ií]tulos?\s+.*|secci[oó]n\s+.*|[Aa]nexos?\s+.*|[Aa]p[eé]ndices?\s+.*|[Cc]aps?\.\s*.*)$",
    re.IGNORECASE)


def recortar_extendida(grafia):
    x = grafia
    while True:
        y = LOC_EXTENDIDA.sub("", x)
        y = PUNTUACION_FINAL.sub("", y)
        if y == x:
            return x
        x = y


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    recortar_original = vt133.recortar
    vt133.recortar = recortar_extendida
    try:
        censo, grafias, grupos, filas, origen_de = vt133.calcular()
    finally:
        vt133.recortar = recortar_original

    total_grupos = len(grupos)
    multi = {r: m for r, m in grupos.items() if len(m) > 1}
    sinteticas = {r: m for r, m in grupos.items() if origen_de.get(r) == "SINTETICA"}

    print("grafias: %d" % len(grafias))
    print("grupos totales (4 reglas, cola con Caps?.): %d" % total_grupos)
    print("grupos con 2+ miembros: %d" % len(multi))
    print("canonicas SINTETICAS: %d" % len(sinteticas))
    print("")
    print("SINTETICAS, una por una:")
    for r, miembros in sorted(sinteticas.items(), key=lambda kv: -len(kv[1])):
        n_nodos = sum(censo[m] for m in miembros)
        canonica = vt133_canonica_de(r, miembros, recortar_extendida)
        print("  canonica `%s`: %d grafia(s), %d nodo(s)" % (canonica, len(miembros), n_nodos))
        for m in sorted(miembros):
            print("    %r (%d nodos)" % (m, censo[m]))

    print("")
    print("EXITCODE: 0")
    return 0


def vt133_canonica_de(r, miembros, recortar):
    vieja = max(miembros, key=len)
    return recortar(vieja)


if __name__ == "__main__":
    raise SystemExit(main())
