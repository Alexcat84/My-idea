# -*- coding: utf-8 -*-
r"""vuelta96_tarea3_veredictos_tramo1.py . VUELTA 96, TAREA 3: LOS VEREDICTOS
del primer tramo de OP-E-03, cuarenta pares leidos, con su clase del banco 9.6.1
y su direccion del 9.6.2.

DE DONDE SALEN LOS VEREDICTOS, Y SE DICE SIN ADORNO: los pone LA LECTURA del
ejecutor sobre el material impreso entero por
scripts/loop/vuelta96_tarea3_tramo1_opE03.py
(docs/loop/SALIDA_V96_TAREA3_TRAMO1_MATERIAL.txt, 1.368 lineas). Son una TABLA A
MANO. Por EJECUTOR.md regla 1 ("EL CASO ROJO SE PRUEBA POR MUTACION ... Si la
clasificacion es una tabla a mano y no hay nada que mutar, SE DECLARA QUE NO HAY
CASO ROJO AUTOMATICO"): AQUI SE DECLARA. NO HAY CASO ROJO AUTOMATICO PARA LA
CLASE DE CADA PAR. Lo que si tiene guardas mecanicas, y estan probadas por
mutacion, es el ARMAZON: que los 40 veredictos correspondan uno a uno con las 40
filas reales del tramo, que ninguna clase este fuera de {A,B,C,D}, que ningun
par se repita, y que las cuentas publicadas salgan de contar la tabla y no de
teclearlas.

LA VARA APLICADA, citada y no inventada:
  banco 9.6.1 (docs/BANCO_DE_TEXTOS.md linea 1612), rama contenido manda:
    "Si lo que el hijo anade a lo que la madre ya dice CABE EN UNA LINEA,
    REPITE. Si trae un PROCEDIMIENTO que la madre no tiene, CONTINUA."
  banco 9.6.2 (linea 1737), la direccion:
    "El hijo cabe entero dentro de UN paso de la madre, y la madre conserva
    materia propia que el hijo no toca en ningun paso."
  banco 9.6.3 (linea 1796): el TAMANO del solape no decide; decide que queda
    FUERA.
  CLASES, medidas hoy sobre docs/INTRA_DOMINIO_VEREDICTOS.jsonl y no
    recordadas: A REPITE (551), B DUDOSO (72), C figura aparte (5),
    D CONTINUA (2.760), n 3.388.

LOS CINCO PUNTOS DE OP-E-03.verificacion, y donde se cumple cada uno:
  1 y 2 y 3 (cierre de la cola, resolutor antes de comparar, cuenta sin fugas):
    en el instrumento del material, que es quien los mide; este lee su misma
    bolsa y vuelve a cruzarla.
  4 (LECTURA DIRIGIDA, no entra en la cola y NO mueve el marcador del cribado):
    escrito en cada fila de la salida y del JSONL, y este instrumento NO TOCA
    ningun fichero del cribado ni del grafo.
  5 (los veredictos se cuentan APARTE de la tasa por dominio): la tabla por
    dominio se imprime rotulada como tal y NO se suma a la tasa del banco 9.27.

SALIDA: docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl (40 filas) y la tabla por
pantalla. Es el UNICO fichero que escribe.

USO:
  python scripts/loop/vuelta96_tarea3_veredictos_tramo1.py
  python scripts/loop/vuelta96_tarea3_veredictos_tramo1.py --sin-escribir
"""
import argparse
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta96_tarea3_tramo1_opE03 import reunir  # noqa: E402

SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")

CLASES_VALIDAS = {"A", "B", "C", "D"}

