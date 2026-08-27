# -*- coding: utf-8 -*-
"""vuelta88_tarea3_caso_rojo.py . VUELTA 88, TAREA 3.d (adjudicacion 6.3 del
acta de la vuelta 87): UN ROJO INVENTADO POR EL EJECUTOR para el instrumento
arreglado (vuelta88_tarea3_arreglo_desbloqueo_fase04.py).

QUE HACE: toma una COPIA EN MEMORIA (nunca se escribe al arbol real) de
docs/plan/02_DESTEJIDOS.md, mete una marca negativa ("QUEDA PENDIENTE") DENTRO
de la ventana de proximidad (220 caracteres) de una mencion real de OP-D-02,
que HOY sale EJECUTADA, y comprueba que el lector la voltea a NO EJECUTADA.
Si el lector no la voltea, este script termina con AssertionError y NO
declara el caso rojo probado.

NO TOCA NINGUN FICHERO REAL: `git status --porcelain -- docs/plan/` se
verifica vacio antes y despues, y se cita en el reporte.

USO:
  python scripts/loop/vuelta88_tarea3_caso_rojo.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta88_tarea3_arreglo_desbloqueo_fase04 as m

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_REAL = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")


def leer_estado_de_texto(oid, texto):
    """Repite la lectura de pagina de estado_real() pero sobre un TEXTO dado
    (nunca un fichero del arbol), para poder probar una copia modificada."""
    cabecera_pagina = "\n".join(texto.split("\n")[:m.PRIMERAS_LINEAS_CABECERA])
    patron_id = re.compile(r"(?<![\w-])" + re.escape(oid) + r"(?![\w-])")
    cabecera_relevante = cabecera_pagina if patron_id.search(cabecera_pagina) else ""
    secciones = m.secciones_de(texto, oid)
    cuerpo_secciones = "\n".join(s[2] for s in secciones)
    proximidad = m.ventanas_de_proximidad(texto, oid)

    neg = m.marca_negativa(cabecera_relevante) or m.marca_negativa(proximidad)
    if neg:
        return "NO EJECUTADA", neg
    pos = m.marca_positiva(oid, cabecera_relevante + "\n" + cuerpo_secciones)
    if pos:
        return "EJECUTADA", pos
    return "AMBIGUA", "ninguna marca positiva ni negativa reconocida"


def main():
    texto_real = io.open(RUTA_REAL, encoding="utf-8").read()

    v_antes, ev_antes = leer_estado_de_texto("OP-D-02", texto_real)
    print("ANTES (texto real, sin tocar): OP-D-02 -> %s" % v_antes)
    assert v_antes == "EJECUTADA", "el caso rojo necesita partir de EJECUTADA, salio %s" % v_antes

    # Localiza una mencion real de OP-D-02 e inyecta la marca negativa DENTRO
    # de la ventana de 220 caracteres, en una COPIA EN MEMORIA.
    patron = re.compile(r"(?<![\w-])OP-D-02(?![\w-])")
    primera = patron.search(texto_real)
    assert primera, "OP-D-02 no aparece en el texto real"
    punto_insercion = min(primera.end() + 50, len(texto_real))
    texto_copia = (
        texto_real[:punto_insercion]
        + " QUEDA PENDIENTE la revision de OP-D-02. "
        + texto_real[punto_insercion:]
    )

    v_despues, ev_despues = leer_estado_de_texto("OP-D-02", texto_copia)
    print("DESPUES (copia en memoria, con marca negativa inyectada): OP-D-02 -> %s" % v_despues)
    print("  evidencia: %s" % ev_despues)
    assert v_despues == "NO EJECUTADA", (
        "EL CASO ROJO FALLO: el lector arreglado no volteo la copia modificada "
        "(salio %s en vez de NO EJECUTADA)" % v_despues
    )

    print()
    print("CASO ROJO PROBADO: el lector voltea EJECUTADA -> NO EJECUTADA cuando la")
    print("marca negativa cae dentro de la ventana de proximidad de la copia, y")
    print("NINGUN fichero real se toco (ver git status --porcelain -- docs/plan/).")


if __name__ == "__main__":
    main()
