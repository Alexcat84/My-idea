# -*- coding: utf-8 -*-
"""vuelta160_tarea2b_tramo_al_doble.py . TAREA 2.b Y 2.c DE LA VUELTA 160.

LAS 37 DEL LOTE 2 QUE NADIE HA VUELTO A MIRAR, SEGUNDA PASADA INDEPENDIENTE
(adjudicacion 6.4 del acta 159), leidas una a una CONTRA LOS NODOS con el
dossier `docs/loop/SALIDA_V160_T2B_DOSSIER.txt` delante. La nomina la sella
`vuelta160_tarea2b_nomina_tramo.py` en `docs/loop/NOMINA_V160_TRAMO.json` y este
instrumento la exige.

POR QUE VAN LAS 37 ENTERAS Y NO SOLO LAS QUE CAYERON A D: la discrepancia que
abrio la bajada de credito, la `LD-OPC05-100`, es una que SOSTUVO C, asi que
restringir el tramo a las caidas dejaria fuera justo la especie que lo disparo.
El tramo lleva 8 en C y 29 en D y se relee entero.

LA VARA ES LA 6.4 DEL ACTA 157 CON LA CORRECCION DE LA 6.3 DEL ACTA 158:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

y ESO ES UN EXISTENCIAL: un par que colapsa descarta ESE PAR, no el nodo. Por
eso CADA UNA de las 37 razones NOMBRA EL PAR MAS FUERTE QUE SE DESCARTO y dice
por que no sostiene la figura.

--- LA 2.c, LA AUDITORIA DE CONSISTENCIA DE LA REGLA DE LA INSTANCIA ---

Por la adjudicacion 6.5.b del acta 159. En CADA UNA de las 37 se declara el
estado de la regla UNA INSTANCIA NO ES EL PROCEDIMIENTO DE SU CATEGORIA, y se
declara en TRES estados, no en dos, porque dos no alcanzan para auditar:

  APLICA                  la regla es motivo (solo o acompanado) del descarte de
                          algun par de esta lectura.
  NO APLICA PUDIENDO      la figura de instancia y categoria ESTA a la vista (dos
  PARECER QUE SI          hermanos de una misma clase, un nodo que parece
                          ejemplar del otro) y aun asi la regla NO decide nada
                          aqui, y se dice por que. ESTE ES EL ESTADO QUE HACE
                          AUDITABLE A LA REGLA: sin el, solo se veria donde
                          conviene aplicarla.
  NO SE PLANTEA           no hay ninguna linea de categoria ni ningun parecido de
                          ejemplar en el par.

Y LA CONDICION (a) DE LA 6.5 SE APLICA CON SU LETRA: cuando la regla es el UNICO
motivo del descarte, la razon lo dice con esa letra y la fila QUEDA MARCADA COMO
DISCUTIBLE. Cuando hay un segundo motivo que se sostiene solo, se dice tambien,
y esa fila NO queda marcada por esta via. La diferencia se publica.

--- LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO ---

Dos familias, y se distinguen:
  (i)  las SIETE que la 6.5.a obliga a marcar;
  (ii) las OCHO que marco YO por duda propia, porque aceptaria un veredicto
       distinto si el auditor lo argumenta.
Quince en total sobre 37. Es mucho y se dice: este tramo se lee con la vara
recien estrechada por la `100`, y una vara recien estrechada produce mas dudas
honestas que una vieja.

--- LAS GUARDAS ---

Son las de la 2.d y viven en `vuelta159_motor_veredictos.py`, QUE ES LA FUENTE
UNICA Y NO SE CLONA: frontera con sha256 de `dataset/`, censo y aristas antes y
despues, `n` en 3.388, prefijo intacto en las 154 razones, ningun par movido y
NINGUNA CLASE A `A` (limite de la 6.1 del acta 155: la que salga A no se voltea,
se marca y no se ejecuta ninguna fusion). NINGUNA SALIO A.

USO:  python scripts/loop/vuelta160_tarea2b_tramo_al_doble.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta159_motor_veredictos as motor  # noqa: E402

RAIZ = motor.RAIZ
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V160_TRAMO.json")

MARCA = "SEGUNDA PASADA DEL TRAMO AL DOBLE, VUELTA 160"

APLICA = "APLICA"
PARECE = "NO APLICA PUDIENDO PARECER QUE SI"
NO_PLANTEA = "NO SE PLANTEA"


def cabeza(vieja, nueva):
    if nueva != vieja:
        return ("  [CORRECCION DECLARADA, %s (2026-09-03), ANADIDA SIN BORRAR "
                "NADA DE LO ANTERIOR: LA CLASE PASA DE %s A %s. " % (MARCA, vieja, nueva))
    return ("  [%s (2026-09-03), ANADIDA SIN BORRAR NADA DE LO ANTERIOR: LA "
            "CLASE SE SOSTIENE EN %s. " % (MARCA, vieja))


def nota_md(vieja, nueva, motivo):
    if nueva != vieja:
        return ("CORRECCION DECLARADA (vuelta 160, TRAMO AL DOBLE, adjudicacion "
                "6.4 del acta 159): la clase pasa de ~~%s~~ a %s. %s."
                % (vieja, nueva, motivo[:260]))
    return ("SEGUNDA PASADA DEL TRAMO AL DOBLE (vuelta 160): la clase SE "
            "SOSTIENE en %s y su caso queda escrito en la razon del registro de "
            "citas." % vieja)


# --------------------------------------------------------------------------
# LOS VEREDICTOS. {ld: (clase, motivo)}
# --------------------------------------------------------------------------

V = {
"LD-OPC05-068": ("C",
    "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. LINEA 1, en "
    "eliminar_metas_numericas_gerencia, paso 3: DETERMINAR LA CAPACIDAD REAL "
    "DEL SISTEMA MEDIANTE ANALISIS ESTADISTICO ANTES DE FIJAR CUALQUIER META; "
    "la expanden los cinco pasos de sistema_estable_causas_comunes, que son el "
    "metodo entero (recolectar datos diarios de defectos durante varias "
    "semanas, graficarlos en carta de corrida o de control, clasificar la "
    "variacion como causa comun o especial, y si el sistema es estable "
    "identificar que cambios estructurales mueven su capacidad). LINEA 2, en "
    "sistema_estable_causas_comunes, paso 5: EVITAR FIJAR METAS NUMERICAS O "
    "CULPAR A LA PERSONA HASTA HABER INTERVENIDO SOBRE EL SISTEMA MISMO; la "
    "expanden los pasos 1, 2 y 4 de eliminar_metas (revisar las metas actuales "
    "y verificar si cuentan con un plan de accion concreto, eliminar las que "
    "solo se basen en deseos o presion sin metodo definido, y reemplazar las "
    "arbitrarias por objetivos de mejora continua con planes especificos). DOS "
    "LINEAS DISTINTAS, UNA EN CADA NODO, CADA UNA EXPANDIDA POR UN "
    "PROCEDIMIENTO DEL OTRO, Y NINGUNO ES LA MADRE. PAR MAS FUERTE DESCARTADO: "
    "el paso 5 de eliminar_metas (reconocer el costo oculto de manejar tu "
    "negocio por miedo a los numeros) contra el paso 5 de sistema_estable, que "
    "SE DESCARTA porque las dos lineas colapsan en la misma advertencia y el "
    "9.22 las excluye. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA, no hay "
    "linea de categoria ni parecido de ejemplar en este par"),

"LD-OPC05-069": ("D",
    "LA D SE SOSTIENE. UNA SOLA DIRECCION, Y NI SIQUIERA ESA ES LIMPIA. Los "
    "dos nodos viven en la tabla de capital y por eso se rozan, pero el sujeto "
    "de employee_pool_esop es EL TAMANO Y EL REPARTO DE LA RESERVA frente al "
    "inversionista (negociar el porcentaje, definir si incluye opciones ya "
    "entregadas, calcular la dilucion sobre tu precio por accion, planear el "
    "reparto segun a quien contrataras) y el de vesting_acciones_fundadores es "
    "COMO SE CONSOLIDAN LAS ACCIONES EN EL TIEMPO (emision, 83(b), cliff de un "
    "ano con 25 por ciento, recompra de lo no adquirido, aceleracion de doble "
    "gatillo). PAR MAS FUERTE DESCARTADO: el paso 4 del pool (planea como vas a "
    "repartir esa reserva segun a quien piensas contratar) contra los pasos 3, "
    "8 y 9 de vesting (cronograma estandar, decidir si cada rol consolida por "
    "tiempo o tambien por desempeno, dejar por escrito las condiciones de cada "
    "persona). SE DESCARTA porque vesting dice COMO CONSOLIDA cada persona lo "
    "que ya recibio, y la linea pregunta CUANTO le toca a cada quien de la "
    "reserva: sujeto distinto. BAJO LA 6.3 SE RECORRIO EL RESTO DEL ESPACIO Y "
    "NINGUN OTRO PAR SOSTIENE LA FIGURA. REGLA DE LA INSTANCIA (6.5.b): NO SE "
    "PLANTEA"),

"LD-OPC05-071": ("D",
    "LA D SE SOSTIENE, Y LA DIRECCION QUE FALTA ES LA DE VUELTA. LA IDA SI "
    "TIENE CANDIDATO: el paso 4 de encuadre_desafio_diseno (documentar contexto "
    "y restricciones geograficas, tecnologicas, de tiempo y poblacionales) lo "
    "acompanan los pasos 1 y 2 de usuarios_extremos_globales (investigacion de "
    "campo en comunidades con restricciones extremas y documentar las "
    "limitaciones tecnologicas, linguisticas y economicas reales). LA VUELTA NO "
    "EXISTE: NINGUNA LINEA DE usuarios_extremos_globales ESTA EXPANDIDA POR UN "
    "PROCEDIMIENTO DE encuadre. PAR MAS FUERTE DESCARTADO EN ESA DIRECCION: el "
    "paso 4 de usuarios_extremos (evaluar si la solucion tiene potencial de "
    "aplicacion en otros sectores o mercados) contra los pasos 1 a 3 de "
    "encuadre (formular el problema como pregunta abierta Como podriamos, "
    "definir el impacto ultimo, listar posibles soluciones pensando "
    "ampliamente). SE DESCARTA porque encuadre ABRE UN DESAFIO NUEVO y corre "
    "ANTES de que exista solucion, mientras la linea evalua la "
    "transferibilidad de una solucion YA CONSTRUIDA: momento y sujeto "
    "distintos. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA. REGLA DE "
    "LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-072": ("D",
    "LA D SE SOSTIENE Y NO ES DUDOSA. enfoques_generales_exportacion decide TU "
    "POSTURA (si ya vendes de forma pasiva a compradores que exportan, si hay "
    "compradores domesticos que representan usuarios finales extranjeros, que "
    "nivel de involucramiento quieres) y programas_ex_im_bank tramita "
    "INSTRUMENTOS DE FINANCIAMIENTO (garantia de capital de trabajo, prestamo "
    "directo, seguro de credito, Bank Buyer Credit Policy, tasas de anticipo). "
    "Materias distintas. PAR MAS FUERTE DESCARTADO: el paso 1 de enfoques "
    "(identificar si la empresa ya vende de forma pasiva a compradores que "
    "exportan) contra el paso 3 de ex_im (evalua contratar un seguro de credito "
    "a la exportacion, propio o privado si ya tienes historial como exportador "
    "establecido). SE DESCARTA porque los dos miran tu historial exportador "
    "pero uno lo usa para CLASIFICAR TU POSTURA y el otro para CALIFICARTE ANTE "
    "UNA ASEGURADORA: mismo insumo, actos distintos, y eso no es expansion. "
    "BAJO LA 6.3 SE RECORRIO EL ESPACIO ENTERO. REGLA DE LA INSTANCIA (6.5.b): "
    "NO SE PLANTEA"),

"LD-OPC05-073": ("D",
    "LA D SE SOSTIENE. entrenamiento_supervisores_calidad forma al supervisor "
    "EN EL PROGRAMA CERO DEFECTOS (seis horas de estudio del sistema de "
    "medicion y los costos de calidad, explicar el programa cuatro semanas "
    "antes del dia ZD, manual de referencia, test de comprension) y "
    "identificacion_empleado_con_el_trabajo trabaja LA RELACION SUPERVISOR "
    "EMPLEADO (conocer a cada miembro, mostrar el resultado final de su "
    "trabajo, fomentar que comuniquen problemas, estandares de desempeno, "
    "seguimiento del ausentismo, autoevaluacion periodica). PAR MAS FUERTE "
    "DESCARTADO: el paso 6 de entrenamiento (verifica que cada persona refuerce "
    "la formacion en su area de responsabilidad) contra el paso 4 de "
    "identificacion (establecer estandares de desempeno claros y comprensibles "
    "para cada puesto). SE DESCARTA porque uno verifica el REFUERZO DE UNA "
    "FORMACION y el otro fija ESTANDARES DE DESEMPENO: sujetos distintos, y "
    "ademas el segundo no trae metodo, solo la orden. BAJO LA 6.3 SE RECORRIO "
    "EL ESPACIO ENTERO Y NINGUN OTRO PAR SOSTIENE LA FIGURA. REGLA DE LA "
    "INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-074": ("D",
    "LA D SE SOSTIENE, Y LA MARCO DISCUTIBLE POR DUDA PROPIA porque el par mas "
    "fuerte que descarto lo descarto POR COLAPSO y el colapso siempre admite "
    "una segunda lectura. PAR MAS FUERTE DESCARTADO: el paso 2 de "
    "teoria_de_juegos_en_negociacion (si es multi-ronda, priorizar la "
    "reputacion y evitar tacticas que generen represalias futuras) contra el "
    "paso 4 de estilos_de_negociacion (favorecer la transparencia y calma en "
    "negociaciones con valor reputacional a largo plazo). SE DESCARTA POR EL "
    "9.22: las dos lineas dicen LA MISMA COSA (en relaciones largas, cuida la "
    "reputacion y no uses tacticas que te devuelvan el golpe), y una linea que "
    "se repite no se expande. LOS OTROS PARES TAMPOCO: el paso 2 de estilos "
    "(adaptar la respuesta segun el arquetipo identificado) no lo expande "
    "teoria, porque teoria ramifica por TIPO DE JUEGO (una ronda o multi "
    "ronda) y no por ARQUETIPO DE PERSONA, que es otro insumo; y el paso 4 de "
    "teoria (preguntar a la contraparte cuales son sus 3 terminos mas "
    "importantes) no lo expande ninguna linea de estilos. REGLA DE LA "
    "INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-076": ("D",
    "LA D SE SOSTIENE POR UNA SOLA DIRECCION, Y LA MARCO DISCUTIBLE POR DUDA "
    "PROPIA porque la ida es fuerte y todo depende de la vuelta. LA IDA SI SE "
    "SOSTIENE: el paso 6 de estrategia_crecimiento_clientes (revisar tacticas "
    "especificas de canales web o moviles para identificar ideas adicionales de "
    "crecimiento) lo expanden los seis pasos de get_customers_funnel_webmobile, "
    "que son el procedimiento entero de esas tacticas. LA VUELTA NO SE "
    "SOSTIENE. PAR MAS FUERTE DESCARTADO: el paso 4 del embudo (probar primero "
    "tacticas de adquisicion gratuitas: PR, SEO, redes sociales, marketing "
    "viral) contra el paso 4 de estrategia_crecimiento (disenar mecanismos de "
    "marketing viral y programas de referidos que incentiven a los clientes "
    "actuales a invitar a nuevos). SE DESCARTA POR DOS MOTIVOS QUE SE SOSTIENEN "
    "CADA UNO SOLO, y por eso esta fila NO queda marcada por la 6.5.a: "
    "(1) REGLA DE LA INSTANCIA (6.5.b): APLICA. La linea del embudo enumera "
    "CUATRO tacticas gratuitas como categoria y el otro nodo procedimenta UNA "
    "de ellas; un ejemplar de la lista no es el procedimiento de la lista. "
    "(2) Y ademas el sujeto no calza: el embudo prueba tacticas para ADQUIRIR "
    "DESCONOCIDOS y la linea de crecimiento disena mecanismos para que los "
    "CLIENTES ACTUALES inviten, que es la etapa Grow y no la Get"),

"LD-OPC05-077": ("D",
    "LA D SE SOSTIENE. Son DOS CANALES DE TRACCION HERMANOS del mismo libro, y "
    "hermanos no es madre e hijo, que es exactamente el motivo con que la "
    "LD-OPC05-004 quedo en D. estrategia_plataformas_existentes construye UNA "
    "FEATURE DENTRO DE UNA PLATAFORMA AJENA (identificar donde se congregan tus "
    "clientes, ver que funcionalidad falta, disenar el complemento, priorizar "
    "plataformas nuevas, ser de los primeros, medir el trafico) y "
    "programa_afiliados monta UNA RED DE TERCEROS QUE COBRAN COMISION (elegir "
    "red existente o programa propio, definir la comision por debajo del costo "
    "de adquisicion, reclutar entre clientes actuales, expandir a creadores de "
    "contenido, medir conversion y ajustar). PAR MAS FUERTE DESCARTADO: el paso "
    "1 de plataformas (identificar en que plataformas online se congregan tus "
    "clientes potenciales) contra el paso 4 de afiliados (expandir reclutamiento "
    "a creadores de contenido relacionados con el nicho). SE DESCARTA porque "
    "los dos localizan a la audiencia pero uno para CONSTRUIR ALGO EN LA "
    "PLATAFORMA y el otro para RECLUTAR INTERMEDIARIOS: sujetos distintos. "
    "REGLA DE LA INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE SI, y lo "
    "declaro porque la figura esta a la vista: los dos nodos son ejemplares de "
    "los canales de traccion del mismo autor, y seria comodo cerrar con la "
    "regla. NO SE PUEDE: la regla pide una LINEA DE CATEGORIA en uno de los dos "
    "nodos, y ninguno tiene un paso que diga elige un canal de traccion. El "
    "descarte es por hermandad, no por instancia"),

"LD-OPC05-079": ("D",
    "LA D SE SOSTIENE, Y EL MOTIVO ES DE PRECEDENCIA. "
    "evaluacion_necesidad_franquiciar decide SI FRANQUICIAR (metas de "
    "crecimiento, si el capital basta, si hay prototipo probado, si los "
    "procesos se documentan y ensenan en menos de tres meses, el ROI del "
    "franquiciado, ventajas contra desventajas) y "
    "mix_ubicaciones_corporativas_franquicia decide COMO REPARTIR LOCALES UNA "
    "VEZ TOMADA ESA DECISION (Home Sweet Home, Spiking, Cherry Picking, "
    "criterios de asignacion de mercados, encroachment). PAR MAS FUERTE "
    "DESCARTADO: el paso 6 de evaluacion (compara las ventajas de franquiciar "
    "contra sus desventajas antes de decidir) contra los pasos 1 y 2 de mix "
    "(decide si continuaras abriendo locales corporativos en paralelo; analiza "
    "tu capital disponible y tu plan de salida). SE DESCARTA porque mix "
    "PRESUPONE YA TOMADA la decision de franquiciar: un nodo que empieza donde "
    "el otro termina no puede ser el como se hace de la decision que lo "
    "precede. Precedencia no es expansion. REGLA DE LA INSTANCIA (6.5.b): NO SE "
    "PLANTEA"),

"LD-OPC05-082": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE. PAR "
    "MAS FUERTE DESCARTADO: el paso 1 de iota_analysis (reunir todos los "
    "hallazgos de LOS EJERCICIOS ESTRATEGICOS PREVIOS en una tabla resumen) "
    "contra los seis pasos de future_scenarios_planning. SE DESCARTA porque la "
    "planificacion de escenarios ES UNO de esos ejercicios estrategicos "
    "previos: REGLA DE LA INSTANCIA (6.5.b): APLICA, Y ES EL UNICO MOTIVO. LA "
    "OTRA DIRECCION TAMPOCO SE SOSTIENE, y ahi el motivo es distinto y "
    "independiente: el paso 5 de escenarios (identifica las decisiones "
    "primarias, asigna una probabilidad pequena a los escenarios alternativos y "
    "reconsidera con ella tus decisiones de inversion) no lo expanden los pasos "
    "2 a 5 de IOTA, porque IOTA pone timing, probabilidad e impacto sobre "
    "TENDENCIAS, AMENAZAS Y OPORTUNIDADES sueltas y la linea los pide sobre "
    "ESCENARIOS COMPLETOS: unidad de analisis distinta"),

"LD-OPC05-083": ("D",
    "LA D SE SOSTIENE, Y EL MOTIVO ES QUE UN REMEDIO NO ES EL COMO SE HACE DE "
    "SU DIAGNOSTICO. gates_sin_dientes_problema DIAGNOSTICA (dibuja la curva de "
    "cuantos proyectos sobreviven cada filtro, revisa si casi ninguno se "
    "elimina temprano, identifica cuales de las 7 razones para no matar "
    "proyectos te estan pasando, evalua si tus filtros son decisiones de "
    "inversion o reuniones de seguimiento) y sistema_gates_go_kill INSTALA el "
    "sistema en diecisiete pasos. PAR MAS FUERTE DESCARTADO: el paso 4 del "
    "diagnostico (evalua si tus filtros funcionan como verdaderas decisiones de "
    "inversion o solo como reuniones de seguimiento) contra los pasos 4, 5 y 7 "
    "del sistema (detente y toma una decision explicita Go, Kill, Hold o "
    "Recycle; compromete recursos solo despues de pasar el gate; preguntate de "
    "verdad si sigues o si paras, no solo revises como va el proyecto). SE "
    "DESCARTA porque esos pasos DESCRIBEN EL ESTADO DESEADO, no el "
    "procedimiento de EVALUAR EL ESTADO ACTUAL, que es lo que la linea pide: la "
    "vara del diagnostico es el remedio, pero el remedio no es su metodo. Y la "
    "vuelta no existe: ninguna linea del sistema esta expandida por un "
    "procedimiento del diagnostico, cuyos cuatro pasos son de medicion propia. "
    "REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-086": ("D",
    "LA D SE SOSTIENE Y ES DE LAS CLARAS. gestion_instalaciones decide LA RED "
    "FISICA (rol de cada instalacion, capacidad optima evitando sobre o sub "
    "capacidad, asignar proveedores y mercados a cada instalacion considerando "
    "costos de transporte, impacto en la flexibilidad) y "
    "planificacion_cadena_suministro es EL PROCESO DE SOURCING de otro libro y "
    "otro dominio (documentar la actividad historica de compras, identificar "
    "commodities de alto gasto y criticidad, formar equipo cross-funcional, "
    "analizar la industria proveedora, calcular el costo total de propiedad, "
    "obtener respaldo de la direccion). PAR MAS FUERTE DESCARTADO: el paso 3 de "
    "instalaciones (asignar proveedores y mercados a cada instalacion) contra "
    "los pasos 2 y 4 de sourcing (identificar commodities de alto gasto y alta "
    "criticidad; analizar estructura y tendencias de la industria proveedora). "
    "SE DESCARTA porque sourcing elige QUE COMPRAR Y A QUIEN de forma "
    "estrategica y la linea reparte proveedores YA ELEGIDOS entre sitios "
    "fisicos: sujetos distintos. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-087": ("C",
    "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS, VERIFICADAS CONTRA LOS NODOS Y "
    "NO CONTRA LA FICHA. LINEA 1, en gestion_portafolio_dos_niveles, paso 1: "
    "ESTABLECER UN PROCESO DE GATING PARA REVISAR CADA PROYECTO "
    "INDIVIDUALMENTE; la expanden los diecisiete pasos de sistema_gates_go_kill, "
    "que son el procedimiento entero de ese proceso (definir los gates, fijar "
    "criterios visibles, checklist o scorecard, decision explicita Go, Kill, "
    "Hold, Recycle o Conditional Go, comprometer recursos solo despues, anotar "
    "la decision y el motivo, criterios eliminatorios, entregables estandar por "
    "gate). LINEA 2, en sistema_gates_go_kill, paso 10: CONECTA CADA PUNTO DE "
    "DECISION CON LA FORMA EN QUE ASIGNAS RECURSOS Y CON LA VISION GENERAL DE "
    "TUS PROYECTOS; la expanden los pasos 2, 3 y 4 de dos_niveles (establecer "
    "revisiones de portafolio trimestrales o semestrales que vean el conjunto "
    "completo, definir que decisiones son estrategicas y cuales tacticas, y "
    "usar ambos procesos de forma complementaria y no sustitutiva), que son "
    "literalmente el como se conecta el gate individual con la vision del "
    "conjunto. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE. PAR MAS FUERTE "
    "DESCARTADO: el paso 3 de dos_niveles (definir que decisiones son "
    "estrategicas y cuales tacticas) contra el paso 14 del sistema (decide "
    "quien sera la persona responsable de aprobar cada etapa), que SE DESCARTA "
    "porque uno reparte TIPOS DE DECISION y el otro asigna PERSONAS. REGLA DE "
    "LA INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE SI, y lo declaro: la "
    "frase establecer UN PROCESO DE GATING se lee como categoria y tentaria a "
    "cerrar con la regla. NO SE PUEDE, y el motivo es medible: el otro nodo no "
    "es UNO ENTRE VARIOS procesos de gating, es EL procedimiento completo del "
    "mismo autor y el mismo libro para ese proceso, que es el caso de la 052 y "
    "no el de la 122"),

"LD-OPC05-088": ("C",
    "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. LINEA 1, en "
    "gestion_portafolio_foco, paso 2: APLICAR CRITERIOS ESTRICTOS DE GO/KILL "
    "PARA REDUCIR EL NUMERO DE PROYECTOS EN PIPELINE; la expanden los pasos 2, "
    "3, 12 y 16 de sistema_gates_go_kill (establecer criterios claros y "
    "visibles de si el proyecto esta listo y si el negocio justifica seguir, "
    "crear un checklist o scorecard simple, crear una lista de criterios "
    "eliminatorios para descartar de entrada los inviables, y fijar criterios "
    "must-meet, go/kill financieros y should-meet cualitativos), que son "
    "exactamente EL COMO de aplicar criterios estrictos. LINEA 2, en "
    "sistema_gates_go_kill, paso 13: DECIDE COMO VAS A PRIORIZAR LOS PROYECTOS "
    "QUE SI CUMPLEN, DANDOLE MAS PESO A LO QUE MAS TE IMPORTA; la expanden los "
    "pasos 1, 3 y 5 de foco (auditar el numero de proyectos activos contra la "
    "capacidad real de recursos, priorizar los de mayor potencial estrategico y "
    "financiero, y revisar periodicamente el balance del portafolio por riesgo, "
    "tipo de innovacion y mercados). DOS LINEAS DISTINTAS Y NINGUNO ES LA "
    "MADRE. PAR MAS FUERTE DESCARTADO: el paso 4 de foco (evitar el "
    "multitasking excesivo del personal entre proyectos simultaneos) contra el "
    "paso 5 del sistema (comprometete recursos solo despues de pasar el gate), "
    "que SE DESCARTA porque uno protege LA ATENCION DE LAS PERSONAS y el otro "
    "regula EL MOMENTO DEL COMPROMISO DE RECURSOS. REGLA DE LA INSTANCIA "
    "(6.5.b): NO APLICA PUDIENDO PARECER QUE SI, por el mismo parecido que en "
    "la 087 y por el mismo motivo medible: el sistema de gates no es un "
    "ejemplar de una clase que la linea enumere, es el procedimiento completo "
    "del mismo autor"),

"LD-OPC05-089": ("D",
    "LA D SE SOSTIENE. PAR MAS FUERTE DESCARTADO: el paso 1 de get_visual "
    "(mantener post-its, papel y lapices siempre a mano durante todo el "
    "proceso) contra el paso 5 de reglas_brainstorming (usar Post-it notes o "
    "pizarra para capturar y mover las ideas visualmente). SE DESCARTA POR EL "
    "9.22: las dos lineas son la misma instruccion. SEGUNDO PAR MAS FUERTE, Y "
    "SE DESCARTA POR DOS MOTIVOS QUE SE SOSTIENEN CADA UNO SOLO, por lo que "
    "esta fila NO queda marcada por la 6.5.a: el paso 3 de brainstorming "
    "(establecer, visibilizar y hacer cumplir las reglas: diferir el juicio, "
    "una conversacion a la vez, mantenerse enfocado, cantidad antes que "
    "calidad, SER VISUAL, ideas locas, construir sobre las de otros) contra los "
    "cuatro pasos de get_visual. (1) EL VERBO DE LA LINEA NO ES SER VISUAL, ES "
    "ESTABLECER, VISIBILIZAR Y HACER CUMPLIR LAS REGLAS, y get_visual no "
    "procedimenta como se instalan ni se hacen cumplir unas reglas de sesion. "
    "(2) REGLA DE LA INSTANCIA (6.5.b): APLICA, porque tomando SER VISUAL "
    "suelta, es UNA de las siete reglas que la linea enumera y un ejemplar de "
    "la lista no es el procedimiento de la lista. La vuelta tampoco existe: "
    "ninguna linea de get_visual esta expandida por un procedimiento de "
    "brainstorming"),

"LD-OPC05-091": ("D",
    "LA D SE SOSTIENE, Y EL HALLAZGO QUE LA DECIDE ES QUE LA PALABRA RIESGO "
    "NOMBRA DOS COSAS DISTINTAS EN CADA NODO. PAR MAS FUERTE DESCARTADO: el "
    "paso 2 de seleccion_de_metodo_de_pago (definir cuanto riesgo estas "
    "dispuesto a asumir segun la relacion con el comprador y el pais al que "
    "exportas) contra los pasos 2 y 3 de "
    "incoterms_reglas_comerciales_internacionales (seleccionar el Incoterm "
    "adecuado segun el nivel de responsabilidad que quieres asumir y negociar "
    "con el comprador el punto exacto de transferencia de riesgo y costo). SE "
    "DESCARTA porque el riesgo del Incoterm es EL DE PERDIDA O DANO DE LA "
    "MERCANCIA EN TRANSITO y el del metodo de pago es EL DE CREDITO Y NO PAGO: "
    "misma palabra, riesgos distintos, y un procedimiento que reparte uno no "
    "puede ser el como se decide el otro. LA OTRA DIRECCION TAMPOCO: el paso 4 "
    "de pago (negociar el metodo de pago y dejarlo por escrito en el contrato) "
    "contra el paso 4 de Incoterms (especificar el Incoterm y el puerto "
    "nombrado en la cotizacion, pro forma, factura y contrato) escriben EN EL "
    "MISMO CONTRATO dos clausulas distintas, y compartir soporte no es "
    "expansion. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-092": ("D",
    "LA D SE SOSTIENE. Son DOS JUEGOS HERMANOS del mismo libro con DOS SALIDAS "
    "DISTINTAS: Speed Boat saca UN MAPA DE PAINS PRIORIZADOS por profundidad "
    "del ancla y Product Box saca LOS MENSAJES DE MARKETING Y BENEFICIOS que el "
    "cliente destaca al venderte la caja. PAR MAS FUERTE DESCARTADO: el paso 2 "
    "de speedboat (invita a los clientes a identificar problemas y obstaculos, "
    "cada uno en un post-it) contra el paso 1 de product_box (da a los clientes "
    "una caja de carton y pide que disenen el producto que comprarian). SE "
    "DESCARTA porque son DOS DISPOSITIVOS DE ELICITACION distintos con "
    "entregables distintos, no el como se hace del otro: hermanos, no madre e "
    "hijo. REGLA DE LA INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE SI, y "
    "lo declaro porque los dos nodos son ejemplares de la misma clase (los "
    "Innovation Games) y seria comodo cerrar con la regla. NO SE PUEDE: ninguna "
    "linea de ninguno de los dos NOMBRA la clase, y sin linea de categoria la "
    "regla no tiene donde morder"),

"LD-OPC05-093": ("D",
    "LA D SE SOSTIENE POR UNA SOLA DIRECCION. LA IDA ES FUERTE Y SE RECONOCE: "
    "el paso 3 de international_partner_search (recibe y EVALUA la lista de "
    "hasta 5 socios potenciales prescreened en 15 dias) lo expanden los nueve "
    "pasos de seleccion_representante_extranjero, que son el checklist entero "
    "de esa evaluacion (fuerza de ventas, historial de 5 anos, territorio, "
    "compatibilidad de lineas, instalaciones, politicas de compensacion, perfil "
    "de clientes, cuantos principales representa, enfoque promocional). LA "
    "VUELTA NO EXISTE: seleccion_representante ARRANCA con los candidatos ya en "
    "la mano y ninguna de sus nueve lineas pide conseguirlos. PAR MAS FUERTE "
    "DESCARTADO EN ESA DIRECCION: el paso 2 de seleccion (revisar el historial "
    "de ventas de los ultimos 5 anos) contra el paso 5 de partner_search (pide "
    "un informe ICP para verificar la reputacion y las referencias financieras "
    "del socio). SE DESCARTA porque el ICP trae REPUTACION Y REFERENCIAS "
    "FINANCIERAS y la linea pide EL HISTORIAL DE VENTAS: dentro del mismo "
    "tramite, datos distintos. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
    "CONTINUA. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-094": ("D",
    "LA CLASE PASA DE C A D Y CORRIGE MI PROPIA LECTURA DEL LOTE 2 DE LA VUELTA "
    "159. LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE porque LA REGLA DE LA INSTANCIA "
    "ES EL UNICO MOTIVO DEL DESCARTE DE LA DIRECCION QUE FALTA. LA VUELTA SE "
    "SOSTIENE Y NO ESTA EN DISCUSION: el paso 6 de "
    "investigacion_etnografica_ideacion (traducir los hallazgos observacionales "
    "en conceptos de producto concretos) lo expanden los ocho pasos de "
    "reglas_brainstorming, que son el procedimiento entero de la sesion que "
    "convierte hallazgos en ideas. LA IDA NO PASA LA VARA. Descansaba ENTERA en "
    "el paso 4 de brainstorming (preparar al equipo con una experiencia de "
    "inmersion previa: VISITA DE CAMPO, ENTREVISTAS A CLIENTES) expandido por "
    "los nueve pasos de la etnografia. SE DESCARTA porque esa linea ENUMERA UNA "
    "CATEGORIA CON DOS EJEMPLARES y la etnografia ES UNO DE LOS DOS: REGLA DE "
    "LA INSTANCIA (6.5.b): APLICA, Y ES EL UNICO MOTIVO. Se aplica aqui contra "
    "mi propio veredicto anterior justamente porque la 6.5.b manda auditarla "
    "donde NO conviene y no solo donde conviene. BAJO LA 6.3 SE RECORRIO EL "
    "RESTO DE ESA DIRECCION: el paso 2 de brainstorming (definir un enunciado "
    "claro del problema centrado en necesidad del cliente) tampoco lo expande "
    "la etnografia, cuyo paso 6 produce CONCEPTOS DE PRODUCTO y no un ENUNCIADO "
    "DE PROBLEMA; y el paso 1 (reunir al equipo en un espacio dedicado, con "
    "confianza mutua) no lo expande el paso 9 de la etnografia (construir "
    "confianza con LOS SUJETOS OBSERVADOS), que habla de otra confianza. UNA "
    "SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA"),

"LD-OPC05-096": ("D",
    "LA D SE SOSTIENE. PAR MAS FUERTE DESCARTADO: el paso 3 de "
    "joint_ventures_internacionales (negociar terminos de control gerencial y "
    "PROTECCION DE PROPIEDAD INTELECTUAL) contra el paso 4 de "
    "proteccion_propiedad_intelectual_internacional (incluir clausulas de "
    "proteccion de IP en todo contrato de licenciamiento o joint venture). SE "
    "DESCARTA POR EL 9.22: las dos lineas dicen lo mismo (mete la proteccion de "
    "IP en el contrato del joint venture). Y TOMANDO EN SU LUGAR LOS PASOS 1 A "
    "3 DEL NODO DE IP (registrar patentes y marcas en cada pais objetivo, usar "
    "el PCT y el Madrid Protocol, consultar stopfakes.gov y uspto.gov), "
    "TAMPOCO: esos procedimentan EL REGISTRO ANTE OFICINAS DE PATENTES, y la "
    "linea pide LA NEGOCIACION DE CLAUSULAS CON EL SOCIO. Acto distinto. LA "
    "VUELTA TAMPOCO EXISTE: ninguna linea del nodo de IP esta expandida por un "
    "procedimiento del joint venture, cuyos cinco pasos son de constitucion "
    "societaria. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-098": ("C",
    "LA C SE SOSTIENE Y LA MARCO DISCUTIBLE POR DUDA PROPIA, porque la segunda "
    "linea es la que decide y admite discusion. LINEA 1, en "
    "lean_launchpad_web_startup_process, paso 2: REDACTAR LAS HIPOTESIS DEL "
    "MODELO DE NEGOCIO DE 9 BLOQUES; la expanden los doce pasos de "
    "lienzo_modelo_negocio, que son el procedimiento entero del instrumento que "
    "esa linea nombra. Es el mismo caso que el acta 159 concedio sin discusion "
    "en la linea 2 de la LD-OPC05-100. LINEA 2, en lienzo_modelo_negocio, paso "
    "12: USAR EL LIENZO COMO BASE PARA PIVOTAR O VALIDAR HIPOTESIS DEL NEGOCIO; "
    "la expanden los pasos 5 a 10 de lean_launchpad (construir un sitio de baja "
    "fidelidad con splash page y formularios de pre-orden, dirigir trafico para "
    "probar segmento y propuesta de valor, conectar la interfaz con el backend, "
    "probar el problema del cliente con analytics y encuestas, construir una "
    "version de alta fidelidad para probar la solucion, y pedir dinero con "
    "pre-orden o cobro real), que son UN METODO SECUENCIADO CON INSTRUMENTOS "
    "NOMBRADOS y no una orden con criterio. POR QUE LA MARCO: porque la misma "
    "vara acaba de tumbar la LD-OPC05-101 y la LD-OPC05-118, cuyas segundas "
    "lineas descansaban en ordenes con criterio; aqui hay instrumentos "
    "concretos y por eso la sostengo, pero la frontera entre metodo e "
    "instruccion es exactamente donde esta vuelta se juega el credito. PAR MAS "
    "FUERTE DESCARTADO: el paso 9 del lienzo (pausar para investigar mas "
    "informacion donde haya vacios importantes) contra el paso 8 de "
    "lean_launchpad (probar el problema del cliente recopilando datos mediante "
    "analytics y encuestas), que SE DESCARTA por el mismo motivo con que cayo "
    "la linea 1 de la 100: el instrumento no toma el vacio como insumo. REGLA "
    "DE LA INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE SI, y lo declaro: "
    "lean_launchpad es la version WEB del proceso de Customer Development y "
    "tienta a leerlo como ejemplar de una clase. NO SE PUEDE: la linea que "
    "expande no enumera ninguna clase de metodos"),

"LD-OPC05-099": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE. PAR "
    "MAS FUERTE DESCARTADO: el paso 6 de lienzo_modelo_negocio (MAPEAR CANALES, "
    "RELACIONES Y FUENTES DE INGRESOS) contra los cinco pasos de "
    "patron_free_business_model (determinar que segmento recibe la oferta "
    "gratuita, identificar que otro segmento la financia, elegir el patron "
    "publicidad, freemium o bait and hook, calcular el costo marginal de servir "
    "usuarios gratuitos, disenar el subsidio cruzado). SE DESCARTA porque FREE "
    "ES UN PATRON entre los patrones de modelo de negocio y la linea manda "
    "mapear LA CATEGORIA fuentes de ingresos: REGLA DE LA INSTANCIA (6.5.b): "
    "APLICA, Y ES EL UNICO MOTIVO DE ESTE DESCARTE. LA OTRA DIRECCION TAMPOCO "
    "SE SOSTIENE, con motivo independiente: el paso 1 de FREE (determinar que "
    "segmento de clientes puede recibir la oferta gratuita) no lo expande el "
    "paso 4 del lienzo (identificar los segmentos de clientes a los que se "
    "dirige la organizacion), porque identificar SEGMENTOS no es elegir CUAL DE "
    "ELLOS NO PAGA"),

"LD-OPC05-101": ("D",
    "LA CLASE PASA DE C A D Y CORRIGE MI PROPIA LECTURA DEL LOTE 2 DE LA VUELTA "
    "159. LA MARCO DISCUTIBLE POR DUDA PROPIA. LA IDA SE SOSTIENE Y ES MUY "
    "FUERTE: el paso 8 de search_for_business_model (usar el Business Model "
    "Canvas y el Value Proposition Canvas como herramientas de planificacion "
    "flexible) y su paso 2 (listar explicitamente las hipotesis de mercado, "
    "cliente, producto, canal y precio) los expanden los doce pasos del lienzo. "
    "LA VUELTA NO PASA LA VARA, Y LA TUMBA LA MISMA MEDIDA CON QUE SE DECIDIO "
    "LA LD-OPC05-100 EN ESTA MISMA VUELTA. PAR MAS FUERTE DESCARTADO: el paso "
    "12 del lienzo (usar el lienzo como base para pivotar o validar hipotesis "
    "del negocio) contra los pasos 3 y 5 de search (aplica el proceso de "
    "Customer Development para salir a probar cada hipotesis con clientes "
    "reales; itera y pivota segun la evidencia recogida hasta encontrar un "
    "modelo repetible y escalable). SE DESCARTA POR DOS MOTIVOS: (1) el paso 3 "
    "REMITE a otro cuerpo (el proceso de Customer Development) en vez de "
    "procedimentar, y la remision no es procedimiento, que es la letra con que "
    "cayo la LD-OPC05-027; (2) el paso 5 es UNA ORDEN CON CRITERIO DE PARADA "
    "(itera y pivota hasta que sea repetible y escalable), no un metodo: no "
    "dice QUE cambiar ni COMO, que es la letra con que cayo la LD-OPC05-004. "
    "SEGUNDO PAR DESCARTADO: el paso 10 del lienzo (iterar y discutir en grupo "
    "hasta lograr coherencia entre los bloques) contra el paso 5 de search, que "
    "iteran cosas distintas, coherencia interna contra evidencia de mercado. Y "
    "LO CORROBORA EL CAMPO ENTREGABLE, medido igual que en la 100: el de search "
    "esta escrito EN TERMINOS DEL LIENZO (un lienzo de hipotesis marcado como "
    "no probado) y el del lienzo no menciona a search. UNA SOLA DIRECCION ES "
    "MADRE E HIJO Y EL PAR CONTINUA. REGLA DE LA INSTANCIA (6.5.b): NO SE "
    "PLANTEA"),

"LD-OPC05-102": ("D",
    "LA D SE SOSTIENE POR UNA SOLA DIRECCION. LA IDA SI SE SOSTIENE: el paso 4 "
    "del lienzo (identificar los segmentos de clientes a los que se dirige la "
    "organizacion) lo expanden los seis pasos de "
    "segmentos_de_clientes_problema_necesidad (salir del edificio a observar "
    "como viven el problema, clasificarlo en la escala latente, pasivo, activo "
    "o con solucion casera, determinar si el producto es must-have o "
    "nice-to-have, mapear quien usa, quien influye y quien recomienda, "
    "documentar un dia en la vida, y revisar si el mercado es de uno o de "
    "varios lados). LA VUELTA NO EXISTE. PAR MAS FUERTE DESCARTADO: el paso 4 "
    "de segmentos (mapea los tipos de cliente: quien usa el producto, quien "
    "influye en la compra y quien lo recomienda) contra los pasos 4 y 5 del "
    "lienzo (identificar los segmentos; definir la propuesta de valor para cada "
    "segmento). SE DESCARTA por dos cosas: colapsa con la ida en el mismo acto "
    "de identificar clientes, que es el 9.22, y ademas el lienzo NO procedimenta "
    "el reparto por ROL (usuario, influenciador, recomendador) que la linea "
    "pide. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA. REGLA DE LA "
    "INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-104": ("D",
    "LA D SE SOSTIENE, Y EL MOTIVO SE PUEDE ENUNCIAR EN UNA LINEA: "
    "metrics_that_matter_framework ES CIEGO AL TIPO DE MERCADO. LA VUELTA TIENE "
    "CANDIDATO: el paso 2 de metrics (calcula las unidades vendidas por periodo "
    "y el precio de venta promedio validado con clientes) lo acompanan los "
    "pasos 2 a 4 de market_type_revenue_growth (estimar la cuota de mercado que "
    "puedes capturar, buscar proxies y mercados adyacentes, evaluar el tamano "
    "del segmento y la tasa de adopcion). PAR MAS FUERTE DESCARTADO EN LA OTRA "
    "DIRECCION: el paso 6 de market_type (ajusta tus proyecciones de ingresos "
    "SEGUN EL TIPO DE MERCADO identificado y documenta tus supuestos) contra "
    "los pasos 2 a 5 de metrics (unidades y precio, restar descuentos y costos "
    "de canal, restar costos para el burn rate, construir la hoja trimestral). "
    "SE DESCARTA porque metrics da LA ARITMETICA DE UNA PROYECCION y no trae "
    "una sola linea que la ajuste POR TIPO DE MERCADO, que es el contenido "
    "operativo de la linea: expandir la mitad ociosa de una linea no la "
    "expande. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR CONTINUA. REGLA DE LA "
    "INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-106": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE, Y ESTE "
    "ES EL EJEMPLAR MAS PURO DE LA REGLA EN TODO EL TRAMO. PAR MAS FUERTE "
    "DESCARTADO: el paso 3 de motor_de_crecimiento (SELECCIONAR EL MOTOR DE "
    "CRECIMIENTO ESPECIFICO: PEGAJOSO, VIRAL O PAGADO, y sus metricas "
    "asociadas) contra los cinco pasos de motor_crecimiento_viral (calcular el "
    "coeficiente viral, identificar el mecanismo de transmision inherente, "
    "eliminar friccion en registro y recomendacion, enfocar el desarrollo en "
    "subir el coeficiente, evaluar si el modelo debe basarse en ingresos "
    "indirectos). SE DESCARTA porque la linea ENUMERA TRES MOTORES y el otro "
    "nodo ES UNO DE LOS TRES: REGLA DE LA INSTANCIA (6.5.b): APLICA, Y ES EL "
    "UNICO MOTIVO. LA OTRA DIRECCION NI SIQUIERA TIENE CANDIDATO: los cuatro "
    "pasos de motor_de_crecimiento son elegir, descartar metricas de vanidad, "
    "seleccionar y enfocar, y ninguno procedimenta el calculo del coeficiente "
    "viral ni la eliminacion de friccion"),

"LD-OPC05-107": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE. PAR "
    "MAS FUERTE DESCARTADO: el paso 1 de term_sheet_negociacion (revisar CADA "
    "SECCION del term sheet, dividendos, liquidacion, conversion, antidilucion, "
    "voto y board, con un abogado) contra los cuatro pasos de "
    "no_shop_agreement. SE DESCARTA porque el no-shop ES UNA CLAUSULA del term "
    "sheet, o sea un ejemplar de la categoria que la linea enumera: REGLA DE LA "
    "INSTANCIA (6.5.b): APLICA, Y ES EL UNICO MOTIVO. LA OTRA DIRECCION "
    "TAMPOCO: el paso 2 del no-shop (ten claro que esta clausula es vinculante "
    "desde que firmas el term sheet, a diferencia del resto de sus condiciones) "
    "no lo expanden los pasos 1 y 5 de term_sheet (revisar con abogado, firmar "
    "solo despues de validar), que procedimentan LA REVISION Y LA FIRMA y no LA "
    "NATURALEZA VINCULANTE de una clausula concreta"),

"LD-OPC05-108": ("D",
    "LA D SE SOSTIENE. Los dos nodos son del mismo autor y los dos dicen "
    "EMPIEZA TEMPRANO, y por eso se rozan, pero empiezan temprano COSAS "
    "DISTINTAS. PAR MAS FUERTE DESCARTADO: el paso 1 de "
    "plan_de_lanzamiento_al_mercado (empieza a armar tu plan de lanzamiento "
    "desde las primeras etapas del proyecto, no lo dejes para el final) contra "
    "los pasos 1 y 4 de reduccion_tiempo_de_mercado_velocidad (realizar el "
    "trabajo de homework temprano, VoC y definicion de producto, para evitar "
    "retrabajos; usar procesamiento paralelo de tareas en lugar de secuencial). "
    "SE DESCARTA porque el homework temprano de velocidad es VOZ DEL CLIENTE Y "
    "DEFINICION DE PRODUCTO, no el plan de lanzamiento, y el procesamiento "
    "paralelo es UNA POSTURA DE CRONOGRAMA, no el como se arma un plan de "
    "lanzamiento. LA VUELTA TAMPOCO: ninguna de las seis lineas de velocidad "
    "esta expandida por un procedimiento del plan de lanzamiento, cuyos cinco "
    "pasos son de contenido del plan y no de aceleracion del ciclo. REGLA DE LA "
    "INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-109": ("C",
    "LA C SE SOSTIENE Y AQUI VAN SUS DOS LINEAS. LINEA 1, en "
    "plan_gestion_interesados, paso 3: DEFINE QUE NECESITA SABER CADA PERSONA Y "
    "COMO SE LO VAS A COMUNICAR; la expanden los seis pasos de "
    "plan_gestion_comunicaciones, que son el procedimiento entero de esa "
    "definicion (lista de personas o grupos, tipo de informacion para cada uno, "
    "metodo de entrega, cada cuanto, quien es el responsable de mandarla, y las "
    "restricciones y el glosario). LINEA 2, en plan_gestion_comunicaciones, "
    "paso 1: HAZ UNA LISTA DE LAS PERSONAS O GRUPOS QUE NECESITAN RECIBIR "
    "INFORMACION DE TU PROYECTO; la expanden los pasos 1, 2 y 4 de "
    "plan_gestion_interesados (anotar el nivel de compromiso actual y el "
    "deseado de cada persona, ubicar a cada una segun si no lo conoce, se "
    "resiste, es neutral, lo apoya o ya lo defiende, e identificar como se "
    "relacionan entre si los grupos), que son EL COMO se construye y se "
    "cualifica esa lista. DOS LINEAS DISTINTAS Y NINGUNO ES LA MADRE. PAR MAS "
    "FUERTE DESCARTADO: el paso 5 de interesados (piensa como vas a acercar a "
    "cada una al nivel de compromiso que necesitas) contra el paso 3 de "
    "comunicaciones (decide el metodo de entrega), que SE DESCARTA porque "
    "elegir un canal no es una estrategia de acercamiento. REGLA DE LA "
    "INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE SI, y lo declaro porque "
    "el parecido es fuerte: los dos son PLANES SUBSIDIARIOS del mismo cuerpo, y "
    "la 6.5 usa literalmente consolida los planes subsidiarios como su ejemplo "
    "de linea de categoria. NO SE PUEDE APLICAR AQUI, y es medible: esa linea "
    "de categoria NO vive en ninguno de estos dos nodos, vive en "
    "project_management_plan, que es el otro par de este mismo tramo (la 113)"),

"LD-OPC05-111": ("D",
    "LA D SE SOSTIENE. PAR MAS FUERTE DESCARTADO: el paso 4 de "
    "sistema_gestion_calidad (documenta el sistema de gestion de calidad "
    "siguiendo LOS ESTANDARES QUE APLIQUEN EN TU MERCADO) contra los cuatro "
    "pasos de principios_gestion_calidad_iso9000. SE DESCARTA POR DOS MOTIVOS "
    "QUE SE SOSTIENEN CADA UNO SOLO, y por eso esta fila NO queda marcada por "
    "la 6.5.a: (1) REGLA DE LA INSTANCIA (6.5.b): APLICA, porque ISO 9000 es "
    "UNO de los estandares que la linea enumera como categoria; (2) y ademas "
    "los cuatro pasos del nodo de principios son UNA AUTOEVALUACION (evaluar el "
    "grado de cumplimiento, priorizar brechas, incorporar como criterios "
    "rectores, comunicar), y evaluar no es documentar: aunque la regla de la "
    "instancia no existiera, este par caeria igual. LA OTRA DIRECCION TAMPOCO: "
    "el paso 3 de principios (incorporar estos principios como criterios "
    "rectores en el diseno del sistema) no lo expanden los cuatro pasos del "
    "sistema, que mapean procesos, identifican controladores, coordinan y "
    "documentan SIN MENCIONAR LOS PRINCIPIOS ni una vez"),

"LD-OPC05-112": ("D",
    "LA D SE SOSTIENE Y LA MARCO DISCUTIBLE POR DUDA PROPIA, porque la ida es "
    "muy fuerte y la vuelta cae por la forma de las lineas y no por su materia. "
    "LA IDA SE SOSTIENE: el paso 2 de problem_solution_fit (probar si la "
    "solucion propuesta resuelve el problema de forma convincente) lo expanden "
    "los seis pasos de producto_minimo_viable (identificar la hipotesis mas "
    "critica y bajarla al problema mas pequeno que un cliente pagaria por "
    "resolver, disenar la version mas simple que pruebe esa hipotesis, evitar "
    "funciones extra, lanzar a early adopters y no al mercado masivo, medir la "
    "reaccion real y no la opinion, iterar o cambiar de rumbo). PAR MAS FUERTE "
    "DESCARTADO EN LA OTRA DIRECCION: el paso 1 del MVP (identifica la "
    "hipotesis de negocio mas critica y bajala al problema central mas pequeno "
    "que un cliente pagaria por resolver) contra los pasos 1 y 3 de "
    "problem_solution_fit (validar que el problema identificado sea doloroso "
    "para un segmento amplio; verificar alineacion entre modelo de ingresos, "
    "precio y necesidades del cliente). SE DESCARTA porque LOS CUATRO PASOS DE "
    "problem_solution_fit SON ORDENES SIN METODO: validar, probar, verificar y "
    "considerar, sin instrumento, sin secuencia y sin entregable propio. Es "
    "exactamente la forma que la LD-OPC05-100 y la LD-OPC05-122 excluyeron: "
    "nombrar sin procedimentar. UNA SOLA DIRECCION ES MADRE E HIJO Y EL PAR "
    "CONTINUA. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-113": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE, y "
    "ademas ESTE ES EL PAR DEL QUE SALIO EL EJEMPLO LITERAL DE LA REGLA. PAR "
    "MAS FUERTE DESCARTADO: el paso 5 de project_management_plan (CONSOLIDAR "
    "TODOS LOS PLANES SUBSIDIARIOS y lineas base en un documento unico) contra "
    "los cinco pasos de scope_management_plan (definir como se desarrollara el "
    "Project Scope Statement, establecer la estructura del WBS, determinar los "
    "campos del WBS Dictionary, diferenciar cambio de alcance de revision "
    "menor, definir como se validara cada entregable). SE DESCARTA porque el "
    "plan de alcance ES UNO de los planes subsidiarios que la linea manda "
    "consolidar: REGLA DE LA INSTANCIA (6.5.b): APLICA, Y ES EL UNICO MOTIVO. "
    "LA OTRA DIRECCION TAMPOCO: ninguna de las cinco lineas del plan de alcance "
    "esta expandida por un procedimiento del plan maestro, cuyos seis pasos "
    "eligen ciclo de vida, procesos, herramientas, umbrales, consolidacion y "
    "frecuencia de revisiones, sin tocar el WBS"),

"LD-OPC05-114": ("D",
    "LA D SE SOSTIENE Y LA MARCO DISCUTIBLE POR DUDA PROPIA. Son DOS TECNICAS "
    "DE PROTOTIPADO HERMANAS con CRITERIOS DE SELECCION DE MATERIAL OPUESTOS, y "
    "esa oposicion es lo que decide. PAR MAS FUERTE DESCARTADO: el paso 3 de "
    "prototipar_con_medios_no_convencionales (construye una version de tu idea "
    "central usando ese medio no convencional) contra los pasos 2 a 5 de "
    "prototipado_rapido (construir una representacion fisica minima en minutos "
    "u horas, usar el prototipo como herramienta de discusion, evitar invertir "
    "en acabados, iterar rapido con la retroalimentacion). SE DESCARTA porque "
    "el metodo de prototipado_rapido PRESUPONE MATERIALES BARATOS Y ACCESIBLES "
    "(su paso 1 lo dice: carton, cinta, objetos cotidianos) mientras el "
    "contenido operativo de la linea es UN MEDIO RADICALMENTE DISTINTO AL "
    "HABITUAL, que puede no ser ni barato ni accesible: dos criterios de "
    "seleccion opuestos no pueden ser el como se hace uno del otro. LA VUELTA "
    "TAMPOCO: el paso 1 de prototipado_rapido (seleccionar materiales baratos y "
    "accesibles) y los pasos 1 y 2 de no_convencionales (identifica tu medio "
    "por defecto, elige uno radicalmente distinto) se contradicen en vez de "
    "expandirse. REGLA DE LA INSTANCIA (6.5.b): NO APLICA PUDIENDO PARECER QUE "
    "SI, y lo declaro porque los dos son ejemplares de la clase tecnicas de "
    "prototipado; NO SE PUEDE aplicar porque ninguna linea de ninguno de los "
    "dos nombra esa clase"),

"LD-OPC05-117": ("D",
    "LA D SE SOSTIENE. riesgos_lanzamiento_mvp trata LOS MIEDOS QUE FRENAN AL "
    "FUNDADOR (consultar al abogado por las patentes, recordar que la ventaja "
    "es ejecutar rapido y no el secreto, lanzar con otro nombre si te preocupa "
    "la marca, comprometerte de antemano a iterar, preparar el animo del "
    "equipo) y wizard_of_oz_testing es UN DISPOSITIVO DE PRUEBA (definir la "
    "experiencia final ocultando como se genera el resultado, sustituir el "
    "backend por personas, lanzar sin revelar que es simulado, medir uso y "
    "retencion, iterar antes de invertir en la tecnologia). PAR MAS FUERTE "
    "DESCARTADO: el paso 3 de riesgos (si te preocupa tu marca, lanza el MVP "
    "con un nombre distinto al que ya usas, separado de tu negocio conocido) "
    "contra el paso 3 de wizard (lanza el producto a un grupo reducido de "
    "usuarios reales sin revelar que es simulado). SE DESCARTA porque las dos "
    "OCULTAN COSAS DISTINTAS, la marca y el mecanismo, y dos precauciones "
    "hermanas no son madre e hija. BAJO LA 6.3 SE RECORRIO EL ESPACIO ENTERO Y "
    "NINGUN OTRO PAR SOSTIENE LA FIGURA. REGLA DE LA INSTANCIA (6.5.b): NO SE "
    "PLANTEA"),

"LD-OPC05-118": ("D",
    "LA CLASE PASA DE C A D Y CORRIGE MI PROPIA LECTURA DEL LOTE 2 DE LA VUELTA "
    "159. LA MARCO DISCUTIBLE POR DUDA PROPIA. LA VUELTA SE SOSTIENE: el paso 5 "
    "de search_for_business_model (itera y pivota segun la evidencia recogida "
    "hasta encontrar un modelo repetible y escalable) lo acompanan los pasos 3, "
    "4 y 5 de vision_estrategia_producto_pivote (distinguir ajustes menores de "
    "cambios de rumbo mayores, establecer el ciclo Construir-Medir-Aprender "
    "como mecanismo de direccion continua, y evaluar regularmente si perseverar "
    "o pivotar). LA IDA NO PASA LA VARA. PAR MAS FUERTE DESCARTADO: el paso 5 "
    "de vision (evalua regularmente si mantener el rumbo actual o hacer un giro "
    "brusco) contra los pasos 3 y 5 de search. SE DESCARTA POR LOS MISMOS DOS "
    "MOTIVOS CON QUE CAYO LA 101 EN ESTA MISMA CORRIDA, y se aplican igual "
    "aunque aqui me cueste una C propia: el paso 3 de search REMITE al proceso "
    "de Customer Development en vez de procedimentar, y el paso 5 es UNA ORDEN "
    "CON CRITERIO DE PARADA y no un metodo, sin instrumento nombrado que diga "
    "COMO se hace la evaluacion de perseverar o pivotar. SEGUNDO PAR "
    "DESCARTADO: el paso 2 de vision (formula una estrategia inicial: modelo de "
    "negocio, hoja de ruta, cliente objetivo, postura frente a competidores) "
    "contra el paso 2 de search (lista las hipotesis marcadas como NO "
    "PROBADAS), que SE DESCARTA porque los dos nodos estan EN TENSION y no en "
    "expansion: el paso 7 de search manda literalmente abandonar la idea de "
    "escribir un plan detallado al inicio. UNA SOLA DIRECCION ES MADRE E HIJO Y "
    "EL PAR CONTINUA. REGLA DE LA INSTANCIA (6.5.b): NO SE PLANTEA"),

"LD-OPC05-119": ("D",
    "LA D SE SOSTIENE Y LA 6.5.a OBLIGA A MARCARLA DISCUTIBLE, porque LA REGLA "
    "DE LA INSTANCIA ES EL UNICO MOTIVO DEL DESCARTE DEL PAR MAS FUERTE. PAR "
    "MAS FUERTE DESCARTADO: el paso 8 de simulacion_de_operaciones_supply_chain "
    "(probar COMBINACIONES DE TECNOLOGIAS, ROBOTS, MANUFACTURA ADITIVA, "
    "VEHICULOS AUTONOMOS, en el modelo) contra los cinco pasos de "
    "vehiculos_autonomos_drones_supply_chain. SE DESCARTA porque la linea "
    "enumera TRES TECNOLOGIAS y el otro nodo ES UNA DE LAS TRES: REGLA DE LA "
    "INSTANCIA (6.5.b): APLICA, Y ES EL UNICO MOTIVO. LA OTRA DIRECCION "
    "TAMPOCO: el paso 5 de vehiculos (lanza un piloto en una ruta o area "
    "limitada y mide su desempeno antes de escalar) no lo expanden los pasos 3 "
    "a 6 de simulacion, porque la simulacion VALIDA ANTES DE IMPLEMENTAR "
    "FISICAMENTE (su paso 6 lo dice) y un piloto YA ES implementacion fisica: "
    "actos distintos en momentos distintos"),

"LD-OPC05-121": ("D",
    "LA D SE SOSTIENE Y LA MARCO DISCUTIBLE POR DUDA PROPIA, porque los dos "
    "nodos son EL GENERAL Y EL DE PRECIO del mismo instrumento y esa relacion "
    "de todo y parte siempre invita a leerla como figura. PAR MAS FUERTE "
    "DESCARTADO: el paso 3 de venture_debt_introduccion (identificar bancos "
    "especializados como SVB o fondos de deuda de riesgo con track record en el "
    "sector) contra el paso 5 de venture_debt_terminos_economicos (compara "
    "ofertas entre bancos, que suelen pedir menos warrants pero imponen mas "
    "restricciones, y fondos de deuda, que piden mas warrants pero imponen "
    "menos). SE DESCARTA porque el paso 5 compara OFERTAS YA RECIBIDAS y da el "
    "canje entre warrants y covenants, mientras la linea pide COMO IDENTIFICAR "
    "PRESTAMISTAS y verificar su track record: el otro nodo presupone hecho lo "
    "que la linea pide hacer. Precedencia inversa, no expansion. LA OTRA "
    "DIRECCION TAMPOCO: el paso 4 de terminos (negocia el precio de ejercicio "
    "de los warrants anclandolo a la valoracion de tu proxima ronda) y el paso "
    "5 de introduccion (definir el proposito del prestamo: runway, capex, "
    "adquisicion, puente a proxima ronda) NOMBRAN LOS DOS LA PROXIMA RONDA pero "
    "uno fija un precio y el otro un proposito. REGLA DE LA INSTANCIA (6.5.b): "
    "NO APLICA PUDIENDO PARECER QUE SI, y lo declaro por la relacion de todo y "
    "parte; NO SE PUEDE aplicar porque ninguna linea enumera una categoria de "
    "la que el otro sea ejemplar"),
}


# --------------------------------------------------------------------------
# LA 2.c: EL ESTADO DE LA REGLA DE LA INSTANCIA EN CADA UNA DE LAS 37
# --------------------------------------------------------------------------

REGLA = {
    "LD-OPC05-068": NO_PLANTEA, "LD-OPC05-069": NO_PLANTEA,
    "LD-OPC05-071": NO_PLANTEA, "LD-OPC05-072": NO_PLANTEA,
    "LD-OPC05-073": NO_PLANTEA, "LD-OPC05-074": NO_PLANTEA,
    "LD-OPC05-076": APLICA,     "LD-OPC05-077": PARECE,
    "LD-OPC05-079": NO_PLANTEA, "LD-OPC05-082": APLICA,
    "LD-OPC05-083": NO_PLANTEA, "LD-OPC05-086": NO_PLANTEA,
    "LD-OPC05-087": PARECE,     "LD-OPC05-088": PARECE,
    "LD-OPC05-089": APLICA,     "LD-OPC05-091": NO_PLANTEA,
    "LD-OPC05-092": PARECE,     "LD-OPC05-093": NO_PLANTEA,
    "LD-OPC05-094": APLICA,     "LD-OPC05-096": NO_PLANTEA,
    "LD-OPC05-098": PARECE,     "LD-OPC05-099": APLICA,
    "LD-OPC05-101": NO_PLANTEA, "LD-OPC05-102": NO_PLANTEA,
    "LD-OPC05-104": NO_PLANTEA, "LD-OPC05-106": APLICA,
    "LD-OPC05-107": APLICA,     "LD-OPC05-108": NO_PLANTEA,
    "LD-OPC05-109": PARECE,     "LD-OPC05-111": APLICA,
    "LD-OPC05-112": NO_PLANTEA, "LD-OPC05-113": APLICA,
    "LD-OPC05-114": PARECE,     "LD-OPC05-117": NO_PLANTEA,
    "LD-OPC05-118": NO_PLANTEA, "LD-OPC05-119": APLICA,
    "LD-OPC05-121": PARECE,
}

# LAS SIETE QUE LA 6.5.a OBLIGA A MARCAR: la regla es el UNICO motivo del
# descarte del par mas fuerte.
UNICO_MOTIVO = ("LD-OPC05-082", "LD-OPC05-094", "LD-OPC05-099", "LD-OPC05-106",
                "LD-OPC05-107", "LD-OPC05-113", "LD-OPC05-119")

# LAS TRES EN QUE LA REGLA APLICA PERO NO ES EL UNICO MOTIVO, y por eso NO se
# marcan por esta via. La diferencia se publica porque es lo que hace auditable
# a la condicion (a).
APLICA_CON_SEGUNDO_MOTIVO = ("LD-OPC05-076", "LD-OPC05-089", "LD-OPC05-111")

# LOS QUE MARCO YO POR DUDA PROPIA, antes de saber si acierto.
DUDA_PROPIA = ("LD-OPC05-074", "LD-OPC05-076", "LD-OPC05-098", "LD-OPC05-101",
               "LD-OPC05-112", "LD-OPC05-114", "LD-OPC05-118", "LD-OPC05-121")


def main():
    nomina = json.load(io.open(NOMINA, encoding="utf-8"))["tramo"]

    # LA GUARDA QUE VA ANTES DE ESCRIBIR NADA: cada una de las 37 declara su
    # estado de la regla, y el estado declarado en REGLA tiene que estar
    # ESCRITO LITERALMENTE en la razon. Una tabla que no case con su prosa es
    # una tabla tecleada.
    faltan = [ld for ld in nomina if ld not in REGLA]
    assert not faltan, "sin estado de la regla: %s" % ", ".join(faltan)
    mal = [ld for ld in nomina if ("REGLA DE LA INSTANCIA (6.5.b): " + REGLA[ld])
           not in V[ld][1]]
    assert not mal, ("el estado declarado en la tabla NO esta escrito en la "
                     "razon de: %s" % ", ".join(mal))

    rc = motor.aplicar(
        "VUELTA 160, TAREA 2.b: LAS 37 DEL TRAMO AL DOBLE, SEGUNDA PASADA",
        V, MARCA, cabeza, nota_md, ids_esperados=nomina)
    if rc:
        return rc

    print("=" * 78)
    print("E) LA 2.c, AUDITORIA DE CONSISTENCIA DE LA REGLA DE LA INSTANCIA")
    print("   (adjudicacion 6.5.b del acta 159)")
    print("=" * 78)
    cuenta = {APLICA: 0, PARECE: 0, NO_PLANTEA: 0}
    for ld in nomina:
        cuenta[REGLA[ld]] += 1
    print("")
    print("   CIFRA lecturas del tramo: %d" % len(nomina))
    print("   CIFRA en que la regla APLICA: %d" % cuenta[APLICA])
    print("   CIFRA en que NO APLICA PUDIENDO PARECER QUE SI: %d" % cuenta[PARECE])
    print("   CIFRA en que NO SE PLANTEA: %d" % cuenta[NO_PLANTEA])
    assert sum(cuenta.values()) == len(nomina)
    print("")
    print("   LAS QUE APLICA, UNA A UNA:")
    for ld in nomina:
        if REGLA[ld] == APLICA:
            solo = "UNICO MOTIVO" if ld in UNICO_MOTIVO else "CON SEGUNDO MOTIVO INDEPENDIENTE"
            print("      %-16s %s" % (ld, solo))
    print("   CIFRA de ellas en que es el UNICO motivo del descarte: %d"
          % len(UNICO_MOTIVO))
    print("   CIFRA de ellas con un segundo motivo que se sostiene solo: %d"
          % len(APLICA_CON_SEGUNDO_MOTIVO))
    assert (len(UNICO_MOTIVO) + len(APLICA_CON_SEGUNDO_MOTIVO)) == cuenta[APLICA]
    print("")
    print("   LAS QUE NO APLICA PUDIENDO PARECER QUE SI, UNA A UNA, Y ESTE ES EL")
    print("   ESTADO QUE HACE AUDITABLE A LA REGLA: sin el solo se veria donde")
    print("   conviene aplicarla.")
    for ld in nomina:
        if REGLA[ld] == PARECE:
            print("      %s" % ld)
    print("")

    print("F) LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
    print("   (i) LAS QUE LA 6.5.a OBLIGA A MARCAR (regla = unico motivo): %d"
          % len(UNICO_MOTIVO))
    for ld in UNICO_MOTIVO:
        print("      %s" % ld)
    print("   (ii) LAS QUE MARCO POR DUDA PROPIA: %d" % len(DUDA_PROPIA))
    for ld in DUDA_PROPIA:
        print("      %s" % ld)
    todos = sorted(set(UNICO_MOTIVO) | set(DUDA_PROPIA))
    print("   CIFRA discutibles de este tramo: %d de %d" % (len(todos), len(nomina)))
    print("   ES MUCHO Y SE DICE POR QUE: este tramo se lee con la vara recien")
    print("   estrechada por la LD-OPC05-100, y una vara recien estrechada")
    print("   produce mas dudas honestas que una vieja.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
