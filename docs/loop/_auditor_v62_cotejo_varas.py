# Relectura al doble, vuelta 62: coteja, para LOS 21 ACTOS, las cuentas de
# pasos y condiciones que el motivo sellado cita (pasos X contra Y,
# condiciones X contra Y) contra el arbol de APERTURA (d9fd6a54), y el
# superviviente sellado contra el grafo de HOY.
import io, json, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

raw = subprocess.run(["git", "show", "d9fd6a54:dataset/metadata/master_graph.json"],
                     capture_output=True).stdout
apertura = json.loads(raw.decode("utf-8"))["nodos"]
hoy = json.load(io.open(r"dataset\metadata\master_graph.json", encoding="utf-8"))["nodos"]

fallas = 0
total = 0
for L in ("A", "B"):
    p = json.load(io.open(r"docs\loop\PLAN_V62_OPU01_LOTE_%s.json" % L, encoding="utf-8"))
    for a in p["actos"]:
        total += 1
        sup = a["superviviente"]
        muerto = [m for m in a["miembros_del_acto_entero"] if m != sup][0]
        n_sup, n_mue = apertura[sup], apertura[muerto]
        ps, pm = len(n_sup["pasos_accionables"]), len(n_mue["pasos_accionables"])
        cs, cm = len(n_sup["condiciones_activacion"]), len(n_mue["condiciones_activacion"])
        motivo = a["motivo"]
        problemas = []
        # cada "pasos X contra Y" del motivo tiene que casar con {ps,pm} como conjunto
        for m in re.finditer(r"pasos (\d+) contra (\d+)", motivo):
            x, y = int(m.group(1)), int(m.group(2))
            if {x, y} != {ps, pm} and not (x == y == ps == pm):
                problemas.append("pasos %d contra %d citados, medidos %d (sup) y %d (muerto)" % (x, y, ps, pm))
        for m in re.finditer(r"condiciones (\d+) contra (\d+)", motivo):
            x, y = int(m.group(1)), int(m.group(2))
            if {x, y} != {cs, cm} and not (x == y == cs == cm):
                problemas.append("condiciones %d contra %d citadas, medidas %d (sup) y %d (muerto)" % (x, y, cs, cm))
        # el superviviente sellado vive HOY y el muerto resuelve a el
        if hoy[sup].get("deprecado", False):
            problemas.append("el superviviente %s esta deprecado HOY" % sup)
        if not hoy[muerto].get("deprecado", False):
            problemas.append("el absorbido %s sigue vivo HOY" % muerto)
        if muerto not in hoy[sup].get("ids_alias", []):
            problemas.append("el absorbido %s no esta en ids_alias del superviviente" % muerto)
        estado = "OK" if not problemas else "FALLA"
        if problemas:
            fallas += 1
        print("%s acto %2d  %-6s sup=%s  pasos %d/%d cond %d/%d" % (L, a["orden"], estado, sup, ps, pm, cs, cm))
        for x in problemas:
            print("        !! " + x)

print()
print("actos cotejados: %d | con falla: %d" % (total, fallas))
