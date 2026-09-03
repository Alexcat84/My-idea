# -*- coding: utf-8 -*-
"""vuelta159_tarea2b_relectura_tramo.py . TAREA 2.b DE LA VUELTA 159, EL TRAMO
QUE SE RELEE AL DOBLE.

LAS 41 LECTURAS DEL LOTE 1 QUE CAYERON A D Y QUE NADIE HABIA VUELTO A MIRAR
(adjudicacion 6.5 del acta 158), leidas una a una CONTRA LOS NODOS con el
dossier `docs/loop/SALIDA_V159_T2B_DOSSIER.txt`, en SEGUNDA PASADA
INDEPENDIENTE. La nomina no se teclea: la sella
`vuelta159_tarea2b_nomina_relectura.py` en
`docs/loop/NOMINA_V159_RELECTURA.json` y este instrumento la exige.

LA VARA ES LA 6.4 DEL ACTA 157 CON LA CORRECCION DE LA 6.3 DEL ACTA 158, Y LA
6.3 VA PUESTA DESDE LA PRIMERA LECTURA:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

es un EXISTENCIAL. Por eso CADA UNA de las 41 razones de esta tarea NOMBRA EL
PAR MAS FUERTE QUE SE DESCARTO y dice por que no sostiene la figura, en vez de
descartar el primer par que se encuentra. Esa es la comprobacion que al lote 1
le falto y la que aqui se hace en las 41 sin excepcion.

QUE SALIO, ADELANTADO PARA QUE NO HAYA QUE CONTARLO A MANO: CUARENTA SOSTIENEN
LA D Y UNA VUELVE A C (`LD-OPC05-052`), que va MARCADA COMO DISCUTIBLE junto a
otras seis. La segunda pasada no es un tramite: encontro una segunda de la
misma especie que la 005.

LAS GUARDAS SON LAS DE LA 2.d Y VIVEN EN `vuelta159_motor_veredictos.py`.

USO:  python scripts/loop/vuelta159_tarea2b_relectura_tramo.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

RAIZ = motor.RAIZ
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V159_RELECTURA.json")

MARCA = "SEGUNDA PASADA DE LA VUELTA 159"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR "
                "NADA DE LO ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
            "CLASE SE SOSTIENE EN %s, LEIDA DE NUEVO CONTRA LOS NODOS Y CON LA "
            "COMPROBACION DE LA 6.3 HECHA. " % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 159, SEGUNDA PASADA del tramo "
                "releido al doble): la clase pasa de ~~%s~~ a %s. %s."
                % (vieja, nueva, motivo[:260]))
    return ("SEGUNDA PASADA (vuelta 159, tramo releido al doble por la 6.5 del "
            "acta 158): la %s SE SOSTIENE con la comprobacion existencial de la "
            "6.3 hecha, y el par mas fuerte descartado queda nombrado en la "
            "razon del registro de citas." % vieja)


# Cada motivo trae, por la 6.3: (i) por que no hay figura, y (ii) EL PAR MAS
# FUERTE QUE SE DESCARTO, nombrado con sus dos lineas.
V = {
"LD-OPC05-001": ("D",
 "NINGUNA DIRECCION SE SOSTIENE. cero_defectos es un ESTANDAR y un evento de "
 "lanzamiento (fija el compromiso, comunicalo caso por caso, dia ZD, reconoce, "
 "extiende, refuerza, elimina el lenguaje AQL); accion_correctiva_sistematica "
 "es un SISTEMA DE SEGUIMIENTO en tres ritmos. PAR MAS FUERTE DESCARTADO: el "
 "paso 7 de accion correctiva (definir acciones que corrijan la causa raiz y "
 "prevengan la recurrencia) contra el paso 1 de ZD (establecer el estandar de "
 "Cero Defectos como compromiso personal): un compromiso no es el como se hace "
 "una accion correctiva, y ninguno de los siete pasos de ZD procedimenta una "
 "linea del otro. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-003": ("D",
 "UNA SOLA DIRECCION, Y NI ESA ES LIMPIA. El paso 1 del cronograma (recopilar "
 "lista de actividades, diagrama de red y ESTIMACIONES DE DURACION) CONSUME la "
 "salida de activity_duration_estimates; consumir una salida no es que el otro "
 "nodo expanda esa linea, porque la linea es RECOPILAR y no ESTIMAR. PAR MAS "
 "FUERTE DESCARTADO: paso 1 del cronograma contra los cuatro pasos de "
 "activity_duration (metodo parametrico, analogo o tres puntos, conversion a "
 "dias, reserva de contingencia, documentar). Y EN LA OTRA DIRECCION NO HAY "
 "NADA: ninguno de los cuatro pasos de activity_duration esta expandido por el "
 "cronograma. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-004": ("D",
 "DISCUTIBLE, Y LO MARCO YO. UNA DIRECCION LIMPIA Y LA OTRA NO. El paso 4 de "
 "reempaquetado (actualizar el lienzo de modelo de negocio con el nuevo modelo "
 "de entrega o precio) SI lo expanden los cuatro pasos del tune-up (revisa la "
 "propuesta de valor con el feedback, reevalua segmentos, ajusta hipotesis de "
 "ingresos, documenta cambios y sorpresas). PAR MAS FUERTE DESCARTADO EN LA "
 "OTRA DIRECCION: el paso 3 del tune-up (ajusta tus hipotesis de ingresos "
 "segun los segmentos que mostraron entusiasmo) contra los pasos 1 a 3 de "
 "reempaquetado (identificar si el problema es de tecnologia o de "
 "empaquetado, explorar modulos, suscripcion y versiones escalonadas, validar "
 "con clientes). SE DESCARTA porque reempaquetado es UN REMEDIO HERMANO, una "
 "de varias clases de pivote, y contesta QUE CAMBIAR, no COMO SE AJUSTAN las "
 "hipotesis de ingresos. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-006": ("D",
 "MATERIAS DISTINTAS: uno alinea la TECNOLOGIA con el modelo (aplicaciones, "
 "datos, infraestructura, seguridad, capacitacion tecnologica) y el otro alinea "
 "la ORGANIZACION con el Modelo Estrella (estrategia, estructura, procesos, "
 "recompensas, personas). PAR MAS FUERTE DESCARTADO: el paso 1 de "
 "alineacion_ti_negocio (usa el Canvas para describir tu vision antes de "
 "definir que necesitas de tecnologia) contra el paso 1 del Modelo Estrella "
 "(definir la estrategia e identificar como impulsa el modelo de negocio). SE "
 "DESCARTA DOS VECES: ni uno procedimenta al otro, y ademas las dos apuntan a "
 "LA MISMA LINEA (partir de la estrategia del modelo), que es el separador "
 "literal del 9.22. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-008": ("D",
 "AQUI SI HAY DOS DIRECCIONES, Y POR ESO ESTE CASO IMPORTA: COLAPSAN EN UNA "
 "SOLA LINEA. Los seis pasos del dilema expanden el paso 5 de motivaciones "
 "(identifica si lo tuyo es el control o la riqueza), y los pasos 1 a 3 de "
 "motivaciones (influencias familiares, tus 4 motivaciones de una lista de 13 "
 "con una herramienta tipo CareerLeader, comparacion con perfiles tipicos) "
 "expanden los pasos 1 y 2 del dilema (reflexiona sobre que es mas importante "
 "para ti, preguntate si tu motivacion principal es la riqueza o el control). "
 "PERO EL PASO 5 DE MOTIVACIONES Y LOS PASOS 1 Y 2 DEL DILEMA SON LA MISMA "
 "LINEA: determinar si te mueve la riqueza o el control. El 9.22 lo excluye con "
 "todas sus letras. Y NINGUN OTRO PAR SOSTIENE LA FIGURA, comprobado: los "
 "pasos 3 a 6 del dilema (evaluar cuanto control pierdes en cada ronda, definir "
 "que no cedes, estructuras hibridas) no los expande motivaciones, y los pasos "
 "1 a 4 de motivaciones no los expande el dilema"),

"LD-OPC05-009": ("D",
 "MATERIAS DISTINTAS: uno es el METODO DE INTERPRETACION (recolectar, apartar "
 "tiempo, buscar patrones, armar una historia creible, unir objetivos que "
 "chocan) y el otro es el RITMO DEL PROCESO (divergir, poner deadline, embudo, "
 "polinizacion cruzada, alternar, matar a los hijos favoritos). PAR MAS FUERTE "
 "DESCARTADO: el paso 2 de analisis_y_sintesis (aparta un tiempo dedicado solo "
 "a organizar e interpretar) contra el paso 2 de convergente_divergente (fijar "
 "un deadline claro para la fase de divergencia): los dos acotan tiempo, pero "
 "acotan FASES DISTINTAS y ninguno es el como se hace del otro. NINGUN OTRO PAR "
 "SOSTIENE LA FIGURA"),

"LD-OPC05-010": ("D",
 "DOS CLAUSULAS PARALELAS DEL MISMO TERM SHEET, sin nido entre ellas. PAR MAS "
 "FUERTE DESCARTADO: el paso 3 de antidilucion (negociar una clausula de "
 "renuncia o waiver por mayoria de la Serie A, para cuando la mayoria acuerde "
 "financiar una ronda futura a precio menor) contra el paso 1 de pay to play "
 "(definir que constituye una Qualified Financing que gatilla la clausula): las "
 "dos tocan el mismo evento de ronda a la baja, pero cada una define SU PROPIA "
 "mecanica y ninguna procedimenta a la otra. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-012": ("D",
 "UNA SOLA DIRECCION. El paso 1 de gates_huecos (verificar que cada decision Go "
 "venga con compromiso explicito de recursos) SI lo expanden los cinco pasos de "
 "asignacion_recursos_en_gates (mostrar la lista de proyectos activos con sus "
 "compromisos, elegir metodo de seguimiento, verificar disponibilidad real, no "
 "agregar sin resolver implicaciones, comprometerse en la reunion). PAR MAS "
 "FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 4 de asignacion (evitar "
 "agregar proyectos a la lista activa sin resolver las implicaciones de "
 "recursos) contra el paso 3 de gates_huecos (eliminar la practica de aprobar "
 "proyectos en principio sin asignacion real): es LA MISMA LINEA dicha dos "
 "veces, no una expansion. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
 "CONTINUA"),

"LD-OPC05-013": ("D",
 "MEDIR CONTRA ESCRIBIR, y ninguna direccion cierra. PAR MAS FUERTE "
 "DESCARTADO: el paso 2 de desarrollar_posicionamiento (comparar la descripcion "
 "de la empresa con la de sus competidores) contra el paso 5 de la auditoria "
 "(comparar percepciones externas vs internas): las dos comparan, pero COSAS "
 "DISTINTAS, y una comparacion de otro par de objetos no es el como se hace de "
 "la primera. Y en la otra direccion ninguno de los cinco pasos de la auditoria "
 "esta expandido por los cinco de desarrollar. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-015": ("D",
 "A LO SUMO UNA DIRECCION, Y DEBIL. El paso 5 de entrada_mercado_nuevo (evaluar "
 "que evitara que un competidor con mas recursos tome el mercado una vez "
 "creado) lo roza el brief competitivo (como definen la base de la competencia, "
 "que te hace dramaticamente diferente, la razon de compra). PAR MAS FUERTE "
 "DESCARTADO EN LA OTRA DIRECCION: el paso 3 del brief (si tu mercado es nuevo, "
 "evalua que hace hoy la gente sin tu producto) contra los pasos 1 a 3 de "
 "entrada (identificar mercados adyacentes, articular la vision, estimar el "
 "presupuesto de educacion del mercado): identificar de donde vendran los "
 "primeros clientes NO es el como se averigua que hace hoy la gente sin tu "
 "producto. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-016": ("D",
 "MATERIAS DISTINTAS: la diana prueba CANALES con experimentos baratos y elige "
 "el canal nucleo; el camino critico enumera HITOS y excluye lo que no es "
 "imprescindible. PAR MAS FUERTE DESCARTADO: el paso 5 de bullseye (elige el "
 "canal con mejores resultados y concentra ahi la mayoria de tus recursos) "
 "contra el paso 2 de critical_path (excluye actividades que no sean "
 "absolutamente necesarias, aunque las pidan usuarios): las dos son reglas de "
 "foco, PARALELAS y sobre objetos distintos (canales contra hitos), y ninguna "
 "procedimenta a la otra. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-018": ("D",
 "DISCUTIBLE, Y LO MARCO YO: ES EL CASO MAS CERRADO DE ESTE TRAMO. UNA "
 "DIRECCION LIMPIA: el paso 1 de scenarios (identifica dos o mas impulsores de "
 "incertidumbre clave que puedan transformar tu industria) lo expanden los seis "
 "pasos del mapeo del entorno (fuerzas de mercado, fuerzas de industria, "
 "tendencias regulatorias y tecnologicas, macroeconomia, preguntas por bloque, "
 "stakeholders). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 5 del "
 "mapeo (formular preguntas estrategicas por cada bloque del Canvas EN BASE A "
 "LOS HALLAZGOS del entorno) contra el paso 4 de scenarios (taller donde se "
 "desarrolla un modelo de negocio por escenario y se formulan preguntas "
 "especificas por bloque KP, KA, VP, CR, CS, C$, R$). SE DESCARTA POR EL "
 "INSUMO: el paso 4 de scenarios procedimenta esas preguntas PARA CADA "
 "ESCENARIO, no para los hallazgos del entorno, y un procedimiento que contesta "
 "otro insumo no es la expansion de esa linea. UNA SOLA DIRECCION ES MADRE E "
 "HIJO Y EL PAR CONTINUA"),

"LD-OPC05-021": ("D",
 "MATERIAS DISTINTAS: uno mide la BRECHA entre diseno y produccion, el otro "
 "cuantifica el COSTO en cuatro categorias. PAR MAS FUERTE DESCARTADO: el paso "
 "4 de calidad_de_diseno (investigar causas raiz de las desviaciones, no solo "
 "los sintomas) contra el paso 1 del COPQ (identificar y categorizar todos los "
 "costos de fallos internos, externos, evaluacion y prevencion): categorizar "
 "COSTOS no es el como se investigan CAUSAS. Y en la otra direccion, ninguno de "
 "los seis pasos del COPQ esta expandido por los cuatro del otro. NINGUN OTRO "
 "PAR SOSTIENE LA FIGURA"),

"LD-OPC05-022": ("D",
 "UN BLOQUE DEL CANVAS CONTRA UNA INSTANCIA DE CANAL. Nombrar un canal como "
 "ejemplo no es expandir la linea que lo nombra. PAR MAS FUERTE DESCARTADO: el "
 "paso 4 de canales (calcular costo-eficiencia de cada canal seleccionado) "
 "contra los pasos 2, 4 y 6 de eventos (empieza con un evento pequeno y de bajo "
 "costo, busca un espacio accesible para reducir gastos, manten el precio de "
 "entrada relativamente alto): esas son decisiones de costo DENTRO del evento, "
 "no el procedimiento para calcular la costo-eficiencia de un canal. Y el paso "
 "1 de canales (mapear las 5 fases del canal por segmento) no lo expande nada "
 "de eventos. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-024": ("D",
 "UNA SOLA DIRECCION. El paso 4 de mejora_continua (verificar que las pruebas "
 "del producto final esten en control estadistico) SI lo expanden los pasos 1 a "
 "3 de causas (recopilar en orden cronologico, graficar en carta de control y "
 "calcular limites, aplicar reglas de senal). PAR MAS FUERTE DESCARTADO EN LA "
 "OTRA DIRECCION: el paso 7 de causas (si la causa es del sistema, redisenar el "
 "proceso en lugar de sancionar al individuo) contra el paso 3 de mejora "
 "(trabajar en procesos, materiales y componentes en lugar de solo medir "
 "resultados finales): es un PRINCIPIO dicho al mismo nivel de abstraccion o "
 "mas arriba, no un procedimiento que lo expanda. UNA SOLA DIRECCION ES MADRE E "
 "HIJO Y EL PAR CONTINUA"),

"LD-OPC05-025": ("D",
 "CONSTRUIR CONTRA DESMONTAR CREENCIAS, y ninguna direccion cierra. PAR MAS "
 "FUERTE DESCARTADO: el paso 2 de mitos (confirmar que existan flexibilidad y "
 "posibilidad de saltar u omitir etapas segun el riesgo) contra el paso 5 del "
 "checklist (crear versiones escalables del proceso segun el riesgo y tamano "
 "del proyecto): estan AL MISMO NIVEL DE ABSTRACCION, los dos dicen adapta el "
 "proceso al riesgo, y una linea igual de general no expande a la otra. En la "
 "otra direccion, ninguno de los siete pasos del checklist esta expandido por "
 "los cinco de mitos. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-028": ("D",
 "NOMBRAR LA SESION NO ES PROCEDIMENTAR LA REGLA QUE LA DISPARA. PAR MAS FUERTE "
 "DESCARTADO: el paso 3 del master (definir una regla simple e inequivoca sobre "
 "que incidentes disparan automaticamente una sesion de Cinco Porques) contra "
 "los siete pasos de five_whys: la ACCION de esa linea es DEFINIR LA REGLA DE "
 "DISPARO, y la sesion aparece solo como objeto nombrado; el 9.6.4 y la 6.4 "
 "excluyen la mencion. SEGUNDO PAR DESCARTADO: el paso 5 de five_whys (revisar "
 "despues si el problema se repitio para validar la efectividad) contra el paso "
 "5 del master (evaluar periodicamente si las inversiones de prevencion estan "
 "reduciendo frecuencia y severidad): misma linea dicha dos veces. NINGUN OTRO "
 "PAR SOSTIENE LA FIGURA"),

"LD-OPC05-033": ("D",
 "ACTITUDES CONTRA ETAPAS. Los cuatro pasos de la concepcion hormica son todos "
 "evitar, permitir, reconocer y dejar de exigirse: son POSTURAS, no "
 "procedimientos, y una postura no expande una linea. PAR MAS FUERTE "
 "DESCARTADO: el paso 2 de Wallas (incubacion, alejate deliberadamente del "
 "problema sin forzar una solucion) contra el paso 2 de la hormica (permitir "
 "que distintas partes del pensamiento actuen de forma semi independiente): la "
 "hormica enuncia la PRECONDICION que la incubacion supone, y precondicion no "
 "cuenta bajo la 6.4. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-034": ("D",
 "MATERIAS DISTINTAS: datos personales y emocionales del cliente contra el "
 "redisenio de dieciseis pasos de los procesos internos. PAR MAS FUERTE "
 "DESCARTADO: el paso 1 de conexion (clasifica los datos que tienes de tus "
 "clientes en personales, emocionales o ambos) contra los pasos 8 y 9 del "
 "redisenio (unificar y consolidar las herramientas internas de informacion del "
 "cliente): las dos tocan datos de cliente, pero una CLASIFICA TIPOS DE DATO y "
 "la otra CONSOLIDA HERRAMIENTAS, y ninguna es el como se hace de la otra. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-036": ("D",
 "UNA SOLA DIRECCION. El paso 4 de contacto_con_el_cliente (reconocer que toda "
 "la organizacion, vea o no al cliente, contribuye a la calidad del servicio) "
 "SI lo expanden los pasos 2, 6 y 7 del redisenio (ensena a todas las personas "
 "cual es su papel, diagnostica si los empleados saben que la experiencia es "
 "parte de su trabajo, disena un programa de capacitacion peer to peer con "
 "plazos). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 2 del "
 "redisenio contra el paso 3 de contacto (capacitar especificamente a los "
 "contact men en manejo de clientes): contacto cubre SOLO al personal de "
 "contacto, que es un subconjunto, y lo dice al mismo nivel (capacitar), asi "
 "que no lo expande. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-037": ("D",
 "CONSUMIR UNA SALIDA NO ES EXPANDIR UNA LINEA. PAR MAS FUERTE DESCARTADO: el "
 "paso 4 de contract_close_out (documentar el analisis de desempeno del "
 "proveedor y el registro de cambios) contra los pasos 2 y 3 del "
 "contractor_status_report (revisar desempeno de alcance, calidad, cronograma y "
 "costo del periodo; analizar pronosticos de fecha y costo final): el informe "
 "periodico es el INSUMO del cierre, no su procedimiento. Y en la otra "
 "direccion, el paso 5 del informe (integrar la informacion en el Informe de "
 "Desempeno del Proyecto) no lo expande el cierre. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-039": ("D",
 "DISCUTIBLE, Y LO MARCO YO. UNA DIRECCION LIMPIA: el paso 2 de definiciones "
 "operacionales (definir una prueba especifica y REPRODUCIBLE para evaluar el "
 "concepto) lo expanden los seis pasos del control estadistico del metodo de "
 "medicion (mediciones repetidas en R-chart, limites de control, comparacion "
 "entre operadores, entre instrumentos, criterios de reproducibilidad, rechazo "
 "del metodo). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 5 del "
 "control estadistico (establece criterios de reproducibilidad aceptable antes "
 "de iniciar las pruebas) contra los pasos 3 y 4 de definiciones (establecer un "
 "criterio de juicio claro y cuantificable, definir la regla de decision si o "
 "no). SE DESCARTA POR EL OBJETO: el criterio de definiciones es para LA "
 "CARACTERISTICA DE CALIDAD y el del control estadistico es para LA "
 "REPRODUCIBILIDAD DEL METODO, y ademas los dos estan al mismo nivel. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-042": ("D",
 "DISCUTIBLE, Y LO MARCO YO, POR SEGUNDA VEZ EN ESTE PAR. UNA DIRECCION SE "
 "SOSTIENE: el paso 1 de la rejilla (reune informacion objetiva sobre el estado "
 "actual de la gestion de calidad) lo expande el COPQ, que produce justo una de "
 "esas cifras objetivas. PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el "
 "paso 5 del COPQ (usa el resultado para decidir si invertir en mejora de "
 "calidad en vez de recortar costos que danen el servicio) contra los pasos 4 y "
 "5 de la rejilla (compara la etapa actual con la siguiente para identificar "
 "acciones concretas, disena un plan de transicion). SE DESCARTA POR EL INSUMO: "
 "la rejilla decide a partir de la ETAPA DE MADUREZ, no a partir del resultado "
 "del COPQ, y un procedimiento que arranca de otro insumo no expande esa linea. "
 "SEGUNDO PAR DESCARTADO: el paso 3 del COPQ (comparar contra benchmarks de la "
 "industria) contra el paso 2 de la rejilla (ubicar tu negocio en una de las "
 "cinco etapas): el nodo de la rejilla NO dice que sus etapas traigan cifras de "
 "COPQ, y leer eso seria leer el libro y no el nodo. UNA SOLA DIRECCION ES "
 "MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-045": ("D",
 "UNA SOLA DIRECCION. El paso 2 de Wallas (incubacion, alejate deliberadamente "
 "del problema) SI lo expanden los pasos 2 a 5 de ruptura_de_habitos (altera tu "
 "rutina cambiando horario, lugar o actividad; reduce el consumo de informacion "
 "rutinaria; busca experiencias nuevas mientras sigues pensando en el problema; "
 "alterna entre modos de trabajo). PAR MAS FUERTE DESCARTADO EN LA OTRA "
 "DIRECCION: el paso 1 de ruptura (vigilar senales de rigidez, estancamiento o "
 "mecanizacion en tu propio pensamiento) contra el paso 6 de Wallas (anota en "
 "que etapa esta cada idea, preparacion, incubacion, iluminacion o "
 "verificacion): anotar la ETAPA de una idea no es el como se detecta la "
 "RIGIDEZ; son dos observaciones distintas. UNA SOLA DIRECCION ES MADRE E HIJO "
 "Y EL PAR CONTINUA"),

"LD-OPC05-046": ("D",
 "SANO SIN FIGURA ES D, Y ADEMAS EL MEJOR PAR COLAPSA. PAR MAS FUERTE "
 "DESCARTADO: el paso 2 de cultura_de_seguridad (establecer un sistema que "
 "recolecte, analice y difunda informacion de incidentes) contra el paso 1 de "
 "cultura_de_aprendizaje (establecer mecanismos formales de analisis de datos "
 "del sistema de reporte de seguridad, con forma sistematica de observar "
 "incidentes y momentos regulares para analizar): son LA MISMA LINEA dicha en "
 "los dos nodos, que es el separador literal del 9.22. SEGUNDO PAR DESCARTADO: "
 "el paso 1 de cultura_de_seguridad (evaluar los cuatro subcomponentes) contra "
 "el nodo entero de aprendizaje, que ES uno de esos cuatro: relacion de parte a "
 "todo, no de linea a procedimiento. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-048": ("D",
 "PAR MAS FUERTE DESCARTADO, Y COLAPSA: el paso 3 del SIPOC (identificar "
 "clientes y las salidas que responden a sus necesidades) contra el paso 2 de "
 "la hoja de necesidades (lista en la primera columna a tus clientes, internos "
 "y externos, en orden de prioridad): las dos ENUMERAN CLIENTES, o sea la misma "
 "linea, y el 9.22 lo excluye. Y en la otra direccion los cinco pasos del SIPOC "
 "(definir el proceso, proveedores e insumos, clientes y salidas, cinco a ocho "
 "pasos mayores, validar con las funciones clave) no expanden ninguna linea de "
 "la hoja, que correlaciona clientes con NECESIDADES y no con salidas. NINGUN "
 "OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-050": ("D",
 "UNA SOLA DIRECCION. El paso 2 de decision_pivotar_o_proceder (confirma que la "
 "llegada de clientes es predecible, escalable y RENTABLE) SI lo expanden los "
 "seis pasos de validar_modelo_financiero (costo de producto y mercado, CAC y "
 "LTV, costos operativos y margenes, precio promedio e ingresos, runway, P and "
 "L multianual). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 1 de "
 "validar (recopilar metricas de valor propuesto: costo de producto, tamano de "
 "mercado, cuota alcanzable) contra el paso 4 de pivotar (toma un Canvas nuevo "
 "y busca game changers revisando propuesta de valor, precios, canales): "
 "rehacer el Canvas no es el como se recopilan metricas. UNA SOLA DIRECCION ES "
 "MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-051": ("D",
 "UNA SOLA DIRECCION. El paso 3 de defensas_en_profundidad (implementar "
 "mecanismos de deteccion temprana de fallas latentes antes de que se acumulen) "
 "SI lo expanden los pasos 2, 3, 4 y 6 de fallas_activas (buscar las decisiones "
 "previas que crearon condiciones latentes, tabla que separa activas de "
 "latentes, rastrear el origen hasta la decision gerencial, mantener un "
 "registro para monitorearlas de forma continua). PAR MAS FUERTE DESCARTADO EN "
 "LA OTRA DIRECCION: el paso 5 de fallas_activas (priorizar la correccion de "
 "condiciones latentes por su impacto en futuros eventos) contra los pasos 6 y "
 "7 de defensas (identificar funciones defensivas ausentes o debiles, disenar "
 "redundancia entre capas): eso es EL REMEDIO, no el como se PRIORIZA. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-052": ("C",
 "LA CLASE VUELVE DE D A C Y ES CORRECCION DE MI PROPIO VEREDICTO DEL LOTE 1 DE "
 "LA VUELTA 157. ES LA SEGUNDA DE LA MISMA ESPECIE QUE LA 005: la lectura "
 "anterior descarto la figura por la impresion de que uno alinea y el otro "
 "balancea, sin recorrer el espacio de pares que la 6.3 del acta 158 obliga a "
 "recorrer. HAY DOS LINEAS DISTINTAS Y CADA UNA LA EXPANDE UN PROCEDIMIENTO DEL "
 "OTRO NODO. LINEA 1, en definicion_alineacion_cadena_suministro, paso 3: "
 "DEFINIR SI TU ESTRATEGIA COMPETITIVA SE BASA EN PRECIO BAJO (requiere "
 "eficiencia) O EN SERVICIO Y CONVENIENCIA (requiere capacidad de respuesta); "
 "la expanden los pasos 1, 2, 3 y 7 de trade_off_responsividad_eficiencia "
 "(analizar que valora mas tu segmento, evaluar el exceso de capacidad, "
 "inventario y flexibilidad de transporte actuales, ajustar cada driver hacia "
 "el extremo del espectro, determinar si el entorno es estable o volatil). "
 "LINEA 2, en trade_off_responsividad_eficiencia, paso 1: ANALIZAR QUE VALORA "
 "MAS TU SEGMENTO DE CLIENTES, precio bajo o rapidez y servicio; la expande el "
 "paso 8 de alineacion, que es un instrumento nombrado y de seis dimensiones "
 "(responder las 6 preguntas de Chopra y Meindl sobre tu mercado: cantidad por "
 "lote, tiempo de respuesta, variedad, nivel de servicio, precio y tasa de "
 "innovacion). LAS DOS LINEAS SON DISTINTAS: una DECIDE TU ESTRATEGIA y la otra "
 "MIDE LA PREFERENCIA DEL MERCADO, verbos y sujetos distintos, asi que no hay "
 "colapso del 9.22. EL PAR QUE SI COLAPSA Y QUE POR ESO SE DESCARTA es el paso "
 "3 de trade_off (ajustar cada driver hacia el extremo del espectro) contra el "
 "paso 4 de alineacion (alinear produccion, inventario, ubicacion y transporte "
 "con la estrategia elegida, que son los 5 drivers): esa si es la misma linea, "
 "y descartarla no descarta la figura. VA MARCADA COMO DISCUTIBLE"),

"LD-OPC05-053": ("D",
 "LAS DOS DIRECCIONES COLAPSAN EN UNA SOLA LINEA. PAR MAS FUERTE DESCARTADO: el "
 "paso 2 de madurez_de_riesgo (identifica el escalon siguiente y UNA SOLA "
 "practica que te llevaria a el) contra el paso 1 de empieza_con_lo_que_ya_"
 "funciona (elige DOS O TRES practicas simples y probadas en vez de un modelo "
 "complicado): las dos son ELEGIR QUE PRACTICA ADOPTAR A CONTINUACION, la misma "
 "linea, y ademas se contradicen en el numero. SEGUNDO PAR DESCARTADO: el paso "
 "4 de empieza (sofistica el metodo solo cuando lo simple se te quede corto) "
 "contra el paso 3 de madurez (no intentes saltar al metodo perfecto, consolida "
 "un nivel antes de subir): otra vez la misma linea. NINGUN OTRO PAR SOSTIENE "
 "LA FIGURA"),

"LD-OPC05-054": ("D",
 "UNA SOLA DIRECCION. El paso 6 de desarrollo_presentacion_problema (anota el "
 "costo estimado del problema para el cliente, en tiempo, dinero o frustracion) "
 "SI lo expanden los pasos 3 y 4 de preguntas_ipo (preguntar casualmente cuanto "
 "le cuesta el problema en terminos monetarios o de tiempo, y registrar la "
 "respuesta). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 4 de IPO "
 "(registrar la respuesta para usarla luego en la presentacion de validacion) "
 "contra los siete pasos de la presentacion: la presentacion es DONDE SE USA la "
 "respuesta, y usar una salida no expande la linea que la registra. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-057": ("D",
 "NI UNA DIRECCION. PAR MAS FUERTE DESCARTADO: el paso 3 del dia de cero "
 "defectos (explica el programa a todos EL MISMO DIA) contra el paso 2 de "
 "entrenamiento_supervisores (explica de forma completa el programa ZD y el "
 "metodo de eliminacion de causas a quienes te ayudan, AL MENOS 4 SEMANAS ANTES "
 "del dia ZD): el verbo es el mismo pero el PUBLICO y el MOMENTO son otros, y "
 "una accion paralela sobre otro publico no es el como se hace de la primera. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-058": ("D",
 "A LO SUMO UNA DIRECCION, Y DEBIL. Los pasos 2 a 4 de terminologia_clave "
 "(diferenciar sintomas de causas, aplicar Pareto para la causa dominante, "
 "documentar teorias antes de validarlas) rozan el paso 1 de "
 "diagnostico_antes_remedio (no aplicar ningun remedio sin evidencia validada "
 "de la causa real). PAR MAS FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 4 "
 "de terminologia (documentar teorias propuestas antes de validarlas con datos) "
 "contra el paso 4 de diagnostico (usar datos historicos parecidos a estudios "
 "de fallas para validar tus hipotesis): el primero DOCUMENTA y el segundo "
 "VALIDA; son acciones adyacentes y distintas, no una expansion. UNA SOLA "
 "DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-059": ("D",
 "LAS DOS DIRECCIONES COLAPSAN. PAR MAS FUERTE DESCARTADO: el paso 2 del puzzle "
 "(evalua si tus decisiones estan priorizando el control por encima de "
 "maximizar el valor financiero) contra los pasos 1 y 2 del dilema (reflexiona "
 "sobre que es mas importante para ti, preguntate si tu motivacion principal es "
 "la riqueza o el control): misma linea, y el 9.22 lo excluye. Y LO QUE QUEDA "
 "DEL PUZZLE NO ES PROCEDIMIENTO: sus otros dos pasos son un ARGUMENTO EMPIRICO "
 "(cuestiona la suposicion de que fundar te hace mas rico) y una ACTITUD "
 "(acepta el costo de oportunidad conscientemente), y ni argumento ni actitud "
 "expanden una linea del dilema. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-060": ("D",
 "UNA INSTANCIA CONTRA SU CATEGORIA. PAR MAS FUERTE DESCARTADO: el paso 3 de "
 "diseno_intencional (incluir revisiones eticas como parte del proceso de "
 "prototipado e iteracion) contra los cuatro pasos de diseno_etico_de_privacidad "
 "(enumerar datos sensibles, disenar opt-out reales, evaluar el trade-off de "
 "conveniencia, comunicar quien se beneficia): privacidad es UN TEMA de revision "
 "etica, un ejemplar, y un ejemplar no es el procedimiento general de la linea. "
 "En la otra direccion, el paso 2 de intencional (evaluar si los efectos "
 "secundarios son deseados o accidentales) no lo procedimenta privacidad, que "
 "solo cubre un efecto. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-061": ("D",
 "MATERIAS DISTINTAS: la carpeta documental del embarque contra las polizas de "
 "carga y de credito. PAR MAS FUERTE DESCARTADO: el paso 1 del seguro "
 "(determinar segun terminos de venta quien es responsable del seguro de carga) "
 "contra el paso 3 de documentacion (emite la factura comercial incluyendo los "
 "TERMINOS DE VENTA y pago): la factura REGISTRA los terminos, y registrar un "
 "dato no es el como se determina una responsabilidad. NINGUN OTRO PAR SOSTIENE "
 "LA FIGURA"),

"LD-OPC05-062": ("D",
 "NOMBRAR AL MISMO ACTOR NO ES EXPANDIR. PAR MAS FUERTE DESCARTADO: el paso 4 "
 "de documentacion (verifica el codigo HS y DELEGA la preparacion en un agente "
 "de carga o un agente aduanal) contra el paso 1 de seleccion_metodo_transporte "
 "(CONSULTA con un freight forwarder internacional para determinar el mejor "
 "metodo de envio): los dos nombran al freight forwarder, pero uno le delega "
 "documentos y el otro le consulta el modo de transporte, y ninguno procedimenta "
 "al otro. NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-063": ("D",
 "DISCUTIBLE, Y LO MARCO YO. LAS DOS DIRECCIONES CAEN SOBRE LA MISMA LINEA: "
 "CUANDO PRESENTAR LA SOLUCION. PAR MAS FUERTE DESCARTADO: el paso 6 de "
 "modelo_spin_preguntas (presenta tu solucion recien cuando el cliente haya "
 "articulado la Necesidad Explicita) contra los pasos 1 y 4 de "
 "ecuacion_de_valor (mapear que tan grande percibe el cliente su problema; solo "
 "entonces presentar la solucion y su costo, cuando la balanza de valor ya se "
 "inclino): es el mismo criterio dicho con otras palabras. SEGUNDO PAR "
 "DESCARTADO: los pasos 2 y 3 de ecuacion (usar preguntas de Implicacion, usar "
 "preguntas de Necesidad-Beneficio) contra los pasos 3 y 4 del modelo (desarrolla "
 "preguntas de Implicacion, cierra con preguntas de Necesidad-Beneficio): mismo "
 "nivel de abstraccion, repeticion y no expansion. NINGUN OTRO PAR SOSTIENE LA "
 "FIGURA"),

"LD-OPC05-064": ("D",
 "UNA SOLA DIRECCION. El paso 1 de responsabilidad_gerencial (comprometerte a "
 "aprender de primera mano la filosofia y los metodos de calidad) SI lo "
 "expanden los cinco pasos de educacion_estadistica (disenar la capacitacion "
 "para ti y para cada persona, formacion practica en cartas de control, "
 "extender a muestreo, alianzas con instituciones). PAR MAS FUERTE DESCARTADO "
 "EN LA OTRA DIRECCION: el paso 1 de educacion (disenar una capacitacion en "
 "metodos estadisticos para ti y para cada persona) contra los pasos 1 y 2 de "
 "responsabilidad (comprometerte a aprender, asumir tu mismo el liderazgo de "
 "las mejoras): eso es la PRECONDICION ACTITUDINAL que la capacitacion supone, "
 "y precondicion no cuenta bajo la 6.4. UNA SOLA DIRECCION ES MADRE E HIJO Y EL "
 "PAR CONTINUA"),

"LD-OPC05-065": ("D",
 "PAR MAS FUERTE DESCARTADO, Y COLAPSA: el paso 1 de ejecucion_auditoria "
 "(confirma cada hallazgo con la persona responsable de esa area ANTES de "
 "escribirlo en el reporte) contra el paso 5 de relaciones_humanas (realizar "
 "una reunion post auditoria para validar hallazgos con el equipo auditado): "
 "las dos VALIDAN LOS HALLAZGOS CON EL AUDITADO, la misma linea, y el 9.22 lo "
 "excluye. En la otra direccion, ni el paso 2 de relaciones (evitar la busqueda "
 "de culpables) ni el 3 (incluir observaciones positivas) los expande ejecucion. "
 "NINGUN OTRO PAR SOSTIENE LA FIGURA"),

"LD-OPC05-066": ("D",
 "DISCUTIBLE, Y LO MARCO YO. UNA DIRECCION SE SOSTIENE: el paso 3 de "
 "el_riesgo_eres_tu (escribe que pasa con tus clientes si no puedes trabajar "
 "por dos semanas y como se les avisaria) lo expanden los pasos 1, 3 y 4 de "
 "sigue_operando (define las pocas funciones que no pueden parar, decide de "
 "antemano que puede esperar, avisa a tus clientes con honestidad). PAR MAS "
 "FUERTE DESCARTADO EN LA OTRA DIRECCION: el paso 2 de sigue_operando (para "
 "cada funcion critica, piensa como la sostendrias con lo minimo si el resto "
 "esta en crisis) contra los pasos 1 y 2 de el_riesgo_eres_tu (documenta en un "
 "solo lugar donde vive todo; nombra un contacto de emergencia y dale acceso "
 "seguro). SE DESCARTA POR EL MODO DE FALLO: esos dos pasos contestan al "
 "FUNDADOR AUSENTE, no al RESTO EN CRISIS, y ademas documentar donde vive todo "
 "es la PRECONDICION de la continuidad, no el procedimiento de sostener una "
 "funcion con lo minimo. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),
}


def main():
    ids = json.load(io.open(NOMINA, encoding="utf-8"))["tramo"]
    return motor.aplicar(
        "VUELTA 159, TAREA 2.b: EL TRAMO RELEIDO AL DOBLE, 41 SEGUNDAS LECTURAS",
        V, MARCA, cabeza, nota_md, ids_esperados=ids)


if __name__ == "__main__":
    raise SystemExit(main())
