# -*- coding: utf-8 -*-
"""La GUARDA del 100 % de las neutrales (scripts/corrida_final/verificar_cache.py, decision del fundador del 8 oct
2026): ademas de los papeles supuestos, detecta los cuatro patrones que hicieron fallar la muestra ciega (semilla
20261008, 49 de 200): el genero marcado al lector, la segunda peticion que la base no tiene, las personas sin
condicional y el contexto propio de la base que se pierde. Prueba pura, sin API ni archivos."""
import importlib.util
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("verificar_cache", os.path.join(RAIZ, "scripts", "corrida_final", "verificar_cache.py"))
vc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vc)

BASE = "¿Cómo atiendes hoy a las personas interesadas en tu franquicia?"

# 1. genero marcado al lector (los casos reales de la muestra)
assert "genero" in vc.patrones(BASE, "¿Las atiendes tú misma, si trabajas sola?")
assert "genero" in vc.patrones(BASE, "¿Te sientes preparada para atender a quienes se interesan en tu franquicia?")
assert "genero" not in vc.patrones(BASE, "¿Las atiendes tú mismo o con ayuda, en tu franquicia?")

# 2. segunda peticion: mas preguntas que la base
assert "segunda_peticion" in vc.patrones(BASE, "¿Cómo atiendes a los interesados en tu franquicia? ¿Y si tuvieras jefe?")
assert "segunda_peticion" not in vc.patrones(BASE, "¿Cómo atiendes hoy a quienes se interesan en tu franquicia?")

# 3. personas sin condicional (la base no las supone)
B3 = "¿Qué haces cuando un cliente se queja?"
assert "personas_sin_condicional" in vc.patrones(B3, "¿Qué hacen las personas que te acompañan cuando un cliente se queja?")
assert "personas_sin_condicional" not in vc.patrones(B3, "¿Qué haces cuando un cliente se queja, tú o quienes trabajen contigo si los tienes?")

# 4. contexto propio perdido: el tema concreto de la base desaparece de la neutral
assert "contexto_perdido" in vc.patrones(BASE, "¿Cómo atiendes hoy a las personas interesadas en lo que ofreces?")
assert "contexto_perdido" not in vc.patrones(BASE, "¿Cómo atiendes hoy a quienes se interesan en tu franquicia?")
B4 = "¿Qué pasaría si uno de tus proveedores falla una entrega?"
assert "contexto_perdido" in vc.patrones(B4, "¿Qué pasaría si algo falla en una entrega?")

# una neutral fiel no dispara nada
assert vc.patrones(BASE, "¿Cómo atiendes hoy a quienes se interesan en tu franquicia?") == []
print("OK guarda de las neutrales: genero, segunda peticion, personas sin condicional y contexto perdido")
