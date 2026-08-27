# -*- coding: utf-8 -*-
"""vuelta94_tarea3b_retirar_1281_1992.py . VUELTA 94, TAREA 3(b): RETIRA LAS
DOS ARISTAS DE LAS RELECTURAS CONJUNTAS (scripts/loop/
vuelta94_tarea3_relectura_1281_1992.py, las dos SALEN) DE dataset/nodos/, LAS
DOS VISTAS (nodos_siguientes de la madre escrita, nodos_previos del hijo
escrito), mismo mecanismo exacto que
scripts/loop/vuelta93_tarea3b_retirar_1009.py.

PUESTO 1281: get_visual -> pensamiento_visual_modelos_negocio.
PUESTO 1992: seleccion_de_metodo_de_pago -> metodos_pago_electronico_internacional.

RESUELVE ALIAS con la misma funcion res() canonica que las vueltas 92 y 93.

IDEMPOTENTE: si una arista ya no esta (segunda corrida), imprime NO_ESTABA
para esa arista y no toca ese fichero.

USO:
  python scripts/loop/vuelta94_tarea3b_retirar_1281_1992.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

PARES = [
    ("get_visual", "pensamiento_visual_modelos_negocio", 1281),
    ("seleccion_de_metodo_de_pago", "metodos_pago_electronico_internacional", 1992),
]


def construir_alias():
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
    print("=" * 90)
    print("TAREA 3(b) de la vuelta 94: RETIRA LAS ARISTAS DE LOS PUESTOS 1281 Y 1992")
    print("=" * 90)

    retiradas = 0
    for madre_cruda, hijo_crudo, puesto in PARES:
        m, h = res(madre_cruda), res(hijo_crudo)
        print()
        print("puesto %d: cruda %s -> %s" % (puesto, madre_cruda, hijo_crudo))
        print("resuelta: %s -> %s%s" % (m, h, "" if (m, h) == (madre_cruda, hijo_crudo) else " (con alias)"))
        if m not in G or h not in G:
            print("ROJO: un id resuelto no existe en el grafo. NO SE TOCA NADA MAS.")
            return 1
        resultado = retirar_par(m, h)
        print("RESULTADO: %s" % resultado)
        if resultado == "RETIRADA":
            retiradas += 1

    print()
    print("RETIRADAS ESTA CORRIDA: %d" % retiradas)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
