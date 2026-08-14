# -*- coding: utf-8 -*-
"""Instrumento del AUDITOR, vuelta 21. SOLO LECTURA.

Recomputa desde los archivos, sin copiar nada del reporte 20 ni de actas:
  1.  marcador A/B/C/D, puestos, tasa por dominio
  2.  inventario: entradas, tipos, actos superadas/vigentes, CERRADOS/ABIERTOS,
      deuda de P.5, figuras con marca de tanda
  3.  cota de EL PASO DE OFICIO con TRES cadenas: la de la vuelta 18, la del
      instrumento (ancha) y la del CRITERIO LITERAL escrito en la nota
      (v18 con solo el reemplazo de us commercial service)
  4.  la tanda de los cuatro libros, medida independiente sobre el grafo:
      declaraciones en 2a+ posicion, grupos, solapes, nodos distintos,
      posicion final, nominas contra RECORTE_POSICIONAL.md y OP-F-04-HOR
  5.  pasos de los tres casos de la tabla de 01_FUENTES
  6.  cola de relectura post fusion, forastero, sales roadmap (archivo + LDs)
  7.  guiones largos/medios en las ocho rutas de la vuelta 20
  8.  aditividad del diff de INVENTARIO.jsonl contra 33d37f3c
  9.  lo reservado: blobs identicos entre 33d37f3c y HEAD
  10. LD-71 ausente en todas las sedes de dirigidas
"""
import collections
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
HASH_BASE = "33d37f3c"
HASH_TRABAJO = "1bfab1c4"

RUTAS_V20 = [
    "docs/plan/01_FUENTES.md", "docs/plan/INVENTARIO.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md", "docs/plan/RECOMPUTO_3388.md",
    "scripts/loop/vuelta20_medir.py", "scripts/loop/vuelta20_horowitz.py",
    "scripts/loop/vuelta20_tarea1.py", "scripts/loop/vuelta20_tarea1b.py",
]

PISTAS_V18 = ["oficina de comercio exterior", "comercio exterior", "us commercial service",
              "servicio comercial", "district export council", "distrito de exportacion",
              "consulta con la oficina", "oficina que lo administra"]
PISTAS_INSTRUMENTO = ["comercio exterior", "commercial service", "servicio comercial",
                      "district export council", "distrito de exportacion",
                      "consejo de distrito"]
# el criterio LITERAL que la nota publica: v18 con SOLO el reemplazo
PISTAS_CRITERIO_LITERAL = ["oficina de comercio exterior", "comercio exterior",
                           "commercial service", "servicio comercial",
                           "district export council", "distrito de exportacion",
                           "consulta con la oficina", "oficina que lo administra"]

LIBROS = {
    "hugos": ("hugos",),
    "coleman": ("coleman",),
    "horowitz": ("horowitz", "hard thing"),
    "weinberg": ("weinberg", "traction"),
    "rackham": ("rackham", "spin selling"),
    "mollick": ("mollick", "co-intelligence"),
}
TANDA4 = ("coleman", "horowitz", "weinberg", "rackham")

MIEMBROS_SR = ["customer_validation_sales_roadmap", "estrategia_de_ventas",
               "hoja_de_ruta_de_ventas", "refinar_sales_roadmap", "sales_roadmap",
               "sales_roadmap_vs_sales_force"]


def jsonl(*p):
    with open(RAIZ.joinpath(*p), encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, cwd=RAIZ)
    return r.stdout.decode("utf-8", errors="replace")


