# -*- coding: utf-8 -*-
"""Expansión v1.3 — validador de esquema (RUNBOOK §1, corregido contra el
código real). Lista blanca de campos del esquema VIGENTE de los 2805 nodos,
obligatorios no vacíos, ids ascii en minúscula. Solo REPORTA (exit 1 si hay
fallas); los arreglos se hacen con scripts dedicados y registro.

Uso:
  python scripts/expansion/validar_esquema.py <carpeta_de_nodos> [...]
"""
import json
import re
import sys
from pathlib import Path

# Esquema vigente (verificado contra dataset/nodos y master_graph 2026-07-11).
CAMPOS_PERMITIDOS = {
    "node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
    "resumen_teorico", "pasos_accionables", "entregable_esperado",
    "nodos_previos", "nodos_siguientes", "condiciones_activacion",
    # legado del saneamiento (paso1 ascii) y estándar nuevo v1.3:
    "ids_alias", "etiqueta_arbol",
}
OBLIGATORIOS_NO_VACIOS = {
    "node_id", "fase_proyecto", "dominio", "titulo_concepto", "fuente",
    "resumen_teorico", "pasos_accionables", "entregable_esperado",
    "condiciones_activacion",
}
FASES_VALIDAS = {"ideacion", "validacion", "planificacion", "ejecucion"}
RE_ID = re.compile(r"^[a-z0-9_]+$")


def validar_carpeta(carpeta: Path):
    fallas = []
    archivos = sorted(carpeta.glob("*.json"))
    nodos = [a for a in archivos if not a.name.startswith("_")]
    for a in nodos:
        try:
            d = json.loads(a.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fallas.append((a.name, f"JSON inválido: {e}"))
            continue
        extras = set(d.keys()) - CAMPOS_PERMITIDOS
        if extras:
            fallas.append((a.name, f"campos fuera de la lista blanca: {sorted(extras)}"))
        for campo in OBLIGATORIOS_NO_VACIOS:
            v = d.get(campo)
            if v is None or (isinstance(v, str) and not v.strip()) or (isinstance(v, list) and not v):
                fallas.append((a.name, f"obligatorio vacío o ausente: {campo}"))
        nid = d.get("node_id", "")
        if not RE_ID.match(nid or ""):
            fallas.append((a.name, f"node_id no ascii-minúscula: {nid!r}"))
        if nid and nid != a.stem:
            fallas.append((a.name, f"node_id != nombre de archivo ({nid})"))
        if d.get("fase_proyecto") not in FASES_VALIDAS:
            fallas.append((a.name, f"fase_proyecto inválida: {d.get('fase_proyecto')!r}"))
        for campo in ("pasos_accionables", "nodos_previos", "nodos_siguientes", "condiciones_activacion"):
            if campo in d and not isinstance(d[campo], list):
                fallas.append((a.name, f"{campo} debe ser lista"))
    return len(nodos), fallas


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    total_fallas = 0
    for arg in sys.argv[1:]:
        carpeta = Path(arg)
        n, fallas = validar_carpeta(carpeta)
        print(f"\n== {carpeta} : {n} nodos, {len(fallas)} falla(s)")
        for nombre, msg in fallas[:60]:
            print(f"  {nombre}: {msg}")
        if len(fallas) > 60:
            print(f"  ... y {len(fallas) - 60} más")
        total_fallas += len(fallas)
    sys.exit(1 if total_fallas else 0)


if __name__ == "__main__":
    main()
