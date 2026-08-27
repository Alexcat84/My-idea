# -*- coding: utf-8 -*-
r"""vuelta97_tarea2_veredictos_tramo2.py . VUELTA 97, TAREA 2: LOS VEREDICTOS
del SEGUNDO tramo de OP-E-03, sesenta pares leidos (filas 41 a 100 de las 183 de
docs/plan/DIFERENCIA_CONTRA_COLA.jsonl), con su clase del banco 9.6.1 y su
direccion del 9.6.2.

HERMANO DECLARADO de scripts/loop/vuelta96_tarea3_veredictos_tramo1.py, y NO UNA
COPIA: este fichero IMPORTA construir_filas() de aquel y solo le pasa SU tabla y
SU tramo (--desde 40 --cuantos 60). El armazon (uno a uno con el material, clases
en {A,B,C,D}, sin repetidos, la direccion nombrando los DOS nodos resueltos de la
fila) es literalmente el mismo codigo ya probado por mutacion en la vuelta 96, y
se vuelve a probar por mutacion aqui, sobre ESTA tabla, en
scripts/loop/vuelta97_tarea2_prueba_mutacion.py.

DE DONDE SALEN LOS VEREDICTOS, Y SE DICE SIN ADORNO: los pone LA LECTURA del
ejecutor sobre el material impreso entero por
scripts/loop/vuelta96_tarea3_tramo1_opE03.py --desde 40 --cuantos 60
(docs/loop/SALIDA_V97_TAREA2_TRAMO2_MATERIAL.txt). Son una TABLA A MANO. Por
EJECUTOR.md regla 1 ("EL CASO ROJO SE PRUEBA POR MUTACION ... Si la clasificacion
es una tabla a mano y no hay nada que mutar, SE DECLARA QUE NO HAY CASO ROJO
AUTOMATICO"): AQUI SE DECLARA. NO HAY CASO ROJO AUTOMATICO PARA LA CLASE NI PARA
LA DIRECCION DE CADA PAR. Lo que si tiene guardas mecanicas, y estan probadas por
mutacion, es el armazon.

UNA HONESTIDAD SOBRE LA CABECERA DEL MATERIAL, dicha en vez de callada: el
instrumento del material se llama "tramo1" y su cabecera imprime "PRIMER TRAMO DE
LECTURA DIRIGIDA (vuelta 96, TAREA 3)" tambien cuando se le pasa --desde 40. El
rotulo es del fichero de la vuelta 96; la linea que SI depende de los argumentos
("Este tramo: filas 41 a 100 (60 pares)") es correcta y es la que manda. NO se
toco aquel codigo, porque el encargo dice expresamente que el auditor probo que
acepta el salto SIN TOCAR CODIGO.

LA VARA APLICADA, citada y no inventada, con las lineas leidas hoy de
docs/BANCO_DE_TEXTOS.md:
  9.6.1 (linea 1612), rama contenido manda: "Si lo que el hijo anade a lo que la
    madre ya dice CABE EN UNA LINEA, REPITE. Si trae un PROCEDIMIENTO que la
    madre no tiene, CONTINUA."
  9.6.2 (linea 1737), la direccion: "El hijo cabe entero dentro de UN paso de la
    madre, y la madre conserva materia propia que el hijo no toca en ningun
    paso."
  9.6.3 (linea 1796): el TAMANO del solape no decide; decide que queda FUERA y en
    que lado.

EL UMBRAL DE DIRECCION NO SE MUEVE, y se dice por que: el acta de la vuelta 96
seccion 4.4 (docs/loop/ACTA_AUDITOR.md linea 34367, leida hoy) adjudica que "el
umbral esta bien puesto y no se toca", tras leer a ciegas las cinco que el
ejecutor marco y llegar a NO RESUELTA en las cinco. Este tramo se lee con EL
MISMO umbral que el tramo 1, y la proporcion que salga se declara como salga.

SALIDA: docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl (60 filas) y la tabla por
pantalla. Es el UNICO fichero que escribe. NO toca el cribado ni el grafo.

USO:
  python scripts/loop/vuelta97_tarea2_veredictos_tramo2.py
  python scripts/loop/vuelta97_tarea2_veredictos_tramo2.py --sin-escribir
"""
import argparse
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from vuelta96_tarea3_veredictos_tramo1 import construir_filas  # noqa: E402

SALIDA = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")

DESDE = 40
CUANTOS = 60

