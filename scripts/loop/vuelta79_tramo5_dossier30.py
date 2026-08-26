# -*- coding: utf-8 -*-
"""VUELTA 79, TAREA 5 punto 3: dossier de las primeras 30 UNIDADES de lectura
(guarda del par no dirigido aplicada) de
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl, con: el paso senalado por
el calibrador, el resumen y pasos_accionables de madre e hijo, el veredicto
propio si lo hay, y si los dos caen en el mismo racimo declarado. Solo junta
datos para lectura, no decide.
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
RACIMOS = RAIZ / "docs" / "RACIMOS_MIEMBROS.jsonl"
NODOS = RAIZ / "dataset" / "nodos"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta79_guarda_par_no_dirigido import agrupar_por_par_no_dirigido  # noqa: E402


def cargar(nid):
    return json.load(open(NODOS / f"{nid}.json", encoding="utf-8"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    limpios = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()]
    parejas, sueltas = agrupar_por_par_no_dirigido(limpios)
    pos = {id(f): i for i, f in enumerate(limpios)}
    unidades = []
    for grupo in parejas:
        unidades.append((min(pos[id(f)] for f in grupo), grupo))
    for f in sueltas:
        unidades.append((pos[id(f)], [f]))
    unidades.sort(key=lambda u: u[0])
    unidades = unidades[:30]

    veredictos = {}
    for l in VEREDICTOS.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        v = json.loads(l)
        veredictos.setdefault(frozenset((v["nodo_a"], v["nodo_b"])), v)
    racimos = [json.loads(l) for l in RACIMOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    racimo_de = {}
    for r in racimos:
        nombre = r.get("nombre") or r.get("id")
        for m in r.get("miembros", []):
            racimo_de.setdefault(m.get("node_id"), []).append(nombre)

    for i, (_, grupo) in enumerate(unidades):
        etiqueta_pareja = " [PAREJA, guarda del par no dirigido]" if len(grupo) > 1 else ""
        for fila in grupo:
            madre_id, hijo_id, paso = fila["madre"], fila["hijo"], fila["paso"]
            madre = cargar(madre_id)
            hijo = cargar(hijo_id)
            v = veredictos.get(frozenset((madre_id, hijo_id)))
            mismo_racimo = set(racimo_de.get(madre_id, [])) & set(racimo_de.get(hijo_id, []))

            print("=" * 100)
            print(f"[{i}]{etiqueta_pareja} {madre_id} -> {hijo_id}  (dominio {fila['dominio']}, paso senalado {paso})")
            if v:
                print(f"  veredicto propio: puesto {v['puesto_intra']}, clase {v['clase']}: {v['razon'][:200]}")
            else:
                print("  veredicto propio: NINGUNO")
            print(f"  mismo racimo declarado: {sorted(mismo_racimo) if mismo_racimo else 'NO'}")
            print(f"  MADRE ({madre_id}), fuente: {madre.get('fuente')}")
            print(f"    resumen: {madre.get('resumen_teorico')}")
            pasos_m = madre.get("pasos_accionables") or []
            for j, p in enumerate(pasos_m, 1):
                marcador = " <== SENALADO" if j == paso else ""
                texto = p if isinstance(p, str) else p.get("texto") or p.get("paso") or str(p)
                print(f"    paso {j}: {texto}{marcador}")
            print(f"  HIJO ({hijo_id}), fuente: {hijo.get('fuente')}")
            print(f"    resumen: {hijo.get('resumen_teorico')}")
            pasos_h = hijo.get("pasos_accionables") or []
            for j, p in enumerate(pasos_h, 1):
                texto = p if isinstance(p, str) else p.get("texto") or p.get("paso") or str(p)
                print(f"    paso {j}: {texto}")
            print()


if __name__ == "__main__":
    main()
