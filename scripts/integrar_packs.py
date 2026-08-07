# -*- coding: utf-8 -*-
"""
integrar_packs.py — Fase 3.5 (bloque 4): la LÍNEA DE ENSAMBLAJE que
convierte los packs saneados (P1-HSEQ, tag hseq-sanitized-v1) en parte
del universo recorrible del motor.

PREREQUISITO HUMANO BLOQUEANTE: packs/<dominio>/metadata/bridges_aprobados.json
para CADA pack pendiente (el usuario aprueba 10-15 puentes por dominio desde
bridges_propuestos.json; regla: ningún nodo core ancla más de 2-3 puentes
por dominio). Sin esos archivos, este script se niega a correr.

v1.3.2: los packs se descubren de packs/*/nodos (data-driven, nada hardcodeado);
los ya integrados (HSEQ, fase 3.5) se detectan porque sus nodos viven en
dataset/nodos/ y se saltan — congelados.

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
DATASET_NODOS = BASE / "dataset" / "nodos"
MASTER_GRAPH = BASE / "dataset" / "metadata" / "master_graph.json"


def descubrir_packs():
    """v1.3.2: los packs se descubren de packs/*/nodos (nada hardcodeado) y se
    separan en ya-integrados (todos sus nodos viven en dataset/nodos, p.ej. los
    HSEQ de la fase 3.5, congelados) y pendientes. Un estado parcial es un bug.
    """
    integrados, pendientes = [], []
    for carpeta in sorted(p for p in (BASE / "packs").iterdir() if (p / "nodos").is_dir()):
        nodos = sorted((carpeta / "nodos").glob("*.json"))
        if not nodos:
            continue
        en_dataset = sum(1 for n in nodos if (DATASET_NODOS / n.name).exists())
        if en_dataset == len(nodos):
            integrados.append(carpeta.name)
        elif en_dataset == 0:
            pendientes.append(carpeta.name)
        else:
            fallar(
                f"pack '{carpeta.name}' en estado PARCIAL: {en_dataset}/{len(nodos)} nodos "
                "ya están en dataset/nodos/ — integración a medias, revisar antes de seguir"
            )
    return integrados, pendientes


def fallar(msg):
    print(f"\nERROR: {msg}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Reanudación POR PASO.
#
# La avería de origen (2026-08-07, integrando compras y entrega): el paso (a)
# copió los nodos a dataset/ y el paso (e) fallo. Al reintentar, descubrir_packs
# vio los nodos ya en dataset/, declaro los packs "ya integrados" y el script
# dijo "no hay packs pendientes, nada que hacer" — con los pasos b a f sin
# correr. Salio en verde con la mitad del trabajo sin hacer.
#
# La causa es que el estado se DEDUCIA de un efecto de un solo paso. Ahora se
# ESCRIBE, paso a paso: el archivo nace antes del primero y muere despues del
# ultimo, asi que su sola existencia significa "esto quedo a medias".
# ---------------------------------------------------------------------------
ESTADO = BASE / "dataset" / "metadata" / "_integracion_en_curso.json"

PASOS = [
    "a_nodos_y_puentes", "e_gate0", "e_bis_etiquetas", "b_familias",
    "c_cache_preguntas", "d_indice_voyage", "f_sync", "f_suite_web", "f_suite_python",
]


def pasos_pendientes(estado):
    hechos = set((estado or {}).get("hechos", []))
    return [p for p in PASOS if p not in hechos]


def decidir_accion(estado, pendientes):
    """Que hacer, en una funcion pura y testeable.

    Devuelve ('reanudar', faltan) | ('integrar', packs) | ('nada', []).
    NUNCA devuelve 'nada' habiendo trabajo a medias: ese era el bug.
    """
    if estado:
        faltan = pasos_pendientes(estado)
        if faltan:
            return "reanudar", faltan
        # Archivo huerfano: todos los pasos hechos pero nadie lo borro.
        return "nada", []
    if pendientes:
        return "integrar", pendientes
    return "nada", []


def guardar_estado(estado):
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guardar_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validar_prerequisitos(packs):
    """El muro humano: bridges_aprobados.json en TODOS los packs pendientes."""
    faltantes = []
    puentes_por_dominio = {}
    for d in packs:
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
            "en bridges_aprobados.json. Este script NO corre sin el archivo de cada pack pendiente."
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


def paso_a_integrar_nodos_y_puentes(packs, puentes_por_dominio):
    """Copia los nodos de packs al dataset y teje los puentes bidireccionales."""
    print("\n=== a. Integrando nodos de packs + puentes aprobados ===")
    copiados = 0
    for d in packs:
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
    # Windows: pnpm es pnpm.cmd — subprocess sin shell no lo resuelve solo.
    ejecutable = shutil.which(cmd[0])
    if ejecutable:
        cmd = [ejecutable] + cmd[1:]
    r = subprocess.run(cmd, cwd=BASE)
    if r.returncode != 0:
        fallar(f"'{descripcion}' terminó con código {r.returncode} — línea de ensamblaje DETENIDA (revisar antes de reintentar)")


def main():
    ap = argparse.ArgumentParser()
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--dry-run", action="store_true", help="valida prerequisitos sin tocar nada")
    modo.add_argument("--ejecutar", action="store_true", help="corre la línea de ensamblaje completa")
    args = ap.parse_args()

    integrados, pendientes = descubrir_packs()
    estado = json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else None
    accion, detalle = decidir_accion(estado, pendientes)

    if integrados:
        print(f"Packs ya integrados (congelados, no se tocan): {', '.join(integrados)}")

    if accion == "nada":
        if estado:
            print(f"Todos los pasos estaban hechos; borrando {ESTADO.name} huerfano.")
            ESTADO.unlink(missing_ok=True)
        print("No hay packs pendientes de integrar. Nada que hacer.")
        return

    if accion == "reanudar":
        pendientes = estado["packs"]
        print(f"\nINTEGRACION A MEDIAS de {', '.join(pendientes)}: "
              f"{len(estado['hechos'])} pasos hechos, faltan {len(detalle)}.")
        for p in detalle:
            print(f"   pendiente: {p}")
        if args.dry_run:
            print("\n--dry-run: nada tocado. Para reanudar: python scripts/integrar_packs.py --ejecutar")
            return
        print("Se REANUDA desde el primer paso pendiente.\n")
    else:
        print(f"Packs pendientes: {', '.join(pendientes)}")

    puentes = validar_prerequisitos(pendientes)
    total_pack_nodes = sum(len(list((BASE / "packs" / d / "nodos").glob("*.json"))) for d in pendientes)
    print(f"Prerequisitos OK: puentes aprobados en {len(pendientes)} packs; {total_pack_nodes} nodos listos.")

    if args.dry_run:
        print("\n--dry-run: nada tocado. Para ejecutar: python scripts/integrar_packs.py --ejecutar")
        return

    if estado is None:
        estado = {"packs": pendientes, "hechos": [], "tocados_core": []}
        guardar_estado(estado)

    def paso(nombre, fn):
        """Corre el paso si falta; lo marca solo DESPUES de que salga bien."""
        if nombre in estado["hechos"]:
            print(f"\n=== [ya hecho, se salta] {nombre} ===")
            return
        fn()
        estado["hechos"].append(nombre)
        guardar_estado(estado)

    def _a():
        estado["tocados_core"] = sorted(paso_a_integrar_nodos_y_puentes(pendientes, puentes))
    paso("a_nodos_y_puentes", _a)

    # e-parte-1. recompilar master_graph + Gate 0 (los nodos ya están en dataset/)
    # --reaplico-curaduria: run_phase1 avisa a gritos y FALLA cuando la
    # recompilación revierte las etiquetas de cara. Aquí ese aviso sobra,
    # porque el paso siguiente (e-bis) las reaplica; sin la bandera pararía la
    # línea justo antes de arreglarlo.
    paso("e_gate0", lambda: correr(
        [sys.executable, "scripts/run_phase1.py", "--reaplico-curaduria"],
        "e. run_phase1: recompilación + Gate 0 (debe quedar VERDE)"))

    # e-parte-1b. RE-APLICAR las etiquetas de cara. Cazado el 2026-08-07
    # integrando compras y entrega: la curaduría de etiquetas parchea las dos
    # COPIAS del grafo, no los archivos de nodo, así que run_phase1 la revierte
    # cada vez que recompila el master desde dataset/nodos/. Sin este paso, una
    # integración devuelve a 71 nodos del core su jerga original ("Canvas",
    # "Pivotar", "SPIN") sin que nada se queje: el grafo queda válido y el
    # usuario ve palabras que el fundador saco de la casa hace una fase.
    #
    # ESTE PASO ES LA UNICA FUENTE DE CURADURIA DE ETIQUETAS. La capa
    # re-aplicable solo es legitima mientras sea unica: si alguien cura una
    # etiqueta en otro sitio (a mano en un nodo, en un script aparte, en el
    # espejo de la web), la proxima recompilacion revive el bug con otro
    # disfraz y ademas nadie sabra cual de las dos curadurias manda. Lo que
    # haya que curar se escribe en dataset/metadata/etiquetas_de_cara_v1*.json
    # y entra por aqui, o no entra.
    paso("e_bis_etiquetas", lambda: correr(
        [sys.executable, "scripts/etiquetas_de_cara.py", "--aplicar"],
        "e-bis. Re-aplicar las etiquetas de cara (run_phase1 las revierte)"))

    # b. familias (sin costo) — DESPUÉS de run_phase1: plan_readiness lee
    # master_graph.json, que recién queda recompilado con el grafo ampliado.
    paso("b_familias", lambda: correr(
        [sys.executable, "engine/plan_readiness.py"],
        "b. Etiquetas de familia (readiness) para el grafo ampliado"))

    # c. caché de preguntas PARCIAL: nodos de packs + cores tocados por puentes.
    # La lista va en un archivo (--patch-file): 1500+ ids exceden el límite de
    # línea de comandos de Windows.
    def _c():
        pack_ids = [p.stem for d in pendientes for p in (BASE / "packs" / d / "nodos").glob("*.json")]
        tocados_core = estado.get("tocados_core", [])
        a_parchear = pack_ids + sorted(tocados_core)
        print(f"\n  caché parcial: {len(pack_ids)} nodos de packs + {len(tocados_core)} cores con sucesores nuevos")
        patch_file = BASE / "engine" / "_patch_pendientes.txt"
        patch_file.write_text("\n".join(a_parchear) + "\n", encoding="utf-8")
        correr(
            [sys.executable, "engine/build_question_cache.py", "--patch-file", str(patch_file)],
            "c. Caché de preguntas parcial (packs + cores tocados)",
        )
        patch_file.unlink(missing_ok=True)
    paso("c_cache_preguntas", _c)

    # d. índice Voyage completo
    paso("d_indice_voyage", lambda: correr(
        [sys.executable, "scripts/build_semantic_index_voyage.py"],
        "d. Índice semántico Voyage completo"))

    # f. sync de assets a la web + suites
    paso("f_sync", lambda: correr(
        [sys.executable, "scripts/sync_assets_web.py"], "f. Sync de assets a web/lib/assets"))
    # 'run test' (script del package.json), no 'vitest run' bare: pnpm bajo
    # subprocess de Windows mal-parsea el binario suelto ("web" not found).
    paso("f_suite_web", lambda: correr(
        ["pnpm", "-C", "web", "run", "test"],
        "f. Suite web (checksums + contrato) — debe quedar verde"))
    paso("f_suite_python", lambda: correr(
        [sys.executable, "engine/run_all_tests.py"], "f. Suite python — debe quedar verde"))

    # Solo aqui, con TODOS los pasos hechos, desaparece la marca de "a medias".
    ESTADO.unlink(missing_ok=True)

    print(
        "\nLÍNEA DE ENSAMBLAJE COMPLETA. Revisar los costos reales que reportaron "
        "build_question_cache (c) y build_semantic_index_voyage (d) arriba (b es gratis, "
        "clasificador por palabras clave) e incluirlos en el reporte de fase. "
        "Recordar: commit de dataset/ + packs/ + web/lib/assets en el MISMO commit."
    )


if __name__ == "__main__":
    main()
