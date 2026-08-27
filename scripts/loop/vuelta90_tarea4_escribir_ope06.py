# -*- coding: utf-8 -*-
"""vuelta90_tarea4_escribir_ope06.py . VUELTA 90, TAREA 4, SEGUNDA MITAD: SE
ABRE `OP-E-06` ESCRIBIENDO LOS 114 PARES DE `docs/plan/OP_E_06_DIRECCION_V90.
jsonl` EN `dataset/nodos/*.json`.

LA SEMANTICA CANONICA DE resolverId, EXACTA (encargo de la vuelta 90, "la
semantica canonica de resolverId para la escritura, la de aristas_duplicadas_
tras_resolver.py, que camina la cadena entera"): antes de escribir, `madre` y
`hijo` se resuelven caminando la cadena COMPLETA de `ids_alias` (no un solo
salto), exactamente la funcion `res()` de `scripts/plan/
aristas_duplicadas_tras_resolver.py`, copiada aqui sin variarla. La arista se
escribe SIEMPRE sobre el id resuelto, nunca sobre el alias literal (P.9).

POR QUE IMPORTA DE VERDAD Y NO ES UN FORMALISMO, CON EL EJEMPLAR DELANTE: los
puestos 2015 (madre `nafta_free_trade_agreements`) y 2023 (madre
`certificado_de_origen_tratados_libre_comercio`) PARECEN dos aristas
distintas por sus ids literales, pero `nafta_free_trade_agreements` ESTA
DEPRECADO y es alias de `certificado_de_origen_tratados_libre_comercio`: las
dos resuelven a LA MISMA arista (`certificado_de_origen_tratados_libre_
comercio -> certificacion_origen_producto`). Sin resolver por la cadena
completa, esto habria escrito una entrada duplicada tras resolver, EXACTAMENTE
LA CLASE QUE `scripts/plan/aristas_duplicadas_tras_resolver.py` existe para
contar y que `OP-C-05` existe para impedir. Procesando en ORDEN DE PUESTO
(2015 antes que 2023) y releyendo el fichero en cada paso (igual que
`scripts/loop/vuelta87_tramo12_escribir.py`), el puesto 2023 sale `YA_ESTABA`
en vez de escribir una segunda vez la misma arista.

LA VIA DE OP-C-05, CABLEADA (encargo de la vuelta 90): este script NO corre
solo. El uso completo, el que abre la operacion, es:

  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 90 --antes
  python scripts/loop/vuelta90_tarea4_escribir_ope06.py
  python scripts/loop/vuelta89_tarea4_guarda_op_c05.py --vuelta 90 --despues

El sello de `--antes` y la comprobacion de `--despues` llevan el numero de
ESTA vuelta (90), no el de la 89 donde el instrumento nacio: cada vuelta
sella el suyo (asi lo dejo escrito el propio instrumento).

ESCALERA, identica a `scripts/loop/vuelta87_tramo12_escribir.py`: si el hijo
YA esta en `nodos_siguientes` de la madre, `YA_ESTABA` (no se toca nada); si
el hijo YA esta en `nodos_previos` de la madre, o si la madre YA esta en
`nodos_siguientes` del hijo (arista puesta al reves por otra fuente),
`ESCALERA_ROTA` y NO SE ESCRIBE (la escalera del banco no admite la vuelta).

QUE NO HACE: no decide direccion (eso ya lo hizo `scripts/loop/
vuelta90_tarea4_direccion_ope06.py`), no toca los tres pares de enlace mutuo
excluidos (2082, 2084, 2112, quedan en `PENDIENTES`), y no toca
`dataset/metadata/master_graph.json` directamente: ese fichero se
RECOMPUTA con el ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) DESPUES
de que este script termine, igual que toda escritura de esta fase.

USO:
  python scripts/loop/vuelta90_tarea4_escribir_ope06.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DIRECCION = os.path.join(PLAN, "OP_E_06_DIRECCION_V90.jsonl")
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
    print("VUELTA 90, TAREA 4 (segunda mitad): ESCRITURA DE OP-E-06, %d PARES" % len(pares))
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
        marca = ("%s -> %s" % (m, h)) if m != p["madre"] or h != p["hijo"] else "%s -> %s" % (m, h)
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
