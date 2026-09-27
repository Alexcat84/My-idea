# -*- coding: utf-8 -*-
"""engine/build_question_cache.py: el generador de preguntas adapta los roles de empresa grande al contexto real del
emprendedor (decision del fundador del 28 sep 2026, tras el vuelo del mundo 11: preguntas con "tu propio jefe",
recursos humanos y directivos a una persona que es duena de su negocio).

La regla vive en SYSTEM_PREGUNTA, que es lo unico que el modelo recibe como instruccion. Se comprueba que nombra los
tres roles y que manda adaptarlos o preguntarlos en condicional, y que no dar por hecho un jefe es regla, no ejemplo.

    python engine/test_question_cache_roles.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "engine"))

import build_question_cache as bqc  # noqa: E402


def main():
    t = bqc.SYSTEM_PREGUNTA
    fallos = [f"falta '{x}' en SYSTEM_PREGUNTA" for x in
              ("ROLES DE EMPRESA GRANDE", "jefe", "recursos humanos", "directivos", "condicional", "no tiene jefe")
              if x not in t]
    if fallos:
        print("ROJO:", *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: el generador adapta jefe, recursos humanos y directivos al contexto real del emprendedor")


if __name__ == "__main__":
    main()
