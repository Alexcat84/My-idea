# -*- coding: utf-8 -*-
r"""vuelta98_tarea4_juicios.py . LOS JUICIOS DE LECTURA DEL TERCER TRAMO DE
OP-E-03 (vuelta 98, TAREA 4).

AQUI SOLO VA LO QUE UN INSTRUMENTO NO PUEDE DAR: la CLASE del banco 9.6.1, la
DIRECCION del 9.6.2 y la RAZON. Todo lo demas (dominio, ids de madre e hijo,
paso casado, las cuatro marcas de LECTURA DIRIGIDA) lo parsea
scripts/loop/vuelta98_tarea4_escribir_tramo3.py de la salida del instrumento de
lectura, PARA QUE NINGUN ID SE TECLEE.

La direccion se escribe "madre -> hijo" con los ids TAL COMO el material los
nombra; el escritor CAE en rojo si un id de la direccion no es la madre ni el
hijo de esa fila segun el material, que es la guarda que hace imposible colar un
id tecleado mal.

direccion None significa NO RESUELTA, y se declara como tal.

SE DECLARA, Y NO SE FABRICA (EJECUTOR.md regla 1): la CLASE y la DIRECCION de
cada par son LECTURA A MANO contra el grafo. NO TIENEN CASO ROJO AUTOMATICO,
porque no hay dentro del repo una segunda fuente independiente contra la que
contrastarlas. Su control es la relectura ciega del auditor, no un assert. Lo
que si tiene prueba de mutacion son las GUARDAS del escritor.
"""

