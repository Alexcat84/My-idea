# -*- coding: utf-8 -*-
# Cuenta independiente del auditor, vuelta 64: la fusion OP-M-03-II contra el
# grafo de HOY y contra el arbol de APERTURA (f0f8605b), el cableado por las
# dos varas, el D10 sellado, las cinco consumidas en OPERACIONES.jsonl y el
# tramo unico de OP-U-02, sin reusar los verificadores del ejecutor.
import json, io, sys, os, subprocess, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
NODOS = "dataset/nodos"
APERTURA = "f0f8605b"

def cargar(nid):
    for raiz, _dirs, fs in os.walk(NODOS):
        if nid + ".json" in fs:
            return json.load(open(os.path.join(raiz, nid + ".json"), encoding="utf-8"))
    raise SystemExit("NO ENCONTRADO: " + nid)

def cargar_apertura(nid):
    out = subprocess.run(["git", "show", f"{APERTURA}:dataset/nodos/{nid}.json"],
                         capture_output=True)
    return json.loads(out.stdout.decode("utf-8"))

fallos = []
total = [0]
def check(nombre, cond, detalle=""):
    total[0] += 1
    print(("OK   " if cond else "FALLO") + " | " + nombre + (" | " + detalle if detalle else ""))
    if not cond:
        fallos.append(nombre)

def vivo(d):
    return not (d.get("deprecado") or d.get("deprecated") or d.get("estado") == "deprecado")

print("=== OP-M-03-II: EL ESTADO FINAL CONTRA EL PLAN ===")
sup = cargar("pivote_o_proceder")
mue = cargar("pivotar_o_proceder")
sup_a = cargar_apertura("pivote_o_proceder")
mue_a = cargar_apertura("pivotar_o_proceder")
ps, pm = sup["pasos_accionables"], mue["pasos_accionables"]
ps_a, pm_a = sup_a["pasos_accionables"], mue_a["pasos_accionables"]
cs, cm = sup["condiciones_activacion"], mue["condiciones_activacion"]
cs_a, cm_a = sup_a["condiciones_activacion"], mue_a["condiciones_activacion"]

check("superviviente vivo", vivo(sup))
check("absorbido deprecado", not vivo(mue))
check("superviviente 9 pasos", len(ps) == 9, "mide %d" % len(ps))
check("superviviente 2 condiciones", len(cs) == 2, "mide %d" % len(cs))
check("pasos 1-6 del superviviente intactos", ps[:6] == ps_a[:6])
check("paso 7 = viejo mas el INCISO verbatim del paso 4 del muerto",
      ps[6] == ps_a[6] + " hacia la validación con clientes" and
      "hacia la validación con clientes" in pm_a[3])
check("paso 8 = paso 2 del muerto VERBATIM (evidencia real, no opiniones)", ps[7] == pm_a[1])
check("paso 9 = paso 3 del muerto VERBATIM (amor total a indiferencia)", ps[8] == pm_a[2])
check("condicion 1 del superviviente intacta", cs[0] == cs_a[0])
check("condicion 2 = condicion 2 del muerto VERBATIM", cs[1] == cm_a[1])
check("absorbido con sus 5 pasos INTACTOS al byte", pm == pm_a and len(pm) == 5)
check("absorbido con sus 2 condiciones INTACTAS", cm == cm_a and len(cm) == 2)
mo = sup.get("merged_originals") or []
mo_ids = [x.get("node_id") if isinstance(x, dict) else x for x in mo]
alias = (sup.get("ids_alias") or []) + mo_ids
check("alias/merged_originals carga al muerto", "pivotar_o_proceder" in alias,
      "merged_originals forma: " + ("dicts" if mo and isinstance(mo[0], dict) else "cadenas"))
enl_sup = (sup.get("nodos_previos") or []) + (sup.get("nodos_siguientes") or [])
check("superviviente sin auto-arista", "pivote_o_proceder" not in enl_sup and
      "pivotar_o_proceder" not in enl_sup)

print()
print("=== EL CABLEADO POR LAS DOS VARAS, SOBRE EL ARBOL DE APERTURA ===")
salida = subprocess.run(["git", "ls-tree", "-r", "--name-only", APERTURA],
                        capture_output=True).stdout.decode()
rutas = [l for l in salida.splitlines() if l.startswith("dataset/nodos/") and l.endswith(".json")]
inst = {"pivotar_o_proceder": 0, "pivote_o_proceder": 0}
cruda = {"pivotar_o_proceder": 0, "pivote_o_proceder": 0}
for r in rutas:
    nid = r.split("/")[-1][:-5]
    if nid in inst:
        continue
    raw = subprocess.run(["git", "show", f"{APERTURA}:{r}"], capture_output=True).stdout.decode("utf-8")
    d = json.loads(raw)
    enl = (d.get("nodos_previos") or []) + (d.get("nodos_siguientes") or [])
    for k in inst:
        if vivo(d):
            inst[k] += enl.count(k)
        if '"%s"' % k in raw:
            cruda[k] += 1
check("vara del instrumento: 10 contra 5",
      inst["pivotar_o_proceder"] == 10 and inst["pivote_o_proceder"] == 5,
      "mide %d contra %d" % (inst["pivotar_o_proceder"], inst["pivote_o_proceder"]))
check("vara cruda declarada: 12 contra 6",
      cruda["pivotar_o_proceder"] == 12 and cruda["pivote_o_proceder"] == 6,
      "mide %d contra %d" % (cruda["pivotar_o_proceder"], cruda["pivote_o_proceder"]))