# LA TABLA A MANO. (n, clase, direccion, razon).
# direccion: "madre -> hijo" con los ids, o None cuando la lectura NO la resuelve.
# Ninguna razon repite formula de otra sin haberla leido: cada una cita el paso.
VEREDICTOS = [
    (1, "D", "segmentos_de_clientes_problema_necesidad -> get_out_of_the_building",
     "Su paso 1, 'Sal del edificio a observar como tus clientes viven el problema', es UNA LINEA, y get_out_of_the_building trae el procedimiento entero de esa linea: programar reuniones repetidas, liderarlas uno mismo, no hacer lista de features pedidas, y documentar cada conversacion en el momento. La madre conserva la escala del problema, el must-have contra nice-to-have, los tipos de cliente y el mercado de varios lados, que el hijo no toca."),
    (2, "D", "medicion_servicios -> make_certain_programa",
     "Su paso 3, 'Implementar el programa Make Certain para servicio y areas administrativas', es UNA LINEA, y make_certain_programa trae los siete pasos de ejecutarlo: informar a los directivos, designar coordinadores, recolectar ejemplos reales, la sesion del mayor problema, evidenciar la atribucion a terceros, pedir ideas escritas y establecer reuniones regulares de prevencion."),
    (3, "D", "medicion_servicios -> programa_make_certain_3",
     "Mismo paso 3 de la misma madre, y programa_make_certain_3 trae OTRO procedimiento de esa linea: identificar procesos administrativos criticos, capacitar con la guia del instructor, implementar los pasos de prevencion de errores de oficina y monitorear la exactitud de datos en la cadena de comunicacion. FIGURA: es el segundo de TRES hijos del mismo paso, ver la nota de figuras."),
    (4, "D", "consejo_de_calidad_y_rol_del_director -> planificacion_estrategica_despliegue_2",
     "Su paso 3, 'Integra las metas de calidad en tus planes de negocio y de desempeno', es UNA LINEA, y planificacion_estrategica_despliegue_2 trae los siete pasos de esa integracion, incluidos poner la voz del cliente al nivel de las metas financieras, usar el mismo lenguaje para los terminos clave y eliminar las iniciativas no alineadas."),
    (5, "D", "planificacion_cero_defectos -> eliminacion_causas_error_4",
     "Su paso 6, 'Planificar el programa de eliminacion de causas de error como continuacion', es UNA LINEA que nombra un programa, y eliminacion_causas_error_4 trae el sistema entero: canal con formulario sin exigir solucion, agradecimiento inmediato, clasificar y priorizar, actuar rapido, justificar el no actuar ante alguien de mas experiencia, y confirmar la decision a quien aviso."),
    (6, "D", "issue_spotting_ambiental -> triple_bottom_line_2",
     "Su paso 2, 'Decide si tu enfoque sera solo ambiental o si vas a incluir tambien lo social y economico', es UNA LINEA de decision, y triple_bottom_line_2 trae el procedimiento del lado social: identificar los asuntos sociales, evaluar practicas laborales, de diversidad y de derechos humanos en la cadena de valor, e integrar metricas sociales junto a las ambientales."),
    (7, "D", "customer_development_team -> get_out_of_the_building",
     "Su paso 2, 'Define como vas a salir a hablar con clientes en persona', es UNA LINEA, y get_out_of_the_building trae el procedimiento. Es el mismo hijo del par 1 con OTRA madre: hijo con casa propia y dos madres, no duplicado."),
    (8, "D", "analisis_de_sistemas_de_medicion_msa -> capacidad_de_proceso_2",
     "Su paso 3, 'Verificar que el proceso de medicion este bajo control estadistico mediante carta de control', es UNA LINEA, y capacidad_de_proceso_2 trae el procedimiento de la carta: elegir la unidad, recolectar unos tres meses de datos, construir las cartas, decidir si esta dentro de limites e intervenir SOBRE EL SISTEMA y no sobre el individuo, que es materia propia del hijo y queda fuera de la madre."),
    (9, "D", "dmadv_fase_verificacion -> capacidad_de_proceso",
     "Su paso 2, 'Haz un analisis de capacidad y revisa tus sistemas de medicion', es UNA LINEA, y capacidad_de_proceso trae el procedimiento: recolectar historico, calcular los indices contra especificaciones, decidir frecuencia de medicion y mantenimiento, y determinar si el proceso necesita rediseno."),
    (10, "D", "validacion_sistema_medicion -> analisis_de_sistemas_de_medicion_msa",
     "Su paso 1, 'Evalua la capacidad de tu sistema de medicion usando el analisis MSA', es UNA LINEA que nombra el metodo, y el MSA trae sus seis pasos. Nota de forma: el MSA es HIJO aqui y MADRE en el par 8, o sea cadena de tres y no dos madres del mismo nivel."),
    (11, "D", None,
     "CONTINUA sin discusion, pero la DIRECCION NO SE RESUELVE y no se fuerza. El paso 3 de introduccion_validacion_clientes dice 'Probar canales de ventas y distribucion', y herramientas_online_canal_fisico no PRUEBA canales: MONTA presencia en linea de apoyo al canal fisico (sitio web, redes, campanas de email, equilibrio entre push y pull). Construir no es probar, asi que el hijo no cabe dentro de ese paso y el par no ensena quien es la madre."),
    (12, "A", None,
     "REPITE, y es el unico A del tramo. MISMA FUENTE (Dekker). El paso 1 de human_error_como_sintoma ya manda preguntar que condiciones contribuyeron en lugar de quien fallo, y su paso 2 ya manda redisenar el sistema en vez de entrenar o sancionar. preguntar_que_no_quien dice esas dos mismas cosas con otras palabras en sus pasos 1, 2 y 4. Lo UNICO que anade es su paso 3, 'anota las condiciones de trabajo que rodeaban el momento', y eso CABE EN UNA LINEA. Vara del 9.6.1, rama contenido manda: REPITE."),
    (13, "D", "waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development",
     "Su paso 3, 'Alinear el proceso de desarrollo de producto con el proceso de Customer Development', es UNA LINEA que nombra el otro proceso, y desarrollo_de_clientes_customer_development lo trae entero: convertir hipotesis en preguntas, entrevistar antes de construir, iterar con el feedback, y combinar el aprendizaje con ingenieria agil."),
    (14, "D", "medicion_servicios -> programa_make_certain",
     "Mismo paso 3 de medicion_servicios, TERCER hijo distinto de esa misma linea, con procedimiento propio: identificar tasas de repeticion de trabajo, disenar el programa de cinco semanas, lanzarlo en la etapa de concientizacion y medir el costo de calidad antes y despues. Ver la nota de figuras."),
    (15, "D", None,
     "CONTINUA y la DIRECCION ES NINGUNA: no son madre e hijo, son los DOS LADOS DEL BALANCE. clasificacion_tipos_activos clasifica ACTIVOS en corrientes y de largo plazo; tipos_de_pasivos clasifica DEUDAS con el mismo corte. El barrido caso la forma de la frase, no la materia. Es el caso 2.195 que el banco 9.6.2 ya nombra: linea compartida y procedimiento propio a cada lado."),
    (16, "D", "proceso_venta_franquicias -> proceso_llamada_inicial_venta",
     "CONTINUA, y la DIRECCION SALE INVERTIDA respecto a la etiqueta del barrido, que es justo el error que el banco 9.6.2 nace para evitar. El paso 1 de proceso_venta_franquicias, 'Disenar un flujo de proceso de ventas adaptado al tipo de franquicia', es UNA LINEA, y proceso_llamada_inicial_venta trae los NUEVE pasos de la primera llamada, que caben enteros dentro de ese flujo. La madre conserva la capacitacion en motivaciones, la estrategia de Discovery Day, el FDD con abogado y la medicion del proceso."),
    (17, "D", "customer_discovery_overview -> mvp_catalogo_tecnicas",
     "Su paso 3, 'Muestrales tu producto minimo viable y tu propuesta de valor para validar la solucion', es UNA LINEA, y mvp_catalogo_tecnicas trae el procedimiento de conseguir ese MVP: identificar la hipotesis a validar, empezar por el mas barato, escalar la sofisticacion solo si lo inicial promete, y usar herramientas accesibles antes de produccion profesional."),
    (18, "D", "dmaic_fase_measure -> capacidad_del_proceso",
     "Su paso 5, 'Determinar si el proceso esta en control estadistico y medir su capacidad a corto plazo', es UNA LINEA, y capacidad_del_proceso trae el procedimiento: verificar el control primero, calcular media y rango del proceso estable, aplicar las formulas con sus constantes, y comunicar la capacidad real a diseno e ingenieria."),
    (19, "D", "diseno_de_flujos_pace_layers -> framework_ppph_flujos",
     "Ejemplar limpio del 9.6.2. Su paso 3, 'Para cualquier flujo relevante analiza su Proposito, Partes, Lugar y Pace', es UNA LINEA que enuncia cuatro nombres, y framework_ppph_flujos dedica UN paso a cada uno mas el de identificar el flujo. La madre conserva las capas de ritmo y los puntos de desaceleracion intencional, que el hijo no toca."),
    (20, "D", "waterfall_vs_agile_development -> modelo_customer_development",
     "Mismo paso 3 que el par 13, SEGUNDO hijo de esa misma linea, con procedimiento propio: identificar en que paso esta la startup, formular hipotesis antes de cada paso, disenar experimentos fuera del edificio, evaluar en cada senal de alto si hay velocidad de escape, y estar dispuesto a retroceder. Ver la nota de figuras."),
    (21, "D", "build_measure_learn -> value_proposition_canvas",
     "Su paso 1, 'Paso 0: Generar una hipotesis clara a partir de los Canvas de Value Proposition y Business Model', es UNA LINEA que nombra el artefacto, y value_proposition_canvas trae el procedimiento de construirlo: descargar la plantilla, dibujar el perfil del cliente, dibujar el mapa de valor, iterar los dos lados hasta el encaje, comunicarlo y usarlo como marcador en las conversaciones."),
    (22, "D", None,
     "CONTINUA, pero la DIRECCION NO SE RESUELVE. El paso 1 de extraer_priorizar_hipotesis manda LISTAR todo lo que tiene que ser cierto sobre el modelo, la propuesta de valor y el cliente; value_proposition_startup no lista hipotesis: CONSTRUYE la propuesta de valor y verifica su encaje. La linea NOMBRA la propuesta de valor de pasada, y nombrar no es mandar ejecutar."),
    (23, "B", None,
     "DUDOSO, y se declara en vez de forzarlo a A o a D. El paso 3 del hijo, 'Verifica el encaje entre tu propuesta de valor y tu segmento hablando directamente con ellos', ES el paso 2 de fit_problema_solucion, 'Testear si los clientes quieren tu propuesta de valor concreta'. Lo que value_proposition_startup anade son sus pasos 1 y 2, identificar los problemas reales y definir que caracteristicas los resuelven: es mas que una linea y menos que un procedimiento con logica propia, y ademas son de fuentes distintas (Value Proposition Design contra Blank). La vara del 9.6.1 no lo resuelve sola."),
    (24, "D", "preparacion_preguntas_problema_precall -> preguntas_situacion",
     "Su paso 4, 'Usar estas preguntas para minimizar preguntas de situacion irrelevantes', es UNA LINEA, y preguntas_situacion trae el procedimiento de esa minimizacion: investigar al cliente antes para reducir preguntas innecesarias, limitarlas a lo estrictamente necesario, y usarlas como apertura breve antes de pasar al problema."),
    (25, "D", "histograma_calidad -> capacidad_del_proceso",
     "Su paso 4, 'Evaluar el centrado, ancho y forma del histograma para determinar capacidad del proceso', es UNA LINEA, y capacidad_del_proceso trae el procedimiento de determinarla. Mismo hijo que el par 18 con otra madre; las dos madres lo nombran en una linea y ninguna lo desarrolla."),
    (26, "D", None,
     "CONTINUA, pero la DIRECCION ES NINGUNA: cada lado trae procedimiento propio sobre una linea compartida, el caso 2.195 del banco 9.6.2 otra vez. rol_gates_agile anade revisar tambien los recursos en cada punto, no separar los puntos de hardware y software, y sostener un cronograma de hitos estable; gates_go_kill_decision_points anade anotar QUE se decidio entre cinco salidas posibles. Ninguno de los dos cabe entero dentro de un paso del otro. DISCUTIBLE: esta cerca de A y no lo es porque lo que anade rol_gates_agile son tres instrucciones operativas, no una linea."),
    (27, "D", "estrategia_innovacion_producto -> strat_map_arenas_estrategicas",
     "Su paso 3, 'Identificar y priorizar las arenas estrategicas en las que se enfocara el esfuerzo de I+D', es UNA LINEA, y strat_map_arenas_estrategicas trae los seis pasos de hacerlo: definir la base actual, identificar arenas potenciales, definir de 6 a 8 criterios por eje, recolectar datos y calificar de 0 a 10, graficar las burbujas y elegir el cuadrante superior derecho."),
    (28, "D", "timing_solicitud_referidos -> fase_adopt_ciclo_cliente",
     "Su paso 5, 'Comunica el programa en momentos clave del ciclo de vida, por ejemplo la fase Adopt', es UNA LINEA que NOMBRA la fase, y fase_adopt_ciclo_cliente trae el procedimiento de esa fase: definir que comportamientos indican adopcion, disenar interacciones para los seis canales, implementar la encuesta de exito y establecer el ritual de hitos. Es la formula del 9.6.2: un procedimiento nombrado en una linea."),
    (29, "D", "abolir_inspeccion_masiva -> control_estadistico_del_proceso",
     "Su paso 5, 'Reduce gradualmente la inspeccion masiva a medida que tu proceso demuestre estar en control estadistico', es UNA LINEA que nombra el control estadistico, y control_estadistico_del_proceso trae sus siete pasos. La madre conserva medir el costo de la inspeccion al 100%, el muestreo aleatorio y la reserva de la inspeccion total para casos criticos."),
    (30, "D", "tres_preguntas_carrera -> evaluacion_ventana_mercado",
     "Su paso 3, 'Evalua el factor de mercado: preguntate si la oportunidad y el momento son favorables', es UNA LINEA, y evaluacion_ventana_mercado trae el procedimiento: estimar tamano y crecimiento, analizar la competencia y el punto de la curva en S, determinar si hay reloj corriendo que favorezca ser primero, y ajustar el calendario segun sea disruptivo o sostenido. La madre conserva los factores de carrera y personal."),
    (31, "D", "control_estadistico_del_proceso -> causas_comunes_vs_especiales",
     "Su paso 3, 'Identificar y eliminar causas especiales de variacion hasta que el proceso muestre estabilidad', es UNA LINEA, y causas_comunes_vs_especiales trae QUINCE pasos para esa distincion. Nota de forma: el SPC es HIJO en el par 29 y MADRE aqui, o sea cadena de tres."),
    (32, "D", None,
     "CONTINUA y la DIRECCION ES NINGUNA, y el motivo merece registro aparte: el hijo no desarrolla el paso de la madre, LO REFUTA. requisitos_numericos_calidad_lotes manda definir indices AQL (Juran); critica_acceptable_quality_level manda revisar si usas AQL, cuestionar su origen y cambiar la mentalidad por Cero Defectos (Crosby). Dos doctrinas opuestas sobre la misma linea. Ver la nota de figuras."),
    (33, "D", "diamante_de_innovacion -> estrategia_de_innovacion_de_producto",
     "Su paso 1, 'Definir una estrategia de innovacion clara: donde enfocar los esfuerzos y recursos', es UNA LINEA, y estrategia_de_innovacion_de_producto trae los seis pasos: objetivos con porcentaje de ventas a 3 a 5 anos, vinculo con las metas del negocio, arenas estrategicas, cubos de recursos, hoja de ruta de producto y compromiso de largo plazo. La madre conserva los otros tres pilares del diamante."),
    (34, "D", None,
     "CONTINUA, pero la DIRECCION NO SE RESUELVE. El paso 4 de hipotesis_relacion_clientes_web habla del MVP de BAJA fidelidad, y mvp_alta_fidelidad es el de ALTA, que empieza justo donde acaba el otro ('Partir del MVP de baja fidelidad'). Son sucesivos, no uno dentro del otro."),
    (35, "D", None,
     "CONTINUA, pero la DIRECCION NO SE RESUELVE y se dice en vez de forzarla. El paso 1 de producto_mercado_fit_motores manda DEFINIR LA METRICA del motor elegido; afinar_motor_crecimiento no define la metrica: corre el ciclo de experimentos para MEJORARLA. Comparten el motor y se reparten el trabajo, pero el hijo no cabe dentro de ese paso."),
    (36, "D", None,
     "CONTINUA, pero la DIRECCION NO SE RESUELVE. El paso 5 de relaciones_publicas_leads_franquicia manda extender el beneficio de RELACIONES PUBLICAS a los franquiciados existentes; referidos_franquiciados_existentes monta un programa de REFERIDOS con esos mismos franquiciados. Coinciden las personas, no la actividad."),
    (37, "D", None,
     "CONTINUA, pero la DIRECCION NO SE RESUELVE. El paso 1 de valor_intangible_sostenibilidad manda incorporar metricas de sostenibilidad al seguimiento del negocio; compromiso_cliente_sostenibilidad monta campanas en plataformas sociales que vinculan la interaccion del cliente con acciones ambientales. El hijo mide y comunica, como la madre, pero por un canal que la madre no nombra en ningun paso."),
    (38, "D", "obtencion_compromiso -> enfoque_etapa_investigacion",
     "Su paso 4, 'Pon tu esfuerzo de mejora en las etapas de investigacion y demostracion de capacidad, no en el cierre', es UNA LINEA, y enfoque_etapa_investigacion trae el procedimiento de ese esfuerzo: dedicar mas tiempo a disenar preguntas que discurso, no mostrar beneficios antes de desarrollar el problema, auditar las llamadas pasadas, entrenar primero Situacion y Problema, y practicar escuchar lo no dicho."),
    (39, "D", "modelos_gestion_seguridad -> fallas_activas_condiciones_latentes",
     "Su paso 4, 'Incorporar analisis de condiciones latentes y defensas del sistema propio del modelo organizacional', es UNA LINEA que nombra el analisis, y fallas_activas_condiciones_latentes lo trae entero: identificar los actos inseguros, buscar las decisiones previas que crearon las condiciones, tabular unas contra otras, rastrear el origen gerencial de cada una, priorizar por impacto futuro y mantener el registro vivo."),
    (40, "D", "analisis_valor -> customer_needs_spreadsheet",
     "Su paso 1, 'Elaborar una hoja de calculo que relacione costos con necesidades del cliente por prioridad', es UNA LINEA que nombra el artefacto, y customer_needs_spreadsheet trae los seis pasos de construirlo. SALVEDAD DECLARADA: la matriz del hijo cruza clientes contra necesidades y la de la madre cruza costos contra necesidades, asi que el artefacto no es identico; la direccion se sostiene porque la madre lo pide en una linea y el hijo es el unico de los dos que ensena a construirlo."),
]

