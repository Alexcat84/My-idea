# -*- coding: utf-8 -*-
"""engine/build_question_cache.py: el generador de preguntas adapta los papeles de empresa grande al contexto real
de la persona. Nacio el 28 sep 2026 como una regla suelta (ROLES DE EMPRESA GRANDE en SYSTEM_PREGUNTA) tras el vuelo
del mundo 11; con el visto del fundador del mismo dia la sustituye la REGLA UNICA del contexto del usuario
(web/lib/reglaContextoUsuario.ts, copiada letra a letra en REGLA_CONTEXTO_USUARIO), que el generador lleva en
SYSTEM_PREGUNTA_CON_REGLA, con el que nacen las preguntas nuevas (--faltantes).

Se comprueba que la regla unica nombra los papeles y manda adaptarlos o preguntarlos en condicional, que el
generador de preguntas nuevas la lleva, y que la regla suelta ya no esta.

    python engine/test_question_cache_roles.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "engine"))

import build_question_cache as bqc  # noqa: E402


def main():
    fallos = []
    regla = bqc.REGLA_CONTEXTO_USUARIO
    for x in ("jefe", "recursos humanos", "directivos", "condicional", "no tiene jefe", "forma, nunca el fondo"):
        if x not in regla:
            fallos.append(f"falta '{x}' en la regla unica")
    if not bqc.SYSTEM_PREGUNTA_CON_REGLA.endswith(regla):
        fallos.append("el generador de preguntas nuevas no lleva la regla unica")
    if "ROLES DE EMPRESA GRANDE" in bqc.SYSTEM_PREGUNTA:
        fallos.append("la regla suelta ROLES DE EMPRESA GRANDE sigue en SYSTEM_PREGUNTA")
    if fallos:
        print("ROJO:", *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: el generador adapta los papeles con la regla unica, sin la regla suelta")


if __name__ == "__main__":
    main()
