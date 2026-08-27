# -*- coding: utf-8 -*-
"""vuelta92_tarea3b_retirar_1098.py . VUELTA 92, TAREA 3(b): RETIRA LA ARISTA
`customer_validation_sell_phase -> prueba_solucion_con_cliente` (puesto 1098)
DE `dataset/nodos/`, LAS DOS VISTAS (`nodos_siguientes` de la madre,
`nodos_previos` del hijo).

POR QUE. Acta de la vuelta 91 (`docs/loop/ACTA_AUDITOR.md`, seccion 3.1 y
5.1), y el guarda de la TAREA 2 lo confirma (`vuelta92_tarea3a_filtrar_ope07.py`,
EL UNICO puesto que su vara saca de las 88 de OP-E-07 es el 1098): la arista se
escribio en la vuelta 91 sobre un par cuya propia razon manda que SALGA de la
cosecha ("verificacion" de OP-E-07, "el par sale de la cosecha y se anota por
que"). Es LA VERIFICACION DE OP-E-07 aplicandose al reves de como se aplico:
no es un borrado sin regla.

RESUELVE ALIAS igual que `vuelta91_tarea4_escribir_ope07.py` (la funcion
`res()` de `scripts/plan/aristas_duplicadas_tras_resolver.py`, copiada aqui
sin variarla), por si alguno de los dos ids resuelve a otro por
`ids_alias` antes de tocar el fichero.

IDEMPOTENTE: si la arista ya no esta (segunda corrida), imprime "0
RETIRADAS" y no toca ningun fichero.

USO:
  python scripts/loop/vuelta92_tarea3b_retirar_1098.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

MADRE_CRUDA = "customer_validation_sell_phase"
HIJO_CRUDO = "prueba_solucion_con_cliente"


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
    print("TAREA 3(b): RETIRA LA ARISTA DEL PUESTO 1098")
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
