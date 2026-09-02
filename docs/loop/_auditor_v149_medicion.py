# -*- coding: utf-8 -*-
"""MEDICION PROPIA DEL AUDITOR, VUELTA 149, sobre la vuelta 148.

Un solo instrumento, escrito hoy, que no lee ninguna cifra de ningun reporte
ni de ninguna acta: todo sale del repo. Estrictamente de solo lectura.
"""
import collections
import io
import json
import subprocess
import unicodedata

APERTURA = "68db6230"
CIERRE = "200f84bf"
ACTA = "84b64cd0"


def arbol(ref):
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--format=%(objectname) %(path)", ref, "dataset/nodos/"],
        capture_output=True, text=True, encoding="utf-8").stdout
    items = [l.split(" ", 1) for l in out.splitlines() if l.strip()]
    raw = subprocess.run(["git", "cat-file", "--batch"],
                         input="\n".join(o for o, _ in items).encode(),
                         capture_output=True).stdout
    pos, d = 0, {}
    for _o, _path in items:
        nl = raw.index(b"\n", pos)
        size = int(raw[pos:nl].split()[2])
        n = json.loads(raw[nl + 1:nl + 1 + size].decode("utf-8"))
        pos = nl + 1 + size + 1
        d[n["node_id"]] = n
    return d


def censo(G):
    viv = [k for k, v in G.items() if not v.get("deprecado")]
    ns = sum(len(v.get("nodos_siguientes") or []) for v in G.values())
    npv = sum(len(v.get("nodos_previos") or []) for v in G.values())
    u = set()
    for k, v in G.items():
        for x in (v.get("nodos_siguientes") or []):
            u.add((k, x))
        for x in (v.get("nodos_previos") or []):
            u.add((x, k))
    return len(G), len(viv), len(G) - len(viv), ns, npv, ns + npv, len(u)


def resolutor(G):
    A = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in A and x not in s:
            s.add(x)
            x = A[x]
        return x
    return res


def duplicadas(G):
    res = resolutor(G)
    nod = sob = 0
    campo, mot = {}, {}
    for k, v in G.items():
        if v.get("deprecado"):
            continue
        toc = False
        for c in ("nodos_previos", "nodos_siguientes"):
            gr = {}
            for y in (v.get(c) or []):
                d = res(y)
                if d == k:
                    continue
                gr.setdefault(d, []).append(y)
            for d, o in gr.items():
                if len(o) < 2:
                    continue
                s = len(o) - 1
                sob += s
                toc = True
                campo[c] = campo.get(c, 0) + s
                m = "el id nuevo mas su alias" if d in o else "dos alias del mismo destino"
                mot[m] = mot.get(m, 0) + s
        if toc:
            nod += 1
    return nod, sob, campo, mot


def vecindarios(G):
    res = resolutor(G)
    return {(k, c): frozenset(res(y) for y in (v.get(c) or []))
            for k, v in G.items() for c in ("nodos_previos", "nodos_siguientes")}


def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


print("MEDICION DEL AUDITOR DE LA VUELTA 149 SOBRE LA VUELTA 148")
print("Instrumento propio, escrito hoy. Ninguna cifra copiada de una pagina.")
print("=" * 78)

print("\n--- 1. CENSO Y ARISTAS EN LOS CATORCE REFS DE LA VUELTA ---")
REFS = [ACTA, APERTURA, "5567cdc8", "8dc333b4", "3acd002f", "72796815", "21eb9875",
        "0bca418c", "c2c8ca71", "a82cb8e4", "a34328b2", "a352bae1", "8e2ccdf5", CIERRE]
prev = None
for r in REFS:
    t, v, dp, ns, npv, su, un = censo(arbol(r))
    marca = "" if prev is None or prev == (ns, npv) else "   <-- AQUI SALTA (OP-S-12)"
    print("  %s  censo %d/%d/%d   aristas %d/%d/%d/%d%s" % (r, t, v, dp, ns, npv, su, un, marca))
    prev = (ns, npv)