# LA TABLA A MANO. (n, clase, direccion, razon).
# direccion: "madre -> hijo" con los ids RESUELTOS, o None cuando la lectura NO
# la resuelve. Cada razon cita el paso que el barrido caso.
VEREDICTOS = [
    (41, "D", None,
     "SON HERMANOS, NO MADRE E HIJO, y el titulo del propio nodo lo dice: la madre se rotula 'Quality by Design - Paso 4' y el hijo es el paso siguiente de la misma secuencia de Juran, las caracteristicas del PROCESO despues de las del PRODUCTO. El paso 6 casado ('Desarrollar caracteristicas y metas detalladas para cada componente') es de producto; el hijo lista procesos capaces, evalua su capacidad, elige el optimo y le fija metas. Cada lado trae su procedimiento, asi que CONTINUA por 9.6.3, pero la direccion NO SE RESUELVE: es el caso 2.195 que el 9.6.2 nombra."),
    (42, "A", "cultura_justa_2 -> preguntar_que_no_quien",
     "El hijo cabe entero dentro del paso 2 de la madre ('Preguntar que es responsable en vez de quien es responsable ante cada incidente') y la madre conserva materia propia que el hijo no toca: no comprar programas de cultura justa prediseniados, involucrar a pares con credibilidad tecnica y explorar la justicia restaurativa. Quitado lo que la madre ya dice, al hijo le quedan dos lineas sueltas ('anota las condiciones de trabajo que rodeaban el momento' y 'usa lo que encuentres para cambiar el sistema'), no una secuencia con logica propia. REPITE por 9.6.1."),
    (43, "D", None,
     "FALSO AMIGO DE TITULO, con titulo_ratio 92,1 y nada debajo. El paso 3 casado es 'Definir la estructura de reporte del area de exportacion', o sea el ORGANIGRAMA de quien reporta a quien; el hijo es la ESTRUCTURA DEL DOCUMENTO del plan de exportacion (indice, declaracion de politica, analisis de situacion, marketing, tacticas, presupuesto, cronograma). Comparten la palabra 'estructura' y el dominio, nada mas. Procedimiento en los dos lados: CONTINUA. Direccion NO RESUELTA."),
    (44, "D", None,
     "EL BARRIDO CASA UN PASO CON SU CONTRARIO, por el token 'NDA'. El paso 2 de la madre es 'Nunca solicitar un acuerdo de confidencialidad (NDA) a un VC', en fundraising; el hijo manda EXIGIR un NDA bidireccional antes del due diligence, en una ADQUISICION. Consejos opuestos sobre transacciones distintas. Cada lado trae su procedimiento: CONTINUA. Direccion NO RESUELTA."),
    (45, "D", "estrategia_de_innovacion_de_producto -> strat_map_arenas_estrategicas",
     "Su paso 3, 'Definir arenas estrategicas (mercados, tecnologias, sectores) donde enfocar los esfuerzos de innovacion', es UNA LINEA, y el hijo trae el metodo Strat-Map entero: definir el home base, identificar arenas potenciales, fijar de 6 a 8 criterios de atractivo y otros tantos de fortaleza, calificar de 0 a 10, graficar las burbujas y elegir el cuadrante superior derecho. La madre conserva los objetivos porcentuales a 3 y 5 anios, los buckets de recursos, el roadmap y la vision de largo plazo."),
    (46, "D", "customer_discovery_get_out_of_building -> prueba_solucion_con_cliente",
     "El hijo trae el protocolo entero de la prueba de solucion: ampliar a diez clientes, preguntas de presupuesto, explorar el limite de precio de arriba hacia abajo, canal preferido, proceso interno de aprobacion de compra y ficha comparable por entrevista. La madre conserva la identificacion de hipotesis, el evitar focus groups y el contraste con lo que se pensaba al principio. SE ANOTA que el barrido caso el paso 1 y el hijo ejecuta en realidad el paso 2 ('Sal a entrevistar clientes potenciales de forma repetida'); la direccion se sostiene igual, pero el paso citado por el barrido no es el que el hijo despliega."),
    (47, "B", "reporte_estado_miembro_equipo -> variance_analysis",
     "DUDOSO Y SE DECLARA EN VEZ DE FORZARLO. La direccion si se lee: el hijo cabe dentro del paso 3 ('Identificar las causas raiz de las variaciones en actividades y costos') y la madre conserva listar actividades planeadas y no logradas, reportar riesgos nuevos y planificar el periodo siguiente. Lo que no resuelve la vara sola es la CLASE: quitado lo que la madre ya dice en sus pasos 2, 3 y 4, al hijo le queda extender la comparacion a cronograma y calidad y calcular la magnitud de la variacion. Eso es mas que una linea y menos que un procedimiento propio, que es exactamente donde vive la clase B."),
    (48, "D", "concepto_proyecto_breakthrough -> proyectos_vitales_pocos",
     "Su paso 2, 'Clasificar el proyecto como parte de los vitales pocos o utiles muchos', es UNA LINEA, y el hijo trae el procedimiento: clasificar por impacto potencial, asignar equipos multifuncionales a los vitales pocos, delegar los de bajo impacto a equipos departamentales y balancear recursos por ROI esperado. La madre conserva la definicion del problema cronico y la asignacion del equipo."),
    (49, "D", "terminologia_clave_breakthrough -> analisis_sintomas",
     "Su paso 2, 'Diferenciar sintomas de causas en cada problema detectado', es UNA LINEA, y el hijo trae el procedimiento de diagnostico: recolectar datos de ocurrencia, ubicar la falla con diagramas de flujo, aplicar Pareto y estratificacion, y documentar frecuencia, severidad y tipo. La madre conserva definir los terminos con el equipo y documentar las teorias antes de validarlas. El Pareto aparece en los dos lados, y por 9.6.3 el tamanio del solape no decide."),
    (50, "D", None,
     "OBJETOS DISTINTOS bajo una palabra compartida. El paso 2 casado, 'Identificar reacciones a palabras como verde, ambiental, sostenibilidad', mide ACTITUDES DE LOS EMPLEADOS; el hijo hace un FODA ambiental por linea de producto, compara con competidores y busca atributos verdes no comunicados al mercado, o sea mira AFUERA. Procedimiento en los dos lados: CONTINUA. Direccion NO RESUELTA."),
    (51, "D", None,
     "EL BARRIDO CASA UNA TECNICA CON LA DOCTRINA QUE LA REFUTA, y esta vez entre libros. El paso 1 de la madre es 'Centrar el proceso entre los limites de especificacion al iniciar' (PRE-Control, Juran); el hijo es el nodo de Deming que manda 'Nunca ajustar el proceso basandose en si un punto individual cae dentro o fuera de especificacion'. Es la misma especie que el par 32 del tramo 1 (el AQL de Juran contra la critica al AQL de Crosby). Cada lado trae su procedimiento: CONTINUA. Direccion NO RESUELTA."),
    (52, "D", "posicionamiento_por_tipo_de_mercado -> resegmentacion_mercado_nicho_bajo_costo",
     "Su paso 5, 'Si es re-segmentacion: comunicar comprension unica de un nicho o ventaja de bajo costo', es UNA LINEA, y el hijo trae el metodo entero: de que mercados existentes vendrian los clientes desatendidos, si pagarian mas o aceptarian menor desempenio por menor precio, que caracteristicas los harian abandonar a su proveedor, el mapa de mercado y la prueba cuantitativa del costo de cambio. La madre conserva los otros tres tipos de mercado (existente, nuevo y clon), que el hijo no toca."),
    (53, "D", "control_calidad_operaciones_servicio -> descubrir_necesidades_del_cliente",
     "El fragmento 'y las necesidades del cliente' de su paso 1 es UNA LINEA, y el hijo trae el procedimiento entero de descubrirlas: planificar los metodos de recoleccion, recopilar en el lenguaje del cliente, distinguir necesidades declaradas, reales, percibidas y culturales por segmento, investigar usos no previstos y sus riesgos, priorizar por consenso y traducir al lenguaje tecnico. La madre conserva los sujetos de control, los indicadores, los valores objetivo, la medicion y el troubleshooting."),
    (54, "D", None,
     "NO HAY PASO QUE CONTENGA AL HIJO. La madre es el nodo ancla del pack, el riesgo como disciplina permanente, y su paso 2 casado es 'Convierte la gestion de riesgo en un habito permanente'; el hijo es la GESTION DE LA CRISIS, o sea el momento en que el riesgo ya se volvio hecho, con su plan B y su contencion del danio. Habito contra respuesta: momentos distintos del mismo asunto. Procedimiento en los dos lados: CONTINUA. Direccion NO RESUELTA."),
    (55, "D", None,
     "FUENTES DE FONDOS DISTINTAS. El paso 3 casado es 'Evalua financiamiento de la SBA o Ex-Im Bank', o sea programas GUBERNAMENTALES; el hijo trabaja con la BANCA COMERCIAL: acercarse al banco habitual, ampliar la linea de capital de trabajo, buscar banco con departamento internacional y consultar tarifas de confirmacion de cartas de credito. El hijo hace algo adyacente al paso, no lo ejecuta. CONTINUA. Direccion NO RESUELTA."),
    (56, "D", None,
     "El paso 1 casado, 'Identificar todas las caracteristicas criticas de calidad del producto segun el cliente', pertenece a las definiciones operacionales de Deming, que acaban en cartas de control compartidas con el cliente; el hijo es la OPTIMIZACION DEL DISENIO de Juran: revisiones formales con especialistas externos, equipos multifuncionales, reglas de negociacion estructurada y herramientas como FMEA. No hay paso de la madre que contenga eso. CONTINUA. Direccion NO RESUELTA."),
    (57, "D", "autocontrol_y_controlabilidad -> capacidad_del_proceso",
     "Su paso 1, 'Verificar que el proceso tenga capacidad real para cumplir las metas fijadas', es UNA LINEA, y el hijo trae el procedimiento estadistico de verificarla: comprobar primero que el proceso este en control, calcular media y rango promedio del proceso estable, determinar la capacidad con las constantes d2 y A2, y comunicarla a disenio para ajustar especificaciones realistas. La madre conserva las otras tres condiciones de autocontrol, la lista de verificacion y el revisar si la culpa es del disenio antes de culpar a quien ejecuta. Que madre e hijo salgan de libros distintos (Juran y Deming) no cambia la vara."),
    (58, "D", "qfd_matriz -> identificar_clientes_externos_e_internos",
     "Su paso 2, 'Identifica a tus clientes internos y externos y descubre sus necesidades', es UNA LINEA, y el hijo trae el procedimiento: diagrama de flujo del proceso, listado de clientes externos por tipo (compradores, usuarios finales, comerciantes, procesadores, proveedores, potenciales y ocultos), identificacion de los internos por la relacion proveedor-procesador-cliente, distincion entre quien ordena y quien usa, y priorizacion consensuada. La madre conserva el encadenamiento de matrices y la transferencia a operaciones."),
    (59, "D", "requisitos_gates_con_dientes -> post_launch_review",
     "Su paso 6, 'Haz una revision despues del lanzamiento para confirmar que se cumplio lo prometido', es UNA LINEA, y el hijo trae la revision entera: comparar ventas, costos y ganancias reales contra las proyecciones, evaluar el desempenio del equipo, hacer la auditoria retrospectiva, documentar lecciones aprendidas y disolver el equipo transfiriendo el producto a la linea regular. La madre conserva las otras cinco condiciones para que un gate tenga fuerza."),
    (60, "D", None,
     "MISMA TENSION QUE EL 51, con los papeles cambiados. El paso 4 casado es de Deming, 'Si el sistema esta en control pero no cumple especificaciones, revisar el disenio del proceso o la especificacion misma'; el hijo es PRE-Control de Juran, que reacciona por zonas respecto a los limites de ESPECIFICACION, que es precisamente lo que ese paso desaconseja como reflejo. El hijo no ejecuta el paso. CONTINUA. Direccion NO RESUELTA."),
    (61, "D", "participacion_preferente -> seed_deals_riesgos_precedente",
     "Su paso 4, 'Recordar que los terminos de la ronda semilla suelen convertirse en precedente para rondas futuras', es UNA LINEA de advertencia, y el hijo trae el procedimiento de tratarla: evaluar si la valuacion obtenida es sostenible con el desempenio real, anticipar el crecimiento necesario y el impacto en rondas futuras, preferir un inversionista lider en vez de una ronda de fiesta, comunicar el riesgo de rondas a la baja a los semilla no sofisticados y evitar valuaciones infladas. La madre conserva los tres tipos de participacion y el calculo de escenarios de retorno."),
    (62, "D", "preservar_efectivo_buscar_modelo -> validar_modelo_negocio_hechos",
     "Su paso 1, 'No contrates equipo de ventas ni marketing hasta validar el modelo con hechos, no hipotesis', nombra en una linea una validacion que el hijo ejecuta entera: reunir las snapshots semanales del canvas, verificar casilla por casilla que cada componente tenga respuesta factica, recorrerlo con el checklist, identificar pruebas pass/fail por hipotesis y comprobar si se cumplen los objetivos de trafico o financieros. La madre conserva el test de escalabilidad, el burn rate, el presupuesto por experimento y la reserva para multiples pivotes."),
    (63, "D", None,
     "El paso 5 casado es de MEDICION ('Monitorear la reduccion del tiempo de entrega y la mejora en confiabilidad') como resultado de haber pasado a pull; el hijo es un ciclo generico de MEJORA (diagnosticar causas de consumo excesivo de tiempo, desarrollar remedios, medir su impacto) que no es lo que el paso pide. CONTINUA por el procedimiento propio de cada lado, direccion NO RESUELTA. Y se anota la figura: este hijo tiene un gemelo casi homonimo en el par 70."),
    (64, "D", "medicion_calidad -> clasificacion_seriedad_defectos",
     "Su paso 6, 'Clasificar los defectos por gravedad, causa y responsabilidad', es UNA LINEA, y el hijo trae el procedimiento: listar caracteristicas de calidad desde las especificaciones, listar aparte los defectos, definir categorias de seriedad (critico, mayor, menor) con quienes ayudan, aplicar la clasificacion para reducir lo que hay que verificar y validar con pilotos ante quienes se resistan. La madre conserva las metricas por area, la linea base, la publicacion en graficos y la revision diaria."),
    (65, "D", None,
     "EL HIJO ESTA POR ENCIMA DEL PASO, NO DENTRO. El paso 3 casado, 'Evalua financiamiento de la SBA o Ex-Im Bank', es una fuente concreta; el hijo da el marco general de decision de financiamiento de exportacion (si el financiamiento define el cierre de la venta, el plazo que pide el comprador, comparacion de tasas y comisiones, riesgo pais y capital de trabajo antes y despues del embarque), que aplica a cualquier fuente. No cabe entero dentro del paso. CONTINUA. Direccion NO RESUELTA, con sospecha de INVERSION anotada."),
    (66, "D", "cultura_justa_3 -> cultura_de_aprendizaje",
     "La clausula 'la proteccion al aprendizaje organizacional' de su paso 3 es UNA LINEA, y el hijo trae la maquinaria entera de esa clausula: mecanismos formales de analisis de los datos del sistema de reporte, procesos de decision para implementar reformas con tiempo y recursos comprometidos, medicion de la efectividad de las reformas e institucionalizacion de la revision de lecciones. La madre conserva las politicas de reporte que no penalizan la honestidad, el apoyo a segundas victimas y los criterios de conducta sancionable. ES UNA LECTURA DE FRONTERA y va marcada como discutible: el paso pide BALANCEAR dos cosas y el hijo solo entrega una de las dos."),
    (67, "D", None,
     "PAPELES OPUESTOS BAJO EL MISMO NOMBRE PROPIO. El paso 1 casado es 'Pide certificacion Energy Star en cada equipo que compres', o sea el papel de COMPRADOR; el hijo certifica TU PROPIO local o proyecto bajo LEED o Energy Star, o sea el papel de SOLICITANTE, con Portfolio Manager, puntos por categoria y expediente de evidencia. Comparten la etiqueta y nada mas. CONTINUA. Direccion NO RESUELTA."),
    (68, "D", None,
     "CRITERIO DE SELECCION DISTINTO. El paso 1 casado pide identificar las caracteristicas CORRELACIONADAS, que es lo que un grafico multivariado necesita; el hijo identifica y clasifica las caracteristicas CLAVE por importancia relativa y criticidad, y las registra en planos. Son dos cribas distintas sobre el mismo conjunto. CONTINUA por el procedimiento propio de cada lado, direccion NO RESUELTA."),
    (69, "D", None,
     "EL HIJO ES MAS GRANDE QUE EL PASO. El paso 6 casado, 'Actualizar el modelo de negocio con los costos de adquisicion reales descubiertos', pide actualizar UNA casilla del canvas; el hijo valida el canvas ENTERO casilla por casilla con datos facticos y pruebas pass/fail. No cabe dentro del paso. CONTINUA. Direccion NO RESUELTA. Se anota el contraste con el par 62, donde el MISMO hijo si cabe dentro del paso de OTRA madre: la diferencia es cual paso caso el barrido, no el hijo."),
    (70, "D", None,
     "SIN PARENTESCO. El paso 1 casado es 'Recolectar datos de desempenio del proceso en el tiempo', primer paso de una carta de control; el hijo son siete tacticas de reduccion de tiempo de ciclo (eliminar bucles de reproceso, simplificar pasos de valor marginal, quitar inspecciones redundantes, combinar pasos, bajar aprobaciones, paralelizar, automatizar). Es la senal mas debil del tramo, titulo_ratio 72,4. CONTINUA. Direccion NO RESUELTA."),
    (71, "D", None,
     "METAS CONTRA ACCIONES. El paso 3 casado es 'Establece metas de reduccion a corto y largo plazo' de EMISIONES; el hijo es un plan de ACCION de sostenibilidad a uno, tres y cinco anios (quick wins, pilotos, escalado, agenda por funcion, redisenio profundo). Comparten el eje temporal, no el objeto. CONTINUA. Direccion NO RESUELTA."),
    (72, "D", None,
     "El paso 4 casado, 'Emplear hojas de calculo de necesidades del cliente y de disenio de producto para vincular necesidades con caracteristicas', nombra un artefacto concreto; el hijo es la optimizacion del disenio (revisiones formales, equipos multifuncionales, negociacion estructurada, FMEA), que no es ese artefacto. CONTINUA. Direccion NO RESUELTA. Es la segunda fila de la bolsa que cuelga este mismo hijo de una madre que no es la suya, ver la nota de figuras."),
    (73, "D", "takt_time -> smed_setup_reduction",
     "Su paso 5, 'Reducir tiempos de cambio (setup) para permitir lotes mas pequenios', es UNA LINEA, y el hijo trae SMED entero: documentar el cambio actual, clasificar actividades en internas y externas, mover internas a externas, simplificar y estandarizar las internas restantes y eliminar la necesidad de ajustes y pruebas de ensayo. La madre conserva el calculo del takt, el balanceo de estaciones y la separacion de lineas de valor. Es de los encajes mas limpios del tramo."),
    (74, "D", "ingenieria_calidad_proveedores -> relaciones_largo_plazo_con_proveedores",
     "Su paso 4, 'Desarrollar relaciones de largo plazo con proveedores que permitan conocer su cultura de calidad real', es UNA LINEA, y el hijo trae el procedimiento de consolidacion: revisar cuantos proveedores hay por articulo clave, definir criterios con evidencia estadistica y no solo precio, reducir poco a poco hasta uno o muy pocos y formalizar acuerdos de largo plazo. La madre conserva involucrar a calidad desde el disenio conceptual, el papel de catalizador entre compras e ingenieria y el aviso contra las auditorias de visita rapida."),
    (75, "D", "dia_cero_defectos_2 -> eliminacion_causas_error_4",
     "Su paso 6, 'Iniciar al dia siguiente el programa de eliminacion de causas de error', es UNA LINEA que nombra un programa, y el hijo trae el sistema entero: canal con formulario que no exige proponer solucion, agradecimiento personal inmediato, clasificar y priorizar cada aviso, actuar rapido, justificar ante alguien de mas experiencia cuando se decide no actuar, y confirmar la decision a quien aviso. La madre conserva el dia de sugerencias previo, la carta explicativa, el evento y la firma del compromiso uno a uno."),
    (76, "D", None,
     "MISMOS ESTADOS FINANCIEROS, ASUNTO DISTINTO. El paso 6 casado es 'Entiende el impacto de la DEPRECIACION Y AMORTIZACION en tu estado de resultados y tu balance'; el hijo analiza el impacto cruzado de las DECISIONES OPERATIVAS (compras, ventas, contrataciones) sobre esos mismos dos estados, y no menciona depreciacion. El paso no contiene al hijo. CONTINUA. Direccion NO RESUELTA."),
    (77, "D", "desarrollo_expertos_capaces -> evaluacion_desempeno_proyectos",
     "El objeto de su paso 4, 'el desempenio de los proyectos de mejora', es UNA LINEA, y el hijo trae el tablero entero de medirlo: metricas de proyectos iniciados, en progreso, completados y abortados, valor generado en reduccion de costos y ROI, porcentaje de empleados activos en equipos de mejora y criterios cualitativos de contribucion individual. La madre conserva la linea base de competencias, el curriculo por rol y el programa de certificacion interno. ES UNA LECTURA DE FRONTERA y va marcada como discutible: el paso pide medir el impacto DE LA CAPACITACION sobre ese desempenio, y el hijo mide el desempenio sin cerrar ese vinculo causal."),
    (78, "D", "customer_discovery_phase2_problem_test -> captura_conocimiento_mercado",
     "Su paso 5, 'Capturar conocimiento competitivo y de mercado durante las entrevistas', es UNA LINEA que el hijo lleva por titulo, y trae el procedimiento entero: reunirse con empresas de mercados adyacentes e influenciadores, googlear el problema a fondo, investigar a cada competidor por dentro y por fuera, leer reportes de analistas, asistir a dos conferencias, construir el Competitive Grid y el Market Map, y conseguir demos de los competidores. La madre conserva el disenio de los experimentos de problema, la preparacion de contactos y la profundizacion en perfiles de cliente."),
    (79, "D", None,
     "USOS DISTINTOS DEL MISMO ARTEFACTO. El paso 4 casado es 'Dibuja el modelo de negocio (Business Model Canvas) de cada parte separada, como si fuera su propio negocio', que es el patron de desagregacion de Osterwalder; el hijo es la disciplina semanal del canvas de Blank (llenar las nueve areas, actualizar cada semana, resaltar cambios en rojo, conservar todas las versiones como flip book). Comparten el nombre del artefacto, no la operacion. CONTINUA. Direccion NO RESUELTA."),
    (80, "D", "estudio_desempeno_run_charts_servicios -> causas_comunes_vs_especiales",
     "Su paso 3, 'Construir graficos de corrida o distribuciones para detectar causas especiales de variacion', es UNA LINEA, y el hijo trae quince pasos que la ejecutan y la exceden: datos en orden cronologico, limites estadisticos, reglas de deteccion, investigacion inmediata de la senial, listado de causas comunes propias del sistema, accion distinta por tipo de causa y redisenio en vez de sancion. La madre conserva la identificacion de variables criticas del servicio y el dirigir recursos de capacitacion a las areas fuera de control."),
    (81, "D", None,
     "El paso 2 casado pide que la meta SMART sea medible en cuatro dimensiones (calidad, cantidad, costo y tiempo); el hijo es el paso 4 del programa de Crosby, el calculo del costo de la calidad como porcentaje de ventas contra el referente del 2,5 al 4 por ciento. Comparten la palabra costo. CONTINUA. Direccion NO RESUELTA."),
    (82, "D", None,
     "SOSPECHA DE INVERSION, y se declara en vez de forzar la direccion. El paso 2 casado es una TECNICA de estimacion ('identificar el costo total de la categoria y estimar el porcentaje atribuible a mala calidad'); el hijo es el PROGRAMA de costo de la calidad de Crosby, que es el marco dentro del cual esa tecnica se usaria, no al reves. El etiquetado de la bolsa pone de hijo al que parece el mayor. CONTINUA. Direccion NO RESUELTA."),
    (83, "D", "programa_mejora_calidad_14_pasos -> costo_de_calidad_3",
     "AQUI SI ES LA MADRE, Y ES LA TERCERA FILA SEGUIDA CON EL MISMO HIJO. Su paso 3, 'Definir como vas a medir la calidad y el costo de la no calidad', es UNA LINEA, y el hijo, que se titula literalmente 'Paso 4' del mismo programa de Crosby y sale del mismo libro, trae el procedimiento: informar a quien lleva las cuentas, sumar todos los componentes sin minimizar cifras, calcular el porcentaje sobre ventas y compararlo con el referente, priorizar prevencion sobre inspeccion, fijar meta de reduccion y volverlo medicion recurrente. La madre conserva los otros trece pasos del programa."),
    (84, "D", "liderazgo_ejecutivo_innovacion -> estrategia_innovacion_producto",
     "Su paso 1, 'Define y comunica tu vision y tu estrategia de innovacion conectadas con hacia donde va tu negocio', es UNA LINEA, y el hijo trae el documento entero: metas generales del esfuerzo de innovacion, rol de los nuevos productos en las metas del negocio, priorizacion de arenas estrategicas, asignacion de recursos entre arenas y planes de ataque por arena. La madre conserva los otros seis habitos del lider. Y SE ANOTA LA FIGURA: este hijo es gemelo casi homonimo de la madre del par 45."),
    (85, "D", None,
     "El paso 7 casado, 'Anota tu decision final: cambias de rumbo o sigues adelante', es el REGISTRO de la decision; el hijo es quien la conduce (participar en persona, no delegar en ventas ni marketing, escuchar el feedback negativo de primera mano, formar un equipo de apoyo que ejecuta pero no decide, retener la autoridad de pivotar). Ninguno cabe dentro del otro. CONTINUA. Direccion NO RESUELTA."),
    (86, "D", None,
     "METAS CONJUNTAS CONTRA METAS INTERNAS. El paso 4 casado es 'Fijar metas conjuntas de mejora' entre COMPRADOR Y PROVEEDOR; el hijo es el paso 10 de Crosby, dos metas por grupo interno a 30, 60 y 90 dias una semana despues del Dia de Cero Defectos. Otro libro y otra relacion. CONTINUA. Direccion NO RESUELTA, y se anota que la madre natural del hijo esta en la propia bolsa (par 83)."),
    (87, "D", "emprendedor_como_puesto_de_trabajo -> contabilidad_innovacion_pivote",
     "Su paso 2, 'Evalua ese trabajo con la contabilidad de innovacion, no con las metricas tradicionales de un puesto operativo', es UNA LINEA que nombra un metodo, y el hijo lo trae entero: documentar las hipotesis de salto de fe al inicio, medir metricas accionables (registro, activacion, retencion, referencia) en cada iteracion, comparar contra predicciones cuantitativas previas y no declarar exito retroactivamente con metricas de vanidad. La madre conserva la creacion del puesto, la reincubacion y la ampliacion gradual del sandbox."),
    (88, "A", "genchi_gembutsu_salir_del_edificio -> get_out_of_the_building",
     "El hijo cabe entero dentro del paso 2 de la madre, que hasta lo nombra en ingles ('lo que se llama get out of the building'), y la madre conserva las preguntas de fe, la observacion en contexto natural y el contraste con las hipotesis iniciales. Pero quitado lo que la madre ya dice, al hijo le quedan dos lineas sueltas ('lideralas tu mismo, no las delegues en personal junior' y 'evita hacer listas con todas las caracteristicas que te piden'), no una secuencia con logica propia. REPITE por 9.6.1, con la agravante de que son dos casas del mismo consejo en dos libros distintos."),
    (89, "D", None,
     "SOSPECHA DE INVERSION, declarada. El paso 2 casado, 'Minimizar el tiempo entre la emision de deuda convertible y su conversion a equity', es una mitigacion puntual de riesgo fiduciario; el hijo son los FUNDAMENTOS del instrumento (descuento, valuation cap, tasa, plazo de maduracion, monto de Qualified Financing, comparacion de costos legales contra una semilla preferente). Lo etiquetado como hijo parece la madre. CONTINUA. Direccion NO RESUELTA."),
    (90, "D", None,
     "DEFINICION CONTRA PROCEDIMIENTO DE OTRA COSA. El paso 1 casado es una definicion de que es calidad (caracteristicas del producto mas ausencia de fallos); el hijo es el procedimiento de identificar y clasificar las caracteristicas clave de producto y proceso. El paso no lo contiene. CONTINUA. Direccion NO RESUELTA. Segunda fila de la bolsa con este mismo hijo colgado de una madre que no es la suya."),
    (91, "D", "gestion_de_portafolio_gates_go_kill -> tipos_criterios_gate",
     "Su paso 2, 'Establecer gates o puntos de decision formales con criterios visibles de Go/Kill', es UNA LINEA, y el hijo trae el procedimiento: lista de preguntas must-meet eliminatorias para las primeras etapas, umbrales financieros minimos (NPV, IRR, Payback) para el Go/Kill en etapas avanzadas, scorecard para las should-meet, factores principales consistentes entre gates y adaptacion de los criterios por tipo de proyecto. La madre conserva el embudo, los seis criterios de evaluacion, el matar en firme y el balance del portafolio."),
    (92, "D", "etapa_build_business_case -> posicionamiento_por_tipo_de_mercado",
     "La clausula 'posicionamiento' de su paso 1 es UNA LINEA, y el hijo trae el metodo: identificar el tipo de mercado y aplicar el posicionamiento que corresponde a cada uno de los cuatro (existente, nuevo, clon, re-segmentado). La madre conserva la investigacion de mercado detallada, la VoC, la prueba de concepto, la evaluacion tecnica y el analisis financiero con NPV e IRR. SE ANOTA que este hijo es MADRE en el par 52: los dos juntos forman una cadena de tres niveles, que es forma sana y no gemelo."),
    (93, "D", "estandares_voluntarios -> definiciones_operacionales_de_calidad",
     "Su paso 3, 'Documentar el estandar con definiciones operacionales claras y medibles', es UNA LINEA, y el hijo trae el procedimiento: identificar las caracteristicas criticas segun el cliente, traducir con el cliente los requisitos subjetivos a metricas medibles, establecer cartas X-barra y R por caracteristica clave y compartir sus resultados de forma continua. La madre conserva la evaluacion de si hace falta regulacion obligatoria, la formacion de comites tecnicos, la promocion de la adopcion y el monitoreo de la presion regulatoria."),
    (94, "D", "testear_circulo_cuadrado_rectangulo -> validar_modelo_financiero",
     "Su paso 3, 'Finalmente, validar que el modelo de negocio completo (socios, canales, ingresos, costos) es viable (rectangulo)', es UNA LINEA, y el hijo trae la validacion entera: metricas de valor propuesto, costo de adquisicion, tasas de conversion y LTV, costos operativos y de canal con sus margenes, proyeccion de precio, ingresos y clientes por anio, runway, y el P y L, balance y flujo de caja multianual. La madre conserva los niveles del circulo y del cuadrado y la regla de no avanzar sin evidencia del anterior."),
    (95, "D", None,
     "EL FALSO AMIGO MAS LIMPIO DEL TRAMO, y por eso queda nombrado. El paso 5 casado es 'Definir ESPACIOS DE OPORTUNIDAD concretos para la empresa', salido de un analisis de mega-tendencias de Cooper; el hijo es el COSTO DE OPORTUNIDAD de un libro de finanzas, o sea comparar alternativas de uso del capital. Comparten la palabra oportunidad y nada mas: ni libro, ni dominio de fondo, ni objeto. CONTINUA. Direccion NO RESUELTA."),
    (96, "D", None,
     "EL HIJO ES ANTERIOR AL PASO, NO INTERIOR. El paso 3 casado es 'Probar canales de ventas y distribucion', que es Customer Validation; el hijo es la HIPOTESIS de canal, que es Customer Discovery y va antes (elegir fisico, digital o hibrido, evaluar precio contra canal, calcular costos del canal, seleccionar UNO y recalcular el ingreso neto). Sus propias fases lo dicen: la madre es validacion y el hijo planificacion. CONTINUA. Direccion NO RESUELTA."),
    (97, "D", "principios_alineacion_empresarial -> desarrollar_estrategias_largo_plazo",
     "Su paso 3, 'Alinear estrategias, sistemas y metas de largo plazo con el proposito central', es UNA LINEA, y el hijo trae el procedimiento de tener esas estrategias: evaluar las cinco areas clave (satisfaccion del cliente, costos de mala calidad, cultura, procesos internos y comparacion con la competencia), analizar los datos en un FODA, definir de 4 a 5 estrategias que aporten a la vision y asignar responsable a cada una. Ese 'que aporten de verdad a tu vision' es la alineacion que el paso pide, y por eso el hijo cabe dentro. La madre conserva la definicion de vision, proposito y valores, el mapa de interdependencias y la correccion de silos."),
    (98, "D", "control_del_proceso_del_proveedor -> buenas_practicas_manufactura_cgmp",
     "Su paso 3, 'Definir tareas especiales y buenas practicas de manufactura requeridas', es UNA LINEA, y el hijo trae el sistema cGMP entero: sistema robusto de gestion de calidad, procedimientos operativos estandarizados y validados, deteccion e investigacion de desviaciones, laboratorios calibrados y actualizacion continua de tecnologias para seguir siendo current. La madre conserva los otros ocho requisitos del plan, incluidos SPC, clasificacion de seriedad, estandares sensoriales, metodos de prueba y trazabilidad de lotes."),
    (99, "D", "juran_rcca_metodo -> prueba_teorias_causa_raiz",
     "La clausula 'formular teorias, probarlas' de su paso 2 es UNA LINEA, y el hijo trae el procedimiento: seleccionar las teorias mas probables del diagrama de causa y efecto, disenar y recolectar datos especificos para cada una, analizarlos para confirmarlas o descartarlas, repetir el por que hasta una causa raiz controlable y verificar que no queden teorias alternativas plausibles sin descartar. La madre conserva definir el problema, mejorar y controlar, que son sus otros tres pasos."),
    (100, "A", "desarrollar_metas_anuales -> metas_negocio_calidad",
     "El hijo cabe dentro del paso 3 ('Filtra y prioriza las metas que entraran en tu plan de negocio') y la madre conserva la revision de las siete areas clave y la recoleccion de propuestas de todos. Pero quitado lo que la madre ya dice, casi no queda nada: el paso 1 de la madre ya barre las areas (incluido el costo de mala calidad), su paso 5 ya exige que cada meta sea especifica, medible y con plazo, y su paso 3 ya las mete en el plan de negocio. Al hijo le queda el encuadre 'amenazas y oportunidades estrategicas relacionadas con calidad', que es UNA LINEA. REPITE por 9.6.1."),
]