JUICIOS = {

    101: {
        "clase": "D",
        "direccion": "rol_alta_direccion_calidad -> metas_negocio_calidad",
        "razon": (
            "El paso 2 de la madre ('Definir estrategias y metas de calidad alineadas "
            "con tu vision del negocio') dice QUE hacer y ni una palabra de COMO. El "
            "hijo tarda tres pasos en ejecutarlo: identificar amenazas y oportunidades "
            "estrategicas de calidad, traducirlas a metas cuantificadas con plazo, e "
            "incorporarlas formalmente al plan de negocio. Diagnostico, cuantificacion "
            "e incorporacion, con dependencia entre ellos. La madre conserva materia "
            "propia que el hijo no toca en ningun paso: el espacio de revision de "
            "calidad, la asignacion de recursos, la participacion personal en los "
            "equipos de problemas cronicos, la revision periodica y el reconocimiento. "
            "La senial de los entregables del 9.6.2 lo confirma: la madre entrega un "
            "compromiso documentado del director, el hijo una seccion de metas dentro "
            "del plan de negocio, que es lo que el paso 2 produce al ejecutarse. "
            "Procedimiento en un solo sentido: tercera fila del 9.22, CONTINUA."
        ),
    },

    102: {
        "clase": "D",
        "direccion": "brecha_de_calidad_cuatro_gaps -> necesidades_reales_vs_declaradas",
        "razon": (
            "El paso 1 de la madre ('Evaluar el nivel actual de comprension de las "
            "necesidades reales del cliente') nombra la evaluacion sin decir como se "
            "hace. El hijo la ejecuta en cuatro pasos con logica propia: preguntar por "
            "que compra y que servicio espera, traducir lo declarado a lo real, evitar "
            "centrarse en el producto ignorando la funcion, y redisenar la propuesta de "
            "valor sobre la necesidad real. La madre conserva materia propia intacta: "
            "las otras tres brechas (diseno, capacidad de proceso y auditoria de la "
            "operacion diaria), que el hijo no toca. Procedimiento en un solo sentido, "
            "tercera fila del 9.22: madre e hijo, CONTINUA. El 9.6.3 se aplica y no "
            "cambia nada: lo que decide no es cuanto solapan sino que queda fuera y de "
            "que lado, y fuera queda un procedimiento de un lado y tres brechas del otro."
        ),
    },

    103: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y la razon es que el hijo no ejecuta el paso de la madre sino "
            "que actua sobre el mismo objeto con OTRA accion. El paso 3 de la madre dice "
            "'PRESUPUESTA el desarrollo de tu manual de operaciones', y el hijo no "
            "presupuesta nada: DESARROLLA el manual en seis pasos y entrega el manual "
            "mismo, redactado y revisado legalmente. El test de reconocimiento del 9.6.2 "
            "('el hijo cabe entero dentro de UN paso de la madre') NO se cumple, porque "
            "presupuestar no es construir. Que exista dependencia entre las dos cosas (no "
            "se presupuesta bien lo que no se ha alcanzado) es relacion de flujo de "
            "trabajo, no relacion de linea contra procedimiento, y afirmar direccion aqui "
            "seria inventar una relacion que la vara no entrega, que es exactamente lo "
            "que el acta 97 seccion 3.5 confirmo como prudencia. El par CONTINUA: los dos "
            "conservan materia propia entera y no hay duplicacion. FIGURA REGISTRADA: el "
            "barrido caso por el OBJETO compartido ('manual de operaciones') y no por la "
            "accion, y su propia senial lo delata, porque etiqueta el paso de la madre "
            "como familia CONSTRUIR cuando 'presupuesta' no construye nada."
        ),
    },

    104: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por LINEA COMPARTIDA Y PROCEDIMIENTO PROPIO A CADA LADO, que es "
            "el caso que el propio 9.6.2 nombra en su ejemplar del puesto 2.195. La linea "
            "compartida esta escrita casi igual en los dos: paso 1 de la madre "
            "('Enfocate en validar un solo canal de distribucion antes de expandirte') y "
            "paso 5 del hijo ('Enfocarse en UN canal principal durante el customer "
            "discovery'). Pero ninguno DESPLIEGA la linea del otro: la madre sigue hacia "
            "MAPEAR la cadena (dibujar los eslabones, documentar responsabilidades, "
            "calcular descuentos y margenes, disenar el plan de gestion) y el hijo sigue "
            "hacia SELECCIONAR el canal (habitos de compra, si el canal fortalece la "
            "venta y a que costo, complejidad y precio, recalculo de ingresos netos). Dos "
            "procedimientos distintos colgados de la misma linea. No hay madre ni hijo, y "
            "no es la figura del 9.22 tampoco, porque el 9.22 exige que cada uno expanda "
            "una linea DEL OTRO y aqui ninguno expande nada del otro. CONTINUA."
        ),
    },

    105: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA. El test de reconocimiento del 9.6.2 falla por los dos extremos: "
            "el hijo NO cabe dentro de un solo paso de la madre, porque su material se "
            "reparte entre el paso 2 de ella ('analiza la causa raiz de los defectos') y "
            "el paso 4 ('redisena tu proceso de produccion para construir calidad desde "
            "el origen'), y ademas anade materia que la madre no tiene en ningun paso "
            "(definir los requisitos del cliente ANTES de disenar, y documentar los "
            "procedimientos que garantizan ese diseno). La madre tampoco despliega ninguna "
            "linea del hijo: su procedimiento es el desmontaje de la inspeccion masiva "
            "(medir su costo, muestreo aleatorio, reduccion gradual, 100 por ciento solo "
            "en criticos), que el hijo no nombra. Los dos son nodos del mismo libro sobre "
            "la misma doctrina, con solape parcial y materia propia a cada lado. CONTINUA. "
            "FIGURA REGISTRADA: la madre de este par y la del par 123 son casi homonimas "
            "del mismo libro ('Abolicion de la Inspeccion Masiva como Estrategia de "
            "Calidad' contra 'Sustitucion de la Inspeccion Masiva por Control "
            "Estadistico'): sospecha de gemelos, SIN ADJUDICAR."
        ),
    },

    106: {
        "clase": "D",
        "direccion": "activity_attributes -> assumption_constraint_log",
        "razon": (
            "El paso 4 de la madre ('Especificar restricciones y supuestos por actividad') "
            "es una instruccion pelada: dice QUE registrar y nada de COMO. El hijo tarda "
            "cinco pasos en ejecutarla y son una secuencia con logica propia y con "
            "dependencia entre eslabones: identificar y categorizar los supuestos, "
            "documentar las restricciones segun su origen (charter, cliente, regulador), "
            "asignar responsable y fecha limite para validar cada uno, registrar acciones "
            "y estado, y actualizar el log conforme se validan o invalidan. Es la "
            "formulacion literal del 9.6.2: una linea que tarda cinco pasos en ejecutarse "
            "no es una linea, es un procedimiento nombrado en una linea. La madre conserva "
            "materia propia que el hijo no toca: predecesoras y sucesoras, tipo de "
            "relacion logica, leads y lags, y requisitos de recursos y habilidades. "
            "Procedimiento en un solo sentido: CONTINUA."
        ),
    },

    107: {
        "clase": "D",
        "direccion": "juran_quality_by_design -> diseno_controles_proceso_mejorado",
        "razon": (
            "Caso de manual del 9.6.2. El paso 6 de la madre ('Desarrolla controles de "
            "proceso, documenta cada etapa y transfiere el diseno a operaciones') nombra "
            "el desarrollo de los controles sin una palabra de como, y el hijo entero es "
            "el procedimiento de seis pasos que lo hace: actualizar el FMEA para "
            "identificar los controles necesarios, aplicar mistake-proofing, disenar los "
            "controles para las Xs y las Ys, establecer estandares basados en el desempeno "
            "real, determinar como se comparara el desempeno contra el estandar por SPC, y "
            "establecer el autocontrol de los responsables. La madre conserva materia "
            "propia entera y el hijo no toca ninguna: decidir si el modelo sera continuo o "
            "puntual, fijar metas del diseno, definir mercado y clientes objetivo, "
            "descubrir necesidades y desarrollar las caracteristicas. Los entregables lo "
            "confirman: la madre entrega el plan de diseno con las seis etapas, el hijo el "
            "plan de control, que es el producto de su paso 6. CONTINUA."
        ),
    },

    108: {
        "clase": "D",
        "direccion": "analisis_de_ratios_financieros -> gestion_dso",
        "razon": (
            "El paso 4 de la madre nombra el DSO como una linea de calculo entre siete "
            "ratios ('Calcular ratios de eficiencia: rotacion de activos y dias de ventas "
            "pendientes de cobro'). El paso 1 del hijo es exactamente ese calculo, y lo "
            "que sigue es residuo con logica propia y dependencia: investigar con "
            "operaciones si hay problemas de calidad o entrega que retrasen pagos, "
            "consultar a ventas sobre la salud financiera de los clientes, definir "
            "politicas de credito concretas (terminos, 2/10 net 30) y fijar el perfil de "
            "cliente al que se otorga credito. Diagnostico, consulta y politica: no son "
            "lineas sueltas, cada una consume lo anterior. La madre conserva materia "
            "propia intacta: rentabilidad, apalancamiento, liquidez, comparacion "
            "historica y sectorial, y la indagacion de los ratios fuera de rango. "
            "Procedimiento en un solo sentido, tercera fila del 9.22: CONTINUA. El 9.6.3 "
            "no lo cambia: lo que decide no es cuanto solapan sino que queda fuera y de "
            "que lado."
        ),
    },

    109: {
        "clase": "D",
        "direccion": "business_model_canvas_scorecard -> key_partners_hypothesis",
        "razon": (
            "El paso 1 de la madre nombra las NUEVE areas del canvas de un tiron "
            "('segmentos, propuesta de valor, canales, relaciones, recursos, socios e "
            "ingresos') y el hijo despliega UNA de esas nueve en seis pasos: listar los "
            "socios primarios y sus suplentes clasificados en cuatro tipos, definir en "
            "tabla que provee cada uno y que recibe a cambio, evaluar su flexibilidad en "
            "tiempos, pedidos, credito y precio, distinguir socios de recursos clave, "
            "actualizar el canvas y planear la validacion con reuniones reales. El hijo "
            "cabe entero dentro de ese paso 1 y la madre conserva materia propia que el "
            "hijo no toca: la actualizacion semanal, el resaltado en rojo de los cambios, "
            "la integracion al canvas base, el flip book y el aviso de no convertirlo en "
            "plan operativo prematuro. Test de reconocimiento del 9.6.2 cumplido por los "
            "dos lados: CONTINUA."
        ),
    },

    110: {
        "clase": "D",
        "direccion": ("emprendimiento_como_disciplina_de_gestion -> "
                      "emprendedor_como_puesto_de_trabajo"),
        "razon": (
            "El paso 6 de la madre ('Tratar el rol de emprendedor como una funcion formal "
            "y reconocida dentro de la organizacion') es una instruccion pelada sin una "
            "palabra de como, y el hijo tarda cuatro pasos en ejecutarla: crear el puesto "
            "real de Emprendedor Interno, evaluarlo con contabilidad de innovacion en vez "
            "de metricas operativas, dejar que quien lo ocupa entrene un equipo nuevo y "
            "vuelva a incubar cuando el producto crezca, y ampliar el sandbox por "
            "resultados en vez de sacarlo de golpe. Es la misma forma exacta que el par 42 "
            "del tramo 2, que esta vuelta se movio de A a D por relectura conjunta, y se "
            "lee igual por consistencia. La madre conserva materia propia entera: los "
            "cinco pasos sobre la disciplina de gestion, que el hijo no toca. Es la "
            "formulacion literal del 9.6.2 (una linea que tarda cuatro pasos en "
            "ejecutarse es un procedimiento nombrado en una linea) y la tercera fila del "
            "9.22: CONTINUA."
        ),
    },

    111: {
        "clase": "C",
        "direccion": ("limites_especificacion_funcionales -> ctq_caracteristicas_criticas"),
        "razon": (
            "FIGURA DEL 9.22, PRIMER POLO: PROCEDIMIENTO EN LOS DOS SENTIDOS SOBRE DOS "
            "LINEAS DISTINTAS, y por eso C y no D. Sentido A hacia B: el paso 1 de la "
            "madre ('Identifica que caracteristicas son criticas para que tu producto "
            "funcione') es una linea, y el hijo entero es el procedimiento que la ejecuta "
            "(recoger la voz del cliente, traducirla a terminos tecnicos y medibles, "
            "definir metrica, unidad y limites por cada CTQ, priorizar por impacto en "
            "satisfaccion y usar las CTQ para comparar alternativas de diseno). Sentido B "
            "hacia A, y sobre OTRA linea, que es lo que el 9.22 exige: el paso 3 del hijo "
            "('Define para cada CTQ una metrica, una unidad de medida y los limites "
            "aceptables') es una linea, y la madre entera es el procedimiento que la "
            "ejecuta (disenar pruebas que relacionen la variacion del componente con el "
            "desempeno, construir diagramas de dispersion y ecuaciones de regresion, fijar "
            "los limites de tolerancia sobre esos datos dentro de margenes de confianza, y "
            "verificar que la muestra basta y el proceso esta bajo control). LA "
            "COMPROBACION QUE EL 9.22 EXIGE PARA SEPARARLA DE LA DUPLICACION: las dos "
            "direcciones NO apuntan a la misma linea. Una apunta a 'cuales son criticas' y "
            "la otra a 'con que limites'. El arreglo que la figura prescribe es ENLACE "
            "MUTUO, dos aristas, y NO fusion, que borraria los dos procedimientos. NO SE "
            "ESCRIBE NINGUNA ARISTA: OP-E-03 es LECTURA DIRIGIDA y su producto es el "
            "juicio. La direccion se registra como madre hacia hijo por ser la del primer "
            "sentido, y se DECLARA que en esta clase la relacion es mutua."
        ),
    },

    112: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por FALSO AMIGO. El paso 6 de la madre dice 'Orientar al equipo "
            "sobre el contenido y proposito del PROGRAMA DE CALIDAD', que en Crosby es el "
            "programa de mejora de calidad de la empresa; el hijo define el proposito y el "
            "alcance de un PROGRAMA DE AUDITORIA de calidad, de otro libro (Juran), y sus "
            "cuatro pasos (orientar a cumplimiento o efectividad, decidir auditor interno "
            "o externo, fijar el alcance, documentar proposito y reglas) no orientan a "
            "nadie sobre el programa de la madre: constituyen otro programa. El barrido "
            "caso por los tokens compartidos 'programa', 'calidad' y 'proposito'. El test "
            "de reconocimiento del 9.6.2 no se cumple en ningun sentido y ninguno de los "
            "dos despliega una linea del otro, asi que tampoco es la figura del 9.22. "
            "CONTINUA, y la direccion no se afirma porque no hay relacion que dar la vuelta."
        ),
    },

    113: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y ademas es la tercera aparicion de la especie que casa un paso "
            "con su propia REFUTACION, esta vez Blank contra Ries. El paso 1 de la madre "
            "manda 'Despliega una version de ALTA FIDELIDAD de tu MVP', y el hijo, de otro "
            "libro, manda lo contrario en su paso 2 ('Considera hacer antes una prueba "
            "rapida de interes, smoke test, antes de invertir mas recursos'): el hijo no "
            "ejecuta la linea de la madre, la discute. Ademas su fin es otro (fijar la "
            "linea base de metricas, no validar el modelo de negocio) y su materia propia "
            "(identificar la suposicion mas riesgosa y probarla primero, recolectar "
            "conversion, registro, prueba y valor de vida) no cabe dentro de ese paso 1. "
            "Ni test de reconocimiento del 9.6.2 ni figura del 9.22: CONTINUA con "
            "direccion no afirmada, que es el suelo correcto cuando la vara no entrega "
            "relacion, segun la adjudicacion 3.5 del acta 97."
        ),
    },

    114: {
        "clase": "D",
        "direccion": "economia_de_la_experiencia -> ejecucion_de_touchpoints",
        "razon": (
            "DIRECCION INVERTIDA respecto a la etiqueta de la bolsa, y afirmada, que es el "
            "mismo gesto que el par 16 del tramo 1. Lo que la bolsa llama hijo es la "
            "madre. La linea esta en economia_de_la_experiencia, paso 4 ('Evaluar la "
            "ejecucion del detalle, calidad, distribucion, precio, diseno fisico, ya que "
            "fallas de ejecucion destruyen buenas ideas'), y el procedimiento que la "
            "ejecuta es ejecucion_de_touchpoints entero, sus cuatro pasos: identificar "
            "todos los touchpoints, disenar cada detalle sensorial visual, sonoro y tactil, "
            "probar la consistencia en escenarios repetidos y ajustar los detalles menores "
            "que arruinan la percepcion de calidad. En el sentido que la bolsa etiquetaba "
            "NO hay procedimiento: el paso 1 de ejecucion_de_touchpoints ('Identificar "
            "todos los touchpoints') no lo despliega el hijo, que solo mapea los "
            "touchpoints donde el usuario pasaria de consumo pasivo a participacion "
            "activa, que es un subconjunto con otro criterio. Aqui SI hay linea de un lado "
            "y procedimiento del otro, que es lo que faltaba en los pares 82, 89 y 65 del "
            "tramo 2 y por lo que alli no se afirmo la inversion. Procedimiento en un solo "
            "sentido, tercera fila del 9.22: CONTINUA."
        ),
    },

    115: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por LINEA COMPARTIDA Y PROCEDIMIENTO PROPIO A CADA LADO, el caso "
            "del puesto 2.195 que el 9.6.2 nombra. La linea compartida es el rechazo de la "
            "estandarizacion: paso 2 de la madre ('Evaluar si las soluciones actuales "
            "tienden a la estandarizacion que erosiona esa diversidad') y paso 2 del hijo "
            "('Evitar soluciones universales talla unica que ignoren las condiciones "
            "especificas del lugar'). Pero ninguno despliega al otro: la madre sigue hacia "
            "el soporte activo de la diversidad (identificar los elementos relevantes y "
            "disenar mecanismos cientificos y logisticos de preservacion) y el hijo sigue "
            "hacia el diseno adaptado al contexto (analizar clima, cultura y recursos, "
            "sistemas multifuncion tipo policultivo, resiliencia ante perturbaciones, "
            "nichos funcionales y flujos de energia y materiales del entorno). Del mismo "
            "libro y sobre el mismo principio, con materia propia a cada lado. CONTINUA."
        ),
    },

    116: {
        "clase": "D",
        "direccion": "metodologia_spin_selling -> preguntas_need_payoff",
        "razon": (
            "El caso mas limpio del tramo, porque la madre ANUNCIA AL HIJO EN SU PROPIO "
            "TEXTO: el paso 3 dice 'Prepararse para usar preguntas de Situacion, Problema, "
            "Implicacion y Necesidad-Beneficio (SE DETALLAN EN CAPITULOS POSTERIORES)'. Esa "
            "coletilla es, dentro del propio material, la prueba que el 9.6.2 pide de que "
            "el paso de la madre es un procedimiento nombrado en una linea: existe el hijo "
            "que lo ejecuta, y el libro lo dice. El hijo despliega una de las cuatro clases "
            "de pregunta en seis pasos con dependencia entre ellos: esperar a que el "
            "cliente reconozca una necesidad explicita, preguntar si resolverla seria "
            "valioso, pedirle que explique por que, explorar beneficios adicionales, evitar "
            "usarlas al inicio o sobre necesidades que no se pueden cubrir, y guardar sus "
            "palabras para el cierre. La madre conserva materia propia que el hijo no toca: "
            "diagnosticar venta pequena contra grande, abandonar el cierre agresivo y medir "
            "el impacto de la investigacion. CONTINUA."
        ),
    },

    117: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA. Son dos METODOS ALTERNATIVOS para el mismo fin, no madre e hijo. "
            "El paso 3 de la madre ('Leer el plan de muestreo correspondiente en la tabla "
            "maestra') pertenece al camino de la norma ANSI/ASQC Z1.4: determinar AQL, "
            "tamano de lote y nivel de inspeccion, buscar la letra de codigo, leer el plan, "
            "y aplicar las reglas de cambio a inspeccion estricta o reducida. El hijo NO "
            "lee ninguna tabla: disena el plan desde principios economicos y estadisticos "
            "(promedio de proceso del proveedor, costo del dano por defectos no detectados, "
            "balance entre inspeccion al 100 por ciento y muestreo, curva caracteristica de "
            "operacion y errores de medicion). Ninguno despliega una linea del otro; son "
            "dos rutas para llegar a un plan de muestreo, asi que el test de reconocimiento "
            "del 9.6.2 no se cumple en ningun sentido y tampoco es la figura del 9.22. "
            "CONTINUA. FIGURA REGISTRADA: "
            "titulo_ratio 86,3, el mas alto del tramo, sobre titulos casi sinonimos "
            "('Seleccion y Aplicacion de Planes de Muestreo' contra 'Planes de Muestreo de "
            "Aceptacion') que NO son gemelos, porque su contenido es complementario y no "
            "repetido. Es un falso gemelo por titulo, y avisa de que el titulo_ratio alto "
            "no implica duplicacion."
        ),
    },

    118: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por FALSO AMIGO, y de dos libros distintos. El paso 2 de la madre "
            "('Evalua como queda compuesta la junta en cada ronda antes de firmar los "
            "terminos del acuerdo') habla de la COMPOSICION DEL BOARD; el hijo habla de la "
            "CLAUSULA DE DIVIDENDOS del mismo documento (acumulativo o no, su porcentaje, "
            "el efecto si el negocio va bien o mal, exigir mayoria amplia del consejo para "
            "repartir, y si se paga en efectivo o en acciones). El barrido caso por los "
            "tokens compartidos 'term sheet' y 'board'. Comparten el documento, no la "
            "linea: son dos clausulas distintas del mismo contrato, y el hijo no despliega "
            "en ningun paso la evaluacion de la composicion de la junta. Ni reconocimiento "
            "del 9.6.2 ni figura del 9.22. CONTINUA."
        ),
    },

    119: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y es la MISMA MADRE del par 113 con otro hijo: customer_"
            "validation es un NODO IMAN, del que el barrido cuelga varias filas por su "
            "paso 1. Misma especie que el 113: el paso 1 manda desplegar un MVP de ALTA "
            "FIDELIDAD y el hijo, de otro libro, manda empezar por el MVP mas barato "
            "posible (data sheet, brochure, storyboard) y escalar la sofisticacion solo si "
            "los resultados iniciales prometen. El hijo no ejecuta la linea de la madre: "
            "propone el orden contrario. Su materia propia (identificar la hipotesis "
            "concreta a validar antes de elegir el tipo de MVP, usar herramientas "
            "accesibles antes de produccion profesional) no cabe dentro de ese paso, con lo "
            "cual el test de reconocimiento del 9.6.2 falla. CONTINUA sin direccion "
            "afirmada, mismo suelo que la adjudicacion 3.5 del acta 97 confirmo."
        ),
    },

    120: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y es el borde mas fino del tramo, asi que va marcado como "
            "discutible. El paso 8 de la madre ('Usar el Business Model Canvas y Value "
            "Proposition Canvas como herramientas de planificacion flexible') nombra dos "
            "lienzos como concepto; el hijo, de otro libro, trata del MEDIO en que se "
            "trabaja uno de ellos: empezar en papel con post-its para maximizar la "
            "creatividad grupal, migrar a herramienta digital para versionado y "
            "colaboracion remota, usarla para simulaciones financieras y aprovechar bases "
            "de datos de patrones. Eso es soporte y versionado, no el uso del lienzo como "
            "herramienta de planificacion flexible, que es lo que la linea nombra, con lo "
            "cual el test de reconocimiento del 9.6.2 no se cumple; y el "
            "hijo cubre uno de los dos lienzos, no los dos. Se deja NO RESUELTA porque "
            "afirmarla exigiria leer 'usar el canvas' como 'con que medio trabajarlo', que "
            "es un paso que la vara no da sola. CONTINUA."
        ),
    },

    121: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por FALSO AMIGO sobre un token muy comun. El paso 2 de la madre "
            "('Diferenciar entre necesidad de control y necesidad de mejora') es doctrina "
            "de la trilogia de Juran: decidir en que zona esta el proceso. El hijo es una "
            "TECNICA concreta de piso de planta (centrar el proceso entre los limites, "
            "definir zonas verde, amarilla y roja, muestrear tres piezas consecutivas, "
            "detener si dos de tres caen en amarillo del mismo lado, ajustar y reiniciar), "
            "y no diferencia nada entre control y mejora. Lo unico que comparten es la "
            "palabra control. Ni reconocimiento del 9.6.2 ni figura del 9.22. CONTINUA."
        ),
    },

    122: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y es la CUARTA aparicion de la especie del paso casado con su "
            "refutacion, esta vez DENTRO DEL MISMO LIBRO. La madre es el grafico CUSUM y "
            "el hijo es PRE-Control, cuyo propio entregable dice que opera 'sin necesidad "
            "de graficos de control tradicionales': el hijo es la ALTERNATIVA que evita a "
            "la madre, no su despliegue. El paso 1 de la madre ('Calcular el estadistico "
            "de control, por ejemplo x-barra, para cada muestra') no lo ejecuta ningun paso "
            "del hijo, que muestrea tres piezas consecutivas y decide por zonas de color. "
            "CONTINUA. FIGURA REGISTRADA: pre_control_estadistico es NODO IMAN, cuelga "
            "como hijo de dos madres distintas en este tramo (pares 121 y 122). Ni "
            "reconocimiento del 9.6.2 ni figura del 9.22."
        ),
    },

    123: {
        "clase": "D",
        "direccion": ("eliminacion_inspeccion_masiva_por_control_estadistico -> "
                      "muestreo_estadistico_para_inspeccion"),
        "razon": (
            "El paso 3 de la madre ('Reemplazar inspeccion 100 por ciento por muestreo "
            "estadistico para mantenimiento de la carta de control') nombra el reemplazo "
            "sin decir como se disena el muestreo, y el hijo entero es ese procedimiento en "
            "cinco pasos: definir la poblacion total de transacciones, activos o "
            "documentos, disenar un tamano de muestra estadisticamente representativo "
            "incluyendo el 100 por ciento de los casos sospechosos, aplicarlo de forma "
            "continua o periodica, usar los resultados para estimar el desempeno general, "
            "y reasignar al personal liberado a mejora o produccion. La madre conserva "
            "materia propia que el hijo no toca: establecer las cartas de control, "
            "demostrar con datos que el proceso esta bajo control estadistico y comunicar "
            "el cambio con su justificacion a calidad y a los clientes. Mismo libro, y el test "
            "de reconocimiento del 9.6.2 se cumple por los dos lados: procedimiento en un "
            "solo sentido, tercera fila del 9.22, CONTINUA."
        ),
    },

    124: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA, y va marcada como discutible porque es de las que mas cerca "
            "estan de caer del otro lado. El paso 4 de la madre ('Fomentar el conocimiento "
            "de las necesidades de clientes internos y externos') es un acto de DIFUSION "
            "hacia la fuerza laboral; el hijo es el metodo de IDENTIFICACION del elenco de "
            "clientes (diagrama de flujo del proceso, listar los externos, identificar los "
            "internos por la cadena proveedor-procesador-cliente, distinguir quien ordena "
            "de quien usa, y priorizar por consenso del equipo). Identificar no es "
            "fomentar el conocimiento de: el hijo produce la lista y la madre pide "
            "difundirla, que es dependencia de flujo y no linea contra procedimiento, "
            "con lo cual el 9.6.2 no entrega direccion y el 9.22 no encuentra "
            "procedimiento en ninguno de los dos sentidos sobre esa linea. Se deja en el "
            "suelo que la vara da. CONTINUA."
        ),
    },

    125: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por LINEA COMPARTIDA Y PROCEDIMIENTO PROPIO A CADA LADO, entre "
            "dos libros. La linea compartida es que la calidad no sea tarea de un area "
            "aislada: paso 5 de la madre ('Evita que la calidad quede como tarea exclusiva "
            "de un area aislada de tu negocio') y paso 6 del hijo ('Ensenar estos conceptos "
            "y herramientas a todos los que trabajan contigo, no solo a quien se encarga de "
            "la calidad'). Pero el hijo no despliega esa linea: es un procedimiento de "
            "planificacion estrategica de siete pasos (definir vision, mision y metas "
            "anuales integradas, poner la voz del cliente al nivel de las metas "
            "financieras, reconocer y premiar segun las metas, hacer participar a todos, "
            "unificar el lenguaje de los terminos clave, ensenar, y eliminar las "
            "iniciativas no alineadas) cuyo producto es el plan estrategico anual. Y la "
            "madre tampoco despliega ninguna linea del hijo: su materia es el compromiso "
            "sostenido del director. Es el ejemplar del 2.195 que el 9.6.2 nombra, y no la "
            "figura del 9.22, que exigiria que cada uno expandiese una linea del otro. "
            "CONTINUA."
        ),
    },

    126: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por casado por el OBJETO y no por la ACCION, la misma especie que "
            "el par 103. El paso 4 de la madre es COMUNICAR ('Comunicar los ahorros de "
            "costos y beneficios ambientales generados') y el hijo es un metodo de "
            "VALORACION monetaria (determinar si hay mercado sustituto, elegir metodo de "
            "demanda o de oferta, recopilar datos de encuestas o costos de restauracion, y "
            "asignar el valor monetario). Valorar no es comunicar: el hijo produce la cifra "
            "que despues se podria comunicar, y eso es dependencia de flujo, no linea "
            "contra procedimiento. Ninguno de los dos despliega una linea del otro, asi que "
            "ni test de reconocimiento del 9.6.2 ni figura del 9.22. CONTINUA."
        ),
    },

    127: {
        "clase": "D",
        "direccion": ("coordinacion_colaboracion_cadena_suministro -> "
                      "plataforma_colaboracion_masiva"),
        "razon": (
            "El paso 10 de la madre ('Establecer una plataforma de colaboracion online "
            "para dar seguimiento en tiempo real a la implementacion') nombra la "
            "plataforma sin una palabra de como se construye, y el hijo entero es ese "
            "procedimiento de cuatro pasos: seleccionar tecnologia simple y accesible para "
            "todos los participantes grandes y pequenos, definir APIs seguras para "
            "importar y exportar datos entre ERP, sensores y reportes, disenar una "
            "visualizacion simple que cualquiera entienda, y pilotarla con un grupo "
            "reducido expandiendo por incrementos. La madre conserva once pasos de materia "
            "propia que el hijo no toca. Mismo libro, procedimiento en un solo sentido: "
            "CONTINUA. FIGURA REGISTRADA, y es sobre la madre y no sobre el par: la madre "
            "dice DOS VECES lo mismo en su propia lista, en el paso 4 ('Crear plataformas "
            "de colaboracion online donde las partes discutan problemas y oportunidades en "
            "tiempo real') y en el paso 10. Duplicacion INTERNA de un nodo, especie nueva "
            "en esta lectura, SIN ADJUDICAR. Que el barrido casara el 10 y no el 4 no "
            "cambia el juicio, porque el 9.6.3 dice que el tamano del solape no decide."
        ),
    },

    128: {
        "clase": "D",
        "direccion": "product_roadmap_estrategico -> equipo_multifuncional_real",
        "razon": (
            "El paso 2 de la madre ('Ensamblar un equipo multifuncional de roadmapping') "
            "es una instruccion pelada, y el hijo tarda siete pasos en ejecutarla: asignar "
            "un lider dedicado con autoridad real y espiritu emprendedor, liberar tiempo "
            "real de las tareas habituales, definir indicadores y recompensas por "
            "desempeno del equipo y no individual, mantener un nucleo estable de principio "
            "a fin, elegir el modo de organizacion segun la complejidad, buscar que esten "
            "fisicamente juntos o con comunicacion efectiva a distancia, y evitar el modelo "
            "de pasar el proyecto de area en area. Mismo libro. La madre conserva materia "
            "propia entera: reunir los inputs, generar la wish list, la reunion Gate 0 con "
            "su scorecard, seleccionar los proyectos y su linea de tiempo, derivar el "
            "roadmap de tecnologia y actualizarlo anualmente. Test de reconocimiento del "
            "9.6.2 cumplido por los dos lados, tercera fila del 9.22: CONTINUA."
        ),
    },

    129: {
        "clase": "D",
        "direccion": "product_design_spreadsheet -> traduccion_necesidades_cliente",
        "razon": (
            "El paso 1 de la madre nombra tres cosas como insumo de la hoja ('Colocar las "
            "necesidades del cliente, SU TRADUCCION y medicion en el lado izquierdo') y el "
            "hijo es el procedimiento de cinco pasos que produce esa traduccion: "
            "identificar los terminos vagos o ambiguos del cliente, crear un glosario con "
            "definiciones acordadas, usar muestras fisicas o audiovisuales para las "
            "caracteristicas cualitativas, montar un proceso de traduccion si el volumen lo "
            "pide, y convertir lo cualitativo en mediciones numericas. La madre conserva "
            "materia propia que el hijo no toca: listar las caracteristicas candidatas como "
            "columnas, marcar la fuerza de la relacion entre cada caracteristica y cada "
            "necesidad, verificar que cada necesidad prioritaria este cubierta y que cada "
            "caracteristica sea necesaria. Mismo libro. Se afirma la direccion, y se dice "
            "que es algo mas debil que las de los pares 127 y 128: aqui el hijo produce lo "
            "que el paso de la madre COLOCA, en vez de ejecutar el verbo del paso. Aun asi "
            "el 9.6.2 la entrega, porque su formulacion mira si el paso nombra algo que "
            "tarda varios pasos en existir, y la traduccion tarda cinco. CONTINUA."
        ),
    },

    130: {
        "clase": "D",
        "direccion": "testing_process_completo -> test_card",
        "razon": (
            "La madre nombra al hijo POR SU NOMBRE en el paso casado: 'Disena experimentos "
            "(TARJETA DE TEST) para cada hipotesis prioritaria'. El hijo es la tarjeta y su "
            "procedimiento de seis pasos: nombrar el test con fecha limite y responsable, "
            "describir la hipotesis y su criticidad, disenar el experimento, estimar costo, "
            "fiabilidad de los datos y tiempo, definir la metrica y el umbral de exito o "
            "fracaso, y repetir ordenando las tarjetas por prioridad. Mismo libro. La madre "
            "conserva materia propia entera: dar forma con los dos lienzos, extraer las "
            "hipotesis criticas, ejecutar el ciclo de aprendizaje con la tarjeta de "
            "aprendizaje, y medir con el Progress Board y el termometro de Blank. Es la "
            "prueba que el 9.6.2 pide, dicha por el propio material: existe el hijo que "
            "ejecuta el paso, y la madre lo llama por su nombre. Tercera fila del 9.22: "
            "CONTINUA."
        ),
    },

    131: {
        "clase": "D",
        "direccion": None,
        "razon": (
            "NO RESUELTA por FALSO AMIGO sobre un nombre de cargo. El paso 1 de la madre "
            "('Elaborar una matriz de competencias para el rol de Director de Calidad') "
            "pide una matriz de competencias clasificada por niveles de Bloom; el hijo "
            "monta un CONSEJO de calidad y lo hace funcionar (formarlo con quienes deciden, "
            "definir vision, mision, valores y politica, integrar las metas de calidad en "
            "los planes, designar responsables de los proyectos clave y revisar el progreso "
            "quitando obstaculos). En ningun paso elabora matriz de competencias ninguna. "
            "Comparten el nombre del cargo y nada mas. CONTINUA. FIGURA REGISTRADA: los "
            "pasos 2, 3 y 5 de este hijo dicen casi lo mismo que los pasos 2, 3 y 5 de la "
            "madre del par 101 (rol_alta_direccion_calidad) y que los pasos 1 a 3 del hijo "
            "del par 125 (planificacion_estrategica_despliegue_2). Hay un racimo de "
            "liderazgo de calidad en el mismo libro con repeticion interna fuerte, y "
            "consejo_de_calidad_y_rol_del_director ya venia senalado como sospecha de "
            "gemelo en la propia evidencia de OP-E-03. SIN ADJUDICAR. Ni reconocimiento "
            "del 9.6.2 ni figura del 9.22 en el par mismo."
        ),
    },

    132: {
        "clase": "D",
        "direccion": ("estructura_organizacional_funcional_proceso -> "
                      "empoderamiento_empleados"),
        "razon": (
            "El paso 5 de la madre ('Evaluar el nivel de involucramiento de empleados en "
            "equipos permanentes y ad hoc') lo ejecuta el paso 1 del hijo casi con las "
            "mismas palabras, y lo que sigue en el hijo es residuo con logica propia y "
            "orden obligado: implantar primero un entorno consultivo donde se consulte "
            "antes de decidir, despues formar equipos de proyecto para problemas "
            "concretos, y solo entonces escalar a equipos autodirigidos con mas autoridad. "
            "Una escalera de tres peldanos donde cada uno supone el anterior no son lineas "
            "sueltas, y su propio entregable lo dice ('plan de evolucion con etapas "
            "definidas'). La madre conserva materia propia que el hijo no toca: ventajas y "
            "desventajas de la estructura funcional, si los procesos cross-funcionales "
            "piden dueno dedicado, y los mecanismos matriciales de resolucion de "
            "conflictos. Mismo libro, test de reconocimiento del 9.6.2 cumplido por los dos "
            "lados y procedimiento en un solo sentido, tercera fila del 9.22: CONTINUA."
        ),
    },

}
