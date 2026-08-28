# -*- coding: utf-8 -*-
r"""vuelta99_tarea3_escribir_tramo4.py . VUELTA 99, TAREA 3: ESCRIBE EL CUARTO Y
ULTIMO TRAMO DE LECTURA DE OP-E-03 (filas 151 a 183 de
docs/plan/DIFERENCIA_CONTRA_COLA.jsonl), a partir del material impreso por
scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 150 --cuantos 33
(docs/loop/SALIDA_V99_TAREA3_TRAMO3_MATERIAL.txt).

CADA FILA ES UNA LECTURA A MANO: el juicio A/B/C/D del banco 9.6.1, la
direccion del 9.6.2, y las figuras (iman, falso amigo, casado por objeto) no
las produce ningun instrumento, las pone el ejecutor leyendo el material
entero. Este script solo la SERIALIZA con la marca completa de LECTURA
DIRIGIDA y las mismas guardas de rojo que el resto de la familia.

MECANICA DE ROJO: si el fichero de salida ya existe, si el conteo de filas no
da 33, si algun puesto_tramo se repite o no cae en el rango 151 a 183, o si
algun campo obligatorio falta, NO SE ESCRIBE NADA.

USO:
  python scripts/loop/vuelta99_tarea3_escribir_tramo4.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl")

VARA = ("banco 9.6.1 rama contenido manda; direccion por 9.6.2 (test: el hijo cabe "
        "entero dentro de UN paso de la madre, sin decir cual); tamano del solape no "
        "decide por 9.6.3; la figura de los dos sentidos por 9.22; la frontera "
        "caveat/refutacion por donde cae la tension, nombrada en el acta 98 3.5")

FILAS = [
    dict(n=151, dom="core", madre="conditions_precedent_financing", hijo="entender_term_sheet",
         paso=3, clase="D", dir=None,
         razon="El paso 3 (negociar el contrato del fundador ANTES de firmar el term sheet) es un tramite ESPECIFICO dentro de las condiciones previas al cierre. El hijo clasifica clausulas del term sheet por dos EJES DISTINTOS (economia y control), un marco de lectura general que no ejecuta ese tramite ni ningun otro paso entero de la madre. FALSO AMIGO POR OBJETO COMPARTIDO (el term sheet), no por accion: la madre lista condiciones de cierre, el hijo ensena a leer clausulas. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=152, dom="quality", madre="definiciones_operacionales_2", hijo="muestreo_de_aceptacion",
         paso=2, clase="D", dir=None,
         razon="El paso 2 (establecer el criterio de aceptacion o rechazo) es una linea generica de una definicion operacional CUALQUIERA. El hijo es el procedimiento COMPLETO de muestreo de aceptacion por lotes (Dodge-Romig): objetivo lote/proceso, tamano de muestra, niveles de riesgo alfa/beta, diseno del plan, aplicacion. La mayor parte de ese contenido (riesgo, diseno del plan) NO cabe dentro del paso 2 ni de ningun otro paso de la madre (que solo habla de metodo de prueba, comunicacion y consistencia entre inspectores): el hijo EXCEDE el paso casado. El test del 9.6.2 falla por exceso. NO RESUELTA."),
    dict(n=153, dom="quality", madre="dia_cero_defectos_3", hijo="eliminacion_causas_error_4",
         paso=4, clase="D", dir="dia_cero_defectos_3 -> eliminacion_causas_error_4",
         razon="El paso 4 de la madre SOLO anuncia el inicio de la fase ECR al dia siguiente del evento. El hijo, titulado exactamente 'Eliminacion de Causas de Error (ECR)', es el procedimiento COMPLETO de esa fase: canal de reporte, agradecimiento, clasificacion, accion, justificacion si no se actua, cierre. Coincidencia de sigla y de objeto: el paso nombra el procedimiento en una linea, el hijo lo ejecuta entero (9.6.2). La madre conserva material propio (organizar el evento, show business, firmas, reconocimiento) que el hijo no toca. RESUELTA."),
    dict(n=154, dom="core", madre="desarrollo_de_clientes_customer_development", hijo="customer_development_agile_pairing",
         paso=4, clase="D", dir="desarrollo_de_clientes_customer_development -> customer_development_agile_pairing",
         razon="El paso 4 dice 'combinar el aprendizaje del cliente con ingenieria agil para ajustar rapidamente el producto'; el hijo se titula 'Junta el aprendizaje del cliente con la construccion rapida del producto' y sus cinco pasos son exactamente esa combinacion (iteraciones cortas, un solo ciclo de aprendizaje y construccion, lanzar en pedazos, no cerrar specs, MVP). Los otros tres pasos de la madre (convertir hipotesis en preguntas, entrevistar antes de construir, iterar con feedback) no los toca el hijo. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=155, dom="quality", madre="transformacion_calidad_compromiso_alta_direccion_japon", hijo="planificacion_calidad_crosby",
         paso=5, clase="D", dir=None,
         razon="La madre (Deming, compromiso de la alta direccion, evitar que la calidad quede aislada en un area) y el hijo (Crosby, inventario escrito de actividades de calidad con responsable y linea de accion por tarea) son DOS MARCOS DE DOS AUTORES DISTINTOS con el mismo tema general y ningun paso en comun: el hijo no ejecuta 'evitar que la calidad quede aislada', hace un inventario operativo de actividades. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=156, dom="core", madre="formalizar_un_proceso_ad_hoc", hijo="metricas_calidad",
         paso=4, clase="D", dir="formalizar_un_proceso_ad_hoc -> metricas_calidad",
         razon="El paso 4 (establecer metricas de exito en cada etapa) cabe entero en el hijo, que es el 'como' generico de definir una metrica (atributo, metrica, metodo, documentacion con ID) sin exceder ese paso. FIGURA REGISTRADA, no adjudicada: metricas_calidad es NODO IMAN en este tramo, casado como hijo con TRES madres distintas (156, 157, 158) por el termino compartido 'metrica'; aqui el ajuste es limpio porque el paso casado nombra explicitamente 'establecer metricas'. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=157, dom="core", madre="medir_lo_que_importa_no_solo_lo_facil", hijo="metricas_calidad",
         paso=1, clase="D", dir=None,
         razon="La madre busca metricas PROXY para VALORES INTANGIBLES no medidos (social, ambiental, bienestar), justo lo que su entregable nombra. El hijo es una plantilla generica para definir CUALQUIER metrica cuantitativa y no distingue tangible de intangible ni menciona proxies. FALSO AMIGO POR TOKEN COMPARTIDO ('metrica'): mismo nodo iman de la fila 156, pero aqui el ajuste NO calza, porque el paso 1 casado (listar metricas actuales) es un inventario, no una definicion nueva. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=158, dom="core", madre="plan_mejora_procesos", hijo="metricas_calidad",
         paso=3, clase="D", dir="plan_mejora_procesos -> metricas_calidad",
         razon="El paso 3 (definir metricas y limites de control actuales) es compuesto; el hijo cubre entero el sub tramo de METRICAS (atributo, metrica, metodo, documentacion), sin exceder hacia limites de control, que la madre conserva sin tocar en otros pasos. Tercer ejemplar del nodo iman metricas_calidad (156, 157, 158): aqui, igual que en el 156, el paso casado nombra la operacion literal. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=159, dom="quality", madre="sujetos_de_control", hijo="establecer_metas_caracteristicas",
         paso=3, clase="D", dir=None,
         razon="El paso 3 (traducir la voz del cliente en caracteristicas, KPC) es la seleccion de sujetos de control; el hijo fija METAS CUANTIFICADAS para caracteristicas YA seleccionadas, una actividad posterior y distinta, no la ejecucion de ese paso. Es continuidad de proceso (KPC elegido, luego meta fijada), no un paso que se despliega en un procedimiento: el test de 'el hijo cabe entero en UN paso' no se cumple porque ningun paso de la madre pide fijar metas. FIGURA REGISTRADA: establecer_metas_caracteristicas es NODO IMAN, hijo de dos madres distintas de este tramo (159 y 173). NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=160, dom="core", madre="escenarios_diseno_modelo_negocio", hijo="escenarios_de_evolucion_de_la_ia",
         paso=5, clase="D", dir=None,
         razon="FALSO AMIGO POR TOKEN COMPARTIDO ('escenarios'): la madre disena escenarios de cliente o de entorno para el lienzo de modelo de negocio (Osterwalder); el hijo es una practica especifica de planificacion de riesgo ante la evolucion de la IA (Mollick), con senales de alerta y plan de contingencia que la madre no pide en ningun paso. El paso 5 casado (evaluar si un modelo sirve para todos los escenarios) no lo ejecuta el hijo. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=161, dom="core", madre="seis_herramientas_comunicacion_celebracion", hijo="celebracion_automatizada_de_hitos",
         paso=2, clase="D", dir="seis_herramientas_comunicacion_celebracion -> celebracion_automatizada_de_hitos",
         razon="El paso 2 ('disenar un mensaje de celebracion especifico para el logro del cliente') es casi verbatim el paso 2 del hijo ('disenar un mensaje de celebracion que se dispare inmediatamente despues del logro'). El hijo es la version AUTOMATIZADA y con upsell de la misma practica de celebracion; la madre conserva la evaluacion de canal y la medicion de reaccion, que el hijo no toca. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=162, dom="quality", madre="inventario_conocimiento_estadistico_personal", hijo="roi_proyectos_calidad",
         paso=4, clase="D", dir=None,
         razon="El paso 4 (integrar al personal estadistico en proyectos de mejora) es sobre GESTION DE PERSONAL; el hijo calcula el ROI FINANCIERO de un proyecto de calidad, una practica distinta que no ejecuta ese paso ni ningun otro de la madre (mapeo de talento, mentoria, formacion continua). NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=163, dom="entrega", madre="reconocer_mercancia_peligrosa_disfrazada", hijo="clasificar_tipo_paquete",
         paso=4, clase="D", dir=None,
         razon="CASADO POR OBJETO Y NO POR ACCION: los dos hablan de clasificar un paquete antes de despachar, pero la madre distingue mercancia PELIGROSA de la que no lo es (quimicos, baterias, liquidos inflamables) y el hijo distingue FORMA del paquete (plano, alargado, fragil) para fines de embalaje. El paso 4 (capacitarse antes del primer envio de este tipo) no lo ejecuta el hijo. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=164, dom="environmental", madre="identificacion_proveedores_criticos", hijo="validacion_externa_reportes",
         paso=4, clase="D", dir=None,
         razon="El paso 4 (revisar los reportes de sostenibilidad de la competencia para comparar) es investigacion COMPARATIVA hacia afuera; el hijo es la VALIDACION EXTERNA del reporte PROPIO (certificacion, comite de revision). Comparten el objeto 'reportes de sostenibilidad' pero no la accion. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=165, dom="core", madre="tipos_de_riesgo_invencion_vs_mercado", hijo="fundadores_lideran_validacion",
         paso=4, clase="D", dir=None,
         razon="El paso 4 decide QUE TIPO de validacion combinar segun el tipo de riesgo (tecnico o de mercado); el hijo decide QUIEN debe liderar la validacion (el fundador, no ventas ni marketing). Son dos ejes distintos del mismo proceso de Customer Development, y el hijo no ejecuta la decision de tipo de riesgo. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=166, dom="quality", madre="definicion_y_concepto_de_aseguramiento_de_calidad", hijo="planificacion_inicial_calidad",
         paso=1, clase="D", dir=None,
         razon="El paso 1 (definir hasta donde llega el aseguramiento de calidad en el negocio) es una decision de ALCANCE Y POLITICA; el hijo es un procedimiento OPERATIVO de planificacion de calidad en manufactura (revision de diseno, KPCs, clasificacion, capacidad de proceso), que no ejecuta esa decision de alcance ni ningun otro paso de la madre. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=167, dom="quality", madre="planificacion_recoleccion_datos", hijo="analisis_pareto_proyectos_elefante",
         paso=7, clase="D", dir=None,
         razon="El paso 7 (evaluar supuestos de tamano de muestra y de analisis) es un paso ESTADISTICO puntual dentro de un plan de recoleccion de datos de 13 pasos; el hijo trata de como DIVIDIR un proyecto demasiado grande en subproyectos con Pareto, un problema de alcance organizacional sin relacion con supuestos de muestreo. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=168, dom="core", madre="formalizar_junta_asesora", hijo="tamano_junta_directiva_vc",
         paso=6, clase="D", dir=None,
         razon="FALSO AMIGO POR TOKEN COMPARTIDO ('junta'): la madre formaliza la JUNTA ASESORA (advisors sin voto); el hijo decide el tamano de la JUNTA DIRECTIVA con inversionistas (board con voto y control). Son dos organos de gobierno distintos en una startup; el paso 6 (documentar tamano/composicion/operacion de la junta asesora) no lo ejecuta el hijo. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=169, dom="core", madre="modelo_customer_development", hijo="diseno_experimentos_pass_fail",
         paso=3, clase="D", dir="modelo_customer_development -> diseno_experimentos_pass_fail",
         razon="El paso 3 ('disenar experimentos para testear cada hipotesis fuera del edificio') se ejecuta entero en el hijo: definir que se quiere aprender, disenar el test pass/fail mas simple, fijar el criterio numerico de exito, ejecutar con clientes reales, evitar confundir maximo local con global, registrar insights. Los otros cuatro pasos de la madre (identificar el paso actual, formular hipotesis, evaluar stop sign, estar dispuesto a retroceder) no los toca el hijo. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=170, dom="quality", madre="rol_director_calidad", hijo="circulos_calidad_qc",
         paso=4, clase="D", dir=None,
         razon="El paso 4 (actuar como asesor estrategico en las decisiones de calidad que tu tomas) describe el ROL GENERAL del director; el hijo es la practica ESPECIFICA de circulos de calidad (dejar elegir tema, no controlar, reconocer al grupo), una tecnica participativa concreta que no es la ejecucion de ese rol asesor sino una practica distinta con su propia logica. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=171, dom="core", madre="canales_distribucion", hijo="ocho_fases_experiencia_cliente",
         paso=3, clase="D", dir=None,
         razon="El paso 3 (evaluar la integracion entre canales para una experiencia coherente) es sobre CANALES DE DISTRIBUCION (Osterwalder); el hijo es el marco de las OCHO FASES DE EXPERIENCIA DEL CLIENTE (Coleman), un framework distinto de otro autor que no ejecuta la integracion de canales. FALSO AMIGO POR TOKEN COMPARTIDO ('experiencia de cliente'). NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=172, dom="core", madre="desarrollo_en_espiral", hijo="protocepto",
         paso=1, clase="D", dir="desarrollo_en_espiral -> protocepto",
         razon="El paso 1 nombra literalmente el termino 'protocept' entre sus sinonimos (prototipo, MVP, protocept); el hijo, titulado 'protocept', es la elaboracion completa de como construirlo y usarlo con el cliente cada ciclo. Los otros pasos de la madre (probar con clientes reales para medir intencion de compra, revisar propuesta de valor, repetir 3 a 15 ciclos, documentar) quedan enteros y sin tocar por el hijo. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=173, dom="quality", madre="establecer_diseno_final_producto", hijo="establecer_metas_caracteristicas",
         paso=1, clase="D", dir=None,
         razon="El paso 1 (definir como autorizar y publicar el diseno final ya terminado) es un paso de GOBERNANZA Y CIERRE; el hijo fija METAS para caracteristicas, una actividad de planificacion TEMPRANA que logicamente precede a publicar un diseno final, no su ejecucion. Segundo ejemplar del NODO IMAN establecer_metas_caracteristicas (ver 159): aqui tampoco calza. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=174, dom="franquicias", madre="desarrollo_value_proposition_usp", hijo="posicionamiento_vs_competidores",
         paso=1, clase="D", dir="desarrollo_value_proposition_usp -> posicionamiento_vs_competidores",
         razon="El paso 1 (identificar que hace unico al negocio frente a competidores directos) se ejecuta entero en el hijo, que es la conversacion aplicada de ese analisis con un candidato a franquiciado (preguntar que otras franquicias considera, comparar en detalle, responder con las diferencias). Los otros pasos de la madre (analizar estrategias de diferenciacion del sector, definir la USP en una frase, validar consultas no solicitadas, documentar valor adicional) no los toca el hijo. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=175, dom="core", madre="validar_modelo_financiero", hijo="valor_de_vida_del_cliente",
         paso=2, clase="D", dir="validar_modelo_financiero -> valor_de_vida_del_cliente",
         razon="El paso 2 nombra literalmente 'Customer Lifetime Value (LTV)' junto a CAC y tasa de conversion; el hijo, titulado exactamente 'Valor de Vida del Cliente (Customer Lifetime Value - LTV)', desarrolla ese termino entero: calcularlo, monitorearlo, implementar programas para subirlo, mejorar retencion. La madre conserva CAC, tasa de conversion, costos operativos, runway y el P&L completo, que el hijo no toca. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=176, dom="quality", madre="constraint_management", hijo="caso_estudio_benchmarking_terminal",
         paso=4, clase="D", dir=None,
         razon="El paso 4 (elevar el desempeno de la restriccion mediante inversion o mejora) es un principio GENERICO de la Teoria de las Restricciones; el hijo es un CASO DE ESTUDIO DE BENCHMARKING con una metodologia distinta (costos controlables, rediseno organizacional, mantenimiento por riesgo, repetir benchmarking anual) que no ejecuta ese principio TOC. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=177, dom="core", madre="liderazgo_ejecutivo_innovacion", hijo="estrategia_de_innovacion_de_producto",
         paso=1, clase="D", dir="liderazgo_ejecutivo_innovacion -> estrategia_de_innovacion_de_producto",
         razon="El paso 1 ('define y comunica tu vision y tu estrategia de innovacion conectadas con hacia donde va tu negocio') se ejecuta entero en el hijo, titulado 'Estrategia de Innovacion de Producto y Tecnologia': objetivos, vinculo con metas del negocio, arenas estrategicas, buckets de recursos, roadmap, compromiso de largo plazo. Los otros pasos de la madre (participar en decisiones de seguir o frenar, revisar el portafolio, no microgestionar, metas personales) describen COMPORTAMIENTO DE LIDERAZGO y no los toca el hijo. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=178, dom="quality", madre="ingenieria_calidad_proveedores", hijo="desarrollar_estrategias_largo_plazo",
         paso=4, clase="D", dir=None,
         razon="El paso 4 (desarrollar relaciones de largo plazo con PROVEEDORES para conocer su cultura de calidad) es especifico de ingenieria de proveedores; el hijo es un ejercicio de ESTRATEGIA GENERAL DEL NEGOCIO (cinco areas clave, FODA, 4 a 5 estrategias), sin relacion con proveedores. FALSO AMIGO POR TOKEN COMPARTIDO ('largo plazo' / 'estrategias'). NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=179, dom="quality", madre="juran_rcca_metodo", hijo="diseno_implementacion_remedio",
         paso=3, clase="D", dir="juran_rcca_metodo -> diseno_implementacion_remedio",
         razon="El paso 3 ('Mejorar: disenar e implementar el remedio') es casi el titulo exacto del hijo, 'Diseno e Implementacion del Remedio', que lo desarrolla entero: verificar que la solucion cumple el objetivo, recursos, procedimientos a modificar, capacitacion, prueba de errores, plan de implementacion. Los otros tres pasos del metodo RCCA (definir, analizar, controlar) son fases distintas que el hijo no toca. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=180, dom="exportacion", madre="licenciamiento_tecnologico", hijo="proteccion_patentes_internacional",
         paso=3, clase="D", dir="licenciamiento_tecnologico -> proteccion_patentes_internacional",
         razon="El paso 3 (registrar patentes y marcas en cada pais objetivo, considerando PCT y Protocolo de Madrid) se ejecuta entero en el hijo: determinar paises, verificar requisitos de novedad, evaluar el PCT, consultar abogado de PI, buscar arte previo en WIPO. La madre conserva el resto del acuerdo de licencia (evaluar conveniencia, negociar compensacion, redactar contrato), que el hijo no toca. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=181, dom="environmental", madre="valor_intangible_sostenibilidad", hijo="alineacion_engagement_estrategia_general",
         paso=1, clase="D", dir=None,
         razon="El paso 1 (incorporar metricas de sostenibilidad en el seguimiento del negocio) es sobre MEDICION Y TRACKING; el hijo es sobre ALINEAR AL EQUIPO Y LIDERAR CON EL EJEMPLO (mostrar con hechos, elegir lideres creibles, reconocer errores), una practica de cultura y liderazgo que no ejecuta la incorporacion de metricas. FALSO AMIGO POR TOKEN COMPARTIDO ('engagement'/'compromiso'). NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
    dict(n=182, dom="core", madre="eliminar_desperdicio_organizacional", hijo="startup_como_experimento_cientifico",
         paso=4, clase="D", dir="eliminar_desperdicio_organizacional -> startup_como_experimento_cientifico",
         razon="El paso 4 ('usa el metodo cientifico: hipotesis, experimento, medicion, en vez de guiarte solo por intuicion') se ejecuta entero en el hijo, titulado 'La Startup como Experimento Cientifico': formular hipotesis falsable, disenar experimento que pueda fallar, ejecutar a pequena escala, analizar resultados contra la hipotesis. Los otros pasos de la madre (cuestionar si el proyecto vale la pena, revisar tareas eficientes sin aprendizaje, redirigir esfuerzo) son el tema mas amplio de eliminar desperdicio y el hijo no los toca. RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): SE CUMPLE."),
    dict(n=183, dom="core", madre="no_shop_agreement", hijo="dividends_terms",
         paso=2, clase="D", dir=None,
         razon="Las dos son clausulas del mismo libro (Venture Deals) y del mismo term sheet, pero SIN NINGUNA RELACION DE CONTENIDO: la madre es la clausula de exclusividad (no shop) y el hijo la clausula de dividendos. El paso 2 (esta clausula es vinculante desde la firma, a diferencia del resto) no lo ejecuta el hijo, que habla de porcentaje acumulativo, impacto en escenarios y aprobacion del consejo. Es el emparejamiento mas debil del tramo: mismo objeto general (term sheet) y ninguna accion compartida. NO RESUELTA. Test del banco 9.6.2 (el hijo cabe entero dentro de este paso, la madre conserva material propio): NO SE CUMPLE."),
]


CITAS_BANCO = ("9.6.1", "9.6.2", "9.6.3", "9.22")


def construir(fuente=None):
    """Devuelve (filas, fallos). NUNCA lanza excepcion: las cinco guardas se
    acumulan en `fallos` para que la prueba de mutacion pueda dispararlas una
    por una sobre una copia en memoria, sin tocar el fichero de salida."""
    fuente = FILAS if fuente is None else fuente
    fallos = []
    vistos = set()
    filas = []
    for f in fuente:
        n = f["n"]
        if not (151 <= n <= 183):
            fallos.append("puesto %r fuera del rango 151 a 183" % (n,))
        if n in vistos:
            fallos.append("puesto %r repetido dentro del tramo" % (n,))
        vistos.add(n)
        if f["clase"] not in ("A", "B", "C", "D"):
            fallos.append("puesto %s: clase %r no es A, B, C ni D" % (n, f["clase"]))
        if not (f.get("razon") or "").strip():
            fallos.append("puesto %s: razon vacia" % (n,))
        elif not any(c in f["razon"] for c in CITAS_BANCO):
            fallos.append("puesto %s: razon sin ninguna cita del banco (%s)"
                          % (n, ", ".join(CITAS_BANCO)))
        d = f.get("dir")
        if d is not None:
            partes = [p.strip() for p in d.split("->")]
            if len(partes) != 2:
                fallos.append("puesto %s: direccion sin la forma 'a -> b'" % (n,))
            elif set(partes) != {f["madre"], f["hijo"]}:
                fallos.append("puesto %s: direccion nombra un id ajeno al par (%s)"
                              % (n, d))
        filas.append({
            "puesto_tramo": n,
            "operacion": "OP-E-03",
            "marca": "LECTURA DIRIGIDA",
            "fuera_de_la_cola": True,
            "fuera_de_la_tasa_por_dominio": True,
            "mueve_el_marcador_del_cribado": False,
            "dominio": f["dom"],
            "madre_de_la_bolsa": f["madre"],
            "hijo_de_la_bolsa": f["hijo"],
            "paso_casado": f["paso"],
            "clase": f["clase"],
            "direccion_leida": f.get("dir"),
            "razon": f["razon"],
            "vara": VARA,
        })
    if not fallos and (len(vistos) != 33 or vistos != set(range(151, 184))):
        fallos.append("el tramo no cubre exactamente 151 a 183 sin huecos: trae %s"
                      % sorted(vistos))
    return filas, fallos


def main():
    if os.path.exists(SALIDA):
        print("ROJO: %s ya existe. NO SE ESCRIBE NADA." % os.path.relpath(SALIDA, RAIZ))
        return 1
    filas, fallos = construir()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        for r in filas:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("ESCRITO: %s, %d filas (151 a 183)." % (os.path.relpath(SALIDA, RAIZ), len(filas)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
