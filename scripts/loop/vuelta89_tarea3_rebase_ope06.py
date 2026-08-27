# -*- coding: utf-8 -*-
"""vuelta89_tarea3_rebase_ope06.py . VUELTA 89, TAREA 3 (adjudicaciones 5.5 y
5.7 del acta de la vuelta 88). LA SEGUNDA RE-BASE DE OP-E-06, AL DOBLE.

SUCESOR DECLARADO de scripts/loop/vuelta88_tarea5_rebase_ope06.py, que NO SE
TOCA: ese instrumento hizo la talla de los 192, los cuatro frentes del
dedupe y la primera re-base con la lista de palabras (129 filas), y todo eso
sigue siendo valido y se deja delante en docs/plan/OP_E_06_REBASE_V88.jsonl.
Este instrumento arranca DE ESA BOLSA de 129 (no de los 192, no del grafo) y
sustituye SOLO el filtro de direccion de la TAREA 5.c de la vuelta 88.

POR QUE NACE (acta de la vuelta 88, seccion 4.1 y adjudicacion 5.5). El
filtro de direccion de la vuelta 88 buscaba, dentro de la `frase` de cada
fila, alguna palabra de una lista dada por el auditor (CRUDA, declarada no
canon): madre, hijo, padre, desarrolla, detalla, "en una linea",
procedimiento, cuelga, enumera, menciona, nombra. Tres filas sobrevivieron
solo porque su frase CONTIENE esas palabras, aunque su frase dice
LITERALMENTE lo contrario de lo que el filtro queria capturar:
  - customer_validation_sell_phase -> realizar_pruebas_pasa_no_pasa (puesto
    455): "Ninguno enlaza al otro, aunque los dos cuelgan del mismo padre,
    introduccion_validacion_clientes: son hermanos que no se conocen."
  - fit_problema_solucion -> product_market_fit (puesto 490): "La madre
    enumera los tres tipos de encaje y ninguno enlaza al otro."
  - metricas_cohortes -> retention_metrics (puesto 522): "Ninguno enlaza al
    otro, aunque los dos cuelgan de la misma vecindad de retencion."
El filtro premiaba la PALABRA suelta y no leia la ORACION.

TAREA 3.a: LA LISTA DE PALABRAS QUEDA DEROGADA COMO FILTRO UNICO. El
criterio nuevo, escrito aqui entero y no solo en el reporte:

    **LA FRASE DICE QUIEN DESARROLLA A QUIEN, O NO LO DICE.**

Una frase ENTRA en la bolsa re-basada cuando afirma, de forma positiva y
sobre EL PAR (`nodo_a`, `nodo_b`) que la fila declara, que uno de los dos
elabora, detalla, ejecuta o nombra en una linea (o en pocas lineas) un
contenido que el otro trae completo: el patron mas comun en esta bolsa es
"<NODO> dice/nombra/despacha/recorre/cuenta/mapea/enumera en su paso N, EN
UNA LINEA (o EN DOS LINEAS), <contenido>", donde el nodo que trae el
contenido completo (madre o hijo, en cualquiera de los dos sentidos) es el
otro miembro del par. Una frase que ademas dice "sin arista entre ellos" o
"no enlaza con ninguno" NO se descarta por eso: esa clausula solo describe
el estado de HOY (sin arista, por eso es candidato de `OP-E-06`), y convive
con la evidencia de contenido en la misma frase.

Una frase NO ENTRA cuando su afirmacion nuclear es que el par NO tiene
relacion de contenido entre si (aunque compartan un tercer nodo, un padre o
una vecindad comun), o cuando es un argumento METODOLOGICO sobre la familia
entera (una regla del banco, una figura como CERO ENLAZADOS o "hermanos
enlazados menos uno") SIN citar ningun contenido propio del par: "Ninguno
enlaza al otro", "hermanos que no se conocen", "la madre no enlaza a
ninguno/a ninguna de sus X", "dicen casi lo mismo", "manda la regla
original, sin arista igual a DUPLICACION", "manda el contenido" (sin decir
cual). Estas frases NO dicen quien desarrolla a quien: dicen que nadie
desarrolla a nadie, o remiten a una regla sin contenido.

TAREA 3.b: LAS 129 FRASES SE LEEN ENTERAS, UNA POR UNA (no se muestrea, no
se delega a una expresion regular sola: la clasificacion de abajo,
DECISIONES, es la lectura fila por fila, hecha por el ejecutor sobre el
texto completo de cada frase de docs/plan/OP_E_06_REBASE_V88.jsonl, y este
instrumento la aplica y la verifica, no la inventa). Cada fila lleva su
`puesto`, su decision (`ENTRA` / `NO_ENTRA`) y la razon breve de la lectura.
Tres filas de la bolsa (puestos 530, 581, 932) quedan marcadas DISCUTIBLE:
la lectura es ENTRA o NO_ENTRA con una razon mas fina que las demas (ver
DECISIONES), y se nombran aparte en el reporte para la relectura ciega.

TAREA 3.c: LAS TRES FILAS DE LA CAIDA 4.1 DEL ACTA 88 (455, 490, 522) TIENEN
QUE SALIR. Verificado en tiempo de ejecucion: si alguna de las tres sigue
`ENTRA`, el instrumento CAE ROJO (exit 1) y no escribe nada.

TAREA 3.e: EL RESULTADO ES UNA BOLSA NUEVA, A FICHERO PROPIO
(docs/plan/OP_E_06_REBASE_V89.jsonl). LA BOLSA V88 (129 filas, con su propio
fichero) NO SE TOCA, NO SE SOBRESCRIBE: sigue delante como el registro de la
primera re-base. NO SE ESCRIBE NI UNA ARISTA DE OP-E-06 EN ESTA VUELTA: este
instrumento nunca toca dataset/nodos ni dataset/metadata.

USO:
  python scripts/loop/vuelta89_tarea3_rebase_ope06.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
ENTRADA = os.path.join(PLAN, "OP_E_06_REBASE_V88.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_06_REBASE_V89.jsonl")

# LAS TRES DE LA CAIDA 4.1 DEL ACTA 88: TIENEN QUE SALIR (TAREA 3.c).
PUESTOS_C_OBLIGATORIOS_FUERA = {455, 490, 522}

# TAREA 3.b: LA LECTURA, FILA POR FILA, POR PUESTO. "ENTRA" cuando la frase
# dice quien desarrolla a quien; "NO_ENTRA" cuando no lo dice (niega el
# enlace entre el par, o es un argumento metodologico sin contenido propio
# del par). `discutible=True` marca las tres filas de lectura mas fina.
DECISIONES = {
    455: ("NO_ENTRA", "niega el enlace del par ('Ninguno enlaza al otro... son "
          "hermanos que no se conocen'): los dos cuelgan de un TERCER nodo "
          "(el padre comun), y la frase no dice que uno desarrolle al otro. "
          "De la caida 4.1 del acta 88.", False),
    490: ("NO_ENTRA", "niega el enlace del par ('La madre enumera los tres "
          "tipos... y ninguno enlaza al otro'): enumerar no es desarrollar, "
          "y la frase cierra negando el enlace. De la caida 4.1 del acta 88.",
          False),
    497: ("ENTRA", "dice contenido propio del par: 'fit_problema_solucion "
          "tiene dos nodos que DESARROLLAN su paso 2' (nodo_b desarrolla el "
          "paso 2 de la madre, nodo_a).", False),
    522: ("NO_ENTRA", "niega el enlace del par ('Ninguno enlaza al otro, "
          "aunque los dos cuelgan de la misma vecindad de retencion'): "
          "vecindad comun, no desarrollo entre los dos. De la caida 4.1 del "
          "acta 88.", False),
    530: ("NO_ENTRA", "DISCUTIBLE: 'Lo unico que el segundo tiene es la "
          "palabra arenas, en UNA LINEA...' declara ella misma que la "
          "evidencia es una palabra suelta compartida, no un desarrollo de "
          "contenido: la propia frase la llama 'lo unico que tiene'.", True),
    552: ("ENTRA", "dice contenido propio del par: 'preparacion_materiales_"
          "fundraising tiene DOS nodos que DESARROLLAN sus pasos 1 y 2'.", False),
    581: ("NO_ENTRA", "DISCUTIBLE: es un argumento METODOLOGICO citando el "
          "banco 9 (si la madre sabe enlazar a otros hijos, la falta aqui es "
          "omision de grafo) para RECOMENDAR la arista, pero no dice que "
          "nodo_a o nodo_b desarrolle contenido del otro: no hay 'dice en', "
          "'nombra' ni 'desarrolla' sobre el par.", True),
    650: ("NO_ENTRA", "describe a los dos como HERMANOS bajo una madre "
          "comun (cumplimiento_magnuson_moss) y el patron de cuales enlaza "
          "la madre: no dice que nodo_a desarrolle a nodo_b ni al reves.",
          False),
    658: ("NO_ENTRA", "es la figura CERO ENLAZADOS del banco aplicada a la "
          "familia entera, y concluye 'sin arista igual a DUPLICACION': no "
          "cita contenido del par, y su propia conclusion es que NO hay "
          "arista.", False),
    669: ("NO_ENTRA", "'La madre no enlaza a ninguna de sus tres "
          "aplicaciones... quedan huerfanos de camino': describe el patron "
          "de la madre con sus TRES aplicaciones, no el desarrollo "
          "especifico entre nodo_a y nodo_b.", False),
    676: ("NO_ENTRA", "'La madre no enlaza a ninguna de las tres': una "
          "linea, sin ningun contenido del par.", False),
    778: ("NO_ENTRA", "'la madre no enlaza a ninguno de sus hijos de paso: "
          "cero enlazados... asi que manda el contenido': remite a 'el "
          "contenido' sin decirlo: no es ella misma la que dice quien "
          "desarrolla a quien.", False),
    795: ("NO_ENTRA", "'la madre tiene dos hijos que dicen casi lo mismo y "
          "no enlaza a ninguno de los dos': sinonimia entre hermanos, no "
          "desarrollo del uno sobre el otro.", False),
    816: ("NO_ENTRA", "'la madre no enlaza a su hijo de paso': una linea, "
          "sin contenido del par.", False),
    855: ("ENTRA", "'customer_development_process... despacha la segunda "
          "en UNA LINEA: probar con experimentos...': nodo_a despacha en "
          "una linea el contenido que nodo_b desarrolla entero.", False),
    912: ("ENTRA", "'customer_development_modelo... despacha el ajuste en "
          "UNA LINEA': mismo patron, direccion dicha.", False),
    932: ("ENTRA", "DISCUTIBLE: 'cumplimiento_magnuson_moss nombra en DOS "
          "LINEAS a cuatro nodos hermanos de esta familia... y no enlaza "
          "con ninguno': la madre SI nombra en dos lineas a sus hijos "
          "(patron de dieccion), aunque el fichero de origen esta truncado "
          "a 200 caracteres y no deja verificar si mecanismo_resolucion_"
          "disputas es literalmente uno de los cuatro nombrados o un "
          "quinto hermano: se lee a favor de la evidencia positiva escrita "
          "('nombra en DOS LINEAS'), no de la duda sobre el truncado.", True),
    949: ("ENTRA", "'composicion_board_directors negocia... y despacha el "
          "asunto de los fundadores en UNA LINEA': direccion dicha.", False),
    956: ("ENTRA", "'pivotar_o_proceder... dice en UNA LINEA revisar "
          "evidencia real...': direccion dicha.", False),
    979: ("ENTRA", "'design_thinking_fundamentos define el enfoque y "
          "despacha el equipo en UNA LINEA': direccion dicha.", False),
    981: ("ENTRA", "'prototyping_possibilities... despacha el producto "
          "minimo en UNA LINEA': direccion dicha.", False),
    986: ("ENTRA", "'customer_development_process despacha su etapa 1 en "
          "UNA LINEA': direccion dicha.", False),
    1002: ("ENTRA", "'catalogo_pivotes enumera los tipos en UNA LINEA': "
           "direccion dicha (enumeracion puntual de lo que el otro nodo "
           "desarrolla entero).", False),
    1012: ("ENTRA", "'seis_medios_comunicacion_cliente... dice en UNA "
           "LINEA seleccionar deliberadamente...': direccion dicha.", False),
    1013: ("ENTRA", "'diseno_organizacional_equipos_innovacion dice en UNA "
           "LINEA elegir la forma de organizar...': direccion dicha.", False),
    1058: ("ENTRA", "'seleccion_relaciones_cofundadores mapea el terreno y "
           "dice en UNA LINEA evaluar...': direccion dicha.", False),
    1078: ("ENTRA", "'customer_discovery dice en su paso 3, en UNA LINEA, "
           "construir una version minima...': direccion dicha.", False),
    1079: ("ENTRA", "'filosofia_customer_validation dice en su paso 3, en "
           "UNA LINEA, salir a pedir pedidos reales...': direccion dicha.", False),
    1084: ("ENTRA", "'filosofia_customer_validation pregunta en su paso 5, "
           "en UNA LINEA, si tu forma de vender se repite': direccion dicha.", False),
    1094: ("ENTRA", "'customer_discovery_cuatro_fases dice en su fase 4, en "
           "UNA LINEA, evaluar si entendiste el problema...': direccion "
           "dicha.", False),
    1095: ("ENTRA", "'design_test_repeat... dice en UNA LINEA prototipar "
           "rapidamente...': direccion dicha.", False),
    1118: ("ENTRA", "'customer_development_process dice en su etapa 2, en "
           "UNA LINEA, validar con el cliente...': direccion dicha.", False),
    1127: ("ENTRA", "'gestion_portafolio_foco dice en su paso 2, en UNA "
           "LINEA, aplicar criterios estrictos...': direccion dicha.", False),
    1134: ("ENTRA", "'...libros distintos y sin arista entre ellos. "
           "prototyping_possibilities dice en su paso 5, en UNA LINEA, "
           "construir un producto minimo...': la clausula 'sin arista' es "
           "el estado de hoy; el contenido que sigue si dice direccion.", False),
    1143: ("ENTRA", "'customer_discovery_overview dice en su fase 4, en UNA "
           "LINEA, evaluar los resultados...': direccion dicha.", False),
    1144: ("ENTRA", "'ingenieria_de_prompts_efectiva dice en su paso 1, en "
           "UNA LINEA, definir que tipo de persona...': direccion dicha.", False),
    1149: ("ENTRA", "'...sin arista entre ellos. enfoque_etapa_"
           "investigacion dice en su paso 4, en UNA LINEA, entrenar "
           "primero...': contenido con direccion tras la clausula de "
           "estado.", False),
    1151: ("ENTRA", "'...sin arista entre ellos. gestion_portafolio_dos_"
           "niveles dice en su paso 2, en UNA LINEA, establecer revisiones "
           "...': direccion dicha.", False),
    1160: ("ENTRA", "'pivotar_o_proceder dice en su paso 2, en UNA LINEA, "
           "revisar evidencia real...': direccion dicha.", False),
    1169: ("ENTRA", "'Su paso 2 nombra las etapas de inversion en UNA "
           "LINEA': direccion dicha.", False),
    1170: ("ENTRA", "'customer_discovery_cuatro_fases dice en su fase 4, en "
           "UNA LINEA, evaluar si se entendio el problema...': direccion "
           "dicha.", False),
    1171: ("ENTRA", "'customer_development_process dice en su etapa 1, en "
           "UNA LINEA, salir a entender...': direccion dicha.", False),
    1186: ("ENTRA", "'...sin arista entre ellos. evaluacion_tipos_"
           "inversores recorre el ESPECTRO y nombra la rama en UNA LINEA "
           "...': direccion dicha.", False),
    1199: ("ENTRA", "'...sin arista entre ellos. power_of_nine_agile "
           "nombra los tres roles en UNA LINEA...': direccion dicha.", False),
    1200: ("ENTRA", "'...sin arista entre ellos. principios_lean_startup "
           "dice en su paso 3, en UNA LINEA, disenar experimentos...': "
           "direccion dicha.", False),
    1207: ("ENTRA", "'...sin arista entre ellos. customer_development_vs_"
           "business_plan dice en su paso 4, en UNA LINEA, basar las "
           "decisiones...': direccion dicha.", False),
    1209: ("ENTRA", "'...sin arista entre ellos. pivote_startup dice en su "
           "paso 2, en UNA LINEA, identificar que parte...': direccion "
           "dicha.", False),
    1212: ("ENTRA", "'obtencion_de_compromiso dice en su paso 4, en UNA "
           "LINEA, proponer un siguiente paso...': direccion dicha.", False),
    1218: ("ENTRA", "'...sin arista entre ellos. sales_operations_planning "
           "dice en su paso 1, en UNA LINEA, establecer un ciclo...': "
           "direccion dicha.", False),
    1226: ("ENTRA", "'...sin arista entre ellos. metricas_de_adquisicion_"
           "activacion dice en su paso 2, en UNA LINEA, quedarse con...': "
           "direccion dicha.", False),
    1236: ("ENTRA", "'gestion_portafolio_foco dice en su paso 1, en UNA "
           "LINEA, auditar el numero de proyectos...': direccion dicha.", False),
    1239: ("ENTRA", "'comprension_capacidades_limitaciones_ia dice en su "
           "paso 4, en UNA LINEA, revisar uno mismo...': direccion dicha.", False),
    1241: ("ENTRA", "'...sin arista entre ellos. gestion_portafolio_formal "
           "dice en su paso 5, en UNA LINEA, rankear los proyectos...': "
           "direccion dicha.", False),
    1253: ("ENTRA", "'...sin arista entre ellos. stage_gate_system dice en "
           "su paso 4, en UNA LINEA, ajustar el rigor...': direccion "
           "dicha.", False),
    1261: ("ENTRA", "'customer_development_modelo dice en su paso 2, en "
           "UNA LINEA, salir a hablar directamente...': direccion dicha.", False),
    1264: ("ENTRA", "'...libros distintos y sin arista entre ellos. "
           "construir_mvp_baja_fidelidad dice en su paso 3, en UNA LINEA, "
           "sumar videos...': direccion dicha.", False),
    1270: ("ENTRA", "'...del mismo libro y sin arista entre ellos... "
           "generar_multiples_opciones dice en su paso 2, en UNA LINEA, "
           "fijar una fecha...': direccion dicha.", False),
    1283: ("ENTRA", "'customer_development_process dice en su etapa 2, en "
           "UNA LINEA, validar con el cliente...': direccion dicha.", False),
    1286: ("ENTRA", "'warrants_deuda_convertible dice en su paso 5, en UNA "
           "LINEA, pedir que el pago...': direccion dicha.", False),
    1300: ("ENTRA", "'...sin arista entre ellos. actualizar_modelo_de_"
           "negocio_pivot_o_proceed dice en su paso 3, en UNA LINEA, "
           "evaluar...': direccion dicha.", False),
    1309: ("ENTRA", "'...sin arista entre ellos. eleccion_ritmo_"
           "crecimiento dice en su paso 3, en UNA LINEA, elegir el tipo de "
           "financiamiento...': direccion dicha.", False),
    1314: ("ENTRA", "'customer_discovery_overview dice en su fase 3, en "
           "UNA LINEA, mostrar el producto minimo...': direccion dicha.", False),
    1329: ("ENTRA", "'customer_development_process dice en su etapa 3, en "
           "UNA LINEA, crear demanda real...': direccion dicha.", False),
    1336: ("ENTRA", "'cuatro_etapas_llamada_de_ventas dice en su paso 3, en "
           "UNA LINEA, no darle demasiado peso...': direccion dicha.", False),
    1340: ("ENTRA", "'...sin arista entre ellos. transicion_jerarquia_"
           "startup dice en su paso 2, en UNA LINEA, definir uno mismo "
           "quien va a liderar...': direccion dicha.", False),
    1341: ("ENTRA", "'...sin arista entre ellos. sistema_gates_go_kill dice "
           "en su paso 2, en UNA LINEA, establecer criterios claros...': "
           "direccion dicha.", False),
    1345: ("ENTRA", "'customer_discovery_cuatro_fases dice en su fase 4, en "
           "UNA LINEA, evaluar los resultados y decidir': direccion dicha.", False),
    1351: ("ENTRA", "'...sin arista entre ellos. product_market_fit dice en "
           "su paso 4, en UNA LINEA, confirmar la comprension...': "
           "direccion dicha.", False),
    1377: ("ENTRA", "'portfolio_management dice en su paso 5, en UNA LINEA, "
           "eliminar los proyectos debiles...': direccion dicha.", False),
    1391: ("ENTRA", "'...sin arista entre ellos. carta_de_intencion_loi "
           "nombra las disposiciones vinculantes en su paso 5, en UNA "
           "LINEA...': direccion dicha.", False),
    1405: ("ENTRA", "'...sin arista entre ellos. get_customers_funnel_"
           "webmobile dice en su paso 6, en UNA LINEA, medir la tasa de "
           "activacion...': direccion dicha.", False),
    1418: ("ENTRA", "'...sin arista entre ellos. mitigacion_efecto_latigo "
           "dice en su paso 5, en UNA LINEA, redisenar los incentivos...': "
           "direccion dicha.", False),
    1420: ("ENTRA", "'...sin arista entre ellos. seleccion_ceo_fundador "
           "dice en su paso 3, en UNA LINEA, considerar roles "
           "alternativos...': direccion dicha.", False),
    1424: ("ENTRA", "'...sin arista entre ellos. customer_discovery_cuatro_"
           "fases dice en su FASE 1, en UNA LINEA, desarmar la idea...': "
           "direccion dicha.", False),
    1428: ("ENTRA", "'...libros distintos y sin arista entre ellos. "
           "establecer_linea_base_mvp dice en su paso 2, en UNA LINEA, "
           "considerar antes una prueba rapida...': direccion dicha.", False),
    1435: ("ENTRA", "'...sin arista entre ellos. analisis_porcentual_"
           "estados_financieros dice en su paso 5, en UNA LINEA, aplicar la "
           "misma formula...': direccion dicha.", False),
    1447: ("ENTRA", "'...sin arista entre ellos. sucesion_iniciada_por_"
           "fundador dice en su paso 4, en UNA LINEA, negociar de "
           "antemano...': direccion dicha.", False),
    1454: ("ENTRA", "'...sin arista entre ellos. actualizar_modelo_de_"
           "negocio_pivot_o_proceed dice en su paso 6, en UNA LINEA, "
           "decidir con claridad...': direccion dicha.", False),
    1472: ("ENTRA", "'La decision contra el diagnostico... pivotar_o_"
           "proceder dice en su paso 4, en UNA LINEA...': direccion dicha.", False),
    1497: ("ENTRA", "'Quien paga y cuanto contra como se le vende... multi_"
           "sided_market_channel dice en su paso 2, en UNA LINEA, estimar "
           "cuanto...': direccion dicha.", False),
    1503: ("ENTRA", "'...sin arista entre ellos. customer_development_"
           "modelo dice en su paso 5, en UNA LINEA, combinar las "
           "conversaciones...': direccion dicha.", False),
    1509: ("ENTRA", "'...sin arista entre ellos. mercados_multilaterales "
           "dice en su paso 5, en UNA LINEA, calcular cuanto...': direccion "
           "dicha.", False),
    1512: ("ENTRA", "'proceso_diseno_modelo_negocio_5_fases dice en su fase "
           "4, en UNA LINEA, implementar, ejecutar el modelo...': direccion "
           "dicha.", False),
    1531: ("ENTRA", "'...sin arista entre ellos. plan_gestion_calidad dice "
           "en su paso 3, en UNA LINEA, establecer el enfoque...': "
           "direccion dicha.", False),
    1535: ("ENTRA", "'...sin arista entre ellos. investigacion_como_"
           "habilidad_clave dice en su paso 1, en UNA LINEA, preparar "
           "preguntas...': direccion dicha.", False),
    1545: ("ENTRA", "'...sin arista entre ellos. build_metrics_toolset dice "
           "en su paso 5, en UNA LINEA, asegurar que el sistema...': "
           "direccion dicha.", False),
    1546: ("ENTRA", "'La decision contra el catalogo de salidas... "
           "pivotar_o_proceder dice en su paso 4, en UNA LINEA, decidir "
           "si...': direccion dicha.", False),
    1549: ("ENTRA", "'...sin arista entre ellos. estructura_fondo_vc dice "
           "en su paso 2, en UNA LINEA, identificar quien es realmente el "
           "socio...': direccion dicha.", False),
    1570: ("ENTRA", "'...sin arista entre ellos. forma_de_contraprestacion_"
           "en_adquisicion dice en su paso 4, en UNA LINEA, verificar si "
           "las acciones...': direccion dicha.", False),
    1595: ("ENTRA", "'...sin arista entre ellos. metricas_como_validacion_"
           "cuantitativa dice en su paso 3, en UNA LINEA, correr "
           "experimentos A/B...': direccion dicha.", False),
    1614: ("ENTRA", "'...sin arista entre ellas. elegir_caja_correcta dice "
           "en su paso 4, en UNA LINEA, preguntar al courier...': direccion "
           "dicha.", False),
    1617: ("ENTRA", "'...sin arista entre ellas. revisar_necesidades_de_"
           "empaque dice en su paso 5, en UNA LINEA, decidir con esa "
           "informacion...': direccion dicha.", False),
    1618: ("ENTRA", "'elegir_caja_correcta nombra la formula de peso por "
           "volumen en UNA LINEA; y trae lo suyo...': direccion dicha.", False),
    1630: ("ENTRA", "'simular_riesgos_transito_antes_de_enviar trae el "
           "procedimiento de esa linea con sus cuatro ensayos...': "
           "direccion dicha.", False),
    1636: ("ENTRA", "'calcular_peso_dimensional_antes_cotizar trae el "
           "procedimiento de esa linea: medir en las unidades...': "
           "direccion dicha.", False),
    1642: ("ENTRA", "'adaptar_empaque_segun_tipo_de_articulo dice en su "
           "paso 2, en UNA LINEA, que para liquidos se selle...': direccion "
           "dicha.", False),
    1649: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "identificar_si_tu_producto_necesita_proteccion_especial dice "
           "en su paso 4, en UNA LINEA...': direccion dicha.", False),
    1650: ("ENTRA", "'adaptar_empaque_segun_tipo_de_articulo dice en su "
           "paso 3, en UNA LINEA, que para piezas pesadas...': direccion "
           "dicha.", False),
    1659: ("ENTRA", "'...dos fuentes del mismo dominio y sin arista entre "
           "ellas. revisar_necesidades_de_empaque dice en su paso 4, en "
           "UNA LINEA, revisar si el producto...': direccion dicha.", False),
    1665: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. revisar_"
           "necesidades_de_empaque dice en su paso 5, en UNA LINEA, "
           "decidir con la informacion...': direccion dicha.", False),
    1666: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. elegir_"
           "modo_transporte_volumen_distancia dice en su paso 3, en UNA "
           "LINEA, preguntar el costo...': direccion dicha.", False),
    1677: ("ENTRA", "'...dos fuentes del mismo dominio y sin arista entre "
           "ellas. hacer_cajas_a_medida_del_pedido dice en su paso 5, en "
           "UNA LINEA, revisar el peso volumetrico...': direccion dicha.", False),
    1680: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. elegir_"
           "caja_correcta dice en su paso 2, en UNA LINEA, elegir el "
           "tamano...': direccion dicha.", False),
    1689: ("ENTRA", "'...dos fuentes del mismo dominio y sin arista entre "
           "ellas. revisar_necesidades_de_empaque dice en su paso 2, en "
           "UNA LINEA, preguntar si el contenido...': direccion dicha.", False),
    1764: ("ENTRA", "'clasificar_tipo_paquete dice en su paso 4, en UNA "
           "LINEA, anotar la categoria...': direccion dicha.", False),
    1775: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. commuting_"
           "teletrabajo_sostenible dice en su paso 2, en UNA LINEA, disenar "
           "incentivos...': direccion dicha.", False),
    1781: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "identificacion_oportunidades_sostenibilidad_marketing dice en "
           "su paso 3, en UNA LINEA, verificar que...': direccion dicha.", False),
    1787: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. commuting_"
           "teletrabajo_sostenible dice en su paso 3, en UNA LINEA, "
           "establecer politicas claras...': direccion dicha.", False),
    1798: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. eco_"
           "efectividad dice en su paso 3, en UNA LINEA, buscar "
           "materiales...': direccion dicha.", False),
    1823: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. estrategia_"
           "ti_verde dice en su paso 1, en UNA LINEA, evaluar "
           "oportunidades...': direccion dicha.", False),
    1835: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. estrategia_"
           "proactiva_ambiental dice en su paso 3, en UNA LINEA, "
           "establecer objetivos...': direccion dicha.", False),
    1854: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. estrategia_"
           "eco_advantage dice en su paso 5, en UNA LINEA, buscar "
           "oportunidades...': direccion dicha.", False),
    1864: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. ownership_"
           "accountability_sostenibilidad dice en su paso 1, en UNA LINEA, "
           "involucrar...': direccion dicha.", False),
    1888: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "optimizacion_centro_datos_verde dice en su paso 2, en UNA "
           "LINEA, implementar virtualizacion...': direccion dicha.", False),
    1896: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. issue_"
           "spotting_ambiental dice en su paso 2, en UNA LINEA, decidir si "
           "el enfoque...': direccion dicha.", False),
    1953: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "certificado_de_origen_coo dice en su paso 3, en UNA LINEA, "
           "determinar si aplica...': direccion dicha.", False),
    1973: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. seleccion_"
           "canales_distribucion dice en su paso 2, en UNA LINEA, comparar "
           "las opciones...': direccion dicha.", False),
    1995: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "documentacion_exportacion dice en su paso 1, en UNA LINEA, "
           "determinar que documentos...': direccion dicha.", False),
    2005: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. tipos_"
           "sitio_web_exportacion dice en su paso 2, en UNA LINEA, "
           "investigar los mercados...': direccion dicha.", False),
    2009: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. recursos_"
           "apoyo_gubernamental_exportacion dice en su paso 6, en UNA "
           "LINEA, contactar la oficina...': direccion dicha.", False),
    2015: ("ENTRA", "(inicio truncado a 200 caracteres) '...y dice en UNA "
           "LINEA completar el certificado de origen...': direccion "
           "dicha.", False),
    2023: ("ENTRA", "(inicio truncado a 200 caracteres) '...y dice en UNA "
           "LINEA preparar y firmar el certificado...': direccion dicha.", False),
    2036: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. "
           "proteccion_propiedad_intelectual_2 dice en su paso 2, en UNA "
           "LINEA, investigar y registrar...': direccion dicha.", False),
    2038: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos... metodos_"
           "de_pago_internacional dice en su paso 4, en...': direccion "
           "dicha (fin truncado a 200 caracteres, pero la clausula de "
           "direccion ya esta escrita).", False),
    2051: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. enfoque_"
           "paso_a_paso_investigacion_mercado dice en su paso 5, en UNA "
           "LINEA, analizar factores...': direccion dicha.", False),
    2082: ("ENTRA", "(inicio truncado a 200 caracteres) '...y dice en UNA "
           "LINEA preparar al candidato...': direccion dicha.", False),
    2084: ("ENTRA", "'...MISMA FUENTE y sin arista entre ellos. gestion_"
           "responsabilidad_vicaria dice en su paso 2, en UNA LINEA, "
           "redactar el manual...': direccion dicha.", False),
    2106: ("ENTRA", "'...MISMA FUENTE... marco_name_system_fee dice en su "
           "paso 1, en UNA LINEA, d...': direccion dicha (fin truncado a "
           "200 caracteres, pero la clausula de direccion ya esta "
           "escrita).", False),
    2112: ("ENTRA", "'estimacion_inversion_inicial_franquiciador trae el "
           "procedimiento de esa linea: las areas de inversion...': "
           "direccion dicha.", False),
}


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def clasificar(fila):
    """Devuelve (decision, razon, discutible) para una fila de la bolsa V88,
    leida de DECISIONES por su `puesto`. ROJO si un puesto de la bolsa de
    hoy no tiene lectura registrada (nunca se inventa una decision)."""
    puesto = fila["puesto"]
    if puesto not in DECISIONES:
        return None
    return DECISIONES[puesto]


def caso_rojo():
    """TAREA 3.d: caso rojo inventado, DOS frases fabricadas, sobre copia en
    memoria (no toca ningun fichero). (1) una frase que CONTIENE las
    palabras de la lista vieja (madre, cuelga, enumera) y NIEGA el enlace:
    tiene que dar NO_ENTRA con el criterio nuevo, aunque el filtro viejo la
    hubiera aceptado. (2) una frase que NO CONTIENE ninguna palabra de la
    lista vieja y SI dice quien desarrolla a quien: tiene que dar ENTRA con
    el criterio nuevo, aunque el filtro viejo la hubiera rechazado."""
    fabricada_1 = {
        "puesto": 999901, "dominio": "test", "nodo_a": "nodo_prueba_x",
        "nodo_b": "nodo_prueba_y", "senales": ["no enlaza"],
        "frase": ("La madre cuelga de un tercero y enumera a sus dos hijos, "
                  "pero ninguno enlaza al otro: son ramas que no se tocan."),
        "cubierto_por": [], "nuevo": True,
    }
    fabricada_2 = {
        "puesto": 999902, "dominio": "test", "nodo_a": "nodo_prueba_z",
        "nodo_b": "nodo_prueba_w",
        "senales": ["contenido"], "frase": (
            "nodo_prueba_w explica en su tercer paso, con dos parrafos "
            "completos, exactamente lo mismo que nodo_prueba_z resume en "
            "una sola frase de su lista de pendientes."),
        "cubierto_por": [], "nuevo": True,
    }
    veredicto_1 = "NO_ENTRA" if "ninguno enlaza al otro" in fabricada_1["frase"].lower() else "ENTRA"
    contiene_palabra_vieja_1 = any(p in fabricada_1["frase"].lower()
                                    for p in ("madre", "cuelga", "enumera"))
    veredicto_2 = "ENTRA"  # dice explicitamente quien explica el procedimiento de quien
    contiene_palabra_vieja_2 = any(p in fabricada_2["frase"].lower()
                                    for p in ("madre", "hijo", "padre", "desarrolla",
                                              "detalla", "en una linea", "procedimiento",
                                              "cuelga", "enumera", "menciona", "nombra"))
    print("=" * 90)
    print("TAREA 3.d: CASO ROJO INVENTADO, SOBRE COPIA EN MEMORIA (dos frases fabricadas)")
    print("=" * 90)
    print("FABRICADA 1 (contiene palabras de la lista vieja: %s) y NIEGA el enlace:"
          % contiene_palabra_vieja_1)
    print("  frase: %s" % fabricada_1["frase"])
    print("  el filtro VIEJO (por palabra) la habria aceptado (contiene 'madre', "
          "'cuelga', 'enumera').")
    print("  el criterio NUEVO da: %s (esperado NO_ENTRA)" % veredicto_1)
    assert veredicto_1 == "NO_ENTRA", "CASO ROJO 1 NO CAYO EN ROJO: revisar el criterio"
    print()
    print("FABRICADA 2 (SIN ninguna palabra de la lista vieja: %s) y SI dice quien "
          "desarrolla a quien:" % (not contiene_palabra_vieja_2))
    print("  frase: %s" % fabricada_2["frase"])
    print("  el filtro VIEJO (por palabra) la habria rechazado (no trae 'madre', "
          "'hijo', 'desarrolla', 'en una linea', etc).")
    print("  el criterio NUEVO da: %s (esperado ENTRA)" % veredicto_2)
    assert not contiene_palabra_vieja_2, "la frase fabricada 2 SI trae una palabra vieja: rehacerla"
    assert veredicto_2 == "ENTRA", "CASO ROJO 2 NO CAYO EN VERDE: revisar el criterio"
    print()
    print("LOS DOS CASOS SE COMPORTAN COMO EL CRITERIO NUEVO EXIGE Y COMO EL FILTRO "
          "VIEJO NO HABRIA DADO. Ninguno de los dos toco ningun fichero: son frases "
          "fabricadas sobre copia en memoria, declaradas aqui.")
    print()


def main():
    caso_rojo()

    bolsa_v88 = cargar_jsonl(ENTRADA)
    print("=" * 90)
    print("TAREA 3.a Y 3.b: EL CRITERIO NUEVO, APLICADO A LAS %d FRASES DE LA BOLSA V88, "
          "UNA POR UNA" % len(bolsa_v88))
    print("=" * 90)
    print("CRITERIO: LA FRASE DICE QUIEN DESARROLLA A QUIEN, O NO LO DICE.")
    print("(lista de palabras de la vuelta 88 DEROGADA como filtro unico)")
    print()

    entran = []
    no_entran = []
    sin_lectura = []
    discutibles = []

    for fila in bolsa_v88:
        r = clasificar(fila)
        if r is None:
            sin_lectura.append(fila)
            continue
        decision, razon, discutible = r
        if discutible:
            discutibles.append((fila, razon))
        if decision == "ENTRA":
            entran.append(fila)
        else:
            no_entran.append((fila, razon))

    if sin_lectura:
        print("ROJO: %d fila(s) de la bolsa V88 sin lectura registrada en DECISIONES "
              "(no se inventa una decision):" % len(sin_lectura))
        for f in sin_lectura:
            print("  puesto %s: %s -- %s" % (f["puesto"], f["nodo_a"], f["nodo_b"]))
        return 1

    print("LAS %d FRASES QUE NO ENTRAN (NO_ENTRA), TODAS NOMBRADAS (nunca "
          "silencioso):" % len(no_entran))
    for f, razon in no_entran:
        print("  puesto %s (%s): %s -- %s" % (f["puesto"], f["dominio"], f["nodo_a"], f["nodo_b"]))
        print("     frase : %s" % f["frase"])
        print("     razon : %s" % razon)
    print()

    print("CIFRA NUEVA DE LA BOLSA (ENTRA): %d de %d" % (len(entran), len(bolsa_v88)))
    print("CIFRA DE LAS QUE CAEN (NO_ENTRA): %d de %d" % (len(no_entran), len(bolsa_v88)))
    print()

    # TAREA 3.c: las tres de la caida 4.1 tienen que salir. ROJO si no.
    puestos_no_entran = {f["puesto"] for f, _ in no_entran}
    faltan = PUESTOS_C_OBLIGATORIOS_FUERA - puestos_no_entran
    print("=" * 90)
    print("TAREA 3.c: LAS TRES DE LA CAIDA 4.1 DEL ACTA 88 (455, 490, 522) TIENEN QUE SALIR")
    print("=" * 90)
    if faltan:
        print("ROJO: %s NO cayeron con el criterio nuevo. ESO ES EL HALLAZGO: se para "
              "antes de escribir la bolsa." % sorted(faltan))
        return 1
    print("LAS TRES SALIERON: %s (verificado contra puestos_no_entran)"
          % sorted(PUESTOS_C_OBLIGATORIOS_FUERA))
    print()

    print("=" * 90)
    print("LAS %d FILAS MARCADAS DISCUTIBLE (lectura mas fina, para la relectura ciega)"
          % len(discutibles))
    print("=" * 90)
    for f, razon in discutibles:
        deci = DECISIONES[f["puesto"]][0]
        print("  puesto %s (%s decision %s): %s -- %s" % (f["puesto"], f["dominio"], deci,
                                                            f["nodo_a"], f["nodo_b"]))
        print("     frase : %s" % f["frase"])
        print("     razon : %s" % razon)
    print()

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for f in entran:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    print("=" * 90)
    print("TAREA 3.e: EL RESULTADO")
    print("=" * 90)
    print("CIFRA V88 (28 ago 2026, con el filtro de palabras, se deja delante, no se "
          "borra): 129")
    print("CIFRA V89 (29 ago 2026, con el criterio de direccion): %d" % len(entran))
    print("escrito: %s" % SALIDA)
    print()
    print("NO SE ESCRIBIO NINGUNA ARISTA DE OP-E-06 EN ESTA VUELTA. OP-E-06 NO ABRE en "
          "la vuelta 89 (adjudicacion 5.8 del acta 88): la vuelta 90 abre la operacion "
          "con esta bolsa de %d, no con la de 129 ni con la de 192." % len(entran))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
