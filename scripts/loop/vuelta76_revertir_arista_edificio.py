"""VUELTA 76, TAREA 1.3.a: revierte la arista
segmentos_de_clientes_problema_necesidad -> get_out_of_the_building, escrita
en la vuelta 75 contra P.9 punto 1 (el destino esta en el campo eliminar de
OP-M-05-EDIFICIO, fusion de la fase 03 enrutada a la fase 06, no ejecutada
todavia). Adjudicado por el auditor, acta vuelta 75 seccion 4.5.

Quita el id de las dos listas donde la vuelta 75 lo dejo: nodos_siguientes de
la madre (escrito por el ejecutor) y nodos_previos del hijo (completado por
el paso 5 de run_phase1.py, aristas_a_simetrizar). El ciclo de Gate 0 no
BORRA reciprocas: solo anade las que faltan. Por eso las dos puntas se quitan
aqui a mano, y despues se corre el ciclo entero para comprobar que no vuelve
a aparecer sola.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

MADRE = "segmentos_de_clientes_problema_necesidad"
HIJO = "get_out_of_the_building"


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def guardar(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    data_madre, p_madre = cargar(MADRE)
    sig = data_madre.get("nodos_siguientes") or []
    if HIJO in sig:
        sig.remove(HIJO)
        data_madre["nodos_siguientes"] = sig
        guardar(data_madre, p_madre)
        print(f"QUITADO de nodos_siguientes de {MADRE}: {HIJO}")
    else:
        print(f"YA NO ESTABA en nodos_siguientes de {MADRE} (nada que hacer)")

    data_hijo, p_hijo = cargar(HIJO)
    prev = data_hijo.get("nodos_previos") or []
    if MADRE in prev:
        prev.remove(MADRE)
        data_hijo["nodos_previos"] = prev
        guardar(data_hijo, p_hijo)
        print(f"QUITADO de nodos_previos de {HIJO}: {MADRE}")
    else:
        print(f"YA NO ESTABA en nodos_previos de {HIJO} (nada que hacer)")


if __name__ == "__main__":
    main()
