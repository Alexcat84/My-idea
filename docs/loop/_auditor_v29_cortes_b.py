# -*- coding: utf-8 -*-
"""AUDITOR v29, segundo cotejo: donantes con union de cortes por plan."""
import json, subprocess
def show(commit, node_id):
    r = subprocess.run(["git","show","%s:dataset/nodos/%s.json"%(commit,node_id)],capture_output=True)
    return json.loads(r.stdout.decode("utf-8")) if r.returncode==0 else None
PLANES = [
    ("docs/loop/PLAN_V27_OPF02.json","f4ad6d45","2d96e3d3","cortes"),
    ("docs/loop/PLAN_V29_OPF03_PROPIOS.json","7521f039","9d4a8eb1","cortes"),
    ("docs/loop/PLAN_V29_OPF04_WEI.json","9d4a8eb1","1eef1c6b","cortes"),
    ("docs/loop/PLAN_V29_OPF04_HOR.json","1eef1c6b","2bd8dd76","cortes"),
]
for ruta, antes, despues, clave in PLANES:
    plan=json.load(open(ruta,encoding="utf-8"))
    pordon={}
    for c in plan[clave]:
        pordon.setdefault(c.get("origen") or c.get("desde"), set()).update(c["pasos_que_salen"])
    for don, idx in sorted(pordon.items()):
        a=show(antes,don); d=show(despues,don)
        esperado=[p for i,p in enumerate(a["pasos_accionables"],1) if i not in idx]
        ok = d["pasos_accionables"]==esperado
        print("[%s] %-46s %s: quedan %d de %d" % ("OK " if ok else "FALLO", don, ruta.split('/')[-1][:22], len(d["pasos_accionables"]), len(a["pasos_accionables"])))
        if not ok:
            print("   esperado:", [p[:40] for p in esperado])
            print("   arbol   :", [p[:40] for p in d["pasos_accionables"]])
