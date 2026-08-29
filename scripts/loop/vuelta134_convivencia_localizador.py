# -*- coding: utf-8 -*-
"""vuelta134_convivencia_localizador.py . TAREA 4.c de la vuelta 134.

Para cada familia del censo que trae un localizador de capitulo, dice si lo
trae ESCRITO (capitulo/seccion/anexo/apendice, lo que ya recorta
LOC de vuelta133_cola_localizador_apendice.py), ABREVIADO (`, Cap.` o
`, Caps.`) o LAS DOS FORMAS. La familia se define por la forma recortada
bajo la cola EXTENDIDA (vuelta134_efecto_cap_abreviado.recortar_extendida):
agrupa las grafias del mismo libro sin importar que forma de localizador
traiga cada una.

Salida: parte de docs/loop/SALIDA_V134_4C_CONVIVENCIA.txt

USO:
  python scripts/loop/vuelta134_convivencia_localizador.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta131_grupos_por_titulo import cargar_censo  # noqa: E402
from vuelta133_cola_localizador_apendice import LOC  # noqa: E402
from vuelta134_efecto_cap_abreviado import recortar_extendida  # noqa: E402

ABREVIADO = re.compile(r",\s*Caps?\.", re.IGNORECASE)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo = cargar_censo()
    grafias = sorted(censo.keys())

    familias = {}
    for g in grafias:
        clave = recortar_extendida(g)
        familias.setdefault(clave, []).append(g)

    con_localizador = {clave: miembros for clave, miembros in familias.items()
                        if any(LOC.search(m) or ABREVIADO.search(m) for m in miembros)}

    escritas = []
    abreviadas = []
    ambas = []
    for clave, miembros in sorted(con_localizador.items()):
        tiene_escrita = any(LOC.search(m) for m in miembros)
        tiene_abreviada = any(ABREVIADO.search(m) for m in miembros)
        if tiene_escrita and tiene_abreviada:
            ambas.append(clave)
        elif tiene_escrita:
            escritas.append(clave)
        elif tiene_abreviada:
            abreviadas.append(clave)

    print("familias del censo CON localizador de capitulo: %d" % len(con_localizador))
    print("")
    print("familias con la forma LAS DOS (escrita Y abreviada): %d" % len(ambas))
    for clave in ambas:
        print("  %r" % clave)
    print("")
    print("familias SOLO escrita (capitulo/seccion/anexo/apendice): %d" % len(escritas))
    for clave in escritas:
        print("  %r (%d grafia(s))" % (clave, len(con_localizador[clave])))
    print("")
    print("familias SOLO abreviada (, Cap. / , Caps.): %d" % len(abreviadas))
    for clave in abreviadas:
        print("  %r (%d grafia(s))" % (clave, len(con_localizador[clave])))

    conjunto_escritas = set(escritas)
    conjunto_abreviadas = set(abreviadas)
    disjuntos = conjunto_escritas.isdisjoint(conjunto_abreviadas) and not ambas
    print("")
    print("CONJUNTOS DISJUNTOS (ninguna familia trae las dos formas): %s" % disjuntos)
    print("")
    print("EXITCODE: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
