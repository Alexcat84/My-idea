# -*- coding: utf-8 -*-
"""
integrar_packs.py — Fase 3.5 (bloque 4): la LÍNEA DE ENSAMBLAJE que
convierte los packs saneados (P1-HSEQ, tag hseq-sanitized-v1) en parte
del universo recorrible del motor.

PREREQUISITO HUMANO BLOQUEANTE: packs/<dominio>/metadata/bridges_aprobados.json
para LOS TRES dominios (el usuario aprueba 10-15 puentes por dominio desde
bridges_propuestos.json; regla: ningún nodo core ancla más de 2-3 puentes
por dominio). Sin los tres archivos, este script se niega a correr.

Secuencia (plan de fase, puntos a-f):
  a. Compilar master_graph con core + packs + puentes aprobados
     (bidireccionales: alta el hijo en nodos_siguientes del padre y el
     padre en nodos_previos del hijo, en los archivos fuente).
  b. Etiquetado de familias (etiqueta del árbol de readiness) para los
     nodos de packs: engine/plan_readiness.py — mismo clasificador por
     palabras clave del core, sin costo de API.
  c. Caché de preguntas PARCIAL: engine/build_question_cache.py --patch
     con los nodos de packs + los nodos core cuyos sucesores cambiaron
     por puentes (los únicos cuyo contexto de pregunta cambió).
  d. Índice semántico Voyage COMPLETO (~2805 nodos):
     scripts/build_semantic_index_voyage.py.
  e. scripts/run_phase1.py con dominios ampliados — Gate 0 debe quedar
     VERDE (0 rotos, 1 componente, cobertura del componente principal).
  f. scripts/sync_assets_web.py + suites web (checksums de prompts y
     contrato) verdes.
Reporta costos reales de b+c+d (b es gratis; c y d llaman APIs).

Uso:
  python scripts/integrar_packs.py --dry-run   # valida prerequisitos sin tocar nada
  python scripts/integrar_packs.py --ejecutar  # corre la línea completa
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PACKS = ["quality", "health_safety", "environmental"]
DATASET_NODOS = BASE / "dataset" / "nodos"
MASTER_GRAPH = BASE / "dataset" / "metadata" / "master_graph.json"


def fallar(msg):
    print(f"\nERROR: {msg}")
    sys.exit(1)


def cargar_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guardar_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validar_prerequisitos():
    """El muro humano: bridges_aprobados.json en los TRES dominios."""
    faltantes = []
    puentes_por_dominio = {}
    for d in PACKS:
        ruta = BASE / "packs" / d / "metadata" / "bridges_aprobados.json"
        if not ruta.exists():
            faltantes.append(str(ruta.relative_to(BASE)))
            continue
        puentes = cargar_json(ruta)
        # Forma aprobada por el usuario: {"nota": ..., "aprobados": [pares]}.
        # La nota viaja en el archivo; aquí solo consumimos los pares.
        if isinstance(puentes, dict) and isinstance(puentes.get("aprobados"), list):
            puentes = puentes["aprobados"]
        if not isinstance(puentes, list) or len(puentes) == 0:
            fallar(f"{ruta.name} de '{d}' está vacío o no es una lista (ni {{nota, aprobados}})")
        puentes_por_dominio[d] = puentes
    if faltantes:
        fallar(
            "PREREQUISITO HUMANO PENDIENTE — faltan las aprobaciones de puentes:\n  - "
            + "\n  - ".join(faltantes)
            + "\nEl usuario debe aprobar 10-15 puentes por dominio desde bridges_propuestos.json "
            "(regla: ningún nodo core ancla más de 2-3 puentes por dominio) y guardar la selección "
            "en bridges_aprobados.json. Este script NO corre sin los tres archivos."
        )
    # Regla de concentración: ningún nodo core ancla más de 3 puentes por dominio.
    # Formato esperado (el de bridges_propuestos.json['candidatos']):
    # {"core": <id core>, "dominio": <id del nodo del pack>, "score": ...}
    for d, puentes in puentes_por_dominio.items():
        conteo = {}
        for p in puentes:
            core = p.get("core")
            if not core:
                fallar(f"puente sin campo 'core' en '{d}': {json.dumps(p, ensure_ascii=False)[:120]}")
            conteo[core] = conteo.get(core, 0) + 1
        excedidos = {k: v for k, v in conteo.items() if v > 3}
        if excedidos:
            fallar(f"'{d}': nodos core anclando más de 3 puentes (regla del plan): {excedidos}")
        if not (5 <= len(puentes) <= 20):
            print(f"  AVISO: '{d}' tiene {len(puentes)} puentes (esperado 10-15±) — verificar que es intencional.")
    return puentes_por_dominio


def paso_a_integrar_nodos_y_puentes(puentes_por_dominio):
    """Copia los nodos de packs al dataset y teje los puentes bidireccionales."""
    print("\n=== a. Integrando nodos de packs + puentes aprobados ===")
    copiados = 0
    for d in PACKS:
        origen = BASE / "packs" / d / "nodos"
        for archivo in sorted(origen.glob("*.json")):
            destino = DATASET_NODOS / archivo.name
            if destino.exists():
                fallar(f"colisión de node_id entre core y '{d}': {archivo.name} ya existe en dataset/nodos/")
            shutil.copy2(archivo, destino)
            copiados += 1
    print(f"  {copiados} nodos de packs copiados a dataset/nodos/.")

    tejidos = 0
    tocados_core = set()
    for d, puentes in puentes_por_dominio.items():
        for p in puentes:
            core_id = p.get("core")
            pack_id = p.get("dominio")  # así llama bridges_propuestos al nodo del pack
            if not pack_id:
                fallar(f"puente sin campo 'dominio' (nodo del pack) en '{d}': {json.dumps(p, ensure_ascii=False)[:120]}")
            ruta_core = DATASET_NODOS / f"{core_id}.json"
            ruta_pack = DATASET_NODOS / f"{pack_id}.json"
            if not ruta_core.exists() or not ruta_pack.exists():
                fallar(f"puente {core_id} -> {pack_id}: alguno de los dos no existe en dataset/nodos/")
            nodo_core = cargar_json(ruta_core)
            nodo_pack = cargar_json(ruta_pack)
            if pack_id not in nodo_core.get("nodos_siguientes", []):
                nodo_core.setdefault("nodos_siguientes", []).append(pack_id)
            if core_id not in nodo_pack.get("nodos_previos", []):
                nodo_pack.setdefault("nodos_previos", []).append(core_id)
            guardar_json(ruta_core, nodo_core)
            guardar_json(ruta_pack, nodo_pack)
            tejidos += 1
            tocados_core.add(core_id)
    print(f"  {tejidos} puentes tejidos (bidireccionales) sobre {len(tocados_core)} nodos core.")
    return tocados_core


def correr(cmd, descripcion):
    print(f"\n=== {descripcion} ===\n  $ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=BASE)
    if r.returncode != 0:
        fallar(f"'{descripcion}' terminó con código {r.returncode} — línea de ensamblaje DETENIDA (revisar antes de reintentar)")


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--dry-run", action="store_true", help="valida prerequisitos sin tocar nada")
    modo.add_argument("--ejecutar", action="store_true", help="corre la línea de ensamblaje completa")
    args = ap.parse_args()

    puentes = validar_prerequisitos()
    total_pack_nodes = sum(len(list((BASE / "packs" / d / "nodos").glob("*.json"))) for d in PACKS)
    print(f"Prerequisitos OK: puentes aprobados en los 3 dominios; {total_pack_nodes} nodos de packs listos.")

    if args.dry_run:
        print("\n--dry-run: nada tocado. Para ejecutar: python scripts/integrar_packs.py --ejecutar")
        return

    tocados_core = paso_a_integrar_nodos_y_puentes(puentes)

    # e-parte-1. recompilar master_graph + Gate 0 (los nodos ya están en dataset/)
    correr([sys.executable, "scripts/run_phase1.py"], "e. run_phase1: recompilación + Gate 0 (debe quedar VERDE)")

    # b. familias (sin costo) — DESPUÉS de run_phase1: plan_readiness lee
    # master_graph.json, que recién queda recompilado con el grafo ampliado.
    correr([sys.executable, "engine/plan_readiness.py"], "b. Etiquetas de familia (readiness) para el grafo ampliado")

    # c. caché de preguntas PARCIAL: nodos de packs + cores tocados por puentes.
    # La lista va en un archivo (--patch-file): 1500+ ids exceden el límite de
    # línea de comandos de Windows.
    pack_ids = [p.stem for d in PACKS for p in (BASE / "packs" / d / "nodos").glob("*.json")]
    a_parchear = pack_ids + sorted(tocados_core)
    print(f"\n  caché parcial: {len(pack_ids)} nodos de packs + {len(tocados_core)} cores con sucesores nuevos")
    patch_file = BASE / "engine" / "_patch_pendientes.txt"
    patch_file.write_text("\n".join(a_parchear) + "\n", encoding="utf-8")
    correr(
        [sys.executable, "engine/build_question_cache.py", "--patch-file", str(patch_file)],
        "c. Caché de preguntas parcial (packs + cores tocados)",
    )
    patch_file.unlink(missing_ok=True)

    # d. índice Voyage completo
    correr([sys.executable, "scripts/build_semantic_index_voyage.py"], "d. Índice semántico Voyage completo")

    # f. sync de assets a la web + suites
    correr([sys.executable, "scripts/sync_assets_web.py"], "f. Sync de assets a web/lib/assets")
    correr(["pnpm", "-C", "web", "vitest", "run"], "f. Suite web (checksums + contrato) — debe quedar verde")
    correr([sys.executable, "engine/run_all_tests.py"], "f. Suite python — debe quedar verde")

    print(
        "\nLÍNEA DE ENSAMBLAJE COMPLETA. Revisar los costos reales que reportaron "
        "build_question_cache (c) y build_semantic_index_voyage (d) arriba (b es gratis, "
        "clasificador por palabras clave) e incluirlos en el reporte de fase. "
        "Recordar: commit de dataset/ + packs/ + web/lib/assets en el MISMO commit."
    )


if __name__ == "__main__":
    main()
