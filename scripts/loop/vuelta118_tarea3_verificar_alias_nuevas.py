# -*- coding: utf-8 -*-
r"""vuelta118_tarea3_verificar_alias_nuevas.py . TAREA 3.1 de la vuelta 118.

Verifica, para las 296 aristas de las tres fuentes de la fase 04 (OP-E-01
ESCRITA, OP-E-06 direccion V90, OP-E-07 direccion V94), cuantas resuelven por
alias (al menos un extremo), y de esas, cuantas tienen su FORMA CRUDA (los
ids TAL COMO se escribieron, sin resolver) ya presente como arista en el
grafo de hoy: eso seria una "arista por alias nueva", que el criterio de
HECHO de la fase 04 (00_INDICE.md fila 4) exige en CERO.

USO:
  python scripts/loop/vuelta118_tarea3_verificar_alias_nuevas.py
"""
import json

RUTA_GRAFO = "dataset/metadata/master_graph.json"


def leer_pares(ruta, filtro_decision=None):
    filas = [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]
    if filtro_decision:
        filas = [f for f in filas if f.get("decision") == filtro_decision]
    return [(f["madre"], f["hijo"]) for f in filas]


def construir_alias_de(nodos):
    alias_de = {}
    for nid, n in nodos.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias_de[a] = nid
    return alias_de


def hacer_resolver(nodos, alias_de):
    def resolver(nid):
        n = nodos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid, True
        visto = {nid}
        cur = nid
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = nodos.get(cur)
            if c is None:
                continue
            if not c.get("deprecado"):
                return cur, True
        return nid, False
    return resolver


def main():
    grafo = json.load(open(RUTA_GRAFO, encoding="utf-8"))["nodos"]
    alias_de = construir_alias_de(grafo)
    resolver = hacer_resolver(grafo, alias_de)

    fuentes = [
        ("OP-E-01", leer_pares("docs/plan/OP_E_01_DECIDIDAS.jsonl", filtro_decision="ESCRITA")),
        ("OP-E-06", leer_pares("docs/plan/OP_E_06_DIRECCION_V90.jsonl")),
        ("OP-E-07", leer_pares("docs/plan/OP_E_07_DIRECCION_V94.jsonl")),
    ]

    total = 0
    total_alias = 0
    crudo_escrito = []
    for nombre, pares in fuentes:
        for m, h in pares:
            total += 1
            rm, _vm = resolver(m)
            rh, _vh = resolver(h)
            via_alias = (rm != m) or (rh != h)
            if via_alias:
                total_alias += 1
                nm = grafo.get(m) or {}
                nh = grafo.get(h) or {}
                cruda_sig = h in (nm.get("nodos_siguientes") or [])
                cruda_prev = m in (nh.get("nodos_previos") or [])
                if cruda_sig or cruda_prev:
                    crudo_escrito.append((nombre, m, h, cruda_sig, cruda_prev))

    print("TOTAL de pares en las tres fuentes: %d" % total)
    print("resueltos por alias (al menos un extremo): %d" % total_alias)
    print("de esos, con su forma CRUDA (sin resolver) YA ESCRITA como arista en el grafo: %d"
          % len(crudo_escrito))
    for x in crudo_escrito:
        print("   %s: %s -> %s (sig=%s prev=%s)" % x)
    if not crudo_escrito:
        print("CERO aristas por alias nuevas: ninguno de los %d pares resueltos por alias "
              "tiene su forma cruda escrita en el grafo." % total_alias)


if __name__ == "__main__":
    main()
