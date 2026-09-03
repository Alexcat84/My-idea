# -*- coding: utf-8 -*-
"""vuelta159_tarea3_lote2.py . TAREA 3 DE LA VUELTA 159, EL LOTE 2 DEL SACO.

LAS 53 LECTURAS DIRIGIDAS QUE SIGUEN EN C Y QUE NADIE HA LEIDO (adjudicacion
6.12 del acta 158), de `LD-OPC05-068` a `LD-OPC05-121`, leidas una a una CONTRA
LOS NODOS con el dossier `docs/loop/SALIDA_V159_T3_DOSSIER.txt`. La nomina la
sella `vuelta159_tarea3_nomina_lote2.py` en `docs/loop/NOMINA_V159_LOTE2.json`
y este instrumento la exige.

EL LOTE 2 CABE ENTERO CON SUS GUARDAS COMPLETAS Y POR ESO NO SE PARTE. El
encargo autoriza partirlo diciendolo; no hizo falta.

LA VARA ES LA 6.4 DEL ACTA 157 CON LA 6.3 DEL ACTA 158 PUESTA DESDE LA PRIMERA
LECTURA: la pregunta es un EXISTENCIAL, asi que CADA UNA de las 53 razones
NOMBRA EL PAR MAS FUERTE QUE SE DESCARTO y dice por que no sostiene la figura.

UN CRITERIO QUE ESTE LOTE OBLIGO A ESCRIBIR, Y SE DECLARA PARA QUE SE PUEDA
AUDITAR SU CONSISTENCIA: UNA INSTANCIA NO ES EL PROCEDIMIENTO DE SU CATEGORIA.
Cuando la linea de un nodo dice "aplica tecnicas graficas", "mapea tus fuentes
de ingresos" o "consolida los planes subsidiarios", y el otro nodo ES UNA de
esas tecnicas, uno de esos patrones o uno de esos planes, ESO NO ES EXPANSION:
es un ejemplar de la categoria. Se aplico igual en `LD-OPC05-060`, `078`, `099`,
`103`, `106`, `107`, `113` y `117`, y en ninguna se hizo la excepcion comoda.

QUE SALIO: CATORCE SOSTIENEN LA C Y TREINTA Y NUEVE BAJAN A D. Cinco van
MARCADAS COMO DISCUTIBLES.

LAS GUARDAS SON LAS DE LA 2.d Y VIVEN EN `vuelta159_motor_veredictos.py`.

USO:  python scripts/loop/vuelta159_tarea3_lote2.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

RAIZ = motor.RAIZ
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V159_LOTE2.json")

MARCA = "LOTE 2 DE LA VUELTA 159"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR "
                "NADA DE LO ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
            "CLASE SE QUEDA EN %s. LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. "
            % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 159, LOTE 2): la clase pasa de "
                "~~%s~~ a %s. %s." % (vieja, nueva, motivo[:260]))
    return ("LECTURA DEL LOTE 2 (vuelta 159): la C SE SOSTIENE y sus dos lineas "
            "distintas quedan nombradas en la razon del registro de citas, con "
            "la comprobacion existencial de la 6.3 hecha.")


V = {
"LD-OPC05-068": ("C",
 "LINEA 1, en eliminar_metas_numericas_gerencia, paso 3: DETERMINAR LA "
 "CAPACIDAD REAL DEL SISTEMA MEDIANTE ANALISIS ESTADISTICO antes de fijar "
 "cualquier meta; la expanden los pasos 1 a 4 de sistema_estable_causas_comunes "
 "(recolectar datos diarios de defectos durante varias semanas, graficarlos en "
 "carta de corrida o de control, clasificar la variacion en causa comun o "
 "especial, y si el sistema es estable identificar que cambios estructurales "
 "mueven su capacidad). LINEA 2, en sistema_estable_causas_comunes, paso 5: "
 "EVITAR FIJAR METAS NUMERICAS o culpar a quien te ayuda hasta haber "
 "intervenido sobre el sistema; la expanden los pasos 1, 2 y 4 de eliminar_"
 "metas (revisar las metas actuales y verificar si tienen plan de accion "
 "concreto, eliminar las que solo se basan en deseo o presion sin metodo, "
 "reemplazarlas por objetivos de mejora continua con planes especificos). DOS "
 "LINEAS DISTINTAS, UNA MIDE LA CAPACIDAD Y LA OTRA GOBIERNA LAS METAS, Y "
 "NINGUNO ES LA MADRE"),

"LD-OPC05-069": ("D",
 "UNA SOLA DIRECCION. El paso 4 del ESOP (planea como vas a repartir esa "
 "reserva segun a quien piensas contratar) lo rozan los pasos 8 y 9 del vesting "
 "(decide si cada rol consolida por tiempo o tambien por desempeno, deja por "
 "escrito las condiciones de cada persona). PAR MAS FUERTE DESCARTADO EN LA "
 "OTRA DIRECCION: el paso 3 del vesting (cronograma estandar con cliff de 1 ano "
 "al 25% y el resto mensual en 3 anos) contra los pasos 1 y 2 del ESOP "
 "(negociar el tamano de la reserva como porcentaje de la tabla de capital, "
 "definir si incluye opciones ya entregadas): dimensionar EL DEPOSITO no es el "
 "como se fija UN CALENDARIO de consolidacion. UNA SOLA DIRECCION ES MADRE E "
 "HIJO Y EL PAR CONTINUA"),

"LD-OPC05-070": ("D",
 "MATERIAS DISTINTAS: encuadrar la pregunta de diseno contra el triple criterio "
 "de deseabilidad, viabilidad y factibilidad en emprendimiento social. PAR MAS "
 "FUERTE DESCARTADO: el paso 6 del encuadre (validar el brief con conocimiento "
 "local de ONGs o actores en terreno antes de prototipar) contra el paso 2 de "
 "integracion (formar equipos interdisciplinarios que incluyan expertos "
 "tecnicos y del sector). SE DESCARTA: los dos traen saber externo, pero FORMAR "
 "UN EQUIPO no es el como se VALIDA UN BRIEF con conocimiento local. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-071": ("D",
 "UNA SOLA DIRECCION. El paso 4 del encuadre (documentar contexto y "
 "restricciones geograficas, tecnologicas, de tiempo y poblacionales) SI lo "
 "expanden los pasos 1 y 2 de usuarios_extremos (investigacion de campo en "
 "comunidades con restricciones extremas de recursos, infraestructura o acceso; "
 "documentar las limitaciones tecnologicas, linguisticas y economicas reales de "
 "la poblacion). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 1 de "
 "usuarios_extremos (realizar investigacion de campo) contra el paso 6 del "
 "encuadre (validar el brief con conocimiento local de ONGs): validar un brief "
 "es un paso suelto y al mismo nivel, no el procedimiento del trabajo de campo. "
 "UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-072": ("D",
 "MATERIAS DISTINTAS: el nivel de involucramiento en la exportacion contra los "
 "programas de financiamiento del Ex-Im Bank. PAR MAS FUERTE DESCARTADO: el "
 "paso 4 de enfoques_generales (documentar el enfoque o combinacion de enfoques "
 "elegidos) contra el paso 6 de ex_im (consultar la oficina local del U.S. "
 "Commercial Service o exim.gov el proceso de solicitud y los bancos "
 "participantes): los dos nombran el mismo aparato exportador, pero uno "
 "DOCUMENTA UNA DECISION y el otro TRAMITA UN FINANCIAMIENTO. NINGUN OTRO PAR "
 "SOSTIENE LA FIGURA"),

"LD-OPC05-073": ("D",
 "MATERIAS DISTINTAS: capacitar al supervisor en el programa ZD contra la "
 "identificacion del empleado con su trabajo. PAR MAS FUERTE DESCARTADO: el "
 "paso 6 de identificacion (aplicar una autoevaluacion periodica del supervisor "
 "sobre su relacion con el equipo) contra el paso 4 de entrenamiento (hacer un "
 "test de comprension sobre el concepto ZD antes de replicarlo): los dos evaluan "
 "al supervisor, pero uno sobre SU RELACION CON EL EQUIPO y el otro sobre SU "
 "COMPRENSION DEL CONCEPTO; objetos distintos. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-074": ("D",
 "LAS DOS DIRECCIONES COLAPSAN EN UNA LINEA. PAR MAS FUERTE DESCARTADO: el paso "
 "4 de estilos_de_negociacion (favorecer la transparencia y calma en "
 "negociaciones con valor reputacional a largo plazo) contra el paso 2 de "
 "teoria_de_juegos (si es multi ronda, priorizar la reputacion y evitar tacticas "
 "que generen represalias futuras): es LA MISMA LINEA dicha dos veces, y el "
 "9.22 la excluye. Y el resto no cierra: uno clasifica POR ARQUETIPO DE PERSONA "
 "y el otro POR TIPO DE JUEGO, dos variables distintas. NINGUN OTRO PAR "
 "SOSTIENE LA FIGURA"),

"LD-OPC05-075": ("D",
 "OBJETOS DISTINTOS. PAR MAS FUERTE DESCARTADO: el paso 1 de captura_mercado "
 "(identifica senales tempranas de que un mercado entra en fase de crecimiento "
 "fuerte) contra los pasos 1 a 4 de market_type (determina el tipo de mercado, "
 "estima cuota si es existente, busca proxies si es nuevo, evalua tamano y tasa "
 "de adopcion si es re segmentado): market_type CLASIFICA EL MERCADO Y PROYECTA "
 "INGRESOS, y clasificar un tipo no es el como se DETECTA LA SENAL de una fase "
 "de crecimiento. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-076": ("D",
 "DOS ETAPAS DISTINTAS DEL EMBUDO: uno es GROW sobre la base actual (venta "
 "cruzada, referidos, motores de recomendacion) y el otro es GET sobre "
 "desconocidos. PAR MAS FUERTE DESCARTADO: el paso 6 de estrategia_crecimiento "
 "(revisar tacticas especificas de canales web o moviles para identificar ideas "
 "adicionales) contra los seis pasos del embudo: eso es UNA REMISION al otro "
 "nodo, y remitir no es expandir, que es lo que la 6.4 excluye con todas sus "
 "letras. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-077": ("D",
 "DOS CANALES DE TRACCION PARALELOS. PAR MAS FUERTE DESCARTADO: el paso 6 de "
 "plataformas (lanzar la integracion y medir el trafico y referidos generados) "
 "contra el paso 5 de afiliados (medir conversion, calidad de leads y ajustar "
 "comisiones o segmentar por desempeno): los dos MIDEN, pero cada uno mide SU "
 "PROPIO canal, y una medicion paralela no es la expansion de la otra. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-078": ("D",
 "DISCUTIBLE, Y LO MARCO YO, PORQUE LA DECIDE UN CRITERIO Y NO UNA EVIDENCIA. "
 "UNA DIRECCION SE SOSTIENE: el paso 7 de estratificacion (planificar "
 "confirmacion adicional de los hallazgos) lo expanden los trece pasos de "
 "planificacion_recoleccion_datos. PAR MAS FUERTE DESCARTADO EN LA OTRA "
 "DIRECCION: el paso 8 de planificacion (aplicar tecnicas graficas y "
 "estadisticas al problema original) contra los siete pasos de estratificacion. "
 "SE DESCARTA POR EL CRITERIO DE INSTANCIA: la estratificacion es UNA de las "
 "tecnicas graficas y estadisticas, un ejemplar de la categoria que la linea "
 "nombra, y un ejemplar no es el procedimiento de su categoria. El mismo "
 "criterio se aplico a la 060, la 099, la 103, la 106, la 107, la 113 y la 117. "
 "UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-079": ("D",
 "PAR MAS FUERTE DESCARTADO, Y COLAPSA: el paso 2 de mix_ubicaciones (analiza "
 "tu capital disponible y tu plan de salida para orientar la eleccion de "
 "estrategia) contra el paso 2 de evaluacion_necesidad_franquiciar (evalua si "
 "tu capital y capacidad de gestion actuales bastan para alcanzar tus metas): "
 "las dos EVALUAN EL CAPITAL DISPONIBLE al mismo nivel, la misma linea. Y en la "
 "otra direccion, el paso 6 de evaluacion (comparar ventajas y desventajas de "
 "franquiciar antes de decidir) no lo expande el mix, que ya presupone la "
 "decision tomada. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-080": ("D",
 "UNA SOLA DIRECCION, Y DEBIL. El paso 4 de vulnerabilidad_instalacion (analizar "
 "historicos de fallas de mantenimiento para confirmar predominancia de errores "
 "de instalacion) lo rozan los pasos 1 a 4 de fallas_activas. PAR MAS FUERTE "
 "DESCARTADO EN LA OTRA DIRECCION: el paso 5 de fallas_activas (priorizar la "
 "correccion de condiciones latentes por su impacto en futuros eventos) contra "
 "los pasos 1 a 3 de vulnerabilidad (procedimientos de reinstalacion numerados, "
 "checklists obligatorias con firma paso a paso, doble verificacion e "
 "inspeccion independiente): eso es EL REMEDIO DE UNA condicion latente "
 "concreta, no el como se PRIORIZAN todas. UNA SOLA DIRECCION ES MADRE E HIJO Y "
 "EL PAR CONTINUA"),

"LD-OPC05-081": ("C",
 "DISCUTIBLE, Y LO MARCO YO, PORQUE LOS DOS NODOS SON DEL MISMO LIBRO Y CORREN "
 "MUY EN PARALELO. LINEA 1, en fase_accomplish_experiencia_cliente, paso 3: "
 "CLASIFICAR CADA RELACION CON CLIENTE en uno de los tres escenarios, Mission "
 "Accomplished, Lukewarm Bath o Mission Failure; la expanden los pasos 1, 7, 8 "
 "y 9 de reunion_conclusion_proyecto (programar la reunion revisando los "
 "objetivos y metricas definidos en el kickoff, revisarlos uno a uno, hacer una "
 "evaluacion honesta del nivel de exito en cada metrica, solicitar el feedback "
 "del cliente sobre esas metricas), que es literalmente como se decide en cual "
 "de los tres cae. LINEA 2, en reunion_conclusion_proyecto, paso 5: ESTABLECER "
 "UN PERIODO DE MONITOREO POSTERIOR, por ejemplo tres meses, para mitigar el "
 "remordimiento post lanzamiento; la expanden los pasos 8, 9 y 10 de accomplish "
 "(disenar un punto de seguimiento posterior al logro del objetivo aparente, "
 "mantener contacto y apoyo mas alla del cumplimiento nominal del contrato, "
 "evitar que el equipo desacelere justo cuando el cliente cree haber "
 "terminado). DOS LINEAS DISTINTAS, UNA CLASIFICA EL RESULTADO Y LA OTRA "
 "SOSTIENE EL DESPUES, Y NINGUNO ES LA MADRE"),

"LD-OPC05-082": ("D",
 "SER INSUMO NO ES SER EXPANSION. PAR MAS FUERTE DESCARTADO: el paso 1 de "
 "iota_analysis (reunir todos los hallazgos de los ejercicios estrategicos "
 "previos en una tabla resumen) contra los seis pasos de future_scenarios: los "
 "escenarios son UNO de esos ejercicios previos, o sea el INSUMO de esa linea, "
 "y consumir una salida no expande la linea que la consume. En la otra "
 "direccion, el paso 6 de scenarios (identificar senales y marcadores tempranos) "
 "no lo expande el IOTA, que asigna timing y probabilidad a lo ya listado. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-083": ("D",
 "DIAGNOSTICO CONTRA SISTEMA, Y LA VUELTA NO CIERRA. PAR MAS FUERTE DESCARTADO: "
 "el paso 4 de gates_sin_dientes (evalua si tus filtros funcionan como "
 "verdaderas decisiones de inversion o solo como reuniones de seguimiento) "
 "contra los pasos 4, 5 y 7 de sistema_gates (toma una decision explicita Go, "
 "Kill, Hold o Recycle; comprometete recursos solo despues de pasar el gate; "
 "preguntate de verdad si sigues o si paras): sistema_gates DEFINE EL ESTANDAR "
 "contra el que se diagnostica, y definir el estandar no es el como se hace el "
 "diagnostico, que lo dan los pasos 1 a 3 del propio nodo diagnostico (la curva "
 "de supervivencia y las siete razones para no matar). NINGUN OTRO PAR SOSTIENE "
 "LA FIGURA"),

"LD-OPC05-084": ("C",
 "DISCUTIBLE, Y LO MARCO YO, PORQUE LA SEGUNDA DIRECCION ES UN METODO DE "
 "VALIDACION Y NO UN DISENO DE EXPERIMENTOS EN SENTIDO ESTRICTO. LINEA 1, en "
 "genchi_gembutsu_salir_del_edificio, paso 1: IDENTIFICAR LAS PREGUNTAS DE FE "
 "mas criticas del negocio; la expanden los pasos 1 a 4 de leap_of_faith_"
 "assumptions (revisa tu plan y separa los hechos comprobados de las "
 "suposiciones, identifica cuales son de bajo riesgo y cuales son verdaderos "
 "saltos de fe, reescribe tus comparaciones en terminos concretos y "
 "verificables, ordena tus supuestos segun el riesgo). LINEA 2, en "
 "leap_of_faith_assumptions, paso 5: DISENAR EXPERIMENTOS ESPECIFICOS PARA "
 "VALIDAR cada leap of faith question antes de construir el producto completo; "
 "la expanden los pasos 2 a 6 de genchi (salir fisicamente a hablar con "
 "clientes potenciales reales y no solo encuestas remotas, observar el "
 "comportamiento real en su contexto natural, evitar reportes de segunda mano, "
 "documentar los hallazgos firsthand para contrastarlos con las hipotesis, usar "
 "las observaciones para ajustar el producto). DOS LINEAS DISTINTAS, UNA ORDENA "
 "LOS SUPUESTOS Y LA OTRA LOS PONE A PRUEBA, Y NINGUNO ES LA MADRE"),

"LD-OPC05-085": ("D",
 "UNA SOLA DIRECCION. El paso 3 de gestion_alucinaciones (usar la IA para "
 "generar borradores o hipotesis, nunca como fuente final de verdad) SI lo "
 "expanden los cinco pasos de ia_generacion_ideas (invitar a la IA al "
 "brainstorming, pedirle combinar dos o tres conceptos distantes, solicitar "
 "listas de mas de veinte ideas, asignarle un rol experto en el prompt, repetir "
 "con distintos contextos). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el "
 "paso 3 de ia_generacion (filtrar humanamente las de mayor potencial) contra "
 "los pasos 4 y 5 de alucinaciones (entrenar al equipo en detectar el patron de "
 "sonar creible, repetir la misma pregunta de distintas formas): son DOS "
 "FILTROS SOBRE OBJETOS DISTINTOS, uno filtra por POTENCIAL DE LA IDEA y el "
 "otro por VERACIDAD DEL DATO. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
 "CONTINUA"),

"LD-OPC05-086": ("D",
 "OBJETOS DISTINTOS. PAR MAS FUERTE DESCARTADO: el paso 3 de gestion_"
 "instalaciones (asignar proveedores y mercados a cada instalacion considerando "
 "costos de transporte) contra los seis pasos de planificacion_cadena_suministro "
 "(documentar la actividad de compras, identificar commodities de alto gasto y "
 "criticidad, equipo cross funcional, analizar la industria proveedora, "
 "calcular el costo total de propiedad, obtener respaldo de la direccion): el "
 "sourcing SELECCIONA PROVEEDORES POR COMMODITY, y seleccionar no es el como se "
 "ASIGNAN proveedores y mercados A UNA INSTALACION por costo de transporte. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-087": ("C",
 "LINEA 1, en gestion_portafolio_dos_niveles, paso 1: ESTABLECER UN PROCESO DE "
 "GATING para revisar cada proyecto individualmente; lo expanden los diecisiete "
 "pasos de sistema_gates_go_kill (definir los gates en los puntos clave, "
 "establecer criterios visibles, checklist o scorecard, decision explicita Go, "
 "Kill, Hold, Recycle o Conditional Go, comprometer recursos solo despues, "
 "anotar la decision y el motivo, criterios eliminatorios, entregables "
 "estandar). LINEA 2, en sistema_gates_go_kill, paso 10: CONECTA CADA PUNTO DE "
 "DECISION CON LA FORMA EN QUE ASIGNAS RECURSOS Y CON LA VISION GENERAL DE TUS "
 "PROYECTOS; la expanden los pasos 2, 3 y 4 de dos_niveles (establecer "
 "revisiones de portafolio trimestrales o semestrales que vean el conjunto "
 "completo, definir que decisiones son estrategicas y cuales tacticas, usar "
 "ambos procesos de forma complementaria y no sustitutiva). DOS LINEAS "
 "DISTINTAS, UNA INSTALA EL GATE INDIVIDUAL Y LA OTRA LO ATA AL CONJUNTO, Y "
 "NINGUNO ES LA MADRE. Ademas la ficha de OP-E-04 ya declara este par como "
 "MUTUO EXCEPTUADO del 9.22 en su verificacion 5, y esa declaracion sellada es "
 "contraste, no fuente: lo que se publica aqui es la lectura contra los nodos"),

"LD-OPC05-088": ("C",
 "LINEA 1, en gestion_portafolio_foco, paso 2: APLICAR CRITERIOS ESTRICTOS DE "
 "GO Y KILL para reducir el numero de proyectos en pipeline; los expanden los "
 "pasos 3, 4, 12, 15 y 16 de sistema_gates_go_kill (checklist o scorecard, "
 "decision explicita, lista de criterios eliminatorios, entregables estandar "
 "por gate, criterios must meet y go kill financieros y should meet "
 "cualitativos). LINEA 2, en sistema_gates_go_kill, paso 10: CONECTA CADA PUNTO "
 "DE DECISION CON LA FORMA EN QUE ASIGNAS RECURSOS Y CON LA VISION GENERAL; la "
 "expanden los pasos 1, 3 y 5 de foco (auditar el numero de proyectos activos "
 "contra la capacidad real de recursos, priorizar por potencial estrategico y "
 "financiero, revisar periodicamente el balance del portafolio por riesgo, tipo "
 "de innovacion y mercados). DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE. La "
 "ficha de OP-E-04 lo declara exceptuado en su verificacion 5, y eso es "
 "contraste y no fuente"),

"LD-OPC05-089": ("D",
 "PAR MAS FUERTE DESCARTADO, Y COLAPSA: el paso 5 de reglas_brainstorming (usar "
 "Post-it notes o pizarra para capturar y mover las ideas visualmente) contra "
 "el paso 1 de get_visual (mantener post-its, papel y lapices siempre a mano "
 "durante todo el proceso): es LA MISMA LINEA en los dos nodos, y el 9.22 la "
 "excluye. Queda una sola direccion real, get_visual como el como del ser "
 "visual del brainstorming, y en la vuelta el paso 3 de get_visual (explicar "
 "los dibujos al equipo) no lo expande ninguna de las ocho reglas. NINGUN OTRO "
 "PAR SOSTIENE LA FIGURA"),

"LD-OPC05-090": ("D",
 "ANCLAS DISTINTAS: uno prueba EN UN MODELO y el otro mide UN PILOTO REAL. PAR "
 "MAS FUERTE DESCARTADO: el paso 5 de ia_en_supply_chain (medir la mejora en "
 "precision de pronostico o eficiencia operativa antes de escalar a otra area) "
 "contra los pasos 5 y 6 de simulacion (comparar resultados de escenarios para "
 "seleccionar el diseno con mejor relacion costo servicio, validar la solucion "
 "ANTES de implementarla fisicamente): la simulacion valida en el modelo y la "
 "linea de IA mide en la realidad; metodos distintos sobre objetos distintos. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-091": ("D",
 "DOS RIESGOS DISTINTOS DE LA MISMA OPERACION. PAR MAS FUERTE DESCARTADO: el "
 "paso 2 de seleccion_de_metodo_de_pago (definir cuanto riesgo estas dispuesto "
 "a asumir segun la relacion con el comprador y el pais) contra el paso 2 de "
 "incoterms (seleccionar el Incoterm adecuado segun el nivel de responsabilidad "
 "que quieres asumir): los dos deciden CUANTO RIESGO TOMAS, pero uno es RIESGO "
 "DE COBRO y el otro RIESGO DE ENTREGA Y COSTO, y ninguno procedimenta al otro. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA. El auditor leyo este par a ciegas en la "
 "vuelta 157 y tambien dio D"),

"LD-OPC05-092": ("D",
 "DOS JUEGOS PARALELOS CON DOS SALIDAS DISTINTAS: uno saca dolores priorizados "
 "por profundidad del ancla y el otro saca mensajes de marketing y beneficios. "
 "PAR MAS FUERTE DESCARTADO: el paso 4 de speedboat (compara los resultados con "
 "tu entendimiento previo de los pains del cliente) contra el paso 4 de "
 "product_box (observa y anota que mensajes y beneficios destacan durante el "
 "pitch): los dos CIERRAN SU PROPIO JUEGO leyendo su propia salida, y una "
 "lectura paralela no es la expansion de la otra. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-093": ("D",
 "UNA SOLA DIRECCION. El paso 3 de international_partner_search (recibe y "
 "EVALUA la lista de hasta 5 socios potenciales prescreened) SI lo expanden los "
 "nueve puntos del checklist de seleccion_representante (tamano y capacidad de "
 "expansion de la fuerza de ventas, historial de ventas de los ultimos 5 anos, "
 "territorio cubierto, compatibilidad de lineas y conflictos de interes, "
 "instalaciones y servicio tecnico, politicas de compensacion y capacitacion, "
 "perfil de clientes, cuantos principales representa, enfoque promocional). PAR "
 "MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 2 del checklist (revisar "
 "el historial de ventas de los ultimos 5 anos) contra el paso 5 de "
 "partner_search (pide un informe ICP para verificar la reputacion y las "
 "referencias financieras del socio): el ICP verifica REPUTACION Y FINANZAS, no "
 "HISTORIAL DE VENTAS; objeto distinto. UNA SOLA DIRECCION ES MADRE E HIJO Y EL "
 "PAR CONTINUA"),

"LD-OPC05-094": ("C",
 "LINEA 1, en reglas_brainstorming, paso 4: PREPARAR AL EQUIPO CON UNA "
 "EXPERIENCIA DE INMERSION PREVIA, visita de campo o entrevistas a clientes; la "
 "expanden los nueve pasos de investigacion_etnografica (seleccionar un contexto "
 "de uso real, observar a los usuarios usando o mal usando el producto durante "
 "un periodo extendido, documentar problemas y comportamientos no verbalizados, "
 "capacitar al observador en escucha e inferencia, reducir el tiempo por visita "
 "con un dia en la vida, formar equipos con etnografos y disenadores, buscar "
 "situaciones analogas, construir confianza con los sujetos). LINEA 2, en "
 "investigacion_etnografica, paso 6: TRADUCIR LOS HALLAZGOS OBSERVACIONALES EN "
 "CONCEPTOS DE PRODUCTO CONCRETOS; la expanden los pasos 2, 3, 5 y 7 de "
 "reglas_brainstorming (definir un enunciado del problema centrado en la "
 "necesidad del cliente, establecer y hacer cumplir las reglas de diferir el "
 "juicio y construir sobre las ideas de otros, capturar en Post-it, generar el "
 "mayor numero de ideas sin filtrar y separar divergencia de convergencia). DOS "
 "LINEAS DISTINTAS, UNA PREPARA LA SESION Y LA OTRA CONVIERTE EL CAMPO EN "
 "CONCEPTO, Y NINGUNO ES LA MADRE"),

"LD-OPC05-095": ("C",
 "LINEA 1, en investigacion_new_view, paso 1: RECONSTRUIR LA SITUACION TAL COMO "
 "LA VIVIERON LOS INVOLUCRADOS, sin usar el conocimiento del resultado final y "
 "a partir de las senales disponibles en el momento; la expanden los pasos 2, 3 "
 "y 4 de process_tracing (construir el relato especifico del dominio en el "
 "lenguaje tecnico de los practicantes, identificar y aplicar conceptos "
 "dependientes como sorpresa de automatizacion o carga de trabajo, buscar "
 "regularidades a traves de los dos relatos paralelos). LINEA 2, en "
 "process_tracing, paso 1: RECOLECTAR DATOS CRUDOS DEL EPISODIO, registros, "
 "transcripciones, testimonios y datos de sistemas; la expanden los pasos 5, 6 "
 "y 7 de new_view (contrastar la investigacion oficial con relatos revisionistas "
 "o independientes, involucrar perspectivas de colegas, familiares o testigos "
 "cercanos, entrevistar a los involucrados para entender su percepcion y "
 "objetivos en el momento). DOS LINEAS DISTINTAS, UNA RECONSTRUYE Y LA OTRA "
 "REUNE EL MATERIAL, Y NINGUNO ES LA MADRE"),

"LD-OPC05-096": ("D",
 "PAR MAS FUERTE DESCARTADO, Y COLAPSA: el paso 4 de proteccion_propiedad_"
 "intelectual (incluir clausulas de proteccion de IP en todo contrato de "
 "licenciamiento o joint venture) contra el paso 3 de joint_ventures (negociar "
 "terminos de control gerencial y proteccion de propiedad intelectual): es LA "
 "MISMA LINEA escrita en los dos nodos, y el 9.22 la excluye. Queda una sola "
 "direccion, la proteccion de IP como el como de la mitad de propiedad "
 "intelectual de esa linea, y en la vuelta ni el paso 1 de joint_ventures "
 "(requisitos legales sobre participacion extranjera) ni el 5 (resolucion de "
 "conflictos y salida) los expande el otro nodo. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-098": ("C",
 "LINEA 1, en lean_launchpad_web_startup_process, paso 2: REDACTAR LAS "
 "HIPOTESIS DEL MODELO DE NEGOCIO DE 9 BLOQUES; las expanden los doce pasos del "
 "lienzo (imprimirlo en grande, reunirse aceptando que habra vacios, escribir "
 "cada bloque en post-its, identificar segmentos, definir propuesta de valor "
 "por segmento, mapear canales, relaciones e ingresos, mapear recursos, "
 "actividades y asociaciones, calcular costos y profit, iterar hasta la "
 "coherencia). LINEA 2, en lienzo_modelo_negocio, paso 12: USAR EL LIENZO COMO "
 "BASE PARA PIVOTAR O VALIDAR HIPOTESIS DEL NEGOCIO; la expanden los pasos 5, "
 "6, 8, 9 y 10 del launchpad (construir un sitio de baja fidelidad con splash "
 "page y formularios de pre orden, dirigir trafico para probar segmento y "
 "propuesta de valor, probar el problema del cliente con analytics y encuestas, "
 "construir una version de alta fidelidad para probar la solucion, pedir dinero "
 "con pre orden o cobro real). DOS LINEAS DISTINTAS, UNA ESCRIBE LAS HIPOTESIS "
 "Y LA OTRA LAS PONE A PRUEBA CON TRAFICO Y DINERO, Y NINGUNO ES LA MADRE"),

"LD-OPC05-099": ("D",
 "CRITERIO DE INSTANCIA. PAR MAS FUERTE DESCARTADO: el paso 6 del lienzo "
 "(mapear canales, relaciones y FUENTES DE INGRESOS) contra los cinco pasos de "
 "patron_free (determinar que segmento recibe la oferta gratuita, identificar "
 "quien la financia, elegir entre publicidad, freemium o bait and hook, "
 "calcular el costo marginal de servir a los gratuitos, disenar el subsidio "
 "cruzado): FREE es UN PATRON de ingresos entre muchos, un ejemplar de la "
 "categoria que la linea nombra, y un ejemplar no es el procedimiento de su "
 "categoria, igual que en la 060, la 078 y la 103. En la otra direccion, el "
 "paso 5 de patron_free (disenar mecanismos de conversion o subsidio cruzado) "
 "no lo expande ningun paso del lienzo. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-100": ("C",
 "LINEA 1, en lienzo_modelo_negocio, paso 9: PAUSAR PARA INVESTIGAR MAS "
 "INFORMACION DONDE HAYA VACIOS IMPORTANTES; la expande el paso 2 de "
 "proceso_ideacion (realizar una fase de inmersion investigando clientes, "
 "tecnologias y modelos de negocio existentes), que es exactamente el como se "
 "llena ese vacio, junto con el paso 1 (ensamblar un equipo diverso en "
 "antiguedad, experiencia, area funcional y conocimiento del cliente). LINEA 2, "
 "en proceso_ideacion, paso 5: REDUCIR A ENTRE TRES Y CINCO IDEAS Y "
 "PROTOTIPARLAS USANDO EL LIENZO; la expanden los doce pasos del lienzo, que "
 "son el procedimiento entero de construir cada prototipo. DOS LINEAS "
 "DISTINTAS, UNA MANDA A INVESTIGAR Y LA OTRA MANDA A PROTOTIPAR, Y NINGUNO ES "
 "LA MADRE"),

"LD-OPC05-101": ("C",
 "LINEA 1, en search_for_business_model, paso 2: LISTA EXPLICITAMENTE LAS "
 "HIPOTESIS DE TU MODELO DE NEGOCIO, mercado, cliente, producto, canal y "
 "precio, marcadas como no probadas; las expanden los pasos 3 a 8 del lienzo "
 "(escribir cada bloque en post-its, identificar segmentos, definir propuesta "
 "de valor, mapear canales, relaciones e ingresos, mapear recursos, actividades "
 "y asociaciones, calcular estructura de costos y profit). LINEA 2, en "
 "lienzo_modelo_negocio, paso 12: USAR EL LIENZO COMO BASE PARA PIVOTAR O "
 "VALIDAR HIPOTESIS; la expanden los pasos 3, 4 y 5 de search (aplicar el "
 "proceso de Customer Development para salir a probar cada hipotesis con "
 "clientes reales, evitar montar estructuras de ejecucion antes de validar, "
 "iterar y pivotar segun la evidencia hasta encontrar un modelo repetible y "
 "escalable). DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE"),

"LD-OPC05-102": ("D",
 "UNA SOLA DIRECCION. El paso 4 del lienzo (identificar los segmentos de "
 "clientes a los que se dirige la organizacion) SI lo expanden los seis pasos "
 "de segmentos_de_clientes (sal del edificio a observar como viven el problema, "
 "clasifica el problema en la escala latente, pasivo, activo o con solucion "
 "casera, identifica si eres must have o nice to have, mapea quien usa, quien "
 "influye y quien recomienda, documenta un dia en la vida, revisa si el mercado "
 "es de uno o de varios lados). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: "
 "el paso 6 de segmentos (revisar si tu mercado es de un solo lado o de varios) "
 "contra los pasos 4 y 5 del lienzo (identificar segmentos, definir la "
 "propuesta de valor para cada uno): el lienzo dice QUE hacer al mismo nivel de "
 "generalidad, no COMO se determina si el mercado es multi lado. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-103": ("D",
 "DISCUTIBLE, Y LO MARCO YO, PORQUE OTRA VEZ LA DECIDE EL CRITERIO DE INSTANCIA "
 "Y NO UNA EVIDENCIA. PAR MAS FUERTE DESCARTADO: el paso 4 de mapeo_flujo_valor "
 "(disena y documenta el mapa del estado futuro con las mejoras que quieres "
 "lograr) contra los pasos 4, 5 y 6 de takt_time (ajustar la dotacion y "
 "balancear las estaciones segun el takt, reducir tiempos de cambio para "
 "permitir lotes mas pequenos, separar lineas de valor si la demanda varia): el "
 "balanceo por takt es UNA FAMILIA DE MEJORAS entre varias, un ejemplar de la "
 "categoria, y un ejemplar no es el procedimiento de disenar el estado futuro. "
 "SEGUNDO PAR DESCARTADO: el paso 3 de takt (comparar el takt con tu capacidad "
 "demostrada y teorica) contra el paso 2 de mapeo (documentar tiempos de ciclo, "
 "esperas, inventarios, downtime y capacidad): el mapeo PRODUCE el dato de "
 "capacidad, y ser insumo no es expandir. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-104": ("D",
 "CONSUMIR UNA SALIDA NO ES EXPANDIR UNA LINEA. UNA DIRECCION SE SOSTIENE: el "
 "paso 2 de metrics_that_matter (calcula las unidades vendidas por periodo y el "
 "precio de venta promedio validado con clientes) lo expanden los pasos 2 a 4 "
 "de market_type (estimar la cuota capturable si el mercado es existente, "
 "buscar proxies y comparables si es nuevo, evaluar tamano del segmento y tasa "
 "de adopcion si es re segmentado). PAR MAS FUERTE DESCARTADO EN LA OTRA "
 "DIRECCION: el paso 6 de market_type (ajusta tus proyecciones de ingresos "
 "segun el tipo de mercado y documenta tus supuestos) contra los seis pasos de "
 "metrics: metrics CONSUME la proyeccion para calcular descuentos, costos de "
 "canal, burn rate y efectivo restante, o sea que va AGUAS ABAJO. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-105": ("D",
 "UNA SOLA DIRECCION, Y LA VUELTA ES CIRCULAR. El paso 2 del NPV (definir la "
 "tasa de descuento o hurdle rate de la empresa) SI lo expanden los cuatro "
 "pasos de tasa_de_retorno_requerida (calcular el costo de capital ponderado de "
 "deuda y capital propio, evaluar el costo de oportunidad de otras "
 "alternativas, establecer una tasa minima superior al costo de capital, "
 "ajustarla segun el riesgo del proyecto). PAR MAS FUERTE DESCARTADO EN LA OTRA "
 "DIRECCION: el paso 2 de tasa (evaluar el costo de oportunidad de otras "
 "alternativas de inversion) contra los pasos 1 a 5 del NPV (proyectar flujos, "
 "descontar, sumar, elegir el de mayor NPV positivo): el NPV NECESITA la tasa "
 "que esa linea produce, asi que consume su salida y no la expande, el mismo "
 "criterio de la 003, la 037 y la 104. UNA SOLA DIRECCION ES MADRE E HIJO Y EL "
 "PAR CONTINUA"),

"LD-OPC05-106": ("D",
 "LAS DOS DIRECCIONES FALLAN, CADA UNA POR SU MOTIVO. PAR MAS FUERTE "
 "DESCARTADO, Y COLAPSA: el paso 4 de motor_de_crecimiento (enfocar todos los "
 "experimentos de crecimiento en el motor elegido, evitando dispersion) contra "
 "el paso 4 de motor_crecimiento_viral (enfocar todo el desarrollo de producto "
 "en aumentar el coeficiente viral): es LA MISMA LINEA, una en general y otra "
 "en el caso viral. SEGUNDO PAR DESCARTADO, POR EL CRITERIO DE INSTANCIA: el "
 "paso 3 de motor_de_crecimiento (seleccionar el motor especifico, pegajoso, "
 "viral o pagado) contra los cinco pasos del viral: el viral es UNO de los "
 "motores que esa linea elige, un ejemplar de la categoria. NINGUN OTRO PAR "
 "SOSTIENE LA FIGURA"),

"LD-OPC05-107": ("D",
 "CRITERIO DE INSTANCIA, Y ADEMAS EL NODO NI LA NOMBRA. PAR MAS FUERTE "
 "DESCARTADO: el paso 1 de term_sheet_negociacion (revisar cada seccion del "
 "term sheet, dividendos, liquidacion, conversion, antidilucion, voto y board, "
 "con un abogado) contra los cuatro pasos del no_shop (definir el periodo de "
 "exclusividad, saber que es vinculante desde la firma, obligacion de aviso, "
 "que pasa si no cierras en plazo): el no shop es UNA CLAUSULA del term sheet, "
 "un ejemplar, y la propia enumeracion del paso 1 NI SIQUIERA LA INCLUYE. En la "
 "otra direccion, el paso 1 del no shop (definir el periodo) no lo expande "
 "ningun paso del term sheet. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-108": ("D",
 "CRITERIO DE INSTANCIA. PAR MAS FUERTE DESCARTADO: el paso 4 de "
 "reduccion_tiempo_de_mercado (usar procesamiento paralelo de tareas en lugar "
 "de secuencial) contra el paso 1 del plan de lanzamiento (empieza a armar tu "
 "plan de lanzamiento desde las primeras etapas del proyecto, no lo dejes para "
 "el final): empezar el plan antes es UN EJEMPLAR del procesamiento paralelo, "
 "no su procedimiento. SEGUNDO PAR DESCARTADO: el paso 4 del plan (asegurate de "
 "tener las personas y el presupuesto que el lanzamiento necesita) contra el "
 "paso 6 de velocidad (priorizar y enfocar recursos en menos proyectos pero de "
 "mayor valor): uno dota UN LANZAMIENTO y el otro recorta EL PORTAFOLIO. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-109": ("C",
 "LINEA 1, en plan_gestion_interesados, paso 3: DEFINE QUE NECESITA SABER CADA "
 "PERSONA Y COMO SE LO VAS A COMUNICAR; la expanden los seis pasos del plan de "
 "comunicaciones (lista de personas o grupos que necesitan recibir informacion, "
 "que tipo de informacion para cada uno, metodo de entrega, frecuencia, "
 "responsable de cada envio, restricciones y glosario). LINEA 2, en "
 "plan_gestion_comunicaciones, paso 1: HAZ UNA LISTA DE LAS PERSONAS O GRUPOS "
 "QUE NECESITAN RECIBIR INFORMACION de tu proyecto; la expanden los pasos 1, 2 "
 "y 4 del plan de interesados (anota el nivel de compromiso actual y el deseado "
 "de cada persona, ubica a cada una segun si no lo conoce, se resiste, es "
 "neutral, lo apoya o lo defiende, e identifica como se relacionan entre si los "
 "grupos). DOS LINEAS DISTINTAS, UNA DEFINE EL MENSAJE Y LA OTRA CONSTRUYE Y "
 "CARACTERIZA LA LISTA, Y NINGUNO ES LA MADRE"),

"LD-OPC05-110": ("C",
 "LINEA 1, en portfolio_management, paso 4: TOMAR DECISIONES GO Y KILL "
 "CONTINUAS SOBRE PROYECTOS INDIVIDUALES; las expanden los diecisiete pasos de "
 "sistema_gates_go_kill, que son el procedimiento entero de esa decision. LINEA "
 "2, en sistema_gates_go_kill, paso 10: CONECTA CADA PUNTO DE DECISION CON LA "
 "FORMA EN QUE ASIGNAS RECURSOS Y CON LA VISION GENERAL DE TUS PROYECTOS; la "
 "expanden los pasos 1, 2, 3 y 6 de portfolio_management (evaluar si hay "
 "demasiados proyectos para los recursos disponibles, revisar el balance entre "
 "proyectos pequenos y de alto valor, implementar revisiones periodicas "
 "holisticas, reasignar los recursos liberados a los de mayor valor). DOS "
 "LINEAS DISTINTAS Y NINGUNO ES LA MADRE. La ficha de OP-E-04 lo declara "
 "exceptuado en su verificacion 5, y eso es contraste y no fuente"),

"LD-OPC05-111": ("D",
 "UNA SOLA DIRECCION. El paso 3 de principios_iso9000 (incorporar estos "
 "principios como criterios rectores EN EL DISENO DEL SISTEMA de gestion de "
 "calidad) SI lo expanden los cuatro pasos de sistema_gestion_calidad (mapear "
 "todos los procesos que afectan la calidad mas alla de produccion, identificar "
 "quien controla hoy cada parte, establecer una forma de coordinar entre las "
 "partes, documentar el sistema segun los estandares del mercado). PAR MAS "
 "FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 4 de sistema_gestion "
 "(documenta el sistema siguiendo los estandares que apliquen) contra los pasos "
 "1 y 2 de iso9000 (evaluar el grado de cumplimiento actual de cada uno de los "
 "ocho principios, priorizar los de mayor brecha): la matriz de autoevaluacion "
 "MIDE UNA BRECHA, y medir una brecha no es el como se DOCUMENTA un sistema. "
 "UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-112": ("D",
 "UN CRITERIO NO EXPANDE UNA LINEA. El paso 2 de problem_solution_fit (probar "
 "si la solucion propuesta resuelve el problema de forma convincente) SI lo "
 "expanden los seis pasos del MVP (identifica la hipotesis mas critica y bajala "
 "al problema mas pequeno que un cliente pagaria, disena la version mas simple "
 "que pruebe esa hipotesis, evita funciones extra, lanza a early adopters, mide "
 "la reaccion real y no la opinion, itera o cambia de rumbo). PAR MAS FUERTE "
 "DESCARTADO EN LA OTRA DIRECCION: el paso 1 del MVP contra los pasos 1 y 3 de "
 "problem_solution_fit (validar que el problema sea doloroso para un segmento "
 "amplio, verificar la alineacion entre modelo de ingresos, precio y "
 "necesidades): los cuatro pasos del problem/solution fit son CRITERIOS DE "
 "ACEPTACION escritos como validar, probar, verificar y considerar, no "
 "procedimientos. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-113": ("D",
 "CRITERIO DE INSTANCIA. PAR MAS FUERTE DESCARTADO: el paso 5 del "
 "project_management_plan (consolidar todos los planes subsidiarios y lineas "
 "base en un documento unico) contra los cinco pasos del scope_management_plan: "
 "el plan de alcance es UNO de los planes subsidiarios que esa linea consolida, "
 "un ejemplar y ademas un insumo. SEGUNDO PAR DESCARTADO: el paso 4 del "
 "pm_plan (establecer umbrales de variacion para alcance, cronograma y costo) "
 "contra el paso 4 del scope_plan (diferenciar que constituye un cambio de "
 "alcance frente a una revision menor): esa direccion si es expansion, pero la "
 "vuelta no existe, porque ningun paso del scope_plan esta expandido por el "
 "pm_plan. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-114": ("D",
 "PROPOSITOS DISTINTOS PARA EL MISMO VERBO. PAR MAS FUERTE DESCARTADO: el paso "
 "3 de prototipar_con_medios_no_convencionales (construye una version de tu "
 "idea central usando ese medio no convencional) contra los pasos 2, 3 y 5 de "
 "prototipado_rapido (construir una representacion fisica minima en minutos u "
 "horas, usar el prototipo como herramienta de discusion, iterar rapidamente): "
 "el prototipado rapido procedimenta CONSTRUIR BARATO Y RAPIDO, y la linea pide "
 "construir EN UN MEDIO RADICALMENTE DISTINTO AL HABITUAL para que emerjan "
 "propiedades nuevas; el proposito es otro y por eso no la expande. NINGUN OTRO "
 "PAR SOSTIENE LA FIGURA"),

"LD-OPC05-115": ("D",
 "UNA SOLA DIRECCION, Y LA VUELTA FALLA POR UNA LINEA QUE NO ESTA ESCRITA. El "
 "paso 4 de recomendaciones_smart (validar la recomendacion con los "
 "responsables de implementacion considerando restricciones de produccion y "
 "eficiencia) lo expanden los pasos 2 y 3 de revision_de_aprendizaje (formular "
 "la pregunta clave que necesitan ustedes para mejorar esto, fomentar un "
 "dialogo abierto sobre como las personas se adaptan a conflictos de metas y "
 "restricciones de recursos). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: "
 "el paso 2 de smart (redactar la recomendacion especificando que parte de la "
 "organizacion debe hacer que y cuando) contra los cuatro pasos de revision: la "
 "revision de aprendizaje PROMETE propuestas de mejora en su entregable pero "
 "NINGUNO de sus cuatro pasos es redactarlas, y una linea que no esta escrita "
 "en el nodo no se puede expandir. El auditor leyo este par a ciegas en la "
 "vuelta 157 y tambien dio D. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
 "CONTINUA"),

"LD-OPC05-116": ("C",
 "DISCUTIBLE, Y LO MARCO YO, PORQUE ESTE PAR ROZA EL CRITERIO DE INSTANCIA QUE "
 "ESTE MISMO LOTE APLICA EN OTRAS OCHO. LINEA 1, en reglas_gestion_riesgo_"
 "gambling, paso 4: DEFINIR PUNTOS DE DECISION CLAROS DONDE PUEDAS MATAR EL "
 "PROYECTO si la informacion no es favorable; los expanden los diecisiete pasos "
 "de sistema_gates_go_kill. LINEA 2, en sistema_gates_go_kill, paso 2: "
 "ESTABLECE CRITERIOS CLAROS Y VISIBLES PARA CADA GATE, si el proyecto esta "
 "listo, si el negocio justifica seguir y que recursos necesita la siguiente "
 "etapa; la expanden los pasos 1, 3 y 5 de gambling (evaluar el nivel de "
 "incertidumbre actual antes de asignar recursos, invertir en investigacion de "
 "mercado y tecnica para reducir la incertidumbre antes de aumentar el gasto, "
 "aumentar el monto invertido solo cuando la incertidumbre haya bajado en la "
 "etapa anterior), que es el criterio de riesgo que un gate necesita para "
 "decidir. DOS LINEAS DISTINTAS, UNA PIDE EL PUNTO DE SALIDA Y LA OTRA PIDE EL "
 "CRITERIO, Y NINGUNO ES LA MADRE. LO QUE ME HACE MARCARLA: gambling se puede "
 "leer como UNA REGLA DE RIESGO que el sistema de gates materializa, y bajo esa "
 "lectura seria instancia y caeria a D"),

"LD-OPC05-117": ("D",
 "CRITERIO DE INSTANCIA, Y ADEMAS UNA LINEA QUE NO ES ACCION. PAR MAS FUERTE "
 "DESCARTADO: el paso 2 de riesgos_lanzamiento_mvp (si temes que te copien la "
 "idea, recuerda que tu verdadera ventaja no es el secreto sino ejecutar rapido "
 "y aprender antes que los demas) contra los seis pasos de wizard_of_oz: el "
 "Mago de Oz es UNA TECNICA de aprendizaje rapido entre varias, un ejemplar, y "
 "ademas esa linea es UN CONSEJO DE ANIMO y no una accion procedimentable. En "
 "la otra direccion, el paso 3 de wizard (lanza el producto a un grupo reducido "
 "sin revelar que es simulado) no lo expande ninguno de los cinco miedos. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-118": ("C",
 "LINEA 1, en vision_estrategia_producto_pivote, paso 2: FORMULA UNA ESTRATEGIA "
 "INICIAL, modelo de negocio, hoja de ruta de producto, cliente objetivo y "
 "postura frente a competidores; la expanden los pasos 1, 2, 3 y 8 de search "
 "(determina si estas en modo busqueda o en modo ejecucion, lista explicitamente "
 "las hipotesis de mercado, cliente, producto, canal y precio marcadas como no "
 "probadas, aplica Customer Development para probarlas con clientes reales, usa "
 "el Business Model Canvas y el Value Proposition Canvas como herramientas de "
 "planificacion flexible). LINEA 2, en search_for_business_model, paso 5: ITERA "
 "Y PIVOTA SEGUN LA EVIDENCIA hasta encontrar un modelo repetible y escalable; "
 "la expanden los pasos 3, 4 y 5 de vision (distingue explicitamente entre "
 "ajustes menores y cambios de rumbo mayores, establece el ciclo Construir "
 "Medir Aprender como mecanismo de direccion continua, evalua regularmente si "
 "perseverar o pivotar). DOS LINEAS DISTINTAS, UNA FORMULA Y LA OTRA GOBIERNA "
 "EL GIRO, Y NINGUNO ES LA MADRE"),

"LD-OPC05-119": ("D",
 "ANCLAS DISTINTAS: MODELO CONTRA MUNDO. PAR MAS FUERTE DESCARTADO: el paso 8 "
 "de simulacion (probar combinaciones de tecnologias, robots, manufactura "
 "aditiva y vehiculos autonomos, EN EL MODELO) contra los cinco pasos de "
 "vehiculos_autonomos (identificar tramos de alto volumen repetitivo, revisar "
 "el marco regulatorio local, evaluar el tipo de vehiculo por tramo, disenar el "
 "sistema central de coordinacion, lanzar un piloto en area limitada y medir): "
 "la linea pide probar EN EL MODELO y el otro nodo procedimenta UN DESPLIEGUE "
 "FISICO. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-120": ("D",
 "SUJETOS DISTINTOS. PAR MAS FUERTE DESCARTADO: el paso 4 de "
 "tesis_boulder_inclusividad (facilitar la integracion de recien llegados a la "
 "ciudad o comunidad) contra los pasos 1 y 2 de tesis_boulder_stack (disena "
 "actividades practicas, encuentros de trabajo intensivo o fines de semana de "
 "arranque, en lugar de solo juntadas; asegurate de que participen de verdad "
 "todos los roles, fundadores, inversionistas, mentores y posibles "
 "integrantes): el stack habla de QUE PARTICIPEN TODOS LOS ROLES, no de QUE "
 "ENTREN LOS RECIEN LLEGADOS, y sujeto distinto es la definicion de D. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-121": ("D",
 "DOS MOMENTOS DISTINTOS DEL MISMO TRAMITE. PAR MAS FUERTE DESCARTADO: el paso "
 "3 de venture_debt_introduccion (identificar bancos especializados o fondos de "
 "deuda de riesgo con track record en el sector) contra el paso 5 de "
 "venture_debt_terminos (comparar ofertas entre bancos, que piden menos "
 "warrants pero imponen mas covenants, y fondos de deuda, que piden mas "
 "warrants pero imponen menos): IDENTIFICAR A QUIEN PEDIR y COMPARAR LAS "
 "OFERTAS RECIBIDAS son acciones distintas en momentos distintos, y la segunda "
 "no es el como de la primera. En la otra direccion, los pasos 1 a 4 de "
 "terminos son negociacion de precio y no los expande la introduccion. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),
}


def main():
    ids = json.load(io.open(NOMINA, encoding="utf-8"))["lote"]
    return motor.aplicar(
        "VUELTA 159, TAREA 3: EL LOTE 2 DEL SACO, 53 LECTURAS",
        V, MARCA, cabeza, nota_md, ids_esperados=ids)


if __name__ == "__main__":
    raise SystemExit(main())
