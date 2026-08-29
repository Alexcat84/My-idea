# -*- coding: utf-8 -*-
"""vuelta134_censo_cola_no_recorta.py . TAREA 4.a de la vuelta 134.

La cola de localizador de la 133 (`vuelta133_cola_localizador_apendice.py`,
regex `LOC`) recorta ", capitulo(s) ...", ", seccion ...", ", anexo(s) ..."
y ", apendice(s) ...", pero NO reconoce la abreviatura `Cap.` (con punto),
y eso no lo vio nadie hasta hoy.

Censo: de las 129 grafias del corte, cuantas la cola de la 133 NO recorta
(`LOC.search(grafia)` da None), y para esas, agrupa por la PRIMERA PALABRA
que sigue a su ULTIMA coma (con su cuenta).

Reusa `cargar_censo` de vuelta131_grupos_por_titulo.py y `LOC` de
vuelta133_cola_localizador_apendice.py: no reimplementa ninguna de las dos.

Salida: docs/loop/SALIDA_V134_4A_CENSO_COLA.txt

USO:
  python scripts/loop/vuelta134_censo_cola_no_recorta.py
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import cargar_censo  # noqa: E402
from vuelta133_cola_localizador_apendice import LOC  # noqa: E402


def primera_palabra_tras_ultima_coma(grafia):
    if "," not in grafia:
        return None
    resto = grafia.rsplit(",", 1)[1].strip()
    if not resto:
        return None
    return resto.split()[0]


def main():
    censo = cargar_censo()
    grafias = sorted(censo.keys())

    no_recorta = [g for g in grafias if LOC.search(g) is None]

    por_palabra = Counter()
    for g in no_recorta:
        palabra = primera_palabra_tras_ultima_coma(g)
        if palabra is not None:
            por_palabra[palabra] += 1

    print("TOTAL grafias del censo: %d" % len(grafias))
    print("NO recortadas por la cola de la 133: %d" % len(no_recorta))
    print("")
    print("agrupadas por la primera palabra tras su ULTIMA coma, orden descendente:")
    for palabra, n in por_palabra.most_common():
        print("  %s: %d" % (palabra, n))

    sin_coma = [g for g in no_recorta if primera_palabra_tras_ultima_coma(g) is None]
    print("")
    print("no recortadas y SIN coma en la grafia (%d):" % len(sin_coma))
    for g in sin_coma:
        print("  %r" % g)

    print("")
    print("EXITCODE: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
