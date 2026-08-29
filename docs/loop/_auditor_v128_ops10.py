# -*- coding: utf-8 -*-
"""Auditor v128: reconstruye el tramo de OP-S-10 con codigo propio."""
import json, io, subprocess, sys

def grafo(ref):
    if ref == 'WORK':
        return json.load(io.open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
    out = subprocess.run(['git','show',ref+':dataset/metadata/master_graph.json'],
                         capture_output=True)
    return json.loads(out.stdout.decode('utf-8'))['nodos']

nomina = None
for l in io.open('docs/plan/OPERACIONES.jsonl', encoding='utf-8'):
    if not l.strip(): continue
    o = json.loads(l)
    if o.get('id_op') == 'OP-S-10':
        nomina = o['nodos']
print("NOMINA (campo nodos):", len(nomina), "unicos:", len(set(nomina)))

APER, WORK = grafo('9ef3705d'), grafo('WORK')
LIT = "Solo aplica si vendes o piensas vender franquicias en Estados Unidos"

def clasifica(G):
    vivos, depre = [], []
    for nid in sorted(set(nomina)):
        n = G.get(nid)
        if n is None: depre.append((nid,'AUSENTE')); continue
        (depre if n.get('deprecado') else vivos).append(nid)
    return vivos, depre

va, da = clasifica(APER)
vw, dw = clasifica(WORK)
print("APERTURA: vivos", len(va), "deprecados", len(da), [d for d in da])
print("WORK    : vivos", len(vw), "deprecados", len(dw))

def nombra_pais(n):
    return any('Estados Unidos' in c for c in (n.get('condiciones_activacion') or []))
def tiene_literal(n):
    ca = n.get('condiciones_activacion') or []
    return bool(ca) and ca[0].strip() == LIT

cand_ap = [i for i in va if not nombra_pais(APER[i])]
print("\nCANDIDATOS EN APERTURA (vivos que NO nombran el pais en condiciones_activacion):", len(cand_ap))
for i in cand_ap: print("   -", i)

# los que ya llevaban el literal en apertura = tramo de la 126
ya126 = [i for i in va if tiene_literal(APER[i])]
print("\nCON EL LITERAL YA EN APERTURA (tramo vuelta 126):", len(ya126))

nuevos = [i for i in vw if tiene_literal(WORK[i]) and not tiene_literal(APER.get(i,{}))]
print("\nNODOS QUE ESTA VUELTA ANTEPONE EL LITERAL:", len(nuevos))
for i in nuevos: print("   -", i)

print("\nDIFERENCIA candidatos_apertura vs escritos:",
      "sobran", sorted(set(nuevos)-set(cand_ap)), "faltan", sorted(set(cand_ap)-set(nuevos)))

# viejas enteras y en su orden
malos = []
for i in nuevos:
    a = APER[i].get('condiciones_activacion') or []
    h = WORK[i].get('condiciones_activacion') or []
    if h[1:] != a: malos.append(i)
print("VIEJAS ENTERAS Y EN SU ORDEN (h[1:]==a) FALLAN EN:", malos or "NINGUNO")

# contramodelos y deprecados intactos
contra = ['comprender_definicion_legal_franquicia','cumplimiento_ftc_rule_436']
for c in contra:
    print("CONTRAMODELO", c, "intacto:", APER[c].get('condiciones_activacion')==WORK[c].get('condiciones_activacion'))
for d in da:
    nid=d[0]
    if nid in APER and nid in WORK:
        print("DEPRECADO", nid, "intacto:", APER[nid]==WORK[nid])

# cobertura final: de los 28 vivos, cuantos nombran el pais en condiciones_activacion
cob = [i for i in vw if nombra_pais(WORK[i])]
print("\nCOBERTURA FINAL: vivos que nombran el pais en condiciones_activacion:", len(cob), "de", len(vw))
sin = [i for i in vw if not nombra_pais(WORK[i])]
print("SIN CUBRIR:", sin or "NINGUNO")
# literal exacto vs otros
print("con el literal exacto primero:", sum(1 for i in vw if tiene_literal(WORK[i])))
