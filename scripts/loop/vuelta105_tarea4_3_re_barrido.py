# -*- coding: utf-8 -*-
r"""vuelta105_tarea4_3_re_barrido.py . VUELTA 105, TAREA 4.1 y 4.3: LA GUARDA
DEL PASO MAL CASADO Y EL RE-BARRIDO CON LA PREGUNTA COMPLETA (encargo del
auditor, acta de la vuelta 104).

SUCESOR DECLARADO de scripts/loop/vuelta104_tarea4_2_barrido_especie28.py, al
que NO reemplaza (aquella tabla queda como esta, con su bendicion ya
retirada en docs/plan/04_ENLACES.md). Corre SOBRE LOS 41 PARES que aquella
vuelta dio OBJETO.

(4.1) LA GUARDA DEL PASO MAL CASADO, QUE ES BARATA: antes de emitir
veredicto sobre un puesto, se lee su `razon` en el registro
(`docs/plan/OP_E_03_LECTURA_TRAMO{1,2}_V9{6,7}.jsonl`) y, si trae la nota de
paso mal casado (la misma que censa
scripts/loop/vuelta105_tarea4_censo_paso_mal_casado.py), el puesto SALTA: no
se emite veredicto contra el, se imprime el motivo y se sigue con el
siguiente. Caso positivo, medido: el 46 salta.

(4.3) EL RE-BARRIDO, TRES RESPUESTAS EN VEZ DE DOS. La lectura dirigida del
ejecutor (mismo verbo y objeto citados que la vuelta 104, mas la
reclasificacion de esta vuelta) contesta, para cada puesto que NO salto por
(4.1): OBJETO (el hijo es el objeto del imperativo), SATELITE (esta
nombrado, pero en complemento preposicional: de origen, de destino, o
instrumental "con + N"), o NO_OBJETO (ejemplo, condicion o subordinada; esta
respuesta ya no deberia aparecer aqui porque el pool de entrada son los 41
que YA dieron OBJETO en la vuelta 104, pero se deja la rama por si una
relectura mas fina cambia de opinion).

MECANICA DE ROJO: identica a la del padre (vuelta104_tarea4_2_...): si el
texto del paso_casado leido HOY de dataset/nodos/ no coincide con el texto
contra el que se emitio el veredicto, NO SE IMPRIME LA TABLA y sale exit 1.

USO:
  python scripts/loop/vuelta105_tarea4_3_re_barrido.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
TRAMO2 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

RE_PASO_MAL_CASADO = re.compile(r"el barrido cas\w* el paso\s*\d+", re.IGNORECASE)

# LOS 41 PARES QUE LA VUELTA 104 DIO OBJETO (SALIDA_V104_TAREA4_2_BARRIDO.txt),
# EN EL MISMO ORDEN. Puesto: (texto_paso_esperado, verbo, objeto, veredicto_v104).
LECTURA_V104 = {
    1: ("Sal del edificio (get out of the building) a observar como tus clientes viven el problema",
        "Sal", "del edificio (get out of the building), a observar como tus clientes viven el problema"),
    2: ("Implementar el programa 'Make Certain' para servicio y áreas administrativas",
        "Implementar", "el programa 'Make Certain'"),
    4: ("Integra las metas de calidad en tus planes de negocio y de desempeño",
        "Integra", "las metas de calidad en tus planes de negocio y de desempeño"),
    9: ("Haz un análisis de capacidad y revisa tus sistemas de medición",
        "Haz", "un analisis de capacidad"),
    14: ("Implementar el programa 'Make Certain' para servicio y áreas administrativas",
         "Implementar", "el programa 'Make Certain'"),
    17: ("Muestrales tu producto minimo viable (MVP) y tu propuesta de valor para validar la solución",
         "Muestrales", "tu producto minimo viable (MVP) y tu propuesta de valor"),
    18: ("Determinar si el proceso está en control estadístico y medir su capacidad a corto plazo",
         "medir", "su capacidad a corto plazo"),
    20: ("Alinear el proceso de desarrollo de producto con el proceso de Customer Development.",
         "Alinear", "el proceso de desarrollo de producto con el proceso de Customer Development"),
    21: ("Paso 0: Generar una hipótesis clara a partir de los Canvas de Value Proposition y Business Model",
         "Generar", "una hipotesis clara a partir de los Canvas de Value Proposition y Business Model"),
    38: ("Pon tu esfuerzo de mejora en las etapas de investigación y demostración de capacidad, no en el cierre",
         "Pon", "tu esfuerzo de mejora en las etapas de investigacion y demostracion de capacidad"),
    39: ("Incorporar análisis de condiciones latentes y defensas del sistema propio del modelo organizacional",
         "Incorporar", "analisis de condiciones latentes y defensas del sistema"),
    42: ("Preguntar 'qué es responsable' en vez de 'quién es responsable' ante cada incidente",
         "Preguntar", "'que es responsable' en vez de 'quien es responsable'"),
    45: ("Definir arenas estratégicas (mercados, tecnologías, sectores) donde enfocar los esfuerzos de innovación",
         "Definir", "arenas estrategicas (mercados, tecnologias, sectores)"),
    46: ("Identifica tus hipótesis clave sobre el problema, el cliente y la solución",
         "Identifica", "tus hipotesis clave sobre el problema, el cliente y la solucion"),
    47: ("Identificar las causas raíz de las variaciones en actividades y costos",
         "Identificar", "las causas raiz de las variaciones en actividades y costos"),
    48: ("Clasificar el proyecto como parte de los 'vitales pocos' o 'útiles muchos'",
         "Clasificar", "el proyecto como parte de los 'vitales pocos' o 'utiles muchos'"),
    49: ("Diferenciar síntomas de causas en cada problema detectado",
         "Diferenciar", "sintomas de causas"),
    53: ("Identificar el proceso principal, su objetivo, y las necesidades del cliente",
         "Identificar", "el proceso principal, su objetivo, y las necesidades del cliente"),
    57: ("Verificar que el proceso tenga capacidad real para cumplir las metas fijadas",
         "Verificar", "que el proceso tenga capacidad real"),
    58: ("Identifica a tus clientes internos y externos y descubre sus necesidades",
         "Identifica", "a tus clientes internos y externos"),
    59: ("Haz una revisión después del lanzamiento para confirmar que se cumplió lo prometido.",
         "Haz", "una revision despues del lanzamiento"),
    61: ("Recordar que los términos de la ronda semilla suelen convertirse en precedente para rondas "
         "futuras, por lo que vale la pena negociarlos bien desde el inicio.",
         "Recordar", "que los terminos de la ronda semilla suelen convertirse en precedente para rondas futuras"),
    64: ("Clasificar los defectos por gravedad, causa y responsabilidad",
         "Clasificar", "los defectos por gravedad, causa y responsabilidad"),
    66: ("Balancear la necesidad de accountability con la protección al aprendizaje organizacional",
         "Balancear", "la necesidad de accountability con la proteccion al aprendizaje organizacional"),
    73: ("Reducir tiempos de cambio (setup) para permitir lotes más pequeños",
         "Reducir", "tiempos de cambio (setup)"),
    74: ("Desarrollar relaciones de largo plazo con proveedores que permitan conocer su cultura de calidad real",
         "Desarrollar", "relaciones de largo plazo con proveedores"),
    75: ("Iniciar al día siguiente el programa de eliminación de causas de error",
         "Iniciar", "el programa de eliminacion de causas de error"),
    77: ("Medir el impacto de la capacitación en el desempeño de los proyectos de mejora",
         "Medir", "el impacto de la capacitacion en el desempeno de los proyectos de mejora"),
    78: ("Capturar conocimiento competitivo y de mercado durante las entrevistas",
         "Capturar", "conocimiento competitivo y de mercado"),
    83: ("Definir cómo vas a medir la calidad y el costo de la no calidad",
         "Definir", "como vas a medir la calidad y el costo de la no calidad"),
    84: ("Define y comunica tu visión y tu estrategia de innovación conectadas con hacia dónde va tu negocio.",
         "Define", "tu vision y tu estrategia de innovacion"),
    87: ("Evalúa ese trabajo con la contabilidad de innovación, no con las métricas tradicionales de un puesto operativo.",
         "Evalua", "ese trabajo con la contabilidad de innovacion"),
    88: ("Salir físicamente a hablar con clientes potenciales reales, no solo encuestas remotas, lo que se "
         "llama get out of the building",
         "Salir", "fisicamente a hablar con clientes potenciales reales"),
    91: ("Establecer gates o puntos de decisión formales con criterios visibles de Go/Kill",
         "Establecer", "gates o puntos de decision formales con criterios visibles de Go/Kill"),
    92: ("Definir el mercado objetivo, posicionamiento y propuesta de valor del producto",
         "Definir", "el mercado objetivo, posicionamiento y propuesta de valor"),
    93: ("Documentar el estándar con definiciones operacionales claras y medibles.",
         "Documentar", "el estandar con definiciones operacionales claras y medibles"),
    94: ("Finalmente, validar que el modelo de negocio completo (socios, canales, ingresos, costos) es "
         "viable (rectángulo)",
         "validar", "que el modelo de negocio completo (socios, canales, ingresos, costos) es viable"),
    97: ("Alinear estrategias, sistemas y metas de largo plazo con el propósito central",
         "Alinear", "estrategias, sistemas y metas de largo plazo"),
    98: ("Definir tareas especiales y buenas prácticas de manufactura requeridas",
         "Definir", "tareas especiales y buenas practicas de manufactura requeridas"),
    99: ("Analizar y diagnosticar: analizar síntomas, formular teorías, probarlas e identificar la causa raíz",
         "probarlas", "[las teorias de causa raiz]"),
    100: ("Filtra y prioriza las metas que entraran en tu plan de negocio",
          "Filtra y prioriza", "las metas que entraran en tu plan de negocio"),
}

TRAMO1_PUESTOS_POOL = {1, 2, 4, 9, 14, 17, 18, 20, 21, 38, 39}

# (TAREA 4.3) LA RECLASIFICACION DE ESTA VUELTA: OBJETO o SATELITE (con su
# motivo), aplicando la regla del encargo (complemento preposicional de
# origen/destino/instrumental "con+N" = SATELITE). Los siete que el auditor
# ya nombro (20, 21, 38, 66, 87, 91, 93; el 46 queda fuera, SALTA por 4.1)
# se confirman aqui con la MISMA lectura; los 33 restantes (mas el 1 y el 88,
# que son APOSICION LITERAL, especie distinta del complemento preposicional
# y por eso quedan OBJETO) se releyeron con la misma regla y NINGUNO cambia:
# es el resultado, no un cero forzado.
VEREDICTO_3VIAS = {
    1: ("OBJETO", "aposicion literal (glosa en ingles que ES el hijo, no complemento que lo aloja): "
                  "misma especie que el 88, no la que el encargo pide reclasificar"),
    2: ("OBJETO", "objeto directo, nombra el programa que el hijo desarrolla"),
    4: ("OBJETO", "objeto directo primero; 'en tus planes...' es complemento ADICIONAL, no el unico lugar "
                  "donde vive el hijo"),
    9: ("OBJETO", "objeto directo del primer verbo coordinado, nombra 'capacidad' literalmente"),
    14: ("OBJETO", "mismo paso y mismo razonamiento que el puesto 2"),
    17: ("OBJETO", "objeto directo, el MVP esta nombrado como lo que se muestra"),
    18: ("OBJETO", "objeto directo del segundo verbo coordinado"),
    20: ("SATELITE", "complemento directo 'con + N' (con el proceso de Customer Development): el hijo vive "
                     "en el termino regido por 'con', no en el objeto directo del verbo 'alinear'"),
    21: ("SATELITE", "complemento de origen del verbo ('a partir de los Canvas...')"),
    38: ("SATELITE", "complemento de destino directo ('en las etapas de investigacion...')"),
    39: ("OBJETO", "objeto directo, nombra 'condiciones latentes' literalmente"),
    42: ("OBJETO", "objeto directo, es exactamente la distincion que el hijo desarrolla"),
    45: ("OBJETO", "objeto directo, nombra 'arenas estrategicas' literalmente"),
    47: ("OBJETO", "objeto directo, nombra 'variaciones' literalmente"),
    48: ("OBJETO", "'como' es predicativo, no marca de ejemplo; parte del objeto"),
    49: ("OBJETO", "objeto directo, nombra 'sintomas' literalmente"),
    53: ("OBJETO", "objeto directo, nombra 'necesidades del cliente' literalmente"),
    57: ("OBJETO", "objeto (clausula) del verbo, nombra 'capacidad' dentro del objeto mismo"),
    58: ("OBJETO", "objeto directo con 'a' personal, nombra exactamente el hijo"),
    59: ("OBJETO", "objeto directo, nombra 'revision post lanzamiento' literalmente"),
    61: ("OBJETO", "objeto (clausula) del verbo, es exactamente el contenido que el hijo desarrolla"),
    64: ("OBJETO", "objeto directo, nombra 'clasificacion de seriedad de defectos' literalmente"),
    66: ("SATELITE", "complemento directo 'con + N' (con la proteccion al aprendizaje organizacional)"),
    73: ("OBJETO", "objeto directo, con glosa parentetica del propio objeto"),
    74: ("OBJETO", "'con proveedores' integra el objeto directo mismo ('relaciones... con proveedores'), "
                   "no gobierna el tema del hijo desde fuera"),
    75: ("OBJETO", "objeto directo; 'al dia siguiente' es adverbio de tiempo, no aloja al hijo"),
    77: ("OBJETO", "objeto directo, nombra el hijo literalmente"),
    78: ("OBJETO", "objeto directo; 'durante las entrevistas' es adverbio de tiempo, no aloja al hijo"),
    83: ("OBJETO", "objeto (clausula) del verbo, nombra 'costo de la no calidad' literalmente"),
    84: ("OBJETO", "objeto directo, nombra el hijo literalmente"),
    87: ("SATELITE", "complemento directo 'con + N' (con la contabilidad de innovacion)"),
    88: ("OBJETO", "aposicion literal ('lo que se llama get out of the building' ES el hijo)"),
    91: ("SATELITE", "'con criterios visibles de Go/Kill' gobierna el tema del hijo desde fuera del objeto "
                     "directo ('gates o puntos de decision formales')"),
    92: ("OBJETO", "objeto directo, nombra 'posicionamiento' literalmente"),
    93: ("SATELITE", "complemento directo 'con + N' (con definiciones operacionales)"),
    94: ("OBJETO", "objeto (clausula) del verbo, es el modelo financiero completo que el hijo valida"),
    97: ("OBJETO", "objeto directo, nombra 'estrategias de largo plazo' literalmente"),
    98: ("OBJETO", "objeto directo, nombra cGMP literalmente"),
    99: ("OBJETO", "objeto directo de uno de los verbos coordinados"),
    100: ("OBJETO", "objeto directo, nombra 'metas de negocio' literalmente"),
}


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []

    t1 = {f["puesto_tramo"]: f for f in cargar(TRAMO1)}
    t2 = {f["puesto_tramo"]: f for f in cargar(TRAMO2)}

    saltan = []
    filas = []
    for p in sorted(LECTURA_V104):
        f = t1.get(p) if p in TRAMO1_PUESTOS_POOL else t2.get(p)
        if f is None:
            fallos.append("puesto %d no existe en su tramo" % p)
            continue
        razon = f.get("razon", "")
        m = RE_PASO_MAL_CASADO.search(razon)
        if m:
            saltan.append((p, f["madre_de_la_bolsa"], f["hijo_de_la_bolsa"],
                          razon[max(0, m.start() - 20):m.end() + 100]))
            continue

        texto_esperado, verbo, objeto = LECTURA_V104[p]
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
                          "se emitio el veredicto: DESFASE, revisar antes de publicar" % (p, pc, madre_id, texto_real))
            continue
        if p not in VEREDICTO_3VIAS:
            fallos.append("puesto %d no tiene reclasificacion de 3 vias" % p)
            continue
        veredicto, motivo = VEREDICTO_3VIAS[p]
        filas.append((p, madre_id, f["hijo_de_la_bolsa"], pc, verbo, objeto, veredicto, motivo))

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME LA TABLA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("RE-BARRIDO CON LA PREGUNTA COMPLETA, TAREA 4.3 VUELTA 105: %d de %d puestos del pool "
          "(los que no traen nota de paso mal casado)" % (len(filas), len(LECTURA_V104)))
    print("=" * 100)
    if saltan:
        print()
        print("SALTAN %d puesto(s) por (4.1), nota de paso mal casado (NO se emite veredicto):" % len(saltan))
        for p, madre_id, hijo_id, frag in saltan:
            print("  puesto %d: %s -> %s -- %s" % (p, madre_id, hijo_id, frag))

    satelite = [f for f in filas if f[6] == "SATELITE"]
    objeto = [f for f in filas if f[6] == "OBJETO"]
    no_objeto = [f for f in filas if f[6] == "NO_OBJETO"]
    for p, madre_id, hijo_id, pc, verbo, obj, veredicto, motivo in filas:
        print()
        print("--- PUESTO %d --- %s -> %s (paso %d)" % (p, madre_id, hijo_id, pc))
        print("  verbo citado: %r" % verbo)
        print("  objeto citado: %r" % obj)
        print("  VEREDICTO: %s -- %s" % (veredicto, motivo))

    print()
    print("=" * 100)
    print("RESUMEN: OBJETO %d, SATELITE %d, NO_OBJETO %d (de %d clasificados; %d SALTAN por 4.1)"
          % (len(objeto), len(satelite), len(no_objeto), len(filas), len(saltan)))
    print("SATELITE (van a lectura entera, TAREA 4.4): %s" % ", ".join(str(f[0]) for f in satelite))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
