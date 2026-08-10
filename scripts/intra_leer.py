# -*- coding: utf-8 -*-
"""intra_leer.py DESDE HASTA [ancho] - imprime los pares intra-dominio para leer.

SOLO LECTURA. Herramienta del cribado intra-dominio: imprime cada par de la cola
con los pasos de sus dos nodos, su clave, si es de la banda 0,78 a 0,80, su
estado de procedencia y a que racimo pertenece cada nodo si pertenece a alguno.

Vive en scripts/ y no en un temporal a proposito: el cribado son 3388 pares y se
reanuda entre sesiones. La herramienta tiene que sobrevivir a la sesion.

Uso:
  python scripts/intra_leer.py 149 170
  python scripts/intra_leer.py 149 170 70
"""
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
D, H = int(sys.argv[1]), int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 95

G = json.loads(open("dataset/metadata/master_graph.json", encoding="utf-8").read())["nodos"]
P = [json.loads(l) for l in open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
P = {p["puesto_intra"]: p for p in P}
RAC = {}
for l in open("docs/RACIMOS_MIEMBROS.jsonl", encoding="utf-8"):
    if l.strip():
        r = json.loads(l)
        for m in r["miembros"]:
            RAC.setdefault(m["node_id"], []).append(r["racimo"])

def pasos(k):
    n = G.get(k)
    if not n:
        return ["*** NODO INEXISTENTE ***"]
    return [" ".join(str(s).split())[:W] for s in (n.get("pasos_accionables") or [])]

for i in range(D, H + 1):
    p = P.get(i)
    if not p:
        print("### %d NO EXISTE" % i); continue
    cl = max(p["sim_semantica"], p["sim_titulo"] / 100)
    print("=" * 116)
    print("#%d [%s] clave %.4f  sem %.4f  tit %.1f%s  %s" % (
        i, p["dominio"], cl, p["sim_semantica"], p["sim_titulo"],
        "  BANDA" if p["banda_078_080"] else "", p["estado"]))
    if p["procedencia_pareja"]:
        print("   PAREJA YA MARCADA: %s" % "; ".join(p["procedencia_pareja"]))
    for lado in ("a", "b"):
        k = p["nodo_" + lado]
        rr = RAC.get(k)
        print("  %s %s | %s" % (lado.upper(), k, p["titulo_" + lado]))
        if rr:
            print("     racimo: %s" % "; ".join(rr))
        # Las condiciones de activacion se imprimen SIEMPRE, y no es adorno: la
        # figura de marco-pais se decide ahi, no en los pasos. El 9 ago 2026 se
        # emitieron cinco veredictos falsos de pais cableado por leer solo los
        # pasos de la familia Magnuson-Moss, que condiciona por pais en su
        # condicion_activacion y no en sus pasos.
        cond = (G.get(k) or {}).get("condiciones_activacion") or []
        if cond:
            print("     condiciones: %s" % " | ".join(" ".join(str(c).split())[:70] for c in cond))
        for j, s in enumerate(pasos(k), 1):
            print("     %d. %s" % (j, s))
    print()
