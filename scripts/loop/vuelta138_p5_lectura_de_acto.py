# -*- coding: utf-8 -*-
"""vuelta138_p5_lectura_de_acto.py . LA LECTURA DE ACTO POR P.5, MEDIDA PAR A
PAR, PARA UNA FUSION DE MESA.

P.5, con su letra: "CADA ACTO SE LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE
SU FUSION", con su motivo escrito ("una vez fundido, el acto es un nodo y la
pregunta de si eran una familia o dos se vuelve irrespondible"). Y con su alcance
acotado por la correccion declarada del 15 ago 2026: EL ACTO EN OPERACION Y NADA
MAS, o sea que esto NO abre re-cribado; un par de fuera del acto no se lee, se
anota.

QUE HACE. Toma los N nodos de la ficha (superviviente mas absorbidos), enumera
los N*(N-1)/2 pares internos, y para cada uno BUSCA su veredicto en los
registros de la casa, sin inventar ninguno:
  - docs/INTRA_DOMINIO_VEREDICTOS.jsonl, el registro del cribado, por el par de
    ids en cualquiera de los dos ordenes (P.1: se compara por id resuelto, y
    aqui los ids son los de la ficha, que el generador ya coteja contra el
    catalogo);
  - docs/plan/LD_*.md y docs/plan/LECTURAS_DIRIGIDAS.md, las lecturas dirigidas,
    por la aparicion de los DOS ids en la misma cabecera de veredicto.

LO QUE NO HACE, y se dice: NO decide una clase, NO redacta un veredicto y NO
inventa un par. Lo que no encuentra lo declara SIN LEER, con todas sus letras,
para que el que funde sepa que le falta antes de fundir y no despues.

USO:
  python scripts/loop/vuelta138_p5_lectura_de_acto.py --id-op OP-M-01-FUSION
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PLAN = os.path.join(RAIZ, "docs", "plan")


def ficha(id_op):
    for l in io.open(OPERACIONES, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("id_op") == id_op:
            return d
    return None


def veredictos_del_cribado():
    """(a, b) ordenado -> (puesto, clase, razon). El registro es la fuente; aqui
    no se computa ninguna clase."""
    por_par = {}
    for l in io.open(VEREDICTOS, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        k = tuple(sorted((d.get("nodo_a"), d.get("nodo_b"))))
        por_par[k] = (d.get("puesto_intra"), d.get("clase"), d.get("razon") or "")
    return por_par


def cabeceras_de_lecturas_dirigidas():
    """Devuelve [(fichero, linea_de_cabecera)] de todo docs/plan/LD_*.md y de
    LECTURAS_DIRIGIDAS.md. Una cabecera de veredicto es una linea de titulo que
    nombra dos nodos con 'contra'."""
    filas = []
    nombres = sorted(n for n in os.listdir(PLAN)
                     if n.startswith("LD_") and n.endswith(".md"))
    if os.path.exists(os.path.join(PLAN, "LECTURAS_DIRIGIDAS.md")):
        nombres.append("LECTURAS_DIRIGIDAS.md")
    for n in nombres:
        for linea in io.open(os.path.join(PLAN, n), encoding="utf-8"):
            if " contra " in linea and linea.lstrip().startswith("#"):
                filas.append((n, linea.strip()))
    return filas


def busca_en_dirigidas(filas, a, b):
    hallados = []
    for fichero, linea in filas:
        # los ids van entre acentos graves en las cabeceras de la casa
        if ("`%s`" % a) in linea and ("`%s`" % b) in linea:
            m = re.search(r"\*\*([A-D])\.", linea)
            clase = m.group(1) if m else "?"
            hallados.append((fichero, clase, linea))
    return hallados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id-op", dest="id_op", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    op = ficha(a.id_op)
    if op is None:
        print("ROJO: %s no esta en docs/plan/OPERACIONES.jsonl." % a.id_op)
        return 1

    miembros = list(op.get("nodos") or [])
    sup = op.get("superviviente")
    print("=" * 78)
    print("P.5, LA LECTURA DEL ACTO %s, PAR A PAR" % a.id_op)
    print("  miembros (%d): %s" % (len(miembros), ", ".join(miembros)))
    print("  superviviente: %s" % sup)
    print("=" * 78)

    pares = []
    for i in range(len(miembros)):
        for j in range(i + 1, len(miembros)):
            pares.append((miembros[i], miembros[j]))
    print("  pares internos posibles: %d" % len(pares))
    print("")

    cribado = veredictos_del_cribado()
    dirigidas = cabeceras_de_lecturas_dirigidas()

    leidos, sin_leer = [], []
    for x, y in pares:
        k = tuple(sorted((x, y)))
        fuente, clase, detalle = None, None, ""
        if k in cribado:
            puesto, clase, razon = cribado[k]
            fuente = "cribado, puesto %s" % puesto
            detalle = razon[:110]
        else:
            hall = busca_en_dirigidas(dirigidas, x, y)
            if hall:
                fichero, clase, linea = hall[0]
                fuente = "lectura dirigida, %s" % fichero
                detalle = linea[:110]
        if fuente:
            leidos.append((x, y, clase, fuente, detalle))
        else:
            sin_leer.append((x, y))

    for x, y, clase, fuente, detalle in leidos:
        print("  LEIDO   %-3s  %s  contra  %s" % (clase, x, y))
        print("          %s" % fuente)
        if detalle:
            print("          %s" % detalle)
    for x, y in sin_leer:
        print("  SIN LEER     %s  contra  %s" % (x, y))
        print("          no aparece ni en el registro del cribado ni en ninguna "
              "cabecera de lectura dirigida")

    print("")
    clases = {}
    for _, _, c, _, _ in leidos:
        clases[c] = clases.get(c, 0) + 1
    print("CIFRA pares internos del acto: %d pares" % len(pares))
    print("CIFRA pares leidos: %d pares" % len(leidos))
    print("CIFRA pares sin leer: %d pares" % len(sin_leer))
    print("  reparto por clase de los leidos: %s"
          % (", ".join("%s %d" % (k, v) for k, v in sorted(clases.items())) or "ninguno"))
    print("")
    if sin_leer:
        print("P.5 NO SATISFECHA POR EL REGISTRO: %d par(es) del acto sin lectura. "
              "La lectura de esos pares es trabajo propio ANTES de fundir." % len(sin_leer))
        print("FIN")
        return 1
    print("P.5 SATISFECHA POR EL REGISTRO: los %d pares del acto tienen lectura." % len(pares))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
