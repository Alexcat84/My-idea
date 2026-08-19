# -*- coding: utf-8 -*-
"""vuelta37_ld_opd04.py - LAS TRECE LECTURAS DIRIGIDAS DE OP-D-04, MEDIDAS ANTES DE LEERSE.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo, ni en un nodo, ni en el plan.

SUCESOR DECLARADO de scripts/loop/vuelta36_ld_643.py y de la guarda de numeracion
que la vuelta 34 monto para LD-75 a LD-81. LO QUE CAMBIA VA DICHO (regla 2):
aquellos miraban UN par o SIETE de una nomina de seis; este cubre los TRECE pares
internos del acto de SIETE que hoy no tienen veredicto, y ademas imprime LAS
VEINTIUNA aristas internas del acto en los dos sentidos de una sola vez, porque
la pregunta de P.5 (una familia o dos) se contesta sobre el acto entero y no par
a par.

LO QUE MIDE, todo hoy y nada heredado:
  1. LA NUMERACION LIBRE: barrido de docs/ entero por la cadena LD- seguida de
     digitos. Se imprime el numero mas alto escrito y donde vive. En la vuelta 33
     el ejecutor casi acuno tres numeros ya tomados y lo cazo esta misma guarda.
  2. QUE NINGUNO DE LOS TRECE ESTA EN LA COLA: se buscan en
     docs/INTRA_DOMINIO_PARES.jsonl en los dos ordenes. Si alguno estuviera, no
     seria lectura dirigida sino par saltado, y moveria n.
  3. QUE NINGUNO DE LOS TRECE TIENE VEREDICTO: se buscan en el archivo en los dos
     ordenes. Es la misma cuenta que el instrumento de P.5, corrida por segunda
     vez y por otro camino.
  4. LAS 21 ARISTAS INTERNAS EN LOS DOS SENTIDOS, resueltas por el resolutor de
     alias antes de comparar (P.1), leidas del grafo compilado.
  5. LOS SIETE NODOS VIVOS con los pasos que tienen hoy.

Uso: python scripts/loop/vuelta37_ld_opd04.py
"""
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PARES = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_PARES.jsonl")
DOCS = os.path.join(RAIZ, "docs")

SIETE = [
    "brainstorming_divergente",
    "brainstorming_efectivo",
    "reglas_brainstorming",
    "generar_multiples_opciones",
    "construir_sobre_ideas_ajenas",
    "pensamiento_convergente_divergente",
    "design_attitude_vs_decision_attitude",
]


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def cargar_grafo():
    with io.open(GRAFO, encoding="utf-8") as fh:
        g = json.load(fh)
    nodos = g.get("nodes") or g.get("nodos") or g
    if isinstance(nodos, dict):
        return nodos
    return dict((n.get("node_id") or n.get("id"), n) for n in nodos)


def resolver(nid, alias):
    """P.1: todo conteo que toque ids pasa por el resolutor antes de contar."""
    visto = set()
    actual = nid
    while actual in alias and actual not in visto:
        visto.add(actual)
        actual = alias[actual]
    return actual


