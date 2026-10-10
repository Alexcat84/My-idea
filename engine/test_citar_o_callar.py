# -*- coding: utf-8 -*-
"""CITAR O CALLAR en el motor (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 3). El motor comparte
SYSTEM_PLAN con la web, asi que su redactor tambien escribe marcas de respaldo; el motor no tiene las respuestas
numeradas para validarlas (eso lo hace la web, web/lib/engine/citarOCallar.ts), pero nunca deja una marca en el plan:
las quita todas, tambien las mal cerradas. Sin API."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

ABRE, CIERRA = chr(0x27E6), chr(0x27E7)
texto = ("Vendes 12 macetas al mes " + ABRE + "R1" + CIERRA + ". Anota cuantas " + ABRE + "R1|" + chr(0xBF) + "Vendes mas?"
         + CIERRA + " salen.\n1. " + chr(0xBF) + "La tienda te paga lo mismo? " + ABRE + "?" + CIERRA + "\n2. Mal " + ABRE + "abierta")
limpio = pm._quitar_marcas(texto)
assert ABRE not in limpio and CIERRA not in limpio, limpio
assert limpio.startswith("Vendes 12 macetas al mes. Anota cuantas salen."), limpio
assert "CITAR O CALLAR" in pm.SYSTEM_PLAN
print("TODO OK: el motor nunca deja una marca de respaldo en el plan.")
