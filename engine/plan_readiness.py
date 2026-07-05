# -*- coding: utf-8 -*-
"""
plan_readiness.py - Clasifica nodos en familias para el medidor de completitud (Fase 2.2)

Clasificacion por palabras clave (sin llamadas a la API, corrida unica y
reproducible) sobre titulo_concepto + resumen_teorico, normalizados (sin
acentos, minusculas). Familias: accion_clientes (validar con clientes
reales), viabilidad_economica (numeros del negocio), general (todo lo
demas). La lista de palabras clave es revisable mas abajo.

Uso: python engine/plan_readiness.py   # regenera engine/node_families.json
"""
import json
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
FAMILIES_PATH = BASE / "engine" / "node_families.json"

MIN_NODOS_COMPLETA = 5

# Revisar/ajustar aqui. Coincidencia por substring sobre texto normalizado
# (sin acentos, minusculas) de titulo_concepto + resumen_teorico.
KEYWORDS_ACCION_CLIENTES = [
    "entrevista", "voz del cliente", "mvp", "producto minimo viable",
    "prueba de usuario", "pruebas de usuario", "testeo con usuario",
    "validacion con cliente", "desarrollo de clientes", "customer development",
    "customer discovery", "investigacion de usuario", "user research",
    "prototipo", "feedback de cliente", "retroalimentacion de cliente",
    "presentacion del problema", "descubrimiento de clientes",
    "investigacion etnografica", "observacion de campo",
]

KEYWORDS_VIABILIDAD_ECONOMICA = [
    "punto de equilibrio", "flujo de caja", "flujo de efectivo",
    "unit economics", "metricas financieras", "modelo de ingresos",
    "estructura de costos", "analisis financiero", "proyeccion financiera",
    "presupuesto operativo", "margen de contribucion", "burn rate", "runway",
    "break even", "break-even", "estado de resultados",
    "inteligencia financiera", "arte de las finanzas", "fuentes de financiamiento",
    "rentabilidad", "numeros del negocio", "precio de venta",
    "estrategia de precios", "modelo de precios",
]


def _normalizar(texto):
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def _coincide(texto_normalizado, palabras_clave):
    return any(p in texto_normalizado for p in palabras_clave)


def clasificar_nodo(node):
    texto = _normalizar(f"{node.get('titulo_concepto', '')} {node.get('resumen_teorico', '')}")
    if _coincide(texto, KEYWORDS_ACCION_CLIENTES):
        return "accion_clientes"
    if _coincide(texto, KEYWORDS_VIABILIDAD_ECONOMICA):
        return "viabilidad_economica"
    return "general"


def clasificar_grafo(graph):
    return {nid: clasificar_nodo(n) for nid, n in graph.items()}


def cargar_families(graph):
    if FAMILIES_PATH.exists():
        return json.load(open(FAMILIES_PATH, encoding="utf-8"))
    return clasificar_grafo(graph)


def evaluar_ruta(ruta, families):
    """Evalua si una ruta esta lista para un plan completo (toca >=1 nodo de
    accion_clientes y >=1 de viabilidad_economica, con al menos 5 nodos)."""
    familias_en_ruta = {families.get(nid, "general") for nid in ruta}
    tiene_accion = "accion_clientes" in familias_en_ruta
    tiene_viabilidad = "viabilidad_economica" in familias_en_ruta
    es_completa = tiene_accion and tiene_viabilidad and len(ruta) >= MIN_NODOS_COMPLETA
    faltantes = []
    if not tiene_accion:
        faltantes.append("validar con clientes reales (entrevistas, MVP, pruebas de usuario)")
    if not tiene_viabilidad:
        faltantes.append("los numeros del negocio (costos, precios, punto de equilibrio)")
    if len(ruta) < MIN_NODOS_COMPLETA:
        faltantes.append("mas profundidad en el recorrido")
    return {
        "es_completa": es_completa,
        "tiene_accion_clientes": tiene_accion,
        "tiene_viabilidad_economica": tiene_viabilidad,
        "num_nodos": len(ruta),
        "familias_faltantes": faltantes,
    }


def main():
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))["nodos"]
    families = clasificar_grafo(graph)
    FAMILIES_PATH.write_text(json.dumps(families, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for f in families.values():
        counts[f] = counts.get(f, 0) + 1
    print(f"Guardado: {FAMILIES_PATH}  ({len(families)} nodos)")
    for fam, n in sorted(counts.items()):
        print(f"  {fam}: {n}")


if __name__ == "__main__":
    main()
