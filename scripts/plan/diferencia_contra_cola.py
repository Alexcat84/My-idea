#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""diferencia_contra_cola.py . LA DIFERENCIA DEL BARRIDO CONTRA LA COLA DEL CRIBADO.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo.

PARA QUE EXISTE, y es la adjudicacion del 11 ago 2026: el barrido calibrado NO
abre una puerta nueva al cribado. Se corre EL DIA EN QUE LA COLA DE UN DOMINIO
CIERRA, y solo se pregunta una cosa:

    de los candidatos que el barrido levanto en ese dominio,
    CUALES NO ESTABAN EN LA COLA?

Esa diferencia, y nada mas que esa diferencia, va a LECTURAS DIRIGIDAS. Lo que ya
estaba en la cola no se lee dos veces: la cola lo cubre por su cuenta y su
veredicto vale por los dos caminos.

POR QUE ASI Y NO ABRIENDO EL BARRIDO COMO FUENTE: porque una lectura que entra por
dos puertas se cuenta dos veces, y entonces la tasa por dominio del banco 9.27 deja
de significar nada. La diferencia contra la cola es la unica forma de sumar sin
contar doble.

ENTRADA
  --cola        docs/INTRA_DOMINIO_PARES.jsonl      (los pares que la cola planifico)
  --veredictos  docs/INTRA_DOMINIO_VEREDICTOS.jsonl (los pares ya leidos)
  --candidatos  docs/plan/PASO_NODO_CALIBRADO.jsonl (la bolsa calibrada)
  --dominio     el dominio que acaba de cerrar; se puede repetir; sin el, todos

SALIDA
  la diferencia por dominio, con su cuenta, y el detalle a
  docs/plan/DIFERENCIA_CONTRA_COLA.jsonl

REGLA P.1 DEL BANCO DEL PLAN: todo conteo que toque ids pasa por el resolutor antes
de contar. Aqui importa de verdad: el barrido nombra nodos vivos, pero la cola se
escribio antes de fusiones y renombres, y comparar literal daria diferencias falsas.

LA SALIDA PISA, Y ES A PROPOSITO, CON LA COSTUMBRE DECLARADA (vuelta 95, TAREA
4.c del encargo). `--salida` por defecto siempre escribe
`docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`: es LA DIFERENCIA VIGENTE, la del
barrido mas reciente, y cada corrida nueva reemplaza a la anterior a
proposito (no tiene sentido leer dos veces la diferencia de dos barridos
distintos del mismo dominio). Lo que rompio la costumbre buena de esta casa
(una salida por vuelta, ninguna pisada) fue que la corrida de agosto (387
filas, commit `88b3f7c6`) se perdio SIN QUEDAR CITADA en ningun lado antes de
que la corrida de la vuelta 94 (183 filas, commit `4c22a083`) la pisara: no
hay como reconstruir HOY que llevaba esa corrida vieja salvo yendo a git. Esa
corrida vieja quedo recuperada, una sola vez, en
`docs/plan/DIFERENCIA_CONTRA_COLA_ENSAYO_AGOSTO.jsonl` (fichero de contraste
historico, con nombre propio, nunca vuelto a escribir por este script). Si
una vuelta futura necesita conservar DOS diferencias vigentes a la vez (por
ejemplo, dos dominios que cierran en corridas separadas y hay que comparar
ambas), usar `--salida` (ya existe, arriba) con un nombre versionado
explicito en vez de dejar la corrida nueva pisar la vieja en silencio.
"""
import argparse, collections, json, io, os, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--cola", default=str(RAIZ / "docs" / "INTRA_DOMINIO_PARES.jsonl"))
    ap.add_argument("--veredictos", default=str(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"))
    ap.add_argument("--candidatos", default=str(RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"))
    ap.add_argument("--salida", default=str(RAIZ / "docs" / "plan" / "DIFERENCIA_CONTRA_COLA.jsonl"))
    ap.add_argument("--dominio", action="append", default=None,
                    help="dominio que acaba de cerrar; repetible. Sin el, todos los dominios.")
    ap.add_argument("--solo-sin-arista", action="store_true", default=True)
    args = ap.parse_args()

    G = json.load(io.open(args.grafo, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        """EL RESOLUTOR, con la semantica de resolverId del motor: camina la cadena
        de alias hasta el id final, sin ciclar."""
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    def par(a, b):
        a, b = res(a), res(b)
        return None if a == b else frozenset((a, b))

    cola = set()
    for r in cargar(args.cola):
        p = par(r["nodo_a"], r["nodo_b"])
        if p:
            cola.add(p)
    for r in cargar(args.veredictos):
        p = par(r["nodo_a"], r["nodo_b"])
        if p:
            cola.add(p)

    cand = cargar(args.candidatos)
    if args.solo_sin_arista:
        cand = [f for f in cand if not f.get("arista")]
    doms = set(args.dominio) if args.dominio else None

    vistos, filas = set(), []
    dentro = collections.Counter()
    fuera = collections.Counter()
    repe = collections.Counter()   # filas que son el MISMO par por otro paso de la misma madre
    for f in cand:
        d = f.get("dominio") or "?"
        if doms and d not in doms:
            continue
        p = par(f["madre"], f["hijo"])
        if not p:
            continue
        if p in cola:
            dentro[d] += 1
            continue
        if p in vistos:
            repe[d] += 1
            continue
        vistos.add(p)
        fuera[d] += 1
        filas.append({"dominio": d, "madre": res(f["madre"]), "hijo": res(f["hijo"]),
                      "paso": f["paso"], "texto_paso": f["texto_paso"],
                      "titulo_hijo": f.get("titulo_hijo"),
                      "titulo_ratio": f.get("titulo_ratio"), "contencion": f.get("contencion"),
                      "familia_paso": f.get("familia_paso"), "familia_hijo": f.get("familia_hijo"),
                      "origen": "barrido calibrado, diferencia contra la cola"})

    with io.open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
        for x in filas:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")

    print("DIFERENCIA CONTRA LA COLA. dominios: %s" % (", ".join(sorted(doms)) if doms else "todos"))
    print()
    print("| dominio | filas | par repetido | YA en la cola | **DIFERENCIA** |")
    print("|---|---:|---:|---:|---:|")
    tot = lambda d: dentro[d] + fuera[d] + repe[d]
    for d in sorted(set(list(dentro) + list(fuera) + list(repe)), key=lambda x: -tot(x)):
        print("| %s | %d | %d | %d | **%d** |" % (d, tot(d), repe[d], dentro[d], fuera[d]))
    print("| **TOTAL** | **%d** | **%d** | **%d** | **%d** |"
          % (sum(dentro.values()) + sum(fuera.values()) + sum(repe.values()),
             sum(repe.values()), sum(dentro.values()), sum(fuera.values())))
    print()
    print("pares distintos en la diferencia (sin repetir por varios pasos de la misma madre): %d" % len(vistos))
    print("escrito: %s" % args.salida)
    print()
    print("LO QUE SIGUE, y no lo hace este script: la diferencia va a LECTURAS DIRIGIDAS,")
    print("se marca como tal, NO entra en la cola y NO mueve el marcador del cribado.")


if __name__ == "__main__":
    main()
