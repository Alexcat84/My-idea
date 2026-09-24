# -*- coding: utf-8 -*-
"""AUD-09 B14a: el respaldo del detector de decision (cuando la IA no lee la
respuesta) decidia por SUBCADENAS: 'playa' contiene 'ya' y cortaba la
exploracion. Frases explicitas a cualquier largo; palabras sueltas solo
enteras y en una respuesta corta. Paridad con web/lib/engine/recorrido.ts
(decisionPorPalabras): los mismos casos, calculados a mano."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

CASOS = [
    ("playa", "continuar"),
    ("vendo en la playa", "continuar"),
    ("ya tengo tres clientes fijos", "continuar"),
    ("", "continuar"),
    ("ya", "generar_ya"),
    ("Listo.", "generar_ya"),
    ("ya, dale", "generar_ya"),
    ("dame mi plan ya, con esto alcanza", "generar_ya"),
    ("Así está bien", "generar_ya"),
]

fallas = []
for texto, esperado in CASOS:
    obtenido = pm._decision_por_palabras(texto)
    if obtenido != esperado:
        fallas.append(f"{texto!r}: esperado {esperado}, obtenido {obtenido}")

if fallas:
    print("FALLA:\n  " + "\n  ".join(fallas))
    sys.exit(1)
print(f"OK: {len(CASOS)} casos del respaldo por palabras")
