# -*- coding: utf-8 -*-
"""vuelta102_tarea3_relectura_ciega_tramo1.py . VUELTA 102, TAREA 3: LA
RELECTURA AL DOBLE DEL TRAMO 1, DISPARADA POR LA CAIDA DE CLASE DEL AUDITOR
(acta de la vuelta 101, seccion 4.3: la discrepancia del puesto 5 aparecio
FUERA de los discutibles marcados, y `AUDITOR.md` 1.2 manda releer al doble
sin distinguir quien se equivoco).

MUESTRA, EN LOS DOS FLANCOS, EL DOBLE DE LO NORMAL (8 en vez de 4), fijado
como el acta 99/100: 4 RESUELTAS de MENOR `titulo_ratio` y 4 NO RESUELTAS de
MAYOR `titulo_ratio` (el flanco que ha dado los hallazgos hasta ahora),
LEIDO de `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl`, indexado por
`puesto_tramo - 1` (mismo mecanismo verificado que usaron las vueltas 99 y
100). El puesto 5 QUEDA FUERA de la muestra: ya esta adjudicado y cerrado
(acta 101, 4.2, CEDIDO por el auditor).

--modo blind: A CIEGAS DE VERDAD, CON INSTRUMENTO Y NO A OJO. Para cada
puesto de la muestra, vuelca el `entregable_esperado` y los
`pasos_accionables` COMPLETOS de la madre y el hijo, leidos de
`dataset/nodos/<id>.json`. NO IMPRIME `clase`, NI `direccion_leida`, NI
`razon`, NI CUAL paso esta casado: la adjudicacion del ejecutor se escribe
DESPUES de leer solo esto, y solo entonces se corre --modo reveal para
comparar contra el registro.

--modo reveal: destapa, para la misma muestra, `paso_casado`,
`direccion_leida` (RESUELTA/NO RESUELTA) y `razon` de
`docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`.

USO:
  python scripts/loop/vuelta102_tarea3_relectura_ciega_tramo1.py --modo blind
  python scripts/loop/vuelta102_tarea3_relectura_ciega_tramo1.py --modo reveal

MECANICA DE ROJO: si `DIFERENCIA_CONTRA_COLA.jsonl` no tiene 183 filas, si el
cotejo puesto-a-puesto de un puesto de la muestra no casa madre/hijo contra
`OP_E_03_LECTURA_TRAMO1_V96.jsonl`, o si falta el fichero de un nodo, NO SE
IMPRIME NADA y sale con exit 1.
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
DIFCOLA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

PUESTO_EXCLUIDO = 5


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def estado_efectivo(f):
    return bool(f.get("direccion_leida"))


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
        if p == PUESTO_EXCLUIDO:
            continue
        d = dc[p - 1]
        if d.get("madre") != f.get("madre_de_la_bolsa") or d.get("hijo") != f.get("hijo_de_la_bolsa"):
            fallos.append("puesto_tramo %d no casa madre/hijo contra DIFERENCIA_CONTRA_COLA[%d]" % (p, p - 1))
            continue
        filas.append((p, estado_efectivo(f), d.get("titulo_ratio"), f))

    resueltas = sorted([r for r in filas if r[1]], key=lambda r: r[2])[:4]
    no_resueltas = sorted([r for r in filas if not r[1]], key=lambda r: -r[2])[:4]
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
    print("MUESTRA (8 puestos, excluido el 5): %s" % ", ".join(str(p) for p in orden))
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
        print("direccion_leida (registro): %s" % ("RESUELTA (" + str(f.get("direccion_leida")) + ")" if efectivo else "NO RESUELTA"))
        print("razon: %s" % f.get("razon"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
