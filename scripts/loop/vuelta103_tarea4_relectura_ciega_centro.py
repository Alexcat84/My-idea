# -*- coding: utf-8 -*-
"""vuelta103_tarea4_relectura_ciega_centro.py . VUELTA 103, TAREA 4: LA
RELECTURA AL DOBLE DEL TRAMO 1 POR EL CENTRO (encargo del auditor, acta de la
vuelta 102: "el 28 tiene ratio 87,5 y el 40 tiene 74,3, los dos EN MITAD del
flanco RESUELTA, donde la regla de los extremos no llega nunca").

A DIFERENCIA de `vuelta102_tarea3_relectura_ciega_tramo1.py` (4 RESUELTA de
MENOR titulo_ratio y 4 NO RESUELTA de MAYOR titulo_ratio, los DOS EXTREMOS),
esta muestra toma, en cada flanco, los 4 puestos MAS CERCANOS A LA MEDIANA
del flanco (el centro, no las puntas), leido de
`docs/plan/DIFERENCIA_CONTRA_COLA.jsonl` indexado por `puesto_tramo - 1`.

QUEDAN FUERA de la muestra (no cuentan para los 8): el puesto 5 (cerrado en
la vuelta 101), los ocho de la TAREA 3 de la vuelta 102 (33, 30, 7, 27, 22,
23, 26, 12), y el 28 y el 40 (resueltos en la TAREA 2 de esta misma vuelta,
con `correccion_v103`). El estado RESUELTA/NO RESUELTA de cada puesto se lee
EFECTIVO (aplica `correccion_vNN` sobre `direccion_leida` si la fila trae
alguna), no crudo.

--modo blind: A CIEGAS DE VERDAD, CON INSTRUMENTO Y NO A OJO. Para cada
puesto de la muestra, vuelca el `entregable_esperado` y los
`pasos_accionables` COMPLETOS de la madre y el hijo, leidos de
`dataset/nodos/<id>.json`. NO IMPRIME `clase`, NI `direccion_leida`, NI
`razon`, NI CUAL paso esta casado.

--modo reveal: destapa, para la misma muestra, `paso_casado`,
`direccion_leida` efectiva (RESUELTA/NO RESUELTA) y `razon` de
`docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`.

USO:
  python scripts/loop/vuelta103_tarea4_relectura_ciega_centro.py --modo blind
  python scripts/loop/vuelta103_tarea4_relectura_ciega_centro.py --modo reveal

MECANICA DE ROJO: si `DIFERENCIA_CONTRA_COLA.jsonl` no tiene 183 filas, si el
cotejo puesto-a-puesto de un puesto de la muestra no casa madre/hijo contra
`OP_E_03_LECTURA_TRAMO1_V96.jsonl`, o si falta el fichero de un nodo, NO SE
IMPRIME NADA y sale con exit 1.
"""
import argparse
import io
import json
import os
import statistics
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
DIFCOLA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

EXCLUIDOS = {5, 33, 30, 7, 27, 22, 23, 26, 12, 28, 40}


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def direccion_efectiva(f):
    valor = f.get("direccion_leida")
    for k in sorted(x for x in f if x.startswith("correccion_v")):
        c = f[k]
        if c.get("campo_corregido") == "direccion_leida":
            valor = c.get("valor_nuevo")
    return valor


def muestra(fallos):
    tramo = cargar(TRAMO1)
    if len(tramo) != 40:
        fallos.append("%s trae %d filas, se esperaban 40" % (os.path.basename(TRAMO1), len(tramo)))
        return []
    dc = cargar(DIFCOLA)
    if len(dc) != 183:
        fallos.append("DIFERENCIA_CONTRA_COLA.jsonl trae %d filas, se esperaban 183" % len(dc))
        return []

    filas = []
    for f in tramo:
        p = f["puesto_tramo"]
        if p in EXCLUIDOS:
            continue
        d = dc[p - 1]
        if d.get("madre") != f.get("madre_de_la_bolsa") or d.get("hijo") != f.get("hijo_de_la_bolsa"):
            fallos.append("puesto_tramo %d no casa madre/hijo contra DIFERENCIA_CONTRA_COLA[%d]" % (p, p - 1))
            continue
        filas.append((p, bool(direccion_efectiva(f)), d.get("titulo_ratio"), f))

    def centro4(lst):
        ratios = sorted(r[2] for r in lst)
        med = statistics.median(ratios)
        ordenado = sorted(lst, key=lambda r: (abs(r[2] - med), r[2]))
        return sorted(ordenado[:4], key=lambda r: r[2])

    resueltas = centro4([r for r in filas if r[1]])
    no_resueltas = centro4([r for r in filas if not r[1]])
    return resueltas + no_resueltas


def cargar_nodo(node_id, fallos):
    ruta = os.path.join(NODOS, "%s.json" % node_id)
    if not os.path.exists(ruta):
        fallos.append("no existe dataset/nodos/%s.json" % node_id)
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modo", choices=["blind", "reveal"], required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    filas = muestra(fallos)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    orden = [p for p, _, _, _ in filas]
    print("=" * 100)
    print("MUESTRA POR EL CENTRO (8 puestos, excluidos %s): %s"
          % (", ".join(str(x) for x in sorted(EXCLUIDOS)), ", ".join(str(p) for p in orden)))
    print("=" * 100)

    if a.modo == "blind":
        for p, efectivo, tr, f in filas:
            madre_id = f["madre_de_la_bolsa"]
            hijo_id = f["hijo_de_la_bolsa"]
            madre = cargar_nodo(madre_id, fallos)
            hijo = cargar_nodo(hijo_id, fallos)
            if madre is None or hijo is None:
                continue
            print()
            print("--- PUESTO %d ---" % p)
            print("MADRE: %s" % madre_id)
            print("  entregable_esperado: %s" % madre.get("entregable_esperado"))
            print("  pasos_accionables:")
            for i, paso in enumerate(madre.get("pasos_accionables", []), 1):
                print("    %d. %s" % (i, paso))
            print("HIJO: %s" % hijo_id)
            print("  entregable_esperado: %s" % hijo.get("entregable_esperado"))
            print("  pasos_accionables:")
            for i, paso in enumerate(hijo.get("pasos_accionables", []), 1):
                print("    %d. %s" % (i, paso))
        if fallos:
            print()
            print("ROJO, %d cosa(s) no se pudieron leer:" % len(fallos))
            for x in fallos:
                print("   %s" % x)
            return 1
        return 0

    # --modo reveal
    for p, efectivo, tr, f in filas:
        print()
        print("--- PUESTO %d ---" % p)
        print("madre: %s -- hijo: %s" % (f["madre_de_la_bolsa"], f["hijo_de_la_bolsa"]))
        print("titulo_ratio: %s" % tr)
        print("paso_casado: %s" % f.get("paso_casado"))
        print("direccion_leida (registro efectivo): %s" % ("RESUELTA (" + str(direccion_efectiva(f)) + ")" if efectivo else "NO RESUELTA"))
        print("razon: %s" % f.get("razon"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
