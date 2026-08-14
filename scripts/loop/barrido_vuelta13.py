#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_vuelta13.py . TAREA 2.A vuelta 13: mide pares y actos en los dos
cortes (2117 y 3388) para las operaciones que quedaron fuera del barrido
anterior. SOLO LECTURA. Modelado sobre scripts/plan/recomputo_3388.py.
"""
import io
import itertools
import json
import subprocess
import collections
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def cargar_jsonl_texto(texto):
    return [json.loads(l) for l in texto.splitlines() if l.strip()]


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def git_show(hash_, ruta):
    out = subprocess.run(["git", "show", "%s:%s" % (hash_, ruta)], cwd=str(RAIZ),
                          capture_output=True, encoding="utf-8")
    if out.returncode != 0:
        raise RuntimeError(out.stderr)
    return out.stdout


class Corte:
    def __init__(self, nombre, veredictos, G, ALIAS):
        self.nombre = nombre
        self.V = veredictos
        self.G = G
        self.ALIAS = ALIAS
        self._construir()

    def res(self, x):
        visto = set()
        while x in self.ALIAS and x not in visto:
            visto.add(x)
            x = self.ALIAS[x]
        return x

    def _construir(self):
        a_crudas = [r for r in self.V if r["clase"] == "A"]
        retrato = {}
        for r in a_crudas:
            ra, rb = self.res(r["nodo_a"]), self.res(r["nodo_b"])
            if ra == rb:
                continue
            key = frozenset((ra, rb))
            retrato.setdefault(key, []).append(r)
        self.retrato = retrato

        leido = {}
        for r in self.V:
            ra, rb = self.res(r["nodo_a"]), self.res(r["nodo_b"])
            if ra == rb:
                continue
            leido[frozenset((ra, rb))] = r
        self.leido = leido

        ady = collections.defaultdict(set)
        for (ra, rb) in retrato:
            ady[ra].add(rb)
            ady[rb].add(ra)
        vistos = set()
        componentes = []
        for n in list(ady):
            if n in vistos:
                continue
            pila = [n]
            c = set()
            while pila:
                x = pila.pop()
                if x in c:
                    continue
                c.add(x)
                pila.extend(ady[x] - c)
            vistos |= c
            componentes.append(c)
        self.componentes = [c for c in componentes if len(c) >= 2]
        # mapa nodo resuelto -> componente (indice)
        self.nodo_a_comp = {}
        for i, c in enumerate(self.componentes):
            for n in c:
                self.nodo_a_comp[n] = i

    def medir_nomina(self, nomina):
        resueltos = sorted(set(self.res(n) for n in nomina))
        pares = list(itertools.combinations(sorted(nomina), 2))
        # pares posibles se cuentan sobre la nomina cruda (banco: nomina declarada),
        # pero resolver antes de comparar contra leido (P.1)
        leidos = []
        clases = collections.Counter()
        for a, b in pares:
            ra, rb = self.res(a), self.res(b)
            if ra == rb:
                continue
            key = frozenset((ra, rb))
            if key in self.leido:
                leidos.append((a, b))
                clases[self.leido[key]["clase"]] += 1
        actos_tocados = set()
        nodos_en_acto = set()
        for n in resueltos:
            if n in self.nodo_a_comp:
                actos_tocados.add(self.nodo_a_comp[n])
                nodos_en_acto.add(n)
        return {
            "n_nomina": len(nomina),
            "n_resueltos": len(resueltos),
            "pares_posibles": len(pares),
            "pares_leidos": len(leidos),
            "clases": dict(clases),
            "A": clases.get("A", 0),
            "actos_tocados": len(actos_tocados),
            "nodos_en_acto": len(nodos_en_acto),
            "detalle_actos": [(sorted(self.componentes[i]), len(self.componentes[i])) for i in sorted(actos_tocados)],
        }


def main():
    G = json.load(io.open(RAIZ / "dataset" / "metadata" / "master_graph.json", encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    V_nuevo = cargar_jsonl(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl")
    texto_viejo = git_show("c16a24f5", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    V_viejo = cargar_jsonl_texto(texto_viejo)
    assert len(V_viejo) == 2117, len(V_viejo)
    assert max(r["puesto_intra"] for r in V_nuevo) == 3388

    c2117 = Corte("2117", V_viejo, G, ALIAS)
    c3388 = Corte("3388", V_nuevo, G, ALIAS)

    ops = cargar_jsonl(RAIZ / "docs" / "plan" / "OPERACIONES.jsonl")
    dops = {o["id_op"]: o for o in ops}

    universo = ["OP-F-01", "OP-F-02", "OP-F-03", "OP-F-04-COL", "OP-F-04-HOR", "OP-F-04-WEI", "OP-F-04-RAC",
                "OP-S-01", "OP-S-02", "OP-S-03", "OP-S-04", "OP-S-05", "OP-S-06", "OP-S-07", "OP-S-08",
                "OP-S-09", "OP-S-10", "OP-S-11", "OP-S-12",
                "OP-D-07", "OP-E-04", "OP-E-05", "OP-E-01", "OP-E-02",
                "OP-C-01", "OP-C-02", "OP-C-03", "OP-C-04", "OP-C-05",
                "OP-A-01", "OP-A-02", "OP-V-01", "OP-I-01", "OP-L-01", "OP-L-03"]

    for idop in universo:
        o = dops.get(idop)
        if o is None:
            print("%s: NO EXISTE EN OPERACIONES.jsonl" % idop)
            continue
        nom = o["nodos"]
        print("=" * 70)
        print("%s | tipo=%s | fase=%s | nomina=%d" % (idop, o["tipo"], o["fase"], len(nom)))
        if len(nom) < 2:
            print("  nomina < 2: sin pares que comparar entre cortes (razonamiento en el reporte)")
            continue
        m17 = c2117.medir_nomina(nom)
        m88 = c3388.medir_nomina(nom)
        cambia = (m17["pares_leidos"] != m88["pares_leidos"] or m17["A"] != m88["A"]
                  or m17["actos_tocados"] != m88["actos_tocados"] or m17["nodos_en_acto"] != m88["nodos_en_acto"])
        print("  2117: pares_posibles=%d leidos=%d (A=%d) | actos_tocados=%d sobre %d nodos"
              % (m17["pares_posibles"], m17["pares_leidos"], m17["A"], m17["actos_tocados"], m17["nodos_en_acto"]))
        print("  3388: pares_posibles=%d leidos=%d (A=%d) | actos_tocados=%d sobre %d nodos"
              % (m88["pares_posibles"], m88["pares_leidos"], m88["A"], m88["actos_tocados"], m88["nodos_en_acto"]))
        print("  CAMBIA: %s" % cambia)
        if cambia:
            print("  DETALLE ACTOS 2117: %s" % m17["detalle_actos"])
            print("  DETALLE ACTOS 3388: %s" % m88["detalle_actos"])


if __name__ == "__main__":
    main()
