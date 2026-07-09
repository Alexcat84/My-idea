#!/usr/bin/env python3
"""Paso 0: censo y anomalias. Concilia conteos, encuentra nodos sin dominio
o con dominio incorrecto, y archivos no-JSON colados. Solo REPORTA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import BASE, CATEGORIAS, cargar_dominio, dir_nodos

total = 0
problemas = 0
for cat, clave in CATEGORIAS.items():
    todos = list(dir_nodos(cat).iterdir())
    jsons = [f for f in todos if f.suffix == ".json"]
    extras = [f.name for f in todos if f.suffix != ".json"]
    nodos = cargar_dominio(cat)
    total += len(nodos)
    sin_dominio = [i for i, d in nodos.items() if "dominio" not in d]
    mal_dominio = [i for i, d in nodos.items() if d.get("dominio") not in (None, clave)]
    sin_titulo = [i for i, d in nodos.items() if not d.get("titulo")]
    print(f"\n== {cat} (esperado dominio='{clave}') ==")
    print(f"  archivos: {len(todos)} | json: {len(jsons)} | otros: {extras or 'ninguno'}")
    print(f"  sin campo dominio: {sin_dominio or 'ninguno'}")
    print(f"  dominio incorrecto: {mal_dominio or 'ninguno'}")
    print(f"  sin titulo: {sin_titulo or 'ninguno'}")
    problemas += len(sin_dominio) + len(mal_dominio) + len(sin_titulo)
print(f"\nTOTAL nodos JSON: {total}")
print("ACCION: estampar dominio a los 'sin campo' si son nodos legitimos;")
print("mover a metadata/ cualquier archivo que no sea un nodo.")
sys.exit(1 if problemas else 0)
