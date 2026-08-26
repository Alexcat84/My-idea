# CUENTA INDEPENDIENTE DE LAS DOS FUSIONES DEL LOTE D (auditor, vuelta 68).
# Contrato del plan sellado contra el arbol vivo y contra la apertura por
# git show 2bd639c7 (el commit de la TAREA 1, anterior a la fusion), sin
# reusar los verificadores del ejecutor. Molde: cuenta_fusion.py del acta 67.
import json, subprocess, glob

REPO = r"C:\Users\AlexDesk\Documents\I have an idea"
APERTURA = "2bd639c7"
PLAN = REPO + r"\docs\loop\PLAN_V68_OPU02_LOTE_D.json"

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

vivo = lambda i: json.load(open(REPO + rf"\dataset\nodos\{i}.json", encoding="utf-8"))

plan = json.load(open(PLAN, encoding="utf-8"))

# lo que el reporte publica, acto por acto
ESPERADO = {
    "division_trabajo_humano_ia": dict(
        pasos_ap=4, pasos_ci=7, cond_ap=2, cond_ci=5,
        piezas=17, APPEND=6, CUBIERTO=11, INCISO=0, perdidas=6),
    "comprension_capacidades_limitaciones_ia": dict(
        pasos_ap=5, pasos_ci=9, cond_ap=1, cond_ci=3,
        piezas=17, APPEND=6, CUBIERTO=9, INCISO=2, perdidas=5),
}
INCISO_ESPERADOS = {
    "comprension_capacidades_limitaciones_ia": [
        (2, "Prueba la IA en los casos l"),
        (5, "Ajusta la instrucci"),
    ]
}

todos_absorbidos = []
for a in plan["actos"]:
    surv_id = a["superviviente"]
    absorbidos = a["absorbidos"]
    todos_absorbidos += absorbidos
    e = ESPERADO[surv_id]
    surv = vivo(surv_id)
    surv_ap = show(f"dataset/nodos/{surv_id}.json")

    check(f"{surv_id} vivo", not surv.get("deprecado", False), "deprecado")
    check(f"{surv_id} pasos apertura {e['pasos_ap']}",
          len(surv_ap["pasos_accionables"]) == e["pasos_ap"], len(surv_ap["pasos_accionables"]))
    check(f"{surv_id} pasos cierre {e['pasos_ci']}",
          len(surv["pasos_accionables"]) == e["pasos_ci"], len(surv["pasos_accionables"]))
    check(f"{surv_id} cond apertura {e['cond_ap']}",
          len(surv_ap["condiciones_activacion"]) == e["cond_ap"], len(surv_ap["condiciones_activacion"]))
    check(f"{surv_id} cond cierre {e['cond_ci']}",
          len(surv["condiciones_activacion"]) == e["cond_ci"], len(surv["condiciones_activacion"]))

    # pasos viejos del superviviente conservados en orden (INCISO puede hacerlos crecer)
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
        check(f"{surv_id} paso viejo conservado: {pv[:40]}", hallado, "NO HALLADO en orden")

    CAMPOS = ["resumen_teorico", "pasos_accionables", "condiciones_activacion",
              "entregable_esperado"]
    for ab in absorbidos:
        n = vivo(ab)
        n_ap = show(f"dataset/nodos/{ab}.json")
        check(f"{ab} deprecado", n.get("deprecado") is True, n.get("deprecado"))
        for c in CAMPOS:
            check(f"{ab}.{c} INTACTO", n.get(c) == n_ap.get(c), "difiere de apertura")
        check(f"{ab} en merged_originals",
              ab in json.dumps(surv.get("merged_originals", [])), "ausente")

    piezas = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
    for bloque, campo in [("pasos", "pasos_accionables"), ("condiciones", "condiciones_activacion")]:
        rep = a[bloque]
        for ab in absorbidos:
            n_ap = show(f"dataset/nodos/{ab}.json")
            idx_reales = set(str(i + 1) for i in range(len(n_ap[campo])))
            idx_plan = set(rep.get(ab, {}).keys())
            check(f"{surv_id} cobertura {bloque} {ab}", idx_reales == idx_plan,
                  f"reales {sorted(idx_reales)} plan {sorted(idx_plan)}")
            for k, v in rep.get(ab, {}).items():
                clave = v.split(":")[0]
                piezas[clave] = piezas.get(clave, 0) + 1

    check(f"{surv_id} piezas {e['piezas']}", sum(piezas.values()) == e["piezas"], piezas)
    for cl in ("APPEND", "CUBIERTO", "INCISO"):
        check(f"{surv_id} {cl} {e[cl]}", piezas[cl] == e[cl], piezas)

    # APPEND verbatim
    for bloque, campo in [("pasos", "pasos_accionables"), ("condiciones", "condiciones_activacion")]:
        for ab in absorbidos:
            n_ap = show(f"dataset/nodos/{ab}.json")
            for k, v in a[bloque].get(ab, {}).items():
                if v.split(":")[0] == "APPEND":
                    texto = n_ap[campo][int(k) - 1]
                    check(f"APPEND verbatim {ab} {bloque} {k}",
                          texto in surv[campo], texto[:50])

    for pos, prefijo in INCISO_ESPERADOS.get(surv_id, []):
        check(f"{surv_id} INCISO en paso {pos}",
              prefijo in surv["pasos_accionables"][pos - 1],
              surv["pasos_accionables"][pos - 1][:70])

    check(f"{surv_id} cero pasos repetidos", len(set(nuevos)) == len(nuevos), "hay repetidos")
    cn = surv["condiciones_activacion"]
    check(f"{surv_id} cero condiciones repetidas", len(set(cn)) == len(cn), "hay repetidas")
    check(f"{surv_id} perdidas {e['perdidas']}", len(a["perdidas"]) == e["perdidas"], len(a["perdidas"]))

# grafo entero: 3237 vivos, 616 deprecados, cero referencias vivas a
# absorbidos, cero auto-aristas
vivos = dep = 0
refs_malas = []
autos = []
for f in glob.glob(REPO + r"\dataset\nodos\*.json"):
    n = json.load(open(f, encoding="utf-8"))
    if n.get("deprecado") is True:
        dep += 1
        continue
    vivos += 1
    nid = n["node_id"]
    for campo in ("nodos_previos", "nodos_siguientes"):
        for r in n.get(campo, []):
            if r in todos_absorbidos:
                refs_malas.append((nid, campo, r))
            if r == nid:
                autos.append((nid, campo))
check("vivos 3237", vivos == 3237, vivos)
check("deprecados 616", dep == 616, dep)
check("cero referencias vivas a absorbidos", not refs_malas, refs_malas[:5])
check("cero auto-aristas", not autos, autos[:5])
check("absorbidos 6", len(todos_absorbidos) == 6, todos_absorbidos)

# banco_rumbos sin rastro de ningun absorbido
rumbos = json.dumps(json.load(open(REPO + r"\scripts\rumbos\banco_rumbos.json", encoding="utf-8")), ensure_ascii=False)
for ab in todos_absorbidos:
    check(f"rumbos sin {ab}", ab not in rumbos, "aparece")

print(f"COMPROBACIONES OK: {ok}")
print(f"FALLOS: {len(fallos)}")
for f in fallos:
    print("  FALLO:", f)
