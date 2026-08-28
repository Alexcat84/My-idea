# -*- coding: utf-8 -*-
r"""vuelta116_tarea3_3_criterio_hecho_fase04.py . TAREA 3.3 de la vuelta 116,
encargo del auditor (acta de la vuelta 115).

QUE MIDE. El criterio de HECHO de la fase 04 esta escrito en
docs/plan/00_INDICE.md, tabla "EL ORDEN", fila 4: "las aristas escritas con
ids RESUELTOS, una sola direccion salvo los dos enlaces mutuos, y cero
aristas por alias nuevas". Este instrumento mide las TRES cosas sobre las 98
filas ESCRITA de docs/plan/OP_E_01_DECIDIDAS.jsonl y sobre el campo
`aristas_nuevas` de OP-E-02 en docs/plan/OPERACIONES.jsonl, CONTRA EL GRAFO
DE HOY (dataset/metadata/master_graph.json):

  (1) IDS RESUELTOS: para cada madre/hijo, si el valor es una clave directa
      de `nodos` (RESUELTO) o si solo aparece dentro del `ids_alias` de otro
      nodo (naceria RESOLVIENDO POR ALIAS).
  (2) UNA SOLA DIRECCION: cuantos pares (madre, hijo) de las ESCRITA tienen
      tambien su inverso (hijo, madre) escrito, y si esos pares coinciden con
      los DOS enlaces mutuos del banco 9.22 (`LD-41`:
      requisitos_gates_con_dientes / gestion_portafolio_formal, y `LD-43`:
      requisitos_gates_con_dientes / gestion_portafolio_dos_niveles,
      docs/plan/LD_MESA_UNIDA.md lineas 140 y 160) o si hay alguna mas.
  (3) ARISTAS POR ALIAS: cuantas aristas de las ESCRITA nacerian resolviendo
      por alias (subconjunto de (1)).

SOLO MEDIR. No adjudica si el criterio de HECHO de la fase 04 esta cumplido:
esa es la adjudicacion del auditor en la 117.

USO:
  python scripts/loop/vuelta116_tarea3_3_criterio_hecho_fase04.py
"""
import json

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_DECIDIDAS = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
RUTA_OPS = "docs/plan/OPERACIONES.jsonl"

ENLACES_MUTUOS_9_22 = [
    frozenset(("requisitos_gates_con_dientes", "gestion_portafolio_formal")),  # LD-41
    frozenset(("requisitos_gates_con_dientes", "gestion_portafolio_dos_niveles")),  # LD-43
]


def cargar_grafo():
    g = json.load(open(RUTA_GRAFO, encoding="utf-8"))
    return g["nodos"]


def indice_alias(nodos):
    idx = {}
    for nid, n in nodos.items():
        for a in (n.get("ids_alias") or []):
            idx[a] = nid
    return idx


def main():
    nodos = cargar_grafo()
    alias_idx = indice_alias(nodos)

    filas = [json.loads(l) for l in open(RUTA_DECIDIDAS, encoding="utf-8") if l.strip()]
    escritas = [f for f in filas if f["decision"] == "ESCRITA"]
    pares = [(f["madre"], f["hijo"]) for f in escritas]
    set_pares = set(pares)

    print("CRITERIO DE HECHO DE LA FASE 04 CONTRA EL GRAFO DE HOY, TAREA 3.3 VUELTA 116.")
    print("=" * 100)
    print("Fuente ESCRITA: %s (%d filas). Fuente grafo: %s." % (RUTA_DECIDIDAS, len(escritas), RUTA_GRAFO))
    print()

    print("--- (1) IDS RESUELTOS ---")
    resueltos = 0
    por_alias = []
    rotos = []
    for m, h in pares:
        estado_m = "RESUELTO" if m in nodos else ("ALIAS->%s" % alias_idx[m] if m in alias_idx else "ROTO")
        estado_h = "RESUELTO" if h in nodos else ("ALIAS->%s" % alias_idx[h] if h in alias_idx else "ROTO")
        if estado_m == "RESUELTO" and estado_h == "RESUELTO":
            resueltos += 1
        if "ALIAS" in estado_m or "ALIAS" in estado_h:
            por_alias.append((m, h, estado_m, estado_h))
        if "ROTO" in estado_m or "ROTO" in estado_h:
            rotos.append((m, h, estado_m, estado_h))
    print("aristas con LOS DOS extremos RESUELTOS (id vivo): %d de %d" % (resueltos, len(pares)))
    print("aristas que NACERIAN RESOLVIENDO POR ALIAS (al menos un extremo): %d" % len(por_alias))
    for x in por_alias:
        print("   ALIAS: %s -> %s (%s / %s)" % x)
    print("aristas ROTAS (ni id vivo ni alias conocido, en ninguno de los dos): %d" % len(rotos))
    for x in rotos:
        print("   ROTO: %s -> %s (%s / %s)" % x)
    print()

    print("--- (2) UNA SOLA DIRECCION ---")
    bidireccionales = set()
    for m, h in pares:
        if (h, m) in set_pares:
            bidireccionales.add(frozenset((m, h)))
    print("pares con las DOS direcciones escritas entre las 98 ESCRITA: %d" % len(bidireccionales))
    for par in bidireccionales:
        m, h = tuple(par)
        es_9_22 = par in ENLACES_MUTUOS_9_22
        print("   %s <-> %s -- %s" % (m, h, "ES uno de los dos enlaces mutuos del 9.22" if es_9_22 else "NO es de los dos del 9.22, ALGUNA MAS"))
    faltan_9_22 = [par for par in ENLACES_MUTUOS_9_22 if par not in bidireccionales]
    for par in faltan_9_22:
        m, h = tuple(par)
        print("   NOTA: el enlace mutuo del 9.22 %s <-> %s NO esta entre las 98 ESCRITA de OP-E-01 (LD_MESA_UNIDA.md lo asigna a OP-E-05, no a OP-E-01)." % (m, h))
    print()

    print("--- (3) ARISTAS POR ALIAS (subconjunto de (1)) ---")
    print("total de aristas por alias entre las 98 ESCRITA: %d" % len(por_alias))
    print()

    print("--- OP-E-02, sobre sus propias aristas ---")
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    by_id = {o["id_op"]: o for o in ops}
    aristas_e02 = by_id["OP-E-02"].get("aristas_nuevas") or []
    print("OP-E-02.aristas_nuevas (docs/plan/OPERACIONES.jsonl): %d fila(s). %s"
          % (len(aristas_e02), "NADA QUE MEDIR (campo vacio)." if not aristas_e02 else str(aristas_e02)))


if __name__ == "__main__":
    main()
