# -*- coding: utf-8 -*-
"""vuelta91_tarea4_rebase_ope07.py . VUELTA 91, TAREA 4, PRIMERA MITAD: LA
BOLSA DE OP-E-07 (101 puestos, `nuevo == true` con `senales == ["continua
por la vara"]` de docs/plan/COSECHA_RAZONES_D.jsonl), RE-BASADA CONTRA EL
GRAFO DE HOY, ANTES DE LEER NINGUNA RAZON.

POR QUE HACE FALTA. El encargo de la vuelta 91 exige, ANTES de escribir nada
de OP-E-07: "dedupe en los cuatro frentes de OP-E-06, semantica canonica de
resolverId..., y la via de OP-C-05". Este instrumento corre esos cuatro
frentes sobre la bolsa de OP-E-07, con el MISMO codigo que
scripts/loop/vuelta88_tarea5_rebase_ope06.py uso para OP-E-06 (frente 1
contra PASO_NODO_CALIBRADO.jsonl, frente 2 contra aristas_nuevas de
OPERACIONES.jsonl, frente 3 contra la cola de relectura post fusion, frente
4 contra pares con arista YA en el grafo de hoy resolviendo por alias, con
la semantica canonica de resolverId que camina la cadena entera). NO aplica
el filtro de palabras de direccion de OP-E-06: OP-E-07 extrae la direccion
LEYENDO la razon completa, que es la TAREA de la segunda mitad
(vuelta91_tarea4_direccion_ope07.py), no filtrando la frase truncada.

CIFRA ESPERADA: 101 (bolsa de la ficha). Verificado en tiempo de ejecucion:
ROJO si el reparto por dominio no calza con el de la ficha (core 74,
environmental 12, exportacion 11, entrega 4).

SALIDA: docs/plan/OP_E_07_REBASE_V91.jsonl (el remanente tras los cuatro
frentes). NO ESCRIBE NINGUNA ARISTA EN dataset/: eso es una tarea aparte,
posterior a leer la direccion de cada razon.

USO:
  python scripts/loop/vuelta91_tarea4_rebase_ope07.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
COSECHA = os.path.join(PLAN, "COSECHA_RAZONES_D.jsonl")
CALIBRADO = os.path.join(PLAN, "PASO_NODO_CALIBRADO.jsonl")
OPERACIONES = os.path.join(PLAN, "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
SALIDA = os.path.join(PLAN, "OP_E_07_REBASE_V91.jsonl")

# La misma cola de relectura post fusion que uso OP-E-06 (00_INDICE.md linea
# 409, siete puestos, listados en 08_VERIFICACION.md "LA LISTA"): el frente 3
# es del PLAN, no de una operacion, y aplica igual aqui.
COLA_RELECTURA_POST_FUSION = {707, 1096, 196, 253, 224, 591, 968}

REPARTO_ESPERADO_FICHA = {"core": 74, "environmental": 12, "exportacion": 11, "entrega": 4}


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def par_no_dirigido(a, b):
    return tuple(sorted((a, b)))


def resolver_alias(grafo_nodos):
    alias_de = {}
    for nid, n in grafo_nodos.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias_de[a] = nid

    def resolver(nid):
        visto = {nid}
        cur = nid
        while cur in alias_de:
            siguiente = alias_de[cur]
            if siguiente in visto:
                break
            visto.add(siguiente)
            cur = siguiente
        return cur

    return resolver


def main():
    filas = cargar_jsonl(COSECHA)
    bolsa = [r for r in filas if r.get("nuevo") and r.get("senales") == ["continua por la vara"]]

    print("=" * 90)
    print("TAREA 4.a: LA BOLSA DE OP-E-07, TALLADA DE docs/plan/COSECHA_RAZONES_D.jsonl")
    print("=" * 90)
    print("filas totales de la cosecha: %d" % len(filas))
    print("bolsa OP-E-07 (nuevo=true, senales==['continua por la vara']): %d" % len(bolsa))
    reparto = {}
    for r in bolsa:
        reparto[r["dominio"]] = reparto.get(r["dominio"], 0) + 1
    print("reparto por dominio: %s" % reparto)
    if reparto != REPARTO_ESPERADO_FICHA or len(bolsa) != 101:
        print("ROJO: el reparto o la cifra no calzan con la ficha de OP-E-07 (101: core 74, "
              "environmental 12, exportacion 11, entrega 4). NO SE TALLA NADA MAS.")
        return 1
    print()

    # --- LOS CUATRO FRENTES DEL DEDUPE, SOBRE EL GRAFO DE HOY ---
    print("=" * 90)
    print("TAREA 4.b: LOS CUATRO FRENTES DEL DEDUPE, SOBRE EL GRAFO DE HOY")
    print("=" * 90)

    calibrado = cargar_jsonl(CALIBRADO)
    pares_calibrado = {par_no_dirigido(r["madre"], r["hijo"]) for r in calibrado}
    quitados_f1 = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) in pares_calibrado]
    bolsa = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) not in pares_calibrado]
    print("FRENTE 1, contra la bolsa de PASO_NODO_CALIBRADO.jsonl (%d filas hoy): quita %d"
          % (len(calibrado), len(quitados_f1)))
    for r in quitados_f1:
        print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    ops = cargar_jsonl(OPERACIONES)
    patron_flecha = re.compile(r"([a-z0-9_]{4,})\s*->\s*([a-z0-9_]{4,})")
    pares_declarados = set()
    for d in ops:
        for texto in (d.get("aristas_nuevas") or []):
            for m in patron_flecha.finditer(texto):
                pares_declarados.add(par_no_dirigido(m.group(1), m.group(2)))
    quitados_f2 = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) in pares_declarados]
    bolsa = [r for r in bolsa if par_no_dirigido(r["nodo_a"], r["nodo_b"]) not in pares_declarados]
    print("FRENTE 2, contra %d pares ya declarados en aristas_nuevas de otras operaciones: quita %d"
          % (len(pares_declarados), len(quitados_f2)))
    for r in quitados_f2:
        print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    quitados_f3 = [r for r in bolsa if r["puesto"] in COLA_RELECTURA_POST_FUSION]
    bolsa = [r for r in bolsa if r["puesto"] not in COLA_RELECTURA_POST_FUSION]
    print("FRENTE 3, contra los 7 puestos de la cola de relectura post fusion: quita %d"
          % len(quitados_f3))
    for r in quitados_f3:
        print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    grafo = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    resolver = resolver_alias(grafo)

    def existe_arista(a, b):
        ra, rb = resolver(a), resolver(b)
        na, nb = grafo.get(ra), grafo.get(rb)
        if na is None or nb is None:
            return False
        if rb in (na.get("nodos_siguientes") or []) or ra in (nb.get("nodos_previos") or []):
            return True
        if ra in (nb.get("nodos_siguientes") or []) or rb in (na.get("nodos_previos") or []):
            return True
        return False

    quitados_f4 = [r for r in bolsa if existe_arista(r["nodo_a"], r["nodo_b"])]
    bolsa = [r for r in bolsa if not existe_arista(r["nodo_a"], r["nodo_b"])]
    print("FRENTE 4, contra pares con arista YA en el grafo de hoy (resolviendo por alias): quita %d"
          % len(quitados_f4))
    for r in quitados_f4:
        print("  puesto %s: %s -- %s" % (r["puesto"], r["nodo_a"], r["nodo_b"]))
    print()

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for r in bolsa:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("=" * 90)
    print("TAREA 4.c: EL RESULTADO")
    print("=" * 90)
    print("CIFRA VIEJA (12 ago 2026, ficha de OP-E-07): 101")
    print("CIFRA RE-BASADA (29 ago 2026, vuelta 91, sobre el grafo de hoy): %d" % len(bolsa))
    print("escrito: %s" % SALIDA)
    print()
    print("NO SE ESCRIBIO NINGUNA ARISTA. La direccion de cada fila se lee de su razon")
    print("completa en una tarea aparte (vuelta91_tarea4_direccion_ope07.py).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
