# -*- coding: utf-8 -*-
"""vuelta159_dossier.py . EL DOSSIER DE LA VUELTA 159, CON LA NOMINA COMO
ARGUMENTO.

IMPRIME LOS DOS NODOS DE CADA LECTURA de una nomina sellada, para que la
pregunta de la adjudicacion 6.4 del acta 157, corregida por la 6.3 del acta 158,
se pueda contestar CONTRA LOS NODOS y no contra la razon escrita:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

Y LA CORRECCION DE LA 6.3, QUE ES LO QUE ESTA VUELTA ANADE: LA PREGUNTA ES UN
EXISTENCIAL. Un par de lineas que colapsa descarta ESE PAR, no el nodo. Por eso
el dossier imprime LOS PASOS ENTEROS DE LOS DOS NODOS y no un resumen: sin los
pasos enteros no se puede recorrer el espacio de pares.

POR QUE NACE CON NOMINA COMO ARGUMENTO Y NO CLONADO: la vuelta 159 tiene TRES
nominas distintas (las tres en disputa, el tramo de 41 que se relee al doble y
el lote 2 de 53), y la del lote 1 ya tenia su propio clon. Un solo instrumento
con `--nomina` evita tres copias que se desincronizan.

USO:
  python scripts/loop/vuelta159_dossier.py --nomina docs/loop/NOMINA_V159_RELECTURA.json
  python scripts/loop/vuelta159_dossier.py --ids LD-OPC05-005,LD-OPC05-027
  python scripts/loop/vuelta159_dossier.py --nomina X.json --desde 0 --hasta 20
"""
import argparse
import io
import json
import os
import sys

# --- CORRECCION DECLARADA (vuelta 159, TAREA 3), Y NO SE TAPA LO QUE CORRIGE ---
# La primera corrida del dossier del lote 2 MURIO en la lectura 14 de 53 con
# UnicodeEncodeError: la consola de Windows redirige en cp1252 y el paso 13 de
# `reunion_conclusion_proyecto` trae un caracter U+2192 (flecha). La salida quedo
# TRUNCADA con exit 1. Un dossier truncado que no se declara es una lectura a
# medias vendida como entera, asi que se arregla el instrumento y se dice.
# El arreglo NO cambia lo que se imprime: solo fuerza utf-8 en la salida.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")


def razon_original(razon):
    i = razon.find("  [")
    return razon if i < 0 else razon[:i]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", default=None)
    ap.add_argument("--clave", default="tramo")
    ap.add_argument("--ids", default=None)
    ap.add_argument("--desde", type=int, default=0)
    ap.add_argument("--hasta", type=int, default=9999)
    a = ap.parse_args()

    if a.ids:
        ids = [x.strip() for x in a.ids.split(",") if x.strip()]
        origen = "--ids en la linea de comandos"
    else:
        ruta = os.path.join(RAIZ, a.nomina)
        d = json.load(io.open(ruta, encoding="utf-8"))
        ids = d[a.clave]
        origen = a.nomina + " (clave %s)" % a.clave

    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    E = {}
    for x in io.open(REGISTRO, encoding="utf-8").read().splitlines():
        if x.strip():
            e = json.loads(x)
            E[e["cita"].split(",")[0].strip()] = e

    print("DOSSIER DE LA VUELTA 159. NOMINA: %s" % origen)
    print("CIFRA lecturas de la nomina: %d. ESTE TRAMO CUBRE [%d, %d)."
          % (len(ids), a.desde, a.hasta))
    print("")

    for i, ld in enumerate(ids):
        if not (a.desde <= i < a.hasta):
            continue
        e = E[ld]
        print("=" * 78)
        print("%s  [%d de %d]  clase de hoy: %s" % (ld, i + 1, len(ids), e["clase"]))
        print("PAR: %s <-> %s" % (e["par"][0], e["par"][1]))
        print("RAZON ORIGINAL: %s" % razon_original(e["razon"]).strip())
        print("=" * 78)
        for nid in e["par"]:
            n = N.get(nid) or {}
            print("")
            print("  --- %s ---" % nid)
            print("  TITULO   : %s" % (n.get("titulo_concepto") or "(sin titulo)"))
            print("  FUENTE   : %s" % (n.get("fuente") or "(sin fuente)"))
            print("  DOMINIO  : %s" % (n.get("dominio") or "(sin dominio)"))
            ent = n.get("entregable_esperado") or n.get("entregable") or ""
            print("  ENTREGABLE: %s" % (ent or "(sin entregable)"))
            pasos = n.get("pasos_accionables") or []
            print("  PASOS (%d):" % len(pasos))
            for j, p in enumerate(pasos, 1):
                if isinstance(p, dict):
                    p = p.get("texto") or p.get("paso") or json.dumps(p, ensure_ascii=False)
                print("    %d. %s" % (j, p))
        print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