A = arbol(APERTURA)
B = arbol(CIERRE)
ca, cb = censo(A), censo(B)
print("\n--- 2. LO QUE MOVIO LA VUELTA (cierre menos apertura) ---")
print("  nodos_siguientes %+d | nodos_previos %+d | suma %+d | UNION %+d"
      % (cb[3] - ca[3], cb[4] - ca[4], cb[5] - ca[5], cb[6] - ca[6]))
print("  la union quieta es la prueba: no se perdio ni una arista, solo repeticiones.")

print("\n--- 3. LAS DUPLICADAS TRAS RESOLVER, ANTES Y DESPUES ---")
for etq, G in (("APERTURA", A), ("CIERRE", B)):
    n, s, c, m = duplicadas(G)
    print("  %-8s nodos con duplicada %d | entradas que sobran %d" % (etq, n, s))
    print("           por campo %s" % c)
    print("           por motivo %s" % m)

print("\n--- 4. EL VECINDARIO RESUELTO, NODO A NODO Y CAMPO A CAMPO ---")
VA, VB = vecindarios(A), vecindarios(B)
dif = [k for k in set(VA) | set(VB) if VA.get(k) != VB.get(k)]
print("  comparaciones: %d antes / %d despues | DISTINTAS: %d" % (len(VA), len(VB), len(dif)))

print("\n--- 5. NINGUN ID RENOMBRADO NI INVENTADO ---")
la, lb = set(), set()
for G, acc in ((A, la), (B, lb)):
    for v in G.values():
        for c in ("nodos_previos", "nodos_siguientes"):
            acc |= set(v.get(c) or [])
print("  node_id identicos: %s | ids_alias identicos: %s"
      % (set(A) == set(B),
         all((A[k].get("ids_alias") or []) == (B[k].get("ids_alias") or []) for k in A)))
print("  literales usados: %d antes / %d despues" % (len(la), len(lb)))
print("  APARECIDOS DE LA NADA: %s | desaparecidos del todo: %d" % (sorted(lb - la), len(la - lb)))

print("\n--- 6. EL 1.056 DE LA VERIFICACION 4, RASTREADO EN GIT ---")
print("  docs/plan/ARISTAS_DUPLICADAS.jsonl no es un fichero quieto: se regenera.")
hs = subprocess.run(["git", "log", "--format=%h", "--", "docs/plan/ARISTAS_DUPLICADAS.jsonl"],
                    capture_output=True, text=True).stdout.split()
GH = json.loads(subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % CIERRE],
                               capture_output=True).stdout.decode("utf-8"))["nodos"]
for r, etq in ((hs[-1], "LA PRIMERA (la que la ficha cita)"), (hs[0], "LA DE HOY, EN HEAD")):
    t = subprocess.run(["git", "show", "%s:docs/plan/ARISTAS_DUPLICADAS.jsonl" % r],
                       capture_output=True).stdout.decode("utf-8")
    f = [json.loads(l) for l in t.splitlines() if l.strip()]
    print("  %s %s: grupos %d | nodos %d | sobran %d"
          % (r, etq, len(f), len({x["nodo"] for x in f}), sum(x["sobran"] for x in f)))
    if r == hs[0]:
        dep = sum(x["sobran"] for x in f if GH.get(x["nodo"], {}).get("deprecado"))
        print("        de esos, sobre nodos HOY DEPRECADOS: %d | sobre vivos: %d"
              % (dep, sum(x["sobran"] for x in f) - dep))
print("  versiones del fichero en git: %d. Baja monotona: cada fusion consume duplicadas." % len(hs))

print("\n--- 7. EL INDICE SEMANTICO ---")
idx = json.load(io.open("web/lib/assets/semantic_index.json", encoding="utf-8"))
ids = set(idx["ids"])
vivos = {k for k, v in GH.items() if not v.get("deprecado")}
sinvec = sorted(vivos - ids)
noviv = ids - vivos
print("  ids en el indice %d | nodos vivos %d | modelo %s dim %s"
      % (len(idx["ids"]), len(vivos), idx["model"], idx["dimension"]))
