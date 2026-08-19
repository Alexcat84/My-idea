# -*- coding: utf-8 -*-
"""vuelta38_sellar_planes.py - SELLA LOS DOS PLANES DE FUSION DE OP-D-04.

NO TOCA NI UN NODO. Lo unico que escribe son los dos ficheros de plan bajo
docs/loop/, que son documentacion sellada y no dataset. La fusion NO se ejecuta
en esta vuelta: el encargo del 19 ago 2026 la deja esperando el acta del auditor.

POR QUE ES UN SCRIPT Y NO UN JSON TECLEADO (EJECUTOR.md regla 1, cuarto parrafo:
LA TABLA SE IMPRIME, NO SE TECLEA). Los textos de origen se LEEN de
dataset/nodos/*.json y viajan verbatim al plan; los pasos finales se DERIVAN de
los grupos, no se escriben dos veces; y la particion se comprueba aqui mismo:
cada origen tiene que aparecer exactamente UNA vez. Un plan tecleado a mano es
la especie de caida que las vueltas 31 y 32 pagaron dos veces.

LO QUE EL PLAN LLEVA Y LOS DE ANTES NO, y va dicho porque es lo que esta vuelta
midio (regla 2): el bloque simetrizacion_esperada. El ejecutor de fusiones de la
casa redirige a los vecinos y NO le escribe al superviviente las aristas del
absorbido; quien las escribe es scripts/run_phase1.py en su paso 5, y el
precedente esta medido en el log de la fusion de OP-D-02 (commit 72c718ea:
symmetrize_added trae las dos del superviviente). Se declara la lista ENTERA
para que el dia de la ejecucion la guarda sea exacta y no aproximada.

Uso: python scripts/loop/vuelta38_sellar_planes.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta38_bloques as B

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
DESTINO = os.path.join(RAIZ, "docs", "loop")

CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

FECHA = "2026-08-19"


def nodo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def origenes(mapa):
    """mapa: prefijo -> node_id. Devuelve el diccionario de fichas verbatim."""
    out = {}
    for pref, nid in mapa.items():
        d = nodo(nid)
        for i, p in enumerate(d.get("pasos_accionables") or [], 1):
            out["%s%d" % (pref, i)] = p
        for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
            out["%sC%d" % (pref, i)] = c
    return out


def derivar(grupos):
    return [g["texto"] for g in grupos]


def comprobar_particion(grupos, esperados, etiqueta):
    vistos = []
    for g in grupos:
        vistos.extend(g["origenes"])
    fallos = []
    if len(vistos) != len(set(vistos)):
        rep = sorted(set(x for x in vistos if vistos.count(x) > 1))
        fallos.append("%s: origenes repetidos %s" % (etiqueta, rep))
    faltan = sorted(set(esperados) - set(vistos))
    sobran = sorted(set(vistos) - set(esperados))
    if faltan:
        fallos.append("%s: origenes sin colocar %s" % (etiqueta, faltan))
    if sobran:
        fallos.append("%s: origenes inventados %s" % (etiqueta, sobran))
    return fallos


# ---------------------------------------------------------------------------
# FUSION 1: EL TALLER. reglas_brainstorming absorbe a los otros dos.
# ---------------------------------------------------------------------------
MAPA_T = {"R": "reglas_brainstorming",
          "D": "brainstorming_divergente",
          "E": "brainstorming_efectivo"}
ORI_T = origenes(MAPA_T)

GRUPOS_T = [
    {"origenes": ["D1", "E3"],
     "texto": "Reunir al equipo en un espacio dedicado sin distracciones, formando grupos "
              "donde los participantes se conozcan y tengan confianza mutua para evitar el "
              "escepticismo que reduce la generación de ideas.",
     "motivo": "LAS DOS PIEZAS SON DEL MISMO OBJETO, quien esta en la sala y donde. El "
               "superviviente no dice ni una cosa ni la otra en ninguno de sus cinco pasos, "
               "asi que las dos VIAJAN. Va primero porque en los dos donantes precede a todo "
               "y porque colocarla a la cabeza no mueve ninguno de los cinco pasos del "
               "superviviente entre si."},
    {"origenes": ["R1"],
     "texto": "Definir un enunciado claro del problema centrado en necesidad del cliente",
     "motivo": "VERBATIM del superviviente."},
    {"origenes": ["R2", "D2", "E1", "E2"],
     "texto": "Establecer, visibilizar y hacer cumplir las reglas: diferir el juicio, una "
              "conversación a la vez, mantenerse enfocado en el tema, ir por cantidad antes "
              "que por calidad, ser visual, fomentar ideas locas o descabelladas, y construir "
              "sobre las ideas de otros por encima de generar ideas propias de forma aislada.",
     "motivo": "EL BLOQUE DE REGLAS DE LOS TRES EN UNO. El superviviente ya traia diferir el "
               "juicio, una conversacion a la vez, ir por cantidad, ser visual y las ideas "
               "locas. VIAJAN tres piezas que no tenia: hacerlas VISIBLES, mantenerse enfocado "
               "en el tema, y la regla de construir sobre las ideas de otros, que es la unica "
               "regla del acto que el superviviente no dice en ninguna parte. El procedimiento "
               "de esa ultima no se injerta porque vive en construir_sobre_ideas_ajenas, que "
               "queda VIVO y enlazado por P.10."},
    {"origenes": ["R3"],
     "texto": "Preparar al equipo con una experiencia de inmersión previa (visita de campo, "
              "entrevistas a clientes)",
     "motivo": "VERBATIM del superviviente. Es la pieza que ningun otro miembro del acto "
               "tiene, y la razon del puesto 834 ya la llamo lo mas caro de perder."},
    {"origenes": ["R4", "D4"],
     "texto": "Usar Post-it notes o pizarra para capturar y mover las ideas visualmente",
     "motivo": "MISMO GESTO EN LOS DOS. El superviviente ya capturaba y movia en post-its; "
               "del donante VIAJA solo el otro soporte nombrado, la pizarra."},
    {"origenes": ["R5"],
     "texto": "Opcional: realizar el ejercicio 'Silly Cow' como calentamiento creativo",
     "motivo": "VERBATIM del superviviente."},
    {"origenes": ["D3", "E4"],
     "texto": "Generar el mayor número de ideas posible sin filtrar prematuramente, en "
              "sesiones dedicadas solo a generar opciones (divergencia) y separadas de las "
              "sesiones de selección (convergencia).",
     "motivo": "EL ACTO DE GENERAR Y SU ENCUADRE. El superviviente manda ir por cantidad "
               "dentro de sus reglas pero no tiene paso de generacion, y no dice en ninguna "
               "parte que la sesion de generar vaya separada de la de elegir. Las dos VIAJAN "
               "y van al final porque son lo que se hace despues del calentamiento."},
]

GRUPOS_COND_T = [
    {"origenes": ["RC1", "EC1"],
     "texto": "Cuando el equipo necesita generar gran volumen de ideas en poco tiempo, antes "
              "de tomar decisiones",
     "motivo": "LA MISMA CONDICION DICHA DOS VECES. Del donante VIAJA el para que, antes de "
               "tomar decisiones."},
    {"origenes": ["RC2"],
     "texto": "Si las discusiones se estancan en crítica prematura de ideas",
     "motivo": "VERBATIM del superviviente."},
    {"origenes": ["DC1", "DC2"],
     "texto": "Cuando el equipo necesita explorar múltiples soluciones posibles antes de "
              "comprometerse con una, o el problema aún no tiene una dirección clara de "
              "solución",
     "motivo": "LAS DOS DEL DONANTE, que dicen el mismo momento del proyecto y ninguna de las "
               "dos esta en el superviviente. VIAJAN juntas."},
    {"origenes": ["EC2"],
     "texto": "Cuando el equipo no se conoce bien o carece de confianza para colaborar "
              "espontáneamente",
     "motivo": "VIAJA entera: es la condicion que hace falta para el primer paso del "
               "resultado, y el superviviente no la tenia."},
]

PLAN_TALLER = {
    "operacion": "OP-D-04, FUSION 1 de 2: EL TALLER. reglas_brainstorming absorbe a "
                 "brainstorming_divergente y a brainstorming_efectivo",
    "estado": "SELLADO Y SIN EJECUTAR. La fusion espera el acta del auditor (decision del "
              "fundador, 19 ago 2026): no se ejecuta en la misma vuelta que la decide.",
    "regla": "OP-D-04 (docs/plan/02_DESTEJIDOS.md) con la forma final adjudicada por el "
             "fundador el 19 ago 2026, siete a tres; superviviente por P.8 (el cableado "
             "desempata, no decide) elegido por LECTURA DE CONTENIDO; perdidas repartidas y "
             "reclasificadas por P.13; simulacion previa sobre copia en memoria por P.7; "
             "limpieza de lo que la propia fusion fabrica por P.16.",
    "motivo": "El acto se leyo ENTERO por P.5 (21 de 21, vuelta 37) y resulto ser DOS "
              "triangulos cerrados, un nodo colgado y TRES nodos puente. P.10 prohibe fundir "
              "la componente entera y deja como tercera salida fundir solo el subconjunto "
              "CERRADO y enlazar el resto. Este es el primero de los dos subconjuntos "
              "cerrados: sus tres pares internos son A (puestos 823, 834 y 234).",
    "fecha_corte": FECHA,
    "superviviente": "reglas_brainstorming",
    "absorbidos": ["brainstorming_divergente", "brainstorming_efectivo"],
    "fuente_esperada": "Business Model Generation (Osterwalder)",
    "prefijos": {"R": "reglas_brainstorming (superviviente)",
                 "D": "brainstorming_divergente", "E": "brainstorming_efectivo"},
    "origenes": ORI_T,
    "grupos_pasos": GRUPOS_T,
    "grupos_condiciones": GRUPOS_COND_T,
    "pasos_finales": derivar(GRUPOS_T),
    "condiciones_finales": derivar(GRUPOS_COND_T),
    "entregable_final": "Sesión de brainstorming documentada con una colección amplia de ideas "
                        "generadas colaborativamente, capturadas en Post-its y agrupadas por "
                        "tema, lista para ser filtrada en la fase de convergencia",
    "titulo_sin_cambio": "Reglas de Brainstorming Efectivo",
    "etiqueta_arbol_sin_cambio": "Organiza tu Lluvia de Ideas",
    "preservar_literal": [
        "inmersión previa",
        "Silly Cow",
        "construir sobre las ideas de otros",
        "sin distracciones",
        "confianza mutua",
    ],
    "rastros": ["Post-it", "cliente", "divergencia", "convergencia", "cantidad"],
}

# ---------------------------------------------------------------------------
# FUSION 2: LA ALTERNANCIA. pensamiento_convergente_divergente absorbe a los otros dos.
# ---------------------------------------------------------------------------
MAPA_A = {"P": "pensamiento_convergente_divergente",
          "G": "generar_multiples_opciones",
          "T": "design_attitude_vs_decision_attitude"}
ORI_A = origenes(MAPA_A)

GRUPOS_A = [
    {"origenes": ["P1", "G1", "T2"],
     "texto": "Antes de buscar la solución, dedicar tiempo y energía explícitos a generar "
              "deliberadamente múltiples alternativas sin juzgarlas (fase divergente).",
     "motivo": "LOS TRES DICEN LA MISMA ORDEN y el superviviente la dice entera. De los "
               "donantes VIAJA solo el matiz: deliberadamente, y la energia ademas del tiempo."},
    {"origenes": ["G2"],
     "texto": "Fijar un deadline claro para la fase de divergencia, evitando la parálisis por "
              "análisis.",
     "motivo": "VIAJA ENTERO. El superviviente no pone limite a la divergencia en ninguno de "
               "sus cuatro pasos, y sin limite la orden de divergir no tiene freno escrito."},
    {"origenes": ["P2"],
     "texto": "Usar la metáfora del embudo: abrir posibilidades ampliamente y luego estrechar "
              "hacia soluciones concretas.",
     "motivo": "VERBATIM del superviviente."},
    {"origenes": ["G3"],
     "texto": "Permitir la 'polinización cruzada' entre ideas distintas antes de converger en "
              "una.",
     "motivo": "VIAJA ENTERO. Es lo unico del donante que no es la orden de divergir, y el "
               "superviviente no lo dice."},
    {"origenes": ["P3", "T3"],
     "texto": "Alternar conscientemente entre fases de generación de ideas y fases de "
              "selección o eliminación de ideas, de forma no lineal entre investigación de "
              "mercado, prototipado y generación.",
     "motivo": "LA ALTERNANCIA ES DEL SUPERVIVIENTE y viaja el matiz del donante, que nombra "
               "las TRES actividades entre las que se alterna. Ninguna de las tres esta "
               "nombrada en el superviviente."},
    {"origenes": ["P4", "T4"],
     "texto": "Aceptar que descartar ideas prometedoras ('matar a los hijos favoritos') es "
              "parte necesaria del proceso, y evitar adoptar la primera solución razonable.",
     "motivo": "LAS DOS CARAS DE LA MISMA DISCIPLINA, soltar lo bueno y no agarrar lo primero. "
               "La segunda VIAJA del donante."},
    {"origenes": ["T1"],
     "texto": "Aceptar la ambigüedad y la incertidumbre como parte natural del proceso "
              "creativo.",
     "motivo": "VIAJA ENTERO y va al final porque es la actitud que sostiene a los seis "
               "anteriores, no un paso que se ejecute antes que ellos. El superviviente no la "
               "nombra."},
]

GRUPOS_COND_A = [
    {"origenes": ["PC1", "GC1", "TC1"],
     "texto": "Cuando el equipo converge demasiado rápido en una única idea sin explorar "
              "alternativas.",
     "motivo": "LA MISMA CONDICION EN LOS TRES NODOS, escrita tres veces."},
    {"origenes": ["PC2"],
     "texto": "Cuando se necesita generar innovación disruptiva en lugar de mejoras "
              "incrementales.",
     "motivo": "VERBATIM del superviviente."},
    {"origenes": ["GC2"],
     "texto": "En la fase de ideación de un proyecto de diseño.",
     "motivo": "VIAJA entera: es la unica que situa el momento y el superviviente no lo situa."},
]

PLAN_ALT = {
    "operacion": "OP-D-04, FUSION 2 de 2: LA ALTERNANCIA. pensamiento_convergente_divergente "
                 "absorbe a generar_multiples_opciones y a "
                 "design_attitude_vs_decision_attitude",
    "estado": "SELLADO Y SIN EJECUTAR. La fusion espera el acta del auditor (decision del "
              "fundador, 19 ago 2026): no se ejecuta en la misma vuelta que la decide.",
    "regla": "OP-D-04 (docs/plan/02_DESTEJIDOS.md) con la forma final adjudicada por el "
             "fundador el 19 ago 2026, siete a tres; superviviente por P.8 (el cableado "
             "desempata, no decide) elegido por LECTURA DE CONTENIDO; perdidas repartidas y "
             "reclasificadas por P.13; simulacion previa sobre copia en memoria por P.7; "
             "limpieza de lo que la propia fusion fabrica por P.16.",
    "motivo": "Segundo subconjunto cerrado del acto de OP-D-04. Sus tres pares internos son A: "
              "los puestos 943 y 885 del cribado y la lectura dirigida LD-93 del 19 ago 2026, "
              "que es la que cerro el triangulo.",
    "fecha_corte": FECHA,
    "superviviente": "pensamiento_convergente_divergente",
    "absorbidos": ["generar_multiples_opciones", "design_attitude_vs_decision_attitude"],
    "fuente_esperada": "Change by Design",
    "prefijos": {"P": "pensamiento_convergente_divergente (superviviente)",
                 "G": "generar_multiples_opciones",
                 "T": "design_attitude_vs_decision_attitude"},
    "origenes": ORI_A,
    "grupos_pasos": GRUPOS_A,
    "grupos_condiciones": GRUPOS_COND_A,
    "pasos_finales": derivar(GRUPOS_A),
    "condiciones_finales": derivar(GRUPOS_COND_A),
    "entregable_final": "Un mapa o registro de iteraciones mostrando ciclos de divergencia y "
                        "convergencia a lo largo del proyecto, con un set documentado de al "
                        "menos 3-5 alternativas de solución evaluadas antes de cada decisión "
                        "final",
    "titulo_sin_cambio": "Pensamiento Convergente y Divergente",
    "etiqueta_arbol_sin_cambio": "Abre y Cierra tus Opciones",
    "preservar_literal": [
        "matar a los hijos favoritos",
        "polinización cruzada",
        "deadline",
        "ambigüedad",
        "3-5 alternativas",
    ],
    "rastros": ["embudo", "divergencia", "convergencia", "iteraciones", "prototipado"],
}


def medir_grafo(plan):
    """Todo lo que la fusion le va a hacer al grafo, MEDIDO y no supuesto.

    Las tres cifras que van al plan salen de aqui y no de un teclado:
      - redirecciones_esperadas: quien nombra hoy a cada absorbido, solo vivos,
        que es el criterio del instrumento sellado de la casa.
      - duplicadas_nuevas_esperadas: entradas que tras la fusion resuelven dos
        veces al mismo destino dentro del mismo campo, contando antes y despues
        y restando, para que salgan SOLO las nuevas.
      - simetrizacion_esperada: las aristas que quedarian declaradas en un solo
        extremo y que scripts/run_phase1.py escribe en su paso 5.
    """
    with io.open(GRAFO, encoding="utf-8") as fh:
        G = json.load(fh)["nodos"]
    A0 = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
    sup = plan["superviviente"]
    A1 = dict(A0)
    for m in plan["absorbidos"]:
        A1[m] = sup

    def hacer_res(tabla):
        def res(x):
            s = set()
            while x in tabla and x not in s:
                s.add(x)
                x = tabla[x]
            return x
        return res

    res0, res1 = hacer_res(A0), hacer_res(A1)

    redirecciones, muertos = [], []
    for nid, d in sorted(G.items()):
        if nid in plan["absorbidos"]:
            continue
        for c in CAMPOS:
            for m in plan["absorbidos"]:
                if m in (d.get(c) or []):
                    fila = {"nodo": nid, "campo": c, "nombraba": m}
                    (muertos if d.get("deprecado") else redirecciones).append(fila)

    def dups(res):
        out = set()
        for nid, d in G.items():
            if d.get("deprecado"):
                continue
            for c in CAMPOS:
                vistos, rep = set(), set()
                for y in (d.get(c) or []):
                    z = res(y)
                    if z == nid:
                        continue
                    if z in vistos:
                        rep.add(z)
                    vistos.add(z)
                for z in rep:
                    out.add((nid, c, z))
        return out

    nuevas = sorted(dups(res1) - dups(res0))

    propias = dict((c, [res0(y) for y in (G[sup].get(c) or [])]) for c in CAMPOS)
    simetria = set()
    for nid, d in G.items():
        if d.get("deprecado") or nid == sup or nid in plan["absorbidos"]:
            continue
        for c in CAMPOS:
            for m in plan["absorbidos"]:
                if m in (d.get(c) or []) and nid not in propias[OPUESTO[c]]:
                    simetria.add((OPUESTO[c], nid))

    return {
        "instrumento": "scripts/plan/simular_fusion.py (P.7) mas "
                       "scripts/loop/vuelta38_reciprocidad_post.py",
        "redirecciones_esperadas": redirecciones,
        "redirecciones_no_tocadas_por_deprecadas": muertos,
        "duplicadas_nuevas_esperadas": [
            {"nodo": a, "campo": c, "resuelve_a": z} for a, c, z in nuevas],
        "simetrizacion_esperada": {
            "quien_la_escribe": "scripts/run_phase1.py, paso 5, Simetrizacion de enlaces. NO la "
                                "escribe el ejecutor de fusiones: el redirige a los vecinos y "
                                "no toca la lista propia del superviviente.",
            "precedente_medido": "commit 72c718ea (OP-D-02 fundida, 15 ago 2026): su "
                                 "phase1_run_log.json trae symmetrize_added con las DOS aristas "
                                 "que el superviviente gano, ventaja_competitiva_producto y "
                                 "procesamiento_paralelo_con_espirales.",
            "vara": "la tasa de reciprocidad del grafo medida hoy es 99,59 por ciento (15.448 "
                    "de 15.511 aristas de nodos vivos, resueltas por P.1), asi que dejar una "
                    "arista declarada en un solo extremo es un defecto y no la costumbre",
            "guarda_para_el_dia_de_la_ejecucion": "symmetrize_added tiene que traer EXACTAMENTE "
                                                  "estas entradas para el superviviente, ni una "
                                                  "mas ni una menos",
            "aristas": [{"campo": c, "vecino": n} for c, n in sorted(simetria)],
        },
    }


def main():
    PLAN_TALLER["resumen_final"] = B.RESUMEN_TALLER
    PLAN_TALLER["eleccion_p8"] = B.ELECCION_TALLER
    PLAN_TALLER["tabla_perdidas_p13"] = B.PERDIDAS_TALLER
    PLAN_ALT["resumen_final"] = B.RESUMEN_ALTERNANCIA
    PLAN_ALT["eleccion_p8"] = B.ELECCION_ALTERNANCIA
    PLAN_ALT["tabla_perdidas_p13"] = B.PERDIDAS_ALTERNANCIA

    fallos = []
    for plan, mapa in ((PLAN_TALLER, MAPA_T), (PLAN_ALT, MAPA_A)):
        plan["simulacion"] = medir_grafo(plan)
        sup = plan["superviviente"]
        pref_sup = [p for p, n in mapa.items() if n == sup][0]
        d = nodo(sup)
        plan["entregable_viejo"] = d.get("entregable_esperado")
        plan["resumen_viejo"] = d.get("resumen_teorico")
        plan["pasos_totales"] = dict((n, len(nodo(n).get("pasos_accionables") or []))
                                     for n in [sup] + plan["absorbidos"])
        plan["condiciones_totales"] = dict(
            (n, len(nodo(n).get("condiciones_activacion") or []))
            for n in [sup] + plan["absorbidos"])
        esperados_pasos = [k for k in plan["origenes"] if "C" not in k[1:]]
        esperados_cond = [k for k in plan["origenes"] if "C" in k[1:]]
        fallos += comprobar_particion(plan["grupos_pasos"], esperados_pasos,
                                      "%s pasos" % sup)
        fallos += comprobar_particion(plan["grupos_condiciones"], esperados_cond,
                                      "%s condiciones" % sup)
        del pref_sup

    if fallos:
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s) de particion:" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print("=" * 78)
    print("GUARDA DE PARTICION: cada origen colocado exactamente una vez. OK")
    print("=" * 78)
    for plan, nombre in ((PLAN_TALLER, "PLAN_V38_OPD04_TALLER.json"),
                         (PLAN_ALT, "PLAN_V38_OPD04_ALTERNANCIA.json")):
        ruta = os.path.join(DESTINO, nombre)
        with io.open(ruta, "w", encoding="utf-8") as fh:
            json.dump(plan, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print("")
        print("ESCRITO: docs/loop/%s" % nombre)
        print("  superviviente : %s" % plan["superviviente"])
        print("  absorbidos    : %s" % ", ".join(plan["absorbidos"]))
        print("  origenes de paso colocados: %d en %d grupos"
              % (sum(len(g["origenes"]) for g in plan["grupos_pasos"]),
                 len(plan["grupos_pasos"])))
        print("  origenes de condicion colocados: %d en %d grupos"
              % (sum(len(g["origenes"]) for g in plan["grupos_condiciones"]),
                 len(plan["grupos_condiciones"])))
        print("  pasos finales : %d" % len(plan["pasos_finales"]))
        for i, p in enumerate(plan["pasos_finales"], 1):
            print("     %d. %s" % (i, p))
        print("  condiciones finales: %d" % len(plan["condiciones_finales"]))
        for i, c in enumerate(plan["condiciones_finales"], 1):
            print("     %d. %s" % (i, c))
        print("  entregable: %s" % plan["entregable_final"])
        sim = plan["simulacion"]
        print("  redirecciones esperadas: %d" % len(sim["redirecciones_esperadas"]))
        for r in sim["redirecciones_esperadas"]:
            print("     %-45s %-17s (nombraba %s)" % (r["nodo"], r["campo"], r["nombraba"]))
        print("  deprecados que nombran y NO se tocan: %d"
              % len(sim["redirecciones_no_tocadas_por_deprecadas"]))
        print("  duplicadas NUEVAS que la fusion fabrica: %d"
              % len(sim["duplicadas_nuevas_esperadas"]))
        for d in sim["duplicadas_nuevas_esperadas"]:
            print("     %-45s %-17s -> %s" % (d["nodo"], d["campo"], d["resuelve_a"]))
        print("  aristas que run_phase1 paso 5 tendra que simetrizar: %d"
              % len(sim["simetrizacion_esperada"]["aristas"]))
        for a in sim["simetrizacion_esperada"]["aristas"]:
            print("     %s.%-17s += %s" % (plan["superviviente"], a["campo"], a["vecino"]))
        print("  perdidas clasificadas por P.13: %d  (VIAJA %d, VIVE DENTRO %d, YA NO APLICA %d)"
              % (len(plan["tabla_perdidas_p13"]),
                 sum(1 for p in plan["tabla_perdidas_p13"] if p["clase"] == "VIAJA"),
                 sum(1 for p in plan["tabla_perdidas_p13"] if p["clase"] == "VIVE DENTRO"),
                 sum(1 for p in plan["tabla_perdidas_p13"] if p["clase"] == "YA NO APLICA")))
        print("  superviviente elegido por: %s (P.8). Cableado usado para decidir: %s"
              % (plan["eleccion_p8"]["decide"],
                 plan["eleccion_p8"]["cableado_solo_como_desempate"]["usado_para_decidir"]))
    print("")
    print("NINGUN NODO TOCADO. dataset/ intacto.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
