# -*- coding: utf-8 -*-
"""vuelta91_tarea4_escribir_ope07.py . VUELTA 91, TAREA 4, TERCERA MITAD: SE
ABRE `OP-E-07` ESCRIBIENDO LOS 88 PARES DE `docs/plan/OP_E_07_DIRECCION_V91.
jsonl` EN `dataset/nodos/*.json`.

IDENTICO EN SEMANTICA A `scripts/loop/vuelta90_tarea4_escribir_ope06.py`
(reutiliza su misma logica de resolucion y de escalera, copiada aqui sin
variarla): antes de escribir, `madre` y `hijo` se resuelven caminando la
cadena COMPLETA de `ids_alias` (la funcion `res()` de `scripts/plan/
aristas_duplicadas_tras_resolver.py`), y la arista se escribe SIEMPRE sobre
el id resuelto (P.9). ESCALERA: si el hijo YA esta en `nodos_siguientes` de
la madre, `YA_ESTABA`; si la arista existe puesta AL REVES por otra fuente,
`ESCALERA_ROTA` y no se escribe.

LA VIA DE OP-C-05, CABLEADA (misma via que OP-E-06): este script NO corre
solo. El uso completo, el que abre la operacion:

  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 91 --antes
  python scripts/loop/vuelta91_tarea4_escribir_ope07.py
  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 91 --despues

QUE NO HACE: no decide direccion (vuelta91_tarea4_direccion_ope07.py ya lo
hizo), y no toca `dataset/metadata/master_graph.json` directamente: ese
fichero se RECOMPUTA con el ciclo de tres DESPUES de que este script
termine.

USO:
  python scripts/loop/vuelta91_tarea4_escribir_ope07.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DIRECCION = os.path.join(PLAN, "OP_E_07_DIRECCION_V91.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def construir_alias():
    """LA SEMANTICA CANONICA DE resolverId, copiada literal de
    scripts/plan/aristas_duplicadas_tras_resolver.py (funcion `res`), sin
    variarla: camina la cadena de ids_alias entera, no un solo salto."""
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


def escribir_par(madre_id, hijo_id):
    madre, ruta_m = cargar_nodo(madre_id)
    hijo, ruta_h = cargar_nodo(hijo_id)

    if hijo_id in (madre.get("nodos_siguientes") or []):
        return "YA_ESTABA"
    if hijo_id in (madre.get("nodos_previos") or []):
        return "ESCALERA_ROTA"
    if madre_id in (hijo.get("nodos_siguientes") or []):
        return "ESCALERA_ROTA"

    madre.setdefault("nodos_siguientes", [])
    madre["nodos_siguientes"].append(hijo_id)
    hijo.setdefault("nodos_previos", [])
    hijo["nodos_previos"].append(madre_id)

    with io.open(ruta_m, "w", encoding="utf-8") as f:
        json.dump(madre, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with io.open(ruta_h, "w", encoding="utf-8") as f:
        json.dump(hijo, f, ensure_ascii=False, indent=2)
        f.write("\n")

    return "ESCRITA"


def main():
    pares = sorted(cargar_jsonl(DIRECCION), key=lambda p: p["puesto"])
    G, res = construir_alias()

    print("=" * 90)
    print("VUELTA 91, TAREA 4 (tercera mitad): ESCRITURA DE OP-E-07, %d PARES" % len(pares))
    print("=" * 90)

    fallos_resolucion = []
    for p in pares:
        m, h = res(p["madre"]), res(p["hijo"])
        if m not in G or h not in G:
            fallos_resolucion.append((p["puesto"], p["madre"], p["hijo"], m, h, "id resuelto no existe en el grafo"))
        elif m == h:
            fallos_resolucion.append((p["puesto"], p["madre"], p["hijo"], m, h, "COLAPSO: madre e hijo resuelven al mismo nodo"))
        elif G[m].get("deprecado") or G[h].get("deprecado"):
            fallos_resolucion.append((p["puesto"], p["madre"], p["hijo"], m, h, "un lado resuelto sigue deprecado"))

    if fallos_resolucion:
        print("ROJO: %d par(es) no pasan la resolucion. NO SE ESCRIBE NADA:" % len(fallos_resolucion))
        for puesto, ma, hi, m, h, motivo in fallos_resolucion:
            print("   puesto %s (%s -> %s, resuelto %s -> %s): %s" % (puesto, ma, hi, m, h, motivo))
        return 1

    resultados = []
    for p in pares:
        m, h = res(p["madre"]), res(p["hijo"])
        r = escribir_par(m, h)
        resultados.append((p["puesto"], p["madre"], p["hijo"], m, h, r))
        marca = "%s -> %s" % (m, h)
        print("puesto %-6s | %-14s | %s (resuelto: %s)" % (p["puesto"], r, marca,
              "%s -> %s" % (p["madre"], p["hijo"]) if (m, h) != (p["madre"], p["hijo"]) else "sin alias"))

    escritas = sum(1 for r in resultados if r[5] == "ESCRITA")
    ya_estaban = sum(1 for r in resultados if r[5] == "YA_ESTABA")
    rotas = sum(1 for r in resultados if r[5] == "ESCALERA_ROTA")

    print()
    print("=" * 90)
    print("TOTAL ARISTAS ESCRITAS ESTA CORRIDA: %d de %d" % (escritas, len(pares)))
    print("YA_ESTABA (arista resuelta que ya existia, sin tocar nada): %d" % ya_estaban)
    print("ESCALERA_ROTA (no se escribe): %d" % rotas)
    if rotas:
        print("PARES CON ESCALERA ROTA, nombrados:")
        for puesto, ma, hi, m, h, r in resultados:
            if r == "ESCALERA_ROTA":
                print("   puesto %s: %s -> %s (resuelto %s -> %s)" % (puesto, ma, hi, m, h))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
