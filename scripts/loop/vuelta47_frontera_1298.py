"""Vuelta 47, TAREA 1.2: LA FRONTERA DEL 1298, MEDIDA HOY EN SUS DOS LADOS.

La frontera se re-declara, asi que sus dos lados se MIDEN contra el grafo de hoy en
vez de copiarse de la pagina del 12 ago 2026. Este instrumento no opina: lee los
cuatro nodos que la frontera nombra (el sujeto, la puerta, el nodo propio y el nodo de
Blank), imprime sus pasos y su fuente, y localiza las dos frases que la frontera
manda conservar, una por lado.

De solo lectura. No escribe ni un byte del dataset.

Uso: python scripts/loop/vuelta47_frontera_1298.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

SUJETO = "decision_pivote_perseverar"
PUERTA = "pivotar_o_perseverar"
PROPIO = "puntos_brillantes_antes_del_pivote"
BLANK = "pivote_startup"
ACTO = "pivote_estrategico"

# Los cinco pasos del bloque del punto brillante, copiados del registro de la vuelta
# 46 (docs/plan/02_DESTEJIDOS.md, tabla "EL BLOQUE DEL PUNTO BRILLANTE, PASO POR PASO
# Y VERBATIM"). Se buscan por prefijo para no depender de la tilde final.
HUELLAS_BRILLANTE = [
    u"Busca evidencia de clientes genuinamente comprometidos",
    u"caracter",
    u"adoptadores tempranos de un mercado grande",
    u"timing de mercado es el problema",
    u"Solo pivota si no encuentras",
]
HUELLA_RAPIDO = u"rapidez y sin miedo al fracaso"


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def leer(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    return json.load(io.open(p, encoding="utf-8"))


def main():
    sep("1. LOS CINCO NODOS DE LA FRONTERA DEL 1298, LEIDOS DEL GRAFO DE HOY")
    nodos = {}
    for nid in (SUJETO, PUERTA, PROPIO, BLANK, ACTO):
        d = leer(nid)
        nodos[nid] = d
        if d is None:
            print("  %-40s FICHERO AUSENTE" % nid)
            continue
        print("  %-40s pasos %2d   deprecado %-5s   fuente: %s"
              % (nid, len(d.get("pasos_accionables", [])),
                 d.get("deprecado", False), d.get("fuente")))

    sep("2. EL LADO DEL PUNTO BRILLANTE: DONDE VIVEN SUS CINCO PASOS")
    print("  se buscan las CINCO huellas del bloque en cada uno de los tres nodos")
    print("  candidatos, sin decidir de antemano cual las tiene\n")
    print("  %-40s %s" % ("nodo", "huellas del bloque halladas"))
    for nid in (PROPIO, PUERTA, SUJETO):
        d = nodos[nid]
        if d is None:
            continue
        texto = " || ".join(d.get("pasos_accionables", []))
        n = sum(1 for h in HUELLAS_BRILLANTE if h in texto)
        print("  %-40s %d de %d" % (nid, n, len(HUELLAS_BRILLANTE)))
    d = nodos[PROPIO]
    if d is not None:
        print("\n  los pasos del nodo propio, en su orden de hoy:")
        for i, s in enumerate(d.get("pasos_accionables", []), 1):
            print("    %d. %s" % (i, s))

    sep("3. EL LADO DE DECIDIR RAPIDO: DONDE VIVE SU FRASE")
    print("  %-40s %s" % ("nodo", "trae la frase"))
    for nid in (BLANK, ACTO, PUERTA, SUJETO, PROPIO):
        d = nodos[nid]
        if d is None:
            continue
        pasos = d.get("pasos_accionables", [])
        donde = [i for i, s in enumerate(pasos, 1) if HUELLA_RAPIDO in s]
        print("  %-40s %s" % (nid, ("SI, paso %s" % donde[0]) if donde else "no"))
    d = nodos[BLANK]
    if d is not None:
        for i, s in enumerate(d.get("pasos_accionables", []), 1):
            if HUELLA_RAPIDO in s:
                print("\n    literal del paso %d: %s" % (i, s))

    sep("4. LA ARISTA QUE SOSTIENE LA FRONTERA, MEDIDA EN LOS DOS SENTIDOS")
    a = nodos[SUJETO]
    b = nodos[PROPIO]
    if a is not None and b is not None:
        print("  %s nombra a %s en nodos_siguientes: %s"
              % (SUJETO, PROPIO, PROPIO in (a.get("nodos_siguientes") or [])))
        print("  %s nombra a %s en nodos_previos   : %s"
              % (PROPIO, SUJETO, SUJETO in (b.get("nodos_previos") or [])))
        print("  %s nombra a %s en algun campo     : %s"
              % (PUERTA, PROPIO,
                 PROPIO in ((nodos[PUERTA].get("nodos_previos") or []) +
                            (nodos[PUERTA].get("nodos_siguientes") or []))))
        print()
        print("  LECTURA: el nodo propio cuelga HOY del sujeto. Cuando OP-M-03-I mate")
        print("  al sujeto, esa entrada se redirige al superviviente (la puerta), que")
        print("  es lo que la re-declaracion de la frontera escribe.")

    sep("5. EL PAR 1298 EN EL ARCHIVO, LEIDO HOY")
    for linea in io.open(VER, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        v = json.loads(linea)
        if v.get("puesto_intra") == 1298:
            print("  puesto %s   clase %s" % (v.get("puesto_intra"), v.get("clase")))
            print("  nodos : %s  contra  %s" % (v.get("nodo_a"), v.get("nodo_b")))
            r = v.get("razon") or ""
            print("  razon (primeras 320): %s" % r[:320])
            break
    return 0


if __name__ == "__main__":
    sys.exit(main())
