# -*- coding: utf-8 -*-
"""vuelta88_tarea2_relectura_117.py . TAREA 2.a de la vuelta 88.

POR QUE NACE (acta de la vuelta 87, seccion 2.1 y adjudicacion 6.1): el auditor
publico una discrepancia de clase sobre la unidad 117 (`juran_rcca_metodo ->
diseno_implementacion_remedio`) y trajo un camino de seis nodos como cadena
propia de la madre. La relectura conjunta manda "verificar contra el grafo, no
contra el acta" las seis aristas de ese camino. Este instrumento lee las DOS
vistas (`nodos_siguientes` de cada nodo de origen Y `nodos_previos` del nodo de
destino) directo de `dataset/nodos/*.json`, para cada uno de los seis saltos, y
declara si cada uno de los seis nodos del camino es o no un paso literal de la
madre (leyendo `pasos_accionables` de `juran_rcca_metodo.json`).

USO:
  python scripts/loop/vuelta88_tarea2_relectura_117.py
"""
import json
import os

RAIZ = os.path.join(os.path.dirname(__file__), "..", "..", "dataset", "nodos")


def cargar(node_id):
    ruta = os.path.join(RAIZ, node_id + ".json")
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


CAMINO = [
    "juran_rcca_metodo",
    "definicion_problema_moms_2",
    "analisis_sintomas",
    "formulacion_teorias_causa",
    "prueba_teorias_causa_raiz",
    "evaluacion_alternativas_solucion",
    "diseno_implementacion_remedio",
]

# Frases literales de los pasos de la madre (pasos_accionables), para el
# cotejo de que paso enumera cada nodo del camino. Cotejo por lectura, no por
# regex de similitud: se cita el indice del paso (1 a 4) o "NINGUNO".
PASO_DE_CADA_NODO = {
    "definicion_problema_moms_2": 1,
    "analisis_sintomas": 2,
    "formulacion_teorias_causa": 2,
    "prueba_teorias_causa_raiz": 2,
    "evaluacion_alternativas_solucion": None,
    "diseno_implementacion_remedio": 3,
}


def main():
    nodos = {nid: cargar(nid) for nid in CAMINO}
    madre = nodos["juran_rcca_metodo"]

    print("=== LOS CUATRO PASOS DE LA MADRE, LEIDOS DE SU FICHA ===")
    for i, paso in enumerate(madre["pasos_accionables"], 1):
        print("  paso %d: %s" % (i, paso))
    print()

    print("=== LAS SEIS ARISTAS DEL CAMINO, VERIFICADAS EN LAS DOS VISTAS ===")
    todas_ok = True
    for a, b in zip(CAMINO, CAMINO[1:]):
        na, nb = nodos[a], nodos[b]
        en_siguientes = b in na.get("nodos_siguientes", [])
        en_previos = a in nb.get("nodos_previos", [])
        ok = en_siguientes and en_previos
        todas_ok = todas_ok and ok
        print(
            "  %s -> %s | en nodos_siguientes de %s: %s | en nodos_previos de %s: %s | %s"
            % (a, b, a, en_siguientes, b, en_previos, "OK" if ok else "FALTA")
        )
    print()
    print("TODAS LAS ARISTAS PRESENTES: %s" % todas_ok)
    print()

    print("=== DEPRECADO DE CADA NODO DEL CAMINO ===")
    for nid in CAMINO:
        print("  %s: deprecado=%s" % (nid, nodos[nid].get("deprecado", False)))
    print()

    print("=== QUE PASO DE LA MADRE ES CADA NODO DEL CAMINO (lectura declarada) ===")
    for nid in CAMINO[1:]:
        paso = PASO_DE_CADA_NODO[nid]
        if paso is None:
            print("  %s: NINGUN paso de la madre lo enumera (nodo SUELTO)" % nid)
        else:
            print("  %s: paso %d de la madre" % (nid, paso))
    print()

    sueltos = [nid for nid in CAMINO[1:-1] if PASO_DE_CADA_NODO[nid] is None]
    print("NODOS DEL CAMINO (sin contar madre ni hijo) QUE NINGUN PASO DE LA MADRE ENUMERA: %d"
          % len(sueltos))
    for nid in sueltos:
        print("  - %s (%s)" % (nid, nodos[nid]["titulo_concepto"]))


if __name__ == "__main__":
    main()
