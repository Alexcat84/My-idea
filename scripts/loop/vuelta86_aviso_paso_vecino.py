# -*- coding: utf-8 -*-
"""vuelta86_aviso_paso_vecino.py . TAREA 2.d de la vuelta 86 (adjudicacion 5.7
del acta 85), LA PIEZA BARATA QUE NO ES DOCTRINA.

POR QUE NACE. Los caveats de paso ya llevan tres unidades anotadas sin
adjudicar (el par 64, acta 84 6.7; el 73 y el 101 de la vuelta 85; mas el 94):
en los cuatro, la unidad trae un paso de la madre, pero OTRO paso de esa misma
madre nombra al hijo con MAS literalidad que el paso que la unidad trae, y esa
lectura alternativa dependia de que el lector se acordara solo. Esto NO
adjudica nada ni cambia ninguna clase: solo pone la alternativa delante.

LA HEURISTICA ELEGIDA (dila si no convence, esta vuelta la publica): para cada
unidad (madre, hijo, paso i, titulo_ratio de esa fila en el calibrado), se
recomputa `rapidfuzz.fuzz.token_set_ratio` del titulo del hijo contra CADA
paso de `pasos_accionables` de la madre (la MISMA senal 1 que
scripts/plan/paso_contra_nodo_calibrado.py usa para decidir si un paso nombra
a un hijo, sobre `norm()` de scripts/paso_contra_nodo.py, sin recalcular
contencion ni familia de verbo: esas dos son las OTRAS dos senales del
calibrado y no las que "literalidad" nombra aqui). Si algun paso j != i tiene
un ratio ESTRICTAMENTE MAYOR que el de la fila (con margen minimo
AVISO_MARGEN, para no avisar por empates de redondeo), se avisa: "el paso J
nombra al hijo con mas literalidad (ratio X contra Y del paso actual)".

FALSOS POSITIVOS CONOCIDOS, publicados y no callados: la heuristica compara
SOLO titulo_ratio (nombrar), no contencion (vocabulario) ni familia de verbo
(accion). Un paso puede nombrar al hijo con un ratio alto y aun asi ser un
paso que SOLO LO MENCIONA DE PASADA (p. ej. "revisa el resultado de <hijo>
antes de seguir"), mientras el paso que la unidad trae es el que REALMENTE lo
desarrolla con vocabulario compartido. El aviso no distingue esos dos casos:
por eso NO DECIDE, solo avisa, y el lector tiene que leer los dos pasos antes
de fiarse del ratio mas alto.
"""
import json
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

AVISO_MARGEN = 3.0  # puntos de token_set_ratio por encima del paso actual para avisar

_cache_grafo = None


def _cargar_grafo():
    global _cache_grafo
    if _cache_grafo is None:
        _cache_grafo = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    return _cache_grafo


def _norm(texto):
    """Copia minima de scripts/paso_contra_nodo.py:norm() (quita acentos,
    minuscula, colapsa espacio): se copia y no se importa para que este
    instrumento de aviso no dependa de que el original no cambie su firma."""
    t = unicodedata.normalize("NFKD", texto or "")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def aviso_paso_vecino(madre, hijo, paso_actual, titulo_ratio_actual):
    """Devuelve None si ningun otro paso de MADRE nombra a HIJO con mas
    literalidad que PASO_ACTUAL, o un texto de aviso si lo hay. NO decide
    nada: es informativo. paso_actual es 1-based, igual que el campo "paso"
    del calibrado."""
    from rapidfuzz.fuzz import token_set_ratio

    G = _cargar_grafo()
    n_madre = G.get(madre) or {}
    n_hijo = G.get(hijo) or {}
    pasos = n_madre.get("pasos_accionables") or []
    if not pasos or paso_actual is None:
        return None
    titulo_hijo_norm = _norm(n_hijo.get("titulo_concepto") or "")
    if not titulo_hijo_norm:
        return None

    mejor_idx, mejor_ratio = None, None
    for i, paso_texto in enumerate(pasos, 1):
        if i == paso_actual:
            continue
        ratio = token_set_ratio(_norm(paso_texto), titulo_hijo_norm)
        if mejor_ratio is None or ratio > mejor_ratio:
            mejor_idx, mejor_ratio = i, ratio

    if mejor_idx is None:
        return None
    if titulo_ratio_actual is None or mejor_ratio > titulo_ratio_actual + AVISO_MARGEN:
        return ("CAVEAT DE PASO: el paso %d de %s nombra a %s con MAS literalidad "
                "(ratio %.1f) que el paso %d que esta unidad trae (ratio %.1f)"
                % (mejor_idx, madre, hijo, mejor_ratio, paso_actual, titulo_ratio_actual))
    return None
