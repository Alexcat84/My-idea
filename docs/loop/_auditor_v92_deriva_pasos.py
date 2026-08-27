# -*- coding: utf-8 -*-
"""Vara PROPIA del auditor v92: DERIVA DE CONTENIDO. Las razones de OP-E-07 se
escribieron sobre el catalogo del encendido del bucle (50f03099). Mide cuantos
de los nodos de los 87 pares tienen HOY unos pasos_accionables distintos de los
que tenian entonces (las fusiones de la campana los movieron)."""
import io, json, os, subprocess
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "50f03099"
filas = [json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V92.jsonl"),encoding="utf-8") if l.strip()]
ids = sorted({f["madre"] for f in filas} | {f["hijo"] for f in filas})

def pasos_ref(nid):
    try:
        b = subprocess.run(["git","show","%s:dataset/nodos/%s.json" % (BASE, nid)],
                           capture_output=True, check=True).stdout.decode("utf-8")
        return json.loads(b).get("pasos_accionables")
    except Exception:
        return "NO_EXISTIA"

def pasos_hoy(nid):
    p = os.path.join(RAIZ,"dataset","nodos","%s.json" % nid)
    if not os.path.exists(p): return "NO_EXISTE"
    return json.load(io.open(p, encoding="utf-8")).get("pasos_accionables")

movidos = []
for nid in ids:
    a, b = pasos_ref(nid), pasos_hoy(nid)
    if a != b:
        movidos.append((nid, len(a) if isinstance(a,list) else a, len(b) if isinstance(b,list) else b))
print("nodos distintos en los 87 pares: %d" % len(ids))
print("nodos cuyos pasos_accionables CAMBIARON entre %s y hoy: %d" % (BASE, len(movidos)))
for nid, na, nb in movidos:
    print("   %-52s pasos %s -> %s" % (nid, na, nb))
afectados = [f["puesto"] for f in filas if f["madre"] in {m[0] for m in movidos} or f["hijo"] in {m[0] for m in movidos}]
print()
print("PARES de los 87 con al menos un lado movido: %d -> %s" % (len(afectados), sorted(afectados)))
