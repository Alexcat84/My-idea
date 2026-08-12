#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_razones_d.py . LA COSECHA GRATIS QUE ESTABA EN LAS RAZONES.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo ni un veredicto.

DE DONDE SALE. El control de la muestra pineada de las D encontro, sin buscarlo, que
NUEVE de las veintitres D que sostienen nombran una jerarquia o una arista que falta.
Si eso pasa en el 39% de una muestra de veinticuatro, LO MISMO ESTA ESCRITO EN CIENTOS
DE RAZONES QUE NADIE HA VUELTO A LEER.

QUE HACE: recorre TODAS las D del archivo al corte y levanta aquellas cuya RAZON dice
que hay jerarquia o que falta la arista. No interpreta el texto de los nodos: LEE LO
QUE EL VEREDICTO YA DIJO.

POR QUE ESTOS CANDIDATOS VALEN MAS QUE LOS DEL BARRIDO PASO CONTRA NODO: aquellos son
candidatos de un instrumento de vocabulario, con un 69,6% de acierto medido. ESTOS YA
SE LEYERON, PAR POR PAR, Y EL LECTOR ESCRIBIO QUE FALTABA LA ARISTA. Su evidencia no
es una medida de parecido: es un veredicto.

SENALES FUERTES, y cada una se guarda con la frase que la prueba:
  - la formula de la vara: una linea contra el procedimiento de esa linea
  - CONTINUA, que por el banco 9.6.1 es exactamente eso
  - la arista que falta, no enlaza, madre e hijo, escalera

DEDUPE, en tres frentes:
  1. contra la bolsa de la fase 04 (docs/plan/PASO_NODO_CALIBRADO.jsonl, sin arista)
  2. contra las aristas ya escritas en las operaciones del plan
  3. contra la cola de relectura post fusion de 08_VERIFICACION
Y ademas se descarta el par que YA tenga arista en el grafo, resolviendo por alias.
"""
import argparse, collections, json, io, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

FUERTES = [
    ("formula de la vara", re.compile(r"en UNA LINEA.{0,400}?(trae el procedimiento|procedimiento de esa linea)", re.S)),
    ("procedimiento de esa linea", re.compile(r"procedimiento de esa linea")),
    ("la arista que falta", re.compile(r"ARISTA QUE FALTA|arista que falta|de las que faltan")),
    ("no enlaza", re.compile(r"no enlaza|NO ENLAZA")),
    ("madre e hijo", re.compile(r"madre e hijo|MADRE E HIJO|la madre es .{0,60} el hijo")),
    ("escalera", re.compile(r"escalera")),
    ("continua por la vara", re.compile(r"Por la vara del banco 9\.6\.1, CONTINUA")),
]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--veredictos", default=str(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"))
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--bolsa", default=str(RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"))
    ap.add_argument("--operaciones", default=str(RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"))
    ap.add_argument("--salida", default=str(RAIZ / "docs" / "plan" / "COSECHA_RAZONES_D.jsonl"))
    args = ap.parse_args()

    G = json.load(io.open(args.grafo, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    def par(a, b):
        a, b = res(a), res(b)
        return None if a == b else frozenset((a, b))

    # --- dedupe 1: la bolsa de la fase 04 ---
    bolsa = set()
    for f in cargar(args.bolsa):
        if not f.get("arista"):
            p = par(f["madre"], f["hijo"])
            if p:
                bolsa.add(p)
    # --- dedupe 2: las aristas ya escritas en el plan ---
    escritas = set()
    ids = set(G)
    for o in cargar(args.operaciones):
        for a in (o.get("aristas_nuevas") or []):
            toks = [t for t in re.findall(r"[a-z0-9_]{6,}", a) if t in ids]
            for i in range(len(toks)):
                for j in range(i + 1, len(toks)):
                    p = par(toks[i], toks[j])
                    if p:
                        escritas.add(p)
    # --- dedupe 3: la cola post fusion ---
    COLA = {707, 1096, 196, 253, 224, 591, 968}

    V = cargar(args.veredictos)
    corte = max(r["puesto_intra"] for r in V)
    D = [r for r in V if r["clase"] == "D"]
    filas = []
    for r in D:
        raz = r["razon"] or ""
        senales = [n for n, rx in FUERTES if rx.search(raz)]
        if not senales:
            continue
        p = par(r["nodo_a"], r["nodo_b"])
        if not p:
            continue
        # el par ya tiene arista en el grafo?
        a, b = res(r["nodo_a"]), res(r["nodo_b"])
        con_arista = False
        for x, y in ((a, b), (b, a)):
            if x in G:
                for c in ("nodos_previos", "nodos_siguientes"):
                    if y in [res(z) for z in (G[x].get(c) or [])]:
                        con_arista = True
        m = re.search(r"[^.]{0,180}(en UNA LINEA|procedimiento de esa linea|arista que falta|no enlaza|"
                      r"madre e hijo|ARISTA QUE FALTA)[^.]{0,180}\.", raz)
        cubierto = []
        if con_arista:
            cubierto.append("YA TIENE ARISTA en el grafo")
        if p in bolsa:
            cubierto.append("ya esta en la bolsa de la fase 04")
        if p in escritas:
            cubierto.append("ya tiene arista escrita en una operacion")
        if r["puesto_intra"] in COLA:
            cubierto.append("esta en la cola de relectura post fusion")
        filas.append({"puesto": r["puesto_intra"], "dominio": r["dominio"], "nodo_a": a, "nodo_b": b,
                      "senales": senales, "frase": (m.group(0).strip() if m else raz[:200]),
                      "cubierto_por": cubierto, "nuevo": not cubierto})

    filas.sort(key=lambda f: f["puesto"])
    with io.open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    nuevos = [f for f in filas if f["nuevo"]]
    print("BARRIDO DE RAZONES DE LAS D. corte %d | D en el archivo: %d" % (corte, len(D)))
    print()
    print("| | |")
    print("|---|---:|")
    print("| **D que su razon nombra jerarquia o arista que falta** | **%d** | " % len(filas))
    print("| sobre el total de D | **%.1f%%** |" % (100.0 * len(filas) / max(len(D), 1)))
    print("| ya cubiertos | %d |" % (len(filas) - len(nuevos)))
    print("| **NUEVOS** | **%d** |" % len(nuevos))
    print()
    print("POR QUE ESTABAN CUBIERTOS")
    c = collections.Counter(x for f in filas for x in f["cubierto_por"])
    for k, n in c.most_common():
        print("   %-46s %d" % (k, n))
    print()
    print("REPARTO POR DOMINIO DE LOS NUEVOS")
    print("| dominio | nuevos | levantados |")
    print("|---|---:|---:|")
    cn = collections.Counter(f["dominio"] for f in nuevos)
    ct = collections.Counter(f["dominio"] for f in filas)
    for d in sorted(ct, key=lambda x: -cn.get(x, 0)):
        print("| %s | %d | %d |" % (d, cn.get(d, 0), ct[d]))
    print()
    print("SENALES QUE MAS LEVANTAN")
    for k, n in collections.Counter(x for f in filas for x in f["senales"]).most_common():
        print("   %-30s %d" % (k, n))
    print()
    print("escrito: %s" % args.salida)


if __name__ == "__main__":
    main()
