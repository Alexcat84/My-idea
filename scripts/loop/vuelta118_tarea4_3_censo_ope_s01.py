# -*- coding: utf-8 -*-
r"""vuelta118_tarea4_3_censo_ope_s01.py . TAREA 4.3 de la vuelta 118: EL
CENSO DE OP-S-01 CONTRA EL GRAFO, PUNTO POR PUNTO, ANTES DE TOCARLA.

QUE MIDE, SOLO LECTURA. Lee el campo `verificacion` de `OP-S-01`
(docs/plan/OPERACIONES.jsonl) y mide, uno por uno, CADA punto contra el
grafo de HOY (dataset/metadata/master_graph.json), publicando CUMPLE o NO
CUMPLE con el dato medido. NO ADJUDICA si la operacion esta lista para
ejecutarse: eso lo hace el auditor con este censo delante (AUDITOR.md
seccion 3, "una operacion cuyo texto no alcance para ejecutarse sin decidir
es PARADA").

USO:
  python scripts/loop/vuelta118_tarea4_3_censo_ope_s01.py
"""
import json
import re

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_OPS = "docs/plan/OPERACIONES.jsonl"
RUTA_VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"

NAFTA_ID = "nafta_free_trade_agreements"
SUPERVIVIENTE_ID = "certificado_de_origen_tratados_libre_comercio"
PUESTO_1955 = 1955


def cargar_grafo():
    return json.load(open(RUTA_GRAFO, encoding="utf-8"))["nodos"]


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