print()
print("=== LAS DIEZ REDIRECCIONES Y LOS DOS TESTIGOS DE P.16, EN EL GRAFO DE HOY ===")
diez = ["categorias_entusiasmo_cliente", "checkpoints_validacion",
        "decision_pivotar_o_proceder", "filosofia_validacion_clientes",
        "mapa_flujo_trabajo_cliente", "presentacion_solucion_producto",
        "product_market_fit", "scorecard_descubrimiento_cliente",
        "validar_posicionamiento_con_analistas", "verificar_modelo_ingresos"]
mal = []
for nid in diez:
    d = cargar(nid)
    enl = (d.get("nodos_previos") or []) + (d.get("nodos_siguientes") or [])
    if "pivotar_o_proceder" in enl or "pivote_o_proceder" not in enl:
        mal.append(nid)
check("las 10 nombran al superviviente y ninguna al muerto", not mal, str(mal))
pres = cargar("presentacion_solucion_producto")
scor = cargar("scorecard_descubrimiento_cliente")
check("P.16 limpio: presentacion_solucion_producto.previos UNA sola vez",
      (pres.get("nodos_previos") or []).count("pivote_o_proceder") == 1)
check("P.16 limpio: scorecard.siguientes UNA sola vez",
      (scor.get("nodos_siguientes") or []).count("pivote_o_proceder") == 1)

print()
print("=== EL D10 SELLADO EN PLAN_V63_OPM02PROG.json ===")
plan63 = json.load(open("docs/loop/PLAN_V63_OPM02PROG.json", encoding="utf-8"))
perd63 = plan63["actos"][0].get("perdidas") or []
d10 = [p for p in perd63 if p.get("especie") == "DE CONDICIONES" and
       "fases_de_retencion_de_clientes" in p.get("donde", "")]
check("la perdida DE CONDICIONES del D10 existe en el plan 63", len(d10) == 1)
raw63 = json.dumps(plan63, ensure_ascii=False)
check("el texto viejo citado sigue dentro (correccion declarada, no tachadura)",
      "atraer y cerrar ventas" in raw63)

print()
print("=== LAS CINCO CONSUMIDAS EN OPERACIONES.jsonl ===")
ops = [json.loads(l) for l in open("docs/plan/OPERACIONES.jsonl", encoding="utf-8")
       if l.strip()]
check("71 fichas", len(ops) == 71, "mide %d" % len(ops))
claves = set()
for o in ops:
    claves |= set(o.keys())
check("las 18 claves y ninguna nueva", len(claves) == 18, "mide %d: %s" % (len(claves), sorted(claves)))
consum = {"OP-M-02-MEDIOS": ("TRAMO 3", "2091"), "OP-M-02-ASSESS": ("TRAMO 2", "1832"),
          "OP-M-02-ADMIT": ("TRAMO 2", "1840"), "OP-M-02-ACTIVATE": ("TRAMO 1", "417"),
          "OP-M-02-ACCOMPLISH": ("TRAMO 3", "2069")}
for oid, (tramo, linea) in consum.items():
    ficha = next(o for o in ops if o["id_op"] == oid)
    nota = ficha.get("nota", "")
    check("nota de consumida en %s cita %s y linea %s" % (oid, tramo, linea),
          "CONSUMIDA" in nota.upper() and tramo in nota and linea in nota)
divs = [oid for oid in ("OP-M-02-MEDIOS", "OP-M-02-ADMIT")
        if "contraste" not in next(o for o in ops if o["id_op"] == oid).get("nota", "").lower()]
check("MEDIOS y ADMIT declaran la divergencia como contraste", not divs, str(divs))

print()
print("=== EL TRAMO UNICO DE OP-U-02 CONTRA MI RECOMPUTO ===")
filas = [json.loads(l) for l in open("docs/loop/TRAMO_UNICO_OPU02_V64.jsonl", encoding="utf-8")
         if l.strip()]
check("47 filas", len(filas) == 47, "mide %d" % len(filas))
nodos_tramo = sum(len(f.get("miembros") or []) for f in filas)
check("201 nodos", nodos_tramo == 201, "mide %d" % nodos_tramo)
tam = collections.Counter(len(f.get("miembros") or []) for f in filas)
check("tamanos 3:23 4:10 5:7 6:4 8:1 10:1 15:1",
      dict(tam) == {3: 23, 4: 10, 5: 7, 6: 4, 8: 1, 10: 1, 15: 1}, str(dict(tam)))
comps = [json.loads(l) for l in open("docs/loop/_auditor_v64_recomputo_salida.json",
                                     encoding="utf-8") if l.strip()]
ab = [set(c.get("miembros") or []) for c in comps
      if str(c.get("estado", "")).upper().startswith("ABIER")]
check("53 componentes ABIERTAS en mi recomputo", len(ab) == 53, "mide %d" % len(ab))
conj_tramo = [set(f.get("miembros") or []) for f in filas]
en_rec = sum(1 for c in conj_tramo if c in ab)
check("las 47 filas del tramo son componentes ABIERTAS de mi recomputo (P.1)",
      en_rec == 47, "calzan %d de 47" % en_rec)
fuera = [c for c in ab if c not in conj_tramo]
check("las 6 de fuera suman 39 nodos", len(fuera) == 6 and sum(len(c) for c in fuera) == 39,
      "%d componentes, %d nodos" % (len(fuera), sum(len(c) for c in fuera)))

print()
print("RESULTADO: %d comprobaciones, %d fallos%s" %
      (total[0], len(fallos), (": " + ", ".join(fallos)) if fallos else ""))
