"""Auditor vuelta 30: medicion propia, codigo independiente del ejecutor.

Todo se mide HOY contra el arbol en HEAD y contra 4e0a87ea (apertura) via
git show. Ninguna cifra se copia del reporte ni del acta: las del reporte
van como contraste al final de cada bloque.
"""
import json
import subprocess
import sys
from collections import Counter

RAIZ = "."


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8").stdout


def git_json(ref, ruta):
    out = subprocess.run(["git", "show", "%s:%s" % (ref, ruta)],
                         capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)


def leer_jsonl(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def nodo(nid, ref=None):
    ruta = "dataset/nodos/%s.json" % nid
    if ref:
        return git_json(ref, ruta)
    return json.load(open(ruta, encoding="utf-8"))


APERTURA = "4e0a87ea"

print("=" * 74)
print("A) MARCADOR, recomputo propio")
v = leer_jsonl("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
p = sorted(x["puesto_intra"] for x in v)
c = Counter(x["clase"] for x in v)
print("n=%d A=%d B=%d C=%d D=%d fuera=%s" % (
    len(v), c["A"], c["B"], c["C"], c["D"], sorted(set(c) - set("ABCD")) or 0))
print("rango %d..%d huecos=%d dup=%d" % (
    p[0], p[-1], len(set(range(p[0], p[-1] + 1)) - set(p)),
    len([k for k, n in Counter(p).items() if n > 1])))

print()
print("B) GRAFO, recomputo propio")
import os
ficheros = [f for f in os.listdir("dataset/nodos") if f.endswith(".json")]
nodos = {}
for f in ficheros:
    d = json.load(open("dataset/nodos/" + f, encoding="utf-8"))
    nodos[d["node_id"]] = d
vivos = [d for d in nodos.values() if not d.get("deprecado") and not d.get("deprecated")]
enl = sum(len(d.get("nodos_previos") or []) + len(d.get("nodos_siguientes") or [])
          for d in nodos.values())
claves = set()
for d in nodos.values():
    claves |= set(d)
print("ficheros=%d ids=%d vivos=%d deprecados=%d enlaces=%d claves=%d" % (
    len(ficheros), len(nodos), len(vivos), len(nodos) - len(vivos), enl, len(claves)))

print()
print("C) APERTURA contra CIERRE de los cinco nodos tocados, git show %s" % APERTURA)
for nid in ["coeficiente_viral", "viral_loop_marketing", "decision_de_vender_startup",
            "experiencias_exclusivas_vip", "comunidad_tribu_marca"]:
    a = nodo(nid, APERTURA)
    z = nodos[nid]
    print("  %-32s %2d -> %2d  fuente igual: %s" % (
        nid, len(a["pasos_accionables"]), len(z["pasos_accionables"]),
        a.get("fuente") == z.get("fuente")))

print()
print("D) LOS TRES PLANES: cobertura 1..N exacta, fuente, verbatim, salidas")
for pf, nid in [("PLAN_V30_P19_COEFICIENTE.json", "coeficiente_viral"),
                ("PLAN_V30_P19_VENDER.json", "decision_de_vender_startup"),
                ("PLAN_V30_P20_VIRAL_LOOP.json", "viral_loop_marketing")]:
    plan = json.load(open("docs/loop/" + pf, encoding="utf-8"))["nodos"][0]
    N = plan["pasos_totales"]
    a = nodo(nid, APERTURA)
    z = nodos[nid]
    ok_n = len(a["pasos_accionables"]) == N
    origenes = []
    for dest, orig in plan["mapa_destejido"].items():
        origenes += orig
    salidas = plan.get("salidas") or []
    for s in salidas:
        origenes += s["pasos_que_salen"]
    cobertura = sorted(origenes) == list(range(1, N + 1))
    ok_final = len(z["pasos_accionables"]) == len(plan["pasos_finales"])
    ok_texto_final = z["pasos_accionables"] == plan["pasos_finales"]
    ok_fuente = z.get("fuente") == plan["fuente_queda"] == plan["fuente_esperada"]
    # verbatim: destino de UN solo origen debe ser el texto original
    verb_total = verb_ok = 0
    for dest, orig in plan["mapa_destejido"].items():
        if len(orig) == 1:
            verb_total += 1
            if plan["pasos_finales"][int(dest) - 1] == a["pasos_accionables"][orig[0] - 1]:
                verb_ok += 1
    # pasos originales del plan contra la apertura real
    ok_orig = plan["pasos_originales"] == a["pasos_accionables"]
    print("  %-28s N=%2d ok_N=%s cobertura_1aN=%s finales=%d ok_finales=%s" % (
        nid, N, ok_n, cobertura, len(plan["pasos_finales"]), ok_final))
    print("    texto_final_en_arbol=%s fuente_intacta=%s originales_calzan=%s verbatim=%d/%d salidas=%d" % (
        ok_texto_final, ok_fuente, ok_orig, verb_ok, verb_total, len(salidas)))
    for s in salidas:
        did = s["destino"]["nodo"]
        dest = nodos[did]
        for pnum in s["pasos_que_salen"]:
            texto = a["pasos_accionables"][pnum - 1]
            print("    salida paso %d -> %s : TEXTUAL en destino=%s (destino %d pasos)" % (
                pnum, did, texto in dest["pasos_accionables"],
                len(dest["pasos_accionables"])))

print()
print("E) SALDO OP-F-04-WEI y HOR, nomina por campo fuente")
ops = {o["id_op"]: o for o in leer_jsonl("docs/plan/OPERACIONES.jsonl")}
for opid, trozo in [("OP-F-04-WEI", "Traction"), ("OP-F-04-HOR", "Hard Thing")]:
    res = fund = pend = 0
    detalle = []
    for nid in ops[opid]["nodos"]:
        d = nodos.get(nid)
        if d is None or d.get("deprecado") or d.get("deprecated"):
            detalle.append((nid, "AUSENTE/DEP"))
            pend += 1
            continue
        if trozo.lower() in (d.get("fuente") or "").lower():
            fund += 1
            detalle.append((nid, "FUNDIDO (declara %s)" % trozo))
        else:
            res += 1
    print("  %s nomina=%d resueltos=%d fundidos=%d pendientes=%d" % (
        opid, len(ops[opid]["nodos"]), res, fund, pend))
    for nid, e in detalle:
        print("     %s %s" % (nid, e))

print()
print("F) OP-F-01, los seis LARGO LEGITIMO")
for nid in ops["OP-F-01"]["nodos"]:
    print("  %-44s %d pasos" % (nid, len(nodos[nid]["pasos_accionables"])))

print()
print("G) la cifra cazada: seleccion_de_proveedores_por_costo_total")
print("  pasos =", len(nodos["seleccion_de_proveedores_por_costo_total"]["pasos_accionables"]))

print()
print("H) NOTAS de operaciones: el texto viejo entero sigue delante")
texto_viejo = sh("git", "show", "%s:docs/plan/OPERACIONES.jsonl" % APERTURA)
viejas = {json.loads(l)["id_op"]: json.loads(l) for l in texto_viejo.splitlines() if l.strip()}
for opid in ["OP-F-02", "OP-F-03", "OP-F-04-WEI", "OP-F-04-HOR", "OP-F-04-COL"]:
    va = viejas[opid].get("nota") or ""
    vn = ops[opid].get("nota") or ""
    print("  %-12s vieja_entera_presente=%s crecio=%d" % (
        opid, va in vn, len(vn) - len(va)))

print()
print("I) INDICE ROJO contra apertura")
rojo_v = sh("git", "show", "%s:docs/plan/INDICE_ROJO_DECLARADO.jsonl" % APERTURA)
rojo_h = open("docs/plan/INDICE_ROJO_DECLARADO.jsonl", encoding="utf-8").read()
print("  lineas apertura=%d hoy=%d identico=%s" % (
    len(rojo_v.splitlines()), len(rojo_h.splitlines()), rojo_v == rojo_h))

print()
print("J) PROCEDENCIA multifuente declarada en los planes")
for pf in ["PLAN_V30_P19_COEFICIENTE.json", "PLAN_V30_P19_VENDER.json",
           "PLAN_V30_P20_VIRAL_LOOP.json"]:
    plan = json.load(open("docs/loop/" + pf, encoding="utf-8"))["nodos"][0]
    proc = plan.get("procedencia") or []
    print("  %-34s bloques de procedencia=%d" % (plan["nodo"], len(proc)))
    for b in proc:
        print("     %-40s pasos %s" % (b["libro"], b["pasos_del_resultado"]))
print()
print("FIN DE LA MEDICION PROPIA")
