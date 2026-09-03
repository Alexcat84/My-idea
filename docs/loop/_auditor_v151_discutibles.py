# -*- coding: utf-8 -*-
"""Auditor v151: los discutibles 2, 6 y 7 del reporte 150, puestos a prueba con
varas MIAS y no con las suyas.

D2  la fila 06 MESAS medida por SECCION DELIMITADA de docs/plan/06_MESAS.md en
    vez de por la ventana de 4.000 caracteres que el ejecutor eligio a ojo.
D6  la sensibilidad del umbral de CONGELADO DECLARADO a la lista de marcas.
D7  las entradas que sobran sobre nodos DEPRECADOS y sobre VIVOS, hoy.

Salida commiteada en docs/loop/_auditor_v151_discutibles.txt.
"""
import io
import json
import re

OPS = "docs/plan/OPERACIONES.jsonl"
GRAFO = "dataset/metadata/master_graph.json"
PAGINA_MESAS = "docs/plan/06_MESAS.md"


def fichas():
    return [json.loads(x) for x in io.open(OPS, encoding="utf-8").read().splitlines() if x.strip()]


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


def d2_mesas(F):
    print("D2. FILA 06 MESAS POR SECCION DELIMITADA (no por ventana de 4.000)")
    pag = io.open(PAGINA_MESAS, encoding="utf-8").read()
    cortes = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^## .*$", pag)]

    def seccion_de(idop):
        trozos = []
        for i, (p, h) in enumerate(cortes):
            fin = cortes[i + 1][0] if i + 1 < len(cortes) else len(pag)
            if idop in h:
                trozos.append(pag[p:fin])
        return "\n".join(trozos)

    ok = 0
    mesas = [x for x in F if x["fase"] == "06_MESAS"]
    for m in mesas:
        base = " ".join(str(m.get(k) or "") for k in ("adjudicacion", "nota"))
        sec = seccion_de(m["id_op"])
        texto = base + " " + sec
        dec = bool((m.get("adjudicacion") or "").strip())
        mot = bool(re.search(r"\bporque\b|\bmotivo\b", texto, re.I))
        cob = bool(re.search(r"\bcobertura\b|\b\d+\s+de\s+\d+\b|\d+\s*%", texto, re.I))
        v = "OK" if (dec and mot and cob) else "FALLO"
        ok += v == "OK"
        print("   %-10s decision=%-5s motivo=%-5s cobertura=%-5s -> %s "
              "(seccion %d chars, %d bloque(s))"
              % (m["id_op"], dec, mot, cob, v, len(sec), sec.count("## ")))
    print("   POR SECCION DELIMITADA: %d de %d" % (ok, len(mesas)))


def d6_umbral(F):
    print("")
    print("D6. SENSIBILIDAD DEL UMBRAL DE `CONGELADO DECLARADO`")
    listas = [f for f in F if f["estado"] == "LISTA"]
    LISTAS = [
        ("la del ejecutor",
         ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE")),
        ("estrecha (solo CONGELAD y DIFERIDA)",
         ("CONGELAD", "DIFERIDA")),
        ("ancha (mas DECLARADA, NO SE TOCA, RESERVAD, PENDIENTE)",
         ("ESTADO", "DIFERIDA", "CONGELAD", "SIGUE EN LISTA", "NO SE MUEVE",
          "DECLARADA", "NO SE TOCA", "RESERVAD", "PENDIENTE")),
        ("muy estrecha (la palabra estado pegada a un verbo)",
         ("SU ESTADO", "ESTADO NO", "ESTADO SE", "ESTADO SIGUE", "ESTADO QUEDA")),
    ]
    for nombre, marcas in LISTAS:
        d = 0
        for f in listas:
            t = (str(f.get("nota") or "") + " " + str(f.get("adjudicacion") or "")).upper()
            if any(m in t for m in marcas):
                d += 1
        print("   %-54s -> DECLARADAS %d de %d en LISTA" % (nombre, d, len(listas)))


def d7_deprecados():
    print("")
    print("D7. ENTRADAS QUE SOBRAN TRAS RESOLVER, POR UNIVERSO")
    N = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    r = hacer_resolver(N)

    def sobran(univ):
        s = 0
        for nid in univ:
            n = N[nid]
            for campo in ("nodos_previos", "nodos_siguientes"):
                pd = {}
                for d in (n.get(campo) or []):
                    if d in N:
                        pd.setdefault(r(d), []).append(d)
                for _k, e in pd.items():
                    if len(e) > 1:
                        s += len(e) - 1
        return s

    dep = [k for k, v in N.items() if v.get("deprecado")]
    viv = [k for k, v in N.items() if not v.get("deprecado")]
    print("   sobre DEPRECADOS: %d | sobre VIVOS: %d" % (sobran(dep), sobran(viv)))

    # y de paso, la unidad del 307 del caso de borde
    nodos = pares = 0
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        S = {r(d) for d in (n.get("nodos_siguientes") or []) if d in N}
        P = {r(d) for d in (n.get("nodos_previos") or []) if d in N}
        inter = S & P
        if inter:
            nodos += 1
            pares += len(inter)
    print("   CASO DE BORDE, LA UNIDAD: %d destino(s) sobre %d nodo(s) vivo(s), "
          "no %d nodos" % (pares, nodos, pares))


def main():
    F = fichas()
    d2_mesas(F)
    d6_umbral(F)
    d7_deprecados()


if __name__ == "__main__":
    main()
