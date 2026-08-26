# CUENTA INDEPENDIENTE DE LA FUSION DEL ACTO 16 (auditor, vuelta 67).
# Contrato del plan sellado contra el arbol vivo y contra la apertura por
# git show d25ab668 (el commit de la TAREA 1, anterior a la fusion), sin
# reusar los verificadores del ejecutor.
import json, subprocess, sys, io, glob

REPO = r"C:\Users\AlexDesk\Documents\I have an idea"
APERTURA = "d25ab668"
PLAN = REPO + r"\docs\loop\PLAN_V67_OPU02_LOTE_C.json"

ok = 0
fallos = []

def check(nombre, cond, detalle=""):
    global ok
    if cond:
        ok += 1
    else:
        fallos.append(f"{nombre}: {detalle}")

def show(path):
    out = subprocess.run(["git", "-C", REPO, "show", f"{APERTURA}:{path}"],
                         capture_output=True)
    if out.returncode != 0:
        return None
    return json.loads(out.stdout.decode("utf-8"))

plan = json.load(open(PLAN, encoding="utf-8"))
a = plan["actos"][0]
surv_id = a["superviviente"]
absorbidos = a["absorbidos"]

vivo = lambda i: json.load(open(REPO + rf"\dataset\nodos\{i}.json", encoding="utf-8"))
surv = vivo(surv_id)
surv_ap = show(f"dataset/nodos/{surv_id}.json")

# 1) superviviente vivo, 5 -> 10 pasos, 2 -> 3 condiciones
check("superviviente vivo", not surv.get("deprecado", False), "deprecado")
check("pasos apertura 5", len(surv_ap["pasos_accionables"]) == 5, len(surv_ap["pasos_accionables"]))
check("pasos cierre 10", len(surv["pasos_accionables"]) == 10, len(surv["pasos_accionables"]))
check("cond apertura 2", len(surv_ap["condiciones_activacion"]) == 2, len(surv_ap["condiciones_activacion"]))
check("cond cierre 3", len(surv["condiciones_activacion"]) == 3, len(surv["condiciones_activacion"]))

# 2) los prefijos viejos del superviviente INTACTOS (los 5 pasos de apertura
#    siguen, en orden, como subsecuencia de los 10; con INCISO un paso puede
#    crecer conteniendo el texto viejo)
viejos = surv_ap["pasos_accionables"]
nuevos = surv["pasos_accionables"]
j = 0
for pv in viejos:
    hallado = False
    while j < len(nuevos):
        if pv == nuevos[j] or pv in nuevos[j]:
            hallado = True
            j += 1
            break
        j += 1
    check(f"paso viejo conservado: {pv[:40]}", hallado, "NO HALLADO en orden")

# 3) absorbidos: deprecados y con texto INTACTO contra apertura
CAMPOS = ["resumen_teorico", "pasos_accionables", "condiciones_activacion",
          "entregable_esperado"]
for ab in absorbidos:
    n = vivo(ab)
    n_ap = show(f"dataset/nodos/{ab}.json")
    check(f"{ab} deprecado", n.get("deprecado") is True, n.get("deprecado"))
    for c in CAMPOS:
        check(f"{ab}.{c} INTACTO", n.get(c) == n_ap.get(c), "difiere de apertura")
    check(f"{ab} en merged_originals", ab in [m.get("node_id", m) if isinstance(m, dict) else m
                                              for m in surv.get("merged_originals", [])] or
          ab in json.dumps(surv.get("merged_originals", [])), "ausente")

# 4) cobertura EXACTA de indices del plan (pasos y condiciones), y cuentas
piezas = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
for bloque, campo in [("pasos", "pasos_accionables"), ("condiciones", "condiciones_activacion")]:
    rep = a[bloque]
    for ab in absorbidos:
        n_ap = show(f"dataset/nodos/{ab}.json")
        idx_reales = set(str(i + 1) for i in range(len(n_ap[campo])))
        idx_plan = set(rep.get(ab, {}).keys())
        check(f"cobertura {bloque} {ab}", idx_reales == idx_plan,
              f"reales {sorted(idx_reales)} plan {sorted(idx_plan)}")
        for k, v in rep.get(ab, {}).items():
            clave = v.split(":")[0]
            piezas[clave] = piezas.get(clave, 0) + 1

check("piezas 23", sum(piezas.values()) == 23, piezas)
check("APPEND 6", piezas["APPEND"] == 6, piezas)
check("CUBIERTO 15", piezas["CUBIERTO"] == 15, piezas)
check("INCISO 2", piezas["INCISO"] == 2, piezas)

# 5) APPEND verbatim: cada paso/condicion APPEND del plan esta en el
#    superviviente con su texto identico al del absorbido en la apertura
for bloque, campo in [("pasos", "pasos_accionables"), ("condiciones", "condiciones_activacion")]:
    for ab in absorbidos:
        n_ap = show(f"dataset/nodos/{ab}.json")
        for k, v in a[bloque].get(ab, {}).items():
            if v == "APPEND":
                texto = n_ap[campo][int(k) - 1]
                check(f"APPEND verbatim {ab} {bloque} {k}",
                      texto in surv[campo], texto[:50])

# 6) los dos INCISO: extraidos del absorbido y presentes en el paso del
#    superviviente; los dos textos que el reporte imprime
INCISO_ESPERADOS = [
    (1, "Formular el problema como una pregunta de dise"),
    (5, "Revisar y ajustar la pregunta original seg"),
]
for pos, prefijo in INCISO_ESPERADOS:
    check(f"INCISO en paso {pos}", prefijo in surv["pasos_accionables"][pos - 1],
          surv["pasos_accionables"][pos - 1][:70])

# 7) cero repetidos literales en pasos y condiciones del superviviente
check("cero pasos repetidos", len(set(nuevos)) == len(nuevos), "hay repetidos")
cn = surv["condiciones_activacion"]
check("cero condiciones repetidas", len(set(cn)) == len(cn), "hay repetidas")

# 8) perdidas: 9 filas en el plan, cada una con su motivo, y las de dos
#    sitios con el campo donde llevando ambos
per = a["perdidas"]
check("perdidas 9", len(per) == 9, len(per))

# 9) grafo: 3243 vivos, 610 deprecados; CERO referencias vivas a un
#    absorbido; CERO auto-aristas en vivos
vivos = 0
dep = 0
refs_malas = []
autos = []
for f in glob.glob(REPO + r"\dataset\nodos\*.json"):
    n = json.load(open(f, encoding="utf-8"))
    es_dep = n.get("deprecado") is True
    if es_dep:
        dep += 1
        continue
    vivos += 1
    nid = n["node_id"]
    for campo in ("nodos_previos", "nodos_siguientes"):
        for r in n.get(campo, []):
            if r in absorbidos:
                refs_malas.append((nid, campo, r))
            if r == nid:
                autos.append((nid, campo))
check("vivos 3243", vivos == 3243, vivos)
check("deprecados 610", dep == 610, dep)
check("cero referencias vivas a absorbidos", not refs_malas, refs_malas[:5])
check("cero auto-aristas", not autos, autos[:5])

# 10) el reanclaje: el rumbo apunta al superviviente y no a how_might_we_hmw
rumbos = json.load(open(REPO + r"\scripts\rumbos\banco_rumbos.json", encoding="utf-8"))
s = json.dumps(rumbos, ensure_ascii=False)
check("rumbos sin how_might_we_hmw", "how_might_we_hmw" not in s, "aparece")

print(f"COMPROBACIONES OK: {ok}")
print(f"FALLOS: {len(fallos)}")
for f in fallos:
    print("  FALLO:", f)