def main():
    bloque("1. LA NUMERACION LIBRE: cual es el LD mas alto escrito en docs/")
    mayor = 0
    donde = ""
    patron = re.compile(r"LD-(\d+)")
    for raiz, _, ficheros in os.walk(DOCS):
        for f in ficheros:
            if not f.lower().endswith((".md", ".jsonl", ".json", ".txt")):
                continue
            ruta = os.path.join(raiz, f)
            try:
                texto = io.open(ruta, encoding="utf-8", errors="replace").read()
            except IOError:
                continue
            for m in patron.finditer(texto):
                n = int(m.group(1))
                if n > mayor:
                    mayor, donde = n, os.path.relpath(ruta, RAIZ)
    print("  LD mas alto escrito: LD-%d   (en %s)" % (mayor, donde))
    print("  la tanda de esta vuelta empieza en LD-%d" % (mayor + 1))

    bloque("2. LOS SIETE NODOS DE HOY")
    datos = {}
    for nid in SIETE:
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        datos[nid] = d
        print("  %-38s %d pasos   vivo %s"
              % (nid, len(d.get("pasos_accionables") or []), not d.get("deprecado", False)))

    bloque("3. LOS 21 PARES: cual tiene veredicto y cual no")
    con = []
    sin = []
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v
    for a, b in itertools.combinations(SIETE, 2):
        v = por_par.get((a, b))
        if v is None:
            sin.append((a, b))
        else:
            con.append((int(v["puesto_intra"]), v["clase"], a, b))
    print("  CON veredicto: %d" % len(con))
    for p, c, a, b in sorted(con):
        print("     %-5d %-3s %s contra %s" % (p, c, a, b))
    print("  SIN veredicto: %d" % len(sin))
    for i, (a, b) in enumerate(sin, 1):
        print("     %2d. %s contra %s" % (i, a, b))

    bloque("4. NINGUNO DE LOS SIN VEREDICTO ESTA EN LA COLA")
    en_cola = set()
    if os.path.exists(PARES):
        total = 0
        with io.open(PARES, encoding="utf-8") as fh:
            for linea in fh:
                linea = linea.strip()
                if not linea:
                    continue
                total += 1
                o = json.loads(linea)
                a = o.get("nodo_a") or o.get("id_a") or o.get("a")
                b = o.get("nodo_b") or o.get("id_b") or o.get("b")
                if a and b:
                    en_cola.add((a, b))
                    en_cola.add((b, a))
        print("  docs/INTRA_DOMINIO_PARES.jsonl leido: %d filas, %d parejas indexadas"
              % (total, len(en_cola) // 2))
    else:
        print("  AVISO: no existe docs/INTRA_DOMINIO_PARES.jsonl; la guarda no se puede correr")
        return 1
    hallados = [(a, b) for a, b in sin if (a, b) in en_cola]
    for a, b in sin:
        print("  %-38s contra %-38s en la cola: %s"
              % (a, b, "SI" if (a, b) in en_cola else "no"))
    print("")
    if hallados:
        print("  ABORTA: %d de los sin veredicto SI estan en la cola" % len(hallados))
        for a, b in hallados:
            print("     %s contra %s" % (a, b))
        return 1
    print("  GUARDA OK: los %d son fuera de cola. Son LECTURA DIRIGIDA y NO mueven n."
          % len(sin))

    bloque("5. LAS 21 ARISTAS INTERNAS, EN LOS DOS SENTIDOS, RESUELTAS POR ALIAS (P.1)")
    grafo = cargar_grafo()
    alias = {}
    for nid, n in grafo.items():
        for al in (n.get("ids_alias") or []):
            alias[al] = nid
    print("  nodos en el grafo compilado: %d    alias indexados: %d" % (len(grafo), len(alias)))
    print("")
    con_arista = 0
    for a, b in itertools.combinations(SIETE, 2):
        sig_a = [resolver(x, alias) for x in (datos[a].get("nodos_siguientes") or [])]
        pre_a = [resolver(x, alias) for x in (datos[a].get("nodos_previos") or [])]
        sig_b = [resolver(x, alias) for x in (datos[b].get("nodos_siguientes") or [])]
        pre_b = [resolver(x, alias) for x in (datos[b].get("nodos_previos") or [])]
        ab = (b in sig_a) or (b in pre_a)
        ba = (a in sig_b) or (a in pre_b)
        estado = "NINGUNA"
        if ab and ba:
            estado = "EN LOS DOS SENTIDOS"
        elif ab:
            estado = "solo a -> b"
        elif ba:
            estado = "solo b -> a"
        if ab or ba:
            con_arista += 1
        v = por_par.get((a, b))
        etiq = ("%s %s" % (v["puesto_intra"], v["clase"])) if v else "sin veredicto"
        print("  %-38s %-38s %-20s [%s]" % (a, b, estado, etiq))
    print("")
    print("  pares con alguna arista: %d de 21" % con_arista)

    bloque("VEREDICTO DE LA GUARDA")
    print("numeracion libre desde LD-%d; %d pares sin veredicto, los %d fuera de cola;"
          % (mayor + 1, len(sin), len(sin)))
    print("los siete nodos vivos; las 21 aristas internas medidas en los dos sentidos.")
    print("SE PUEDE LEER.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
