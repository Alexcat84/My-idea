"""VUELTA 78, TAREA 4: dossier de los primeros 30 candidatos limpios de
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl, con: el paso senalado por
el calibrador, el resumen y pasos_accionables de madre e hijo, el veredicto
propio si lo hay (docs/INTRA_DOMINIO_VEREDICTOS.jsonl), y si los dos caen en
el mismo racimo declarado (docs/RACIMOS_MIEMBROS.jsonl). Solo junta datos
para lectura, no decide.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
RACIMOS = RAIZ / "docs" / "RACIMOS_MIEMBROS.jsonl"
NODOS = RAIZ / "dataset" / "nodos"


def cargar(nid):
    return json.load(open(NODOS / f"{nid}.json", encoding="utf-8"))


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()][:30]
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

    for i, fila in enumerate(filas):
        madre_id, hijo_id, paso = fila["madre"], fila["hijo"], fila["paso"]
        madre = cargar(madre_id)
        hijo = cargar(hijo_id)
        v = veredictos.get(frozenset((madre_id, hijo_id)))
        mismo_racimo = set(racimo_de.get(madre_id, [])) & set(racimo_de.get(hijo_id, []))

        print("=" * 100)
        print(f"[{i}] {madre_id} -> {hijo_id}  (dominio {fila['dominio']}, paso senalado {paso})")
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
