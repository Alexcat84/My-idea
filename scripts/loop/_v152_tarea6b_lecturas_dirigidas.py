# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.b: LAS 121 LECTURAS DIRIGIDAS DE LOS PARES
BIDIRECCIONALES SIN VEREDICTO, POR P.5, EN TRES TRAMOS.

CADA VEREDICTO ES UNA LECTURA, NO UN SELLO. Se leyo el dossier entero
(docs/loop/SALIDA_V152_T6B_DOSSIER.txt, 3.124 lineas, los 121 pares con el
titulo y los pasos accionables de sus dos nodos) y se aplico la vara del banco
9.22 EN LOS DOS SENTIDOS, que es lo que la figura exige:

  PROCEDIMIENTO en los dos sentidos sobre DOS LINEAS DISTINTAS -> C, ENLACE
    MUTUO, y las dos aristas se quedan.
  LINEA en los dos sentidos -> A, FUSION: es el mismo material dos veces.
  La comprobacion que las separa: si las dos direcciones apuntan A LA MISMA
    LINEA, no es enlace mutuo.

EL RESULTADO ES UNIFORME Y ESO OBLIGA A DECIRLO EN VOZ ALTA: los 121 salen C.
No es que la vara se haya aflojado para llegar al verde, y por eso van
MARCADOS COMO DISCUTIBLES los cuatro pares donde el solape de linea es real y
la clase se sostiene por poco. Un lector que discrepe tiene que ir a esos
cuatro, no a los 121. Estan en DISCUTIBLES, abajo, con su motivo.

POR QUE NINGUNO ES ESCALERA. La escalera del 9.22 es "la vuelta manda al lector
a repetir el paso que acaba de dar". En los 121 pares los dos nodos son
PROCEDIMIENTOS COMPLETOS Y DISTINTOS del curriculo (bloques distintos del
Canvas, pasos distintos del programa de Crosby, planes distintos del PMBOK,
canales distintos de traccion), y cada direccion manda al lector a un
procedimiento que el otro nodo NO contiene. Eso es exactamente el primer polo.

LA VIA. La decision del fundador nombra dos vias automaticas (cribado y P.10) y
manda TODO LO DEMAS a lectura dirigida por P.5. Estas 121 son esa lectura, y su
via en el registro es LECTURA_DIRIGIDA. n NO SE MUEVE: el archivo del cribado
no se toca, sigue en 3.388 lineas.

USO:
  python scripts/loop/_v152_tarea6b_lecturas_dirigidas.py --tramo 1
  python scripts/loop/_v152_tarea6b_lecturas_dirigidas.py --todos --escribir
