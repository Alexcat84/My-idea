# -*- coding: utf-8 -*-
"""VUELTA 20: la FASE II medida al cierre. SOLO LECTURA, no escribe nada.

Mide en esta vuelta, y desde las fuentes, TODA cifra que la vuelta publique:

  1. El marcador del archivo de veredictos y la tasa por dominio.
  2. LA COTA DE EL PASO DE OFICIO con las DOS cadenas, la de la vuelta 18 y la
     corregida, sobre los nodos VIVOS del dominio exportacion: nodos, nodos con
     la linea en su PASO 1, y pares tocados. Es la cifra que TAREA 1.3 regenera,
     y sale de aqui, no de la nota ni del reporte 19.
  3. Los CINCO BLOQUES de la FASE II remedidos: la cola de relectura post
     fusion, el criterio del forastero, el lote de cinco del sales roadmap, las
     lecturas de acto entero de P.5, y los ejemplares de las veinte figuras.
  4. El inventario entero: entradas por tipo, actos vigentes CERRADOS y
     ABIERTOS, y la deuda de P.5.
  5. LA LISTA B: las cifras publicadas con DOS LECTURAS, cada una con sus dos
     sedes leidas hoy, para poder decir cuales quedan sin adjudicar y cuales no.
  6. Lo reservado: que dataset/ y el archivo de veredictos siguen intactos.

Correr DESPUES de los registros de TAREA 1 para la medicion de cierre, y ANTES
para tener el antes. El script no cierra nada: quien cierra la FASE II es el
auditor.
"""
import collections
import io
import itertools
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]

PISTAS_V18 = ["oficina de comercio exterior", "comercio exterior", "us commercial service",
              "servicio comercial", "district export council", "distrito de exportacion",
              "consulta con la oficina", "oficina que lo administra"]
PISTAS_CORREGIDA = ["comercio exterior", "commercial service", "servicio comercial",
                    "district export council", "distrito de exportacion",
                    "consejo de distrito"]

MIEMBROS_SALES_ROADMAP = [
    "customer_validation_sales_roadmap", "estrategia_de_ventas",
    "hoja_de_ruta_de_ventas", "refinar_sales_roadmap", "sales_roadmap",
    "sales_roadmap_vs_sales_force"]


