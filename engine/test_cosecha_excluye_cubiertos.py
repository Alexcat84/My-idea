# -*- coding: utf-8 -*-
"""Ciclo de replanteamiento, Fase 2 (decision del fundador, 27 sep 2026):
cosechar_vecindario excluye los conceptos que el proyecto YA cubrio en
sesiones anteriores, como promete la regla 8 de SYSTEM_PLAN ("el material que
recibes ya excluye lo cubierto"). Antes solo excluia la ruta actual.

Esperado calculado a mano sobre un mini-grafo: a -> {b, c}, los tres del
nucleo y de la misma fase. Sin exclusion la cosecha da {b, c}; con b cubierto,
solo [c]."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm


def nodo(sig, prev):
    return {"titulo_concepto": "x", "resumen_teorico": "", "fase_proyecto": "ideacion",
            "condiciones_activacion": [], "nodos_siguientes": sig, "nodos_previos": prev}


graph = {"a": nodo(["b", "c"], []), "b": nodo([], ["a"]), "c": nodo([], ["a"])}
families = {"a": "general", "b": "general", "c": "general"}
evaluacion = {"tiene_accion_clientes": True, "tiene_viabilidad_economica": True}

sin = pm.cosechar_vecindario(["a"], graph, families, evaluacion, None)
assert sorted(sin) == ["b", "c"], sin
print("Caso 1 OK: sin exclusion, los dos vecinos ->", sorted(sin))

con = pm.cosechar_vecindario(["a"], graph, families, evaluacion, None, excluir={"b"})
assert con == ["c"], con
print("Caso 2 OK: con b ya cubierto, solo c ->", con)

print("\nTODO OK: la cosecha excluye lo ya cubierto.")
