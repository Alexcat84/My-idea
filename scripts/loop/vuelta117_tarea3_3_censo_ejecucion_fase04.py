# -*- coding: utf-8 -*-
r"""vuelta117_tarea3_3_censo_ejecucion_fase04.py . TAREA 3.3 de la vuelta
117, encargo del auditor (acta de la vuelta 116).

QUE MIDE, SOLO LECTURA, CERO ADJUDICACION. Para las DIEZ operaciones de la
fase 04_ENLACES (docs/plan/OPERACIONES.jsonl), leyendo la NOTA de cada una
entera (letra nueva del encargo de la 117: "ANTES DE PREGUNTAR SI UNA
OPERACION SE PUEDE EJECUTAR, SE LEE SU PROPIA NOTA"):

  (1) si trae ADDENDUM DE EJECUCION (con su fecha y su vuelta, leidas del
      propio texto de la nota).
  (2) si trae registro de cierre en la pagina docs/plan/04_ENLACES.md
      (encabezado que cita el id de la operacion y una palabra de cierre:
      CERRADA, SELLADA, EJECUTADA ENTERA, HECHO), con su linea medida hoy.
  (3) que aristas escribio DE VERDAD segun el grafo de hoy
      (dataset/metadata/master_graph.json), resolviendo alias con la misma
      replica del resolvedor de la casa que usa
      scripts/loop/vuelta117_tarea3_1_criterio_hecho_tres_fuentes.py
      (_resolver de scripts/run_phase1.py:989-1009). Las fuentes:
        OP-E-01: las 98 ESCRITA de docs/plan/OP_E_01_DECIDIDAS.jsonl
        OP-E-06: las 114 de docs/plan/OP_E_06_DIRECCION_V90.jsonl
        OP-E-07: las 84 del ULTIMO OP_E_07_DIRECCION_V94.jsonl
        OP-E-02, OP-E-03: `aristas_nuevas` vacio en OPERACIONES.jsonl, nada
          que resolver por esta via (OP-E-03 es LECTURA, no escritura de
          aristas; su registro vive en docs/plan/OP_E_03_LECTURA_*.jsonl)
        las otras cinco (OP-E-04, OP-E-05, OP-M-01-ESLABONES,
          OP-M-01-SEXTO, OP-M-03-ENLACES): pares "madre -> hijo" EXTRAIDOS
          por regex del texto libre de `aristas_nuevas` en OPERACIONES.jsonl
          (no son un JSONL aparte: son prosa con la flecha "->")

NO ADJUDICA NADA: no decide si la operacion es ejecutable ni que le falta.
Eso es la adjudicacion del auditor.

USO:
  python scripts/loop/vuelta117_tarea3_3_censo_ejecucion_fase04.py
"""
import json
import re

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
RUTA_PAGINA = "docs/plan/04_ENLACES.md"
RUTA_DECIDIDAS = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
RUTA_E06 = "docs/plan/OP_E_06_DIRECCION_V90.jsonl"
RUTA_E07 = "docs/plan/OP_E_07_DIRECCION_V94.jsonl"

PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO")
RE_NODE_ID = r"[a-z][a-z0-9_]{2,}"
RE_FLECHA = re.compile(r"(%s)\s*->\s*(%s)" % (RE_NODE_ID, RE_NODE_ID))


def cargar_grafo():
    g = json.load(open(RUTA_GRAFO, encoding="utf-8"))
    return g["nodos"]


def construir_alias_de(nodos):
    alias_de = {}
    for nid, n in nodos.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias_de[a] = nid
    return alias_de


def hacer_resolver(nodos, alias_de):
    def resolver(nid):
        n = nodos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid, True
        visto = {nid}
        cur = nid
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = nodos.get(cur)
            if c is None:
                continue
            if not c.get("deprecado"):
                return cur, True
        return nid, False
    return resolver


def presente(m, h, nodos, resolver):
    rm, vivo_m = resolver(m)
    rh, vivo_h = resolver(h)
    if not vivo_m or not vivo_h:
        return False, "extremo(s) sin id vivo"
    n_madre = nodos.get(rm) or {}
    n_hijo = nodos.get(rh) or {}
    sig = rh in (n_madre.get("nodos_siguientes") or [])
    prev = rm in (n_hijo.get("nodos_previos") or [])
    return (sig and prev), ("sig=%s prev=%s" % (sig, prev))


def leer_pares_jsonl(ruta, filtro_decision=None):
    filas = [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]
    if filtro_decision:
        filas = [f for f in filas if f.get("decision") == filtro_decision]
    return [(f["madre"], f["hijo"]) for f in filas]


def leer_pares_prosa(aristas_nuevas):
    pares = []
    for entrada in aristas_nuevas or []:
        pares.extend(RE_FLECHA.findall(entrada))
    return pares


def cargar_ops():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    return {o["id_op"]: o for o in ops if o.get("fase") == "04_ENLACES"}


