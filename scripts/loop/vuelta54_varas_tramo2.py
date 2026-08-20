# -*- coding: utf-8 -*-
"""vuelta54_varas_tramo2.py . EL CUADRO DE VARAS DE LOS 50 ACTOS DEL TRAMO 2,
UNA FILA POR ACTO, CON LA FORMA DEL VEREDICTO IMPRESA.

DE SOLO LECTURA. Imprime; no toca nada.

POR QUE EXISTE Y QUE CORRIGE DE MI PROPIO INSTRUMENTO ANTERIOR: la mesa
(scripts/loop/vuelta54_mesa_tramo2.py) imprime una columna MATERIAL PROPIO
calculada por SOLAPE LEXICO. Esa columna es un CONTRASTE DE MAQUINA y NO es la
vara: la receta define el contenido como "pasos y condiciones, material propio
y padre declarado EN LAS RAZONES", y el material propio de la receta es el que
LA RAZON DECLARA, no el que un contador de palabras estima. Aqui las varas que
deciden son SOLO las contables sin interpretacion (pasos y condiciones) mas el
cableado, y la pieza declarada la pone la lectura, no la maquina.

LA FORMA que imprime por acto, que es lo que la receta ratificada distingue:

  TODAS DE ACUERDO   las varas de contenido que no empatan apuntan al mismo
                     lado. Se funde hacia ese lado.
  UNA SOLA VARA      solo una vara de contenido no empata. BASTA (acta de la
                     vuelta 53, pregunta 4).
  CHOCAN             dos varas de contenido apuntan a lados distintos. Decide
                     LA PIEZA DECLARADA de mayor peso en las razones; si no
                     hay ninguna, es PARADA (acta 53, pregunta 3).
  CONTENIDO EMPATA   ninguna vara de contenido separa. Decide EL CABLEADO SOLO.
  EMPATE SIN VARA    tampoco el cableado separa. Se DECLARA.

Uso:
  python scripts/loop/vuelta54_varas_tramo2.py --tramo docs/loop/TRAMO2_V54.jsonl
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def protegidos():
    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    pue = set()
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    pue.add(x[extremo])
    return sem | pue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    entra = {}
    for k, v in G.items():
        if v.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (v.get(c) or []):
                entra.setdefault(res(y), set()).add(k)

    prot = protegidos()
    tramo = cargar(a.tramo)

    print("=" * 110)
    print("EL CUADRO DE VARAS DE LOS %d ACTOS DEL TRAMO 2 (vuelta 54)" % len(tramo))
    print("=" * 110)
    print()
    print("  pasos y cond son las varas de CONTENIDO contables; cab es el CABLEADO,")
    print("  que por P.8 solo habla a contenido empatado. La flecha dice a que lado")
    print("  apunta cada vara: 1 el primer miembro por orden alfabetico, 2 el segundo.")
    print()
    print("  %-3s %-46s %-46s %5s %5s %5s %-18s %s"
          % ("#", "miembro 1", "miembro 2", "pasos", "cond", "cab", "FORMA", "puerta"))

    formas = {}
    for act in tramo:
        mi = sorted(act["miembros"])
        d = []
        for x in mi:
            o = json.load(io.open(os.path.join(NODOS, x + ".json"), encoding="utf-8"))
            d.append({
                "id": x,
                "pasos": len(o.get("pasos_accionables") or []),
                "cond": len(o.get("condiciones_activacion") or []),
                "cab": len({res(y) for c in CAMPOS for y in (o.get(c) or [])} - {res(x)}),
            })

        def flecha(k):
            if d[0][k] > d[1][k]:
                return 1
            if d[1][k] > d[0][k]:
                return 2
            return 0

        fp, fc, fk = flecha("pasos"), flecha("cond"), flecha("cab")
        conte = [x for x in (fp, fc) if x]
        if not conte:
            forma = "CONTENIDO EMPATA" if fk else "EMPATE SIN VARA"
        elif len(set(conte)) == 2:
            forma = "CHOCAN"
        elif len(conte) == 1:
            forma = "UNA SOLA VARA"
        else:
            forma = "TODAS DE ACUERDO"
        formas[forma] = formas.get(forma, 0) + 1

        puerta = [x["id"] for x in d if x["id"] in prot]
        print("  %-3d %-46s %-46s %2d/%-2d %s %2d/%-2d %s %2d/%-2d %s %-18s %s"
              % (act["orden_tramo2"], mi[0], mi[1],
                 d[0]["pasos"], d[1]["pasos"], "" if not fp else str(fp),
                 d[0]["cond"], d[1]["cond"], "" if not fc else str(fc),
                 d[0]["cab"], d[1]["cab"], "" if not fk else str(fk),
                 forma, ("SI: " + ", ".join(puerta)) if puerta else ""))

    print()
    print("  POR FORMA: %s" % formas)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
