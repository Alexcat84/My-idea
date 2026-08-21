# -*- coding: utf-8 -*-
"""Cuenta independiente del auditor, vuelta 65 (Fable 5).

AVERIA PROPIA DECLARADA (20 ago 2026): la primera version buscaba la clave
inglesa deprecated donde el esquema usa deprecado, y dio 5 FALLOS falsos
(3853 vivos). Corregida antes de publicar cifra alguna; la especie es la
misma que el acta 64 declaro con la clave id contra id_op.

Verifica la fusion del acto 3 del tramo unico de OP-U-02 (la primera
FUSION N-ARIA de la campana) contra el arbol VIVO y contra el arbol de
APERTURA (b93c28f6), sin reusar los verificadores del ejecutor. Cada
comprobacion imprime OK o FALLO con su detalle. El plan sellado
(PLAN_V65_OPU02_LOTE_A.json) es el contrato; el grafo es el estado.
"""
import json, subprocess, sys, itertools

APERTURA = "b93c28f6"
SUP = "causas_comunes_vs_especiales"
ABS = ["distincion_causas_comunes_especiales",
       "distincion_causas_comunes_especiales_2",
       "distincion_causas_comunes_especiales_incidentes",
       "distincion_causas_especiales_comunes",
       "identificacion_causa_raiz_no_culpa_individual",
       "moral_y_sistema_no_individuo",
       "politica_no_culpar_trabajador",
       "trampa_del_promedio_como_estandar",
       "variacion_del_sistema_vs_individuo"]

fallos = []
n_ok = 0
def check(nombre, cond, detalle=""):
    global n_ok
    if cond:
        n_ok += 1
        print("OK   ", nombre)
    else:
        fallos.append(nombre)
        print("FALLO", nombre, "|", detalle)

def vivo(nid):
    return json.load(open("dataset/nodos/%s.json" % nid, encoding="utf-8"))

def apertura(nid):
    raw = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (APERTURA, nid)],
                         capture_output=True).stdout
    return json.loads(raw)

plan = json.load(open("docs/loop/PLAN_V65_OPU02_LOTE_A.json", encoding="utf-8"))
acto = plan["actos"][0]
check("plan: superviviente es el declarado", acto["superviviente"] == SUP)
check("plan: los 9 absorbidos son los declarados", acto["absorbidos"] == ABS)

s_hoy = vivo(SUP)
s_ap = apertura(SUP)
check("superviviente VIVO (deprecado ausente o falso)", not s_hoy.get("deprecado"))
check("superviviente 15 pasos", len(s_hoy["pasos_accionables"]) == 15, str(len(s_hoy["pasos_accionables"])))
check("superviviente 10 condiciones", len(s_hoy["condiciones_activacion"]) == 10, str(len(s_hoy["condiciones_activacion"])))

# pasos 2, 3, 5 del superviviente INTACTOS; 1, 4, 6 = viejo mas inciso
for i in (2, 3, 5):
    check("sup paso %d INTACTO contra apertura" % i,
          s_hoy["pasos_accionables"][i-1] == s_ap["pasos_accionables"][i-1])
incisos = {1: ("de incidentes o accidentes",),
           4: ("ayudar al trabajador a identificarla y eliminarla",),
           6: ("la proporción estimada de causas sistémicas vs especiales",)}
for i, textos in incisos.items():
    nuevo, viejo = s_hoy["pasos_accionables"][i-1], s_ap["pasos_accionables"][i-1]
    check("sup paso %d ARRANCA en el viejo y trae su inciso" % i,
          nuevo.startswith(viejo) and all(t in nuevo for t in textos),
          nuevo[:120])

# los 9 APPEND de pasos, verbatim del absorbido, en pasos 7..15
appends_pasos = []
for nid in ABS:
    rep = acto["pasos"].get(nid, {})
    for k in sorted(rep, key=int):
        if rep[k] == "APPEND":
            appends_pasos.append((nid, int(k)))
check("son 9 APPEND de pasos en el plan", len(appends_pasos) == 9, str(appends_pasos))
cola = s_hoy["pasos_accionables"][6:]
check("pasos 7..15 son 9", len(cola) == 9)
ap_textos = [apertura(nid)["pasos_accionables"][k-1] for nid, k in appends_pasos]
check("los 9 pasos APPEND estan VERBATIM en la cola del superviviente",
      sorted(cola) == sorted(ap_textos),
      "cola=%r" % (cola[:2],))