def titulo(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


def libros_de(fuente):
    """Lista de (posicion 1-based, libro) por segmento del campo fuente."""
    out = []
    for i, seg in enumerate((fuente or "").split("|"), 1):
        s = seg.strip().lower()
        for lib, toks in LIBROS.items():
            if any(t in s for t in toks):
                out.append((i, lib))
    return out


def main():
    V = jsonl("docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
    inv = jsonl("docs", "plan", "INVENTARIO.jsonl")
    comp = jsonl("docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
    ops = jsonl("docs", "plan", "OPERACIONES.jsonl")
    grafo = json.load(open(RAIZ / "dataset" / "metadata" / "master_graph.json",
                           encoding="utf-8"))
    nodos = grafo["nodos"]
    vivos = {k: x for k, x in nodos.items() if not x.get("deprecado")}

    # -------------------------------------------------------------- 1
    titulo("1. MARCADOR")
    cl = collections.Counter(v["clase"] for v in V)
    n = len(V)
    print("  " + "  ".join("%s=%d (%.1f%%)" % (c, cl[c], 100.0 * cl[c] / n)
                           for c in "ABCD") + "   n=%d" % n)
    puestos = [v["puesto_intra"] for v in V]
    sp = set(puestos)
    print("  puestos: unicos %d, min %d, max %d, dup %d, huecos %d" % (
        len(sp), min(sp), max(sp), len(puestos) - len(sp),
        len(set(range(1, 3389)) - sp)))
    dom = collections.defaultdict(lambda: [0, 0])
    for v in V:
        dom[v["dominio"]][0] += 1
        if v["clase"] == "A":
            dom[v["dominio"]][1] += 1
    for d in sorted(dom, key=lambda k: -dom[k][0]):
        t, a = dom[d]
        print("    %-20s %5d  %4d A  %5.1f%%" % (d, t, a, 100.0 * a / t))

    # -------------------------------------------------------------- 2
    titulo("2. INVENTARIO")
    print("  entradas: %d" % len(inv))
    tipos = collections.Counter(e.get("tipo") for e in inv)
    print("  tipos:", dict(sorted(tipos.items())))
    actos = [e for e in inv if e.get("tipo") == "acto"]
    sup = [e for e in actos if str(e.get("estado", "")).startswith("SUPERADA")]
    vig = [e for e in actos if not str(e.get("estado", "")).startswith("SUPERADA")]
    print("  actos: %d = superadas %d + vigentes %d" % (len(actos), len(sup), len(vig)))
    cerr = sum(1 for e in vig if "CERRADO" in str(e.get("estado", "")))
    abie = sum(1 for e in vig if "ABIERTO" in str(e.get("estado", "")))
    print("  vigentes CERRADOS %d / ABIERTOS %d (sin patron: %d)" % (
        cerr, abie, len(vig) - cerr - abie))
    deuda = cola = fuera = 0
    for e in vig:
        m = re.search(r"(\d+) de (\d+) pares leidos; (\d+) en cola; (\d+) fuera de cola",
                      e.get("cobertura", "") or "")
        if m:
            deuda += int(m.group(2)) - int(m.group(1))
            cola += int(m.group(3))
            fuera += int(m.group(4))
    print("  deuda P.5 por cobertura: %d  (en cola %d, fuera %d)" % (deuda, cola, fuera))
    figs = [e for e in inv if e.get("tipo") == "figura"]
    marca = [e for e in figs if re.search(r"nombrad[ao]s? en (la )?(tanda|vuelta)",
                                          json.dumps(e, ensure_ascii=False), re.I)]
    print("  figuras: %d; con marca de tanda: %d" % (len(figs), len(marca)))
    print("  componentes: %d;  operaciones: %d (estados %s)" % (
        len(comp), len(ops), dict(collections.Counter(o["estado"] for o in ops))))

    # -------------------------------------------------------------- 3
    titulo("3. COTA DE EL PASO DE OFICIO, con TRES cadenas")
    exp_t = {k: x for k, x in nodos.items() if x.get("dominio") == "exportacion"}
    exp_v = {k: x for k, x in exp_t.items() if not x.get("deprecado")}
    pares_exp = [v for v in V if v["dominio"] == "exportacion"]
    print("  exportacion: %d nodos, %d deprecado, %d vivos; %d pares" % (
        len(exp_t), len(exp_t) - len(exp_v), len(exp_v), len(pares_exp)))

    def cota(pistas):
        con = {}
        for nid, x in exp_v.items():
            m = [i for i, p in enumerate(x.get("pasos_accionables") or [], 1)
                 if any(pi in p.lower() for pi in pistas)]
            if m:
                con[nid] = m
        p1 = [k for k, m in con.items() if 1 in m]
        toc = [v for v in pares_exp if v["nodo_a"] in con or v["nodo_b"] in con]
        return con, p1, toc

    res = {}
    for etq, pistas in (("v18 (contraste)", PISTAS_V18),
                        ("instrumento (ancha)", PISTAS_INSTRUMENTO),
                        ("CRITERIO LITERAL de la nota", PISTAS_CRITERIO_LITERAL)):
        con, p1, toc = cota(pistas)
        res[etq] = con
        print("  %-28s nodos %2d / paso1 %d / pares %2d" % (etq, len(con), len(p1), len(toc)))
    dif = set(res["instrumento (ancha)"]) ^ set(res["CRITERIO LITERAL de la nota"])
    print("  diferencia simetrica instrumento vs criterio literal: %d %s" % (
        len(dif), sorted(dif) if dif else ""))

    # -------------------------------------------------------------- 4
    titulo("4. LA TANDA DE LOS CUATRO LIBROS, independiente")
    print("  nodos grafo %d; vivos %d" % (len(nodos), len(vivos)))
    decl2 = []  # (nodo, libro) con el libro en 2a+ posicion
    multi = []
    dobles_mismo = []
    ult_pos = {}
    for nid, x in vivos.items():
        libs = libros_de(x.get("fuente"))
        if not libs:
            continue
        libset = {l for _, l in libs}
        if len(libset) > 1:
            multi.append(nid)
        pos_por_lib = collections.defaultdict(list)
        for pos, lib in libs:
            pos_por_lib[lib].append(pos)
        npos = len((x.get("fuente") or "").split("|"))
        for lib, ps in pos_por_lib.items():
            if any(p >= 2 for p in ps):
                decl2.append((nid, lib))
                ult_pos[(nid, lib)] = (max(ps) == npos)
            if len(ps) > 1:
                dobles_mismo.append((nid, lib, len(ps)))
    print("  con MAS de un libro (de los seis): %d" % len(multi))
    print("  declaraciones en 2a+ posicion (nodo,libro): %d" % len(decl2))
    porlib = collections.Counter(l for _, l in decl2)
    print("  por libro:", dict(sorted(porlib.items())))
    t4 = [(nid, l) for nid, l in decl2 if l in TANDA4]
    nodos4 = sorted({nid for nid, _ in t4})
    print("  tanda de los cuatro: %d declaraciones, %d nodos distintos" % (
        len(t4), len(nodos4)))
    cuenta4 = collections.Counter(nid for nid, _ in t4)
    solapes = sorted(nid for nid, c in cuenta4.items() if c > 1)
    print("  solapes de NODO (dos de los cuatro libros): %s" % solapes)
    no_final = sorted((nid, l) for nid, l in t4 if not ult_pos[(nid, l)])
    print("  declaraciones de la tanda FUERA de la ultima posicion: %d -> %s" % (
        len(no_final), no_final))
    print("  nodos que declaran el MISMO libro dos veces (entre vivos): %s" % (
        sorted((a, b, c) for a, b, c in dobles_mismo)))

    horo = sorted(nid for nid, l in t4 if l == "horowitz")
    print("  nomina Horowitz medida (%d): %s" % (len(horo), horo))
    # contra RECORTE_POSICIONAL.md
    rec = open(RAIZ / "docs" / "plan" / "RECORTE_POSICIONAL.md", encoding="utf-8").read()

    def nomina_recorte(marcador):
        i = rec.find(marcador)
        bloque = rec[i:i + 2000].split("\n")[1]
        return sorted(x.strip() for x in bloque.strip().split(",") if x.strip())

    rec_h = nomina_recorte("The Hard Thing About Hard Things - Ben Horowitz :")
    rec_c = nomina_recorte("Never Lose a Customer Again - Joey Coleman :")
    rec_g = nomina_recorte("Essentials of Supply Chain Management - Michael H. Hugos :")
    cole = sorted(nid for nid, l in t4 if l == "coleman")
    hugo = sorted(nid for nid, l in decl2 if l == "hugos")
    print("  RECORTE: Horowitz %d (identica: %s), Coleman %d (identica: %s), "
          "Hugos %d (identica: %s)" % (
              len(rec_h), rec_h == horo, len(rec_c), rec_c == cole,
              len(rec_g), rec_g == hugo))
    # contra OP-F-04-HOR
    op = [o for o in ops if o["id_op"] == "OP-F-04-HOR"][0]
    n13 = sorted(op["nodos"])
    print("  OP-F-04-HOR.nodos: %d nodos. medida_14 - nomina_13 = %s ; "
          "nomina_13 - medida_14 = %s" % (
              len(n13), sorted(set(horo) - set(n13)), sorted(set(n13) - set(horo))))

    # -------------------------------------------------------------- 5
    titulo("5. LOS TRES CASOS DE LA TABLA DE 01_FUENTES")
    for nid in ("decision_de_vender_startup", "viral_loop_marketing", "coeficiente_viral"):
        x = nodos[nid]
        print("  %-30s pasos=%d  fuente=%s" % (nid, len(x["pasos_accionables"]),
                                               x["fuente"]))
    f = open(RAIZ / "docs" / "plan" / "01_FUENTES.md", encoding="utf-8").read()
    for pat in (r"decision_de_vender_startup[^\n]*?(\d+) pasos",
                r"viral_loop_marketing[^\n]*?(\d+) pasos",
                r"coeficiente_viral[^\n]*?(\d+) pasos"):
        m = re.findall(pat, f)
        print("  01_FUENTES %s -> %s" % (pat.split("[")[0], m[:4]))

    # -------------------------------------------------------------- 6
    titulo("6. COLA POST FUSION, FORASTERO, SALES ROADMAP")
    pp = {v["puesto_intra"]: v for v in V}
    for p in (196, 224, 253, 591, 707, 968, 1096, 751):
        print("  puesto %4d  clase %s" % (p, pp[p]["clase"]))
    for nid in ("tacticas_cierre_ventas", "incentivos_no_monetarios_advocacy"):
        toc = [v for v in V if v["nodo_a"] == nid or v["nodo_b"] == nid]
        print("  %-36s %d pares en archivo: %s" % (
            nid, len(toc), collections.Counter(v["clase"] for v in toc)))
    ms = set(MIEMBROS_SR)
    sr = [v for v in V if v["nodo_a"] in ms and v["nodo_b"] in ms]
    print("  sales roadmap: %d pares internos en archivo (de %d posibles)" % (
        len(sr), len(ms) * (len(ms) - 1) // 2))
    ld = open(RAIZ / "docs" / "plan" / "LD_SALES_ROADMAP.md", encoding="utf-8").read()
    for k in range(66, 71):
        mm = re.search(r"LD-%d[^\n]*" % k, ld)
        print("  %s" % (mm.group(0)[:110] if mm else "LD-%d AUSENTE" % k))

    # -------------------------------------------------------------- 7
    titulo("7. GUIONES EN LAS OCHO RUTAS")
    total = 0
    for r in RUTAS_V20:
        t = open(RAIZ / r, encoding="utf-8").read()
        c = t.count(chr(0x2014)) + t.count(chr(0x2013))
        total += c
        if c:
            print("  %s: %d" % (r, c))
    print("  total guiones largos+medios: %d" % total)

    # -------------------------------------------------------------- 8
    titulo("8. ADITIVIDAD DEL DIFF DE INVENTARIO contra %s" % HASH_BASE)
    viejo = git("show", "%s:docs/plan/INVENTARIO.jsonl" % HASH_BASE).splitlines()
    nuevo = open(RAIZ / "docs" / "plan" / "INVENTARIO.jsonl", encoding="utf-8")\
        .read().splitlines()
    print("  lineas: viejo %d, nuevo %d" % (len(viejo), len(nuevo)))
    cambiadas = [i for i, (a, b) in enumerate(zip(viejo, nuevo)) if a != b]
    print("  lineas cambiadas: %d -> %s" % (len(cambiadas), [i + 1 for i in cambiadas]))
    for i in cambiadas:
        a, b = json.loads(viejo[i]), json.loads(nuevo[i])
        keys_ok = set(a) == set(b)
        campos = []
        for k in a:
            if a[k] != b[k]:
                va, vb = str(a[k]), str(b[k])
                adit = vb.startswith(va) or vb.endswith(va) or va in vb
                campos.append("%s(%s)" % (k, "ADITIVO" if adit else "NO ADITIVO"))
        print("  linea %d [%s]: claves_iguales=%s, campos: %s" % (
            i + 1, a.get("nombre"), keys_ok, ", ".join(campos)))

    # -------------------------------------------------------------- 9
    titulo("9. LO RESERVADO: blobs %s vs HEAD" % HASH_BASE)
    for ruta in ("dataset/metadata/master_graph.json",
                 "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
                 "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl",
                 "docs/plan/OPERACIONES.jsonl"):
        b1 = git("rev-parse", "%s:%s" % (HASH_BASE, ruta)).strip()
        b2 = git("rev-parse", "HEAD:%s" % ruta).strip()
        print("  %-46s identico=%s" % (ruta, b1 == b2))
    d = git("diff", "--stat", HASH_BASE, HASH_TRABAJO, "--", "dataset/")
    print("  git diff --stat %s %s -- dataset/  -> %s" % (
        HASH_BASE, HASH_TRABAJO, repr(d.strip() or "VACIO")))

    # -------------------------------------------------------------- 10
    titulo("10. LD-71 EN TODAS LAS SEDES DE DIRIGIDAS")
    hits = []
    for p in sorted((RAIZ / "docs" / "plan").glob("LD*.md")):
        t = open(p, encoding="utf-8").read()
        if "LD-71" in t:
            hits.append(p.name)
    print("  archivos LD*.md con 'LD-71': %s" % (hits or "NINGUNO"))


if __name__ == "__main__":
    main()
