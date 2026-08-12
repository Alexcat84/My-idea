# -*- coding: utf-8 -*-
"""LAS DOS NOMINAS QUE FALTAN, con los DOS instrumentos del estandar (banco 9.20).
   CONTADOR: levanta por el NOMBRE. BARRIDO DE LAS A: levanta por el ARCHIVO.
   Los dos levantan; la lectura decide. Ningun nodo se toca."""
import json, io, sys, re, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
VIV = {k: v for k, v in G.items() if not v.get("deprecado")}
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
P = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
CORTE = max(r["puesto_intra"] for r in V)
leido = {frozenset((r["nodo_a"], r["nodo_b"])): r for r in V}
encola = {frozenset((p["nodo_a"], p["nodo_b"])) for p in P}
ady = collections.defaultdict(set)
for r in V:
    if r["clase"] == "A":
        ady[r["nodo_a"]].add(r["nodo_b"]); ady[r["nodo_b"]].add(r["nodo_a"])
def comp(n):
    pila = [n]; c = set()
    while pila:
        x = pila.pop()
        if x in c: continue
        c.add(x); pila.extend(ady[x] - c)
    return c
def cobertura(nom, tit):
    pos = len(nom)*(len(nom)-1)//2
    ley = [p for p in itertools.combinations(sorted(nom),2) if frozenset(p) in leido]
    col = [p for p in itertools.combinations(sorted(nom),2) if frozenset(p) in encola and frozenset(p) not in leido]
    fue = [p for p in itertools.combinations(sorted(nom),2) if frozenset(p) not in encola and frozenset(p) not in leido]
    cl = collections.Counter(leido[frozenset(p)]["clase"] for p in ley)
    forma = "PURO" if cl.get("A",0)==len(ley)==pos else ("SUB-PURO" if len(ley) and cl.get("A",0)==len(ley) else "MEZCLADO")
    print("   %s: miembros %d | posibles %d | leidos %d (%s) | en cola %d | fuera de cola %d | FORMA %s | COBERTURA %d de %d"
          % (tit, len(nom), pos, len(ley), dict(cl), len(col), len(fue), forma, len(ley), pos))
    return ley, col, fue, cl, forma

print("="*78); print("# A. EL RACIMO DEL PIVOTE"); print("="*78)
RX = re.compile(r"pivot|perseverar", re.I)
cont = sorted(k for k,v in VIV.items() if RX.search(k) or RX.search(v.get("titulo_concepto") or ""))
print("1. CONTADOR (por el nombre): %d candidatos brutos" % len(cont))
# BARRIDO: solo los que tienen A con otro candidato del tema
tema = set(cont)
nucleo = set()
for k in cont:
    c = comp(k) & tema
    if len(c) > 1: nucleo |= c
print("2. BARRIDO DE LAS A (por el archivo): %d nodos con A dentro del tema" % len(nucleo))
print()
print("### LA NOMINA CONFIRMADA POR LOS DOS INSTRUMENTOS")
for k in sorted(nucleo): print("   -", k, "|", VIV[k].get("titulo_concepto"), "|", (VIV[k].get("fuente") or "")[:34])
ley, col, fue, cl, forma = cobertura(nucleo, "NOMINA")
print()
print("   los pares leidos dentro de la nomina:")
for a,b in ley: print("      [%s] %s | %s  (puesto %d)"%(leido[frozenset((a,b))]["clase"],a,b,leido[frozenset((a,b))]["puesto_intra"]))
print()
print("### CANDIDATOS DEL CONTADOR QUE EL ARCHIVO NO CONFIRMA: %d" % len(tema-nucleo))
for k in sorted(tema-nucleo):
    n = sum(1 for r in V if k in (r["nodo_a"], r["nodo_b"]))
    a = sum(1 for r in V if k in (r["nodo_a"], r["nodo_b"]) and r["clase"]=="A")
    print("   - %-46s lecturas %2d, A %d" % (k, n, a))

print()
print("="*78); print("# B. LA SERIE DE COLEMAN"); print("="*78)
COL = re.compile(r"never lose a customer|coleman", re.I)
todos = sorted(k for k,v in VIV.items() if COL.search(v.get("fuente") or ""))
prim = [k for k in todos if COL.search(re.split(r"\s*\|\s*", VIV[k]["fuente"])[0])]
seg  = [k for k in todos if k not in prim]
print("nodos vivos que declaran el libro: %d | en PRIMERA posicion: %d | en SEGUNDA (segunda casa): %d"
      % (len(todos), len(prim), len(seg)))
FASES = [("Assess","assess|evalua"),("Admit","admit|admis"),("Affirm","affirm|afirma|reafirma"),
         ("Activate","activate|activa"),("Acclimate","acclimate|aclimat"),("Accomplish","accomplish|logro|cumplim"),
         ("Adopt","adopt"),("Advocate","advocate|promotor|embajador")]
prog = re.compile(r"ocho fases|8 fases|ciclo de vida del cliente|primeros 100 dias|100 dias", re.I)
canal = re.compile(r"correo|email|telefono|video|mensaje|regalo|carta|postal|medio|canal", re.I)
def texto(k):
    v=VIV[k]; return " ".join([k, v.get("titulo_concepto") or "", v.get("resumen_teorico") or ""])
fase_de = {}
for k in todos:
    t=texto(k)
    for nom,rx in FASES:
        if re.search(rx, t, re.I): fase_de.setdefault(k, nom)
progs = [k for k in todos if prog.search(texto(k))]
canales = [k for k in todos if canal.search(k) or canal.search(VIV[k].get("titulo_concepto") or "")]
sel = sorted(set(fase_de) | set(progs) | set(canales))
print()
print("### LOS NODOS DE LA SERIE: %d" % len(sel))
print("| id | fase | papel | casa |")
for k in sel:
    papel = []
    if k in progs: papel.append("PROGRAMA")
    if k in fase_de: papel.append("FASE " + fase_de[k])
    if k in canales: papel.append("MEDIO")
    print("| %-44s | %-10s | %-22s | %s |" % (k, fase_de.get(k,""), ", ".join(papel), "SEGUNDA CASA" if k in seg else "propia"))
print()
c1=collections.Counter(fase_de.get(k,"sin fase") for k in sel)
print("por fase:", dict(c1))
print("programa:", len(progs), "| medios:", len(canales), "| segunda casa dentro de la serie:", len([k for k in sel if k in seg]))
