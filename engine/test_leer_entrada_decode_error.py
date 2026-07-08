# -*- coding: utf-8 -*-
"""Verifica que leer_entrada() convierte un UnicodeDecodeError (encontrado
en vivo pegando el texto de un anuncio con emojis en una consola de
Windows) en un cierre elegante (SesionInterrumpida), igual que EOF/Ctrl+C,
en vez de dejar propagar un traceback crudo."""
import builtins
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm


def input_falso_decode_error(prompt=""):
    raise UnicodeDecodeError("utf-8", b"\xf0\x9f\x98\x80", 0, 1, "codepage local no soporta este byte")


builtins_input_original = builtins.input
builtins.input = input_falso_decode_error

try:
    pm.leer_entrada("¿algo?\n> ")
    raise AssertionError("leer_entrada() deberia haber propagado SesionInterrumpida")
except pm.SesionInterrumpida:
    print("OK: UnicodeDecodeError se convierte en SesionInterrumpida (cierre elegante), no en traceback crudo.")
finally:
    builtins.input = builtins_input_original

print("\nTODO OK: leer_entrada() maneja UnicodeDecodeError con gracia.")
