# -*- coding: utf-8 -*-
"""Instrumento del AUDITOR, vuelta 29. Todo se mide HOY contra el arbol en HEAD."""
import json, os, sys
from collections import Counter
RAIZ = os.getcwd()
def jl(ruta):
    out=[]
    for ln in open(ruta, encoding="utf-8"):
        ln=ln.strip()
        if ln: out.append(json.loads(ln))
    return out

print("="*70); print("1. MARCADOR (docs/INTRA_DOMINIO_VEREDICTOS.jsonl)"); print("="*70)
v=jl("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
p=[x["puesto_intra"] for x in v]; c=Counter(x["clase"] for x in v); n=len(v)
print("n=%d  rango %d..%d  huecos=%d  dup=%d  fueraABCD=%s" % (
    n, min(p), max(p), len(set(range(min(p),max(p)+1))-set(p)),
    sum(1 for k,x in Counter(p).items() if x>1),
    sorted(set(c)-set("ABCD")) or 0))
for k in "ABCD": print("  %s %5d  %.1f%%" % (k, c[k], 100.0*c[k]/n))

print(); print("="*70); print("2. GRAFO (dataset/nodos)"); print("="*70)
nodos={}
for f in os.listdir("dataset/nodos"):
    if f.endswith(".json"):
        d=json.load(open("dataset/nodos/"+f, encoding="utf-8"))
        nodos[d["node_id"]]=d
dep=[k for k,d in nodos.items() if d.get("deprecado")]
enl=sum(len(d.get("nodos_previos") or [])+len(d.get("nodos_siguientes") or []) for d in nodos.values())
claves=set()
for d in nodos.values(): claves|=set(d.keys())
print("disco=%d vivos=%d deprecados=%d enlaces=%d claves=%d" % (
    len(nodos), len(nodos)-len(dep), len(dep), enl, len(claves)))

print(); print("="*70); print("3. FAMILIAS al cierre (fuente contiene trozo, vivo; unica=sin barra)"); print("="*70)
for nombre,trozo in [("Weinberg","Traction"),("Horowitz","Hard Thing"),("Hugos","Hugos"),("Coleman","Coleman"),("Rackham","Rackham")]:
    fam=[d for d in nodos.values() if not d.get("deprecado") and trozo in (d.get("fuente") or "")]
    unica=[d for d in fam if "|" not in (d.get("fuente") or "")]
    print("  %-9s trozo=%-10r vivos=%3d unica=%3d" % (nombre,trozo,len(fam),len(unica)))

print(); print("="*70); print("4. OPERACIONES"); print("="*70)
ops=jl("docs/plan/OPERACIONES.jsonl"); ids=[o["id_op"] for o in ops]
rotas=[(o["id_op"],d) for o in ops for d in (o.get("depende_de") or [])+(o.get("bloquea_a") or []) if d not in set(ids)]
print("ops=%d ids_unicos=%d estados=%s rotas=%d" % (len(ops), len(set(ids)), dict(Counter(o["estado"] for o in ops)), len(rotas)))

print(); print("="*70); print("5. INVENTARIO"); print("="*70)
inv=jl("docs/plan/INVENTARIO.jsonl")
tipos=Counter(x.get("tipo") for x in inv)
print("entradas=%d  por tipo=%s" % (len(inv), dict(tipos)))

print(); print("="*70); print("6. INDICE ROJO DECLARADO"); print("="*70)
rojo=jl("docs/plan/INDICE_ROJO_DECLARADO.jsonl")
print("lineas=%d" % len(rojo))
for x in rojo: print("  %(id)s  %(operacion)s  %(fecha)s" % x)
nuevos13=set("""anillo_interior_explotar_el_canal_nucleo critica_del_plan_con_ia driver_de_inventario
escenarios_de_evolucion_de_la_ia estar_listo_para_ser_publica estrategia_circular_y_mecanismo_de_retorno
formalizar_un_proceso_ad_hoc ideacion_con_ia_en_la_sesion inteligencia_de_anuncios_de_la_competencia
la_historia_de_la_empresa producto_como_servicio_de_acceso puntos_brillantes_antes_del_pivote
seleccion_de_proveedores_por_costo_total""".split())
print("los 13 nuevos == ids del rojo (tras restar lineas previas)? ids_rojo=%d, nuevos_en_rojo=%d" % (
    len(rojo), len(nuevos13 & set(x["id"] for x in rojo))))
print("nuevos SIN linea en rojo:", sorted(nuevos13 - set(x["id"] for x in rojo)) or "ninguno")
