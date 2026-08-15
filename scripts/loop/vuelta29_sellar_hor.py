"""Vuelta 29: sella OP-F-04-HOR, la tanda de Horowitz.

DESBLOQUEADA POR CITA: el acta de la vuelta 28 del auditor (adjudicacion 3) leyo
el REGISTRO del fundador en la nota de la propia OP-F-04-HOR de OPERACIONES.jsonl
y adjudico que la tanda NO esta bloqueada en bloque: se ejecuta como WEI, miembro
por P.18 sobre la nomina medida al dia, y nodo propio SOLO en el bloque sin
miembro coincidente.

Las fronteras NO se deciden aqui: estan leidas y publicadas en
docs/plan/01_FUENTES.md desde la vuelta 20, en la tabla LA NOMINA DE LOS 14 DE
HOROWITZ. Lo que esta vuelta anade es el DESTINO por P.18 sobre la nomina de hoy.

NO ENTRA decision_de_vender_startup: es uno de LOS TRES CASOS QUE NO SON UN
SIMPLE APENDICE, va con TOQUE UNICO y su material esta repetido TRES veces. Va
al reporte como PARADA con su lectura.

Uso: python scripts/loop/vuelta29_sellar_hor.py
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
SALIDA = os.path.join(RAIZ, "docs", "loop", "PLAN_V29_OPF04_HOR.json")

HOROWITZ = "The Hard Thing About Hard Things - Ben Horowitz"


def todos():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


BOLSA = {
    "node_id": "estar_listo_para_ser_publica",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Estar Listo para Ser una Empresa Publica",
    "fuente": HOROWITZ,
    "resumen_teorico": (
        "Querer salir a bolsa y estar listo para hacerlo son dos cosas distintas, y la segunda "
        "se mide con honestidad o no se mide. El minimo no es una cifra de ingresos: es que la "
        "operacion sea estable, que los procesos esten ordenados y que las proyecciones se "
        "puedan sostener trimestre tras trimestre delante de gente que no perdona un fallo. La "
        "lista de ventajas y desventajas no se escribe en abstracto sino contra el momento del "
        "mercado, que cambia el calculo entero. Y hay dos conversaciones que ahorran anos: "
        "hablar con quien ya dirigio una empresa publica, y preparar al equipo para lo que la "
        "valuacion va a decir de verdad, incluido el caso incomodo de tener que ofrecer por "
        "debajo de lo que valieron las rondas privadas, porque el precio lo fijan los "
        "comparables del mercado y no la historia propia."
    ),
    "entregable_esperado": (
        "Tu evaluacion honesta de si la operacion, los procesos y las proyecciones aguantan el "
        "escrutinio publico, la lista de ventajas y desventajas contra el momento actual del "
        "mercado, y el rango de precio de oferta calibrado con comparables"
    ),
    "nodos_previos": ["decision_de_salir_a_bolsa"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando la salida a bolsa dejo de ser una idea y hay que decidir si el negocio aguanta "
        "el escrutinio trimestral",
        "Cuando hay que fijar el precio de la oferta y la valuacion privada anterior esta por "
        "encima de lo que dicen los comparables",
    ],
    "etiqueta_arbol": "Mide si Aguantas la Bolsa",
}

PROCESO = {
    "node_id": "formalizar_un_proceso_ad_hoc",
    "fase_proyecto": "ejecucion",
    "dominio": "core",
    "titulo_concepto": "Formalizar un Proceso Ad Hoc que Cruza la Organizacion",
    "fuente": HOROWITZ,
    "resumen_teorico": (
        "Los procesos que mas dano hacen cuando fallan son los que nadie escribio: los que "
        "cruzan fronteras entre areas y se sostienen porque alguien los ejecuta de memoria. "
        "Contratar es el ejemplo tipico. Formalizarlos no se hace desde afuera: se le pide a "
        "la gente que ya los ejecuta que los escriba, porque son quienes saben como funcionan "
        "de verdad. Y el orden importa: primero se define QUE tiene que producir el proceso, "
        "el resultado final concreto, y solo despues se disenan las etapas que llevan hasta "
        "ahi. Cada etapa lleva su metrica propia, que es lo que permite ver en cual se rompe "
        "en vez de saber solo que el resultado fallo, y cada paso lleva un responsable con "
        "nombre. Lo ultimo, y es lo que sostiene todo lo anterior, es hacer visible el "
        "desempeno de cada responsable."
    ),
    "entregable_esperado": (
        "El proceso escrito por quienes ya lo ejecutan, con su resultado final definido antes "
        "que las etapas, una metrica por etapa y un responsable con nombre por cada paso"
    ),
    "nodos_previos": ["plan_mejora_procesos"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando un proceso critico cruza varias areas y funciona solo porque alguien lo "
        "sostiene de memoria",
        "Cuando el resultado de un proceso falla y no se puede saber en que etapa se rompio "
        "porque ninguna tiene metrica propia",
    ],
    "etiqueta_arbol": "Escribe tu Proceso Informal",
}

HISTORIA = {
    "node_id": "la_historia_de_la_empresa",
    "fase_proyecto": "planificacion",
    "dominio": "core",
    "titulo_concepto": "La Historia de la Empresa, y no es el Eslogan",
    "fuente": HOROWITZ,
    "resumen_teorico": (
        "La historia de la empresa no es una frase pegadiza: es el texto completo que contesta "
        "por que existe, por que importa, por que alguien deberia unirse, por que alguien "
        "deberia comprar y por que alguien deberia invertir. Escribirla entera es incomodo "
        "justamente porque obliga a contestar las cinco, y las cartas fundacionales que se "
        "citan como referencia son largas por eso. La prueba de que la historia esta bien no "
        "es que suene bien: es que las personas clave, empleados, inversionistas, prensa y "
        "clientes, puedan contarla con SUS propias palabras sin perder el sentido. Y hay una "
        "senal barata de que no esta clara, que casi siempre se lee mal: cuando adentro se "
        "repite que nadie los entiende o que hace falta mejor marketing, el problema no suele "
        "ser el marketing, es que la historia o la estrategia no estan claras."
    ),
    "entregable_esperado": (
        "La historia completa de tu empresa escrita, contestando por que existe, por que "
        "importa, por que unirse, por que comprar y por que invertir, y la comprobacion de que "
        "las personas clave la pueden contar con sus propias palabras"
    ),
    "nodos_previos": ["posicionamiento_de_empresa"],
    "nodos_siguientes": [],
    "condiciones_activacion": [
        "Cuando el posicionamiento ya esta escrito y hace falta el texto largo que lo sostiene",
        "Cuando adentro se repite que nadie los entiende o que hace falta mejor marketing",
    ],
    "etiqueta_arbol": "Escribe la Historia de tu Empresa",
}

CORTES = [
    ("actualizacion_posiciones_existentes", list(range(5, 20)),
     "The Founder's Dilemmas",
     ("miembro", "evaluacion_balanceada_de_ejecutivos"),
     "apalancamiento real",
     "P.18: el objeto del miembro es evaluar a un ejecutivo SIN quedarse solo con los "
     "resultados, con su ficha de las cuatro areas revisada CADA TRIMESTRE, y el bloque cierra "
     "exactamente ahi: evalua al equipo ejecutivo al menos una vez por trimestre en todas las "
     "dimensiones, no separa la capacidad de escalar del desempeno actual, y prohibe juzgar el "
     "desempeno futuro con teorias sin datos. Los pasos de la conversacion de la degradacion "
     "viajan con el bloque porque la frontera publicada es UNA (1 a 4 / 5 a 19) y esta vuelta "
     "no rehace lecturas publicadas: la heterogeneidad queda declarada como costura."),

    ("background_startup_vs_corporativo", [5, 6, 7, 8, 9],
     "The Founder's Dilemmas",
     ("miembro", "contratar_ambicion_correcta"),
     "primer mes contigo",
     "P.18: el entregable del miembro es una GUIA DE ENTREVISTA con preguntas y senales "
     "especificas para detectar EL TIPO DE AMBICION del candidato, y el bloque entero son esas "
     "preguntas y esas senales: que hara en su primer mes y desconfiar si solo habla de "
     "aprender, por que quiere unirse a un negocio pequeno y desconfiar si la unica motivacion "
     "es el equity, y buscar a alguien motivado por CREAR mas que por administrar."),

    ("contratacion_experiencia_vs_potencial", [5, 6, 7, 8, 9, 10],
     "The Founder's Dilemmas - Wasserman, Noam",
     ("miembro", "contratar_por_fortaleza"),
     "sistema complejo que ya construiste",
     "P.18: el entregable del miembro es un perfil de contratacion basado en LA FORTALEZA "
     "CRITICA ESPECIFICA que necesitas, y el primer paso del bloque es literalmente ese: "
     "definir la razon CONCRETA Y ESPECIFICA por la que necesitas experiencia senior, no una "
     "razon abstracta. Lo que sigue es como se lee esa fortaleza (conocimiento de adentro "
     "contra conocimiento del mercado) y con que estandar se mide."),

    ("decision_de_salir_a_bolsa", [6, 7, 8, 9, 10],
     "The Founder's Dilemmas",
     ("nodo_propio", BOLSA),
     "rondas privadas anteriores",
     "P.18 PUNTO 3. Barrida la nomina de hoy, la familia de Horowitz NO TIENE NINGUN MIEMBRO "
     "sobre la salida a bolsa: el unico nodo del catalogo con ese objeto es el propio donante, "
     "y el donante SALE de la familia al quedarse con Wasserman como fuente unica. Los "
     "vecinos por tema son de venta de la empresa (tipos_adquisiciones_tecnologia, "
     "necesidad_vs_deseo_en_ma), que es la salida contraria."),

    ("estrategia_de_innovacion_producto", [4, 5, 6, 7],
     "Winning at New Products - Robert G. Cooper",
     ("miembro", "coraje_en_decisiones_dificiles"),
     "responsabilidad y el riesgo de esta decisi",
     "P.18: el entregable del miembro es una DECISION DOCUMENTADA CON SU JUSTIFICACION, tomada "
     "A PESAR de la incertidumbre o la oposicion del equipo, y el bloque es ese acto en su "
     "forma mas nitida: reinventar el producto AUNQUE contradiga el feedback documentado de "
     "los clientes, decirle a quien construye que la vision pesa mas que el backlog, y asumir "
     "personalmente la responsabilidad y el riesgo si hay resistencia."),

    ("manejo_empleados_en_adquisicion", [5, 6, 7, 8, 9],
     "Venture Deals - Brad Feld",
     ("miembro", "comunicacion_honesta_en_crisis_al_equipo"),
     "irse con dignidad",
     "P.18: el entregable del miembro es el comunicado de crisis entregado AL EQUIPO con "
     "peticion clara de compromiso, y el bloque es ese comunicado paso por paso: informar "
     "primero y directamente a los afectados ANTES de cualquier anuncio externo, decir el "
     "estado real sin edulcorar, dar la opcion de irse con dignidad, emitir condiciones nuevas "
     "a quien se queda como senal de compromiso mutuo, y poner la claridad interna por encima "
     "de la conveniencia de la prensa."),

    ("metas_vs_proposito", [5, 6, 7, 8, 9],
     "Assembling Tomorrow: A Guide to Designing a Thriving Future | Never Lose a Customer Again - Joey Coleman",
     ("miembro", "diseno_metricas_lideres_rezagados"),
     "white box",
     "P.18: el entregable del miembro es un panel de metricas con senales tempranas y "
     "resultados finales balanceados Y LA RAZON DE CADA UNO ANOTADA, y el bloque es "
     "exactamente el metodo de esa anotacion: definir primero el objetivo cualitativo, "
     "preguntarse que comportamientos generara la metrica ANTES de implementarla, complementar "
     "lo cuantitativo con lo cualitativo, no sacrificar el largo plazo por el numero del "
     "trimestre, y entender COMO se producen los numeros y no solo el resultado."),

    ("organizacion_adaptativa", [5, 6, 7, 8],
     "The Lean Startup - Eric Ries",
     ("miembro", "contratacion_acelerada_hipercrecimiento"),
     "curva de aprendizaje de la gente nueva",
     "P.18: el entregable del miembro es un plan de contratacion escalonado CON UMBRALES DE "
     "ACTIVACION Y DESACTIVACION, y el bloque es la lectura de esos umbrales por dentro: "
     "detectar el momento en que sumar personas genera MAS trabajo del que ahorra, agregar "
     "especializacion solo cuando la curva de aprendizaje se vuelve empinada, y no meter "
     "estructura demasiado pronto ni demasiado tarde."),

    ("plan_mejora_procesos", [6, 7, 8, 9, 10],
     "A Project Manager's Book of Forms",
     ("nodo_propio", PROCESO),
     "formalicen",
     "P.18 PUNTO 3. Barrida la nomina de hoy, ningun miembro tiene por objeto FORMALIZAR UN "
     "PROCESO AD HOC QUE CRUZA FRONTERAS: hr_calidad_gestion y "
     "hr_como_control_de_calidad_gerencial miden el ciclo de vida del EMPLEADO, "
     "proceso_de_promocion_disciplinado es el de ascensos, y framework_excelencia_operacional "
     "AUDITA procesos que ya existen. El bloque los CREA, y su ejemplo (contratar) es un caso, "
     "no el objeto."),

    ("plan_mejora_procesos", [11, 12, 13, 14, 15],
     "A Project Manager's Book of Forms",
     ("miembro", "formalizar_un_proceso_ad_hoc"),
     "visibilidad del desempe",
     "MISMO destino que el corte anterior, por la ADJUDICACION 3 DEL ACTA DE LA VUELTA 27. Los "
     "dos bloques salen del MISMO nodo, declaran al MISMO libro con las dos grafias que ese "
     "nodo trae (la averia que OP-S-11 ya registro, y este es su segundo ejemplar medido) y "
     "dicen lo mismo cuatro veces de cinco: definir el resultado final, disenar las etapas, "
     "metricas por etapa y responsable por paso. Partirlos habria fabricado el gemelo."),

    ("posicionamiento_de_empresa", [6, 7, 8, 9],
     "The Startup Owner's Manual - Steve Blank",
     ("nodo_propio", HISTORIA),
     "Bezos",
     "P.18 PUNTO 3. Barrida la nomina de hoy, ningun miembro tiene por objeto LA HISTORIA "
     "COMPLETA DE LA EMPRESA: atributos_liderazgo_ceo trata la narrativa de vision como uno de "
     "tres atributos del lider y su entregable es un plan personal de desarrollo; "
     "diferenciacion_de_marca_contraintuitiva es posicionamiento de marca contra la "
     "competencia. El bloque pide un TEXTO LARGO que contesta cinco porques y se valida "
     "haciendo que otros lo cuenten con sus palabras, y el propio nodo donante distingue la "
     "historia del eslogan en su primer paso del bloque."),

    ("revisiones_regulares_desempeno_ceo", [5, 6, 7, 8, 9, 10],
     "The Founder's Dilemmas",
     ("miembro", "framework_excelencia_operacional"),
     "fricciones pol",
     "P.18: el entregable del miembro es un DOCUMENTO DE AUDITORIA DE PROCESOS DE GESTION con "
     "metricas balanceadas y diseno organizacional justificado, y el bloque es esa auditoria "
     "en forma de preguntas: la velocidad y calidad de las decisiones tomadas con informacion "
     "incompleta, si el equipo ejecutivo y los procesos de contratacion siguen alineados, si "
     "la gente puede ejecutar sin friccion politica, y si los objetivos estan calibrados a la "
     "oportunidad real y no a benchmarks ajenos."),

    ("seleccion_ceo_fundador", [5, 6, 7, 8, 9, 10, 11, 12],
     "The Founder's Dilemmas",
     ("miembro", "planificacion_sucesion_ceo"),
     "preserven tu control operativo",
     "P.18: el entregable del miembro es un plan de sucesion de liderazgo con candidatos, su "
     "perfil y estrategia de comunicacion, y el bloque es la cara del fundador de esa misma "
     "sucesion: evaluar si tiene la vision de producto para seguir liderando, identificar sus "
     "brechas de CEO, buscar al CEO profesional adecuado e integrarlo preservando sus "
     "fortalezas, asegurar una transicion GRADUAL siguiendo involucrado en producto, y "
     "detectar las senales tempranas de desalineacion."),
]


def main():
    grafo = todos()
    cortes = []
    fallos = []
    creados = set()
    for origen, idx, fuente_queda, (tipo, destino), huella, motivo in CORTES:
        d = grafo[origen]
        pasos = d["pasos_accionables"]
        fuera = [i for i in idx if i < 1 or i > len(pasos)]
        if fuera:
            fallos.append("%s: pasos fuera de rango %s (%d pasos)" % (origen, fuera, len(pasos)))
            continue
        salen = [pasos[i - 1] for i in idx]

        if not any(huella in p for p in salen):
            fallos.append("%s: la huella %r NO esta en el bloque que sale" % (origen, huella))
            continue
        portadores = [nid for nid, dd in grafo.items()
                      if nid != origen and any(huella in p for p in dd.get("pasos_accionables") or [])]
        if portadores:
            fallos.append("%s: la huella %r ya vive fuera del origen, en %s"
                          % (origen, huella, portadores))
            continue

        destino_id = destino["node_id"] if tipo == "nodo_propio" else destino
        if tipo == "nodo_propio":
            if destino_id in grafo:
                fallos.append("%s: el nodo propio %s YA EXISTE" % (origen, destino_id))
                continue
            creados.add(destino_id)
            dest = {"tipo": "nodo_propio", "motivo_p18": motivo, "nuevo": destino}
        else:
            if destino_id not in grafo and destino_id not in creados:
                fallos.append("%s: el destino %s no existe ni lo crea este plan" % (origen, destino_id))
                continue
            dest = {"tipo": "miembro", "nodo": destino_id, "motivo_p18": motivo}
            if destino_id in creados:
                dest["creado_por_este_plan"] = True
            else:
                dest["fuente_esperada_destino"] = grafo[destino_id]["fuente"]

        cortes.append({
            "origen": origen,
            "frontera": "los pasos %s de %d" % (idx, len(pasos)),
            "pasos_que_salen": idx,
            "fuente_queda": fuente_queda,
            "destino": dest,
            "pasos_totales": len(pasos),
            "fuente_esperada": d["fuente"],
            "huella": huella,
            "prefijos": [p[:34] for p in salen],
            "pasos_que_salen_texto": salen,
        })
        print("SELLADO: %-38s %-24s -> %s" % (origen, str(idx)[:24], destino_id))

    if fallos:
        print("\nPARADA: %d guarda(s) en rojo. No se sella nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    plan = {
        "operacion": "OP-F-04-HOR (menos decision_de_vender_startup, que va con TOQUE UNICO)",
        "fecha_corte": "2026-08-14",
        "desbloqueo": (
            "Acta de la vuelta 28 del auditor, adjudicacion 3, POR CITA del REGISTRO del "
            "fundador en la nota de OP-F-04-HOR de OPERACIONES.jsonl: la tanda NO esta "
            "bloqueada en bloque; familia propia es la familia del propio libro, en paralelo "
            "exacto con se reune con SPIN, con el Bullseye y con los 100 dias."
        ),
        "nomina_de_la_familia": (
            "Medida HOY, no copiada: 102 nodos vivos declaran el trozo Hard Thing y 88 lo "
            "declaran como fuente UNICA (docs/loop/SALIDA_V29_FAMILIA_HOROWITZ.txt)."
        ),
        "lo_que_no_entra": (
            "decision_de_vender_startup, 34 pasos, frontera 1 a 10 / 11 a 34, uno de LOS TRES "
            "CASOS QUE NO SON UN SIMPLE APENDICE: declara a Horowitz dos veces con dos grafias "
            "y su material esta repetido TRES veces (11 a 15, 16 a 20 y 21 a 25). Va al reporte "
            "como PARADA con su lectura."
        ),
        "cortes": cortes,
    }
    with open(SALIDA, "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=2)
    print("\nESCRITO: %s  (%d cortes, %d nodos propios nuevos)"
          % (SALIDA, len(cortes), len(creados)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