# los 7 APPEND de condiciones, verbatim, en condiciones 4..10
appends_conds = []
for nid in ABS:
    rep = acto["condiciones"].get(nid, {})
    for k in sorted(rep, key=int):
        if rep[k] == "APPEND":
            appends_conds.append((nid, int(k)))
check("son 7 APPEND de condiciones en el plan", len(appends_conds) == 7, str(appends_conds))
for i in (1, 2, 3):
    check("sup condicion %d INTACTA" % i,
          s_hoy["condiciones_activacion"][i-1] == s_ap["condiciones_activacion"][i-1])
cola_c = s_hoy["condiciones_activacion"][3:]
ap_conds = [apertura(nid)["condiciones_activacion"][k-1] for nid, k in appends_conds]
check("las 7 condiciones APPEND estan VERBATIM en la cola",
      sorted(cola_c) == sorted(ap_conds))

# el reparto CUBRE EXACTO los indices de cada absorbido (guarda 2 re-contada)
for nid in ABS:
    n_ap = apertura(nid)
    claves_p = sorted(int(k) for k in acto["pasos"].get(nid, {}))
    claves_c = sorted(int(k) for k in acto["condiciones"].get(nid, {}))
    check("reparto de %s cubre pasos 1..%d y condiciones 1..%d" %
          (nid, len(n_ap["pasos_accionables"]), len(n_ap["condiciones_activacion"])),
          claves_p == list(range(1, len(n_ap["pasos_accionables"]) + 1)) and
          claves_c == list(range(1, len(n_ap["condiciones_activacion"]) + 1)))

# piezas: 40 pasos + 18 condiciones = 58
total = sum(len(acto["pasos"][n]) for n in ABS) + sum(len(acto["condiciones"][n]) for n in ABS)
check("58 piezas repartidas", total == 58, str(total))

# los 9 absorbidos: deprecados HOY, texto INTACTO al byte (pasos, condiciones,
# resumen y entregable) contra la apertura, y alias hacia el superviviente
for nid in ABS:
    n_hoy, n_ap = vivo(nid), apertura(nid)
    check("%s deprecado" % nid, n_hoy.get("deprecado") is True, json.dumps(n_hoy)[:120])
    check("%s texto INTACTO (pasos+condiciones+resumen+entregable)" % nid,
          all(n_hoy.get(c) == n_ap.get(c) for c in
              ("pasos_accionables", "condiciones_activacion", "resumen_teorico",
               "entregable_esperado")))

# merged_originals del superviviente carga a los 9
mo = json.dumps(s_hoy.get("merged_originals") or [])
check("merged_originals del superviviente nombra a los 9",
      all(nid in mo for nid in ABS))

# cero referencias vivas a un absorbido y cero auto-aristas en todo el grafo
import glob
refs_muertas, auto = [], []
vivos_n = 0
for f in glob.glob("dataset/nodos/*.json"):
    n = json.load(open(f, encoding="utf-8"))
    if n.get("deprecado"):
        continue
    vivos_n += 1
    nid = n["node_id"]
    vecinos = list(n.get("nodos_previos") or []) + list(n.get("nodos_siguientes") or [])
    for v in vecinos:
        if v in ABS:
            refs_muertas.append((nid, v))
        if v == nid:
            auto.append(nid)
print("  nodos vivos recorridos:", vivos_n)
check("CERO referencias vivas a un absorbido", not refs_muertas, str(refs_muertas[:5]))
check("CERO auto-aristas en los vivos", not auto, str(auto[:5]))
check("vivos == 3262 (la cifra de cierre)", vivos_n == 3262, str(vivos_n))

# el vecino de fuera: distincion_causas_comunes_especiales_3 NO es miembro; se
# mira donde esta hoy
n3 = vivo("distincion_causas_comunes_especiales_3")
print("  _3 deprecado?:", bool(n3.get("deprecado")), "| dominio:", n3.get("dominio"))

print()
print("=" * 70)
print("COMPROBACIONES: %d OK, %d FALLOS" % (n_ok, len(fallos)))
for f in fallos:
    print("  FALLO:", f)
sys.exit(1 if fallos else 0)
