# -*- coding: utf-8 -*-
r"""vuelta104_tarea4_2_barrido_especie28.py . VUELTA 104, TAREA 4.2: EL
BARRIDO DIRIGIDO POR LA ESPECIE DEL 28 (encargo del auditor, acta de la
vuelta 103, seccion 7, "RACHAS": tercera relectura al doble seguida del
tramo 1, esta vez ni por los extremos (vuelta 102) ni por el centro (vuelta
103), sino por la ESPECIE del par 28 (y del 29, TAREA 3 de esta vuelta):
un paso casado cuyo objeto real NO es lo que el hijo desarrolla, porque lo
que el hijo desarrolla esta nombrado en el paso solo como EJEMPLO, CONDICION
o dentro de una SUBORDINADA (de "cuando" o de finalidad).

SOBRE QUE PARES CORRE: las QUINCE RESUELTA del tramo 1 que ninguna relectura
anterior toco (acta 103, seccion 7: 1, 2, 4, 6, 8, 9, 14, 17, 18, 20, 21, 24,
25, 38, 39) mas las TREINTA Y TRES RESUELTA del tramo 2 (todas, calculadas
aqui con `direccion_efectiva`, no tecleadas): 48 pares en total.

QUE HACE, Y QUE NO HACE: para cada par imprime el `paso_casado` de la madre,
LEIDO HOY de `dataset/nodos/<madre>.json` (no tecleado de memoria), y el
VEREDICTO de la UNICA PREGUNTA del encargo (objeto del imperativo, o nombrado
como ejemplo/condicion/subordinada), CON EL VERBO Y EL OBJETO CITADOS
LITERALMENTE, para que el auditor pueda cotejarlos sin abrir el nodo. El
veredicto de cada par es LECTURA DIRIGIDA DEL EJECUTOR (juicio sobre texto,
no un calculo mecanico): este script GUARDA esa lectura en una tabla y la
CONTRASTA contra el texto real del paso en esta vuelta (si el paso citado ya
no coincide con lo que el nodo dice hoy, ROJO: el juicio quedo desactualizado
y no se publica sin revisarlo).

USO:
  python scripts/loop/vuelta104_tarea4_2_barrido_especie28.py

MECANICA DE ROJO: si el conteo de RESUELTA del tramo 2 no da 33, si algun
puesto de la lista del tramo 1 no existe o no esta RESUELTA hoy, o si el
texto del paso_casado leido hoy de dataset/nodos/ NO COINCIDE con el texto
contra el que se emitio el veredicto (declarado en la tabla de abajo), NO SE
IMPRIME LA TABLA y sale con exit 1.
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
TRAMO2 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

TRAMO1_PUESTOS = [1, 2, 4, 6, 8, 9, 14, 17, 18, 20, 21, 24, 25, 38, 39]

# LA LECTURA DIRIGIDA DEL EJECUTOR, puesto por puesto: (texto_paso_esperado,
# veredicto, verbo_citado, objeto_citado, motivo). texto_paso_esperado se
# contrasta contra dataset/nodos/ en tiempo de ejecucion (guarda de desfase).
LECTURA = {
    1: ("Sal del edificio (get out of the building) a observar como tus clientes viven el problema",
        "OBJETO", "Sal", "del edificio (get out of the building), a observar como tus clientes viven el problema",
        "el hijo esta nombrado LITERAL dentro del propio paso, como glosa en ingles del verbo mismo"),
    2: ("Implementar el programa 'Make Certain' para servicio y áreas administrativas",
        "OBJETO", "Implementar", "el programa 'Make Certain'",
        "objeto directo, nombra el programa que el hijo desarrolla"),
    4: ("Integra las metas de calidad en tus planes de negocio y de desempeño",
        "OBJETO", "Integra", "las metas de calidad en tus planes de negocio y de desempeño",
        "objeto directo mas complemento de destino; sin marca de ejemplo/condicion/cuando"),
    6: ("Decide si tu enfoque será solo ambiental o si vas a incluir también lo social y económico (triple bottom line)",
        "NO_OBJETO", "Decide", "si tu enfoque sera ambiental, o [decide] incluir tambien lo social y economico",
        "'(triple bottom line)' es una ETIQUETA PARENTETICA sobre UNA de las dos alternativas de una decision "
        "binaria; el objeto real del imperativo 'decide' es la eleccion de alcance, no el marco triple bottom line"),
    8: ("Verificar que el proceso de medición esté bajo control estadístico mediante carta de control",
        "NO_OBJETO", "Verificar", "que el proceso de medicion este bajo control estadistico (mediante carta de control)",
        "'capacidad de proceso' (el hijo) NO APARECE en el paso en ninguna forma: ni como objeto, ni como "
        "ejemplo ni como condicion. El paso verifica control estadistico de la MEDICION, no capacidad"),
    9: ("Haz un análisis de capacidad y revisa tus sistemas de medición",
        "OBJETO", "Haz", "un analisis de capacidad",
        "objeto directo del primer verbo coordinado, nombra 'capacidad' literalmente"),
    14: ("Implementar el programa 'Make Certain' para servicio y áreas administrativas",
         "OBJETO", "Implementar", "el programa 'Make Certain'",
         "mismo paso y mismo razonamiento que el puesto 2 (misma madre, distinto id de hijo)"),
    17: ("Muestrales tu producto minimo viable (MVP) y tu propuesta de valor para validar la solución",
         "OBJETO", "Muestrales", "tu producto minimo viable (MVP) y tu propuesta de valor",
         "objeto directo, el MVP esta nombrado como lo que se muestra, no como ejemplo de otra cosa"),
    18: ("Determinar si el proceso está en control estadístico y medir su capacidad a corto plazo",
         "OBJETO", "medir", "su capacidad a corto plazo",
         "dos imperativos coordinados por 'y'; 'capacidad' es objeto directo del SEGUNDO ('medir'), fuera "
         "de la clausula 'si' del primero"),
    20: ("Alinear el proceso de desarrollo de producto con el proceso de Customer Development.",
         "OBJETO", "Alinear", "el proceso de desarrollo de producto con el proceso de Customer Development",
         "complemento directo del verbo, nombra Customer Development sin marca de ejemplo/condicion"),
    21: ("Paso 0: Generar una hipótesis clara a partir de los Canvas de Value Proposition y Business Model",
         "OBJETO", "Generar", "una hipotesis clara a partir de los Canvas de Value Proposition y Business Model",
         "complemento de origen del verbo, sin marca de ejemplo/condicion/cuando"),
    24: ("Usar estas preguntas para minimizar preguntas de situación irrelevantes",
         "NO_OBJETO", "Usar", "estas preguntas (de problema)",
         "'preguntas de situacion' (el hijo) vive DENTRO de una subordinada de FINALIDAD ('para minimizar "
         "X'), no como objeto de 'usar': el objeto de 'usar' son las preguntas de PROBLEMA, no las de situacion"),
    25: ("Evaluar el centrado, ancho y forma del histograma para determinar capacidad del proceso",
         "NO_OBJETO", "Evaluar", "el centrado, ancho y forma del histograma",
         "'capacidad del proceso' (el hijo) vive DENTRO de una subordinada de FINALIDAD ('para determinar "
         "X'), no como objeto de 'evaluar': el objeto de 'evaluar' es el histograma"),
    38: ("Pon tu esfuerzo de mejora en las etapas de investigación y demostración de capacidad, no en el cierre",
         "OBJETO", "Pon", "tu esfuerzo de mejora en las etapas de investigacion y demostracion de capacidad",
         "complemento de destino directo, nombra 'etapa de investigacion' sin marca de ejemplo/condicion"),
    39: ("Incorporar análisis de condiciones latentes y defensas del sistema propio del modelo organizacional",
         "OBJETO", "Incorporar", "analisis de condiciones latentes y defensas del sistema",
         "objeto directo, nombra 'condiciones latentes' literalmente"),
    42: ("Preguntar 'qué es responsable' en vez de 'quién es responsable' ante cada incidente",
         "OBJETO", "Preguntar", "'que es responsable' en vez de 'quien es responsable'",
         "objeto directo, es exactamente la distincion que el hijo desarrolla"),
    45: ("Definir arenas estratégicas (mercados, tecnologías, sectores) donde enfocar los esfuerzos de innovación",
         "OBJETO", "Definir", "arenas estrategicas (mercados, tecnologias, sectores)",
         "objeto directo, nombra 'arenas estrategicas' literalmente"),
    46: ("Identifica tus hipótesis clave sobre el problema, el cliente y la solución",
         "OBJETO", "Identifica", "tus hipotesis clave sobre el problema, el cliente y la solucion",
         "'la solucion' es uno de los tres complementos del objeto directo, sin marca de ejemplo/condicion"),
    47: ("Identificar las causas raíz de las variaciones en actividades y costos",
         "OBJETO", "Identificar", "las causas raiz de las variaciones en actividades y costos",
         "objeto directo, nombra 'variaciones' literalmente"),
    48: ("Clasificar el proyecto como parte de los 'vitales pocos' o 'útiles muchos'",
         "OBJETO", "Clasificar", "el proyecto como parte de los 'vitales pocos' o 'utiles muchos'",
         "'como' es predicativo ('clasificar X como Y'), no marca de ejemplo; 'vitales pocos' es una de las "
         "dos categorias asignables, parte del objeto"),
    49: ("Diferenciar síntomas de causas en cada problema detectado",
         "OBJETO", "Diferenciar", "sintomas de causas",
         "objeto directo, nombra 'sintomas' literalmente"),
    52: ("Si es re-segmentación: comunicar comprensión única de un nicho o ventaja de bajo costo",
         "NO_OBJETO", "comunicar", "comprension unica de un nicho o ventaja de bajo costo",
         "el paso ENTERO empieza con 'Si es re-segmentacion:', CONDICION explicita; el hijo solo aplica "
         "dentro de esa rama condicional de un paso que cubre varias estrategias alternativas"),
    53: ("Identificar el proceso principal, su objetivo, y las necesidades del cliente",
         "OBJETO", "Identificar", "el proceso principal, su objetivo, y las necesidades del cliente",
         "objeto directo, nombra 'necesidades del cliente' literalmente"),
    57: ("Verificar que el proceso tenga capacidad real para cumplir las metas fijadas",
         "OBJETO", "Verificar", "que el proceso tenga capacidad real",
         "objeto (clausula) del verbo, nombra 'capacidad' literalmente dentro del objeto, no en subordinada aparte"),
    58: ("Identifica a tus clientes internos y externos y descubre sus necesidades",
         "OBJETO", "Identifica", "a tus clientes internos y externos",
         "objeto directo, nombra exactamente el hijo"),
    59: ("Haz una revisión después del lanzamiento para confirmar que se cumplió lo prometido.",
         "OBJETO", "Haz", "una revision despues del lanzamiento",
         "objeto directo, nombra 'revision post lanzamiento' literalmente"),
    61: ("Recordar que los términos de la ronda semilla suelen convertirse en precedente para rondas "
         "futuras, por lo que vale la pena negociarlos bien desde el inicio.",
         "OBJETO", "Recordar", "que los terminos de la ronda semilla suelen convertirse en precedente para rondas futuras",
         "objeto (clausula) del verbo, es exactamente el contenido que el hijo desarrolla"),
    62: ("No contrates equipo de ventas ni marketing hasta validar el modelo con hechos, no hipótesis",
         "NO_OBJETO", "No contrates", "equipo de ventas ni marketing",
         "'validar el modelo con hechos' (el hijo) vive DENTRO de una subordinada TEMPORAL ('hasta + "
         "infinitivo'), como limite de cuando dejar de aplicar la orden principal, no como su objeto"),
    64: ("Clasificar los defectos por gravedad, causa y responsabilidad",
         "OBJETO", "Clasificar", "los defectos por gravedad, causa y responsabilidad",
         "objeto directo, nombra 'clasificacion de seriedad de defectos' literalmente"),
    66: ("Balancear la necesidad de accountability con la protección al aprendizaje organizacional",
         "OBJETO", "Balancear", "la necesidad de accountability con la proteccion al aprendizaje organizacional",
         "complemento directo (con + N), nombra 'aprendizaje organizacional' literalmente"),
    73: ("Reducir tiempos de cambio (setup) para permitir lotes más pequeños",
         "OBJETO", "Reducir", "tiempos de cambio (setup)",
         "objeto directo, con glosa parentetica en ingles del propio objeto, no de otra cosa"),
    74: ("Desarrollar relaciones de largo plazo con proveedores que permitan conocer su cultura de calidad real",
         "OBJETO", "Desarrollar", "relaciones de largo plazo con proveedores",
         "objeto directo, nombra el hijo literalmente"),
    75: ("Iniciar al día siguiente el programa de eliminación de causas de error",
         "OBJETO", "Iniciar", "el programa de eliminacion de causas de error",
         "objeto directo; 'al dia siguiente' es adverbio de tiempo sobre CUANDO iniciar, no subordina al objeto"),
    77: ("Medir el impacto de la capacitación en el desempeño de los proyectos de mejora",
         "OBJETO", "Medir", "el impacto de la capacitacion en el desempeno de los proyectos de mejora",
         "objeto directo, nombra el hijo literalmente"),
    78: ("Capturar conocimiento competitivo y de mercado durante las entrevistas",
         "OBJETO", "Capturar", "conocimiento competitivo y de mercado",
         "objeto directo; 'durante las entrevistas' es adverbio de tiempo, no subordina el objeto"),
    80: ("Construir gráficos de corrida o distribuciones para detectar causas especiales de variación",
         "NO_OBJETO", "Construir", "graficos de corrida o distribuciones",
         "'causas especiales de variacion' vive DENTRO de una subordinada de FINALIDAD ('para detectar X'), "
         "no como objeto de 'construir'; ademas solo nombra 'especiales', nunca 'comunes', y el hijo es "
         "causas_comunes_vs_especiales: posible exceso/defecto de genero, misma familia que el 31"),
    83: ("Definir cómo vas a medir la calidad y el costo de la no calidad",
         "OBJETO", "Definir", "como vas a medir la calidad y el costo de la no calidad",
         "objeto (clausula) del verbo, nombra 'costo de la no calidad' literalmente"),
    84: ("Define y comunica tu visión y tu estrategia de innovación conectadas con hacia dónde va tu negocio.",
         "OBJETO", "Define", "tu vision y tu estrategia de innovacion",
         "objeto directo, nombra el hijo literalmente"),
    87: ("Evalúa ese trabajo con la contabilidad de innovación, no con las métricas tradicionales de un puesto operativo.",
         "OBJETO", "Evalua", "ese trabajo con la contabilidad de innovacion",
         "complemento directo (con + N), nombra 'contabilidad de innovacion' literalmente, sin marca de ejemplo/condicion"),
    88: ("Salir físicamente a hablar con clientes potenciales reales, no solo encuestas remotas, lo que se "
         "llama get out of the building",
         "OBJETO", "Salir", "fisicamente a hablar con clientes potenciales reales",
         "el hijo esta nombrado LITERAL como apositivo del propio verbo ('lo que se llama get out of the building')"),
    91: ("Establecer gates o puntos de decisión formales con criterios visibles de Go/Kill",
         "OBJETO", "Establecer", "gates o puntos de decision formales con criterios visibles de Go/Kill",
         "objeto directo, nombra 'criterios de gate' literalmente"),
    92: ("Definir el mercado objetivo, posicionamiento y propuesta de valor del producto",
         "OBJETO", "Definir", "el mercado objetivo, posicionamiento y propuesta de valor",
         "objeto directo, nombra 'posicionamiento' literalmente"),
    93: ("Documentar el estándar con definiciones operacionales claras y medibles.",
         "OBJETO", "Documentar", "el estandar con definiciones operacionales claras y medibles",
         "complemento directo (con + N), nombra el hijo literalmente"),
    94: ("Finalmente, validar que el modelo de negocio completo (socios, canales, ingresos, costos) es "
         "viable (rectángulo)",
         "OBJETO", "validar", "que el modelo de negocio completo (socios, canales, ingresos, costos) es viable",
         "objeto (clausula) del verbo, es el modelo financiero/de negocio completo que el hijo valida"),
    97: ("Alinear estrategias, sistemas y metas de largo plazo con el propósito central",
         "OBJETO", "Alinear", "estrategias, sistemas y metas de largo plazo",
         "objeto directo, nombra 'estrategias de largo plazo' literalmente"),
    98: ("Definir tareas especiales y buenas prácticas de manufactura requeridas",
         "OBJETO", "Definir", "tareas especiales y buenas practicas de manufactura requeridas",
         "objeto directo, nombra cGMP literalmente"),
    99: ("Analizar y diagnosticar: analizar síntomas, formular teorías, probarlas e identificar la causa raíz",
         "OBJETO", "probarlas", "[las teorias de causa raiz]",
         "objeto directo de uno de los verbos coordinados de la enumeracion, sin marca de ejemplo/condicion"),
    100: ("Filtra y prioriza las metas que entraran en tu plan de negocio",
          "OBJETO", "Filtra y prioriza", "las metas que entraran en tu plan de negocio",
          "objeto directo, nombra 'metas de negocio' literalmente"),
}


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def direccion_efectiva(f):
    valor = f.get("direccion_leida")
    for k in sorted(x for x in f if x.startswith("correccion_v")):
        c = f[k]
        if c.get("campo_corregido") == "direccion_leida":
            valor = c.get("valor_nuevo")
    return valor


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []

    t1 = {f["puesto_tramo"]: f for f in cargar(TRAMO1)}
    t2 = {f["puesto_tramo"]: f for f in cargar(TRAMO2)}
    resueltas2 = sorted(p for p, f in t2.items() if direccion_efectiva(f))
    if len(resueltas2) != 33:
        fallos.append("tramo2 trae %d RESUELTA, se esperaban 33" % len(resueltas2))

    for p in TRAMO1_PUESTOS:
        f = t1.get(p)
        if f is None:
            fallos.append("puesto_tramo %d no existe en tramo1" % p)
            continue
        if not direccion_efectiva(f):
            fallos.append("puesto_tramo %d del tramo1 ya NO esta RESUELTA (correccion posterior)" % p)

    pares = [(p, t1[p], "tramo1") for p in TRAMO1_PUESTOS] + [(p, t2[p], "tramo2") for p in resueltas2]
    if len(pares) != 48:
        fallos.append("total de pares %d, se esperaban 48" % len(pares))

    filas = []
    for p, f, tramo in pares:
        if p not in LECTURA:
            fallos.append("puesto %d no tiene lectura registrada" % p)
            continue
        texto_esperado, veredicto, verbo, objeto, motivo = LECTURA[p]
        madre_id = f["madre_de_la_bolsa"]
        pc = f["paso_casado"]
        ruta_madre = os.path.join(NODOS, "%s.json" % madre_id)
        if not os.path.exists(ruta_madre):
            fallos.append("puesto %d: no existe dataset/nodos/%s.json" % (p, madre_id))
            continue
        madre = json.load(io.open(ruta_madre, encoding="utf-8"))
        pasos = madre.get("pasos_accionables", [])
        texto_real = pasos[pc - 1] if 1 <= pc <= len(pasos) else None
        if texto_real != texto_esperado:
            fallos.append("puesto %d: el paso %d de %s hoy dice %r, DISTINTO del texto contra el que "
                          "se emitio el veredicto (%r): DESFASE, revisar antes de publicar"
                          % (p, pc, madre_id, texto_real, texto_esperado))
            continue
        filas.append((p, tramo, madre_id, f["hijo_de_la_bolsa"], pc, verbo, objeto, veredicto, motivo))

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME LA TABLA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("BARRIDO DIRIGIDO POR LA ESPECIE DEL 28, TAREA 4.2 VUELTA 104: %d pares "
          "(15 del tramo 1 nunca releidos + %d RESUELTA del tramo 2)" % (len(filas), len(resueltas2)))
    print("=" * 100)
    no_objeto = [f for f in filas if f[7] == "NO_OBJETO"]
    for p, tramo, madre_id, hijo_id, pc, verbo, objeto, veredicto, motivo in filas:
        print()
        print("--- PUESTO %d (%s) --- %s -> %s (paso %d)" % (p, tramo, madre_id, hijo_id, pc))
        print("  verbo citado: %r" % verbo)
        print("  objeto citado: %r" % objeto)
        print("  VEREDICTO: %s -- %s" % (veredicto, motivo))
    print()
    print("=" * 100)
    print("RESUMEN: %d de %d pares dan OBJETO (se sostienen sin re-lectura); %d dan NO_OBJETO "
          "y van a lectura entera (TAREA 4.3): %s"
          % (len(filas) - len(no_objeto), len(filas), len(no_objeto),
             ", ".join(str(f[0]) for f in no_objeto)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
