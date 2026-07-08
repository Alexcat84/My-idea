# -*- coding: utf-8 -*-
"""Motor v2.2, prueba mandatada (8d): el guardian GIGO debe abortar el
molde de preguntas de --reporte en cuanto 2 respuestas indican que no
encaja con el tipo de oferta activo (ej. le dan datos de una app de
suscripciones mientras el molde le sigue preguntando por "materiales por
pieza"), reclasificar tipo_oferta, y continuar con las preguntas del
molde correcto -- sin insistir con preguntas irrelevantes ni narrar un
disparate con datos mezclados entre dos moldes distintos.

Corre modo_reporte() completo contra un proyecto local (--offline),
con llamar_claude y leer_entrada mockeados (sin llamadas reales a la API)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

pm.db.forzar_offline(True)

project_id = pm.db.crear_proyecto("una app para llevar el registro de suscripciones de streaming")
families = pm.plan_readiness.cargar_families(pm.cargar_grafo())
graph = pm.cargar_grafo()

# El proyecto arranca con el molde 'producto_fisico' ya asignado (simula
# un proyecto donde --reporte ya se corrio antes bajo el molde por
# defecto, sin saber todavia que es una oferta digital).
pm.db.actualizar_proyecto(project_id, tipo_oferta="producto_fisico", unidad_venta="pieza")

respuestas = [
    "no tengo piezas, esto no es un producto fisico",              # respuesta a costo_materiales_unidad (fisico)
    "no funciona asi, es una suscripcion digital",                  # respuesta a horas_por_unidad (fisico) -> 2do "no aplica"
    "es una app de suscripciones para gestionar pagos recurrentes",  # aclaracion tras el 2do "no aplica"
    "200",   # costos_fijos_mensuales (digital)
    "0",     # costo_materiales_unidad / variable (digital)
    "13",    # precio_tentativo (digital)
    "20",    # unidades_vendidas / meta (digital)
]
idx = {"i": 0}


def leer_entrada_falsa(prompt=""):
    r = respuestas[idx["i"]]
    idx["i"] += 1
    print(prompt)
    print(">", r)
    return r


def llamar_claude_falso(system, user_text, model, max_tokens=1500, componente=None):
    # Reusado tanto para _clasificar_oferta (espera este JSON) como para
    # _narrar_reporte (la narracion en si no se verifica en esta prueba,
    # solo el mecanismo de deteccion/reclasificacion y los numeros
    # capturados).
    return json.dumps({"tipo_oferta": "digital", "unidad_venta": "suscripcion"})


pm.leer_entrada = leer_entrada_falsa
pm.llamar_claude = llamar_claude_falso

pm.modo_reporte(project_id, graph, families)

assert idx["i"] == len(respuestas), (
    f"se esperaba consumir las {len(respuestas)} respuestas encoladas, se consumieron {idx['i']}"
)

proyecto_final = pm.db.obtener_proyecto(project_id)
assert proyecto_final["tipo_oferta"] == "digital", proyecto_final["tipo_oferta"]
assert proyecto_final["unidad_venta"] == "suscripcion", proyecto_final["unidad_venta"]

numeros = proyecto_final["numeros_proyecto"]
CAMPOS_DIGITALES_ESPERADOS = {"costos_fijos_mensuales", "costo_materiales_unidad", "precio_tentativo", "unidades_vendidas"}
assert set(numeros.keys()) == CAMPOS_DIGITALES_ESPERADOS, (
    f"el molde fisico abandonado (horas_por_unidad, valor_hora, capacidad_semanal) "
    f"NO debe dejar rastro en numeros_proyecto; se encontro: {set(numeros.keys())}"
)
assert numeros["costos_fijos_mensuales"]["valor"] == 200, numeros["costos_fijos_mensuales"]
assert numeros["costos_fijos_mensuales"]["unidad"] == "por mes", numeros["costos_fijos_mensuales"]
assert numeros["precio_tentativo"]["valor"] == 13, numeros["precio_tentativo"]
assert numeros["unidades_vendidas"]["valor"] == 20, numeros["unidades_vendidas"]
assert numeros["unidades_vendidas"]["unidad"] == "suscripcion/mes", numeros["unidades_vendidas"]

print("\nTODO OK: guardian GIGO aborta el molde 'producto_fisico' al segundo 'no aplica', "
      "reclasifica a 'digital', y captura los 4 campos correctos (equilibrio esperado: "
      "ceil(200/13)=16, ver test_digital_founder_caso_real en test_calculadora.py) sin "
      "rastro del molde abandonado.")