# FIGURAS observadas en el tramo. No son veredictos de par: son observaciones
# de FORMA que la lectura destapa y que el expediente pide registrar.
FIGURAS = [
    ("TRES HIJOS DE UNA MISMA LINEA, y los tres del mismo libro (Crosby)",
     "El paso 3 de medicion_servicios ('Implementar el programa Make Certain') tiene TRES hijos "
     "distintos en esta bolsa: make_certain_programa (par 2, 7 pasos), programa_make_certain_3 "
     "(par 3, 4 pasos) y programa_make_certain (par 14, 4 pasos). Los tres pares son D por "
     "separado, porque cada hijo trae procedimiento. LO QUE LA FIGURA SENALA NO ES EL PAR, ES EL "
     "TRIO: tres casas para el mismo programa de la misma fuente. Sospecha de gemelos ENTRE ELLOS, "
     "que es otra pregunta y otra operacion."),
    ("DOS HIJOS DE UNA MISMA LINEA, del mismo libro (Blank)",
     "El paso 3 de waterfall_vs_agile_development ('Alinear el proceso de desarrollo de producto "
     "con el proceso de Customer Development') tiene DOS hijos: "
     "desarrollo_de_clientes_customer_development (par 13) y modelo_customer_development (par 20). "
     "Los dos pares son D. Sospecha de gemelos entre esos dos hijos."),
    ("DOS NODOS DE TITULO CASI IDENTICO, uno madre y otro hijo en pares distintos",
     "estrategia_innovacion_producto es MADRE en el par 27 y estrategia_de_innovacion_de_producto "
     "es HIJO en el par 33. Mismo libro (Cooper), titulos casi iguales, y los dos hablan de "
     "objetivos, arenas y recursos. Sospecha de gemelos, y esta vez entre un nodo que hace de "
     "madre y otro que hace de hijo, que es la forma que mas cuesta ver."),
    ("LA FAMILIA DE LA CAPACIDAD DE PROCESO, tres nodos y el Gate 0 ya avisaba",
     "capacidad_de_proceso (par 9), capacidad_del_proceso (pares 18 y 25) y capacidad_de_proceso_2 "
     "(par 8) son tres nodos distintos sobre capacidad de proceso, de dos fuentes (Juran y Deming). "
     "El aviso informativo de Gate 0 de esta misma vuelta ya lista "
     "'capacidad_de_proceso <-> capacidad_del_proceso' con 97,6 de similitud de titulo. La lectura "
     "de estos pares CORROBORA ese aviso desde otro camino."),
    ("EL BARRIDO PUEDE CASAR UN PASO CON SU PROPIA REFUTACION",
     "En el par 32 el nodo casado con el paso 'Definir indices numericos de calidad de lote (AQL)' "
     "de Juran es critica_acceptable_quality_level de Crosby, que manda ELIMINAR el AQL. El barrido "
     "casa por vocabulario y no distingue desarrollar de refutar. NO es un defecto del barrido: es "
     "una propiedad suya que conviene tener escrita antes de leer los 143 pares que quedan."),
    ("UN PAR CON LA DIRECCION INVERTIDA respecto a la etiqueta del barrido",
     "En el par 16 la bolsa etiqueta madre=proceso_llamada_inicial_venta e hijo="
     "proceso_venta_franquicias, y la lectura da lo contrario: el flujo de ventas es la madre y el "
     "guion de la primera llamada cabe entero dentro de su paso 1. Es UNO de 40, pero es "
     "exactamente el error que el banco 9.6.2 nace para evitar, asi que se cuenta y se nombra."),
]


