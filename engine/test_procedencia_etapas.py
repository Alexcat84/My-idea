# -*- coding: utf-8 -*-
"""Fase 3.1 (caja de vidrio): _verificar_procedencia_etapas debe aceptar
ids declarados que SI vienen del material real (ruta+cosecha) y marcar
'procedencia_invalida' cuando el redactor declara un id inventado."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

eventos = []
pm._verificar_procedencia_etapas(
    {"etapas": {"1": ["a", "b"], "2": ["c"]}}, ["a", "b"], ["c"],
    registrar_evento=lambda e: eventos.append(e),
)
assert eventos == [], f"no deberia emitir nada si todos los ids son validos, emitio: {eventos}"
print("Caso 1 OK: ids validos, sin eventos.")

eventos2 = []
pm._verificar_procedencia_etapas(
    {"etapas": {"1": ["a", "id_inventado"]}}, ["a"], [],
    registrar_evento=lambda e: eventos2.append(e),
)
assert len(eventos2) == 1, f"se esperaba exactamente 1 evento, hubo {len(eventos2)}"
assert eventos2[0] == {"tipo": "procedencia_invalida", "etapa": "1", "ids_invalidos": ["id_inventado"]}, eventos2[0]
print("Caso 2 OK: id inventado detectado ->", eventos2[0])

eventos3 = []
pm._verificar_procedencia_etapas(None, ["a"], [], registrar_evento=lambda e: eventos3.append(e))
pm._verificar_procedencia_etapas({"familias_tratadas": ["accion_clientes"]}, ["a"], [], registrar_evento=lambda e: eventos3.append(e))
assert eventos3 == [], "sin autodeclaracion o sin 'etapas' (respaldo por encabezados) no debe emitir nada"
print("Caso 3 OK: sin autodeclaracion / sin 'etapas', sin eventos.")

print("\nTODO OK: verificacion de procedencia por etapa (Fase 3.1) funciona en ambos casos.")