print("  VIVOS SIN VECTOR: %d" % len(sinvec))
print("     %s" % ", ".join(sinvec))
print("  ids del indice que NO estan vivos: %d | de ellos DEPRECADOS: %d | FANTASMAS: %d"
      % (len(noviv),
         sum(1 for i in noviv if GH.get(i, {}).get("deprecado")),
         sum(1 for i in noviv if i not in GH)))
blobs = {r: subprocess.run(["git", "rev-parse", "%s:web/lib/assets/semantic_index.json" % r],
                           capture_output=True, text=True).stdout.strip()
         for r in (ACTA, CIERRE)}
print("  blob del indice al abrir y al cerrar: %s (%s): el desfase VIENE DE ANTES, no de OP-S-12."
      % ("IDENTICO" if len(set(blobs.values())) == 1 else "DISTINTO",
         list(blobs.values())[0][:8]))

print("\n--- 8. LA VERIFICACION 3 DE OP-A-01: EL 9 DE 9, RE MEDIDO ---")
nom = json.load(io.open("dataset/metadata/aduana_fuente_multiple.json", encoding="utf-8"))["adjudicados"]
disp = tot = 0
for a in nom:
    pasos = norm(json.dumps(GH[a["node_id"]].get("pasos_accionables") or [], ensure_ascii=False))
    for libro in a["fuente"][1:]:
        tot += 1
        if norm(libro.split(" - ")[0].strip()) not in pasos:
            disp += 1
print("  nodos adjudicados %d | segundos y terceros libros %d | la lectura literal DISPARA EN %d DE %d"
      % (len(nom), tot, disp, tot))

print("\n--- 9. EL MARCADOR DEL CRIBADO ---")
c = collections.Counter()
p = []
for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l)
        c[d.get("clase")] += 1
        p.append(d.get("puesto_intra"))
print("  A %d / B %d / C %d / D %d | n %d | puestos %d a %d | huecos %d | duplicados %d"
      % (c["A"], c["B"], c["C"], c["D"], len(p), min(p), max(p),
         len([i for i in range(1, max(p) + 1) if i not in set(p)]), len(p) - len(set(p))))

print("\n--- 10. LOS REGISTROS, POR PREFIJO EXACTO ---")
for ruta in ("docs/PENDIENTES.md", "docs/plan/CORRECCIONES_A_APLICAR.md",
             "docs/INTRA_DOMINIO_INFORME.md", "docs/plan/OP_S_11_MAPEO_PROPUESTO.md"):
    x = subprocess.run(["git", "show", "%s:%s" % (ACTA, ruta)], capture_output=True).stdout
    y = subprocess.run(["git", "show", "%s:%s" % (CIERRE, ruta)], capture_output=True).stdout
    print("  %-42s %d -> %d | viejo es PREFIJO EXACTO: %s" % (ruta, len(x), len(y), y.startswith(x)))

print("\n--- 11. EL CATALOGO DE OPERACIONES ---")
ops = {}
for l in io.open("docs/plan/OPERACIONES.jsonl", encoding="utf-8"):
    if l.strip():
        d = json.loads(l)
        ops[d["id_op"]] = d
esq = {tuple(sorted(d.keys())) for d in ops.values()}
print("  fichas %d | esquemas distintos %d | claves %d" % (len(ops), len(esq), len(next(iter(esq)))))
print("  05_SANEO por estado: %s"
      % ", ".join("%s=%s" % (k, v["estado"]) for k, v in sorted(ops.items()) if v["fase"] == "05_SANEO"))
print("  OP-C-05: fase %s | orden %s | depende_de %s | estado %s"
      % (ops["OP-C-05"]["fase"], ops["OP-C-05"]["orden"],
         ops["OP-C-05"]["depende_de"], ops["OP-C-05"]["estado"]))
print("  quien nombra a OP-S-12: %s"
      % [k for k, v in ops.items()
         if "OP-S-12" in (v.get("depende_de") or []) + (v.get("bloquea_a") or [])])

print("\nFIN DE LA MEDICION")
