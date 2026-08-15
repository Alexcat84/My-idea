# -*- coding: utf-8 -*-
"""vuelta35_rancios.py - LA SEGUNDA VARA SOBRE LOS RANCIOS: el TEXTO, no la fecha.

SOLO LECTURA.

POR QUE HACE FALTA UNA SEGUNDA VARA. vuelta35_pares_opd03.py declara RANCIO un
par cuya lectura es anterior al ultimo cambio del fichero de alguno de sus dos
nodos. Esa vara es de FECHA, y un fichero de nodo cambia por cosas que no son su
texto: una redireccion de enlace, un reciprocado del Gate, un campo de fuente.
Contar como rancio un par cuyo texto no se movio seria inflar el hallazgo.

Asi que aqui se compara LO UNICO QUE P.5 protege: los pasos accionables del nodo
en el commit en que el par se leyo, contra los de hoy. Si son identicos, el par
NO es rancio por mucho que el fichero se haya tocado. Si no lo son, se imprime
cuantos pasos habia y cuantos hay.

Uso: python scripts/loop/vuelta35_rancios.py
"""
import io
import itertools
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

SEIS = [
    "ab_testing_optimizacion",
    "optimizacion_embudo_get_customers",
    "split_testing_experimentos_ab",
    "funnel_get_customers_optimizacion",
    "split_testing",
    "test_ab_precio",
]


def git_bytes(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True).stdout


def git(*args):
    return git_bytes(*args).decode("utf-8", "replace").strip()


def pasos_en(commit, nid):
    """Los pasos accionables del nodo TAL COMO ESTABAN en ese commit."""
    crudo = git_bytes("show", "%s:dataset/nodos/%s.json" % (commit, nid))
    if not crudo.strip():
        return None
    try:
        d = json.loads(crudo.decode("utf-8", "replace"))
    except ValueError:
        return None
    return d.get("pasos_accionables") or []


def pasos_hoy(nid):
    d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
    return d.get("pasos_accionables") or []


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v

    print("--- LOS PARES REGISTRADOS DEL ACTO, con la vara de TEXTO ---\n")
    rancios, al_dia = [], []
    for a, b in itertools.combinations(SEIS, 2):
        v = por_par.get((a, b))
        if v is None:
            continue
        fragmento = (v["razon"] or "")[:120]
        commit = git("log", "-1", "--pretty=format:%H", "-S", fragmento,
                     "--", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
        fecha = git("log", "-1", "--date=short", "--pretty=format:%ad", commit)
        print("puesto %-5d clase %-3s  %s contra %s" % (v["puesto_intra"], v["clase"], a, b))
        print("   leido en %s (%s)" % (commit[:8], fecha))
        movidos = []
        for nid in (v["nodo_a"], v["nodo_b"]):
            antes = pasos_en(commit, nid)
            ahora = pasos_hoy(nid)
            if antes is None:
                print("   %-38s NO SE PUDO LEER EN ESE COMMIT" % nid)
                continue
            igual = (antes == ahora)
            print("   %-38s pasos entonces %2d, hoy %2d  -> %s"
                  % (nid, len(antes), len(ahora), "IDENTICOS" if igual else "CAMBIARON"))
            if not igual:
                movidos.append((nid, len(antes), len(ahora)))
        if movidos:
            rancios.append((v["puesto_intra"], v["clase"], movidos))
            print("   VEREDICTO: RANCIO por texto\n")
        else:
            al_dia.append((v["puesto_intra"], v["clase"]))
            print("   VEREDICTO: al dia\n")

    print("=" * 78)
    print("RANCIOS POR TEXTO: %d" % len(rancios))
    for p, c, mov in sorted(rancios):
        detalle = "; ".join("%s de %d a %d pasos" % m for m in mov)
        print("   %-5d %-3s  %s" % (p, c, detalle))
    print("AL DIA: %d -> %s" % (len(al_dia), sorted(al_dia)))
    ra = sorted(p for p, c, _ in rancios if c == "A")
    print("\nRANCIOS DE CLASE A: %s" % ra)
    print("Y SON LOS QUE SOSTIENEN LAS FAMILIAS: una A rancia es una arista de familia")
    print("dibujada sobre un texto que ya no existe.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
