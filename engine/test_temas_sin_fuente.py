# -*- coding: utf-8 -*-
"""'MATERIAL' en el motor (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 1), igual que en la web
(web/lib/engine/temasSinFuente.test.ts). La ultima medicion sostuvo 'El material ensena que...' (M3A-f015-1) y 'El
material de este plan no cubre...' (M3A-f003-3) como procedencia. Los prompts ya no llaman 'material' a los temas, el
payload usa temas_del_recorrido y temas_vecinos, y el codigo quita las frases que citan los temas como fuente. El motor
solo escribe en espanol. Sin API."""
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

MATERIAL = re.compile(r"\bmaterial\b", re.IGNORECASE)

for nombre in ("SYSTEM_PLAN", "SYSTEM_INTERPRETE_MULTI", "SYSTEM_CAMINOS", "REGLA_SIN_CAUSAS_INVENTADAS"):
    texto = getattr(pm, nombre)
    assert not MATERIAL.search(texto), f"{nombre} sigue diciendo 'material': {MATERIAL.search(texto)}"
    assert "material_principal" not in texto and "material_de_apoyo" not in texto, nombre

fuente = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prototipo_motor.py"), encoding="utf8").read()
assert '"temas_del_recorrido": temas_del_recorrido' in fuente and '"temas_vecinos": temas_vecinos' in fuente, \
    "el payload del redactor usa temas_del_recorrido y temas_vecinos"

q = pm._quitar_citas_de_fuente
assert q("El material enseña que la seguridad funciona cuando la gente participa, no cuando se le impone. "
         "Por eso empieza preguntándoles.") == (
    "La seguridad funciona cuando la gente participa, no cuando se le impone. Por eso empieza preguntándoles.", 1)
assert q("Cambia la contraseña de tu correo. El material de este plan no cubre seguridad informática en detalle. "
         "Anota qué cuentas usas.")[0] == "Cambia la contraseña de tu correo. Anota qué cuentas usas."
assert q("Según el material, conviene empezar por lo más barato.")[0] == "Conviene empezar por lo más barato."
for fisico in ("Si el material se agrieta al secar, anota la humedad del día.",
               "Tu material sale caro: anota cuánto gastas por tanda.",
               "Revisa que el material muestra grietas antes de pintar."):
    assert q(fisico) == (fisico, 0), fisico
assert q("1. El material enseña que lo primero es medir. Anota tus costos.")[0] == "1. Lo primero es medir. Anota tus costos."

print("TODO OK: el motor no llama 'material' a los temas y quita las frases que los citan como fuente.")
