# -*- coding: utf-8 -*-
"""Auditor 127: identifica, para cada arista huerfana por fusion NUEVA desde
el nacimiento de pasada-unica (cbc6ce51), de que nodo MUERTO viene y en que
commit murio ese nodo."""
import json, os, subprocess
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
nodos = json.load(open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))["nodos"]
alias={}
for nid,n in nodos.items():
    if n.get("deprecado"): continue
    for x in (n.get("ids_alias") or []): alias[x]=nid
def res(x):
    v=set()
    while x in alias and x not in v: v.add(x); x=alias[x]
    return x
def vivo(i):
    n=nodos.get(i); return n is not None and not n.get("deprecado")
def pres(o,d):
    return d in (nodos[o].get("nodos_siguientes") or []) or o in (nodos[d].get("nodos_previos") or [])
objetivo = {
 ('comprension_capacidades_limitaciones_ia','division_trabajo_humano_ia'),
 ('concepto_quality_is_free','programa_mejora_calidad_14_pasos'),
 ('ecosistema_global_emprendimiento_gee','uso_del_us_commercial_service'),
 ('error_proofing_servicio','metodologia_6s'),
 ('incentivos_reconocimiento_sostenibilidad','vision_alineacion_sostenibilidad'),
 ('metodologia_6s','error_proofing_servicio'),
}
proc={}
for muere,n in nodos.items():
    if not n.get("deprecado"): continue
    sup=res(muere)
    if sup==muere or not vivo(sup): continue
    for campo,dr in (("nodos_siguientes","sig"),("nodos_previos","prev")):
        for x in (n.get(campo) or []):
            otro=res(x)
            if otro==sup or not vivo(otro): continue
            o,d=(sup,otro) if dr=="sig" else (otro,sup)
            if (o,d) in objetivo and not pres(o,d):
                proc.setdefault((o,d),[]).append((muere,campo,x))
def muerte(nid):
    r=subprocess.run(["git","log","--oneline","-S",'"deprecado": true',"--","dataset/nodos/%s.json"%nid],cwd=RAIZ,capture_output=True)
    ls=[l for l in r.stdout.decode("utf-8","replace").splitlines() if l.strip()]
    return ls[0][:90] if ls else "(sin rastro en dataset/nodos)"
for par in sorted(objetivo):
    print("ARISTA FALTANTE: %s -> %s" % par)
    for muere,campo,x in proc.get(par,[]):
        print("   viene del muerto %-45s (%s, entrada cruda '%s')" % (muere,campo,x))
        print("      murio en: %s" % muerte(muere))
