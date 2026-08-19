# -*- coding: utf-8 -*-
"""vuelta41_plan_acto.py - CONSTRUYE Y SELLA el plan de fusion de UN acto de OP-D-06.

ESTRICTAMENTE DE SOLO LECTURA SOBRE EL GRAFO. Lo unico que escribe es el propio
plan en docs/loop/PLAN_V41_ACTO<puesto>.json. No toca ni un nodo.

SUCESOR DECLARADO de scripts/loop/vuelta40_plan_opd05.py, al que NO reemplaza.
Aquel tenia UN acto entero teclado dentro del script (superviviente, absorbidos,
grupos, motivos, entregable, resumen, lectura de P.8), porque era UNA fusion. Los
ocho actos que OP-D-06 funde no caben en ocho copias del mismo script sin que la
octava se desvie de la primera, y una guarda que se copia ocho veces es una
guarda que se afloja ocho veces.

LO QUE CAMBIA, y es el unico cambio: la parte MEDIDA (origenes verbatim,
redirecciones, duplicadas fabricadas, simetrizacion esperada, tabla de P.13) vive
AQUI y se corre igual para los ocho; la parte LEIDA (los grupos, sus motivos, el
entregable, el resumen y la lectura de contenido de P.8) vive en un modulo por
acto bajo scripts/loop/v41_actos/. La lectura no sale de un instrumento, y por
eso se separa en vez de esconderse.

EL ESQUEMA DE SALIDA es el de la vuelta 38 y NO se cambia, porque el ejecutor
scripts/loop/vuelta39_fundir.py lo consume tal cual y sus trece guardas estan
escritas contra el.

Uso: python scripts/loop/vuelta41_plan_acto.py --puesto 285
"""
import argparse
import importlib
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOOP = os.path.join(RAIZ, "docs", "loop")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def leer(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puesto", type=int, required=True)
    args = ap.parse_args()

    cfg = importlib.import_module("v41_actos.acto_%d" % args.puesto)
    SUP = cfg.SUP
    ABS = list(cfg.ABS)
    PREF = dict(cfg.PREF)

    nodos = dict((nid, leer(nid)) for nid in [SUP] + ABS)

    # --- origenes VERBATIM, generados del fichero (regla 1) ---
    origenes = {}
    for p, nid in PREF.items():
        d = nodos[nid]
        for i, t in enumerate(d.get("pasos_accionables") or [], 1):
            origenes["%s%d" % (p, i)] = t
        for i, t in enumerate(d.get("condiciones_activacion") or [], 1):
            origenes["%sC%d" % (p, i)] = t

    # --- las redirecciones, con la MISMA aritmetica del ejecutor de fusiones ---
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = leer(nombre[:-5])
            todos[d["node_id"]] = d
    redirecciones, muertos = [], []
    for nid, d in todos.items():
        if nid in ABS:
            continue
        for campo in CAMPOS:
            for muere in ABS:
                if muere in (d.get(campo) or []):
                    fila = {"nodo": nid, "campo": campo, "nombraba": muere}
                    (muertos if d.get("deprecado") or d.get("deprecated")
                     else redirecciones).append(fila)
    redirecciones.sort(key=lambda r: (r["nodo"], r["campo"], r["nombraba"]))
    muertos.sort(key=lambda r: (r["nodo"], r["campo"], r["nombraba"]))

    # --- las duplicadas que la fusion fabrica, misma aritmetica ---
    dup = []
    for r in redirecciones:
        antes = list(todos[r["nodo"]].get(r["campo"]) or [])
        despues = [SUP if x in ABS else x for x in antes]
        if (len(despues) - len(set(despues))) > (len(antes) - len(set(antes))):
            f = {"nodo": r["nodo"], "campo": r["campo"], "resuelve_a": SUP}
            if f not in dup:
                dup.append(f)

    # --- la simetrizacion esperada, medida y no supuesta ---
    propias = dict((c, list(nodos[SUP].get(c) or [])) for c in CAMPOS)
    sim_aristas = []
    for r in redirecciones:
        if r["nodo"] in propias[OPUESTO[r["campo"]]]:
            continue
        a = {"campo": OPUESTO[r["campo"]], "vecino": r["nodo"]}
        if a not in sim_aristas:
            sim_aristas.append(a)
    sim_aristas.sort(key=lambda a: (a["campo"], a["vecino"]))

    plan = {
        "operacion": cfg.OPERACION,
        "estado": cfg.ESTADO,
        "regla": cfg.REGLA,
        "motivo": cfg.MOTIVO,
        "fecha_corte": "2026-08-19",
        "superviviente": SUP,
        "absorbidos": list(ABS),
        "fuente_esperada": nodos[SUP].get("fuente"),
        "prefijos": dict((p, ("%s (superviviente)" % nid) if nid == SUP else nid)
                         for p, nid in PREF.items()),
        "origenes": origenes,
        "grupos_pasos": [{"origenes": o, "texto": t, "motivo": m}
                         for o, t, m in cfg.GRUPOS_PASOS],
        "grupos_condiciones": [{"origenes": o, "texto": t, "motivo": m}
                               for o, t, m in cfg.GRUPOS_CONDICIONES],
        "pasos_finales": [t for _o, t, _m in cfg.GRUPOS_PASOS],
        "condiciones_finales": [t for _o, t, _m in cfg.GRUPOS_CONDICIONES],
        "entregable_final": cfg.ENTREGABLE,
        "resumen_final": cfg.RESUMEN,
        "titulo_sin_cambio": nodos[SUP].get("titulo_concepto"),
        "etiqueta_arbol_sin_cambio": nodos[SUP].get("etiqueta_arbol"),
        "preservar_literal": list(cfg.PRESERVAR),
        "rastros": list(cfg.RASTROS),
        "entregable_viejo": nodos[SUP].get("entregable_esperado"),
        "resumen_viejo": nodos[SUP].get("resumen_teorico"),
        "pasos_totales": dict((nid, len(nodos[nid].get("pasos_accionables") or []))
                              for nid in [SUP] + ABS),
        "condiciones_totales": dict(
            (nid, len(nodos[nid].get("condiciones_activacion") or []))
            for nid in [SUP] + ABS),
        "eleccion_p8": cfg.ELECCION_P8,
        "simulacion": {
            "instrumento": ("scripts/loop/vuelta39_fundir.py --simular, "
                            "scripts/loop/vuelta40_reciprocidad_post.py y "
                            "scripts/loop/vuelta40_registros_no_grafo.py"),
            "redirecciones_esperadas": redirecciones,
            "redirecciones_no_tocadas_por_deprecadas": muertos,
            "duplicadas_nuevas_esperadas": dup,
            "registros_que_no_son_el_grafo": {
                "por_que_va_en_el_plan": ("la leccion de la vuelta 39: su plan "
                                          "enumero referencias de NODO, no miro el "
                                          "registro de puentes, y Gate 0 cayo en "
                                          "rojo DESPUES de escribir. Aqui se "
                                          "enumera ANTES."),
                "instrumento": ("scripts/loop/vuelta40_registros_no_grafo.py, "
                                "salida sellada por acto"),
                "aun_asi_se_corre": ("scripts/reanclar_por_resolutor.py ENTRE la "
                                     "fusion y run_phase1, practica adjudicada por "
                                     "el acta de la vuelta 39 para toda fusion "
                                     "futura. Una guarda que solo se corre cuando "
                                     "se sospecha no es una guarda."),
            },
            "simetrizacion_esperada": {
                "quien_la_escribe": ("scripts/run_phase1.py, paso 5, Simetrizacion "
                                     "de enlaces. NO la escribe el ejecutor de "
                                     "fusiones: el redirige a los vecinos y no toca "
                                     "la lista propia del superviviente."),
                "guarda_para_el_dia_de_la_ejecucion": ("symmetrize_added tiene que "
                                                       "traer EXACTAMENTE estas "
                                                       "entradas para el "
                                                       "superviviente, ni una mas "
                                                       "ni una menos"),
                "aristas": sim_aristas,
            },
        },
        "tabla_perdidas_p13": [],
    }

    # --- la tabla de perdidas, DERIVADA de los grupos (regla 1) ---
    destino = {}
    for k, (ors, _t, _m) in enumerate(cfg.GRUPOS_PASOS, 1):
        for o in ors:
            destino[o] = "paso %d del resultado" % k
    for k, (ors, _t, _m) in enumerate(cfg.GRUPOS_CONDICIONES, 1):
        for o in ors:
            destino[o] = "condicion %d del resultado" % k
    for clave in sorted(origenes, key=lambda x: (x[0], "C" in x, x)):
        nid = PREF[clave[0]]
        plan["tabla_perdidas_p13"].append({
            "pieza": clave,
            "texto": origenes[clave],
            "de": nid,
            "clase": "VIAJA" if clave in destino else "SE PIERDE",
            "destino": destino.get(clave, ""),
        })

    salida = os.path.join(LOOP, "PLAN_V41_ACTO%d.json" % args.puesto)
    io.open(salida, "w", encoding="utf-8", newline="\n").write(
        json.dumps(plan, ensure_ascii=False, indent=1) + "\n")

    print("PLAN SELLADO: %s" % os.path.relpath(salida, RAIZ).replace("\\", "/"))
    print("  acto          : puesto %d de OP-D-06" % args.puesto)
    print("  superviviente : %s" % SUP)
    print("  absorbidos    : %s" % ", ".join(ABS))
    print("  fuente del superviviente: %s" % plan["fuente_esperada"])
    fuentes = set(nodos[nid].get("fuente") for nid in [SUP] + ABS)
    print("  ACTO DE FUENTE %s (%d fuente(s) distinta(s) medida(s)):"
          % ("MIXTA" if len(fuentes) > 1 else "UNICA", len(fuentes)))
    for nid in [SUP] + ABS:
        print("      %-44s %-14s %s"
              % (nid, "superviviente" if nid == SUP else "absorbido",
                 nodos[nid].get("fuente")))
    print("  origenes generados VERBATIM del fichero: %d" % len(origenes))
    print("  pasos finales : %d (estandar 3 a 6: %s)"
          % (len(plan["pasos_finales"]),
             "DENTRO" if 3 <= len(plan["pasos_finales"]) <= 6 else "FUERA"))
    print("  condiciones finales: %d" % len(plan["condiciones_finales"]))
    print("  redirecciones esperadas: %d" % len(redirecciones))
    for r in redirecciones:
        print("      %-46s %-18s %s" % (r["nodo"], r["campo"], r["nombraba"]))
    print("  deprecados que nombran y no se tocan: %d" % len(muertos))
    for r in muertos:
        print("      %-46s %-18s %s" % (r["nodo"], r["campo"], r["nombraba"]))
    print("  duplicadas que la fusion fabrica: %d" % len(dup))
    for f in dup:
        print("      %-46s %s" % (f["nodo"], f["campo"]))
    print("  simetrizacion esperada: %d aristas" % len(sim_aristas))
    for a in sim_aristas:
        print("      %s.%-18s += %s" % (SUP, a["campo"], a["vecino"]))
    print("")
    print("  LA TABLA DE PERDIDAS, DERIVADA de los grupos y no tecleada:")
    viajan = [f for f in plan["tabla_perdidas_p13"] if f["clase"] == "VIAJA"]
    pierden = [f for f in plan["tabla_perdidas_p13"] if f["clase"] != "VIAJA"]
    for f in plan["tabla_perdidas_p13"]:
        print("      %-5s %-40s %-10s %s" % (f["pieza"], f["de"][:40], f["clase"],
                                             f["destino"]))
    print("      VIAJAN %d de %d. SE PIERDEN %d."
          % (len(viajan), len(plan["tabla_perdidas_p13"]), len(pierden)))
    print("      LECTURA: la regla de reparto de OP-D-06 manda cada perdida al")
    print("      bloque del que proviene, y la que no tenga bloque al")
    print("      superviviente. Con CERO perdidas no hay nada que repartir, y eso")
    print("      es lo que hay que comprobar al cierre, no suponerlo.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