"""
import argparse
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LISTA = os.path.join(RAIZ, "docs", "loop", "_v152_lista_121.txt")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")

# n -> (clase, motivo). El motivo nombra QUE LINEA expande cada direccion.
# Sin `|` en el texto: el registro se lee con un patron de tabla.
M = {
1: ("C", "el paso 6 de Crosby (fichar, revisar y escalar cada problema hasta la causa raiz) contra el estandar ZD y su dia de lanzamiento: cada uno expande un procedimiento que el otro no contiene"),
2: ("C", "dos bloques distintos del Canvas: que ACTIVIDADES exige la propuesta contra que RECURSOS fisicos, financieros, de talento y de propiedad intelectual hacen falta"),
3: ("C", "estimar duraciones por metodo (parametrico, analogo, tres puntos) contra construir el cronograma con dependencias, recursos y ruta: el paso 1 del cronograma consume la salida del otro y no la repite"),
4: ("C", "el tune-up semanal del Canvas con el feedback recibido contra la estrategia de pivote por reempaquetado (modulos, suscripcion, versiones): uno actualiza el lienzo, el otro decide que cambiar"),
5: ("C", "el objetivo del liderazgo de Deming (ayudar y reducir variabilidad entre personas) contra el procedimiento estadistico de 15 pasos que separa causa comun de causa especial"),
6: ("C", "alinear la TECNOLOGIA con el modelo de negocio (aplicaciones, datos, infraestructura, seguridad) contra alinear la ORGANIZACION con el Modelo Estrella (estrategia, estructura, procesos, recompensas, personas)"),
7: ("C", "el perfil motivacional del fundador con sus 13 motivaciones contra los tres factores de CUANDO fundar (carrera, mercado, personales): distinto sujeto y distinta decision"),
8: ("C", "DISCUTIBLE 1. El paso 5 de motivaciones nombra el dilema riqueza contra control, que es el otro nodo entero. Se sostiene C porque motivaciones expande las influencias familiares y las 13 motivaciones, y el dilema expande el trade off en CADA decision de financiamiento"),
9: ("C", "analizar y sintetizar datos de campo en una historia coherente contra alternar deliberadamente fases divergentes y convergentes: uno es el metodo de interpretacion, el otro el ritmo del proceso"),
10: ("C", "la antidilucion (weighted average contra full ratchet, carve outs, waiver) contra el pay to play y su Qualified Financing: dos clausulas distintas del mismo term sheet"),
11: ("C", "la antidilucion contra la preferencia de liquidacion con su participante contra no participante, sus kick outs y su analisis de cascada"),
12: ("C", "el METODO de asignar recursos en el gate contra el DIAGNOSTICO del gate hueco que aprueba sin recursos: uno instala la practica, el otro la audita"),
13: ("C", "la auditoria de posicionamiento (cuestionario externo e interno, entrevistas, comparar percepciones) contra redactar la declaracion de posicionamiento: medir contra escribir"),
14: ("C", "la auditoria de negocio de cinco pasos contra el consejo de calidad de Juran de once, que la encarga y decide los proyectos"),
15: ("C", "el brief competitivo y su razon de compra contra la entrada a un mercado nuevo con sus mercados adyacentes y su presupuesto de educacion"),
16: ("C", "la diana de traccion con sus 19 canales y sus experimentos baratos contra el camino critico que excluye lo que no es imprescindible"),
17: ("C", "el Canvas usado como scorecard SEMANAL con sus cambios en rojo contra el pivote estrategico basado en evidencia: uno es la cadencia, el otro la decision"),
18: ("C", "mapear el entorno del modelo (fuerzas de mercado, industria, tendencias, macro) contra construir escenarios cruzando impulsores de incertidumbre"),
19: ("C", "calcular el ROI cash on cash del franquiciado contra decidir entre franquiciar, unidades propias o capital externo: uno alimenta al otro con una cifra"),
20: ("C", "calibrar tu juicio con rangos al noventa por ciento contra el analisis de sensibilidad que elige que incertidumbre reducir"),
21: ("C", "calidad de diseno contra calidad de produccion y su brecha, frente al COPQ y sus cuatro categorias de costo"),
22: ("C", "el bloque de Canales del Canvas con sus cinco fases contra los eventos presenciales como canal concreto de traccion"),
23: ("C", "armar el cap table basico (pre y post money, bolsa de opciones) contra convertir notas convertibles por tres metodos distintos"),
24: ("C", "el procedimiento estadistico que separa causas contra la mejora continua diaria de Deming, que pregunta que se hizo hoy para mejorar"),
25: ("C", "el checklist de un Stage Gate de primera clase contra la desmitificacion de lo que Stage Gate NO es: uno construye, el otro desmonta creencias"),
26: ("C", "la efectividad del cierre segun complejidad de venta contra el cuestionario de 15 afirmaciones que mide la ACTITUD del vendedor hacia el cierre"),
27: ("C", "la efectividad del cierre segun complejidad contra la metodologia SPIN y su diagnostico de venta pequena o grande"),
28: ("C", "designar al maestro de los cinco porques y su regla de disparo contra la sesion misma con inversion proporcional al nivel del problema"),
29: ("C", "la clausula no shop de 45 a 60 dias contra la lista de condiciones de cierre del LOI"),
30: ("C", "construir comunidad con mision, meta discusion y moderacion delegada contra organizar eventos presenciales con precio, espacio y auspiciantes"),
31: ("C", "DISCUTIBLE 2, EL MAS AJUSTADO DE LOS CUATRO. El paso 1 de compatibilidad y el paso 2 del dilema son casi la misma linea. Se sostiene C porque el sujeto es distinto: compatibilidad se pregunta por TI Y TU SOCIO antes de asociarse, el dilema se pregunta por TI SOLO en cada decision de financiamiento"),
32: ("C", "pedir compromiso de fecha y respuesta si o no contra la secuencia SPIN de preguntas de situacion, problema, implicacion y necesidad beneficio"),
33: ("C", "la concepcion hormica que permite que el pensamiento avance a saltos contra las cuatro etapas de Wallas con su incubacion e iluminacion"),
34: ("C", "conectar con datos personales y emocionales contra el redisenio de 16 pasos de los procesos internos que generan friccion"),
35: ("C", "la teoria de restricciones con sus cinco pasos de foco contra el rediseno del flujo de push a pull con kanbans"),
36: ("C", "gestionar el contacto directo con el cliente y a quien lo atiende contra redisenar los procesos internos que producen la experiencia"),
37: ("C", "cerrar el contrato (disputas resueltas, aceptacion, pagos finales) contra el informe periodico de estado del contratista durante la ejecucion"),
38: ("C", "el SPC y sus diez pasos para construir la carta contra el plan de control que define quien mide, quien actua y como se vuelve a control"),
39: ("C", "validar estadisticamente el METODO DE MEDICION contra escribir definiciones operacionales que hagan reproducible un adjetivo ambiguo"),
40: ("C", "el plan de gestion de costos con sus umbrales de varianza contra el registro de interesados con su influencia y su postura"),
41: ("C", "el COPQ medido con tus registros contables contra el modelo del costo optimo y su punto de interseccion de curvas"),
42: ("C", "DISCUTIBLE 3, Y ES DE INSTRUMENTO ANTES QUE DE LECTURA. Este par SOLO existe tras resolver alias: el dossier muestra copq cableando a rejilla en nodos_previos y rejilla a copq en nodos_siguientes, y la ida y vuelta aparece por la resolucion. La lectura se sostiene igual: el COPQ mide costo, la rejilla ubica al negocio en una de cinco etapas de madurez"),
43: ("C", "el COPQ contra la trilogia de Juran (planificar, controlar, mejorar) y su distincion entre pico esporadico y desperdicio cronico"),
44: ("C", "la funcion Govern del NIST CSF contra los perfiles Current y Target y sus Tiers: una gobierna, la otra mide la brecha"),
45: ("C", "las cuatro etapas de Wallas contra la ruptura deliberada de habitos cuando detectas estancamiento"),
46: ("C", "la cultura de aprendizaje y su ciclo de reformas contra los cuatro subcomponentes de la cultura de seguridad"),
47: ("C", "mapear el viaje del cliente con shadowing y momentos de verdad contra la economia de la experiencia y su paso de consumo pasivo a participacion"),
48: ("C", "la hoja de necesidades del cliente correlacionadas contra el SIPOC que define proveedores, insumos, proceso, salidas y clientes"),
49: ("C", "la decision de pivotar o proceder contra el lienzo mismo y sus doce pasos de construccion"),
50: ("C", "la decision de pivotar o proceder contra validar el modelo financiero (CAC, LTV, runway, P and L)"),
51: ("C", "mapear las capas de defensa y sus dependencias ocultas contra separar fallas activas de condiciones latentes"),
52: ("C", "alinear la cadena de suministro con la estrategia contra el balance concreto entre responsividad y eficiencia en los cinco drivers"),
53: ("C", "los niveles de madurez en gestion de riesgo contra la regla de empezar con dos o tres practicas simples y probadas"),
54: ("C", "preparar la reunion de presentacion del problema (una diapositiva, tres columnas) contra las cuatro preguntas IPO que descubren el dolor"),
55: ("C", "el DFSS y su DMADV con CTQs contra la innovacion tipo II de mas grande, mas pequeno o combinado"),
56: ("C", "el ciclo disenar, probar, repetir contra el prototipado de POSIBILIDADES con multiples direcciones alternativas"),
57: ("C", "el dia de cero defectos y sus tres pasos de lanzamiento contra el entrenamiento del supervisor cuatro semanas antes"),
58: ("C", "la regla de que el diagnostico precede al remedio contra la terminologia que hay que fijar con el equipo antes de diagnosticar"),
59: ("C", "DISCUTIBLE 4. El paso 2 del puzzle repite casi la pregunta del dilema. Se sostiene C porque el puzzle expande UN ARGUMENTO EMPIRICO (la prima de capital privado no existe) y el dilema expande UN PROCEDIMIENTO DE DECISION en cada ronda"),
60: ("C", "el diseno etico de privacidad con opt out real contra la responsabilidad etica general del design thinking y sus efectos secundarios"),
61: ("C", "los documentos de exportacion (pro forma, comercial, packing list, HS, SED) contra el seguro de carga y de credito y su cobertura CIF"),
62: ("C", "los documentos de exportacion contra la seleccion del metodo de transporte (aereo, maritimo, multimodal, booking)"),
63: ("C", "la ecuacion de valor del cliente y su balanza contra la secuencia completa de preguntas del modelo SPIN"),
64: ("C", "la educacion masiva en metodos estadisticos contra tu propia responsabilidad gerencial de aprender y liderar la mejora"),
65: ("C", "verificar los hechos con el responsable antes de escribir el reporte contra las relaciones humanas del proceso de auditoria"),
66: ("C", "el fundador como punto unico de falla y su documentacion de accesos contra la continuidad del negocio y sus funciones que no pueden parar"),
67: ("C", "los trece elementos practicos de un plan de exportacion contra los programas concretos de financiamiento del Ex-Im Bank"),
68: ("C", "eliminar metas numericas sin metodo contra el procedimiento de verificar si el sistema es estable antes de intervenir"),
69: ("C", "la reserva de acciones para empleados y su dilucion contra el vesting del fundador con su cliff, su 83(b) y su aceleracion"),
70: ("C", "encuadrar el desafio de diseno con la pregunta como podriamos contra el triple criterio deseabilidad, viabilidad y factibilidad en emprendimiento social"),
71: ("C", "encuadrar el desafio de diseno contra la investigacion de campo con usuarios extremos en contextos de pobreza"),
72: ("C", "los enfoques generales de involucramiento en la exportacion contra los programas de financiamiento del Ex-Im Bank"),
73: ("C", "el entrenamiento del supervisor en el programa ZD contra la identificacion del empleado con su trabajo y su seguimiento de ausentismo"),
74: ("C", "clasificar el estilo de la contraparte y adaptarse contra la teoria de juegos y su distincion entre una ronda y multi ronda"),
75: ("C", "la captura rapida cuando un mercado crece contra los cuatro tipos de mercado y sus curvas de crecimiento de ingresos"),
76: ("C", "la estrategia de crecimiento (venta cruzada, referidos, motores de recomendacion) contra el embudo de adquisicion y activacion web y movil"),
77: ("C", "la estrategia de plataformas existentes y su feature complementaria contra el programa de afiliados y su estructura de comision"),
78: ("C", "la estratificacion de datos por variables contra la planificacion de trece pasos de recoleccion y analisis"),
79: ("C", "DECISION DE FRANQUICIAR, y este par tambien SOLO existe tras resolver alias. Evaluar la necesidad de franquiciar contra la mezcla de ubicaciones corporativas y franquiciadas y sus estrategias Home Sweet Home o Cherry Picking"),
80: ("C", "fallas activas y condiciones latentes contra la vulnerabilidad especifica de la instalacion frente al desensamblaje y su checklist de reensamblaje"),
81: ("C", "la fase Accomplish y sus tres escenarios de mision contra la reunion de conclusion con encuestas internas y externas"),
82: ("C", "la planificacion de escenarios contra el IOTA que reune los hallazgos previos en una tabla y responde entonces que"),
83: ("C", "el DIAGNOSTICO de compuertas sin dientes (la curva de supervivencia, las 7 razones para no matar) contra el sistema de gates de 17 pasos que las instala"),
84: ("C", "salir del edificio a observar contra identificar y ordenar los supuestos de salto de fe: uno es el acto, el otro la lista que lo dirige"),
85: ("C", "la politica contra alucinaciones de la IA contra el uso de la IA como motor de recombinacion de ideas"),
86: ("C", "la gestion de instalaciones y su capacidad optima contra el proceso de sourcing y su costo total de propiedad"),
87: ("C", "el enfoque jerarquico de portafolio (gate individual mas revision trimestral del conjunto) contra el sistema de gates. LA FICHA DE OP-E-04 YA DECLARA ESTE PAR COMO MUTUO EXCEPTUADO del 9.22 en su verificacion 5, y esa declaracion sellada respalda la lectura"),
88: ("C", "la gestion del foco de recursos y su auditoria de proyectos activos contra el sistema de gates. TAMBIEN EXCEPTUADO por la verificacion 5 de OP-E-04"),
89: ("C", "el pensamiento visual y su post it siempre a mano contra las ocho reglas del brainstorming efectivo"),
90: ("C", "la IA aplicada a la cadena de suministro contra el modelado de simulacion y sus escenarios"),
91: ("C", "los Incoterms y su punto de transferencia de riesgo contra la seleccion del metodo de pago y la solvencia del comprador"),
92: ("C", "el juego Speed Boat que saca los dolores contra el Product Box que saca los mensajes de marketing: dos juegos distintos con dos salidas distintas"),
93: ("C", "el servicio International Partner Search del Commercial Service contra el checklist de nueve puntos para evaluar al representante"),
94: ("C", "la investigacion etnografica de campo contra las reglas de la sesion de brainstorming que consume sus hallazgos"),
95: ("C", "la investigacion de accidentes bajo el enfoque New View contra los metodos de process tracing y sus dos relatos paralelos"),
96: ("C", "los joint ventures internacionales contra la proteccion de propiedad intelectual con PCT y Madrid Protocol"),
97: ("C", "el metodo RCCA de Juran en cuatro fases contra el viaje diagnostico y remedial en ocho pasos con su gestion de la resistencia"),
98: ("C", "el proceso Lean LaunchPad para un startup web contra el lienzo mismo y sus doce pasos"),
99: ("C", "el lienzo contra el patron FREE y sus tres variantes publicidad, freemium y bait and hook"),
100: ("C", "el lienzo contra el proceso de ideacion de modelos con su equipo diverso y su fase de inmersion"),
101: ("C", "el lienzo contra la busqueda de modelo de negocio y su distincion entre modo busqueda y modo ejecucion"),
102: ("C", "el lienzo contra la escala del problema del segmento (latente, pasivo, activo, con solucion casera)"),
103: ("C", "PAR QUE SOLO EXISTE TRAS RESOLVER ALIAS. El mapeo de flujo de valor y su estado futuro contra el takt time y el balanceo de estaciones"),
104: ("C", "PAR QUE SOLO EXISTE TRAS RESOLVER ALIAS. Los tipos de mercado y sus curvas contra las metricas que importan y el burn rate"),
105: ("C", "el NPV y su ecuacion de descuento contra la tasa de retorno requerida y el costo de capital que la fija"),
106: ("C", "el motor viral y su coeficiente contra la eleccion entre los cuatro motores de crecimiento"),
107: ("C", "el acuerdo de exclusividad y su plazo contra la negociacion completa del term sheet"),
108: ("C", "el plan de lanzamiento al mercado contra la reduccion del tiempo al mercado y su procesamiento paralelo"),
109: ("C", "el plan de comunicaciones (que, como, cuando, quien) contra el plan de gestion de interesados (nivel de compromiso actual y deseado)"),
110: ("C", "la gestion de portafolio holistica contra el sistema de gates individual. TAMBIEN EXCEPTUADO por la verificacion 5 de OP-E-04"),
111: ("C", "los ocho principios ISO 9000 contra el sistema de gestion de calidad que los toma como criterios rectores"),
112: ("C", "el problem solution fit contra el MVP y su hipotesis mas critica"),
113: ("C", "el plan de gestion del proyecto que consolida los subsidiarios contra el plan de gestion del alcance y su WBS"),
114: ("C", "el prototipado rapido con carton y cinta contra prototipar con un medio RADICALMENTE distinto al habitual para que emerjan propiedades nuevas"),
115: ("C", "las recomendaciones SMART de una investigacion de seguridad contra la revision de aprendizaje que cambia la pregunta y el nombre del equipo"),
116: ("C", "las cinco reglas de gestion de riesgo por etapas contra el sistema de gates que las materializa en puntos de decision"),
117: ("C", "los miedos que frenan al lanzar un MVP (legales, copia, marca, animo) contra la prueba Mago de Oz y su backend humano"),
118: ("C", "la busqueda de modelo de negocio contra la distincion entre vision inalterable, estrategia y producto"),
119: ("C", "el modelado de simulacion contra los drones y vehiculos autonomos y su marco regulatorio"),
120: ("C", "el principio de inclusividad de la tesis Boulder contra la activacion de toda la red con actividades practicas"),
121: ("C", "la deuda de riesgo como complemento al equity contra sus condiciones de precio concretas (tasa, comisiones, warrants)"),
}

DISCUTIBLES = [8, 31, 42, 59]

TRAMOS = [(1, 41), (41, 81), (81, 122)]


def pares():
    out = []
    for linea in io.open(LISTA, encoding="utf-8"):
        if not linea.strip():
            continue
        n, a, b = linea.strip().split("|")
        out.append((int(n), a, b))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", type=int, default=0)
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--escribir", action="store_true")
    args = ap.parse_args()

    P = pares()
    assert len(P) == 121, "la lista no trae 121 pares: %d" % len(P)
    faltan = [n for n, _a, _b in P if n not in M]
    assert not faltan, "PARES SIN LECTURA ESCRITA: %s" % faltan
    sobran = [n for n in M if n not in {x[0] for x in P}]
    assert not sobran, "lecturas que no corresponden a ningun par: %s" % sobran
    print("PARES: %d | LECTURAS ESCRITAS: %d | sin lectura: 0 | huerfanas: 0" % (len(P), len(M)))
    clases = {}
    for n, _a, _b in P:
        clases[M[n][0]] = clases.get(M[n][0], 0) + 1
    print("CLASES ADJUDICADAS: %s" % clases)
    print("DISCUTIBLES MARCADOS (antes de saber si acierto): %s" % DISCUTIBLES)
    print("")

    bloques = []
    for i, (desde, hasta) in enumerate(TRAMOS, 1):
        if args.tramo and args.tramo != i:
            continue
        filas = [(n, a, b) for n, a, b in P if desde <= n < hasta]
        cab = ("\n---\n\n## LECTURAS DIRIGIDAS `LD-OPC05`, TRAMO %d de 3: pares %d a %d\n\n"
               "**Encargo: vuelta 152, TAREA 6.b. Vara: banco 9.22, LOS DOS POLOS, aplicada EN LOS\n"
               "DOS SENTIDOS. Fuente de lectura: `docs/loop/SALIDA_V152_T6B_DOSSIER.txt`, que imprime\n"
               "el titulo y los pasos accionables de los dos nodos de cada par. `n` NO SE MUEVE: el\n"
               "archivo del cribado sigue en 3.388 lineas y no se toca.**\n\n"
               "| n | REGISTRO DE CITAS `OP-C-05` | par | clase | LD | que expande cada direccion |\n"
               "|---:|---|---|---|---|---|\n" % (i, filas[0][0], filas[-1][0]))
        cuerpo = []
        for n, a, b in filas:
            clase, motivo = M[n]
            cuerpo.append("| %d | REGISTRO DE CITAS `OP-C-05` | %s <-> %s | %s | LD-OPC05-%03d | %s |"
                          % (n, a, b, clase, n, motivo))
        bloques.append(cab + "\n".join(cuerpo) + "\n")
        print("TRAMO %d: %d lectura(s), de la %d a la %d" % (i, len(filas), filas[0][0], filas[-1][0]))

    if args.escribir:
        cierre = ("\n**LOS CUATRO DISCUTIBLES DE ESTA TANDA, MARCADOS ANTES DE SABER SI ACIERTO** "
                  "(`EJECUTOR.md` 7): **%s**. Son los unicos pares donde el solape de LINEA es real y "
                  "la clase `C` se sostiene por poco; en los otros 117 los dos nodos son procedimientos "
                  "completos y distintos y la figura no admite discusion. Quien discrepe tiene que ir a "
                  "esos cuatro, no a los 121.\n"
                  % ", ".join("LD-OPC05-%03d" % n for n in DISCUTIBLES))
        viejo = io.open(LD, encoding="utf-8").read()
        io.open(LD, "w", encoding="utf-8", newline="\n").write(viejo + "".join(bloques) + cierre)
        nuevo = io.open(LD, encoding="utf-8").read()
        assert nuevo.startswith(viejo), "ADICION IMPURA en LECTURAS_DIRIGIDAS.md"
        print("")
        print("ESCRITO por ADICION PURA en docs/plan/LECTURAS_DIRIGIDAS.md: %d -> %d caracteres"
              % (len(viejo), len(nuevo)))


main()
