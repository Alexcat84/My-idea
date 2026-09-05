# -*- coding: utf-8 -*-
r"""vuelta177_tarea2_dossier_actos.py . EL DOSSIER DE LOS ACTOS GRANDES DE
`OP-L-03`, PARA PODER LEERLOS ENTEROS Y NO DE A PARES.

SOLO LECTURA. No escribe nodos, ni veredictos, ni operaciones. Imprime.

POR QUE EXISTE, Y ES LA REGLA `P.5` DEL BANCO DEL PLAN CITADA Y NO
PARAFRASEADA (banco 9.5.0). La clausula de `OP-L-03` dice, verbatim: *"cada acto
que vaya a fundirse SE LEE ENTERO despues de su destejido y antes de su
fusion"*. **LA LECTURA ES DEL ACTO, NO DE LA PAREJA**, y el motivo esta escrito
en el informe intra-dominio, regla de FAMILIA DECLARADA: una familia juzgada de
a pares da incoherencia, **porque la pregunta no es de pares**. Una decision por
acto.

Leer un acto entero exige tener delante, a la vez y en un solo sitio:

  . LOS MIEMBROS con su fuente, su dominio y su texto (resumen, pasos y
    entregable), que es lo que hace que la pregunta se pueda contestar;
  . LOS PARES QUE YA TIENEN VEREDICTO en la cola, con su puesto y su clase, que
    es LO QUE EL PAR DIJO POR SEPARADO;
  . LOS PARES QUE NO ESTAN EN LA COLA, que son los que esta operacion debe leer.

LA CUENTA DE PARES PASA POR EL RESOLUTOR (`P.1`, sin excepcion y da igual quien
haya pedido el conteo). Los ids con los que un acto esta escrito no son siempre
los ids con los que su veredicto se guardo, porque la campana FUNDIO nodos
despues de varios cortes. Sin resolver, un par leido parece sin leer.

DE DONDE SALEN LOS ACTOS: de la LISTA DECLARADA que imprime
`scripts/loop/backlog_l03_vuelta14.py`, que es el instrumento que la propia nota
de la ficha cita. NO SE TECLEA NINGUN ACTO Y NO SE ELIGE NINGUNO A MANO: se pide
un tamano minimo de miembros y salen los que salgan.

USO:
  python scripts/loop/vuelta177_tarea2_dossier_actos.py --minimo 5
  python scripts/loop/vuelta177_tarea2_dossier_actos.py --minimo 5 --sin-texto
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

NL = chr(10)
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PATRON_ACTO = re.compile(r"^\s*\[(\d+),\s*(\d+) pares\]\s*(.+)$")


def actos_del_instrumento():
    """LOS ACTOS DEL BACKLOG, LEIDOS DE LA SALIDA DEL INSTRUMENTO QUE LA FICHA
    CITA. Devuelve lista de (tamano, pares_por_leer, [miembros]).

    Se corre `scripts/loop/backlog_l03_vuelta14.py` y se parsea su LISTA
    DECLARADA. No se re-implementa su metodo: si el instrumento cambia, esto
    cambia con el, que es lo que `EJECUTOR.md` 2 manda."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, os.path.join(AQUI, "backlog_l03_vuelta14.py")],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = r.stdout.decode("utf-8", errors="replace")
    dentro = False
    actos = []
    for linea in salida.split(NL):
        if "LISTA DECLARADA" in linea:
            dentro = True
            continue
        if dentro:
            if linea.strip().startswith("DISCUTIBLE"):
                break
            m = PATRON_ACTO.match(linea)
            if m:
                miembros = [x.strip() for x in m.group(3).split(",") if x.strip()]
                actos.append((int(m.group(1)), int(m.group(2)), miembros))
    return actos, salida


