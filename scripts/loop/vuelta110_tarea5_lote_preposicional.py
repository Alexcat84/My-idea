# -*- coding: utf-8 -*-
r"""vuelta110_tarea5_lote_preposicional.py . TAREA 5 de la vuelta 110: EL
LOTE de todas las RESUELTA vivas cuyo paso_casado (la MADRE del par, el
paso que de verdad se cito, resuelto por id, no el texto de la razon)
lleva complemento preposicional (con, por, a, de, en, hacia, contra),
contado con codigo, ANTES de leer ninguno (encargo de la vuelta 110,
TAREA 5.1: "quiero tu numero limpio").

QUE HACE. (1) `contar_cierre_efectivo.cifras()` sobre los cuatro tramos de
OP-E-03 da las RESUELTA vivas (74, universo n=183 menos sin_dir). (2) Para
cada una, lee su fila del tramo (madre_de_la_bolsa, paso_casado -- un
INDICE 1-based sobre los pasos_accionables de la madre, NO texto: se
comprobo con `docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl` puesto 154,
paso_casado=4). (3) Resuelve `madre_de_la_bolsa` por el MISMO resolutor
que scripts/reanclar_por_resolutor.py (P.1 del banco del plan: todo
conteo que toque ids pasa por el resolutor antes de contar), leyendo
dataset/metadata/master_graph.json (ya curado, Gate 0 en verde). (4) Toma
el texto literal `pasos_accionables[paso_casado - 1]` de la madre YA
RESUELTA. (5) Busca las siete preposiciones como PALABRA SUELTA
(\b...\b, sin distinguir mayusculas) en ESE texto.

SIN TEXTO QUE CONTAR, NO HAY CIFRA: si una madre no resuelve, o el indice
de paso_casado esta fuera de rango, el instrumento cae en ROJO nombrando
el puesto, en vez de contar con lo que si encontro.

USO:
  python scripts/loop/vuelta110_tarea5_lote_preposicional.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce  # noqa: E402

MASTER = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

PREPOSICIONES = ["con", "por", "a", "de", "en", "hacia", "contra"]
RE_PREP = re.compile(r"\b(%s)\b" % "|".join(PREPOSICIONES), re.IGNORECASE)


def cargar_grafo():
    with io.open(MASTER, encoding="utf-8") as f:
        g = json.load(f)
    return g["nodos"]


def resolutor(nodos):
    """Espejo del resolutor de scripts/reanclar_por_resolutor.py: camina
    ids_alias hasta un nodo vivo, o el eslabon mas reciente si toda la
    cadena esta deprecada."""
    alias = {}
    for nid, v in nodos.items():
        for a in (v.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def resolver(n):
        v = nodos.get(n)
        if v and not v.get("deprecado"):
            return n
        visto, cur = {n}, n
        ultimo = n if v else None
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = nodos.get(cur)
            if not c:
                continue
            ultimo = cur
            if not c.get("deprecado"):
                return cur
        return ultimo

    return resolver


def filas_de_tramos():
    filas = {}
    for ruta in cce.TRAMOS_OP_E_03_POR_DEFECTO:
        for f in cce.cargar(ruta):
            filas[f["puesto_tramo"]] = f
    return filas


def main():
    d, fallos = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    resuelta_vivas = sorted(set(range(1, d["n"] + 1)) - set(d["sin_dir"]))
    filas = filas_de_tramos()
    nodos = cargar_grafo()
    resolver = resolutor(nodos)

    fallos2 = []
    con_prep = []
    sin_prep = []
    detalle = []
    for p in resuelta_vivas:
        f = filas.get(p)
        if f is None:
            fallos2.append("puesto %d: no esta en ningun tramo (no deberia ocurrir)" % p)
            continue
        madre_id_original = f["madre_de_la_bolsa"]
        madre_id = resolver(madre_id_original)
        madre = nodos.get(madre_id)
        if madre is None:
            fallos2.append("puesto %d: madre %r (resuelta a %r) no existe en master_graph.json"
                           % (p, madre_id_original, madre_id))
            continue
        pasos = madre.get("pasos_accionables") or []
        idx = f["paso_casado"]
        if not isinstance(idx, int) or idx < 1 or idx > len(pasos):
            fallos2.append("puesto %d: paso_casado %r fuera de rango (madre %s tiene %d pasos)"
                           % (p, idx, madre_id, len(pasos)))
            continue
        texto = pasos[idx - 1]
        tiene_prep = bool(RE_PREP.search(texto))
        (con_prep if tiene_prep else sin_prep).append(p)
        detalle.append((p, madre_id_original, madre_id, idx, texto, tiene_prep))

    if fallos2:
        print("ROJO, %d cosa(s) no cuadran, NO SE CUENTA NADA:" % len(fallos2))
        for x in fallos2:
            print("   %s" % x)
        return 1

    print("RESUELTA vivas (contar_cierre_efectivo.cifras): %d" % len(resuelta_vivas))
    print("CON preposicion (con/por/a/de/en/hacia/contra) en el paso_casado literal: %d"
          % len(con_prep))
    print("SIN preposicion: %d" % len(sin_prep))
    print()
    print("LISTA CON PREPOSICION (%d):" % len(con_prep))
    for p, mid_orig, mid, idx, texto, _ in detalle:
        if p in con_prep:
            resuelto = "" if mid_orig == mid else " [resuelto %s -> %s]" % (mid_orig, mid)
            print("   %d | %s%s p%d: %s" % (p, mid_orig, resuelto, idx, texto))
    print()
    print("LISTA SIN PREPOSICION (%d): %s" % (len(sin_prep), ", ".join(str(p) for p in sin_prep)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
