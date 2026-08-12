# -*- coding: utf-8 -*-
"""Verificacion de la mesa de Coleman ANTES de escribir su expediente. Solo lectura."""
import json, io, sys, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
P = {frozenset((p["nodo_a"], p["nodo_b"])) for p in
     (json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip())}
L = {frozenset((r["nodo_a"], r["nodo_b"])): r for r in V}
AL = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
def res(x):
    s = set()
    while x in AL and x not in s: s.add(x); x = AL[x]
    return x
PROG = {"1 Assess": ["fase_assess","fase_assess_ciclo_cliente","fase_assess_experiencia_cliente"],
        "2 Admit": ["fase_admit","fase_admit_celebracion"],
        "3 Affirm": ["fase_affirm_buyers_remorse"],
        "4 Activate": ["fase_activate","fase_activate_primera_impresion"],
        "5 Acclimate": ["fase_acclimate","fase_acclimate_experiencia_cliente","fase_acclimate_mapa_de_proceso"],
        "6 Accomplish": ["fase_accomplish","fase_accomplish_experiencia_cliente"],
        "7 Adopt": ["fase_adopt","fase_adopt_ciclo_cliente"],
        "8 Advocate": ["advocacy_customer_journey","incentivos_no_monetarios_advocacy"],
        "CABEZA": ["fases_de_retencion_de_clientes","ocho_fases_experiencia_cliente"]}
MED = ["seis_canales_comunicacion_assess","seis_herramientas_comunicacion_fase_activate",
       "seis_herramientas_comunicacion_celebracion","estrategia_multicanal_bienvenida",
       "regalos_estrategicos_personalizados","regalos_estrategicos_sorpresa",
       "sorprender_cliente_estrategico","welcome_call_cliente_veterano"]
SERIE = [x for v in PROG.values() for x in v] + MED
print("SERIE:", len(SERIE), "| programa", sum(len(v) for v in PROG.values()), "| medios", len(MED))
print()
print("=== LAS A DE LA SERIE ===")
As = [(r["puesto_intra"], r["nodo_a"], r["nodo_b"]) for r in V
      if r["clase"] == "A" and r["nodo_a"] in SERIE and r["nodo_b"] in SERIE]
for p, a, b in sorted(As): print("   %4d  %s | %s" % (p, a, b))
print("   TOTAL A:", len(As))
print()
print("=== EL 326: LAS DOS CABEZAS, CABLEADO ===")
for k in PROG["CABEZA"]:
    n = G[k]
    ent = sum(1 for kk, vv in G.items() if not vv.get("deprecado")
              for c in ("nodos_previos","nodos_siguientes") if k in (vv.get(c) or []))
    sal = len(set(res(y) for c in ("nodos_previos","nodos_siguientes") for y in (n.get(c) or [])))
    print("   %-34s pasos %d | alias %s | grados: salen %d, LO NOMBRAN %d"
          % (k, len(n.get("pasos_accionables") or []), n.get("ids_alias"), sal, ent))
    print("       titulo: %s" % n.get("titulo_concepto"))
print()
print("=== MEDIOS: quien los nombra, y desde cuantas FASES distintas ===")
for m in MED:
    desde = []
    for kk, vv in G.items():
        if vv.get("deprecado"): continue
        for c in ("nodos_previos","nodos_siguientes"):
            if m in (vv.get(c) or []): desde.append(kk)
    fases = sorted(set(x for x in set(desde) if x in SERIE))
    print("   %-46s lo nombran %2d | de la serie: %s" % (m, len(set(desde)), ", ".join(fases) or "ninguno"))
print()
print("=== y al reves: que MEDIOS nombra cada nodo de PROGRAMA ===")
for fam, ks in PROG.items():
    for k in ks:
        sal = sorted(set(res(y) for c in ("nodos_previos","nodos_siguientes") for y in (G[k].get(c) or [])) & set(MED))
        if sal: print("   %-14s %-36s -> %s" % (fam, k, ", ".join(sal)))
