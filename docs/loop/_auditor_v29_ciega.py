# -*- coding: utf-8 -*-
"""Relectura ciega v29: imprime bloques y receptores SIN los motivos del ejecutor."""
import json, subprocess, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
def show(commit, nid):
    if commit is None:
        return json.load(open('dataset/nodos/%s.json'%nid,encoding='utf-8'))
    r=subprocess.run(["git","show","%s:dataset/nodos/%s.json"%(commit,nid)],capture_output=True)
    return json.loads(r.stdout.decode('utf-8')) if r.returncode==0 else None
def bloque(commit,nid,idx):
    d=show(commit,nid)
    return [d['pasos_accionables'][i-1] for i in idx]
def pr(t): print(t)
def nodo_resumen(nid, commit=None, con_resumen=True):
    d=show(commit,nid)
    pr("  NODO %s [%s]" % (nid, d.get('titulo_concepto','')))
    if con_resumen:
        pr("   entregable: %s" % d.get('entregable_esperado',''))
    for i,p in enumerate(d['pasos_accionables'],1): pr("    %d. %s" % (i,p))
CASOS = [
 ("d1","1eef1c6b","actualizacion_posiciones_existentes",range(5,20),["evaluacion_balanceada_de_ejecutivos"],"1eef1c6b"),
 ("d4","9d4a8eb1","analisis_trafico_competitivo",range(5,9),["seleccion_plataforma_social_ads"],"9d4a8eb1"),
 ("d5","9d4a8eb1","decision_pivote_perseverar",range(5,10),["identificacion_bolsas_virales"],"9d4a8eb1"),
 ("d7","9d4a8eb1","key_partners_hypothesis",range(11,15),["pipeline_alianzas_bd","alineacion_bd_metricas_core"],"9d4a8eb1"),
 ("d8","9d4a8eb1","metricas_de_adquisicion_activacion",range(6,10),["sem_estrategia_ejecucion"],"9d4a8eb1"),
 ("d9","1eef1c6b","organizacion_adaptativa",range(5,9),["contratacion_acelerada_hipercrecimiento"],"1eef1c6b"),
 ("d10","1eef1c6b","background_startup_vs_corporativo",range(5,10),["contratar_ambicion_correcta","screening_ambicion_organizacional"],"1eef1c6b"),
 ("d11","1eef1c6b","contratacion_experiencia_vs_potencial",range(5,11),["contratar_por_fortaleza"],"1eef1c6b"),
]
for tag, antes, don, idx, cands, cand_commit in CASOS:
    pr("="*100); pr("%s  BLOQUE de %s pasos %s" % (tag,don,list(idx)))
    d=show(antes,don)
    pr("  (titulo donante: %s)" % d.get('titulo_concepto',''))
    for i in idx: pr("    %d. %s" % (i, d['pasos_accionables'][i-1]))
    pr("  --- CANDIDATOS (estado ANTES del corte) ---")
    for c in cands: nodo_resumen(c, cand_commit)
# d3: los tres bloques del anillo
pr("="*100); pr("d3  LOS TRES BLOQUES FUNDIDOS EN anillo_interior_explotar_el_canal_nucleo")
for don,idx in [("enfoque_motor_unico_crecimiento",range(5,10)),("optimizacion_embudo_get_customers",range(6,11)),("ab_testing_optimizacion",range(11,16))]:
    d=show("9d4a8eb1",don)
    pr("  BLOQUE %s:" % don)
    for i in idx: pr("    %d. %s" % (i,d['pasos_accionables'][i-1]))
pr("  --- el nodo nacido (hoy) ---"); nodo_resumen("anillo_interior_explotar_el_canal_nucleo")
# d2: cuerpo de producto_como_servicio_de_acceso contra sus dos bloques
pr("="*100); pr("d2  producto_como_servicio_de_acceso: bloques 5a8 y 9a12 del donante y cuerpo nacido")
d=show("7521f039","transicion_producto_a_experiencia")
for i in list(range(5,13)): pr("    %d. %s" % (i,d['pasos_accionables'][i-1]))
pr("  --- cuerpo nacido ---")
n=show(None,"producto_como_servicio_de_acceso")
pr("   titulo: %s" % n['titulo_concepto']); pr("   resumen: %s" % n['resumen_teorico'])
pr("   entregable: %s" % n['entregable_esperado'])
for i,p in enumerate(n['pasos_accionables'],1): pr("    %d. %s" % (i,p))
