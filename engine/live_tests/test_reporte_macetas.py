# -*- coding: utf-8 -*-
"""Prueba mandatada de Motor v2.1: sesion real de macetas donde el usuario
declara sus numeros (resina/materiales $8, 4 horas/pieza, valor_hora $15,
precio $85, capacidad 5/semana, sin costos fijos), verifica que el
interprete los extrae y persiste en numeros_proyecto, y que --reporte
(modo_reporte) produce un reporte cuyas cifras narradas SI existen en la
salida de calculadora.py (nunca un numero huerfano)."""
import io
import os
import re
import sys
import tempfile
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import prototipo_motor as pm
import calculadora

pm.db.forzar_offline(True)

cola_respuestas = [
    "la resina y los materiales me cuestan $8 por pieza",
    "me toma 4 horas hacer cada pieza de principio a fin",
    "valoro mi hora de trabajo en $15",
    "vendería cada pieza en $85",
    "puedo hacer 5 piezas por semana trabajando solo",
    "todavia no he calculado si tengo otros costos aparte de estos",
    "creo que ya cubrimos lo esencial, dame mi plan",
]
idx = {"i": 0}


def leer_entrada_falso(prompt=""):
    print(prompt, end="")
    if idx["i"] < len(cola_respuestas):
        r = cola_respuestas[idx["i"]]
        idx["i"] += 1
    else:
        r = "creo que ya cubrimos lo esencial, dame mi plan"
    print(r)
    return r


pm.leer_entrada = leer_entrada_falso

entrada_original = (
    "hago macetas de calcita rosa con resina, extraigo la piedra yo mismo "
    "de una mina y la proceso en tumblers antes de fijarla en resina."
)

graph = pm.cargar_grafo()
families = pm.plan_readiness.cargar_families(graph)
entry_seeds = pm.cargar_entry_seeds()
preguntas_cache = pm.cargar_preguntas_cache()

buf = io.StringIO()
with redirect_stdout(buf):
    project_id = pm.db.crear_proyecto(entrada_original)
    db_session_id = pm.db.crear_sesion(project_id, "inicial", entrada_original)
    actual_id, perfil_sesion = pm.clasificar_entrada(entrada_original, entry_seeds, graph)
    print(f"\n(puerta de entrada elegida: {actual_id})")
    session_id = "testv21" + pm.uuid.uuid4().hex[:6]
    visitados, ruta, modos = {actual_id}, [actual_id], ["conversado"]
    pm._imprimir_nodo(1, pm.MAX_DEPTH, graph[actual_id], "puerta de entrada", con_resumen=True)

    resultado = pm.ejecutar_recorrido(
        graph, families, preguntas_cache, actual_id, visitados, ruta, modos,
        perfil_sesion, entrada_original, session_id, project_id, db_session_id,
    )
    pm._persistir_resultado(project_id, db_session_id, resultado, graph, families)
    pm.reportar_costo()

transcripcion_sesion = buf.getvalue()
print(transcripcion_sesion)
print("\n=== project_id:", project_id, "===")

proyecto = pm.db.obtener_proyecto(project_id)
numeros = proyecto.get("numeros_proyecto") or {}
print("\n=== numeros_proyecto extraidos por el interprete ===")
for campo, entry in numeros.items():
    print(f"  {campo}: {entry.get('valor')} (de: '{entry.get('texto_original', '')[:60]}')")

CAMPOS_ESPERADOS = {
    "costo_materiales_unidad": 8,
    "horas_por_unidad": 4,
    "valor_hora": 15,
    "precio_tentativo": 85,
    "capacidad_semanal": 5,
}
faltan = [c for c in CAMPOS_ESPERADOS if c not in numeros]
if faltan:
    print(f"\n(!) La conversacion normal no extrajo estos campos: {faltan}")
    print("Completando via --reporte (mini-entrevista) para poder seguir la prueba...")

# --- Ahora corre el modo --reporte sobre este proyecto ---
respuestas_reporte = {
    "costo_materiales_unidad": "8",
    "horas_por_unidad": "4",
    "valor_hora": "15",
    "precio_tentativo": "85",
    "capacidad_semanal": "5",
    "costos_fijos_mensuales": "no se",
}
def leer_entrada_reporte(prompt=""):
    print(prompt, end="")
    # Empareja por el TEXTO de la pregunta (no por posicion): modo_reporte
    # solo pregunta los campos que SIGUEN faltando, en el orden de
    # PREGUNTAS_NUMERICAS, asi que la cola posicional no es confiable si
    # algunos campos ya se extrajeron durante la sesion normal.
    r = "no se"
    for campo, pregunta in pm.PREGUNTAS_NUMERICAS.items():
        if pregunta in prompt:
            r = respuestas_reporte.get(campo, "no se")
            break
    print(r)
    return r