def construir_filas(veredictos=VEREDICTOS, desde=0, cuantos=40):
    filas_material, fallos, _, total_bolsa, _ = reunir(desde, cuantos)
    por_n = {f["n"]: f for f in filas_material}

    if len(veredictos) != len(filas_material):
        fallos.append("hay %d veredictos y %d filas de material: no es uno a uno"
                      % (len(veredictos), len(filas_material)))

    vistos = set()
    filas = []
    for n, clase, direccion, razon in veredictos:
        if clase not in CLASES_VALIDAS:
            fallos.append("el par %s trae la clase %r, que no es A, B, C ni D" % (n, clase))
        if n in vistos:
            fallos.append("el par %s aparece dos veces en la tabla de veredictos" % n)
        vistos.add(n)
        m = por_n.get(n)
        if m is None:
            fallos.append("el veredicto %s no corresponde a ninguna fila del material del tramo" % n)
            continue
        if direccion is not None:
            partes = [p.strip() for p in direccion.split("->")]
            if len(partes) != 2:
                fallos.append("la direccion del par %s no tiene la forma 'madre -> hijo'" % n)
            elif set(partes) != {m["madre"], m["hijo"]}:
                fallos.append("la direccion del par %s nombra %r, que no son los dos nodos "
                              "resueltos de esa fila (%s, %s)" % (n, partes, m["madre"], m["hijo"]))
        filas.append({
            "puesto_tramo": n,
            "operacion": "OP-E-03",
            "marca": "LECTURA DIRIGIDA",
            "fuera_de_la_cola": True,
            "fuera_de_la_tasa_por_dominio": True,
            "mueve_el_marcador_del_cribado": False,
            "dominio": m["dominio"],
            "madre_de_la_bolsa": m["madre"],
            "hijo_de_la_bolsa": m["hijo"],
            "paso_casado": m["paso"],
            "clase": clase,
            "direccion_leida": direccion,
            "razon": razon,
            "vara": "banco 9.6.1 rama contenido manda; direccion por 9.6.2; tamano del solape no decide por 9.6.3",
        })
    faltan = sorted(set(por_n) - vistos)
    if faltan:
        fallos.append("faltan veredictos para las filas %s del tramo" % faltan)
    return filas, fallos, total_bolsa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-escribir", action="store_true")
    a = ap.parse_args()

    filas, fallos, total_bolsa = construir_filas()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NI SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    por_clase = collections.Counter(f["clase"] for f in filas)
    por_dominio = collections.Counter(f["dominio"] for f in filas)
    con_direccion = [f for f in filas if f["direccion_leida"]]
    sin_direccion = [f for f in filas if not f["direccion_leida"]]

    print("=" * 100)
    print("OP-E-03, VEREDICTOS DEL PRIMER TRAMO (vuelta 96, TAREA 3)")
    print("Bolsa de %d filas; leidas %d. Vara: banco 9.6.1 (clase), 9.6.2 (direccion), 9.6.3 (el solape no decide)."
          % (total_bolsa, len(filas)))
    print("TODAS LAS FILAS: LECTURA DIRIGIDA . FUERA DE LA COLA . FUERA DE LA TASA POR DOMINIO .")
    print("NO MUEVEN EL MARCADOR DEL CRIBADO.")
    print("=" * 100)
    print()
    print("| clase | que significa | cuantas de %d |" % len(filas))
    print("|---|---|---:|")
    print("| A | REPITE (lo que anade cabe en una linea) | %d |" % por_clase["A"])
    print("| B | DUDOSO (la vara no lo resuelve sola) | %d |" % por_clase["B"])
    print("| C | figura aparte | %d |" % por_clase["C"])
    print("| D | CONTINUA (trae procedimiento que el otro no tiene) | %d |" % por_clase["D"])
    print()
    for clase in ("A", "B", "C", "D"):
        nums = [f["puesto_tramo"] for f in filas if f["clase"] == clase]
        print("ENUMERACION clase %s (%d): %s" % (clase, len(nums), ", ".join(str(x) for x in nums) or "ninguna"))
    print()
    print("DIRECCION (banco 9.6.2), contada de la misma tabla:")
    print("| resultado | cuantas |")
    print("|---|---:|")
    print("| direccion LEIDA y afirmada | %d |" % len(con_direccion))
    print("| direccion NO RESUELTA, declarada como tal | %d |" % len(sin_direccion))
    print("ENUMERACION 'direccion no resuelta' (%d): %s"
          % (len(sin_direccion), ", ".join(str(f["puesto_tramo"]) for f in sin_direccion)))
    print()
    print("POR DOMINIO, Y SE ROTULA: ESTA TABLA NO ENTRA EN LA TASA POR DOMINIO DEL BANCO 9.27.")
    print("Se cuenta aparte, como manda el punto 5 de OP-E-03.verificacion.")
    print("| dominio | pares del tramo | A | B | C | D |")
    print("|---|---:|---:|---:|---:|---:|")
    for dom in sorted(por_dominio):
        del_dom = [f for f in filas if f["dominio"] == dom]
        cc = collections.Counter(f["clase"] for f in del_dom)
        print("| %s | %d | %d | %d | %d | %d |" % (dom, len(del_dom), cc["A"], cc["B"], cc["C"], cc["D"]))
    print()
    print("=" * 100)
    print("FIGURAS OBSERVADAS EN EL TRAMO (%d). No son veredictos de par." % len(FIGURAS))
    print("=" * 100)
    for i, (titulo, texto) in enumerate(FIGURAS, 1):
        print()
        print("%d. %s" % (i, titulo))
        print("   %s" % texto)
    print()

    if not a.sin_escribir:
        with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
            for fila in filas:
                f.write(json.dumps(fila, ensure_ascii=False) + "\n")
        print("ESCRITO: %s (%d filas). Unico fichero tocado por este instrumento."
              % (os.path.relpath(SALIDA, RAIZ).replace("\\", "/"), len(filas)))
    else:
        print("NO SE ESCRIBIO NADA (--sin-escribir).")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
