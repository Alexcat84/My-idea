# -*- coding: utf-8 -*-
# Relectura ciega del auditor, vuelta 63: imprime los pasos y condiciones
# de los nodos de las dos fusiones DESDE EL ARBOL DE APERTURA (630c6d19),
# sin abrir los planes sellados.
import json, subprocess, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HASH = "630c6d19"

def nodo(nid):
    raw = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (HASH, nid)],
                         capture_output=True, check=True).stdout
    return json.loads(raw.decode("utf-8-sig"))

for nid in ["pivotar_o_perseverar", "decision_pivote_perseverar",
            "puntos_brillantes_antes_del_pivote",
            "ocho_fases_experiencia_cliente", "fases_de_retencion_de_clientes"]:
    d = nodo(nid)
    print("########## %s (APERTURA %s) ##########" % (nid, HASH))
    print("TITULO:", d.get("titulo_concepto"))
    print("FUENTE:", d.get("fuente"))
    pasos = d.get("pasos_accionables") or []
    print("PASOS (%d):" % len(pasos))
    for i, p in enumerate(pasos, 1):
        print("  %d. %s" % (i, p))
    conds = d.get("condiciones_activacion") or []
    print("CONDICIONES (%d):" % len(conds))
    for i, c in enumerate(conds, 1):
        print("  %d. %s" % (i, c))
    print("PREVIOS:", d.get("nodos_previos"))
    print("SIGUIENTES:", d.get("nodos_siguientes"))
    print()
