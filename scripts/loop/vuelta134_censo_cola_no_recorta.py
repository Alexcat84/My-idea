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

DOS PREDICADOS (TAREA 3.b de la vuelta 135, acta 134, 4.3: "la etiqueta de
mi 4.a ... nombraba UN predicado y admitia DOS"). AHORA PUBLICA LAS DOS
CIFRAS, cada una con su predicado escrito, en vez de solo la primera:
  (A) SIN LOCALIZADOR RECONOCIDO: `LOC.search(g) is None` (el localizador
      NO APARECE en la grafia).
  (B) QUE LA COLA DEJA INTACTAS AL CARACTER:
      `recortar_localizador_con_apendice(g) == g` (la cola NO LA TOCA: la
      aplica y compara byte a byte, distinto de (A), porque una cola puede
      APARECER sin RECORTAR nada si su match no llega al final de la
      cadena o el resultado coincide por otra via).
Las dos mediciones son CORRECTAS a la vez: la grafia que las separa (LOC
la detecta pero la cola NO la recorta al caracter, por el `;` final que
PUNTUACION_FINAL no absorbe en un solo paso del bucle en este caso
particular) se nombra en la salida.
Salida (TAREA 3.b): docs/loop/SALIDA_V135_3B_CENSO_DOS_PREDICADOS.txt

USO:
  python scripts/loop/vuelta134_censo_cola_no_recorta.py
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import cargar_censo  # noqa: E402
from vuelta133_cola_localizador_apendice import (  # noqa: E402
    LOC,
    recortar_localizador_con_apendice,
)


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

    sin_localizador = [g for g in grafias if LOC.search(g) is None]
    cola_no_toca = [g for g in grafias if recortar_localizador_con_apendice(g) == g]

    por_palabra = Counter()
    for g in sin_localizador:
        palabra = primera_palabra_tras_ultima_coma(g)
        if palabra is not None:
            por_palabra[palabra] += 1

    separadoras = sorted(set(sin_localizador) ^ set(cola_no_toca))

    print("TOTAL grafias del censo: %d" % len(grafias))
    print("")
    print("PREDICADO (A) SIN LOCALIZADOR RECONOCIDO (LOC.search(g) is None): %d grafias" %
          len(sin_localizador))
    print("CIFRA sin localizador reconocido (LOC.search es None): %d grafias" % len(sin_localizador))
    print("")
    print("PREDICADO (B) QUE LA COLA DEJA INTACTAS AL CARACTER (recortar(g) == g): %d grafias" %
          len(cola_no_toca))
    print("CIFRA que la cola deja intactas al caracter (recortar(g) == g): %d grafias" %
          len(cola_no_toca))
    print("")
    print("grafia(s) que SEPARAN los dos predicados (en uno y no en el otro), %d:" %
          len(separadoras))
    for g in separadoras:
        print("  %r (LOC.search: %s, recortar==g: %s)" %
              (g, LOC.search(g) is not None, recortar_localizador_con_apendice(g) == g))

    print("")
    print("agrupadas por la primera palabra tras su ULTIMA coma (predicado A), orden descendente:")
    for palabra, n in por_palabra.most_common():
        print("  %s: %d" % (palabra, n))

    sin_coma = [g for g in sin_localizador if primera_palabra_tras_ultima_coma(g) is None]
    print("")
    print("predicado (A) y SIN coma en la grafia (%d):" % len(sin_coma))
    for g in sin_coma:
        print("  %r" % g)

    print("")
    print("EXITCODE: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
