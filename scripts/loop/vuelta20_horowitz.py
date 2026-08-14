# -*- coding: utf-8 -*-
"""VUELTA 20, TAREA 1.4: la nomina de los 14 de Horowitz. SOLO LECTURA.

Salda el cabo que la medicion sola no salda. `docs/plan/01_FUENTES.md` publica
la tanda de los cuatro libros como 43 nodos distintos con grupos 15/13/13/4, y
`docs/plan/10_INVENTARIO.md` publica Horowitz con 14 en segunda o posterior
posicion. Medido en el grafo son 44 nodos distintos y Horowitz son 14. La nomina
de los 13 no esta escrita en ninguna parte, asi que no se puede decir cual
sobra: lo que si se puede es IMPRIMIR LOS 14 Y VERIFICAR LA FORMA EN CADA UNO.

Este instrumento:

  1. Recompone la tanda de los cuatro libros desde `dataset/metadata/master_graph.json`
     con el mismo criterio de la vuelta 19 (nodo VIVO cuyo campo `fuente` trae el
     libro en segunda o posterior posicion), y publica el saldo por libro, la
     suma de declaraciones, los nodos distintos y los solapes nombrados.
  2. Imprime la NOMINA DE LOS 14 DE HOROWITZ con sus pasos enteros y numerados,
     para que la forma de apendice (el bloque del libro 2 pegado al final de los
     pasos, con la frontera visible) se lea nodo por nodo y no se suponga.
  3. Marca, sin decidir por mi, las senales estructurales que acompanan a la
     forma: cuantos libros declara, cuantos pasos tiene, y si el nodo es uno de
     los tres que `01_FUENTES.md` ya aparta por no ser un simple apendice.

No escribe nada. La adjudicacion de la forma es del lector, no del script: el
script pone los pasos delante.
"""
import collections
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

# el canon de la vuelta 19, reproducido tal cual y no importado
CANON = [("Hugos", "Essentials of Supply Chain Man"),
         ("Coleman", "Never Lose a Customer Again"),
         ("Horowitz", "Hard Thing About Hard Thing"),
         ("Weinberg", "Traction"),
         ("Rackham", "SPIN Selling"),
         ("Mollick", "Co-Intelligence")]
CUATRO = ["Coleman", "Horowitz", "Weinberg", "Rackham"]

# los tres que 01_FUENTES.md aparta porque no son un simple apendice
NO_SIMPLES = {"viral_loop_marketing", "coeficiente_viral", "decision_de_vender_startup"}


def titulo(t):
    print()
    print("=" * 98)
    print(t)
    print("=" * 98)


