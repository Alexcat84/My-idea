# Cuenta independiente del auditor, vuelta 62: los 21 actos del tramo 6
# (TRAMO6_V61.jsonl) contra el grafo de HOY y contra los planes sellados.
# Camino propio: no reusa ningun script del ejecutor.
import io, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

sys.stdout.reconfigure(encoding="utf-8")

g = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))
nodos = g["nodos"]

nomina = [json.loads(l) for l in io.open(os.path.join(LOOP, "TRAMO6_V61.jsonl"), encoding="utf-8") if l.strip()]
print("actos en la nomina fijada: %d" % len(nomina))

planes = []
for L in ("A", "B"):
    p = json.load(io.open(os.path.join(LOOP, "PLAN_V62_OPU01_LOTE_%s.json" % L), encoding="utf-8"))
    planes.extend(p["actos"] if "actos" in p else p.get("fusiones", []))
print("actos en los dos planes sellados: %d" % len(planes))

def vivo(nid):
    n = nodos.get(nid)
    return n is not None and not n.get("deprecado", False)

# el superviviente lleva ids_alias con los ids absorbidos: se resuelve por ese mapa
alias_a_vivo = {}
for nid, n in nodos.items():
    if not n.get("deprecado", False):
        for a in n.get("ids_alias", []):
            alias_a_vivo[a] = nid

def resuelve(nid):
    if vivo(nid):
        return nid
    return alias_a_vivo.get(nid)

ids_nomina = set()
fundidos = 0
fallos = []
for acto in nomina:
    ms = acto.get("miembros")
    ids_nomina.update(ms)
    if len(ms) != 2:
        fallos.append("acto con %d miembros: %s" % (len(ms), ms))
        continue
    a, b = ms
    va, vb = vivo(a), vivo(b)
    if va == vb:
        fallos.append("acto %s/%s: vivos=%s,%s (se esperaba uno vivo y uno fundido)" % (a, b, va, vb))
        continue
    muerto = a if vb else b
    superv = b if vb else a
    destino = resuelve(muerto)
    if destino != superv:
        fallos.append("acto %s/%s: el muerto %s resuelve a %s, no al otro miembro" % (a, b, muerto, destino))
        continue
    fundidos += 1
print("actos con UN muerto que resuelve al OTRO miembro: %d" % fundidos)
print("fallos: %d" % len(fallos))
for f in fallos:
    print("  " + f)

# los planes cubren exactamente la nomina
ids_planes = set()
sup_por_plan = {}
for acto in planes:
    par = acto.get("miembros") or [acto.get("muere"), acto.get("sobrevive")]
    ids_planes.update(x for x in par if x)
    if acto.get("sobrevive"):
        sup_por_plan[tuple(sorted(par))] = acto["sobrevive"]
print("ids nomina: %d | ids planes: %d | iguales: %s" %
      (len(ids_nomina), len(ids_planes), ids_nomina == ids_planes))

# la puerta del acto 20 sobrevive
puerta = "mantenimiento_sistema_cui"
print("puerta %s viva: %s" % (puerta, vivo(puerta)))
otro = "getting_started_maintenance"
print("el otro lado %s vivo: %s (resuelve a: %s)" % (otro, vivo(otro), resuelve(otro)))

# deprecados totales y vivos, contraste con la cabecera
dep = sum(1 for n in nodos.values() if n.get("deprecado", False))
print("nodos totales: %d | deprecados: %d | vivos: %d" % (len(nodos), dep, len(nodos) - dep))