# LAS FIGURAS DEL TRAMO. NO son veredictos de par y NO SE ADJUDICAN aqui: las
# sospechas de gemelos entre nodos son otra pregunta y otra operacion (encargo de
# la vuelta 97, literal: "Si el tramo 2 destapa figuras nuevas, mismo trato").
FIGURAS = [
    ("LOS GEMELOS DE LA ESTRATEGIA DE INNOVACION, y el tramo los trae LOS DOS",
     "estrategia_de_innovacion_de_producto es la MADRE del par 45 y estrategia_innovacion_producto "
     "es el HIJO del par 84. Los ids se diferencian en dos preposiciones, los titulos en las "
     "palabras 'y Tecnologia', el libro es el mismo (Cooper) y el contenido se solapa casi entero: "
     "metas de innovacion vinculadas a las del negocio, arenas estrategicas priorizadas y "
     "asignacion de recursos estan en los dos. CORROBORA desde un segundo camino la figura que el "
     "tramo 1 ya registro ('los dos de estrategia de innovacion, uno haciendo de madre y otro de "
     "hijo'), y esta vez los dos papeles se ven dentro del MISMO tramo."),
    ("LOS GEMELOS DEL TIEMPO DE CICLO",
     "reduccion_de_tiempo_de_ciclo (par 63, 3 pasos, 'Reduccion del Tiempo de Ciclo') y "
     "reduccion_tiempo_ciclo (par 70, 7 pasos, 'Reduccion del Tiempo de Ciclo del Proceso'). Ids "
     "que se diferencian en una preposicion, mismo libro (Juran), mismo titulo salvo dos palabras. "
     "Es la misma especie que la familia de la capacidad de proceso que el tramo 1 registro."),
    ("LA FAMILIA CROSBY DE LOS 14 PASOS, REPARTIDA EN LA BOLSA Y MAL EMPAREJADA",
     "costo_de_calidad_3 ('Paso 4'), fijacion_de_metas ('Paso 10'), dia_cero_defectos_2 (el Dia ZD) "
     "y eliminacion_causas_error_4 (ECR) son capitulos numerados del mismo programa de Crosby, cuya "
     "madre es programa_mejora_calidad_14_pasos. En la bolsa aparecen colgados de madres ajenas: el "
     "costo_de_calidad_3 sale TRES filas seguidas (81, 82 y 83) con tres madres distintas y la "
     "misma senial 84,4, y solo la del 83 es la suya; fijacion_de_metas (86) cuelga de un equipo "
     "comprador-proveedor de Juran. Quien cablee esta zona tiene la madre verdadera dentro de la "
     "propia bolsa."),
    ("LOS NODOS IMAN: un hijo que el barrido cuelga de varias madres sin serlo",
     "costo_de_calidad_3 en las filas 81, 82 y 83; optimizacion_caracteristicas_diseno en la 56 y "
     "la 72; key_process_product_characteristics en la 68 y la 90; validar_modelo_negocio_hechos en "
     "la 62 y la 69; y recursos_apoyo_gubernamental_exportacion haciendo de madre con el MISMO paso "
     "3 en la 55 y la 65. Es una propiedad del barrido que conviene tener escrita antes de leer los "
     "83 que quedan: un titulo fuerte atrae varias filas y como mucho una es la real."),
    ("EL MISMO NODO DE MADRE EN UNA FILA Y DE HIJO EN OTRA, y hay que separar DOS casos",
     "pre_control_estadistico es madre en la 51 e hijo en la 60, y ahi SI es figura, porque las dos "
     "filas son falsos amigos. posicionamiento_por_tipo_de_mercado es hijo en la 92 y madre en la "
     "52, y ahi NO es figura: las dos filas juntas dibujan una CADENA de tres niveles "
     "(etapa_build_business_case, posicionamiento_por_tipo_de_mercado, "
     "resegmentacion_mercado_nicho_bajo_costo), que es la forma sana que el caveat de la 9.6.1 ya "
     "nombra. Se registran juntas para que no se confundan."),
    ("EL TRIO DE SALIR DEL EDIFICIO, en dos libros",
     "get_out_of_the_building (Blank), genchi_gembutsu_salir_del_edificio (Ries) y "
     "customer_discovery_get_out_of_building (Blank, madre del par 46) son tres casas para la misma "
     "idea. El par 88 enfrenta a dos de ellos y sale A. Misma clase de sospecha que el trio Make "
     "Certain del tramo 1, y con la agravante de que cruza dos autores."),
    ("EL FALSO AMIGO POR NOMBRE PROPIO COMPARTIDO",
     "El barrido casa por token y no por contenido: 'NDA' en la 44 (la madre dice NUNCA pidas NDA a "
     "un VC y el hijo dice EXIGE NDA bidireccional al comprador), 'Energy Star' en la 67 (comprar "
     "equipos con la etiqueta contra certificar tu propio local) y 'Business Model Canvas' en la "
     "79. El ejemplar mas limpio es la 95: 'espacios de oportunidad' de un analisis de "
     "mega-tendencias contra 'costo de oportunidad' de un libro de finanzas. No comparten nada "
     "salvo la palabra."),
    ("EL BARRIDO VUELVE A CASAR UN PASO CON SU REFUTACION, y ahora es una escuela contra otra",
     "El tramo 1 registro el AQL de Juran contra la critica al AQL de Crosby. Aqui hay DOS filas de "
     "la misma especie y las dos entre Juran y Deming, con pre_control_estadistico en medio: la 51 "
     "(PRE-Control centra el proceso entre los limites de ESPECIFICACION, y el nodo de Deming manda "
     "no ajustar nunca por si un punto cae dentro o fuera de especificacion) y la 60 (el mismo "
     "PRE-Control colgado de un nodo de Deming sobre variacion en servicios). No es un defecto del "
     "barrido: es material real de dos escuelas en tension, y quien cablee esta zona tiene que "
     "saberlo antes de poner una arista."),
    ("UN NODO DE QUINCE PASOS QUE PARECE DOS CASAS",
     "causas_comunes_vs_especiales (par 80) tiene 15 pasos_accionables: del 1 al 9 son mecanica de "
     "control estadistico (datos cronologicos, limites, reglas de deteccion, causas comunes del "
     "sistema) y del 10 al 15 son cultura de no buscar culpables (comunicar 'el problema' y no "
     "'quien lo causo', seguimiento de la moral del equipo, colaboracion entre turnos). Se registra "
     "SIN adjudicar: partir un nodo es otra pregunta y otra operacion."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-escribir", action="store_true")
    a = ap.parse_args()

    filas, fallos, total_bolsa = construir_filas(VEREDICTOS, DESDE, CUANTOS)
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
    print("OP-E-03, VEREDICTOS DEL SEGUNDO TRAMO (vuelta 97, TAREA 2)")
    print("Bolsa de %d filas; este tramo lee las filas %d a %d (%d pares)."
          % (total_bolsa, DESDE + 1, DESDE + len(filas), len(filas)))
    print("Vara: banco 9.6.1 (clase), 9.6.2 (direccion), 9.6.3 (el solape no decide).")
    print("EL UMBRAL DE DIRECCION ES EL MISMO DEL TRAMO 1 (acta 96 seccion 4.4, linea 34367).")
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
    print("ENUMERACION 'direccion leida' (%d): %s"
          % (len(con_direccion), ", ".join(str(f["puesto_tramo"]) for f in con_direccion)))
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
    print("FIGURAS OBSERVADAS EN EL TRAMO (%d). No son veredictos de par y NO SE ADJUDICAN." % len(FIGURAS))
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
