#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_direccion.py . levanta las A cuya razon invoca la vara y prepara su verificacion.

SOLO LECTURA sobre el archivo de veredictos y sobre el grafo. No cambia ni una clase.

La vara del banco 9.6.1 TIENE DIRECCION: pregunta que anade el HIJO a la MADRE.
Una A escrita al reves mata a la madre por enunciar sus pasos en forma compacta.
Este script no decide: SELECCIONA los pares donde hay que mirar, y para cada uno
imprime lo que hace falta para decidir a ojo, los pasos de los dos nodos y quien
sobrevivio segun la razon.

Uso:
  python scripts/barrido_direccion.py --contar
  python scripts/barrido_direccion.py --desde 1 --hasta 2376
  python scripts/barrido_direccion.py --puestos 2127,2145
"""
import json, io, sys, re, argparse, unicodedata

ap = argparse.ArgumentParser()
ap.add_argument("--contar", action="store_true")
ap.add_argument("--desde", type=int, default=1)
ap.add_argument("--hasta", type=int, default=10 ** 9)
ap.add_argument("--puestos", default="")
ap.add_argument("--breve", action="store_true")
ap.add_argument("--tabla", action="store_true", help="prueba de cobertura sobre todas las A que invocan la vara")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")


def sinac(s):
    return "".join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn").upper()


G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
AL = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}


def res(x):
    s = set()
    while x in AL and x not in s:
        s.add(x); x = AL[x]
    return x


def vecinos(k):
    out = set()
    for c in ("nodos_previos", "nodos_siguientes"):
        for y in (G.get(k, {}).get(c) or []):
            out.add(res(y))
    return out


SURV = [r"[Ss]obrevive\s+`?([a-z0-9_]+)", r"[Ss]uperviviente[^a-z0-9_]{0,12}`?([a-z0-9_]+)",
        r"[Gg]ana\s+`?([a-z0-9_]+)", r"direccion de fusion[^a-z0-9_]{0,20}`?([a-z0-9_]+)"]


def surviviente(r):
    """Devuelve el id del superviviente si la razon ELIGE DIRECCION, o None."""
    for pat in SURV:
        m = re.search(pat, r["razon"])
        if m and m.group(1) in (r["nodo_a"], r["nodo_b"]):
            return m.group(1)
    return None




# ---------------------------------------------------------------------------
# LA PRUEBA DE COBERTURA: una A correcta exige que el nodo que MUERE este
# largamente contenido en el que SOBREVIVE. Si el muerto NO esta contenido, la
# vara se aplico al reves: se peso lo que la madre anade al hijo.
# ---------------------------------------------------------------------------
VACIAS = set("""de la el los las un una unos unas y o u en con por para al del que se su sus
lo a e si no mas menos como cuando donde cada todo toda todos todas este esta estos estas
ese esa eso aquel tu tus mi mis te le les nos ya sin sobre entre hasta desde ante tras
es son ser esta estan hay haber tiene tener puede pueden debe deben tambien solo segun
antes despues durante muy bien mejor peor tanto tan asi aunque pero sino porque ni""".split())


def pal(s):
    z = sinac(s).lower()
    z = re.sub(r"[^a-z0-9novaeiou ]+", " ", z)
    return set(w for w in z.split() if len(w) > 3 and w not in VACIAS)


def cobertura(x, y):
    """Fraccion de los pasos de x cuyo vocabulario propio aparece en el texto de y."""
    px = (G.get(x, {}).get("pasos_accionables") or [])
    if not px:
        return None, 0, 0
    ty = pal(" ".join((G.get(y, {}).get("pasos_accionables") or []) + [G.get(y, {}).get("titulo_concepto") or ""]))
    cub = 0
    for s in px:
        ps = pal(s)
        if not ps:
            continue
        if len(ps & ty) / float(len(ps)) >= 0.34:
            cub += 1
    return cub / float(len(px)), cub, len(px)


# La formula y sus variantes, todas normalizadas sin acentos y en mayusculas.
FORMULAS = ["9.6.1", "LA VARA", "POR LA VARA", "CABE EN UNA LINEA", "CABE EN LINEAS",
            "TRAE UN PROCEDIMIENTO", "REPITE", "CONTINUA"]

A = [r for r in V if r["clase"] == "A"]
invocan = []
for r in A:
    z = sinac(r["razon"])
    if any(f in z for f in FORMULAS):
        invocan.append(r)

if a.contar:
    print("veredictos en el archivo: %d" % len(V))
    print("clase A: %d" % len(A))
    print("A cuya razon invoca la vara: %d  (%.1f%% de las A)" % (len(invocan), 100.0 * len(invocan) / len(A)))
    import collections
    c = collections.Counter(r["dominio"] for r in invocan)
    print("por dominio: %s" % dict(c))
    ca = collections.Counter(r["dominio"] for r in A)
    print("A totales por dominio: %s" % dict(ca))
    # cuantas ELIGEN DIRECCION: solo esas pueden estar al reves
    con = [r for r in invocan if surviviente(r)]
    print("de esas, ELIGEN DIRECCION (nombran superviviente): %d" % len(con))
    print("de esas, NO eligen direccion (REPITE sin superviviente): %d" % (len(invocan) - len(con)))
    cc = collections.Counter(r["dominio"] for r in con)
    print("las que eligen direccion, por dominio: %s" % dict(cc))
    sys.exit(0)


if a.tabla:
    filas = []
    for r in invocan:
        n = r["puesto_intra"]
        if not (a.desde <= n <= a.hasta):
            continue
        surv = surviviente(r)
        A_, B_ = r["nodo_a"], r["nodo_b"]
        if surv:
            muere, vive = (A_ if B_ == surv else B_), surv
        else:
            muere, vive = None, None
        if muere:
            c, cub, tot = cobertura(muere, vive)
            cr, cubr, totr = cobertura(vive, muere)
            filas.append((n, r["dominio"], muere, vive, c, cub, tot, cr, cubr, totr))
        else:
            ca, cua, ta = cobertura(A_, B_)
            cb, cub2, tb = cobertura(B_, A_)
            filas.append((n, r["dominio"], None, None, ca, cua, ta, cb, cub2, tb))
    print("puesto dominio           muere->vive  (cub/tot)   vive->muere (cub/tot)  veredicto de la prueba")
    sos = 0
    for n, d, m, v, c, cub, tot, cr, cubr, totr in sorted(filas):
        if m is None:
            print("%6d %-16s SIN DIRECCION ELEGIDA   A->B %d/%d  B->A %d/%d" % (n, d, cub, tot, cubr, totr))
            continue
        et = "OK" if c is not None and c >= 0.5 else ("SOSPECHOSO" if c is not None and c < 0.34 else "REVISAR")
        if et != "OK":
            sos += 1
        print("%6d %-16s %5.0f%% (%d/%d)   %5.0f%% (%d/%d)   %s   muere=%s vive=%s"
              % (n, d, 100 * c, cub, tot, 100 * cr, cubr, totr, et, m, v))
    print()
    print("filas con direccion elegida: %d | no OK: %d" % (sum(1 for f in filas if f[2]), sos))
    sys.exit(0)

sel = set(int(x) for x in a.puestos.split(",") if x.strip()) if a.puestos else None
for r in invocan:
    n = r["puesto_intra"]
    if sel is not None and n not in sel:
        continue
    if not (a.desde <= n <= a.hasta):
        continue
    surv = surviviente(r)
    A_, B_ = r["nodo_a"], r["nodo_b"]
    muere = (A_ if B_ == surv else B_) if surv else None
    arista = (res(B_) in vecinos(A_)) or (res(A_) in vecinos(B_))
    print("=" * 78)
    print("PUESTO %d  [%s]  %s" % (n, r["dominio"], "CON ARISTA" if arista else "sin arista"))
    print("  sobrevive: %s" % (surv or "NO NOMBRADO EN LA RAZON"))
    print("  muere:     %s" % (muere or "NO DEDUCIBLE"))
    for k in (A_, B_):
        nd = G.get(k) or {}
        rol = "MUERE" if k == muere else ("SOBREVIVE" if k == surv else "?")
        print("  --- [%s] %s  (%d pasos)" % (rol, k, len(nd.get("pasos_accionables") or [])))
        if not a.breve:
            for j, s in enumerate(nd.get("pasos_accionables") or [], 1):
                print("      %d. %s" % (j, s[:160]))

