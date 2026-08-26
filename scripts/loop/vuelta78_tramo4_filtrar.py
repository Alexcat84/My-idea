"""VUELTA 78, TAREA 4: filtro de elegibilidad P.9.1 ENSANCHADO CON LA VARA DE
LOS A, corrido ANTES de leer nada, sobre la bolsa RECALIBRADA FRESCA de esta
vuelta (docs/plan/PASO_NODO_CALIBRADO.jsonl, recorrido con
scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo 72
--umbral-contencion 0.45 --min-tokens 4, salida en
docs/loop/SALIDA_V78_CALIBRADO_FRESCO.txt). Usa
scripts/loop/vuelta78_filtro_p91_vara_a.py (eliminar + superviviente + nodos
de RENOMBRE_CON_ALIAS, MAS veredictos A vivos del cribado).
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

sys.path.insert(0, str(RAIZ / "scripts" / "loop"))
from vuelta78_filtro_p91_vara_a import filtrar_candidatos, cargar_vivos  # noqa: E402


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()]
    sin_arista = [f for f in filas if not f["arista"]]
    print(f"BOLSA REDUCIDA TOTAL: {len(filas)}")
    print(f"SIN ARISTA (candidatos): {len(sin_arista)}")

    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    veredictos = [json.loads(l) for l in VEREDICTOS.read_text(encoding="utf-8").splitlines() if l.strip()]
    vivos = cargar_vivos()

    candidatos = [{"madre": f["madre"], "hijo": f["hijo"]} for f in sin_arista]
    limpios_c, apartados_c = filtrar_candidatos(candidatos, ops, veredictos, vivos)
    apartado_keys = {(c["madre"], c["hijo"]): motivos for c, motivos in apartados_c}

    apartados = [(f, apartado_keys[(f["madre"], f["hijo"])]) for f in sin_arista
                 if (f["madre"], f["hijo"]) in apartado_keys]
    limpios = [f for f in sin_arista if (f["madre"], f["hijo"]) not in apartado_keys]

    apartados_por_op = [f for f, m in apartados if any("operacion" in x for x in m) and not any("veredicto A" in x for x in m)]
    apartados_por_a = [f for f, m in apartados if any("veredicto A" in x for x in m)]

    print(f"APARTADOS POR P.9.1 ENSANCHADO (operaciones + vara de los A): {len(apartados)}")
    print(f"  de esos, SOLO por operacion (eliminar/superviviente/nodos): {len(apartados_por_op)}")
    print(f"  de esos, con al menos un motivo de la vara de los A: {len(apartados_por_a)}")
    for fila, motivos in apartados:
        print(f"  {fila['madre']} -> {fila['hijo']}: {'; '.join(motivos)}")
    print(f"LIMPIOS TRAS EL FILTRO, en orden de archivo: {len(limpios)}")

    salida = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl"
    with open(salida, "w", encoding="utf-8") as f:
        for fila in limpios:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print(f"ESCRITO: {salida.relative_to(RAIZ)}")

    print()
    print("CABEZA DE LA BOLSA FILTRADA, primeros 30, en orden de archivo:")
    for i, fila in enumerate(limpios[:30]):
        print(f"  {i}: {fila['madre']} -> {fila['hijo']} (paso {fila['paso']}, dominio {fila['dominio']})")


if __name__ == "__main__":
    main()
