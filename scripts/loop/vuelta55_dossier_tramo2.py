# -*- coding: utf-8 -*-
"""vuelta55_dossier_tramo2.py . EL ACTO LEIDO ENTERO (P.5) PARA LOS ACTOS VIVOS
DEL TRAMO 2, con la RAZON entera de cada par interno pegada al lado.

DE SOLO LECTURA. No escribe nada.

POR QUE EXISTE: P.5 pide el acto leido ENTERO antes de decidir, y la receta de
P.8 pesa el contenido tal como las RAZONES lo declaran (acta 54, pregunta 4).
Este instrumento pone las dos cosas en la misma pagina para que la decision no
dependa de recordar: los pasos y las condiciones de los dos lados con su texto
entero, el cableado crudo, la marca de puerta, y la razon de archivo del par A
sin recortar.

Uso:
  python scripts/loop/vuelta55_dossier_tramo2.py --tramo docs/loop/TRAMO2_V55.jsonl
        [--actos 28,29,30] [--commit <sha>]

  --commit lee los nodos de un commit de git en vez del arbol de trabajo, que
  es lo que hace falta para leer un acto YA FUNDIDO en su estado pre fusion.
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
    puertas = cargar_puertas()

    ver = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        ver[frozenset((v["nodo_a"], v["nodo_b"]))] = v

    print("=" * 78)
    print("DOSSIER DEL TRAMO 2: EL ACTO LEIDO ENTERO (P.5) CON SU RAZON")
    print("=" * 78)
    print("  nodos leidos de: %s" % (("commit " + a.commit) if a.commit else "el arbol de trabajo"))
    print("  universo PROTEGIDO (semillas mas extremos de puente): %d ids" % len(puertas))
    print()

    for r in tramo:
        n = r["orden_tramo2"]
        if quiero and n not in quiero:
            continue
        ms = sorted(r["miembros"])
        print("#" * 78)
        print("# ACTO %d del tramo 2 (puesto %s de hoy, %s en la de la 48)"
              % (n, r.get("puesto_hoy"), r.get("puesto_v48")))
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
