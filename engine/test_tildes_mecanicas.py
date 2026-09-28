# -*- coding: utf-8 -*-
"""Tildes mecanicas del remedio (acta de la auditoria final, seccion 9.3; decision del fundador del 28 sep 2026).

Solo entran las palabras cuya forma sin tilde no existe en espanol y cuya forma con tilde es unica. Las ambiguas
(solo, este, tu, si, mas, el, aun, que, como, esta...) son de los lectores. Los casos esperados se escribieron a mano
antes de escribir la funcion (AGENTS.md): cada uno dice que palabra cambia y por que.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts" / "saneamiento"))

import tildes_mecanicas as tm  # noqa: E402

PARES = json.loads((BASE / "docs" / "saneamiento" / "ortografia" / "tildes_mecanicas.json").read_text(encoding="utf-8"))["pares"]


def test_las_ambiguas_no_estan_en_la_lista():
    # Lista del fundador ("solo, este, tu, si, mas, el, aun y similares") mas las que tienen otra lectura sin tilde.
    ambiguas = ["solo", "este", "esta", "estas", "tu", "si", "mas", "el", "aun", "que", "como", "cuando", "donde",
                "quien", "cual", "critica", "practica", "publico", "calculo", "continua", "limites", "numero",
                "negocio", "cambio", "paso", "seria", "periodo", "diseno", "dano", "envio", "guia", "linea", "ultimo"]
    assert [a for a in ambiguas if a in PARES] == []


def test_corrige_palabra_entera_y_conserva_mayusculas():
    # "decision" -> "decisión"; "Tambien" -> "También" (mayuscula inicial); "DEBERIAS" -> "DEBERÍAS" (todo mayuscula).
    assert tm.corregir("Tambien tomas una decision.", PARES) == "También tomas una decisión."
    assert tm.corregir("hay que decidir cuanto DEBERIAS tener", PARES) == "hay que decidir cuanto DEBERÍAS tener"


def test_no_toca_una_palabra_mas_larga_ni_una_ambigua():
    # "comunicaciones" no lleva tilde y contiene "comunicacion": no se toca. "esta" y "como" son ambiguas: no se tocan.
    assert tm.corregir("las comunicaciones, esta decision y como se hace", PARES) == \
        "las comunicaciones, esta decisión y como se hace"


def test_respeta_los_nombres_en_ingles():
    # "Decision Log", "Cash Conversion Cycle" y "Discovery/Decision Day" son nombres en ingles: se quedan.
    assert tm.corregir("Registro de Decisiones (Decision Log)", PARES) == "Registro de Decisiones (Decision Log)"
    assert tm.corregir("Ciclo de Conversion de Efectivo (Cash Conversion Cycle)", PARES) == \
        "Ciclo de Conversión de Efectivo (Cash Conversion Cycle)"
    assert tm.corregir("cerrar en 'Discovery/Decision Day' o después", PARES) == "cerrar en 'Discovery/Decision Day' o después"


def test_ningun_nodo_vivo_trae_una_palabra_de_la_lista():
    # Guarda permanente: tras la tanda, ningun campo que ve la persona o la IA trae una palabra de la lista sin tilde.
    quedan = tm.pendientes(BASE / "dataset" / "nodos", PARES)
    assert quedan == [], quedan[:10]


if __name__ == "__main__":
    fallas = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_") and callable(f):
            try:
                f()
                print("OK  ", nombre)
            except AssertionError as e:
                fallas += 1
                print("FALLA", nombre, e)
    sys.exit(1 if fallas else 0)
