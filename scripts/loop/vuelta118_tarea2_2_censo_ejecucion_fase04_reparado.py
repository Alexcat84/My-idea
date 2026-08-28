# -*- coding: utf-8 -*-
r"""vuelta118_tarea2_2_censo_ejecucion_fase04_reparado.py . TAREA 2 de la
vuelta 118 (encargo del auditor, acta de la vuelta 117, caida E.2: "UNA
CELDA FALSA POR UNA LISTA DE PALABRAS QUE NO CONTIENE LA PALABRA CIERRE").
REPARA vuelta117_tarea3_3_censo_ejecucion_fase04.py, que es HISTORIA y NO SE
TOCA: este es un fichero NUEVO.

LA CAIDA QUE REPARA. `PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA
ENTERA", "HECHO")` (linea 47 de aquel fichero) no traia la palabra CIERRE, y
por eso `registro_en_pagina()` daba NO para OP-E-03 (04_ENLACES.md:1474, "##
EL CIERRE DE LA LECTURA DE `OP-E-03`...") y se quedaba corto en OP-E-01
(04_ENLACES.md:783, "## `OP-E-01`, CIERRE MEDIDO...", que si traia otras dos
citas por PASO 1/PASO 2 pero no la de cierre real de la operacion entera).

EL REMEDIO (TAREA 2.1/2.2/2.4 del encargo de la 118).
(2.1) EL CRITERIO SE IMPRIME: PALABRAS_CIERRE se imprime con %s desde la
constante.
(2.2) LA LINEA CASADA SE PEGA ENTERA: cada SI trae la o las lineas completas
que casaron, con su numero, ademas del encabezado atribuido (aqui la linea
casada Y el encabezado son la MISMA linea, porque `registro_en_pagina()` mide
sobre encabezados).
(2.4) LA LISTA SE AMPLIA CON "CIERRE" Y SE DECLARA: PALABRAS_CIERRE pasa de 4
a 5 palabras. Al pie de la salida, una linea dice CUANTAS CELDAS DE LA
COLUMNA "registro en pagina" SE MUEVEN respecto de la lista vieja de 4
palabras, y CUALES (comparando ambas listas en la misma corrida, sin volver a
tocar el fichero historico de la 117).

MUTACION DD (scripts/loop/vuelta118_tarea2_6_mutacion_dd.py) prueba el
remedio (2.4) por el LADO ROJO: una copia de este fichero con "CIERRE"
quitado de la lista tiene que volver a imprimir 4 palabras en su cabecera Y
perder al menos una celda de "registro en pagina".

USO:
  python scripts/loop/vuelta118_tarea2_2_censo_ejecucion_fase04_reparado.py
"""
import json
import re

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
RUTA_PAGINA = "docs/plan/04_ENLACES.md"
RUTA_DECIDIDAS = "docs/plan/OP_E_01_DECIDIDAS.jsonl"
RUTA_E06 = "docs/plan/OP_E_06_DIRECCION_V90.jsonl"
RUTA_E07 = "docs/plan/OP_E_07_DIRECCION_V94.jsonl"

PALABRAS_CIERRE_VIEJA_V117 = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO")
PALABRAS_CIERRE = ("CERRADA", "SELLADA", "EJECUTADA ENTERA", "HECHO", "CIERRE")
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


def registro_en_pagina(oid, lineas_encab, palabras):
    return [(n, t) for n, t in lineas_encab if oid in t and any(p in t for p in palabras)]


def main():
    ops = cargar_ops()
    nodos = cargar_grafo()
    alias_de = construir_alias_de(nodos)
    resolver = hacer_resolver(nodos, alias_de)
    lineas_pagina = open(RUTA_PAGINA, encoding="utf-8").readlines()
    lineas_encab = encabezados(lineas_pagina)

    orden = ["OP-E-01", "OP-E-02", "OP-E-03", "OP-E-04", "OP-E-05", "OP-E-06", "OP-E-07",
             "OP-M-01-ESLABONES", "OP-M-01-SEXTO", "OP-M-03-ENLACES"]

    print("CENSO DE EJECUCION DE LA FASE 04, REPARADO, TAREA 2 VUELTA 118.")
    print("=" * 100)
    print("CRITERIO IMPRESO (TAREA 2.1/2.4): PALABRAS_CIERRE (lista ampliada, %d palabra(s)) = %s"
          % (len(PALABRAS_CIERRE), PALABRAS_CIERRE))
    print("  (para contraste en esta misma corrida) PALABRAS_CIERRE_VIEJA_V117 (%d palabra(s)) = %s"
          % (len(PALABRAS_CIERRE_VIEJA_V117), PALABRAS_CIERRE_VIEJA_V117))
    print()

    resumen = []
    resumen_viejo = []
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

        reg = registro_en_pagina(oid, lineas_encab, PALABRAS_CIERRE)
        reg_viejo = registro_en_pagina(oid, lineas_encab, PALABRAS_CIERRE_VIEJA_V117)
        if reg:
            print("(2) registro de cierre en %s (lista ampliada): SI, %d cita(s) -- LINEA CASADA ENTERA:" % (RUTA_PAGINA, len(reg)))
            for n, t in reg:
                print("    %s:%d -- %s" % (RUTA_PAGINA, n, t.strip()))
        else:
            print("(2) registro de cierre en %s (lista ampliada): NO" % RUTA_PAGINA)
        if set(reg) != set(reg_viejo):
            print("    (con la lista VIEJA de 117, %d cita(s): %s)" % (
                len(reg_viejo), [("%s:%d" % (RUTA_PAGINA, n)) for n, _t in reg_viejo]))

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
        resumen_viejo.append((oid, {n for n, _t in reg}, {n for n, _t in reg_viejo}))
        print()

    print("--- RESUMEN (con la lista ampliada, PALABRAS_CIERRE de 5) ---")
    print("| operacion | estado | addendum ejecucion | registro en pagina | aristas presentes/total |")
    print("|---|---|---|---|---|")
    for oid, estado, addendum, reg, total, pres in resumen:
        print("| %s | %s | %s | %s | %d/%d |" % (
            oid, estado, "SI" if addendum else "NO", "SI" if reg else "NO", pres, total))

    print()
    movidas = [oid for oid, lineas_nuevas, lineas_viejas in resumen_viejo if lineas_nuevas != lineas_viejas]
    print("TAREA 2.4: OPERACIONES CUYAS CITAS DE 'registro en pagina' SE MUEVEN (ganan o pierden linea) "
          "respecto de la lista vieja de 117 (4 palabras): %d de %d: %s"
          % (len(movidas), len(resumen_viejo), movidas))
    for oid, lineas_nuevas, lineas_viejas in resumen_viejo:
        if lineas_nuevas != lineas_viejas:
            print("    %s: lista vieja (4 palabras) -> lineas %s | lista ampliada (5 palabras) -> lineas %s"
                  % (oid, sorted(lineas_viejas), sorted(lineas_nuevas)))


if __name__ == "__main__":
    main()
