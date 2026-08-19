# -*- coding: utf-8 -*-
"""vuelta45_opd09.py - EL PLAN SELLADO Y LAS GUARDAS DE OP-D-09.

ESTRICTAMENTE DE SOLO LECTURA sobre dataset/nodos. En modo plan escribe UN
fichero, docs/loop/PLAN_V45_OPD09.json; en modo guardas no escribe nada.

Misma forma que OP-D-08: lo unico tecleado son los grupos y sus motivos, y todo
lo demas se mide del grafo. El plan lo ejecuta scripts/loop/vuelta32_podar.py.

Uso:
    python scripts/loop/vuelta45_opd09.py plan
    python scripts/loop/vuelta45_opd09.py guardas <ANTES|DESPUES>
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DESTINO = os.path.join(RAIZ, "docs", "loop", "PLAN_V45_OPD09.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")

NODO = "planificacion_recoleccion_datos"
FUENTE = "Juran's Quality Handbook_ The C - Joseph A. Defeo"

OPERACION = ("OP-D-09: el destejido de planificacion_recoleccion_datos, DESTEJIDO "
             "SOLO, quitar el indice que se colo como pasos")

REGLA = (
    "OP-D-09 de docs/plan/OPERACIONES.jsonl, leida ENTERA hoy antes de tocar nada. "
    "REMEDIO: QUITAR EL INDICE, tal como la ficha del gradiente lo tenia escrito, "
    "PERO CON LA CORRECCION QUE LA VUELTA 17 MIDIO Y LA FICHA NO DECIA: el indice "
    "son los pasos 2, 3 y 4, NO los cuatro. El paso 1 no tiene casa en el metodo de "
    "5 a 16 y ademas sostiene al paso 14, asi que por la REGLA DE REPARTO de la fase "
    "(la perdida que no tenga bloque va AL SUPERVIVIENTE) sobrevive como CABECERA "
    "del metodo en vez de podarse. EL METODO COMPLETO, pasos 5 a 16, NO SE TOCA.")

MOTIVO = (
    "PODAR LOS CUATRO PASOS DEL INDICE PIERDE LA PREGUNTA, y esta medido: el paso 1 "
    "no es indice de nada, es el marco del que cuelga todo el metodo (el propio "
    "resumen_teorico del nodo dice 'empezar con el fin en mente, trabajando hacia "
    "atras DESDE LA PREGUNTA'), y el paso 14, que sobrevive, apunta al PROBLEMA "
    "TECNICO ORIGINAL que solo el paso 1 establece. Por eso el indice son TRES pasos "
    "y no cuatro. "
    "LOS TRES QUE SE VAN SE COMPRUEBAN UNO A UNO EN SU CASA ANTES DE QUITARLOS Y NO "
    "DESPUES, que es lo que el eliminar de la operacion exige, y la comprobacion se "
    "ve EN EL MAPA, que es donde se puede auditar: cada uno de los tres viaja CON el "
    "paso del metodo que ya lo dice. El paso 2 (decidir QUE medir considerando como "
    "se comunicaran y analizaran los datos) viaja con el 9 (filtrar y analizar), y su "
    "mitad de comunicacion la dice ademas el 15 (presentar los resultados en un "
    "informe claro). El paso 3 (decidir COMO medir la poblacion o muestra: "
    "herramienta, estrategia de muestreo, tamano) viaja con el 7 (disenar, preparar y "
    "probar metodos, formularios e instrucciones, incluir MSA), y su mitad de tamano "
    "de muestra la dice ademas el 10 (evaluar supuestos del tamano de muestra). El "
    "paso 4 (recolectar los datos con MINIMO SESGO) viaja con el 6 (seleccionar y "
    "capacitar recolectores IMPARCIALES), que es donde el sesgo se ataca de raiz, y "
    "lo respaldan ademas el 5 (definir puntos de recoleccion comprensivos) y el 8 "
    "(auditar el proceso de recoleccion y validar resultados). NINGUNO DE LOS TRES "
    "DEJA RESTO SIN CASA, y por eso ninguno abre paso nuevo. "
    "LAS DOS ANCLAS QUE LA OPERACION DECLARA INTOCABLES SE QUEDAN VERBATIM Y SIN "
    "MOVERSE DE SU SITIO RELATIVO: el paso 7, ancla del UNICO veredicto de este nodo "
    "en todo el cribado (el 2695), con su MSA dentro palabra por palabra; y el paso "
    "10, ancla de las DOS candidatas paso a nodo hacia analisis_pareto y "
    "analisis_pareto_proyectos_elefante, que siguen SIN escribirse y NO se escriben "
    "aqui (aristas_nuevas de esta operacion esta VACIO y los enlaces son la fase 04). "
    "LAS CONDICIONES NO SE TOCAN: la operacion legisla PASOS y solo pasos. "
    "EL DESAJUSTE DE 17 CONTRA 16 NO SE RELLENA, y se dice por que: el "
    "resumen_teorico declara que el proceso INVOLUCRA 17 PASOS y el nodo tiene 16 "
    "pasos_accionables. Es HUECO NOMBRADO y decidirlo exige la fuente, que esta FUERA "
    "DEL REPO. La propia operacion lo dejo ANOTADO y no preguntado, y esta vuelta lo "
    "deja igual: rellenarlo seria inventar un paso. "
    "LA DISCREPANCIA DE CORTE, declarada y no cuadrada, tal como la nota de la "
    "operacion la dejo: el instrumento mecanico pone el corte en el paso 11 y la "
    "lectura de la ficha lo pone en el 4. NO SE ELIGE UNO Y SE BORRA EL OTRO. Esta "
    "operacion opera sobre el corte LEIDO, y el mecanico queda escrito al lado como "
    "lo que es, la senal que llevo a mirar. "
    "LA FUENTE NO SE TOCA: es UNICA (Juran, Defeo) y ningun bloque sale del nodo.")

# (origenes, verbatim_del_paso, motivo)
GRUPOS = [
    ([1], 1,
     "LA CABECERA, Y ES LA UNICA PIEZA DEL INDICE QUE NO SE VA. Establecer los "
     "objetivos y FORMULAR LA PREGUNTA ESPECIFICA no tiene casa en el metodo de 5 a "
     "16: ninguno de sus doce pasos formula la pregunta. Sostiene ademas al paso 14, "
     "que manda revisar que las conclusiones respondan AL PROBLEMA TECNICO ORIGINAL, "
     "y sin ella el 14 apuntaria a algo que el nodo ya no dice. Sobrevive VERBATIM y "
     "de PRIMERA, como cabecera del metodo, que es lo que preservar manda."),
    ([5], 5, "METODO, VERBATIM. Primero de los doce que no se tocan."),
    ([4, 6], 6,
     "METODO, VERBATIM, Y AQUI SE COMPRUEBA EL PRIMERO DE LOS TRES PASOS DEL INDICE "
     "ANTES DE QUITARLO. El paso 4 decia 'Recolectar los datos con minimo sesgo' y "
     "este 6 manda seleccionar y capacitar recolectores IMPARCIALES, que es donde el "
     "sesgo se ataca de raiz y no como advertencia. Lo respaldan ademas el 5 (puntos "
     "de recoleccion comprensivos) y el 8 (auditar el proceso y validar), los dos a "
     "la vista en este mismo mapa. El paso 4 no deja resto sin casa."),
    ([3, 7], 7,
     "METODO, VERBATIM, Y ES EL PASO INTOCABLE: ancla del 2695, el UNICO veredicto de "
     "este nodo en todo el cribado, CON SU MSA DENTRO palabra por palabra. Aqui se "
     "comprueba el SEGUNDO paso del indice antes de quitarlo: el 3 decia 'decidir "
     "COMO medir la poblacion o muestra (herramienta, estrategia de muestreo, "
     "tamano)' y este 7 manda disenar, preparar y PROBAR metodos, formularios e "
     "instrucciones; la mitad del tamano de muestra la dice ademas el 10, dos "
     "destinos mas abajo. El paso 3 no deja resto sin casa."),
    ([8], 8, "METODO, VERBATIM."),
    ([2, 9], 9,
     "METODO, VERBATIM, Y AQUI SE COMPRUEBA EL TERCERO Y ULTIMO PASO DEL INDICE. El "
     "paso 2 decia 'decidir QUE medir considerando como se comunicaran y analizaran "
     "los datos': el analisis lo hace este 9 (filtrar y analizar los datos) y la "
     "comunicacion la hace el 15 (presentar los resultados en un informe claro con "
     "resumen ejecutivo), tambien a la vista en este mapa. El paso 2 no deja resto "
     "sin casa, y con el los TRES del indice quedan comprobados uno a uno EN SU CASA "
     "antes de quitarlos, que es lo que el eliminar exige."),
    ([10], 10,
     "METODO, VERBATIM, Y LA SEGUNDA ANCLA INTOCABLE: de este paso salen las DOS "
     "candidatas paso a nodo hacia analisis_pareto y analisis_pareto_proyectos_"
     "elefante (docs/plan/PASO_NODO_CALIBRADO.jsonl), las dos con arista TODAVIA NO "
     "ESCRITA. Ni se toca ni se escribe ninguna de las dos aqui: aristas_nuevas de "
     "esta operacion esta VACIO y los enlaces son la fase 04."),
    ([11], 11, "METODO, VERBATIM."),
    ([12], 12, "METODO, VERBATIM."),
    ([13], 13, "METODO, VERBATIM."),
    ([14], 14,
     "METODO, VERBATIM, Y ES EL PASO QUE NO PUEDE QUEDAR COLGANDO: revisar que las "
     "conclusiones respondan AL PROBLEMA TECNICO ORIGINAL solo se sostiene si el nodo "
     "sigue diciendo en algun sitio cual era ese problema, y lo dice el destino 1, la "
     "cabecera que sobrevive. Si la cirugia se hubiera llevado el paso 1, este se "
     "quedaria apuntando al vacio."),
    ([15], 15,
     "METODO, VERBATIM, y sostiene la tercera de las tres piezas que el entregable "
     "nombra: la presentacion de resultados."),
    ([16], 16, "METODO, VERBATIM. Ultimo de los doce que no se tocan."),
]


def leer(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8").read())


def plan():
    d = leer(NODO)
    pasos = list(d.get("pasos_accionables") or [])
    cond = list(d.get("condiciones_activacion") or [])
    assert d.get("fuente") == FUENTE, repr(d.get("fuente"))

    mapa, finales, filas = {}, [], []
    for i, (origenes, vb, motivo) in enumerate(GRUPOS, 1):
        texto = pasos[vb - 1]
        mapa[str(i)] = list(origenes)
        finales.append(texto)
        filas.append((i, origenes, vb, texto, motivo))

    todos = []
    for v in mapa.values():
        todos.extend(v)
    faltan = sorted(set(range(1, len(pasos) + 1)) - set(todos))
    repes = sorted({x for x in todos if todos.count(x) > 1})
    sobran = sorted(set(todos) - set(range(1, len(pasos) + 1)))

    obj = {
        "operacion": OPERACION, "regla": REGLA, "motivo": MOTIVO,
        "fecha_corte": "2026-08-19",
        "correcciones_declaradas": [
            "LA CIFRA DE ARISTAS DE LA OPERACION ES DE OTRO CORTE Y SE DECLARA EN VEZ "
            "DE COPIARSE (regla 2): su verificacion dice 'el grafo entero tiene 16.866 "
            "entradas de arista antes y despues', cifra de la vuelta 17. MEDIDO HOY, "
            "ANTES DEL ACTO: 16.898. La guarda es CERO MOVIMIENTO, o sea que la cifra "
            "de HOY no se mueva, y asi se comprueba.",
            "LA CIFRA DE VECINOS SI CALZA AL DIGITO: la operacion dice 5 vecinos (2 "
            "previos y 3 siguientes) y hoy son 5 (2 previos y 3 siguientes).",
        ],
        "nodos": [{
            "nodo": NODO, "fuente_esperada": FUENTE,
            "pasos_totales": len(pasos), "condiciones_totales": len(cond),
            "prefijos_pasos": [p[:34] for p in pasos],
            "prefijos_condiciones": [c[:34] for c in cond],
            "pasos_originales": pasos, "condiciones_originales": cond,
            "mapa_pasos": mapa, "pasos_finales": finales,
            "condiciones_finales": None, "mapa_condiciones": None,
            "procedencia": [{"pasos_del_resultado": list(range(1, len(finales) + 1)),
                             "libro": FUENTE}],
            "motivos_por_destino": dict((str(i), m) for i, o, v, t, m in filas),
        }],
    }

    print("=" * 78)
    print("EL PLAN DE OP-D-09, CONSTRUIDO CONTRA EL GRAFO (vuelta 45)")
    print("=" * 78)
    print()
    print("  nodo   : %s  (dominio %s)" % (NODO, d.get("dominio")))
    print("  fuente : %s  (UNICA, sin cambio)" % d.get("fuente"))
    print("  pasos  : %d  ->  %d" % (len(pasos), len(finales)))
    print("  condiciones: %d  ->  %d  (NO SE TOCAN)" % (len(cond), len(cond)))
    print()
    print("  EL MAPA DEL REPARTO, destino <- origenes:")
    print()
    for i, origenes, vb, texto, motivo in filas:
        print("  %-4d %-10s verbatim del paso %-3d %s" % (i, origenes, vb, texto[:66]))
    print()
    print("  GUARDA DEL CONSTRUCTOR, cobertura exacta de 1 a %d:" % len(pasos))
    print("    origenes cubiertos: %d | faltan: %s | repetidos: %s | sobran: %s"
          % (len(todos), faltan or "ninguno", repes or "ninguno", sobran or "ninguno"))
    if faltan or repes or sobran:
        print("  PARADA: la cobertura no cierra. NO se sella el plan.")
        return 1
    print()
    print("  EL METODO 5 A 16, comprobado INTACTO, CONTIGUO Y EN ORDEN:")
    met = [(i, sorted(set(o) & set(range(5, 17)))) for i, o, v, t, m in filas
           if set(o) & set(range(5, 17))]
    print("    destinos que lo llevan: %s" % [i for i, _ in met])
    print("    origenes en orden     : %s" % [x[0] for _, x in met])
    print("    los doce, contiguos y en orden: %s"
          % ([x[0] for _, x in met] == list(range(5, 17))))
    print()
    print("  EL INDICE QUE SE VA, y con quien viaja cada uno:")
    for ind in (2, 3, 4):
        for i, o, v, t, m in filas:
            if ind in o:
                print("    paso %d del indice -> destino %d, que es el paso %d del metodo: %s"
                      % (ind, i, v, t[:52]))
    print()
    with io.open(DESTINO, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(obj, ensure_ascii=False, indent=1) + u"\n")
    print("  PLAN SELLADO en %s" % os.path.relpath(DESTINO, RAIZ))
    print("=" * 78)
    return 0


def guardas(etiqueta):
    d = leer(NODO)
    pasos = d.get("pasos_accionables") or []
    cond = d.get("condiciones_activacion") or []
    bajo = [p.lower() for p in pasos]
    print("=" * 78)
    print("GUARDAS DE OP-D-09, MEDICION DE %s" % etiqueta)
    print("=" * 78)
    print()
    print("  nodo: %s | pasos: %d | condiciones: %d" % (NODO, len(pasos), len(cond)))
    print()
    print("### (A) EL CASO POSITIVO: tiene que CAER antes y PASAR despues")
    print()
    pos = []
    idx = [i + 1 for i, p in enumerate(bajo)
           if u"decidir qu" in p or u"decidir c" in p or u"minimo sesgo" in p
           or u"mínimo sesgo" in p]
    pos.append(("A1 EL INDICE QUE SE COLO COMO PASOS YA NO ESTA", not idx,
                "pasos de indice presentes: %s (son %d)" % (idx or "ninguno", len(idx))))
    pos.append(("A2 EL NODO ES UN METODO Y NO UN RESUMEN MAS UN METODO",
                len(pasos) == 13, "pasos: %d (13 es cabecera mas los doce del metodo)"
                % len(pasos)))
    caen = 0
    for n, ok, det in pos:
        print("  [%s] %s" % ("PASA" if ok else "CAE ", n))
        print("         %s" % det)
        caen += 0 if ok else 1
    print()
    print("  RESULTADO DEL CASO POSITIVO: %d PASAN y %d CAEN" % (len(pos) - caen, caen))
    print()
    print("### (B) LAS INVARIANTES: tienen que PASAR las dos veces")
    print()
    prev, sig = d.get("nodos_previos") or [], d.get("nodos_siguientes") or []
    total = 0
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            x = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
            for c in CAMPOS:
                total += len(x.get(c) or [])
    p7 = [p for p in pasos if u"MSA" in p]
    p10 = [p for p in bajo if u"supuestos del tama" in p]
    p14 = [p for p in bajo if u"problema t" in p and u"original" in p]
    p1 = [p for p in bajo if u"formular la pregunta" in p]
    inv = [
        ("B1 CERO MOVIMIENTO: los vecinos del nodo", len(prev) + len(sig) == 5,
         "previos %d + siguientes %d = %d (la operacion declara 5: 2 y 3)"
         % (len(prev), len(sig), len(prev) + len(sig))),
        ("B2 CERO MOVIMIENTO: las entradas de arista del grafo entero", total == 16898,
         "%d entradas. La cifra escrita en la operacion (16.866) es del corte de la "
         "vuelta 17 y se cita como contraste" % total),
        ("B3 EL PASO 7 VIVO PALABRA POR PALABRA, CON SU MSA DENTRO", len(p7) == 1,
         (p7[0] if p7 else "AUSENTE")),
        ("B4 EL PASO 10 VIVO (ancla de las dos candidatas paso a nodo)", len(p10) == 1,
         "supuestos del tamano de muestra: %s" % ("presente" if p10 else "AUSENTE")),
        ("B5 EL PASO 14 NO QUEDA COLGANDO: el nodo sigue diciendo cual era el problema",
         bool(p14) and bool(p1),
         "el 14 esta: %s | la pregunta del paso 1 esta: %s" % (bool(p14), bool(p1))),
        ("B6 EL ENTREGABLE SIGUE SIENDO CIERTO: preguntas, muestreo y presentacion",
         bool(p1) and any(u"muestra" in p for p in bajo)
         and any(u"presentar" in p for p in bajo),
         "preguntas %s | muestreo %s | presentacion %s"
         % (bool(p1), any(u"muestra" in p for p in bajo),
            any(u"presentar" in p for p in bajo))),
        ("B7 LA FUENTE NO SE TOCA", d.get("fuente") == FUENTE, repr(d.get("fuente"))),
        ("B8 LAS CONDICIONES NO SE TOCAN", len(cond) == 2, "%d condiciones" % len(cond)),
        ("B9 EL DESAJUSTE 17 CONTRA 16 NO SE RELLENA: sigue siendo hueco nombrado",
         u"17 pasos" in (d.get("resumen_teorico") or ""),
         "el resumen sigue diciendo 17 y el nodo tiene %d pasos: NO se toca ninguno "
         "de los dos, porque decidirlo exige la fuente, fuera del repo" % len(pasos)),
    ]
    rojo = 0
    for n, ok, det in inv:
        print("  [%s] %s" % ("OK  " if ok else "ROJO", n))
        print("         %s" % det)
        rojo += 0 if ok else 1
    print()
    print("  RESULTADO DE LAS INVARIANTES: %d en OK y %d en ROJO" % (len(inv) - rojo, rojo))
    print()
    print("=" * 78)
    return 0


modo = sys.argv[1] if len(sys.argv) > 1 else "plan"
raise SystemExit(plan() if modo == "plan" else guardas(sys.argv[2]))