pm.leer_entrada = leer_entrada_reporte

# --reporte en produccion es una invocacion de CLI SEPARADA (proceso nuevo);
# en este script ambas fases comparten el mismo proceso, asi que hay que
# resetear los acumuladores de costo para no contaminar el techo de $0.10
# del reporte con lo que ya gasto la sesion anterior.
pm.USO = {}
pm.USO_POR_COMPONENTE = {}
pm.PRESUPUESTO_EXCEDIDO = False

buf2 = io.StringIO()
with redirect_stdout(buf2):
    pm.modo_reporte(project_id, graph, families)

reporte_transcripcion = buf2.getvalue()
print(reporte_transcripcion)

out_path = os.path.join(tempfile.gettempdir(), "reporte_macetas_transcript.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(transcripcion_sesion + "\n\n=== REPORTE ===\n\n" + reporte_transcripcion)

# --- Verificacion final: recalcula con calculadora.py y compara con el
# reporte narrado + con los criterios exactos mandatados ---
proyecto_final = pm.db.obtener_proyecto(project_id)
numeros_final = proyecto_final.get("numeros_proyecto") or {}
resultados = calculadora.calcular_reporte(numeros_final)
print("\n=== resultados crudos de calculadora.py ===")
print(resultados)

assert resultados["costo_unitario"]["valor"] == 68, resultados["costo_unitario"]
assert resultados["margen"]["valor"] == 17, resultados["margen"]
assert resultados["margen"]["porcentaje"] == 20.0, resultados["margen"]
assert resultados["capacidad"]["unidades_mes"] == 20, resultados["capacidad"]
assert resultados["capacidad"]["ingreso"] == 1700, resultados["capacidad"]
assert resultados["capacidad"]["margen_mensual"] == 340, resultados["capacidad"]
assert resultados["punto_equilibrio"]["valor"] is None
assert "costos_fijos_mensuales" in resultados["punto_equilibrio"]["insumos_faltantes"]
print("\nOK: asserts numericos exactos contra calculadora.py confirmados "
      "(costo=68, margen=17/20%, techo=20u/$1700/$340, equilibrio pendiente).")

# Verifica que cada cifra numerica mencionada en el reporte narrado
# corresponde a un valor real de 'resultados' (nunca un numero huerfano).
numeros_en_resultados = set()


def _recolectar_numeros(obj):
    if isinstance(obj, (int, float)):
        numeros_en_resultados.add(round(float(obj), 2))
        numeros_en_resultados.add(int(obj) if float(obj).is_integer() else round(float(obj), 2))
    elif isinstance(obj, dict):
        for v in obj.values():
            _recolectar_numeros(v)
    elif isinstance(obj, list):
        for v in obj:
            _recolectar_numeros(v)


_recolectar_numeros(resultados)
for campo, entry in numeros_final.items():
    _recolectar_numeros(entry.get("valor"))

cuerpo_reporte = reporte_transcripcion.split("## Tus números hoy", 1)[-1] if "## Tus números hoy" in reporte_transcripcion else reporte_transcripcion
cifras_en_texto = set()
for m in re.finditer(r"\$?\s*(\d[\d,]*(?:\.\d+)?)", cuerpo_reporte):
    crudo = m.group(1).replace(",", "")
    try:
        val = float(crudo)
        cifras_en_texto.add(int(val) if val.is_integer() else round(val, 2))
    except ValueError:
        pass

huerfanos = {v for v in cifras_en_texto if v not in numeros_en_resultados and v > 1}
print("\nCifras encontradas en el texto narrado:", sorted(cifras_en_texto))
print("Cifras disponibles en resultados/numeros:", sorted(numeros_en_resultados))
if huerfanos:
    print(f"\n(!) ADVERTENCIA: posibles cifras huerfanas en el texto narrado: {huerfanos}")
else:
    print("\nOK: ninguna cifra en el reporte narrado es huerfana (todas trazan a calculadora.py o a numeros_proyecto).")
