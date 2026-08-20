# -*- coding: utf-8 -*-
"""_v63_verificar_opm02prog.py . COMPRUEBA, UNA POR UNA, LAS COSAS QUE LA FICHA
DE OP-M-02-PROG MANDA COMPROBAR DESPUES DE FUNDIR.

DE SOLO LECTURA. Lee el arbol de hoy y el arbol de ANTES de la fusion (por git
show), y compara.

LAS CINCO, copiadas del campo verificacion de docs/plan/OPERACIONES.jsonl:
  1. LAS DOS PRIORIDADES estan en el texto del superviviente tras la fusion, que
     es la unica pieza que la ficha manda preservar.
  2. EL SUPERVIVIENTE conserva las piezas propias del que muere, comprobadas una
     por una en su texto.
  3. LAS DOS PIEZAS QUE LA FICHA RECLASIFICA COMO QUE VIVEN DENTRO siguen ahi:
     detectar en que fase se atascan y el plan de avance.
  4. EL ALIAS del superviviente carga el id que muere.
  5. EL ABSORBIDO queda DEPRECADO con su texto INTACTO.
Y una sexta que la ficha escribe y esta vuelta resuelve por P.16, con la
divergencia declarada: LA DUPLICADA QUE LA FUSION FABRICA. La ficha dice que
queda para OP-S-12; P.16 (14 ago 2026, decision del fundador) dice que quien
fabrica limpia en el mismo commit, y su punto 3 convierte a OP-S-12 en
VERIFICACION DE CERO. Aqui se MIDE que no quedo ninguna.

Uso: python scripts/loop/_v63_verificar_opm02prog.py [--antes <hash>]
exit 0 si las seis pasan; exit 1 si alguna falla.
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUP = "ocho_fases_experiencia_cliente"
MUERE = "fases_de_retencion_de_clientes"
TESTIGO = "pensamiento_h2h"
CAMPOS = ("nodos_previos", "nodos_siguientes")
NL = chr(10)


def hoy(nid):
    return json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                             encoding="utf-8"))


def antes(nid, commit):
    bruto = subprocess.check_output(
        ["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)], cwd=RAIZ)
    return json.loads(bruto.decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", default="HEAD",
                    help="commit del arbol PREVIO a la fusion")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    print("=" * 78)
    print("VERIFICACION DE OP-M-02-PROG, LO QUE LA FICHA MANDA COMPROBAR")
    print("  arbol de ANTES: commit %s (por git show)" % a.antes)
    print("=" * 78)

    s = hoy(SUP)
    m = hoy(MUERE)
    m0 = antes(MUERE, a.antes)
    s0 = antes(SUP, a.antes)

    print()
    print("1. LAS DOS PRIORIDADES, EN EL TEXTO DEL SUPERVIVIENTE")
    for aguja in ("Affirm", "Activate"):
        donde = [i for i, x in enumerate(s["pasos_accionables"], 1) if aguja in x]
        ok = bool(donde)
        print("   %-12s %-4s %s" % (aguja, "OK" if ok else "ROJO",
                                    "paso %s" % donde if donde else "NO ESTA"))
        if not ok:
            fallos.append("la prioridad %s no esta en el texto final" % aguja)
    print("   el superviviente queda con %d pasos y %d condiciones (antes %d y %d)"
          % (len(s["pasos_accionables"]), len(s["condiciones_activacion"]),
             len(s0["pasos_accionables"]), len(s0["condiciones_activacion"])))

    print()
    print("2. LAS PIEZAS PROPIAS DEL QUE MUERE, UNA POR UNA")
    piezas = [("paso 3, la priorizacion de Affirm y Activate",
               "Priorizar el dise", s["pasos_accionables"]),
              ("condicion 2, reducir el abandono temprano",
               "abandono temprano", s["condiciones_activacion"])]
    for etq, aguja, lista in piezas:
        donde = [i for i, x in enumerate(lista, 1) if aguja in x]
        ok = bool(donde)
        print("   %-46s %-4s %s" % (etq, "OK" if ok else "ROJO",
                                    "indice %s" % donde if donde else "NO ESTA"))
        if not ok:
            fallos.append("la pieza propia %s no viajo" % etq)

    print()
    print("3. LAS DOS PIEZAS QUE VIVEN DENTRO, INTACTAS Y NO TOCADAS")
    for etq, aguja in (("detectar en que fase se atascan", "atascando"),
                       ("el plan de avance", "plan de acci")):
        donde = [i for i, x in enumerate(s["pasos_accionables"], 1) if aguja in x]
        antes_donde = [i for i, x in enumerate(s0["pasos_accionables"], 1) if aguja in x]
        ok = bool(donde) and donde == antes_donde
        print("   %-36s %-4s hoy en el paso %s (antes %s)"
              % (etq, "OK" if ok else "ROJO", donde, antes_donde))
        if not ok:
            fallos.append("la pieza que vive dentro %s se movio o falta" % etq)

    print()
    print("4. EL ALIAS DEL SUPERVIVIENTE CARGA EL ID QUE MUERE")
    alias = s.get("ids_alias") or []
    fundidos = [x.get("node_id") for x in (s.get("merged_originals") or [])]
    print("   ids_alias: %s | merged_originals: %s" % (alias, fundidos))
    if MUERE not in alias:
        fallos.append("el alias no carga el id que muere")
    if MUERE not in fundidos:
        fallos.append("merged_originals no registra al que muere")

    print()
    print("5. EL ABSORBIDO, DEPRECADO Y CON SU TEXTO INTACTO")
    dep = bool(m.get("deprecado") or m.get("deprecated"))
    intacto = all(m.get(c) == m0.get(c) for c in
                  ("pasos_accionables", "condiciones_activacion") + CAMPOS)
    print("   deprecado: %s | texto y aristas INTACTOS: %s"
          % ("SI" if dep else "NO", "SI" if intacto else "NO"))
    if not dep:
        fallos.append("el absorbido no quedo deprecado")
    if not intacto:
        fallos.append("el absorbido perdio texto o aristas")

    print()
    print("6. LA DUPLICADA QUE LA FUSION FABRICABA, MEDIDA EN EL TESTIGO")
    t = hoy(TESTIGO)
    t0 = antes(TESTIGO, a.antes)
    print("   ANTES, %s en nodos_siguientes nombraba a los DOS miembros: %s"
          % (TESTIGO, SUP in (t0.get("nodos_siguientes") or [])
             and MUERE in (t0.get("nodos_siguientes") or [])))
    lista = t.get("nodos_siguientes") or []
    veces = lista.count(SUP)
    print("   HOY  : lo nombra %d vez(veces) y al muerto %d"
          % (veces, lista.count(MUERE)))
    if veces != 1 or MUERE in lista:
        fallos.append("el testigo no quedo con UNA sola entrada al superviviente")
    auto = SUP in (s.get("nodos_siguientes") or [])
    print("   AUTO-ARISTA: el superviviente se nombra a si mismo: %s (tiene que ser False)"
          % auto)
    if auto:
        fallos.append("quedo la auto-arista que la fusion creaba")

    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d comprobacion(es) fallan:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("LAS SEIS EN VERDE.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
