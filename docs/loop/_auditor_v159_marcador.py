# AUDITOR VUELTA 159: instrumento propio, escrito hoy, sin importar codigo de la casa.
# Recomputa marcador, censo, aristas y registro directamente de los ficheros.
import json, os, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- 1. ARCHIVO DEL CRIBADO ---
filas = []
with open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"), encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        if l:
            filas.append(json.loads(l))
print("CIFRA n, filas del archivo:", len(filas))
clases = collections.Counter(x.get("clase") for x in filas)
for c in ("A", "B", "C", "D"):
    print("CIFRA marcador clase %s:" % c, clases.get(c, 0))
otras = {k: v for k, v in clases.items() if k not in ("A", "B", "C", "D")}
print("CIFRA clases fuera de ABCD:", otras if otras else 0)
puestos = [x.get("puesto_intra") for x in filas]
print("CIFRA puestos distintos:", len(set(puestos)))
print("CIFRA min y max de puesto:", min(puestos), max(puestos))
esperados = set(range(1, len(filas) + 1))
print("CIFRA huecos:", len(esperados - set(puestos)))
dup = [p for p, n in collections.Counter(puestos).items() if n > 1]
print("CIFRA duplicados:", len(dup))

# --- 2. CENSO Y ARISTAS ---
base = os.path.join(RAIZ, "dataset", "nodos")
nodos, vivos, deprec = 0, 0, 0
sig, prev = set(), set()
ids = set()
for dirpath, _, ficheros in os.walk(base):
    for fn in ficheros:
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
            d = json.load(f)
        lista = d if isinstance(d, list) else [d]
        for nodo in lista:
            nodos += 1
            nid = nodo.get("id")
            ids.add(nid)
            if nodo.get("deprecado") or nodo.get("estado") == "deprecado":
                deprec += 1
            else:
                vivos += 1
            for s in (nodo.get("nodos_siguientes") or []):
                sig.add((nid, s if isinstance(s, str) else s.get("id")))
            for p in (nodo.get("nodos_previos") or []):
                prev.add((p if isinstance(p, str) else p.get("id"), nid))
print("CIFRA nodos:", nodos)
print("CIFRA vivos:", vivos)
print("CIFRA deprecados:", deprec)
print("CIFRA aristas nodos_siguientes:", len(sig))
print("CIFRA aristas nodos_previos:", len(prev))
print("CIFRA suma de las dos vistas:", len(sig) + len(prev))
print("CIFRA union DIRIGIDA de las dos vistas:", len(sig | prev))
print("CIFRA solo en nodos_siguientes:", len(sig - prev))
print("CIFRA solo en nodos_previos:", len(prev - sig))
print("CIFRA auto enlaces:", len([a for a in (sig | prev) if a[0] == a[1]]))

# --- 3. REGISTRO DE CITAS ---
reg = []
with open(os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl"), encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        if l:
            reg.append(json.loads(l))
print("CIFRA filas del registro de citas:", len(reg))
vias = collections.Counter()
for r in reg:
    via = "LECTURA_DIRIGIDA" if r["cita"].startswith("LD-") else "CRIBADO"
    vias[(via, r["clase"])] += 1
for k in sorted(vias):
    print("CIFRA registro %s clase %s:" % k, vias[k])
ld = [r for r in reg if r["cita"].startswith("LD-")]
print("CIFRA citas de lectura dirigida:", len(ld))
print("CIFRA citas con rastro de correccion:", len([r for r in reg if "RECLASIFICADA" in r["cita"]]))
print("CIFRA citas en la forma vieja de la vuelta 156:", len([r for r in reg if "RECLASIFICADA A" in r["cita"]]))
# coherencia: el ultimo token de clase en la cita contra el campo clase
malas = [r["cita"][:16] for r in reg if (" clase " in r["cita"]) and (r["cita"].split(" clase ")[1].split()[0].strip("[],") != r["clase"])]
print("CIFRA citas cuya clase escrita NO es la clase vigente:", len(malas), malas[:5])
