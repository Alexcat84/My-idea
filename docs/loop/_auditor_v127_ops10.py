# -*- coding: utf-8 -*-
"""Verificacion PROPIA del auditor 127 sobre el tramo 3.d de OP-S-10:
que los diez tocados sean exactamente los diez primeros vivos alfabeticos
de la nomina que HOY no nombraban el pais en condiciones_activacion, y que
la condicion nueva vaya PRIMERA con las viejas intactas y en su orden."""
import json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ops = [json.loads(l) for l in open(os.path.join(RAIZ,"docs","plan","OPERACIONES.jsonl"), encoding="utf-8") if l.strip()]
op = [o for o in ops if o.get("id_op") == "OP-S-10"][0]
nomina = op["nodos"]
print("nomina OP-S-10: %d ids, unicos %d" % (len(nomina), len(set(nomina))))
def cargar(ref):
    if ref == "WORK":
        return json.load(open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"), encoding="utf-8"))["nodos"]
    r = subprocess.run(["git","show","%s:dataset/metadata/master_graph.json"%ref], cwd=RAIZ, capture_output=True)
    return json.loads(r.stdout.decode("utf-8"))["nodos"]
antes = cargar("7150339f"); hoy = cargar("WORK")
def nombra_pais(txt):
    t = (txt or "").lower()
    return "estados unidos" in t or "ee. uu" in t or "eeuu" in t or "ee.uu" in t
vivos = sorted([i for i in nomina if i in antes and not antes[i].get("deprecado")])
print("vivos en la nomina (estado 7150339f): %d" % len(vivos))
candidatos = [i for i in vivos if not any(nombra_pais(c) for c in (antes[i].get("condiciones_activacion") or []))]
print("candidatos (no nombran el pais en condiciones_activacion) : %d" % len(candidatos))
print("LOS DIEZ PRIMEROS QUE ME SALEN A MI:")
for i in candidatos[:10]: print("   %s" % i)
tocados = sorted(subprocess.run(["git","diff","--name-only","7150339f..HEAD","--","dataset/nodos/"],cwd=RAIZ,capture_output=True).stdout.decode().split())
tocados_ids = [os.path.basename(p)[:-5] for p in tocados if p.endswith(".json")]
print("NODOS TOCADOS EN dataset/nodos POR LA VUELTA: %d -> %s" % (len(tocados_ids), tocados_ids))
esperados = set(candidatos[:10])
reales = set(tocados_ids) - {"dia_cero_defectos_2","eliminacion_causas_error_4"}
print("COINCIDEN EXACTAMENTE: %s" % (esperados == reales))
print("sobran: %r | faltan: %r" % (sorted(reales-esperados), sorted(esperados-reales)))
print("--- CONDICIONES: antes / hoy ---")
for i in sorted(reales):
    a = antes[i].get("condiciones_activacion") or []
    h = hoy[i].get("condiciones_activacion") or []
    ok_prefijo = len(h) == len(a)+1 and h[1:] == a
    print("  %-52s viejas %d -> %d | primera nueva y viejas intactas y en orden: %s" % (i, len(a), len(h), ok_prefijo))
    print("      NUEVA: %s" % h[0])
