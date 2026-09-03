# -*- coding: utf-8 -*-
"""vuelta161_tarea2_relectura.py . TAREA 2 DE LA VUELTA 161.

LAS CATORCE QUE HOY ESTAN EN `C`, RELEIDAS UNA VEZ CON LA VARA CONGELADA, COMO
UN SOLO TRAMO DIRIGIDO. Es UNA sola relectura, no una pasada abierta: la
decision del fundador del 3 sep 2026 dice UNA vez.

LA VARA ES `P.5.1` DEL BANCO DEL PLAN, CONGELADA POR DECISION DEL FUNDADOR, Y SE
CITA POR SU NUMERO EN CADA VEREDICTO:

    LA SEGUNDA LINEA DE UN PAR SOLO CUENTA COMO EXPANSION SI TRAE PROCEDIMIENTO
    PROPIO, Y NO SOLO EL NOMBRE DE OTRO.

COMO SE LEE, DECLARADO ANTES DE LEER PARA QUE SE PUEDA AUDITAR: la frase dice
que la segunda linea *cuenta COMO EXPANSION*, o sea que **LA SEGUNDA LINEA ES EL
LADO QUE EXPANDE**, y lo que se le exige es que traiga procedimiento propio. Esa
lectura es la unica que reproduce LOS CUATRO EJEMPLARES a la vez:
  - `052` ACEPTA: el lado que expande son las **6 preguntas de Chopra y Meindl**
    con sus seis dimensiones enumeradas. Trae procedimiento.
  - `095` ACEPTA: el lado que expande son los **cinco pasos de process tracing**,
    un metodo secuenciado entero. Trae procedimiento.
  - `122` EXCLUYE: el lado que expande *nombra* simplificar el trabajo y no lo
    procedimenta.
  - `100` EXCLUYE: el lado que expande es *la misma orden con tres complementos*.
NO SE ESTRECHA NI SE ENSANCHA NADA: se declara como se lee y se aplica igual a
las catorce.

LOS NODOS SE IMPRIMEN ENTEROS ANTES DE ADJUDICAR: el dossier es
`docs/loop/SALIDA_V161_T2_DOSSIER.txt`, producido por
`vuelta159_dossier.py --nomina docs/loop/NOMINA_V161_TRAMO_C.json`, y cada
veredicto de abajo cita los pasos por su numero.

LA GUARDA DE COHERENCIA DEL ENCARGO, APLICADA: `052` y `095` son los ejemplares
de ACEPTACION de la vara. Si alguna cayera, eso no es una reclasificacion mas: es
la lectura contra la vara que el fundador acaba de congelar, y se para. Las dos
sostienen `C` y el instrumento lo comprueba por assert.

LA PARADA QUE SI TRAIGO, Y NO LA RESUELVO YO (`049` y `098`): en esos dos pares
LA LETRA DE `P.5.1` Y EL EJEMPLAR `100` DE `P.5.1` APUNTAN EN SENTIDOS OPUESTOS
SOBRE EL MISMO NODO (`lienzo_modelo_negocio`). La letra sostiene `C`; el ejemplar
excluye. Resolver esa colision es MOVER LA FRONTERA, y el encargo lo prohibe con
todas sus letras. **LA CLASE NO SE TOCA Y LA VARA TAMPOCO**: se deja `C` como
estaba, se escribe el caso entero en la razon y se trae al fundador.

LA MARCA DE ESTA RELECTURA ES CONTABLE POR `P.5.2`, la definicion que la TAREA
1.c de esta misma vuelta escribio: dice que es una RELECTURA y dice EN QUE
VUELTA. La forma nueva se anade a `FORMAS_QUE_CUENTAN` del contador, o la
definicion escrita hoy no contaria la lectura de hoy.

USO:  python scripts/loop/vuelta161_tarea2_relectura.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = motor.RAIZ
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V161_TRAMO_C.json")
MARCA = "RELECTURA DEL TRAMO DE LAS CATORCE EN C, VUELTA 161"

VARA = ("P.5.1 (la segunda linea solo cuenta como expansion si trae "
        "procedimiento propio y no solo el nombre de otro)")


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR "
                "NADA DE LO ANTERIOR: LA CLASE PASA DE %s A %s. Criterio: %s. "
                % (MARCA, vieja, nueva, VARA))
    return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
            "CLASE SE SOSTIENE EN %s. Criterio: %s. " % (MARCA, vieja, VARA))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 161, relectura de las catorce en C "
                "con la vara congelada P.5.1): la clase pasa de ~~%s~~ a %s. %s."
                % (vieja, nueva, motivo[:260]))
    return ("RELECTURA DEL TRAMO DE LAS CATORCE EN C CON LA VARA CONGELADA P.5.1 "
            "(vuelta 161): la clase SE SOSTIENE en %s y su caso queda escrito en "
            "la razon del registro de citas." % vieja)


# --------------------------------------------------------------------------
# LOS VEREDICTOS. {ld: (clase, motivo)}. Cada motivo NOMBRA LAS DOS LINEAS por
# el numero de paso que el dossier imprime, y dice cual es LA SEGUNDA LINEA (el
# lado que expande) y por que trae o no trae procedimiento propio.
# --------------------------------------------------------------------------
V = {}

V["LD-OPC05-005"] = ("C", (
    "LAS DOS LINEAS, POR SU NUMERO DE PASO. LINEA 1, aim_of_leadership paso 2 "
    "(investigar las causas de raiz del sistema que afectan el desempeno "
    "general); LA EXPANDE causas_comunes_vs_especiales con sus quince pasos, que "
    "son su como se hace: recopilar los datos en orden cronologico y no como "
    "distribucion agregada (paso 1), graficar y calcular limites (paso 2), "
    "aplicar reglas de senal (paso 3), listar las causas comunes propias del "
    "sistema, diseno, materiales, instruccion y condiciones (paso 5) y redisenar "
    "el proceso en vez de sancionar al individuo (paso 7). LINEA 2, "
    "causas_comunes_vs_especiales paso 13 (dar seguimiento y apoyo a quienes "
    "caen fuera de las tolerancias del grupo); LA EXPANDEN los pasos 1, 3 y 5 de "
    "aim_of_leadership. POR LA VARA CONGELADA: el lado que expande la linea 2 "
    "trae procedimiento propio y no el nombre de otro nodo: identificar CON "
    "DATOS O CON CRITERIO y por las DOS COLAS, por bajo o por muy alto desempeno "
    "(paso 1), disenar ayuda individual o reconocimiento segun corresponda (paso "
    "3) y estudiar a los de desempeno excepcional PARA REPLICAR SUS METODOS "
    "(paso 5). Es una secuencia con contenido propio, de la especie del ejemplar "
    "095 y no de la del 122. LA CLASE SE SOSTIENE EN C. QUEDA MARCADA COMO "
    "DISCUTIBLE, Y SE DICE POR QUE ANTES DE SABER SI ACIERTO: el lado que expande "
    "la linea 2 es FINO, y su paso 3 leido solo seria orden mas complemento, o "
    "sea de la especie que el ejemplar 122 excluye; se sostiene porque los tres "
    "pasos leen como secuencia, no porque ninguno de ellos solo procedimente"))

V["LD-OPC05-038"] = ("C", (
    "LINEA 1, control_estadistico_de_procesos paso 9 (calcular limites de "
    "control y definir instrucciones de interpretacion y accion); LA EXPANDE "
    "plan_de_control con sus pasos 4 a 7: donde, cuando y como se registran las "
    "mediciones, quien las analiza y determina si el proceso esta fuera de "
    "control, quien actua para diagnosticar y eliminar la causa asignable, y los "
    "pasos para regresar el proceso a control. LINEA 2, plan_de_control paso 2 "
    "(establecer el estandar que activara una accion, idealmente un limite de "
    "control de una carta de control); LA EXPANDE control_estadistico_de_procesos "
    "con sus pasos 5 a 7: elegir el tipo de grafico, decidir la linea central y "
    "los limites, usualmente mas menos tres sigma calculados a partir del rango "
    "promedio, y elegir subgrupos racionales, por ejemplo n igual a 4 o 5. POR LA "
    "VARA CONGELADA: el lado que expande la linea 2 trae procedimiento propio CON "
    "SUS PARAMETROS (tres sigma, rango promedio, n de 4 o 5), que es la especie "
    "del ejemplar 052, un instrumento con sus dimensiones. SON DOS LINEAS "
    "DISTINTAS, UNA EN CADA NODO, Y NINGUNA DE LAS DOS DIRECCIONES APUNTA A LA "
    "MISMA LINEA. LA CLASE SE SOSTIENE EN C"))

V["LD-OPC05-049"] = ("C", (
    "PARADA, Y LA CLASE NO SE TOCA. AQUI LA LETRA DE LA VARA CONGELADA Y UNO DE "
    "SUS CUATRO EJEMPLARES APUNTAN EN SENTIDOS OPUESTOS SOBRE EL MISMO NODO, "
    "lienzo_modelo_negocio, y resolver esa colision es MOVER LA FRONTERA, que el "
    "encargo del fundador prohibe con todas sus letras. LO QUE DICE LA LETRA: "
    "LINEA 1, decision_pivotar_o_proceder paso 4 (toma un Business Model Canvas "
    "nuevo y busca game changers revisando propuesta de valor, precios, canales y "
    "relaciones con clientes, no solo mejoras incrementales), LA EXPANDEN los "
    "doce pasos de lienzo_modelo_negocio; LINEA 2, lienzo_modelo_negocio paso 12 "
    "(usar el lienzo como base para pivotar o validar hipotesis del negocio), LA "
    "EXPANDEN los seis pasos de decision_pivotar_o_proceder, que traen "
    "procedimiento propio: revisar honestamente si la validacion convirtio "
    "opiniones en hechos (paso 1), confirmar venta, prediccion, escalabilidad, "
    "rentabilidad y proceso de ventas repetible (paso 2), verificar tiempos de "
    "entrega (paso 3), presentar el canvas al consejo asesor para que lo "
    "cuestione (paso 5) y decidir formalmente (paso 6). POR LA LETRA, LA C SE "
    "SOSTENDRIA. LO QUE DICE EL EJEMPLAR 100: ese ejemplar es "
    "lienzo_modelo_negocio contra un nodo que lo CONSUME, y la vara lo EXCLUYE; "
    "el argumento que lo decidio en la vuelta 160 fue el ENTREGABLE, y aqui se "
    "lee igual: el entregable de decision_pivotar_o_proceder dice Business Model "
    "Canvas ACTUALIZADO y el entregable de lienzo_modelo_negocio no menciona la "
    "decision de pivotar, o sea una sola direccion, madre e hijo. POR EL "
    "EJEMPLAR, LA CLASE SERIA D. NO ADJUDICO, NO MUEVO LA CLASE Y NO TOCO LA "
    "VARA: se trae al fundador"))

V["LD-OPC05-052"] = ("C", (
    "EJEMPLAR DE ACEPTACION DE LA VARA CONGELADA, RELEIDO IGUAL QUE LOS DEMAS Y "
    "NO DADO POR BUENO. LINEA 1, definicion_alineacion_cadena_suministro paso 4 "
    "(alinear las decisiones de produccion, inventario, ubicacion y transporte "
    "con la estrategia elegida, que son los 5 drivers); LA EXPANDE "
    "trade_off_responsividad_eficiencia con su paso 3 (ajustar CADA driver hacia "
    "el extremo del espectro que corresponda) apoyado en sus pasos 1, 2, 5, 6 y "
    "7. LINEA 2, trade_off_responsividad_eficiencia paso 1 (analizar que valora "
    "mas tu segmento de clientes, precio bajo o rapidez y servicio); LA EXPANDE "
    "definicion_alineacion_cadena_suministro paso 8, LAS 6 PREGUNTAS DE CHOPRA Y "
    "MEINDL con sus seis dimensiones enumeradas: cantidad por lote, tiempo de "
    "respuesta, variedad, nivel de servicio, precio y tasa de innovacion. POR LA "
    "VARA CONGELADA: ese lado trae procedimiento propio, un instrumento con autor "
    "y seis dimensiones, que es literalmente el ejemplar que la vara nombra. LA "
    "CLASE SE SOSTIENE EN C, como la vara exige por construccion"))

V["LD-OPC05-068"] = ("C", (
    "LINEA 1, eliminar_metas_numericas_gerencia paso 3 (determinar la capacidad "
    "real del sistema mediante analisis estadistico ANTES de fijar cualquier "
    "meta); LA EXPANDE sistema_estable_causas_comunes con sus cinco pasos, que "
    "son un metodo secuenciado entero: recolectar datos diarios de defectos "
    "durante varias semanas (paso 1), graficarlos en carta de corrida o de "
    "control para verificar si la variacion es estable (paso 2), clasificar la "
    "variacion como causa comun o especial (paso 3) y, si el sistema es estable, "
    "identificar que cambios estructurales, materiales, herramientas o "
    "capacitacion, mueven su capacidad (paso 4). LINEA 2, "
    "sistema_estable_causas_comunes paso 5 (evitar fijar metas numericas o culpar "
    "a la persona que te ayuda hasta haber intervenido sobre el sistema mismo); "
    "LA EXPANDEN los pasos 1, 2 y 4 de eliminar_metas_numericas_gerencia: revisar "
    "las metas numericas actuales y verificar si cuentan con un plan de accion "
    "concreto, eliminar las que solo se basen en deseos o presion sin metodo "
    "definido, y reemplazar las arbitrarias por objetivos de mejora continua con "
    "planes de accion especificos. POR LA VARA CONGELADA: ese lado trae "
    "procedimiento propio, con su criterio de descarte escrito (tener o no plan "
    "de accion concreto), y no es el nombre de otro nodo. LA CLASE SE SOSTIENE EN "
    "C. QUEDA MARCADA COMO DISCUTIBLE, Y SE DICE POR QUE ANTES DE SABER SI "
    "ACIERTO: la linea 2 es una PROHIBICION con condicion temporal, no un acto, y "
    "P.11 dice que una advertencia califica el acto y no lo constituye; si P.11 "
    "alcanza tambien al lado EXPANDIDO y no solo al que expande, esta figura se "
    "cae y la clase seria D. NO LO RESUELVO POR MI CUENTA porque P.5.1 solo pone "
    "condicion al lado que expande, y ensancharla o estrecharla es mover la vara"))

V["LD-OPC05-081"] = ("C", (
    "LINEA 1, fase_accomplish_experiencia_cliente paso 2 (implementar un sistema "
    "de seguimiento, automatizado o manual, para saber cuando el cliente alcanza "
    "el objetivo); LA EXPANDE reunion_conclusion_proyecto con sus pasos 1, 7, 8, "
    "9 y 12: programar la reunion de conclusion revisando los objetivos y "
    "metricas del kickoff, revisar esos objetivos y metricas, evaluar "
    "honestamente el nivel de exito en cada metrica, pedir feedback del cliente "
    "sobre esas metricas y establecer un plan de monitoreo post entrega. LINEA 2, "
    "reunion_conclusion_proyecto paso 5 (establecer un periodo de monitoreo "
    "posterior, por ejemplo tres meses, para mitigar el remordimiento post "
    "lanzamiento); LA EXPANDEN los pasos 8, 9, 10 y 11 de "
    "fase_accomplish_experiencia_cliente: disenar un punto de seguimiento "
    "POSTERIOR al logro del objetivo aparente, por ejemplo pedir una foto o "
    "confirmar el resultado real, mantener contacto y apoyo del equipo mas alla "
    "del cumplimiento nominal del contrato, evitar que el equipo desacelere justo "
    "cuando el cliente cree haber terminado, y recoger evidencia del resultado "
    "logrado. POR LA VARA CONGELADA: ese lado trae procedimiento propio, con "
    "actos concretos y no con el nombre de otro nodo. SON DOS LINEAS DISTINTAS "
    "(un sistema de seguimiento del LOGRO contra un periodo de monitoreo POST "
    "ENTREGA) y no colapsan en la misma. LA CLASE SE SOSTIENE EN C"))

V["LD-OPC05-084"] = ("C", (
    "LINEA 1, genchi_gembutsu_salir_del_edificio paso 1 (identificar las "
    "preguntas de fe mas criticas del negocio); LA EXPANDE "
    "leap_of_faith_assumptions con sus cinco pasos: separar los hechos "
    "comprobados de las suposiciones no verificadas incluidos el modelo de "
    "negocio y el spreadsheet financiero, distinguir las de bajo riesgo de los "
    "verdaderos saltos de fe, reescribir las comparaciones en terminos concretos "
    "y verificables evitando analogias que oculten el riesgo, y ordenarlas por "
    "riesgo. LINEA 2, leap_of_faith_assumptions paso 5 (disenar experimentos "
    "especificos para validar cada leap of faith question antes de construir el "
    "producto completo); LA EXPANDEN los pasos 2 a 6 de "
    "genchi_gembutsu_salir_del_edificio: salir fisicamente a hablar con clientes "
    "potenciales reales y no solo encuestas remotas, observar el comportamiento "
    "real en su contexto natural, no decidir con reportes de segunda mano, "
    "documentar los hallazgos de primera mano para contrastarlos con las "
    "hipotesis, y usar esas observaciones para ajustar el diseno. POR LA VARA "
    "CONGELADA: ese lado trae procedimiento propio, con su instrumento y su "
    "prohibicion de metodo, y no es el nombre de otro nodo. LA CLASE SE SOSTIENE "
    "EN C. QUEDA MARCADA COMO DISCUTIBLE, Y SE DICE POR QUE ANTES DE SABER SI "
    "ACIERTO: la linea 2 manda DISENAR EXPERIMENTOS y lo que genchi procedimenta "
    "es OBSERVAR; el encaje es por proposito y no por acto, y un lector estricto "
    "puede leer que genchi no procedimenta el diseno del experimento sino su "
    "ejecucion"))

V["LD-OPC05-087"] = ("C", (
    "LINEA 1, gestion_portafolio_dos_niveles paso 1 (establecer un proceso de "
    "gating para revisar cada proyecto individualmente); LA EXPANDE "
    "sistema_gates_go_kill con sus diecisiete pasos, que traen la disciplina "
    "entera: definir los gates en los puntos clave (paso 1), criterios visibles "
    "por gate (paso 2), checklist o scorecard (paso 3), decision explicita Go, "
    "Kill, Hold, Recycle y Conditional Go (paso 4) y compromiso de recursos solo "
    "despues del gate (paso 5). LINEA 2, sistema_gates_go_kill paso 10 (conecta "
    "cada punto de decision con la forma en que asignas recursos y con la vision "
    "general de tus proyectos); LA EXPANDEN los pasos 2, 3 y 4 de "
    "gestion_portafolio_dos_niveles: revisiones de portafolio trimestrales o "
    "semestrales que vean el conjunto completo, definir que decisiones son "
    "estrategicas y cuales tacticas, y usar ambos procesos de forma "
    "complementaria y no sustitutiva. POR LA VARA CONGELADA: ese lado trae "
    "procedimiento propio, con su frecuencia y su reparto estrategico contra "
    "tactico, y no es el nombre de otro nodo. LA CLASE SE SOSTIENE EN C. Y VA "
    "UNA CORRECCION DE CITA, DECLARADA Y SIN BORRAR EL TEXTO VIEJO: la razon "
    "escrita arriba dice que la ficha de OP-E-04 declara este par mutuo "
    "exceptuado EN SU VERIFICACION 5, y eso NO es lo que dice la ficha leida hoy: "
    "la verificacion 5 es la de P.9 y los ids resueltos, y LA EXCEPCION DEL 9.22 "
    "VIVE EN LA VERIFICACION 6, que nombra los pares exceptuados por las filas "
    "LD-35 con LD-51, LD-49, LD-40 con LD-48 y LD-45 con LD-53. Este par es el de "
    "LD-35 con LD-51 (gestion_portafolio_dos_niveles contra estructura_gates y "
    "contra gates_go_kill_decision_points, los dos alias que mueren en "
    "sistema_gates_go_kill), o sea que la excepcion SI lo cubre; lo que estaba "
    "mal era el numero de la verificacion citada"))

V["LD-OPC05-088"] = ("C", (
    "LINEA 1, gestion_portafolio_foco paso 2 (aplicar criterios estrictos de Go "
    "Kill para reducir el numero de proyectos en pipeline); LA EXPANDE "
    "sistema_gates_go_kill con sus diecisiete pasos, incluidos los criterios "
    "eliminatorios de entrada (paso 12) y los criterios must meet, go kill "
    "financieros y should meet cualitativos (paso 16). LINEA 2, "
    "sistema_gates_go_kill paso 13 (decide como vas a priorizar los proyectos que "
    "si cumplen, dandole mas peso a lo que mas te importa); LA EXPANDEN los pasos "
    "1, 3, 4 y 5 de gestion_portafolio_foco: auditar el numero de proyectos "
    "activos contra la capacidad real de recursos, priorizar los de mayor "
    "potencial estrategico y financiero, evitar el multitasking excesivo del "
    "personal entre proyectos simultaneos, y revisar periodicamente el balance "
    "del portafolio por riesgo, tipo de innovacion y mercados. POR LA VARA "
    "CONGELADA: ese lado trae procedimiento propio, con sus tres ejes de balance "
    "enumerados, que es la especie del ejemplar 052. LA CLASE SE SOSTIENE EN C. "
    "CORRECCION DE CITA DECLARADA, SIN BORRAR EL TEXTO VIEJO: la razon de arriba "
    "cita la VERIFICACION 5 de OP-E-04 y la excepcion del 9.22 vive en la "
    "VERIFICACION 6; este par es el de LD-45 con LD-53 y la excepcion SI lo "
    "cubre"))

V["LD-OPC05-095"] = ("C", (
    "EJEMPLAR DE ACEPTACION DE LA VARA CONGELADA, RELEIDO IGUAL QUE LOS DEMAS Y "
    "NO DADO POR BUENO. LINEA 1, investigacion_new_view paso 1 (reconstruir la "
    "situacion tal como la vivieron los involucrados, sin usar el conocimiento "
    "del resultado final, a partir de la informacion y las senales disponibles "
    "para los actores en el momento); LA EXPANDE process_tracing_methods con sus "
    "cinco pasos, un metodo secuenciado entero: recolectar datos crudos del "
    "episodio, construir el relato especifico del dominio en el lenguaje tecnico "
    "de los practicantes, aplicar conceptos dependientes como sorpresa de "
    "automatizacion o carga de trabajo, buscar regularidades a traves de los dos "
    "relatos paralelos, y documentar evitando el lenguaje de deficit humano. "
    "LINEA 2, process_tracing_methods paso 2 (construir el relato especifico del "
    "dominio en el lenguaje tecnico de los practicantes); LA EXPANDEN los pasos "
    "5, 6 y 7 de investigacion_new_view: contrastar la investigacion oficial con "
    "relatos revisionistas o independientes, involucrar perspectivas de colegas, "
    "familiares o testigos cercanos, y entrevistar a los involucrados para "
    "entender su percepcion y objetivos en el momento. POR LA VARA CONGELADA: los "
    "dos lados traen procedimiento propio y ninguno es el nombre del otro, que es "
    "literalmente el ejemplar que la vara nombra. LA CLASE SE SOSTIENE EN C, como "
    "la vara exige por construccion"))

V["LD-OPC05-098"] = ("C", (
    "PARADA, Y LA CLASE NO SE TOCA. ES LA MISMA COLISION QUE LA LD-OPC05-049 Y "
    "SOBRE EL MISMO NODO, lienzo_modelo_negocio. LO QUE DICE LA LETRA DE P.5.1: "
    "LINEA 1, lean_launchpad_web_startup_process paso 2 (redactar las hipotesis "
    "del modelo de negocio de 9 bloques), LA EXPANDEN los doce pasos de "
    "lienzo_modelo_negocio, que son el como se llenan esos nueve bloques; LINEA "
    "2, lienzo_modelo_negocio paso 12 (usar el lienzo como base para pivotar o "
    "VALIDAR HIPOTESIS del negocio), LA EXPANDEN los pasos 5 a 10 de "
    "lean_launchpad_web_startup_process, que traen procedimiento propio para "
    "validar: construir un sitio de baja fidelidad con splash page y formularios "
    "de pre orden, dirigir trafico para probar segmento y propuesta de valor, "
    "conectar la interfaz con el backend, probar el problema del cliente con "
    "analytics y encuestas, construir la version de alta fidelidad para probar la "
    "solucion, y pedir dinero con pre orden o cobro real. POR LA LETRA, LA C SE "
    "SOSTENDRIA. LO QUE DICE EL EJEMPLAR 100: el paso 12 del lienzo NOMBRA "
    "validar hipotesis y no lo procedimenta, y el otro nodo CONSUME el lienzo en "
    "su paso 2, o sea una sola direccion, madre e hijo. POR EL EJEMPLAR, LA CLASE "
    "SERIA D. Y HAY UNA DIFERENCIA CON LA 049 QUE SE DECLARA EN VEZ DE TAPARSE: "
    "aqui el ENTREGABLE de lean_launchpad no menciona el lienzo (dice sitio web "
    "de alta fidelidad con metricas, feedback y cobro), asi que el argumento del "
    "entregable que decidio la 100 es MAS DEBIL en este par que en la 049. NO "
    "ADJUDICO, NO MUEVO LA CLASE Y NO TOCO LA VARA: se trae al fundador"))

V["LD-OPC05-109"] = ("C", (
    "LINEA 1, plan_gestion_comunicaciones paso 1 (haz una lista de las personas o "
    "grupos que necesitan recibir informacion de tu proyecto); LA EXPANDE "
    "plan_gestion_interesados con sus pasos 1, 2 y 4: anotar el nivel de "
    "compromiso actual y el deseado de cada persona, ubicar a cada una en la "
    "escala de cinco posiciones (no lo conoce, se resiste, es neutral, lo apoya, "
    "ya lo defiende) e identificar como se relacionan entre si los grupos. LINEA "
    "2, plan_gestion_interesados paso 3 (define que necesita saber cada persona y "
    "como se lo vas a comunicar); LA EXPANDEN los pasos 2 a 6 de "
    "plan_gestion_comunicaciones: describir que tipo de informacion va a cada uno "
    "(reportes de avance, actas, actualizaciones), decidir el metodo de entrega, "
    "definir cada cuanto o en que momento, decidir quien es el responsable de "
    "mandar cada comunicacion, y anotar restricciones, supuestos y un glosario. "
    "POR LA VARA CONGELADA: los dos lados traen procedimiento propio con sus "
    "campos enumerados (uno la escala de cinco niveles, el otro los cinco campos "
    "de la matriz de comunicacion) y ninguno es el nombre del otro. SON DOS "
    "LINEAS DISTINTAS (la NOMINA de destinatarios contra el CONTENIDO y el CANAL "
    "por persona) y no colapsan en la misma. LA CLASE SE SOSTIENE EN C"))

V["LD-OPC05-110"] = ("C", (
    "LINEA 1, portfolio_management paso 4 (tomar decisiones Go Kill continuas "
    "sobre proyectos individuales); LA EXPANDE sistema_gates_go_kill con sus "
    "diecisiete pasos, que traen la disciplina de esa decision: puntos de "
    "decision definidos, criterios visibles, checklist, la decision explicita con "
    "sus cinco salidas y el compromiso de recursos solo despues del gate. LINEA "
    "2, sistema_gates_go_kill paso 10 (conecta cada punto de decision con la "
    "forma en que asignas recursos y con la vision general de tus proyectos); LA "
    "EXPANDEN los pasos 1, 2, 3 y 6 de portfolio_management: evaluar si existen "
    "demasiados proyectos para los recursos disponibles, revisar el balance del "
    "portafolio entre proyectos pequenos y de alto valor, implementar revisiones "
    "periodicas de todo el portafolio de forma holistica, y reasignar los "
    "recursos liberados a los proyectos de mayor valor. POR LA VARA CONGELADA: "
    "ese lado trae procedimiento propio, con su criterio de balance y su "
    "reasignacion, y no es el nombre de otro nodo. LA CLASE SE SOSTIENE EN C. "
    "CORRECCION DE CITA DECLARADA, SIN BORRAR EL TEXTO VIEJO: la razon de arriba "
    "cita la VERIFICACION 5 de OP-E-04 y la excepcion del 9.22 vive en la "
    "VERIFICACION 6; este par es el de LD-40 con LD-48 y la excepcion SI lo "
    "cubre. Y SE DECLARA LA CERCANIA CON LA 087, QUE ES REAL: las dos usan el "
    "paso 10 de sistema_gates_go_kill como su linea 2. Eso no es el defecto que "
    "el 9.22 prohibe, que es que LAS DOS DIRECCIONES DE UN MISMO PAR apunten a la "
    "misma linea; aqui son pares distintos y en cada uno las dos direcciones "
    "apuntan a lineas distintas"))

V["LD-OPC05-116"] = ("C", (
    "LINEA 1, reglas_gestion_riesgo_gambling paso 4 (definir puntos de decision "
    "claros, gates, donde puedas matar el proyecto si la informacion no es "
    "favorable); LA EXPANDE sistema_gates_go_kill con sus diecisiete pasos, que "
    "son el como se hace ese gate: donde ponerlo, con que criterios, con que "
    "checklist, con que cinco salidas y con que entregables estandar. LINEA 2, "
    "sistema_gates_go_kill paso 5 (comprometete recursos, tiempo y dinero, solo "
    "despues de pasar el gate y no antes); LA EXPANDEN los pasos 1, 2, 3 y 5 de "
    "reglas_gestion_riesgo_gambling: evaluar el nivel de incertidumbre actual "
    "antes de asignar recursos a la siguiente etapa, dividir la inversion total "
    "en etapas incrementales en vez de comprometer todo el presupuesto de una "
    "vez, invertir en investigacion de mercado y tecnica para reducir la "
    "incertidumbre antes de aumentar el gasto, y aumentar el monto invertido solo "
    "cuando la incertidumbre haya bajado en la etapa anterior. POR LA VARA "
    "CONGELADA: ese lado trae procedimiento propio, y es un procedimiento con su "
    "propia variable de control (la incertidumbre medida etapa a etapa), no el "
    "nombre de otro nodo. Y SE DECLARA LO QUE ESTE PAR NO TIENE, en vez de "
    "callarlo: a diferencia de la 087, la 088 y la 110, ESTE PAR NO ESTA EN LA "
    "EXCEPCION DEL 9.22 DE OP-E-04 (verificacion 6), cuyos pares exceptuados son "
    "LD-35 con LD-51, LD-49, LD-40 con LD-48 y LD-45 con LD-53, y "
    "reglas_gestion_riesgo_gambling no aparece en ninguna de esas filas. La C de "
    "este par se sostiene SOLO por la lectura de sus dos lineas, sin declaracion "
    "sellada detras. LA CLASE SE SOSTIENE EN C"))

PARADAS = ["LD-OPC05-049", "LD-OPC05-098"]
DISCUTIBLES_PROPIOS = ["LD-OPC05-005", "LD-OPC05-068", "LD-OPC05-084"]
EJEMPLARES_DE_ACEPTACION = ["LD-OPC05-052", "LD-OPC05-095"]


def main():
    nomina = json.loads(io.open(NOMINA, encoding="utf-8").read())["tramo"]

    rc = motor.aplicar(
        "VUELTA 161, TAREA 2: LAS CATORCE EN C, RELEIDAS CON LA VARA CONGELADA",
        V, MARCA, cabeza, nota_md, ids_esperados=nomina)
    if rc:
        return rc

    print("=" * 78)
    print("D) LA GUARDA DE COHERENCIA DEL ENCARGO: LOS DOS EJEMPLARES DE ACEPTACION")
    print("=" * 78)
    E = motor.entradas()
    clases = {motor.ld_de(e): e["clase"] for e in E}
    for ld in EJEMPLARES_DE_ACEPTACION:
        print("   %-16s clase tras la relectura: %s" % (ld, clases[ld]))
    caidos = [ld for ld in EJEMPLARES_DE_ACEPTACION if clases[ld] != "C"]
    if caidos:
        print("   PARADA: %s dejo de ser C. La lectura contradice la vara que el"
              % ", ".join(caidos))
        print("   fundador acaba de congelar. NO SE TOCA NI LA CLASE NI LA VARA.")
        return 1
    print("   LOS DOS SOSTIENEN C. La guarda pasa.")
    print("")

    print("=" * 78)
    print("E) EL REPARTO DE LA RELECTURA")
    print("=" * 78)
    sostienen = [ld for ld in nomina if V[ld][0] == clases[ld] == "C"]
    print("   CIFRA lecturas del tramo: %d" % len(nomina))
    print("   CIFRA que SOSTIENEN su clase: %d" % len(sostienen))
    print("   CIFRA que CAMBIAN de clase: %d"
          % len([ld for ld in nomina if clases[ld] != "C"]))
    print("   CIFRA traidas como PARADA de frontera: %d" % len(PARADAS))
    for ld in PARADAS:
        print("      %s (clase intacta en %s)" % (ld, clases[ld]))
    print("")

    print("F) LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    print("   (i) LAS DOS PARADAS DE FRONTERA, que son discutibles por definicion:")
    for ld in PARADAS:
        print("      %s" % ld)
    print("   (ii) LAS QUE MARCO POR DUDA PROPIA: %d" % len(DISCUTIBLES_PROPIOS))
    for ld in DISCUTIBLES_PROPIOS:
        print("      %s" % ld)
    todos = sorted(set(PARADAS) | set(DISCUTIBLES_PROPIOS))
    print("   CIFRA discutibles de este tramo: %d de %d" % (len(todos), len(nomina)))
    print("")
    print("G) LA CORRECCION DE CITA QUE ESTE TRAMO TRAE, Y NO ES MIA")
    print("   Las razones de LD-OPC05-087, LD-OPC05-088 y LD-OPC05-110 dicen que")
    print("   la ficha de OP-E-04 declara el par mutuo exceptuado EN SU")
    print("   VERIFICACION 5. Leida la ficha HOY en docs/plan/OPERACIONES.jsonl,")
    print("   la verificacion 5 es la de P.9 y los ids resueltos, y la excepcion")
    print("   del 9.22 vive en la VERIFICACION 6. Los tres pares SI estan")
    print("   exceptuados; el numero citado estaba mal. Corregido por adicion en")
    print("   las tres razones, sin borrar el texto viejo.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