def encabezados(lineas):
    out = []
    for i, l in enumerate(lineas, start=1):
        if re.match(r"^#{1,4}\s", l):
            out.append((i, l.rstrip("\n")))
    return out


def registro_en_pagina(oid, lineas_encab):
    return [(n, t) for n, t in lineas_encab if oid in t and any(p in t for p in PALABRAS_CIERRE)]


def main():
    ops = cargar_ops()
    nodos = cargar_grafo()
    alias_de = construir_alias_de(nodos)
    resolver = hacer_resolver(nodos, alias_de)
    lineas_pagina = open(RUTA_PAGINA, encoding="utf-8").readlines()
    lineas_encab = encabezados(lineas_pagina)

    orden = ["OP-E-01", "OP-E-02", "OP-E-03", "OP-E-04", "OP-E-05", "OP-E-06", "OP-E-07",
             "OP-M-01-ESLABONES", "OP-M-01-SEXTO", "OP-M-03-ENLACES"]

    print("CENSO DE EJECUCION DE LA FASE 04, LEYENDO LA NOTA DE CADA UNA DE LAS DIEZ, TAREA 3.3 VUELTA 117.")
    print("=" * 100)
    print()

    resumen = []
    for oid in orden:
        o = ops[oid]
        nota = o.get("nota") or ""
        estado = o.get("estado")
        print("--- %s (estado=%s) ---" % (oid, estado))

        idx = nota.find("ADDENDUM DE EJECUCION")
        if idx == -1:
            print("(1) ADDENDUM DE EJECUCION: NO")
            addendum = False
        else:
            cita = nota[idx:idx + 200].strip()
            m = re.search(r"(\d{1,2} \w+ 2026)\s*\(vuelta (\d+)\)", nota[max(0, idx - 60):idx + 200])
            fv = "%s, vuelta %s" % (m.group(1), m.group(2)) if m else "fecha/vuelta no parseada del texto"
            print("(1) ADDENDUM DE EJECUCION: SI (%s) -- \"%s\"" % (fv, cita))
            addendum = True

        reg = registro_en_pagina(oid, lineas_encab)
        if reg:
            print("(2) registro de cierre en %s: SI, %d cita(s):" % (RUTA_PAGINA, len(reg)))
            for n, t in reg:
                print("    %s:%d -- %s" % (RUTA_PAGINA, n, t.strip()))
        else:
            print("(2) registro de cierre en %s: NO" % RUTA_PAGINA)

        if oid == "OP-E-01":
            pares = leer_pares_jsonl(RUTA_DECIDIDAS, filtro_decision="ESCRITA")
            fuente = "%s (98 ESCRITA)" % RUTA_DECIDIDAS
        elif oid == "OP-E-06":
            pares = leer_pares_jsonl(RUTA_E06)
            fuente = RUTA_E06
        elif oid == "OP-E-07":
            pares = leer_pares_jsonl(RUTA_E07)
            fuente = "%s (ULTIMO de 4 ficheros V91-V94)" % RUTA_E07
        elif oid in ("OP-E-02", "OP-E-03"):
            pares = []
            fuente = "aristas_nuevas vacio en OPERACIONES.jsonl (%s)" % (
                "OP-E-03 es LECTURA, no escritura de aristas" if oid == "OP-E-03" else "OP-E-02 sin aristas propias")
        else:
            pares = leer_pares_prosa(o.get("aristas_nuevas"))
            fuente = "prosa de aristas_nuevas en OPERACIONES.jsonl, %d entrada(s), %d par(es) extraidos por regex" % (
                len(o.get("aristas_nuevas") or []), len(pares))

        if not pares:
            print("(3) aristas segun el grafo: 0 par(es) a resolver -- fuente: %s" % fuente)
        else:
            n_pres = 0
            detalle = []
            for m, h in pares:
                ok, det = presente(m, h, nodos, resolver)
                if ok:
                    n_pres += 1
                else:
                    detalle.append((m, h, det))
            print("(3) aristas segun el grafo: %d de %d PRESENTES hoy -- fuente: %s" % (n_pres, len(pares), fuente))
            for m, h, det in detalle:
                print("    AUSENTE: %s -> %s (%s)" % (m, h, det))

        resumen.append((oid, estado, addendum, bool(reg), len(pares),
                        sum(1 for m, h in pares if presente(m, h, nodos, resolver)[0])))
        print()

    print("--- RESUMEN ---")
    print("| operacion | estado | addendum ejecucion | registro en pagina | aristas presentes/total |")
    print("|---|---|---|---|---|")
    for oid, estado, addendum, reg, total, pres in resumen:
        print("| %s | %s | %s | %s | %d/%d |" % (
            oid, estado, "SI" if addendum else "NO", "SI" if reg else "NO", pres, total))


if __name__ == "__main__":
    main()
