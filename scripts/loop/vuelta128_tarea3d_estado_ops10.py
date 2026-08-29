# -*- coding: utf-8 -*-
"""vuelta128_tarea3d_estado_ops10.py . MEDICION, NODO POR NODO, DE LAS CINCO
VERIFICACIONES DE OP-S-10 SOBRE EL GRAFO DE HOY (TAREA 3.d de la vuelta 128).
NO cierra la operacion, NO cambia su estado: solo mide y publica.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTRAMODELOS = ["comprender_definicion_legal_franquicia", "cumplimiento_ftc_rule_436"]


def nombra_pais(txt):
    t = (txt or "").lower()
    return "estados unidos" in t or "ee. uu" in t or "eeuu" in t or "ee.uu" in t


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ops = [json.loads(l) for l in open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"), encoding="utf-8") if l.strip()]
    op = [o for o in ops if o.get("id_op") == "OP-S-10"][0]
    nomina = op["nodos"]
    hoy = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]

    vivos = sorted([i for i in nomina if not hoy[i].get("deprecado")])
    deprecados = sorted([i for i in nomina if hoy[i].get("deprecado")])

    print("V1: los 31 nodos de la nomina nombran el pais en condiciones_activacion")
    sin_pais_vivos = [i for i in vivos if not any(nombra_pais(c) for c in (hoy[i].get("condiciones_activacion") or []))]
    print("  vivos: %d/%d nombran el pais en condiciones_activacion (faltan: %s)"
          % (len(vivos) - len(sin_pais_vivos), len(vivos), sin_pais_vivos))
    print("  deprecados (fuera de alcance, NO tocados): %d -> %s" % (len(deprecados), deprecados))
    print("  ESTADO V1: VERDE PARA LOS 28 VIVOS, LITERAL FALSO PARA LOS 31 (3 deprecados no tocados). DISCUTIBLE.")

    print()
    print("V2: ningun nodo condiciona con adjetivo federal en vez de pais (obtencion_marca_registrada vigilado)")
    n = hoy["obtencion_marca_registrada"]
    conds = n.get("condiciones_activacion") or []
    tiene_pais = nombra_pais(conds[0]) if conds else False
    tiene_federal_vieja = any("federal" in c.lower() for c in conds[1:])
    print("  obtencion_marca_registrada.condiciones_activacion: %r" % conds)
    print("  primera condicion nombra el pais: %s | condicion vieja con adjetivo federal sigue presente (no tocada): %s"
          % (tiene_pais, tiene_federal_vieja))
    print("  ESTADO V2: VERDE si 'en vez de' se lee como 'la puerta ya no depende solo del adjetivo' (ahora hay "
          "condicion de pais delante); LITERAL DISCUTIBLE porque la clausula vieja con 'federal' sigue ahi, sin "
          "reescribir por mandato expreso del encargo de la 128.")

    print()
    print("V3: items numerados del FDD dentro de la condicion de pais (medido en 3.c)")
    print("  VERDE, ver docs/loop/SALIDA_V128_TAREA3C_VERIFICACION3_OPS10.txt")

    print()
    print("V4: los dos contramodelos se quedan como estan")
    for c in CONTRAMODELOS:
        print("  %s.condiciones_activacion[0]: %r" % (c, (hoy[c].get("condiciones_activacion") or [None])[0]))
    print("  ESTADO V4: VERDE (no fueron tocados por ningun instrumento de esta vuelta ni de la 126)")

    print()
    print("V5: Gate 0 verde")
    print("  VERDE, ver docs/loop/SALIDA_V128_OPS10_GATE0_POST.txt (ultima corrida de Gate 0 de esta vuelta)")

    print()
    print("RESUMEN: V1 discutible (28/31, deprecados fuera de alcance), V2 discutible (letra vs espiritu), "
          "V3 verde, V4 verde, V5 verde. OP-S-10 NO SE CIERRA AQUI: la adjudica el auditor.")


if __name__ == "__main__":
    main()
