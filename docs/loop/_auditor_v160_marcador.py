# AUDITOR VUELTA 160: marcador propio, escrito hoy. No copia ninguna cifra.
import json, collections, pathlib
R = pathlib.Path(".")
ver = R/"docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
filas = [json.loads(l) for l in ver.read_text(encoding="utf-8").splitlines() if l.strip()]
print("CIFRA n, filas del archivo:", len(filas))
cl = collections.Counter(f.get("clase") for f in filas)
for k in "ABCD":
    print(f"CIFRA marcador clase {k}:", cl.get(k,0))
puestos = [f.get("puesto_intra") for f in filas if f.get("puesto_intra") is not None]
print("CIFRA puestos distintos:", len(set(puestos)))
if puestos:
    lo, hi = min(puestos), max(puestos)
    print("CIFRA huecos:", len(set(range(lo,hi+1)) - set(puestos)))
print("CIFRA duplicados:", len(puestos)-len(set(puestos)))

g = json.loads((R/"dataset/metadata/master_graph.json").read_text(encoding="utf-8"))
nodos = g["nodos"]
if isinstance(nodos, dict): nodos = list(nodos.values())
print("CIFRA nodos:", len(nodos))
vivos = [n for n in nodos if not n.get("deprecado")]
print("CIFRA vivos:", len(vivos))
print("CIFRA deprecados:", len(nodos)-len(vivos))
sig=set(); prev=set()
ns=np_=0
for n in nodos:
    a = n.get("node_id")
    for b in (n.get("nodos_siguientes") or []):
        ns+=1; sig.add((a,b))
    for b in (n.get("nodos_previos") or []):
        np_+=1; prev.add((b,a))
print("CIFRA aristas nodos_siguientes:", ns)
print("CIFRA aristas nodos_previos:", np_)
print("CIFRA suma de las dos vistas:", ns+np_)
print("CIFRA union DIRIGIDA de las dos vistas:", len(sig|prev))
print("CIFRA solo en nodos_siguientes:", len(sig-prev))
print("CIFRA solo en nodos_previos:", len(prev-sig))
print("CIFRA auto enlaces:", len([1 for a,b in (sig|prev) if a==b]))

reg = [json.loads(l) for l in (R/"docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
print("CIFRA filas del registro de citas:", len(reg))
via = collections.Counter((f.get("via") or "LECTURA_DIRIGIDA" if str(f.get("cita","")).startswith("LD-") else f.get("via"), f.get("clase")) for f in reg)
c2 = collections.Counter()
for f in reg:
    v = f.get("via")
    if not v:
        v = "LECTURA_DIRIGIDA" if str(f.get("cita","")).startswith("LD-") else "CRIBADO"
    c2[(v, f.get("clase"))]+=1
for (v,k),n in sorted(c2.items()):
    print(f"CIFRA registro {v} clase {k}: {n}")
ld = [f for f in reg if str(f.get("cita","")).startswith("LD-")]
print("CIFRA citas de lectura dirigida:", len(ld))
print("CIFRA citas con rastro de correccion:", len([f for f in reg if "CORRECCION DECLARADA" in f.get("razon","") or "RECLASIFICADA" in f.get("cita","")]))
