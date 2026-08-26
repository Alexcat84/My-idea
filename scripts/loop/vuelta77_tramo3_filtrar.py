"""VUELTA 77, TAREA 3: filtro de elegibilidad P.9.1 ENSANCHADO corrido ANTES
de leer nada, sobre la bolsa RECALIBRADA FRESCA de esta vuelta
(docs/plan/PASO_NODO_CALIBRADO.jsonl, recorrido con
scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo 72
--umbral-contencion 0.45 --umbral-tokens 4, salida en
docs/loop/SALIDA_V77_CALIBRADO_FRESCO.txt). Usa
scripts/loop/vuelta77_filtro_p91_ensanchado.py (eliminar + superviviente de
toda operacion NO EJECUTADA, MAS nodos de las RENOMBRE_CON_ALIAS).
"""
import json
import importlib.util
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

spec = importlib.util.spec_from_file_location(
    "vuelta77_filtro_p91_ensanchado",
    RAIZ / "scripts" / "loop" / "vuelta77_filtro_p91_ensanchado.py",
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()]
    sin_arista = [f for f in filas if not f["arista"]]
    print(f"BOLSA REDUCIDA TOTAL: {len(filas)}")
    print(f"SIN ARISTA (candidatos): {len(sin_arista)}")

    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    condenado_por = mod.condenados_por_operacion(ops)

    apartados = []
    limpios = []
    for fila in sin_arista:
        motivos = []
        if fila["madre"] in condenado_por:
            motivos.append(f"madre condenada por {condenado_por[fila['madre']]}")
        if fila["hijo"] in condenado_por:
            motivos.append(f"hijo condenado por {condenado_por[fila['hijo']]}")
        if motivos:
            apartados.append((fila, motivos))
        else:
            limpios.append(fila)

    print(f"APARTADOS POR P.9.1 ENSANCHADO: {len(apartados)}")
    for fila, motivos in apartados:
        print(f"  {fila['madre']} -> {fila['hijo']}: {'; '.join(motivos)}")
    print(f"LIMPIOS TRAS EL FILTRO, en orden de archivo: {len(limpios)}")

    salida = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V77.jsonl"
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
