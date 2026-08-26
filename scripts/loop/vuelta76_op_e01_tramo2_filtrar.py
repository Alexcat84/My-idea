"""VUELTA 76, TAREA 2.3.a y 2.3.b: recalibra la bolsa (ya corrido aparte con
scripts/plan/paso_contra_nodo_calibrado.py, fresco en esta vuelta porque el
grafo se movio con la reversion de 1.3.a) y aplica el FILTRO DE ELEGIBILIDAD
P.9.1 ANTES de leer nada: cruza madre e hijo de cada candidato SIN ARISTA
contra el campo `eliminar` de las 71 operaciones de OPERACIONES.jsonl (todas
en estado LISTA, ninguna ejecutada).

Publica cuantos candidatos aparta el filtro y por que operacion, y escribe la
bolsa YA FILTRADA en orden de archivo (sin sorteo) para que el tramo 2 lea su
cabeza.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BOLSA = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"


def main():
    filas = [json.loads(l) for l in BOLSA.read_text(encoding="utf-8").splitlines() if l.strip()]
    sin_arista = [f for f in filas if not f["arista"]]
    print(f"BOLSA REDUCIDA TOTAL: {len(filas)}")
    print(f"SIN ARISTA (candidatos): {len(sin_arista)}")

    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    no_ejecutadas = [op for op in ops if op["estado"] != "HECHA"]
    condenado_por = {}
    for op in no_ejecutadas:
        for nid in op.get("eliminar") or []:
            condenado_por.setdefault(nid, []).append(op["id_op"])

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

    print(f"APARTADOS POR P.9.1: {len(apartados)}")
    for fila, motivos in apartados:
        print(f"  {fila['madre']} -> {fila['hijo']}: {'; '.join(motivos)}")
    print(f"LIMPIOS TRAS EL FILTRO, en orden de archivo: {len(limpios)}")

    salida = RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl"
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
