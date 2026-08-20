# -*- coding: utf-8 -*-
"""vuelta58_varas_tramo.py . EL CUADRO DE VARAS DE LOS ACTOS DE UN TRAMO,
UNA FILA POR ACTO, CON LA FORMA DEL VEREDICTO IMPRESA.

NOMBRE ESTABLE Y SIN NUMERO DE TRAMO, a proposito y por la misma via que el
tallador de la cabecera del reporte: el tramo se pasa en --tramo y el titulo se
arma SOLO. Este fichero no se clona cada vuelta.

SUCESOR DECLARADO de scripts/loop/vuelta56_varas_tramo3.py, al que NO reemplaza
y CUYA ARITMETICA SE COPIA ENTERA (el fichero se copio byte a byte y solo
despues se le cambio el titulo; el ancestro queda intacto y re-corrible). La via
es la del acta 54 pregunta 3 (linea 13381 de ACTA_AUDITOR.md): las cifras del
ancestro YA estan citadas por un registro (el del tramo 2, en la linea 1647 de
docs/plan/03_FUSIONES.md, cita SALIDA_V54_VARAS_TRAMO2.txt), asi que la logica
NO se toca y se escribe sucesor.

POR QUE NACE, y es una de las DOS OBSERVACIONES SIN ESPECIE del acta 57 (seccion
3): el ancestro lleva el titulo TALLADO A MANO y ENVEJECIDO. Corrido sobre el
fichero del tramo 4 en la vuelta 57, imprimio "EL CUADRO DE VARAS DE LOS 50
ACTOS DEL TRAMO 3 (vuelta 54)" sobre los actos del TRAMO 4 de la VUELTA 57
(SALIDA_V57_VARAS_TRAMO4.txt, primera linea del cuadro). El numero de tramo
estaba escrito como CONSTANTE en el print y no salia de ningun sitio medido, que
es la misma especie que la racha de la cabecera del reporte pago tres veces.

LO UNICO QUE CAMBIA, Y ES SOLO EL TITULO: EL NUMERO DE TRAMO SALE DEL FICHERO
(se lee de la clave del ordinal, que este instrumento ya descubria por su cuenta:
orden_tramo4 dice tramo 4) Y LA VUELTA SALE DEL ARGUMENTO. Ninguna celda de la
aritmetica se toca. Ademas el cuadro imprime la ruta del fichero del tramo, para
que la salida diga sola sobre que se corrio.

DEL ANCESTRO SE CONSERVA su propia unica novedad: LA CLAVE DEL ORDINAL SE
DESCUBRE DEL FICHERO en vez de estar escrita a mano, y si hay ninguna o mas de
una es ROJO y PARA.

DE SOLO LECTURA. Imprime; no toca nada.

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
  python scripts/loop/vuelta58_varas_tramo.py --tramo docs/loop/TRAMO5_V58.jsonl --vuelta 58
"""

import argparse
import io
import json
import os
import re
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
    ap.add_argument("--vuelta", type=int, default=None,
                    help="la vuelta que corre el cuadro; va en el titulo. Sin ella "
                         "el titulo no la nombra, en vez de heredar una vieja.")
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
    # LO UNICO QUE NO ES COPIA: la clave del ordinal se descubre del fichero.
    claves = sorted({k for k in tramo[0] if k.startswith("orden_tramo")}) if tramo else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    # LO UNICO QUE CAMBIA: el numero de tramo sale de la clave del ordinal que el
    # propio fichero trae (orden_tramo4 dice tramo 4), no de una constante. Si la
    # clave no lleva numero, el titulo lo dice en vez de inventarse uno.
    m = re.search(r"(\d+)$", ORD)
    num_tramo = m.group(1) if m else "SIN NUMERO EN LA CLAVE %s" % ORD

    print("=" * 110)
    print("EL CUADRO DE VARAS DE LOS %d ACTOS DEL TRAMO %s%s"
          % (len(tramo), num_tramo,
             "" if a.vuelta is None else " (vuelta %d)" % a.vuelta))
    print("  fichero del tramo: %s" % a.tramo)
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
              % (act[ORD], mi[0], mi[1],
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
