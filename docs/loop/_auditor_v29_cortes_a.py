# -*- coding: utf-8 -*-
"""AUDITOR v29: cotejo textual de TODOS los cortes de la vuelta contra el diff real."""
import json, subprocess, sys
def show(commit, node_id):
    r = subprocess.run(["git","show","%s:dataset/nodos/%s.json"%(commit,node_id)],
                       capture_output=True)
    if r.returncode != 0: return None
    return json.loads(r.stdout.decode("utf-8"))
PLANES = [
    ("docs/loop/PLAN_V27_OPF02.json",      "f4ad6d45","2d96e3d3","cortes"),
    ("docs/loop/PLAN_V29_RELECTURA_D1.json","2d96e3d3","7521f039","mudanzas"),
    ("docs/loop/PLAN_V29_OPF03_PROPIOS.json","7521f039","9d4a8eb1","cortes"),
    ("docs/loop/PLAN_V29_OPF04_WEI.json",  "9d4a8eb1","1eef1c6b","cortes"),
    ("docs/loop/PLAN_V29_OPF04_HOR.json",  "1eef1c6b","2bd8dd76","cortes"),
]
tot=0; fallos=0; creados={}
for ruta, antes, despues, clave in PLANES:
    plan=json.load(open(ruta,encoding="utf-8"))
    print("== %s  (%s -> %s)" % (ruta.split("/")[-1], antes, despues))
    for c in plan[clave]:
        tot+=1
        origen = c.get("origen") or c.get("desde")
        idx = c["pasos_que_salen"]
        d_antes = show(antes, origen); d_desp = show(despues, origen)
        errs=[]
        pasos_antes = d_antes["pasos_accionables"]
        if len(pasos_antes) != c["pasos_totales"]:
            errs.append("pasos_totales plan=%d medido=%d" % (c["pasos_totales"], len(pasos_antes)))
        bloque = [pasos_antes[i-1] for i in idx]
        texto = c.get("pasos_que_salen_texto")
        if texto is not None and bloque != texto:
            errs.append("bloque del arbol != texto del plan")
        # prefijos (relectura no trae texto entero)
        for pref, paso in zip(c.get("prefijos") or [], bloque):
            if not paso.startswith(pref[:30]):
                errs.append("prefijo no calza: %r" % pref[:40])
        # donante despues: perdio exactamente esos pasos, resto intacto y en orden
        esperado = [p for i,p in enumerate(pasos_antes,1) if i not in set(idx)]
        if d_desp["pasos_accionables"] != esperado:
            errs.append("donante despues NO es el resto intacto")
        fq = c.get("fuente_queda")
        if fq and d_desp.get("fuente") != fq:
            errs.append("fuente_queda: plan=%r arbol=%r" % (fq, d_desp.get("fuente")))
        # receptor
        dest=c["destino"]
        if dest["tipo"]=="miembro":
            rid = dest.get("nodo") or dest.get("id")
            r_desp = show(despues, rid); r_antes = show(antes, rid)
            if r_desp is None: errs.append("miembro %s no existe despues" % rid)
            else:
                if r_antes is not None:
                    ganados = [p for p in r_desp["pasos_accionables"] if p not in r_antes["pasos_accionables"]]
                else:
                    ganados = r_desp["pasos_accionables"]  # nodo propio nacido en este mismo plan
                falta = [p for p in bloque if p not in r_desp["pasos_accionables"]]
                if falta: errs.append("receptor %s NO contiene %d pasos del bloque" % (rid, len(falta)))
        else:
            nid = dest["nuevo"]["node_id"]
            r_desp = show(despues, nid)
            if r_desp is None: errs.append("nodo propio %s NO existe" % nid)
            else:
                falta=[p for p in bloque if p not in r_desp["pasos_accionables"]]
                if falta: errs.append("nodo propio %s no contiene %d pasos" % (nid, len(falta)))
                if show(antes, nid) is None: creados.setdefault(nid, []).append(origen)
                if r_desp.get("fuente") != dest["nuevo"].get("fuente"):
                    errs.append("fuente del nuevo != plan")
        est = "OK " if not errs else "FALLO"
        if errs: fallos+=1
        print("  [%s] %-42s [%s..%s] -> %s" % (est, origen, min(idx), max(idx),
              (dest.get("nodo") or dest.get("id") or dest.get("nuevo",{}).get("node_id"))))
        for e in errs: print("        !! %s" % e)
print()
print("TOTAL cortes cotejados: %d   FALLOS: %d" % (tot, fallos))
print("nodos propios nacidos en planes: %d -> %s" % (len(creados), sorted(creados)))