def nodo(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    return json.load(io.open(p, encoding="utf-8"))


def veredictos_por_par(mapa):
    """LOS VEREDICTOS INDEXADOS POR PAR RESUELTO (`P.1`). Devuelve un dict
    {frozenset({a_res, b_res}): fila}."""
    idx = {}
    for fila in T.veredictos():
        a = T.resolver(mapa, fila["nodo_a"])
        b = T.resolver(mapa, fila["nodo_b"])
        idx.setdefault(frozenset((a, b)), []).append(fila)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minimo", type=int, default=5,
                    help="tamano minimo de acto que se saca al dossier")
    ap.add_argument("--sin-texto", dest="sin_texto", action="store_true",
                    help="solo la ficha de pares, sin el cuerpo de los nodos")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("DOSSIER DE LOS ACTOS GRANDES DE OP-L-03 (vuelta 177, TAREA 2)")
    print("=" * 78)
    print("")

    actos, _salida = actos_del_instrumento()
    grandes = [x for x in actos if x[0] >= a.minimo]
    print("A) EL UNIVERSO, LEIDO DEL INSTRUMENTO Y NO TECLEADO")
    print("   instrumento: scripts/loop/backlog_l03_vuelta14.py")
    print("   CIFRA actos del backlog al corte 3.388: %d" % len(actos))
    print("   CIFRA pares por leer en total: %d" % sum(x[1] for x in actos))
    print("   CIFRA actos de %d miembros o mas: %d" % (a.minimo, len(grandes)))
    print("   CIFRA pares por leer en esos actos: %d" % sum(x[1] for x in grandes))
    print("   reparto de los grandes, por tamano:")
    for t in sorted({x[0] for x in grandes}, reverse=True):
        de_ese = [x for x in grandes if x[0] == t]
        print("      tamano %d: %d actos, %d pares por leer"
              % (t, len(de_ese), sum(x[1] for x in de_ese)))
    print("")

    mapa, _n = T.mapa_de_alias()
    idx = veredictos_por_par(mapa)
    print("B) EL RESOLUTOR, PUESTO ANTES DE CONTAR NINGUN PAR (P.1)")
    print("   CIFRA alias del mapa: %d" % len(mapa))
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(T.veredictos()))
    print("   CIFRA pares distintos tras resolver: %d" % len(idx))
    print("")

    for n, (tam, por_leer, miembros) in enumerate(grandes, 1):
        print("#" * 78)
        print("# ACTO %d DE %d: %d MIEMBROS, %d PARES POR LEER" % (n, len(grandes), tam, por_leer))
        print("#" * 78)
        print("")
        print("   MIEMBROS, CON SU FUENTE Y SU DOMINIO")
        for m in miembros:
            d = nodo(m)
            if d is None:
                print("      %-56s NO EXISTE COMO FICHERO" % m)
                continue
            print("      %s" % m)
            print("         titulo:  %s" % d.get("titulo_concepto", ""))
            print("         dominio: %s | fase: %s | fuente: %s"
                  % (d.get("dominio", ""), d.get("fase_proyecto", ""),
                     str(d.get("fuente", ""))[:90]))
        print("")

        print("   LOS PARES DEL ACTO, RESUELTOS Y CONTADOS (P.1)")
        # TRES CAJONES Y NO DOS, Y EL TERCERO ES EL HALLAZGO DE ESTA VUELTA.
        # La primera version de este dossier tenia dos (con veredicto y sin el) y
        # metia en el primero los pares cuyos DOS extremos resuelven AL MISMO
        # NODO, porque `frozenset((x, x))` es un conjunto de un elemento y casaba
        # con una clave degenerada del indice. Eso publicaba "15 pares con
        # veredicto" de un acto que YA NO TIENE PARES: sus seis miembros son hoy
        # el mismo nodo. Un par cuyos dos extremos son el mismo nodo NO ES UN PAR
        # LEIDO NI UN PAR POR LEER: ES UN PAR QUE YA NO EXISTE, y se cuenta aparte.
        en_cola, fuera, fundidos = [], [], []
        for x, y in combinations(sorted(miembros), 2):
            rx, ry = T.resolver(mapa, x), T.resolver(mapa, y)
            if rx == ry:
                fundidos.append((x, y, rx))
                continue
            filas = idx.get(frozenset((rx, ry)), [])
            if filas:
                en_cola.append((x, y, filas))
            else:
                fuera.append((x, y))
        vivos = sorted({T.resolver(mapa, m) for m in miembros})
        print("      CIFRA miembros: %d | CIFRA NODOS VIVOS DISTINTOS TRAS RESOLVER: %d"
              % (tam, len(vivos)))
        if len(vivos) < tam:
            print("      EL ACTO SE ENCOGIO DEBAJO: %d miembros son hoy %d nodo(s)."
                  % (tam, len(vivos)))
            for v in vivos:
                cuales = [m for m in miembros if T.resolver(mapa, m) == v]
                print("         %s  <-  %s" % (v, ", ".join(cuales)))
        print("      CIFRA pares posibles sobre los miembros escritos: %d"
              % (tam * (tam - 1) // 2))
        print("      CIFRA pares QUE YA NO EXISTEN (los dos extremos son el mismo "
              "nodo hoy): %d" % len(fundidos))
        print("      CIFRA pares CON veredicto en la cola: %d" % len(en_cola))
        print("      CIFRA pares FUERA de la cola (los que esta operacion lee): %d"
              % len(fuera))
        print("      el instrumento dice que hay %d por leer, y yo cuento %d: %s"
              % (por_leer, len(fuera), "CALZA" if por_leer == len(fuera) else "NO CALZA"))
        if por_leer != len(fuera):
            print("      LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO "
                  "(EJECUTOR.md 2). El instrumento lee el archivo de componentes")
            print("      del corte 3.388; este dossier resuelve los ids HOY (P.1). "
                  "Si el acto se fundio despues del corte, el archivo lo sigue")
            print("      viendo abierto y el resolutor ya no.")
        print("")
        print("      LOS QUE YA TIENEN VEREDICTO, QUE ES LO QUE EL PAR DIJO POR SEPARADO")
        for x, y, filas in en_cola:
            for f in filas:
                print("         puesto %-5s clase %-2s  %s + %s"
                      % (f["puesto_intra"], f["clase"], x, y))
                print("            razon: %s" % str(f.get("razon", ""))[:150])
        if not en_cola:
            print("         (ninguno)")
        print("")
        print("      LOS PARES QUE YA NO EXISTEN, UNO A UNO")
        for x, y, r in fundidos:
            print("         %s + %s  ->  los dos son %s" % (x, y, r))
        if not fundidos:
            print("         (ninguno)")
        print("")
        print("      LOS QUE NO ESTAN EN LA COLA")
        for x, y in fuera:
            print("         %s + %s" % (x, y))
        if not fuera:
            print("         (ninguno)")
        print("")

        if not a.sin_texto:
            print("   EL TEXTO DEL ACTO, ENTERO, QUE ES LO QUE P.5 MANDA LEER")
            for m in miembros:
                d = nodo(m)
                if d is None:
                    continue
                print("      " + "-" * 68)
                print("      %s . %s" % (m, d.get("titulo_concepto", "")))
                print("      RESUMEN: %s" % str(d.get("resumen_teorico", "")))
                pasos = d.get("pasos_accionables", [])
                print("      PASOS (%d):" % len(pasos))
                for i, pa in enumerate(pasos, 1):
                    print("         %d. %s" % (i, pa))
                print("      ENTREGABLE: %s" % str(d.get("entregable_esperado", "")))
            print("")

    print("FIN DEL DOSSIER")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