def main():
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]
    vivos = {k: x for k, x in nodos.items() if not x.get("deprecado")}

    titulo("1. LA TANDA DE LOS CUATRO LIBROS, recompuesta desde el grafo")
    print("  nodos en el grafo: %d, VIVOS: %d, deprecado: %d" % (
        len(nodos), len(vivos), len(nodos) - len(vivos)))
    seg = collections.defaultdict(set)
    for k, x in vivos.items():
        partes = [p.strip() for p in (x.get("fuente") or "").split(" | ")]
        for nombre, pat in CANON:
            if any(pat in p for p in partes[1:]):
                seg[nombre].add(k)
    print()
    print("  criterio: nodo VIVO cuyo campo fuente trae el libro en SEGUNDA o")
    print("  posterior posicion (el mismo de la vuelta 19).")
    print()
    print("  %-10s %s" % ("libro", "nodos en 2a o posterior"))
    for b in CUATRO:
        print("  %-10s %d" % (b, len(seg[b])))
    suma = sum(len(seg[b]) for b in CUATRO)
    union = set().union(*[seg[b] for b in CUATRO])
    print("  suma de DECLARACIONES por libro: %d" % suma)
    print("  NODOS DISTINTOS: %d" % len(union))
    solapes = sorted(k for k in union
                     if sum(1 for b in CUATRO if k in seg[b]) > 1)
    print("  nodos que declaran DOS de los cuatro: %d  %s" % (len(solapes), solapes))
    for k in solapes:
        print("     %-40s %s" % (k, [b for b in CUATRO if k in seg[b]]))
    print("  aritmetica: %d declaraciones menos %d solapes = %d nodos distintos" % (
        suma, suma - len(union), len(union)))
    print()
    print("  CONTRA LO PUBLICADO:")
    print("    docs/plan/01_FUENTES.md publica 43 nodos distintos y grupos")
    print("    Coleman 15, Horowitz 13, Weinberg 13, Rackham 4.")
    print("    docs/plan/10_INVENTARIO.md publica Horowitz con 14 en 2a o posterior.")

    titulo("2. LA NOMINA DE LOS %d DE HOROWITZ, con sus pasos enteros" % len(seg["Horowitz"]))
    for i, nid in enumerate(sorted(seg["Horowitz"]), 1):
        x = vivos[nid]
        partes = [p.strip() for p in x["fuente"].split(" | ")]
        pasos = x.get("pasos_accionables") or []
        otros = [b for b in CUATRO if nid in seg[b] and b != "Horowitz"]
        print()
        print("  %2d. %s" % (i, nid))
        print("      dominio: %-18s fase: %s" % (
            x.get("dominio"), x.get("fase_proyecto")))
        print("      titulo:  %s" % x.get("titulo_concepto"))
        print("      fuente:  %s" % x["fuente"])
        print("      libros declarados: %d   pasos: %d   tambien en: %s%s" % (
            len(partes), len(pasos), otros or "solo Horowitz",
            "   [APARTADO por 01_FUENTES.md: no es simple apendice]"
            if nid in NO_SIMPLES else ""))
        for j, p in enumerate(pasos, 1):
            print("        %2d. %s" % (j, p))

    titulo("3. LA FORMA, medida por lo que SI se puede medir: la POSICION del bloque")
    print("  La forma que 01_FUENTES.md publica es: el bloque del libro declarado")
    print("  en segunda posicion va PEGADO AL FINAL de los pasos. Leer la frontera")
    print("  entre bloques es del lector; lo que el instrumento si decide solo es")
    print("  si el libro ocupa o no la ULTIMA posicion declarada del campo fuente,")
    print("  porque un libro que no es el ultimo NO PUEDE tener el bloque final.")
    print()
    union44 = sorted(union)
    no_ultima = []
    for nid in union44:
        x = vivos[nid]
        partes = [p.strip() for p in x["fuente"].split(" | ")]
        for b in CUATRO:
            if nid not in seg[b]:
                continue
            pat = dict(CANON)[b]
            posiciones = [i for i, p in enumerate(partes, 1) if pat in p]
            ultima = len(partes) in posiciones
            if not ultima:
                no_ultima.append((nid, b, posiciones, len(partes), partes[-1]))
    print("  nodos de la tanda de los cuatro: %d" % len(union44))
    print("  declaraciones donde el libro NO ocupa la ultima posicion: %d" % len(no_ultima))
    for nid, b, pos, tot, ult in no_ultima:
        print("     %-28s %-9s posicion %s de %d; el ULTIMO declarado es: %s" % (
            nid, b, pos, tot, ult))
    print()
    print("  EL MISMO CORTE, restringido a los 14 de Horowitz:")
    h_no_ultima = [t for t in no_ultima if t[1] == "Horowitz"]
    print("    con Horowitz en la ultima posicion: %d de %d" % (
        len(seg["Horowitz"]) - len(h_no_ultima), len(seg["Horowitz"])))
    print("    con Horowitz NO en la ultima posicion: %d  %s" % (
        len(h_no_ultima), [t[0] for t in h_no_ultima]))

    titulo("4. LOS NODOS QUE DECLARAN UN MISMO LIBRO DOS VECES CON DOS GRAFIAS")
    print("  01_FUENTES.md nombra UNO (decision_de_vender_startup) como evidencia")
    print("  de OP-S-11. Medido hoy sobre los %d de la tanda:" % len(union44))
    for nid in union44:
        partes = [p.strip() for p in vivos[nid]["fuente"].split(" | ")]
        for nombre, pat in CANON:
            hits = [p for p in partes if pat in p]
            if len(hits) > 1:
                print("     %-30s %-9s x%d  %s" % (nid, nombre, len(hits), hits))

    titulo("5. LOS TRES APARTADOS: los pasos que tienen hoy contra los publicados")
    PUB = {"viral_loop_marketing": 30, "coeficiente_viral": 16,
           "decision_de_vender_startup": 25}
    for nid, pub in sorted(PUB.items()):
        x = vivos.get(nid)
        hoy = len(x.get("pasos_accionables") or []) if x else None
        print("  %-30s 01_FUENTES.md publica %2d pasos; medido hoy %s  %s" % (
            nid, pub, hoy, "CALZA" if hoy == pub else "DIFIERE"))

    titulo("6. LOS OTROS TRES GRUPOS, nombrados para que la union sea auditable")
    for b in ["Coleman", "Weinberg", "Rackham"]:
        print()
        print("  %s (%d):" % (b, len(seg[b])))
        for nid in sorted(seg[b]):
            print("     %s" % nid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
