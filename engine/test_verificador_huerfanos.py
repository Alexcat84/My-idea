# -*- coding: utf-8 -*-
"""Fase 3.1 (caja de vidrio): verificador de numeros huerfanos. Casos
mandatados: tolerancia de formato (1.700 vs 1700), y un caso sintetico
con un numero inyectado fuera de material que debe disparar el flag."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificador_huerfanos as vh

# --- Tolerancia de formato ---
assert vh._normalizar_numero("1.700") == 1700.0, "1.700 (miles, estilo hispano) debe normalizar a 1700"
assert vh._normalizar_numero("1,700") == 1700.0, "1,700 (coma de miles) debe normalizar a 1700"
assert vh._normalizar_numero("0.35") == 0.35, "0.35 (2 decimales) NO debe confundirse con separador de miles"
assert vh._normalizar_numero("17.5") == 17.5, "17.5 (1 decimal) es un decimal real"
assert vh._normalizar_numero("$85") == 85.0
assert vh._normalizar_numero("-2976.9%") == -2976.9
print("Caso 1 OK: tolerancia de formato (1.700 vs 1700, comas, %, $) verificada.")

# --- Extraccion con contexto ---
numeros = vh.extraer_numeros("Cada maceta cuesta $68 en materiales y se vende en $85.")
valores = [v for v, _, _ in numeros]
assert 68.0 in valores and 85.0 in valores
print("Caso 2 OK: extraccion de numeros con contexto funciona.")

# --- numeros_de_calculadora / numeros_declarados: extraccion recursiva ---
resultados_calc = {
    "margen": {"valor": 13, "porcentaje": 100.0, "insumos_usados": ["a"], "insumos_faltantes": []},
    "punto_equilibrio": {"valor": 16, "insumos_faltantes": []},
    "capacidad": {"unidades_mes": None, "ingreso": None},
}
nums_calc = vh.numeros_de_calculadora(resultados_calc)
assert nums_calc == {13.0, 100.0, 16.0}, nums_calc
print("Caso 3 OK: numeros_de_calculadora extrae solo los valores numericos hoja, ignora None/listas/strings.")

numeros_proyecto = {"precio_tentativo": {"valor": 13}, "costos_fijos_mensuales": {"valor": 200}}
nums_decl = vh.numeros_declarados(numeros_proyecto)
assert nums_decl == {13.0, 200.0}, nums_decl
print("Caso 4 OK: numeros_declarados extrae los valores del usuario.")

# --- El caso mandatado: numero inyectado fuera de material dispara el flag ---
texto_reporte_sano = (
    "Tu margen por unidad es de $13 (100%). Con costos fijos de $200/mes, "
    "tu punto de equilibrio es de 16 unidades/mes."
)
permitidos = {13.0, 100.0, 200.0, 16.0}
huerfanos_sano = vh.verificar_numeros_huerfanos(texto_reporte_sano, permitidos)
assert huerfanos_sano == [], f"un reporte que solo usa numeros permitidos no debe marcar huerfanos: {huerfanos_sano}"
print("Caso 5 OK: reporte sano (solo numeros permitidos) no dispara ningun flag.")

texto_contaminado = texto_reporte_sano + " Si escalas, podrias llegar a vender 4500 unidades el proximo trimestre."
eventos = []
huerfanos = vh.verificar_numeros_huerfanos(texto_contaminado, permitidos, registrar_evento=lambda e: eventos.append(e))
assert len(huerfanos) == 1, f"se esperaba exactamente 1 numero huerfano (4500), hubo: {huerfanos}"
assert huerfanos[0]["valor"] == "4500"
assert len(eventos) == 1 and eventos[0]["tipo"] == "numero_huerfano" and eventos[0]["valor"] == "4500"
print("Caso 6 OK (mandatado): numero inyectado fuera de material (4500) dispara 'numero_huerfano' con su contexto.")
print("  contexto capturado:", huerfanos[0]["contexto"])

# --- Bug real encontrado en vivo (vuelo.ts fase 3): escenarios_adopcion usa
# claves '50%'/'100%'/'200%' -- un numero en una CLAVE tambien debe contar. ---
resultados_con_claves_pct = {
    "escenarios": {
        "50%": {"unidades": 10, "ingreso": 130},
        "100%": {"unidades": 20, "ingreso": 260},
        "200%": {"unidades": 40, "ingreso": 520},
    },
}
nums_con_claves = vh.numeros_de_calculadora(resultados_con_claves_pct)
assert {50.0, 100.0, 200.0} <= nums_con_claves, (
    f"los numeros en las CLAVES del dict (50%/100%/200%) deben extraerse tambien: {nums_con_claves}"
)
print("Caso 7 OK (bug real, vuelo.ts fase 3): numeros en claves de dict ('50%') tambien se extraen.")

# --- Bug real encontrado en vivo: el narrador hace aritmetica simple de un
# paso sobre numeros ya permitidos (ej. 'a partir del usuario 17' cuando el
# equilibrio es 16; '$60 de ganancia' cuando ingreso=260 y costos=200) --
# eso no es fabricar cifras, cerradura_aritmetica debe tolerarlo. ---
base = {16.0, 20.0, 200.0, 260.0, 130.0, 520.0}
cerradura = vh.cerradura_aritmetica(base)
assert 17.0 in cerradura, "16+1=17 ('a partir del usuario 17') debe estar en la cerradura"
assert 4.0 in cerradura, "20-16=4 ('lo supera por 4') debe estar en la cerradura"
assert 60.0 in cerradura, "260-200=60 ('$60 de ganancia') debe estar en la cerradura"
assert 70.0 in cerradura, "200-130=70 ('deficit de $70') debe estar en la cerradura"
assert 320.0 in cerradura, "520-200=320 ('$320 de ganancia') debe estar en la cerradura"
assert 4500.0 not in cerradura, "la cerradura NO debe volverse tan laxa que acepte cualquier cosa (4500 sigue fuera)"
print("Caso 8 OK (bug real, vuelo.ts fase 3): cerradura_aritmetica tolera narracion derivada sin dejar de detectar huerfanos reales.")

print("\nTODO OK: verificador de numeros huerfanos (Fase 3.1) funciona.")