def jsonl(*p):
    with open(RAIZ.joinpath(*p), encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def titulo(t):
    print()
    print("=" * 98)
    print(t)
    print("=" * 98)


def main():
    V = jsonl("docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
    inv = jsonl("docs", "plan", "INVENTARIO.jsonl")
    comp = jsonl("docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
    grafo = json.load(open(RAIZ / "dataset" / "metadata" / "master_graph.json",
                           encoding="utf-8"))
    nodos = grafo["nodos"]
    vivos = {k: x for k, x in nodos.items() if not x.get("deprecado")}
    por_puesto = {v["puesto_intra"]: v for v in V}
    figuras = [e for e in inv if e.get("tipo") == "figura"]

    # ------------------------------------------------------------------ 1
    titulo("1. EL MARCADOR, desde docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    cl = collections.Counter(v["clase"] for v in V)
    n = len(V)
    for c in ("A", "B", "C", "D"):
        print("  %s  %5d   %4.1f%%" % (c, cl[c], 100.0 * cl[c] / n))
    print("  n  %5d" % n)
    puestos = [v["puesto_intra"] for v in V]
    print("  puestos unicos %d, min %d, max %d, duplicados %d, huecos %d" % (
        len(set(puestos)), min(puestos), max(puestos),
        len(puestos) - len(set(puestos)),
        len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))))
    print()
    print("  tasa por dominio:")
    por_dom = collections.defaultdict(lambda: [0, 0])
    for v in V:
        por_dom[v["dominio"]][0] += 1
        if v["clase"] == "A":
            por_dom[v["dominio"]][1] += 1
    for d in sorted(por_dom):
        t, a = por_dom[d]
        print("    %-20s %5d pares  %4d A  %5.1f%%" % (d, t, a, 100.0 * a / t))

    # ------------------------------------------------------------------ 2
    titulo("2. LA COTA DE EL PASO DE OFICIO, con las DOS cadenas")
    exp_todos = {k: x for k, x in nodos.items() if x.get("dominio") == "exportacion"}
    exp_dep = {k: x for k, x in exp_todos.items() if x.get("deprecado")}
    exp_vivos = {k: x for k, x in exp_todos.items() if not x.get("deprecado")}
    pares_exp = [v for v in V if v["dominio"] == "exportacion"]
    print("  nodos del dominio exportacion en el grafo: %d" % len(exp_todos))
    print("  de esos deprecado: %d;  VIVOS: %d" % (len(exp_dep), len(exp_vivos)))
    print("  pares leidos del dominio: %d" % len(pares_exp))

    def cota(pistas):
        con = {}
        for nid, x in exp_vivos.items():
            m = [i for i, p in enumerate(x.get("pasos_accionables") or [], 1)
                 if any(pi in p.lower() for pi in pistas)]
            if m:
                con[nid] = m
        return con

    resultados = {}
    for etq, pistas in (("vuelta 18", PISTAS_V18), ("corregida", PISTAS_CORREGIDA)):
        con = cota(pistas)
        p1 = sorted(k for k, m in con.items() if 1 in m)
        toc = [v for v in pares_exp if v["nodo_a"] in con or v["nodo_b"] in con]
        resultados[etq] = (con, p1, toc)
        print()
        print("  CADENA %s:" % etq)
        print("    nodos con la linea:            %3d de %d vivos" % (
            len(con), len(exp_vivos)))
        print("    nodos con la linea en PASO 1:  %3d" % len(p1))
        print("    pares tocados:                 %3d de %d" % (len(toc), len(pares_exp)))
    print()
    print("  los nodos de la cota CORREGIDA, uno por uno:")
    con_c = resultados["corregida"][0]
    for nid in sorted(con_c):
        print("    %-54s pasos %-10s deprecado %s" % (
            nid, con_c[nid], bool(nodos[nid].get("deprecado"))))
    print("  los que traen la linea en su PASO 1 (%d):" % len(resultados["corregida"][1]))
    for nid in resultados["corregida"][1]:
        print("    %s" % nid)
    print("  los %d pares tocados por la cota corregida:" % len(resultados["corregida"][2]))
    print("    %s" % sorted(v["puesto_intra"] for v in resultados["corregida"][2]))

    # ------------------------------------------------------------------ 3
    titulo("3. LOS CINCO BLOQUES DE LA FASE II, remedidos")

    print("  BLOQUE 1: la cola de relectura post fusion")
    defecto = [e for e in inv if e.get("tipo") == "defecto"
               and "fusion reabre" in (e.get("nombre") or "")]
    for d in defecto:
        limpio = re.sub(r"\b(?:ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+\d{4}\b",
                        " ", d["nota"])
        cit = sorted(set(int(x) for x in re.findall(r"\b(\d{3,4})\b", limpio)))
        print("    entrada defecto: %s" % d["nombre"])
        print("    campo cobertura: %s" % d["cobertura"])
        print("    puestos citados en su nota: %s" % cit)
        clases = []
        for p in cit:
            v = por_puesto.get(p)
            clases.append((p, v["clase"] if v else "NO EXISTE"))
        print("    clase de cada uno HOY: %s" % clases)
        # la nota separa la cola de la que CAE: el 751 sale por LD-59
        mcae = re.search(r"UNA CAE: el (\d+)", d["nota"])
        cae = int(mcae.group(1)) if mcae else None
        cola_p = [p for p in cit if p != cae]
        print("    LA COLA, segun la nota (los citados menos el que CAE): %d  %s" % (
            len(cola_p), cola_p))
        print("      en B: %s" % [p for p, c in clases if c == "B" and p != cae])
        print("      en A: %s (excepcion escrita en 08_VERIFICACION.md)" % [
            p for p, c in clases if c == "A" and p != cae])
        print("    EL QUE CAE por LD-59: %s, clase hoy %s, fuera de la cola" % (
            cae, dict(clases).get(cae)))
        print("    la cola medida (%d) calza con el campo cobertura (%s): %s" % (
            len(cola_p), d["cobertura"], str(len(cola_p)) == d["cobertura"].strip()))

    print()
    print("  BLOQUE 2: el criterio del forastero")
    fig_f = [f for f in figuras if "forastero" in f["nombre"].lower()][0]
    print("    figura: %s" % fig_f["nombre"])
    print("    cobertura: %s" % fig_f["cobertura"])
    print("    miembros: %s" % fig_f["miembros"])
    for nid in fig_f["miembros"]:
        pares = [v for v in V if nid in (v["nodo_a"], v["nodo_b"])]
        print("      %-40s pares %2d  clases %s" % (
            nid, len(pares), dict(collections.Counter(v["clase"] for v in pares))))
    print("    candidato condicionado registrado en la nota: %s" % (
        "customer_validation_sales_roadmap" in fig_f["nota"]))

    print()
    print("  BLOQUE 3: el lote de cinco del sales roadmap")
    par = {tuple(sorted((v["nodo_a"], v["nodo_b"]))): v for v in V}
    faltan = [p for p in itertools.combinations(sorted(MIEMBROS_SALES_ROADMAP), 2)
              if p not in par]
    print("    pares posibles de la nomina: %d" % (
        len(list(itertools.combinations(MIEMBROS_SALES_ROADMAP, 2)))))
    print("    pares del acto en el archivo de veredictos: %d" % (
        len(list(itertools.combinations(MIEMBROS_SALES_ROADMAP, 2))) - len(faltan)))
    print("    pares que NO estan en el archivo: %d" % len(faltan))
    for x, y in faltan:
        print("      %s contra %s" % (x, y))
    # una busqueda negativa no se puede citar: se buscan LAS CINCO en TODAS las
    # sedes de lecturas dirigidas, no solo en el indice
    sedes = sorted((RAIZ / "docs" / "plan").glob("LD_*.md")) + [
        RAIZ / "docs" / "plan" / "LECTURAS_DIRIGIDAS.md"]
    textos = {p.name: p.read_text(encoding="utf-8") for p in sedes}
    for k in range(66, 71):
        donde = [nom for nom, t in textos.items() if ("LD-%d" % k) in t]
        print("    LD-%d escrita en: %s" % (k, donde or "NINGUNA SEDE"))

    print()
    print("  BLOQUE 4: las lecturas de acto entero de P.5")
    actos_todos = [e for e in inv if e.get("tipo") == "acto"]
    superadas = [e for e in actos_todos
                 if (e.get("estado") or "").upper().startswith("SUPERADA")]
    actos = [e for e in actos_todos if e not in superadas]
    rxc = re.compile(r"(\d+)\s+en\s+cola", re.I)
    rxf = re.compile(r"(\d+)\s+fuera\s+de\s+cola", re.I)
    est = collections.Counter()
    cola = fuera = 0
    for e in actos:
        s = (e.get("estado") or "").upper()
        est["CERRADO" if "CERRADO" in s else ("ABIERTO" if "ABIERTO" in s else "otro")] += 1
        cov = e.get("cobertura") or ""
        mc, mf = rxc.search(cov), rxf.search(cov)
        cola += int(mc.group(1)) if mc else 0
        fuera += int(mf.group(1)) if mf else 0
    print("    actos: %d (superadas %d, vigentes %d)" % (
        len(actos_todos), len(superadas), len(actos)))
    print("    vigentes CERRADOS %d, ABIERTOS %d, otro %d" % (
        est["CERRADO"], est["ABIERTO"], est["otro"]))
    print("    deuda de P.5 por el campo cobertura: %d en cola, %d fuera, TOTAL %d" % (
        cola, fuera, cola + fuera))

    print()
    print("  BLOQUE 5: los ejemplares de las veinte figuras")
    senal_id = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){2,}\b")
    senal_puesto = re.compile(r"\bpuestos?\s+\d{2,4}\b", re.IGNORECASE)
    senal_ld = re.compile(r"\bLD-\d+\b")
    forma = [f for f in figuras
             if senal_id.search(f["nota"]) or senal_puesto.search(f["nota"])
             or senal_ld.search(f["nota"])]
    marcas = ("EJEMPLARES NOMBRADOS EL", "SEDES NOMBRADAS EL")
    tanda = [f for f in figuras if any(m in f["nota"] for m in marcas)]
    print("    figuras: %d" % len(figuras))
    print("    cuenta de FORMA (id, puesto o LD-nn en la nota): %d de %d" % (
        len(forma), len(figuras)))
    print("    cuenta de TANDA (marca explicita de nombramiento): %d de %d" % (
        len(tanda), len(figuras)))
    print("    las que NO traen marca de tanda:")
    for f in figuras:
        if f not in tanda:
            print("      %s" % f["nombre"])

    # ------------------------------------------------------------------ 4
    titulo("4. EL INVENTARIO ENTERO")
    print("  entradas: %d" % len(inv))
    for t, c in sorted(collections.Counter(e.get("tipo") for e in inv).items()):
        print("    %-16s %d" % (t, c))

    # ------------------------------------------------------------------ 5
    titulo("5. LA LISTA B: las cifras publicadas con DOS LECTURAS, leidas hoy")
    fu = (RAIZ / "docs" / "plan" / "01_FUENTES.md").read_text(encoding="utf-8")
    rec = (RAIZ / "docs" / "plan" / "RECOMPUTO_3388.md").read_text(encoding="utf-8")
    rac = [e for e in inv if e.get("tipo") == "racimo"
           and e.get("nombre") == "el sales roadmap"][0]
    acto_sr = [e for e in actos
               if e.get("nombre") == "customer_validation_sales_roadmap"][0]
    comp_sr = [c for c in comp
               if "customer_validation_sales_roadmap" in c["miembros"]][0]
    fig_oficio = [f for f in figuras if f["nombre"] == "EL PASO DE OFICIO"][0]
    fig_firma = [f for f in figuras
                 if f["nombre"].startswith("LA FIRMA POSICIONAL")][0]

    print("  B1. el acto del sales roadmap, entrada de acto contra entrada de racimo")
    print("      acto,   cobertura: %s" % acto_sr["cobertura"][:110])
    print("      acto,   estado:    %s" % acto_sr["estado"][:110])
    print("      racimo, cobertura: %s" % rac["cobertura"][:110])
    print("      racimo, estado:    %s" % (rac.get("estado") or "(sin campo estado)")[:110])
    print("      racimo, forma:     %s" % rac.get("forma"))
    print()
    print("  B2. el mismo acto, entrada de acto contra COMPONENTES.jsonl (foto del corte)")
    print("      COMPONENTES: leidos %d de %d, en cola %d, fuera %d, estado %s" % (
        comp_sr["leidos"], comp_sr["posibles"], comp_sr["en_cola_sin_leer"],
        comp_sr["fuera_de_cola"], comp_sr["estado"]))
    inc = [c for c in comp if c["leidos"] < c["posibles"]]
    print("      deuda total por COMPONENTES: %d" % sum(
        c["posibles"] - c["leidos"] for c in inc))
    print("      deuda total por el inventario: %d" % (cola + fuera))
    print("      leyenda de la diferencia escrita en RECOMPUTO_3388.md: %s" % (
        "Quien cite 329 tiene que decir de que sede sale" in rec))
    print()
    print("  B3. la cota de EL PASO DE OFICIO: 6 de la vuelta 18 contra 26 corregida")
    print("      medidas hoy: vuelta 18 -> %d nodos, %d en paso 1, %d pares" % (
        len(resultados["vuelta 18"][0]), len(resultados["vuelta 18"][1]),
        len(resultados["vuelta 18"][2])))
    print("      medidas hoy: corregida -> %d nodos, %d en paso 1, %d pares" % (
        len(resultados["corregida"][0]), len(resultados["corregida"][1]),
        len(resultados["corregida"][2])))
    print("      la nota de la figura dice VIGENTE la corregida: %s" % (
        "COTA VIGENTE" in fig_oficio["nota"]))
    print()
    print("  B4. la tanda de los cuatro libros: 43 publicado contra 44 medido")
    print("      01_FUENTES.md trae la correccion declarada del 14 ago 2026: %s" % (
        "44" in fu and "CORRECCION DECLARADA" in fu))
    print("      la nota de LA FIRMA POSICIONAL apunta a la nomina: %s" % (
        "NOMINA DE LOS 14" in fig_firma["nota"] or "nomina de los 14" in fig_firma["nota"]))
    print()
    print("  B5. el rotulo del RECOMPUTO: 9 entradas tocadas contra 8 entradas y 9 ediciones")
    print("      la aclaracion de EDICIONES sobre 8 entradas esta escrita: %s" % (
        "EDICIONES" in rec))
    print()
    print("  B6. LD-04 contra LD-71: el numero del par")
    indice = textos["LECTURAS_DIRIGIDAS.md"]
    i = indice.find("`LD-04`")
    j = indice.find("`LD-05`")
    entrada_04 = indice[i:j] if 0 <= i < j else ""
    print("      la entrada de LD-04 apunta a LD_ESTRELLA_DISRUPTIVAS.md: %s" % (
        "LD_ESTRELLA_DISRUPTIVAS" in entrada_04))
    print("      la entrada de LD-04 fecha la relectura del 14 ago 2026: %s" % (
        "14 ago 2026" in entrada_04))
    print("      LD-71 buscada en TODAS las sedes de dirigidas: %s" % (
        [nom for nom, t in textos.items() if "LD-71" in t] or "NINGUNA SEDE"))
    print()
    print("  B7. decision_de_vender_startup: cuantos pasos, censo de TODAS las sedes")
    x = vivos.get("decision_de_vender_startup")
    m = re.search(r"decision_de_vender_startup`\*\*\s*\|\s*\*\*(\d+) pasos", fu)
    print("      MEDIDO HOY en el grafo: %d pasos" % len(x["pasos_accionables"]))
    print("      01_FUENTES.md, tabla LOS TRES CASOS: %s pasos" % (
        m.group(1) if m else "no localizado"))
    # una busqueda negativa no se puede citar: se barre docs/ entero
    censo = collections.defaultdict(list)
    for p in sorted((RAIZ / "docs").rglob("*")):
        if not p.is_file() or p.suffix.lower() not in (".md", ".jsonl"):
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if "decision_de_vender_startup" not in t:
            continue
        for mm in re.finditer(r"decision_de_vender_startup.{0,160}?(\d+)\s*pasos", t, re.S):
            censo[mm.group(1)].append(str(p.relative_to(RAIZ)))
        # y las tablas donde la cifra vive en una columna rotulada pasos: se usa
        # la cabecera INMEDIATAMENTE ANTERIOR a la fila, no la primera del archivo
        cabeceras = [(mm.start(),
                      [c.strip() for c in mm.group(0).strip().strip("|").split("|")])
                     for mm in re.finditer(r"^\|.*\|\s*$", t, re.M)
                     if "pasos" in [c.strip()
                                    for c in mm.group(0).strip().strip("|").split("|")]]
        for mm in re.finditer(r"^\|.*decision_de_vender_startup.*\|\s*$", t, re.M):
            celdas = [c.strip() for c in mm.group(0).strip().strip("|").split("|")]
            previas = [c for pos, c in cabeceras if pos < mm.start()]
            if not previas:
                continue
            cols = previas[-1]
            if len(cols) != len(celdas):
                continue
            celda = celdas[cols.index("pasos")]
            if celda.isdigit():
                censo[celda].append(str(p.relative_to(RAIZ)))
    for cuantos in sorted(censo, key=int):
        sedes_c = sorted(set(censo[cuantos]))
        print("      sedes que dicen %s pasos: %d  %s" % (
            cuantos, len(sedes_c), sedes_c))

    # ------------------------------------------------------------------ 6
    titulo("6. LO RESERVADO")
    print("  lineas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    print("  nodos en dataset/metadata/master_graph.json: %d (vivos %d)" % (
        len(nodos), len(vivos)))
    print("  componentes en RECOMPUTO_3388_COMPONENTES.jsonl: %d" % len(comp))
    print("  operaciones en OPERACIONES.jsonl: %d" % len(
        jsonl("docs", "plan", "OPERACIONES.jsonl")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
