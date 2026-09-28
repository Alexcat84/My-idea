# -*- coding: utf-8 -*-
"""Guarda permanente de la navegacion del catalogo (auditoria final, G2 y G3; acta secciones 4, 6.1 y 8.1).

Murallas de dominio, puentes solo del nucleo a un mundo, ley del ancla, puertas, alcanzabilidad del 100 % en el
nucleo y en cada mundo desde sus propias puertas, jurisdiccion con pais y clase, y cero aristas a deprecados. El
instrumento es scripts/auditoria_final/navegacion.py; esta prueba lo pone en la suite para que no vuelva a romperse.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "auditoria_final"))

import navegacion  # noqa: E402


def test_navegacion_del_catalogo_en_verde():
    r = navegacion.medir()
    assert r["fallos"] == [], r["fallos"]


if __name__ == "__main__":
    try:
        test_navegacion_del_catalogo_en_verde()
        print("OK   test_navegacion_del_catalogo_en_verde")
    except AssertionError as e:
        print("FALLA test_navegacion_del_catalogo_en_verde", e)
        sys.exit(1)
