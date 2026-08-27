# -*- coding: utf-8 -*-
"""vuelta93_tarea3b_retirar_1009.py . VUELTA 93, TAREA 3(b) (analoga a la
TAREA 3(b) de la vuelta 92): RETIRA LA ARISTA
`customer_discovery_phase2_problem_test -> fit_problema_solucion` (puesto
1009) DE `dataset/nodos/`, LAS DOS VISTAS (`nodos_siguientes` de la madre
escrita, `nodos_previos` del hijo escrito).

POR QUE. TAREA 2 de esta vuelta (relectura conjunta): la razon del 1009 no
nombra cual nodo es la madre (usa la formula de la clase D, "trae un
procedimiento que ESA FASE no tiene", nunca "la madre"; no nombra ninguna
linea con su paso; y ella misma declara que el bloque de traccion del hijo
queda FUERA del solape, lo que hace fallar el test del banco 9.6.2). Por
`OP-E-07.verificacion` ("si la razon tampoco lo dice, el par sale de la
cosecha"), el par SALE. El guarda reparado de la TAREA 3
(`scripts/loop/vuelta93_tarea3_guarda_direccion.py`) lo confirma
mecanicamente (`vuelta93_tarea3a_filtrar_1009.py`).

RESUELVE ALIAS igual que `vuelta92_tarea3b_retirar_1098.py` (la misma
funcion `res()` canonica).

IDEMPOTENTE: si la arista ya no esta (segunda corrida), imprime "0
RETIRADAS" y no toca ningun fichero.

USO:
  python scripts/loop/vuelta93_tarea3b_retirar_1009.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

MADRE_CRUDA = "customer_discovery_phase2_problem_test"
HIJO_CRUDO = "fit_problema_solucion"


def construir_alias():
    """LA SEMANTICA CANONICA DE resolverId, copiada literal (P.9): camina la
    cadena de ids_alias entera, no un solo salto."""
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    return G, res


def cargar_nodo(node_id):
    p = os.path.join(NODOS, "%s.json" % node_id)
    with io.open(p, encoding="utf-8") as f:
        return json.load(f), p


def retirar_par(madre_id, hijo_id):
    """Devuelve "RETIRADA" o "NO_ESTABA". Retira LAS DOS VISTAS a la vez o
    ninguna."""
    madre, ruta_m = cargar_nodo(madre_id)
    hijo, ruta_h = cargar_nodo(hijo_id)

    en_siguientes = hijo_id in (madre.get("nodos_siguientes") or [])
    en_previos = madre_id in (hijo.get("nodos_previos") or [])

    if not en_siguientes and not en_previos:
        return "NO_ESTABA"

    if en_siguientes:
        madre["nodos_siguientes"] = [n for n in madre["nodos_siguientes"] if n != hijo_id]
        with io.open(ruta_m, "w", encoding="utf-8") as f:
            json.dump(madre, f, ensure_ascii=False, indent=2)
            f.write("\n")
    if en_previos:
        hijo["nodos_previos"] = [n for n in hijo["nodos_previos"] if n != madre_id]
        with io.open(ruta_h, "w", encoding="utf-8") as f:
            json.dump(hijo, f, ensure_ascii=False, indent=2)
            f.write("\n")

    return "RETIRADA"


def main():
    G, res = construir_alias()
    m, h = res(MADRE_CRUDA), res(HIJO_CRUDO)

    print("=" * 90)
    print("TAREA 3(b) de la vuelta 93: RETIRA LA ARISTA DEL PUESTO 1009")
    print("=" * 90)
    print("cruda:    %s -> %s" % (MADRE_CRUDA, HIJO_CRUDO))
    print("resuelta: %s -> %s%s" % (m, h, "" if (m, h) == (MADRE_CRUDA, HIJO_CRUDO) else " (con alias)"))

    if m not in G or h not in G:
        print("ROJO: un id resuelto no existe en el grafo. NO SE TOCA NADA.")
        return 1

    resultado = retirar_par(m, h)
    print()
    print("RESULTADO: %s" % resultado)
    print("RETIRADAS ESTA CORRIDA: %d" % (1 if resultado == "RETIRADA" else 0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
