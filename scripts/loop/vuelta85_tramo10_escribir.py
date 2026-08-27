# -*- coding: utf-8 -*-
"""VUELTA 85, TAREA 4: escribe en dataset/nodos/*.json las aristas decididas
ESCRITA de las 30 unidades frescas del tramo 10 (indices 72 a 101 de la bolsa
filtrada V85), en las DOS vistas a la vez, con chequeo de escalera (ciclo de
dos). Las razones completas de cada una de las 30 lecturas van en el
REPORTE.md de esta vuelta; este script solo aplica las que la lectura decidio
ESCRITA.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_ESCRITA = [
    ("lienzo_proyecto_innovacion", "actividades_clave"),
    ("estructura_equipos_innovacion_interna", "equipo_multifuncional_real"),
    ("evaluacion_industria_cliente", "analisis_cadena_de_valor"),
    ("diagrama_de_flujo_proceso_map", "analisis_flujo_proceso"),
    ("stage_gate_system", "tipos_criterios_gate"),
    ("waterfall_vs_agile_development", "customer_development_process"),
    ("decidir_vender_solo_online_o_tambien_tienda_fisica", "ofrecer_puntos_recogida"),
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
