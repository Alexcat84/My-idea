# -*- coding: utf-8 -*-
"""vuelta38_ld_racimo.py - LAS TRES LECTURAS DIRIGIDAS DEL CUARTO MIEMBRO DEL RACIMO MIXTO.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo, ni en un nodo, ni en el plan.

SUCESOR DECLARADO de scripts/loop/vuelta37_ld_opd04.py. LO QUE CAMBIA VA DICHO
(regla 2): aquel cubria los TRECE pares internos del acto de SIETE de OP-D-04 por
P.5; este cubre los TRES pares del cuarto miembro del racimo mixto contra el
triangulo del TALLER, que estan FUERA del acto y por tanto FUERA del alcance de
P.5, y solo se pueden leer por la EXCEPCION DE UNA VEZ autorizada por el fundador
el 19 ago 2026 y registrada junto a P.5 en docs/plan/BANCO_DEL_PLAN.md.

LO QUE MIDE, todo hoy y nada heredado:
  1. LA NUMERACION LIBRE: barrido de docs/ entero por la cadena LD- seguida de
     digitos. Se imprime el numero mas alto escrito y donde vive.
  2. LOS CUATRO NODOS VIVOS con los pasos que tienen hoy y su dominio, porque la
     excepcion se autoriza precisamente porque el cuarto es de otro dominio.
  3. QUE NINGUNO DE LOS TRES PARES TIENE VEREDICTO en el archivo, en los dos
     ordenes.
  4. QUE NINGUNO DE LOS TRES ESTA EN LA COLA (docs/INTRA_DOMINIO_PARES.jsonl, en
     los dos ordenes). Si alguno estuviera, no seria lectura dirigida sino par
     saltado, y moveria n.
  5. LAS TRES ARISTAS EN LOS DOS SENTIDOS, resueltas por el resolutor de alias
     antes de comparar (P.1), leidas del grafo compilado.
  6. LOS CUATRO NODOS IMPRESOS ENTEROS, campo por campo, antes de decidir nada.

Uso: python scripts/loop/vuelta38_ld_racimo.py
"""
import io
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

CUARTO = "brainstorming"
TALLER = [
    "brainstorming_divergente",
    "brainstorming_efectivo",
    "reglas_brainstorming",
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


def imprimir_entero(nid, d):
    print("")
    print("-" * 78)
    print("NODO: %s" % nid)
    print("-" * 78)
    print("  dominio           : %s" % d.get("dominio"))
    print("  fase_proyecto     : %s" % d.get("fase_proyecto"))
    print("  titulo_concepto   : %s" % d.get("titulo_concepto"))
    print("  fuente            : %s" % d.get("fuente"))
    print("  etiqueta_arbol    : %s" % d.get("etiqueta_arbol"))
    print("  deprecado         : %s" % d.get("deprecado"))
    print("  resumen_teorico   :")
    for linea in (d.get("resumen_teorico") or "").split("\n"):
        print("      %s" % linea)
    pasos = d.get("pasos_accionables") or []
    print("  pasos_accionables : %d" % len(pasos))
    for i, p in enumerate(pasos, 1):
        print("      %d. %s" % (i, p))
    print("  entregable_esperado:")
    for linea in (d.get("entregable_esperado") or "").split("\n"):
        print("      %s" % linea)
    print("  condiciones_activacion: %s" % json.dumps(
        d.get("condiciones_activacion"), ensure_ascii=False))
    print("  nodos_previos     : %s" % json.dumps(
        d.get("nodos_previos") or [], ensure_ascii=False))
    print("  nodos_siguientes  : %s" % json.dumps(
        d.get("nodos_siguientes") or [], ensure_ascii=False))


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

    bloque("2. LOS CUATRO NODOS DE HOY, con su dominio")
    datos = {}
    for nid in [CUARTO] + TALLER:
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        datos[nid] = d
        print("  %-38s %-12s %d pasos   vivo %s"
              % (nid, d.get("dominio"), len(d.get("pasos_accionables") or []),
                 not d.get("deprecado", False)))
    dom_cuarto = datos[CUARTO].get("dominio")
    doms_taller = set(datos[n].get("dominio") for n in TALLER)
    print("")
    print("  el cuarto es de %s; los tres del taller son de %s"
          % (dom_cuarto, ", ".join(sorted(doms_taller))))
    print("  RACIMO MIXTO CONFIRMADO POR MEDICION: %s"
          % ("SI" if dom_cuarto not in doms_taller else "NO"))

    bloque("3. LOS TRES PARES: ninguno debe tener veredicto")
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v
    print("  docs/INTRA_DOMINIO_VEREDICTOS.jsonl leido: %d filas" % len(V))
    con = []
    for b in TALLER:
        v = por_par.get((CUARTO, b))
        estado = "SIN VEREDICTO" if v is None else (
            "puesto %s clase %s" % (v.get("puesto_intra"), v.get("clase")))
        if v is not None:
            con.append((b, v))
        print("  %-14s contra %-38s %s" % (CUARTO, b, estado))
    if con:
        print("")
        print("  ABORTA: %d de los tres YA tienen veredicto" % len(con))
        return 1
    print("")
    print("  GUARDA OK: los tres estan sin veredicto.")

    bloque("4. NINGUNO DE LOS TRES ESTA EN LA COLA")
    en_cola = set()
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
    hallados = [b for b in TALLER if (CUARTO, b) in en_cola]
    for b in TALLER:
        print("  %-14s contra %-38s en la cola: %s"
              % (CUARTO, b, "SI" if (CUARTO, b) in en_cola else "no"))
    print("")
    if hallados:
        print("  ABORTA: %d de los tres SI estan en la cola" % len(hallados))
        return 1
    print("  GUARDA OK: los tres son fuera de cola. Son LECTURA DIRIGIDA y NO mueven n.")
    print("  n sigue en %d." % total)

    bloque("5. LAS TRES ARISTAS, EN LOS DOS SENTIDOS, RESUELTAS POR ALIAS (P.1)")
    grafo = cargar_grafo()
    alias = {}
    for nid, n in grafo.items():
        for al in (n.get("ids_alias") or []):
            alias[al] = nid
    print("  nodos en el grafo compilado: %d    alias indexados: %d"
          % (len(grafo), len(alias)))
    print("")
    a = CUARTO
    for b in TALLER:
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
        print("  %-14s %-38s %s" % (a, b, estado))
        print("       a.siguientes=%s" % json.dumps(sig_a, ensure_ascii=False))
        print("       a.previos   =%s" % json.dumps(pre_a, ensure_ascii=False))
        print("       b.siguientes=%s" % json.dumps(sig_b, ensure_ascii=False))
        print("       b.previos   =%s" % json.dumps(pre_b, ensure_ascii=False))

    bloque("6. LOS CUATRO NODOS ENTEROS, ANTES DE DECIDIR NADA")
    for nid in [CUARTO] + TALLER:
        imprimir_entero(nid, datos[nid])

    bloque("VEREDICTO DE LA GUARDA")
    print("numeracion libre desde LD-%d; los tres pares sin veredicto y fuera de cola;"
          % (mayor + 1))
    print("los cuatro nodos vivos e impresos enteros; las tres aristas medidas en los")
    print("dos sentidos. SE PUEDE LEER, por la EXCEPCION DE UNA VEZ de P.5 (19 ago 2026).")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
