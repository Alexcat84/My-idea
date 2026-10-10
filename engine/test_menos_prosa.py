# -*- coding: utf-8 -*-
"""MENOS PROSA en el motor (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 4), igual que en la web
(web/lib/engine/menosProsa.test.ts): introduccion corta (primer parrafo, dos frases como mucho) y, en cada etapa, solo
los bloques que empiezan con un rotulo o un paso. Las secciones fijas no se tocan; una etapa sin nada accionable se deja
como vino. Extracto real del plan 85248377 de la ultima medicion. Sin API."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

REAL = "\n".join([
    "# Seguridad en tu taller de macetas",
    "",
    "Trabajas con cemento y polvo todos los días, tienes dos empleados recién contratados y nunca has anotado qué "
    "podría salir mal en el taller. Este plan parte de la mascarilla que ya elegiste. Al final tendrás un taller más seguro.",
    "",
    "## Etapa 1: Anota qué puede lastimarte a ti y a tu taller",
    "",
    "Hasta hoy has ido apagando incendios. Antes de decidir qué proteger primero, hace falta ver todos los peligros juntos.",
    "",
    "**Pasos:**",
    "1. Recorre el taller con calma y anota cada peligro para la salud que veas.",
    "",
    "**Entregable:**",
    "",
    "Una lista de peligros ordenada por riesgo, con fotos.",
    "",
    "**Primera acción:** Anota en tu celular los tres peligros del taller que más te preocupan.",
    "",
    "Predicar con el ejemplo quita el aire de reproche.",
    "",
    "## ¿Puede sostenerse tu idea? Los números en simple",
    "",
    "Tu idea se sostiene si lo que entra cubre lo que sale.",
])

texto, quitadas, intro_recortada = pm._podar_prosa(REAL)
assert "Este plan parte de la mascarilla que ya elegiste." in texto
assert "Al final tendrás un taller más seguro" not in texto and intro_recortada
assert "Hasta hoy has ido apagando incendios" not in texto
assert "Predicar con el ejemplo quita el aire de reproche" not in texto
assert quitadas == 2, quitadas
for queda in ("1. Recorre el taller con calma y anota cada peligro para la salud que veas.",
              "Una lista de peligros ordenada por riesgo, con fotos.",
              "**Primera acción:** Anota en tu celular los tres peligros del taller que más te preocupan.",
              "Tu idea se sostiene si lo que entra cubre lo que sale."):
    assert queda in texto, queda
assert pm._podar_prosa(texto) == (texto, 0, False), "idempotente"
roto = "# Plan\n\nContexto.\n\n## Etapa 1: Algo\n\nSolo un párrafo que explica qué hacer sin lista."
assert "Solo un párrafo que explica qué hacer sin lista." in pm._podar_prosa(roto)[0]

assert "INTRODUCCION CORTA" in pm.SYSTEM_PLAN and "PROHIBIDO un parrafo narrativo" in pm.SYSTEM_PLAN
assert "Vender a amigas te dice que el producto gusta" not in pm.SYSTEM_PLAN

print("TODO OK: el motor deja la introduccion corta y las etapas solo accionables.")
