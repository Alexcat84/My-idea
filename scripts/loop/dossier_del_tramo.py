# -*- coding: utf-8 -*-
"""dossier_del_tramo.py . EL ACTO LEIDO ENTERO (P.5) PARA LOS ACTOS DE UN TRAMO,
con la RAZON entera de cada par interno pegada al lado.

NOMBRE ESTABLE Y SIN NUMERO DE TRAMO, por la misma via que vuelta58_varas_tramo.py
y que el abridor de nombre estable: el tramo entra por --tramo y el titulo se arma
SOLO, leyendo el numero de la clave del ordinal del propio fichero. Este fichero no
se clona cada tramo.

SUCESOR DECLARADO de scripts/loop/vuelta56_dossier_tramo3.py, al que NO reemplaza
y CUYA ARITMETICA SE COPIA ENTERA: el fichero se copio BYTE A BYTE (sha1 del
ancestro d51aa4e05157) y solo despues se le cambio el titulo. El ancestro queda intacto
y re-corrible, que es la via del acta 54 pregunta 3: sus cifras ya estan citadas
por el registro del tramo 3.

POR QUE NACE: el ancestro lleva TRAMO 3 tallado en su cabecera y recibe el sujeto
por --tramo, que es exactamente la especie ROJO del barrido de titulos (sale en la
lista de los 32 con esa marca). Corriendolo sobre el tramo 6 su titulo mentiria, y
una salida publicada con el titulo mintiendo es lo que la racha de la cabecera del
reporte ya pago tres veces. ESTA VUELTA NO PAGA EL ROJO DEL ANCESTRO: lo deja como
esta y escribe sucesor, que es lo que el encargo permite.

DEL ANCESTRO SE CONSERVA su propia unica novedad: LA CLAVE DEL ORDINAL SE
DESCUBRE DEL FICHERO en vez de estar escrita a mano; si hay ninguna o mas de una,
es ROJO y PARA, porque un ordinal ambiguo no es un ordinal.

DE SOLO LECTURA. No escribe nada.

POR QUE EXISTE: P.5 pide el acto leido ENTERO antes de decidir, y la receta de
P.8 pesa el contenido tal como las RAZONES lo declaran (acta 54, pregunta 4).
Este instrumento pone las dos cosas en la misma pagina para que la decision no
dependa de recordar: los pasos y las condiciones de los dos lados con su texto
entero, el cableado crudo, la marca de puerta, y la razon de archivo del par A
sin recortar.

Uso:
  python scripts/loop/dossier_del_tramo.py --tramo docs/loop/TRAMO6_V61.jsonl
        [--actos 1,2,3] [--commit <sha>]
"""

import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def leer_nodo(nid, commit=None):
    if commit:
        p = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)],
                           capture_output=True, cwd=RAIZ)
        if p.returncode != 0:
            return None
        return json.loads(p.stdout.decode("utf-8"))
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def cargar_puertas():
    """MISMA fuente que scripts/loop/vuelta48_puertas_en_el_lote.py."""
    out = set()
    p = os.path.join(RAIZ, "dataset", "metadata", "entry_seeds.json")
    if os.path.exists(p):
        out.update(json.load(io.open(p, encoding="utf-8")).get("seeds", []))
    packs = os.path.join(RAIZ, "packs")
    if os.path.isdir(packs):
        for d in sorted(os.listdir(packs)):
            q = os.path.join(packs, d, "metadata", "entry_seeds.json")
            if os.path.exists(q):
                out.update(json.load(io.open(q, encoding="utf-8")))
            q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
            if os.path.exists(q):
                for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
                    for extremo in ("core", "dominio"):
                        if x.get(extremo):
                            out.add(x[extremo])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    ap.add_argument("--actos", default=None)
    ap.add_argument("--commit", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    quiero = None
    if a.actos:
        quiero = set(int(x) for x in a.actos.split(","))

    tramo = [json.loads(l) for l in io.open(a.tramo, encoding="utf-8") if l.strip()]

    # LO UNICO QUE NO ES COPIA: la clave del ordinal se descubre del fichero.
    claves = sorted({k for k in tramo[0] if k.startswith("orden_tramo")}) if tramo else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    NTRAMO = ORD.replace("orden_tramo", "")

    puertas = cargar_puertas()

    ver = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        ver[frozenset((v["nodo_a"], v["nodo_b"]))] = v

    print("=" * 78)
    print("DOSSIER DEL TRAMO %s: EL ACTO LEIDO ENTERO (P.5) CON SU RAZON" % NTRAMO)
    print("=" * 78)
    print("  nodos leidos de: %s" % (("commit " + a.commit) if a.commit else "el arbol de trabajo"))
    print("  universo PROTEGIDO (semillas mas extremos de puente): %d ids" % len(puertas))
    print()

    for r in tramo:
        n = r[ORD]
        if quiero and n not in quiero:
            continue
        ms = sorted(r["miembros"])
        print("#" * 78)
        print("# ACTO %d del tramo %s (puesto %s de hoy, %s en la de la 48)"
              % (n, NTRAMO, r.get("puesto_hoy"), r.get("puesto_v48") or "nuevo"))
        print("#" * 78)
        v = ver.get(frozenset(ms))
        if v:
            print("  [PAR A] puesto %s, clase %s, dominio %s"
                  % (v.get("puesto_intra"), v.get("clase"), v.get("dominio")))
            print("  nodo_a (EL PRIMERO de la razon): %s" % v.get("nodo_a"))
            print("  nodo_b (EL SEGUNDO de la razon): %s" % v.get("nodo_b"))
            print()
            print("  RAZON ENTERA, sin recortar:")
            print("    %s" % v.get("razon"))
        else:
            print("  [PAR A] NO ENCONTRADO en los veredictos")
        print()
        for m in ms:
            d = leer_nodo(m, a.commit)
            if d is None:
                print("  --- %s: NO SE PUDO LEER" % m)
                continue
            pa = d.get("pasos_accionables") or []
            co = d.get("condiciones_activacion") or []
            pv = d.get("nodos_previos") or []
            sg = d.get("nodos_siguientes") or []
            print("  --- %s%s" % (m, "   [PUERTA: TIENE QUE SOBREVIVIR]" if m in puertas else ""))
            print("      titulo    : %s" % d.get("titulo_concepto"))
            print("      fuente    : %s" % d.get("fuente"))
            print("      pasos %d | condiciones %d | previos %d | siguientes %d | cableado %d"
                  % (len(pa), len(co), len(pv), len(sg), len(pv) + len(sg)))
            for i, x in enumerate(pa, 1):
                print("      paso %d: %s" % (i, x))
            for i, x in enumerate(co, 1):
                print("      cond %d: %s" % (i, x))
            print("      previos   : %s" % pv)
            print("      siguientes: %s" % sg)
            print("      entregable: %s" % d.get("entregable_esperado"))
            print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
