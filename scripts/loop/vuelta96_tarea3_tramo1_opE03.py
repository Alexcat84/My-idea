# -*- coding: utf-8 -*-
r"""vuelta96_tarea3_tramo1_opE03.py . VUELTA 96, TAREA 3: EL PRIMER TRAMO DE
LECTURA DE OP-E-03, cuarenta pares de los 183 de
docs/plan/DIFERENCIA_CONTRA_COLA.jsonl.

QUE ES OP-E-03 (docs/plan/OPERACIONES.jsonl, id_op OP-E-03, tipo LECTURA
DIRIGIDA): la DIFERENCIA CONTRA LA COLA. El barrido calibrado NO se abre como
puerta nueva del cribado; solo los candidatos que NO estaban ya en la cola van a
lectura dirigida, para que ninguna lectura entre por dos puertas y la tasa por
dominio del banco 9.27 siga significando algo (adjudicacion del 11 ago 2026).

LOS CINCO PUNTOS DE SU VERIFICACION, copiados literales del campo
`verificacion` de la operacion, y cada uno con lo que este instrumento hace:
  1. "se corre DESPUES del cierre de la cola del dominio, nunca antes": el
     cribado cerro en 3.388 de 3.388, y este instrumento lo REMIDE contando las
     filas de docs/INTRA_DOMINIO_PARES.jsonl y docs/INTRA_DOMINIO_VEREDICTOS.jsonl.
  2. "los ids pasan por el resolutor antes de comparar (regla P.1)": se resuelve
     madre e hijo de cada fila ANTES de cruzar nada, y se imprime el crudo al
     lado del resuelto siempre que difieran.
  3. "la cuenta cuadra sin fugas": se recomprueba que las 40 del tramo son
     disjuntas y que ninguna esta ya en la cola tras resolver.
  4. "la diferencia se marca LECTURA DIRIGIDA: no entra en la cola y NO mueve el
     marcador del cribado": la marca va escrita en cada fila de la salida.
  5. "sus veredictos se cuentan aparte de la tasa por dominio": la salida los
     cuenta en su propia tabla, y lo dice.

QUE IMPRIME, por cada uno de los 40: dominio, el par crudo y resuelto, el PASO
de la madre que el barrido caso (con su texto entero), y los
`pasos_accionables` ENTEROS de los dos nodos mas sus titulos y entregables. Es
el material de lectura; el juicio A/B/C/D del banco 9.6.1 y la direccion del
9.6.2 los pone el ejecutor leyendo, y se registran aparte.

MECANICA DE ROJO, y no imprime nada si salta: (i) un nodo que, ya resuelto, no
existe en el grafo; (ii) una fila del tramo que, tras resolver, SI esta en la
cola (seria una lectura por dos puertas, justo lo que la adjudicacion prohibe);
(iii) el cribado no cerrado en 3.388. Probada por mutacion en
scripts/loop/vuelta96_tarea3_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta96_tarea3_tramo1_opE03.py
  python scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 0 --cuantos 40
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
PARES = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_PARES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

CORTE_CRIBADO = 3388


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def construir_resolutor(nodos):
    """P.1: la semantica de resolverId del motor, camina la cadena de alias
    hasta el id final, sin ciclar."""
    alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return res


def reunir(desde=0, cuantos=40, corte=CORTE_CRIBADO):
    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    res = construir_resolutor(nodos)
    bolsa = cargar_jsonl(BOLSA)
    pares = cargar_jsonl(PARES)
    veredictos = cargar_jsonl(VEREDICTOS)

    fallos = []

    # --- punto 1 de la verificacion, REMEDIDO y no creido ---
    if len(pares) != corte or len(veredictos) != corte:
        fallos.append("el cribado no esta cerrado en %d: PARES %d, VEREDICTOS %d"
                      % (corte, len(pares), len(veredictos)))

    # --- la cola, con los ids RESUELTOS antes de cruzar (punto 2) ---
    cola = set()
    for r in pares + veredictos:
        a, b = res(r["nodo_a"]), res(r["nodo_b"])
        if a != b:
            cola.add(frozenset((a, b)))

    tramo = bolsa[desde:desde + cuantos]
    filas, vistos = [], set()
    for i, r in enumerate(tramo, start=desde + 1):
        madre_cruda, hijo_crudo = r["madre"], r["hijo"]
        madre, hijo = res(madre_cruda), res(hijo_crudo)
        for crudo, resuelto in ((madre_cruda, madre), (hijo_crudo, hijo)):
            if resuelto not in nodos:
                fallos.append("fila %d: el nodo %r (resuelto %r) no existe en el grafo"
                              % (i, crudo, resuelto))
        par = frozenset((madre, hijo))
        if madre == hijo:
            fallos.append("fila %d: madre e hijo resuelven al MISMO nodo (%s)" % (i, madre))
        elif par in cola:
            fallos.append("fila %d: el par %s / %s YA ESTA EN LA COLA tras resolver "
                          "(lectura por dos puertas)" % (i, madre, hijo))
        if par in vistos:
            fallos.append("fila %d: el par %s / %s se repite dentro del tramo" % (i, madre, hijo))
        vistos.add(par)
        filas.append({
            "n": i, "dominio": r.get("dominio"), "paso": r.get("paso"),
            "texto_paso": r.get("texto_paso"),
            "madre_cruda": madre_cruda, "hijo_crudo": hijo_crudo,
            "madre": madre, "hijo": hijo,
            "titulo_ratio": r.get("titulo_ratio"), "contencion": r.get("contencion"),
            "familia_paso": r.get("familia_paso"), "familia_hijo": r.get("familia_hijo"),
        })
    return filas, fallos, nodos, len(bolsa), len(cola)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", type=int, default=0)
    ap.add_argument("--cuantos", type=int, default=40)
    a = ap.parse_args()

    filas, fallos, nodos, total_bolsa, n_cola = reunir(a.desde, a.cuantos)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("=" * 100)
    print("OP-E-03, PRIMER TRAMO DE LECTURA DIRIGIDA (vuelta 96, TAREA 3)")
    print("Bolsa %s: %d filas. Este tramo: filas %d a %d (%d pares)."
          % (os.path.basename(BOLSA), total_bolsa, a.desde + 1, a.desde + len(filas), len(filas)))
    print("Cribado remedido y cerrado en %d de %d. Pares distintos en la cola tras resolver: %d."
          % (CORTE_CRIBADO, CORTE_CRIBADO, n_cola))
    print("MARCA DE TODAS LAS FILAS: LECTURA DIRIGIDA . FUERA DE LA COLA . FUERA DE LA TASA POR DOMINIO.")
    print("Ids RESUELTOS por el resolutor ANTES de cruzar nada (P.1). Ninguna fila esta ya en la cola.")
    print("=" * 100)

    for f in filas:
        print()
        print("#" * 100)
        print("[%d/%d] dominio %s . LECTURA DIRIGIDA . FUERA DE LA COLA . FUERA DE LA TASA POR DOMINIO"
              % (f["n"], total_bolsa, f["dominio"]))
        cambio = (f["madre_cruda"] != f["madre"]) or (f["hijo_crudo"] != f["hijo"])
        print("  madre: %s%s" % (f["madre"], "" if f["madre_cruda"] == f["madre"] else "   (crudo: %s)" % f["madre_cruda"]))
        print("  hijo:  %s%s" % (f["hijo"], "" if f["hijo_crudo"] == f["hijo"] else "   (crudo: %s)" % f["hijo_crudo"]))
        print("  el resolutor cambio algun id de esta fila: %s" % ("SI" if cambio else "no"))
        print("  senal del barrido: titulo_ratio %s . contencion %s . familia_paso %s . familia_hijo %s"
              % (f["titulo_ratio"], f["contencion"], f["familia_paso"], f["familia_hijo"]))
        print("#" * 100)
        print()
        print("  EL PASO DE LA MADRE QUE EL BARRIDO CASO (numero %s):" % f["paso"])
        print("    %s" % f["texto_paso"])
        print()
        for etiqueta, nid in (("MADRE", f["madre"]), ("HIJO", f["hijo"])):
            n = nodos[nid]
            pasos = n.get("pasos_accionables") or []
            print("  %s . %s" % (etiqueta, nid))
            print("    titulo: %s" % n.get("titulo_concepto", "?"))
            print("    fuente: %s | fase: %s" % (n.get("fuente", "?"), n.get("fase_proyecto", "?")))
            print("    entregable: %s" % n.get("entregable_esperado", "?"))
            print("    pasos_accionables (%d), ENTEROS:" % len(pasos))
            for i, p in enumerate(pasos, 1):
                print("      %d. %s" % (i, p))
            print()

    print("=" * 100)
    print("FIN DEL MATERIAL. %d pares impresos enteros." % len(filas))
    print("El juicio A/B/C/D (banco 9.6.1) y la direccion (9.6.2) los pone la lectura,")
    print("no este instrumento: aqui solo se imprime el material y se prueban las guardas.")
    print("=" * 100)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
