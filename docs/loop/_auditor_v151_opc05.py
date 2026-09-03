# -*- coding: utf-8 -*-
"""Auditor v151: instrumento propio para OP-C-05. La resolucion va RE ESCRITA
aqui siguiendo resolverId, sin importar run_phase1, para que la medicion del
auditor no dependa del codigo que audita.

Mide, sobre cualquier ref de git:
  - duplicadas TRAS RESOLVER en listas de nodos VIVOS (grupos, sobran, nodos)
  - duplicadas LITERALES, que es el contraste que prueba que resolver no es adorno
  - pares BIDIRECCIONALES entre nodos vivos tras resolver

Salida commiteada en docs/loop/_auditor_v151_opc05.txt.
"""
import json
import subprocess


def cargar(ref):
    if ref == "WORK":
        return json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True)
    if b.returncode:
        raise SystemExit("ROJO: no se pudo leer " + ref)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def hacer_resolver(N):
    alias = {}
    for nid, n in N.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def r(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto = {nid}
        cur = nid
        ult = nid if n is not None else None
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ult = cur
            if not c.get("deprecado"):
                return cur
        return ult
    return r


def dup_resueltas(N):
    r = hacer_resolver(N)
    activos = {k: v for k, v in N.items() if not v.get("deprecado")}
    grupos = sobran = 0
    nodos = set()
    for nid in sorted(activos):
        n = activos[nid]
        for campo in ("nodos_previos", "nodos_siguientes"):
            pd = {}
            for d in (n.get(campo) or []):
                if d not in N:
                    continue
                pd.setdefault(r(d), []).append(d)
            for _dest, ent in pd.items():
                if len(ent) > 1:
                    grupos += 1
                    sobran += len(ent) - 1
                    nodos.add(nid)
    return grupos, sobran, len(nodos)


def dup_literales(N):
    activos = {k: v for k, v in N.items() if not v.get("deprecado")}
    g = 0
    for _nid, n in activos.items():
        for campo in ("nodos_previos", "nodos_siguientes"):
            l = [d for d in (n.get(campo) or []) if d in N]
            if len(set(l)) != len(l):
                g += 1
    return g


def bidireccionales(N):
    r = hacer_resolver(N)
    activos = {k: v for k, v in N.items() if not v.get("deprecado")}
    S = set()
    for nid, n in activos.items():
        for d in (n.get("nodos_siguientes") or []):
            if d in N:
                a, b = r(nid), r(d)
                if a and b and a != b and not N[a].get("deprecado") and not N[b].get("deprecado"):
                    S.add((a, b))
    return len({tuple(sorted((a, b))) for (a, b) in S if (b, a) in S})


def main():
    mb = subprocess.run(["git", "merge-base", "HEAD", "main"],
                        capture_output=True, text=True).stdout.strip()
    print("merge-base con main:", mb[:8])
    for etq, ref in (("ANTES de OP-S-12 (a34328b2~1)", "a34328b2~1"),
                     ("HEAD (WORK)", "WORK"),
                     ("mergebase", mb)):
        N = cargar(ref)
        g, s, nd = dup_resueltas(N)
        print("%-32s | dup RESOLVIENDO: grupos %d sobran %d nodos %d | dup LITERALES: %d "
              "listas | BIDIRECCIONALES vivos: %d pares"
              % (etq, g, s, nd, dup_literales(N), bidireccionales(N)))


if __name__ == "__main__":
    main()
