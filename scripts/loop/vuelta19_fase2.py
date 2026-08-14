# -*- coding: utf-8 -*-
"""VUELTA 19: la FASE II medida bloque por bloque, al cierre. SOLO LECTURA.

Mide los CINCO bloques que la vuelta 17 dejo nombrados, mas el estado del bloque
grande (los ejemplares de las veinte figuras) DESPUES del trabajo de esta vuelta,
y ademas cruza las TRES sedes que hoy hablan del mismo acto del sales roadmap
para que sus divergencias se vean en vez de suponerse.

No escribe nada y no cierra nada: mide, y quien cierra la FASE II es el auditor.
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


def jsonl(*p):
    with open(RAIZ.joinpath(*p), encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def titulo(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


def main():
    inv = jsonl("docs", "plan", "INVENTARIO.jsonl")
    V = jsonl("docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
    comp = jsonl("docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
    figuras = [e for e in inv if e.get("tipo") == "figura"]

    titulo("BLOQUE GRANDE: los ejemplares de las veinte figuras")
    # el criterio de FORMA de la vuelta 17, reproducido tal cual, con su limite
    senal_id = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){2,}\b")
    senal_puesto = re.compile(r"\bpuestos?\s+\d{2,4}\b", re.IGNORECASE)
    senal_ld = re.compile(r"\bLD-\d+\b")
    forma = [f for f in figuras
             if senal_id.search(f["nota"]) or senal_puesto.search(f["nota"])
             or senal_ld.search(f["nota"])]
    print("  criterio de FORMA de la vuelta 17: %d de %d figuras nombran" % (
        len(forma), len(figuras)))
    # el criterio SUSTANTIVO: la nota trae la marca de una tanda de nombramiento
    marca = "EJEMPLARES NOMBRADOS EL"
    marca2 = "SEDES NOMBRADAS EL"
    nombradas = [f for f in figuras if marca in f["nota"] or marca2 in f["nota"]]
    print("  con marca explicita de tanda de nombramiento: %d" % len(nombradas))
    for f in figuras:
        m = "SI " if (marca in f["nota"] or marca2 in f["nota"]) else "no "
        print("    %s %-42s %s" % (m, f["nombre"], f["cobertura"]))

    titulo("BLOQUE: las lecturas de acto entero de P.5, y las TRES sedes que lo cuentan")
    actos = [e for e in inv if e.get("tipo") == "acto"
             and "superada" not in (e.get("estado") or "").lower()]
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
    print("  SEDE 1, INVENTARIO.jsonl, actos vigentes: %d" % len(actos))
    print("    CERRADOS %d, ABIERTOS %d, otro %d" % (
        est["CERRADO"], est["ABIERTO"], est["otro"]))
    print("    deuda de P.5 leida del campo cobertura: %d en cola, %d fuera, TOTAL %d" % (
        cola, fuera, cola + fuera))
    ab = [c for c in comp if c["estado"] == "ABIERTO"]
    ce = [c for c in comp if c["estado"] == "CERRADO"]
    inc = [c for c in comp if c["leidos"] < c["posibles"]]
    print("  SEDE 2, RECOMPUTO_3388_COMPONENTES.jsonl: %d componentes" % len(comp))
    print("    CERRADOS %d, ABIERTOS %d" % (len(ce), len(ab)))
    print("    pares que faltan: %d (en cola %d, fuera %d)" % (
        sum(c["posibles"] - c["leidos"] for c in inc),
        sum(c["en_cola_sin_leer"] for c in inc),
        sum(c["fuera_de_cola"] for c in inc)))
    rac = [e for e in inv if e.get("tipo") == "racimo"
           and e.get("nombre") == "el sales roadmap"]
    for r in rac:
        print("  SEDE 3, entrada de tipo racimo el sales roadmap: cobertura %s, forma %s" % (
            r["cobertura"], r["forma"]))
    csr = [c for c in comp
           if "customer_validation_sales_roadmap" in c["miembros"]]
    for c in csr:
        print("  el acto del sales roadmap en la SEDE 2: leidos %d de %d, en cola %d, "
              "fuera %d, estado %s" % (c["leidos"], c["posibles"],
                                       c["en_cola_sin_leer"], c["fuera_de_cola"],
                                       c["estado"]))
    a = [e for e in actos if e["nombre"] == "customer_validation_sales_roadmap"]
    for e in a:
        print("  el mismo acto en la SEDE 1: %s" % e["cobertura"][:96])

    titulo("BLOQUE: el criterio del forastero")
    fig = [f for f in figuras if "forastero" in f["nombre"].lower()][0]
    print("  cobertura: %s | miembros: %s" % (fig["cobertura"], fig["miembros"]))
    for nid in fig["miembros"]:
        pares = [v for v in V if nid in (v["nodo_a"], v["nodo_b"])]
        print("    %-40s pares en el archivo %d, clases %s" % (
            nid, len(pares),
            dict(collections.Counter(v["clase"] for v in pares))))
    print("  candidato condicionado registrado en esta vuelta: %s" % (
        "customer_validation_sales_roadmap" in fig["nota"]))

    titulo("BLOQUE: la cola de relectura post fusion, y el lote del sales roadmap")
    defecto = [e for e in inv if e.get("tipo") == "defecto"
               and "fusion reabre" in (e.get("nombre") or "")]
    for d in defecto:
        # se descartan las fechas: un 2026 detras de un mes no es un puesto
        limpio = re.sub(r"\b(?:ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+\d{4}\b",
                        " ", d["nota"])
        puestos = sorted(set(int(x) for x in re.findall(r"\b(\d{3,4})\b", limpio)))
        print("  entrada defecto %s: puestos citados en su nota %s" % (
            d["nombre"], puestos))
        for p in puestos:
            v = [x for x in V if x["puesto_intra"] == p]
            print("     puesto %-5d clase hoy %s" % (p, v[0]["clase"] if v else "NO EXISTE"))
    M = ["customer_validation_sales_roadmap", "estrategia_de_ventas",
         "hoja_de_ruta_de_ventas", "refinar_sales_roadmap", "sales_roadmap",
         "sales_roadmap_vs_sales_force"]
    par = {tuple(sorted((v["nodo_a"], v["nodo_b"]))): v for v in V}
    faltan = [p for p in itertools.combinations(sorted(M), 2) if p not in par]
    print("  pares del acto del sales roadmap que siguen FUERA del archivo: %d" % len(faltan))
    for x, y in faltan:
        print("     %s contra %s" % (x, y))
    print("  (los cinco estan leidos como dirigidas LD-66 a LD-70; el archivo de")
    print("   veredictos no los recoge y no debe recogerlos)")

    titulo("EL MARCADOR Y LO RESERVADO, al cierre de la vuelta")
    print("  lineas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    cl = collections.Counter(v["clase"] for v in V)
    print("  A %d, B %d, C %d, D %d" % (cl["A"], cl["B"], cl["C"], cl["D"]))
    print("  entradas de docs/plan/INVENTARIO.jsonl: %d" % len(inv))
    print("  tipos: %s" % dict(collections.Counter(e.get("tipo") for e in inv)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
