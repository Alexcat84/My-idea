# -*- coding: utf-8 -*-
r"""vuelta136_aplicar_ops11.py . TAREA 3.c de la vuelta 136: LA ESCRITURA de
`OP-S-11` (el campo `fuente` canonico). REGIMEN B, la primera de muchas
vueltas.

REUSA `vuelta136_simular_ops11.py` (importa `cargar_tabla`,
`cargar_nodos_vivos_con_fuente`, `declaraciones_de`, `normalizar`): no
reimplementa el mapeo ni el union-find. Escribe SOLO el campo `fuente` de
los nodos cuyo campo CAMBIA (la simulacion ya distingue cambia/no cambia);
no toca `nodos_siguientes`, `nodos_previos`, `titulo`, `deprecado` ni
`etiqueta_arbol`.

Salida: docs/loop/SALIDA_V136_3C_ESCRITURA.txt (nodo por nodo, fuente vieja
y fuente nueva).

Uso:
  python scripts/loop/vuelta136_aplicar_ops11.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta136_simular_ops11 import (  # noqa: E402
    cargar_tabla,
    cargar_nodos_vivos_con_fuente,
    declaraciones_de,
    normalizar,
)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V136_3C_ESCRITURA.txt")


def leer_nodo_crudo(ruta):
    """MISMO PATRON que scripts/loop/vuelta56_puntuacion_incisos.py
    (lineas 47 a 59): conserva EXACTAMENTE el final de linea del fichero
    para no fabricar un diff de fichero entero por un cambio de un solo
    campo."""
    with io.open(ruta, encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in (chr(13), chr(10)):
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir_nodo_crudo(ruta, datos, cola):
    with io.open(ruta, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def aplicar():
    mapa = cargar_tabla()
    nodos = cargar_nodos_vivos_con_fuente()

    escritos = []
    for ruta, id_nodo, fuente in nodos:
        declaraciones = declaraciones_de(fuente)
        _mapeadas, deduped = normalizar(declaraciones, mapa)
        if deduped == declaraciones:
            continue
        nueva_fuente = " | ".join(deduped)
        d, cola = leer_nodo_crudo(ruta)
        d["fuente"] = nueva_fuente
        escribir_nodo_crudo(ruta, d, cola)
        escritos.append((id_nodo, fuente, nueva_fuente))
    return escritos


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    escritos = aplicar()

    lineas = []
    lineas.append("ESCRITURA OP-S-11, vuelta 136, TAREA 3.c: campo `fuente` de nodos vivos")
    lineas.append("CIFRA nodos escritos: %d nodos" % len(escritos))
    for id_nodo, vieja, nueva in escritos:
        lineas.append("  %s: %s -> %s" % (id_nodo, vieja, nueva))
    lineas.append("")
    lineas.append("EXITCODE: 0")

    texto = "\n".join(lineas) + "\n"
    with io.open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(texto)
    sys.stdout.write("CIFRA nodos escritos: %d nodos\nEXITCODE: 0\n" % len(escritos))


if __name__ == "__main__":
    raise SystemExit(main())