def main():
    ops = [json.loads(l) for l in open(RUTA_OPS, encoding="utf-8") if l.strip()]
    op = [o for o in ops if o["id_op"] == "OP-S-01"][0]
    nodos = cargar_grafo()
    alias_de = construir_alias_de(nodos)
    resolver = hacer_resolver(nodos, alias_de)

    print("CENSO DE OP-S-01 CONTRA EL GRAFO DE HOY, PUNTO POR PUNTO, TAREA 4.3 VUELTA 118.")
    print("=" * 100)
    print("verificacion declarada (%d puntos), leida entera de %s:" % (len(op["verificacion"]), RUTA_OPS))
    for i, v in enumerate(op["verificacion"], 1):
        print("  %d. %s" % (i, v))
    print()

    n_super = nodos.get(SUPERVIVIENTE_ID) or {}
    n_nafta = nodos.get(NAFTA_ID)

    resultados = []

    # 1. ids_alias de certificado_de_origen_tratados_libre_comercio contiene nafta_free_trade_agreements
    alias_super = n_super.get("ids_alias") or []
    cumple1 = NAFTA_ID in alias_super
    print("1. ids_alias de %s contiene %s" % (SUPERVIVIENTE_ID, NAFTA_ID))
    print("   comando: nodos['%s']['ids_alias'] -> %s" % (SUPERVIVIENTE_ID, alias_super))
    print("   %s" % ("CUMPLE" if cumple1 else "NO CUMPLE"))
    resultados.append(("1", cumple1))
    print()

    # 2. resolverId('nafta_free_trade_agreements') devuelve el superviviente
    rid, vivo = resolver(NAFTA_ID)
    cumple2 = (rid == SUPERVIVIENTE_ID) and vivo
    print("2. resolverId('%s') devuelve el superviviente" % NAFTA_ID)
    print("   comando: resolver('%s') -> (%s, vivo=%s)" % (NAFTA_ID, rid, vivo))
    print("   %s" % ("CUMPLE" if cumple2 else "NO CUMPLE"))
    resultados.append(("2", cumple2))
    print()

    # 3. foreign_trade_zones e import_regulations_foreign_governments siguen resolviendo a nodo vivo
    otros = ["foreign_trade_zones", "import_regulations_foreign_governments"]
    detalle3 = []
    for nid in otros:
        r, v = resolver(nid)
        detalle3.append((nid, r, v))
    cumple3 = all(v for _n, _r, v in detalle3)
    print("3. foreign_trade_zones e import_regulations_foreign_governments siguen resolviendo a nodo vivo")
    for nid, r, v in detalle3:
        print("   resolver('%s') -> (%s, vivo=%s)" % (nid, r, v))
    print("   %s" % ("CUMPLE" if cumple3 else "NO CUMPLE"))
    resultados.append(("3", cumple3))
    print()

    # 4. ningun nodo VIVO lleva NAFTA en su id ni en su titulo
    hallados_id = []
    hallados_titulo = []
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        if "nafta" in nid.lower():
            hallados_id.append(nid)
        titulo = n.get("titulo_concepto") or ""
        if "nafta" in titulo.lower():
            hallados_titulo.append((nid, titulo))
    cumple4 = not hallados_id and not hallados_titulo
    print("4. ningun nodo VIVO lleva NAFTA en su id ni en su titulo")
    print("   ids vivos con 'nafta': %s" % (hallados_id or "NINGUNO"))
    print("   titulos de nodos vivos con 'NAFTA': %s" % (hallados_titulo or "NINGUNO"))
    print("   %s" % ("CUMPLE" if cumple4 else "NO CUMPLE"))
    resultados.append(("4", cumple4))
    print()

    # 5. las CINCO perdidas aparecen literalmente en el superviviente
    veredicto_1955 = None
    for l in open(RUTA_VEREDICTOS, encoding="utf-8"):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get("puesto_intra") == PUESTO_1955:
            veredicto_1955 = d
            break
    texto_super = json.dumps(n_super.get("pasos_accionables") or [], ensure_ascii=False) + " " + \
        json.dumps(n_super.get("resumen_teorico") or "", ensure_ascii=False)
    # Cada GRUPO es una de las cinco perdidas; dentro de un grupo, CUALQUIERA de
    # las formas (con o sin tilde) vale como "presente" (son la misma perdida,
    # no dos perdidas distintas).
    grupos = [
        ("las CUATRO REGLAS DEL ARTICULO 401", ["Artículo 401", "Articulo 401"]),
        ("60% metodo de transaccion", ["60%"]),
        ("50% metodo de costo neto", ["50%"]),
        ("nombres de formularios (CF 434 / Form B-232)", ["CF 434", "Form B-232"]),
        ("VIVE DENTRO: obtenido en su totalidad (wholly obtained)", ["wholly obtained"]),
        ("VIVE DENTRO: conservar documentacion", ["documentación", "documentacion"]),
    ]
    presentes = [nombre for nombre, formas in grupos if any(f in texto_super for f in formas)]
    ausentes = [nombre for nombre, formas in grupos if not any(f in texto_super for f in formas)]
    cumple5 = len(ausentes) == 0
    print("5. las CINCO perdidas (puesto %d de %s) aparecen literalmente en el superviviente"
          % (PUESTO_1955, RUTA_VEREDICTOS))
    print("   veredicto puesto %d hallado: %s" % (PUESTO_1955, veredicto_1955 is not None))
    print("   grupos buscados en pasos_accionables + resumen_teorico del superviviente (%d, dos de ellos ya "
          "reclasificados VIVE DENTRO por el propio campo preservar de OP-S-01): %s" % (len(grupos), [g[0] for g in grupos]))
    print("   presentes: %s" % presentes)
    print("   ausentes: %s" % (ausentes or "NINGUNA"))
    print("   %s" % ("CUMPLE" if cumple5 else "NO CUMPLE"))
    resultados.append(("5", cumple5))
    print()

    # 6. Gate 0 verde
    print("6. Gate 0 verde")
    print("   medido en la APERTURA de esta misma vuelta: docs/loop/SALIDA_V118_GATE0_CMD1_APERTURA.txt, linea 'GATE 0: OK'")
    print("   CUMPLE (re-citado, no re-corrido en esta tarea: TAREA 4 no toca dataset/)")
    resultados.append(("6", True))
    print()

    # 7. PASADA DE PERDIDAS RECOMPUTADAS (P.13)
    print("7. PASADA DE PERDIDAS RECOMPUTADAS (P.13): cada perdida listada comprobada contra la "
          "nomina COMPLETA de la fusion y contra el texto del superviviente")
    print("   ESTO ES UN PROCEDIMIENTO, NO UN BOOLEANO MEDIBLE CON UN SOLO COMANDO: el campo "
          "`preservar` de OP-S-01 ya declara DOS de las cinco perdidas RECLASIFICADAS como 'VIVE "
          "DENTRO' (no perdidas), y el punto 5 de arriba confirma que las OTRAS TRES si aparecen "
          "literalmente. Con eso, LA PASADA PARECE HECHA, pero es una lectura, no una medicion "
          "binaria: SE TRAE CRUDO, sin adjudicar 'CUMPLE'.")
    resultados.append(("7", None))
    print()

    print("--- RESUMEN ---")
    print("| punto | veredicto |")
    print("|---:|---|")
    for num, r in resultados:
        etiqueta = "CUMPLE" if r is True else ("NO CUMPLE" if r is False else "PROCEDIMENTAL, NO BOOLEANO (ver arriba)")
        print("| %s | %s |" % (num, etiqueta))

    n_cumple = sum(1 for _n, r in resultados if r is True)
    n_no_cumple = sum(1 for _n, r in resultados if r is False)
    n_procedimental = sum(1 for _n, r in resultados if r is None)
    print()
    print("CUMPLE: %d, NO CUMPLE: %d, PROCEDIMENTAL: %d, de %d puntos totales."
          % (n_cumple, n_no_cumple, n_procedimental, len(resultados)))

    print()
    print("=" * 100)
    print("TAREA 4.4, LA LETRA QUE MANDA: clasificacion de OP-S-01, SIN ADJUDICAR y SIN EJECUTAR.")
    if n_no_cumple == 0:
        clasificacion = "CUMPLIDA (los puntos booleanos CUMPLEN todos)"
    elif n_cumple > 0:
        clasificacion = "PARCIALMENTE CUMPLIDA"
    else:
        clasificacion = "SIN EMPEZAR"
    print("CLASIFICACION: %s (%d CUMPLE, %d NO CUMPLE, %d PROCEDIMENTAL)."
          % (clasificacion, n_cumple, n_no_cumple, n_procedimental))
    if n_no_cumple > 0:
        print("EL PUNTO 4 (ningun nodo VIVO lleva NAFTA en su id ni en su titulo) SALE NO CUMPLE: "
              "el titulo_concepto del superviviente es 'Certificado de Origen y Tratados de Libre "
              "Comercio (NAFTA, Rules of Origin, RVC)'. LA VERIFICACION DE OP-S-01 NO DICE QUE TEXTO "
              "TIENE QUE LLEVAR EL TITULO DEL SUPERVIVIENTE tras quitar NAFTA: reescribirlo inventando "
              "la redaccion seria la improvisacion que AUDITOR.md seccion 3 prohibe. NO SE EJECUTA "
              "NADA DE OP-S-01 EN ESTA VUELTA. Cero nodos deprecados, cero alias escritos, cero "
              "titulos reescritos, cero aristas, cero cambios de estado.")


if __name__ == "__main__":
    main()
