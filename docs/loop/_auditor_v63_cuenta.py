# -*- coding: utf-8 -*-
# Cuenta independiente del auditor, vuelta 63: las dos fusiones de mesa
# y la nomina de OP-U-02, contra el grafo de HOY, sin reusar los
# verificadores del ejecutor.
import json, hashlib, io, sys, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
NODOS = "dataset/nodos"

def cargar(nid):
    for raiz, _dirs, fs in os.walk(NODOS):
        if nid + ".json" in fs:
            return json.load(open(os.path.join(raiz, nid + ".json"), encoding="utf-8"))
    raise SystemExit("NO ENCONTRADO: " + nid)

fallos = []
def check(nombre, cond, detalle=""):
    print(("OK   " if cond else "FALLO") + " | " + nombre + (" | " + detalle if detalle else ""))
    if not cond:
        fallos.append(nombre)

def vivo(d):
    return not (d.get("deprecado") or d.get("deprecated") or d.get("estado") == "deprecado")

def pasos_de(d):
    return d.get("pasos_accionables") or []

def cond_de(d):
    return d.get("condiciones_activacion") or []

print("=== OP-M-03-I ===")
sup = cargar("pivotar_o_perseverar")
mue = cargar("decision_pivote_perseverar")
pb  = cargar("puntos_brillantes_antes_del_pivote")
pasos_sup = pasos_de(sup)
cond_sup = cond_de(sup)
check("superviviente vivo", vivo(sup))
check("superviviente 6 pasos", len(pasos_sup) == 6, "mide %d" % len(pasos_sup))
check("superviviente 3 condiciones", len(cond_sup) == 3, "mide %d" % len(cond_sup))
alias = (sup.get("ids_alias") or []) + (sup.get("merged_originals") or [])
check("alias carga al muerto", "decision_pivote_perseverar" in alias)
check("absorbido deprecado", not vivo(mue))
pasos_mue = pasos_de(mue)
check("absorbido con texto intacto", len(pasos_mue) > 0, "%d pasos" % len(pasos_mue))
check("nodo propio VIVO", vivo(pb))
pasos_pb = pasos_de(pb)
check("nodo propio 5 pasos", len(pasos_pb) == 5, "mide %d" % len(pasos_pb))
raw_pb = json.dumps(pb, ensure_ascii=False)
check("nodo propio SIN el id muerto", "decision_pivote_perseverar" not in raw_pb)
check("nodo propio nombra al superviviente en previos",
      "pivotar_o_perseverar" in (pb.get("nodos_previos") or []))
check("superviviente nombra al nodo propio en siguientes",
      "puntos_brillantes_antes_del_pivote" in (sup.get("nodos_siguientes") or []))

print()
print("=== OP-M-02-PROG ===")
sup2 = cargar("ocho_fases_experiencia_cliente")
mue2 = cargar("fases_de_retencion_de_clientes")
tes  = cargar("pensamiento_h2h")
pasos2 = pasos_de(sup2)
cond2 = cond_de(sup2)
check("superviviente vivo", vivo(sup2))
check("superviviente 5 pasos", len(pasos2) == 5, "mide %d" % len(pasos2))
check("superviviente 2 condiciones", len(cond2) == 2, "mide %d" % len(cond2))
alias2 = (sup2.get("ids_alias") or []) + (sup2.get("merged_originals") or [])
check("alias carga al muerto", "fases_de_retencion_de_clientes" in alias2)
check("absorbido deprecado", not vivo(mue2))
pasos_mue2 = pasos_de(mue2)
check("absorbido con texto intacto", len(pasos_mue2) > 0, "%d pasos" % len(pasos_mue2))
enl_tes = (tes.get("nodos_previos") or []) + (tes.get("nodos_siguientes") or [])
check("testigo nombra al superviviente UNA vez",
      enl_tes.count("ocho_fases_experiencia_cliente") == 1,
      "cuenta %d" % enl_tes.count("ocho_fases_experiencia_cliente"))
check("testigo nombra al muerto CERO veces",
      enl_tes.count("fases_de_retencion_de_clientes") == 0)
check("testigo sin auto-arista", tes.get("id", "pensamiento_h2h") not in enl_tes)
paso5 = json.dumps(pasos2[4] if len(pasos2) >= 5 else "", ensure_ascii=False)
check("las dos prioridades en el paso 5", "Affirm" in paso5 and "Activate" in paso5)

print()
print("=== NOMINA OP-U-02 contra MI recomputo ===")
nom = [json.loads(l) for l in open("docs/loop/NOMINA_OPU02_V63.jsonl", encoding="utf-8") if l.strip()]
print("filas de la nomina:", len(nom))
claves = set()
for fila in nom:
    ms = fila.get("miembros") or fila.get("nodos") or []
    claves.add(frozenset(ms))
mios = [json.loads(l) for l in open("docs/loop/_auditor_v63_componentes.jsonl", encoding="utf-8") if l.strip()]
abiertos = [c for c in mios if (c.get("estado") or c.get("clase") or "").upper().startswith("ABIERTO")]
if not abiertos:
    # fallback: componentes sin campo estado; ABIERTO = no CERRADO
    abiertos = [c for c in mios if not (c.get("cerrado") or (c.get("estado") or "").upper().startswith("CERR"))]
print("componentes en mi jsonl:", len(mios), "| abiertas segun campo:", len(abiertos))
claves_mias = set()
for c in abiertos:
    ms = c.get("miembros") or c.get("nodos") or []
    claves_mias.add(frozenset(ms))
print("actos de la nomina que calzan con una componente ABIERTA mia:",
      sum(1 for k in claves if k in claves_mias), "de", len(claves))
# el reparto 47 / 6
campos = set()
for fila in nom:
    campos |= set(fila.keys())
print("campos de la nomina:", sorted(campos))
abre = [f for f in nom if f.get("abre")]
fuera = [f for f in nom if not f.get("abre")]
print("abre:", len(abre), "| fuera:", len(fuera))
print("nodos en los que abren:", sum(f.get("tamano") or len(f.get("miembros") or []) for f in abre))
print("nodos en los que quedan fuera:", sum(f.get("tamano") or len(f.get("miembros") or []) for f in fuera))
for f in fuera:
    print("  FUERA tamano %s duenos %s" % (f.get("tamano"), f.get("duenos_mesa_o_destejido")))
tocan = [f for f in nom if f.get("duenos_cualquier_operacion")]
print("criterio ANCHO: tocan alguna nomina:", len(tocan), "| no tocan ninguna:", len(nom) - len(tocan))

print()
print("=== SHA1 DEL ANCESTRO ===")
h = hashlib.sha1(open("scripts/loop/vuelta49_fundir_tramo.py", "rb").read()).hexdigest()
print("sha1 vuelta49_fundir_tramo.py:", h[:12])

print()
print("FALLOS:", len(fallos), fallos if fallos else "")
