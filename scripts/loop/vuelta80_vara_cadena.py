# -*- coding: utf-8 -*-
"""VUELTA 80: LA VARA NUEVA DE LA CADENA, adjudicada por el auditor en el acta
de la vuelta 79 (seccion 3.1 y seccion 5 punto 6), por cita del CAVEAT MEDIDO
de la 9.6.1 ("la familia ENCADENADA no se cuenta por radios [...] antes de
contar, se mira la FORMA"), SIN doctrina nueva.

LA VARA: antes de escribir una arista madre -> hijo de la fase 04, medir si
el hijo YA ES ALCANZABLE desde la madre por `nodos_siguientes` en el grafo
ANTES de esta escritura. Reusa la maquina de `docs/loop/_auditor_v79_atajo.py`
(BFS con tope de 6 saltos), corrida sobre el grafo EN DISCO de esta vuelta en
vez de un commit fijo.

LO QUE LA VARA NO ES, dicho explicito porque el acta 79 lo dejo escrito
("alcanzable no es lo mismo que encadenado", seccion 3.1): esto NO aparta
candidatos por si solo. Marca cada candidato ALCANZABLE para que la lectura
verifique EXPLICITAMENTE si el camino es la CADENA PROPIA de la madre (sus
pasos enumerados, en orden, colgando unos de otros) antes de decidir. Si lo
es, es un radio sobre cableado ya establecido y NO se escribe (banco 9.6, el
hijo no es contenido huerfano de camino). Si es un camino incidental del
grafo ancho, la alcanzabilidad no dice nada sobre esta jerarquia y la
decision sigue por 9.6.2 normal.
"""
import json
from collections import deque
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"


def cargar_adyacencia():
    with open(GRAFO, encoding="utf-8") as f:
        G = json.load(f)["nodos"]
    return {n: [d for d in (G[n].get("nodos_siguientes") or []) if d in G] for n in G}


def camino(ady, o, d, tope=6):
    if o == d:
        return [o]
    vis = {o}
    q = deque([(o, [o])])
    while q:
        c, p = q.popleft()
        if len(p) > tope:
            continue
        for x in ady.get(c, []):
            if x == d:
                return p + [x]
            if x not in vis:
                vis.add(x)
                q.append((x, p + [x]))
    return None


def marcar_alcanzables(candidatos):
    """candidatos: lista de dicts con 'madre' e 'hijo'. Devuelve dict
    (madre, hijo) -> camino (lista de ids) o None si no hay camino <=6 saltos."""
    ady = cargar_adyacencia()
    resultado = {}
    for c in candidatos:
        resultado[(c["madre"], c["hijo"])] = camino(ady, c["madre"], c["hijo"])
    return resultado


if __name__ == "__main__":
    # Caso positivo con los dos ejemplares ya adjudicados en la vuelta 79
    # (acta 79, seccion 3.1): D2 alcanzable POR LA CADENA PROPIA (positivo
    # real, ya revertido en la TAREA 3 de esta vuelta) y un par cualquiera
    # sin camino previo, como control negativo.
    ady = cargar_adyacencia()
    p1 = camino(ady, "identificacion_evaluacion_peligros", "investigacion_incidentes")
    print("identificacion_evaluacion_peligros -> investigacion_incidentes: %s"
          % (" -> ".join(p1) if p1 else "sin camino <=6 saltos"))
    p2 = camino(ady, "mapa_de_canal_de_ventas", "validar_canal_distribucion")
    print("mapa_de_canal_de_ventas -> validar_canal_distribucion: %s"
          % (" -> ".join(p2) if p2 else "sin camino <=6 saltos"))
