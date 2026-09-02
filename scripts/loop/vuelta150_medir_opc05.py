# -*- coding: utf-8 -*-
"""vuelta150_medir_opc05.py . MEDICION PREVIA DE OP-C-05, vuelta 150.

Mide sobre dataset/metadata/master_graph.json (WORK o una ref de git) las DOS
cosas que la guarda de OP-C-05 tiene que vigilar, con el MISMO resolutor que
scripts/run_phase1.py usa para la guarda de auto-arista de OP-C-04 (copia fiel
de resolverId de web/lib/engine/graph.ts):

  A) DUPLICADAS TRAS RESOLVER dentro de una misma lista: dos entradas del mismo
     campo (nodos_previos o nodos_siguientes) de un mismo nodo que RESUELVEN al
     mismo destino.
  B) BIDIRECCIONALES TRAS RESOLVER: pares (A,B) con B en A.nodos_siguientes y A
     en B.nodos_siguientes, los dos resueltos. Y aparte, la lectura de la
     ficha de OP-E-05 sobre nodos_previos.

NO ESCRIBE NADA. Es medicion, no operacion.
"""
import json
import subprocess
import sys


def cargar(ref):
    if ref == "WORK":
        with open("dataset/metadata/master_graph.json", encoding="utf-8") as f:
            return json.load(f)
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True)
    if b.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer " + ref)
    return json.loads(b.stdout.decode("utf-8"))


def hacer_resolutor(nodos_todos):
    alias_de = {}
    for _nid, _n in nodos_todos.items():
        for _a in _n.get("ids_alias") or []:
            if _a != _nid:
                alias_de[_a] = _nid

    def _resolver(nid):
        n = nodos_todos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto = {nid}
        cur = nid
        ultimo_real = nid if n is not None else None
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = nodos_todos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real
    return _resolver


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "WORK"
    N = cargar(ref)["nodos"]
    res = hacer_resolutor(N)
    activos = {k: v for k, v in N.items() if not v.get("deprecado")}
    print("REF: %s | nodos %d | vivos %d" % (ref, len(N), len(activos)))

    # A) duplicadas tras resolver, dentro de una lista, SOBRE VIVOS
    dup_entradas = 0
    dup_grupos = 0
    dup_nodos = set()
    muestra = []
    for nid, n in sorted(activos.items()):
        for campo in ("nodos_previos", "nodos_siguientes"):
            visto = {}
            for dest in n.get(campo) or []:
                if dest not in N:
                    continue
                r = res(dest)
                visto.setdefault(r, []).append(dest)
            for r, origenes in visto.items():
                if len(origenes) > 1:
                    dup_grupos += 1
                    dup_entradas += len(origenes) - 1
                    dup_nodos.add(nid)
                    if len(muestra) < 5:
                        muestra.append("%s.%s -> %s via %s" % (nid, campo, r, origenes))
    print("A) DUPLICADAS TRAS RESOLVER (vivos): grupos %d | entradas que sobran %d | nodos %d"
          % (dup_grupos, dup_entradas, len(dup_nodos)))
    for m in muestra:
        print("   " + m)

    # A2) lo mismo SOBRE TODOS (vivos y deprecados), para saber el universo
    dup_entradas_t = 0
    for nid, n in N.items():
        for campo in ("nodos_previos", "nodos_siguientes"):
            visto = {}
            for dest in n.get(campo) or []:
                if dest not in N:
                    continue
                visto.setdefault(res(dest), []).append(dest)
            for r, origenes in visto.items():
                if len(origenes) > 1:
                    dup_entradas_t += len(origenes) - 1
    print("A2) las mismas SOBRE TODOS (vivos + deprecados): entradas que sobran %d" % dup_entradas_t)

    # B) bidireccionales tras resolver, en nodos_siguientes, sobre vivos
    sig = {}
    for nid, n in activos.items():
        r_nid = res(nid)
        for dest in n.get("nodos_siguientes") or []:
            if dest in N:
                sig.setdefault(r_nid, set()).add(res(dest))
    pares = set()
    for a, ds in sig.items():
        for b in ds:
            if b in sig and a in sig[b] and a != b:
                pares.add(tuple(sorted((a, b))))
    print("B) BIDIRECCIONALES TRAS RESOLVER en nodos_siguientes (vivos): %d par(es)" % len(pares))
    for p in sorted(pares)[:20]:
        print("   %s <-> %s" % p)

    # C) el caso de borde: mismo destino en previos Y en siguientes del MISMO nodo
    borde = 0
    for nid, n in activos.items():
        s = {res(d) for d in (n.get("nodos_siguientes") or []) if d in N}
        p = {res(d) for d in (n.get("nodos_previos") or []) if d in N}
        borde += len(s & p)
    print("C) CASO DE BORDE (mismo destino en previos y siguientes del mismo nodo, tras resolver): %d" % borde)

    # D) las cuatro aristas de OP-E-05, una a una
    print("D) OP-E-05, las cuatro aristas:")
    for a, b in (("requisitos_gates_con_dientes", "gestion_portafolio_formal"),
                 ("requisitos_gates_con_dientes", "gestion_portafolio_dos_niveles")):
        for x, y in ((a, b), (b, a)):
            nx = N.get(x)
            en_sig = (y in (nx.get("nodos_siguientes") or [])) if nx else None
            en_prev = (y in (nx.get("nodos_previos") or [])) if nx else None
            print("   %s -> %s | existe_nodo %s | en_sig %s | en_prev %s"
                  % (x, y, nx is not None, en_sig, en_prev))


main()
