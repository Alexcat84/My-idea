# -*- coding: utf-8 -*-
"""VUELTA 84, TAREA 1.4: escribe en dataset/nodos/*.json las tres aristas que
la relectura conjunta de los pares 33, 44 y 45 (acta de la vuelta 83, seccion
2, adjudicaciones 6.3 y 6.4) decide SE ESCRIBE, en las DOS vistas a la vez,
con chequeo de escalera (ciclo de dos). Sucesor directo de
scripts/loop/vuelta83_tramo8_escribir.py, misma maquina.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_ESCRITA = [
    ("gestion_efectiva_benchmarking", "reconocimiento_publico_recompensas"),
    ("estructura_competencias_six_sigma_lean", "evaluacion_desempeno_proyectos"),
    ("poder_a_traves_de_la_accion", "compromiso_organismico_en_la_accion"),
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
