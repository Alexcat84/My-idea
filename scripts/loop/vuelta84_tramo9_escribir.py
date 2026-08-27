# -*- coding: utf-8 -*-
"""VUELTA 84, TAREA 3: escribe en dataset/nodos/*.json las aristas decididas
ESCRITA de las 30 unidades frescas del tramo 9 (indices 48 a 77 de la bolsa
filtrada V84), en las DOS vistas a la vez, con chequeo de escalera (ciclo de
dos). Las razones completas de cada una de las 30 lecturas van en el
REPORTE.md de esta vuelta; este script solo aplica las 3 que la lectura
decidio ESCRITA.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_ESCRITA = [
    ("gate5_go_to_launch", "plan_de_lanzamiento_al_mercado"),
    ("descubrir_necesidades_del_cliente", "necesidades_psicologicas_cliente"),
    ("mix_medios_marketing_franquicia", "presupuesto_marketing_franquicia"),
]


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def escribir_par(madre_id, hijo_id):
    madre, ruta_m = cargar(madre_id)
    hijo, ruta_h = cargar(hijo_id)

    if hijo_id in (madre.get("nodos_siguientes") or []):
        print(f"YA ESTABA: {madre_id} -> {hijo_id} ya en nodos_siguientes de la madre. No se toca nada.")
        return "YA_ESTABA"
    if hijo_id in (madre.get("nodos_previos") or []):
        print(f"ESCALERA ROTA: {hijo_id} ya esta en nodos_previos de la madre. No se escribe.")
        return "ESCALERA_ROTA"
    if madre_id in (hijo.get("nodos_siguientes") or []):
        print(f"ESCALERA ROTA: {madre_id} ya esta en nodos_siguientes del hijo (invertida). No se escribe.")
        return "ESCALERA_ROTA"

    madre.setdefault("nodos_siguientes", [])
    madre["nodos_siguientes"].append(hijo_id)
    hijo.setdefault("nodos_previos", [])
    hijo["nodos_previos"].append(madre_id)

    with open(ruta_m, "w", encoding="utf-8") as f:
        json.dump(madre, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(ruta_h, "w", encoding="utf-8") as f:
        json.dump(hijo, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"ARISTA ESCRITA (nodos_siguientes Y nodos_previos): {madre_id} -> {hijo_id}")
    return "ESCRITA"


def main():
    resultados = {}
    for madre_id, hijo_id in PARES_ESCRITA:
        resultados[(madre_id, hijo_id)] = escribir_par(madre_id, hijo_id)
    escritas = sum(1 for v in resultados.values() if v == "ESCRITA")
    print()
    print(f"TOTAL ARISTAS ESCRITAS ESTA CORRIDA: {escritas} de {len(PARES_ESCRITA)}")
    print(f"ESCALERA ROTA: {sum(1 for v in resultados.values() if v == 'ESCALERA_ROTA')}")
    print(f"YA ESTABAN: {sum(1 for v in resultados.values() if v == 'YA_ESTABA')}")


if __name__ == "__main__":
    main()
