# -*- coding: utf-8 -*-
# constructor del lote del tramo 2851-2875.
import json, io, collections
lote = []
def add(p, c, r):
    assert "—" not in r and "–" not in r, "guion largo en %d" % p
    lote.append({"puesto": p, "clase": c, "razon": r})

add(2851, "D",
 "redundancia_en_diseno (Uso de Redundancia en el Diseno de Componentes Criticos, Deming: "
 "identificar los componentes criticos, evaluar si cabe un redundante en paralelo, calcular la "
 "fraccion defectuosa combinada p cuadrado, verificar que el redundante actue, comparar costo "
 "beneficio contra mejorar una sola parte, documentar) contra relacion_confiabilidad_sistema_partes "
 "(Relacion entre Confiabilidad de Partes y del Sistema, Juran: identificar las partes criticas y "
 "sus confiabilidades, multiplicar para la confiabilidad del sistema, evaluar si la complejidad la "
 "reduce, disenar redundancia paralela si hace falta, recalcular con Ps igual 1 menos 1 menos P a la "
 "n). FUENTES DISTINTAS, sim_tit 46,7. El primero es la DECISION de redundancia (evaluar, p "
 "cuadrado, verificar, costo beneficio); el segundo es la RELACION partes a sistema (regla de "
 "multiplicacion, complejidad) donde la redundancia es solo un paso. Cada uno con su acto propio. "
 "D. DISCUTIBLE MARCADO: ambos calculan la confiabilidad con redundancia; quien pese ese calculo "
 "comun dira A.")
add(2852, "D",
 "consejo_de_calidad_3 (Consejos de Calidad, Quality Councils, Crosby: conformar el consejo con "
 "representantes de las areas, periodicidad de reuniones, coordinar la repeticion del ciclo de "
 "mejora, institucionalizarlo como estructura permanente) contra mejora_calidad_crosby (Programa "
 "de Mejora de Calidad, Crosby: establecer la mejora como politica obligatoria, implementar un "
 "programa estructurado como el de catorce pasos, fomentar la comunicacion interna, sostenerlo). "
 "MISMA FUENTE Crosby, sim_tit 47,8. El primero es el ORGANO (el consejo, su composicion y "
 "permanencia); el segundo es el PROGRAMA entero (politica obligatoria, estructura de 14 pasos, "
 "comunicacion). El consejo es una pieza del programa, no el programa. consejo_de_calidad_3 vive "
 "en el cumulo de los consejos (=A= consejo_calidad 2523, consejo_calidad_2 2662); mejora_calidad_"
 "crosby es todo D en el cumulo de los programas (2583, 2708). D. DISCUTIBLE MARCADO: el consejo "
 "sostiene el programa; quien lea eso como el mismo acto dira A.")
add(2853, "A",
 "dia_cero_defectos (Dia de Cero Defectos: elegir una fecha unica, actividades especiales, "
 "explicar el programa a todos el mismo dia) contra dia_cero_defectos_3 (Dia de Cero Defectos, "
 "Evento Simbolico ZD: reunir a todos los empleados con lideres significativos, componente de show "
 "business con musica y premios, firmar el compromiso o pledge con el supervisor y recibir un pin, "
 "anunciar el inicio de la eliminacion de causas de error al dia siguiente, reconocer a los "
 "organizadores). MISMA FUENTE Crosby, sim_tit 56,6. A POR TRANSITIVIDAD DEL CUMULO: "
 "dia_cero_defectos =A= dia_cero_defectos_2 (2491) y dia_cero_defectos_3 =A= dia_cero_defectos_2 "
 "(2525), asi que fusionan entre si. Son el mismo evento del Dia ZD, el _3 con el detalle del "
 "pledge y el pin. A, gemelos en el cumulo del Dia ZD (no mueve el contador de mutuas, convencion "
 "de la vuelta 3). DISCUTIBLE MARCADO: la version breve no trae el pledge ni el anuncio de la ECR; "
 "quien pese ese detalle como paso propio dira D.")
add(2854, "D",
 "analisis_identificacion_mejores_practicas (Analisis e Identificacion de Mejores Practicas, "
 "Juran: consolidar los datos, pruebas de significancia, comparar contra el mejor de la clase o el "
 "cuartil, cuantificar brechas, explorar las estrategias de cada participante, considerar factores "
 "de contexto) contra benchmarking_proceso (Benchmarking, Definicion y Proceso, Juran: definir "
 "alcance, elegir a quien comparar, recolectar y normalizar, analizar hallazgos, identificar "
 "practicas lideres, desarrollar e implementar el plan, evaluar y replicar). MISMA FUENTE Juran, "
 "sim_tit 40,0. FICHA CONTRA MAPA: analisis_identificacion es el PASO de analizar e identificar "
 "practicas (significancia, brechas, estrategias); benchmarking_proceso es el proceso COMPLETO de "
 "siete pasos. D POR TRANSITIVIDAD: analisis_identificacion =D= benchmarking_mejores_practicas "
 "(2536) mientras benchmarking_proceso =A= benchmarking_mejores_practicas (2545). El paso de "
 "analisis no es el proceso entero. D. DISCUTIBLE MARCADO: el analisis vive dentro del proceso; "
 "quien lo lea como contenido dira A.")
add(2855, "D",
 "analisis_identificacion_mejores_practicas (Analisis e Identificacion de Mejores Practicas, "
 "Juran: consolidar datos, significancia, comparar contra el mejor de la clase, cuantificar "
 "brechas, explorar estrategias, factores de contexto) contra benchmarking_7_pasos_juran (Proceso "
 "de Benchmarking de 7 Pasos: definir areas y KPIs, recolectar y validar, normalizar, informe con "
 "brechas, talleres de transferencia, plan e implementar, institucionalizar). MISMA FUENTE Juran, "
 "sim_tit 47,7. FICHA CONTRA MAPA otra vez: analisis_identificacion es el paso de analisis; "
 "benchmarking_7_pasos es el proceso de siete pasos entero. La familia del benchmarking separa "
 "cada nodo: 7_pasos =D= todos (2449, 2585, 2617, 2821) y analisis =D= sus hermanos (2536, 2586). "
 "El paso de analisis no es el proceso de siete pasos. D. DISCUTIBLE MARCADO: el analisis es el "
 "paso 3 y 4 del proceso; quien lo lea como contenido dira A.")
add(2856, "D",
 "deteccion_defectos_raros_control_estadistico (Deteccion de Defectos Extremadamente Raros "
 "mediante Cartas de Control, Deming: determinar si la fraccion defectuosa es muy baja, reemplazar "
 "la inspeccion masiva por medicion continua, disenar un muestreo pequeno y frecuente con cartas X "
 "barra y R, detener la produccion ante una causa especial, investigar la causa raiz, decidir si "
 "condena o libera el lote) contra eliminacion_inspeccion_masiva_por_control_estadistico "
 "(Sustitucion de la Inspeccion Masiva por Control Estadistico, Deming: establecer cartas de "
 "control, demostrar con datos que el proceso esta bajo control, reemplazar el 100 por ciento por "
 "muestreo para mantener la carta, comunicar el cambio y su justificacion). MISMA FUENTE Deming, "
 "sim_tit 42,2. Comparten reemplazar la inspeccion masiva por control estadistico, pero el primero "
 "trae el CASO de los defectos rarisimos con su acto propio (muestreo pequeno y frecuente, detener "
 "la produccion, disposicion del lote); el segundo es la sustitucion GENERAL (demostrar control, "
 "comunicar). eliminacion ya salio D contra abolir_inspeccion (2560) y el cumulo del control "
 "separa. D. DISCUTIBLE MARCADO: quien lea el caso raro como repeticion del general (78.2) dira A.")
add(2857, "D",
 "juran_quality_by_design (Modelo Juran de Calidad por Diseno, Quality by Design: decidir si "
 "continuo o por proyecto, establecer metas, definir mercado y clientes, descubrir necesidades, "
 "desarrollar las caracteristicas y los procesos, desarrollar controles y transferir a "
 "operaciones) contra trilogia_de_juran (Trilogia de Juran, Planificacion Control y Mejora: "
 "traducir lo que pide el cliente en especificaciones, ver si el problema es un pico esporadico o "
 "desperdicio cronico, aplicar control para el esporadico, aplicar mejora o breakthrough para el "
 "cronico, revisar contra los criterios de diseno, integrar los tres como ciclo). MISMA FUENTE "
 "Juran, sim_tit 45,7. El QbD es la pierna de PLANIFICACION o diseno (mercado, necesidades, "
 "caracteristicas, controles); la trilogia es el marco de TRES procesos (planificar, controlar, "
 "mejorar). El QbD es una pierna, no la triada. juran_quality_by_design =A= quality_by_design "
 "(2674, su gemelo); trilogia =D= sus vecinos (2642, 2769). D. DISCUTIBLE MARCADO: el QbD es la "
 "planificacion de la trilogia; quien lea eso como contencion dira A, pero la trilogia suma "
 "control y mejora.")
add(2858, "D",
 "mito_departamento_control_calidad (el mito de delegar la calidad por completo, Deming: redefinir "
 "el rol del de calidad como asesor, involucrarte, pedir reportes de estabilidad, liderar la "
 "mejora continua) contra rol_de_mandos_medios_y_supervisores (Liderar la calidad sin ser quien "
 "manda, Juran: desarrollar liderazgo para coordinar equipos que no te responden, definir quien "
 "detecta los problemas, fomentar la participacion, evaluar habilidades de liderazgo). FUENTES "
 "DISTINTAS, sim_tit 48,0. Actos distintos: el primero es el MITO de la delegacion (que el dueno "
 "no delegue del todo la calidad); el segundo es el ROL del mando medio o supervisor que lidera "
 "sin autoridad formal. mito =D= cinco_suposiciones (2806); rol_de_mandos =D= rol_director "
 "(2845). D. DISCUTIBLE MARCADO: ambos hablan de quien lidera la calidad; quien pese ese tema dira "
 "A.")
add(2859, "D",
 "enfoque_en_procesos_no_en_problemas (Enfocarse en los Procesos no Solo en los Problemas, Deming: "
 "documentar los problemas recurrentes, identificar el proceso comun, aplicar PDCA al proceso "
 "raiz, verificar que se elimina la recurrencia) contra mejora_continua_operaciones (Enfoque de "
 "Mejora Continua en Operaciones, Juran: diagnosticar la cultura, clasificar esporadico o cronico, "
 "resolver el esporadico, atacar el cronico de raiz, sumar otras areas, pedir soporte). FUENTES "
 "DISTINTAS, sim_tit 39,1. El primero es el metodo de atacar el PROCESO detras de los problemas "
 "recurrentes (proceso comun, PDCA); el segundo es el ENFOQUE de mejora con cultura y esporadico "
 "contra cronico. enfoque =D= mejora_continua_del_proceso (2820); mejora_continua_operaciones es "
 "todo D (2642, 2692, 2829, 2848). D. DISCUTIBLE MARCADO: ambos mejoran procesos y no sintomas; "
 "quien pese ese nucleo dira A.")
add(2860, "D",
 "control_estadistico_de_procesos_2 (SPC mediante Graficos de Control, Deming: muestras n 4 o 5, "
 "promedio y rango, limites 3 sigma, graficar, investigar los puntos fuera como causa especial) "
 "contra grafico_box_jenkins (Grafico de Ajuste Manual Box Jenkins, Juran: recolectar datos "
 "secuenciales tras cada observacion, modelar la serie temporal Box Jenkins, calcular el ajuste "
 "recomendado, aplicarlo para minimizar la variacion acumulada, repetir observacion y ajuste). "
 "FUENTES DISTINTAS, sim_tit 35,4. Filosofias OPUESTAS: el SPC deja en paz la variacion comun y "
 "solo actua ante causa especial; el Box Jenkins AJUSTA el proceso tras cada observacion (control "
 "de ingenieria, lo que el SPC llama sobreajuste). control_estadistico_2 es todo D salvo su gemelo "
 "(2590). D. DISCUTIBLE MARCADO: ambos son graficos del proceso en el tiempo; quien pese esa forma "
 "dira A, pero el acto es opuesto.")
add(2861, "D",
 "ingenieria_calidad (Ingenieria de Calidad, Crosby: definir con quien disena las caracteristicas "
 "del producto, coordinar el metodo de produccion y los puntos de control, detallar que "
 "inspeccionar y capacitar, fijar metricas y frecuencia) contra organizacion_independiente_de_"
 "calidad (Calidad independiente y objetiva, Crosby: ubicar a calidad al nivel de ingenieria y "
 "produccion, que reporte directo al dueno, elegir a alguien que comunique sin antagonismo, que "
 "prevenga y no solo detecte). MISMA FUENTE Crosby, sim_tit 56,6. Actos distintos: el primero es "
 "la FUNCION operativa de ingenieria de calidad (caracteristicas, puntos de control, metricas); el "
 "segundo es la ESTRUCTURA e independencia del area de calidad en el organigrama (nivel, linea de "
 "reporte, perfil). ingenieria_calidad es todo D (2611, 2714, 2763, 2807). D. DISCUTIBLE MARCADO: "
 "ambos son la funcion de calidad; quien pese ese marco dira A.")
add(2862, "D",
 "lean_six_sigma_roadmap (Roadmap Lean Six Sigma, DMAIC con tareas Lean: Definir el problema y "
 "alcance, Medir el estado con mapas de flujo, Analizar causas raiz, Mejorar con soluciones Lean "
 "pull kanban trabajo estandar, Controlar con tableros y auditorias) contra "
 "roadmap_despliegue_lean_six_sigma (Roadmap de Despliegue Lean Six Sigma, Decide Prepare Launch "
 "Expand Sustain: evaluar si Six Sigma encaja, elegir capacitador, pausar iniciativas, definir "
 "quien guia, capacitar Champions y Belts, ejecutar los primeros proyectos, expandir a otras "
 "areas, comparar con clase mundial, revisiones regulares). MISMA FUENTE Juran, sim_tit 49,6. DOS "
 "ROADMAPS DISTINTOS pese al titulo comun: el primero es DMAIC, el ciclo de un PROYECTO de mejora "
 "(Definir Medir Analizar Mejorar Controlar); el segundo es DPLES, el DESPLIEGUE de la iniciativa "
 "en toda la organizacion por anos. roadmap_despliegue =A= juran_transformation_roadmap (2811, "
 "ambos DPLES); lean_six_sigma_roadmap es el DMAIC. Correr un proyecto DMAIC no es desplegar la "
 "iniciativa DPLES. D. DISCUTIBLE MARCADO fuerte: los dos se llaman roadmap Lean Six Sigma; quien "
 "los confunda dira A.")
add(2863, "D",
 "especificacion_requisitos_proveedores (Especificacion de Requisitos de Calidad para Proveedores, "
 "Juran: comunicar el uso final y las condiciones, obtener evidencia de capacidad, redactar las "
 "especificaciones de producto y de sistema de calidad, contratos de desarrollo si es complejo) "
 "contra planificacion_tecnologica_conjunta (Planificacion Tecnologica Conjunta con Proveedores, "
 "Juran: acordar el significado exacto de los requisitos, cuantificar confiabilidad y "
 "mantenibilidad evitando errores de la regla de multiplicacion, pedir un plan de control con SPC, "
 "clasificar la seriedad de defectos, estandarizar los metodos de prueba, sistema de trazabilidad "
 "de lotes). MISMA FUENTE Juran, sim_tit 54,7. Actos distintos: el primero ESPECIFICA los "
 "requisitos al proveedor (uso, capacidad, especificaciones); el segundo es la PLANIFICACION "
 "TECNICA CONJUNTA mas profunda (cuantificar confiabilidad, SPC, trazabilidad, estandarizar "
 "pruebas). especificacion ya salio D contra definicion_sistema_calidad_proveedor (2819). D. "
 "DISCUTIBLE MARCADO: ambos acuerdan requisitos con el proveedor; quien pese ese solape dira A.")
add(2864, "D",
 "inspeccion_optima_proceso (Optimizacion del Punto y Tipo de Inspeccion, Deming: mapear los "
 "puntos de inspeccion, calcular el costo de cada punto contra no inspeccionar, pedir evidencia de "
 "control estadistico al proveedor para reducir la entrada, eliminar inspecciones que no generan "
 "registros) contra regla_todo_o_nada_inspeccion_2 (Regla de Inspeccion Todo o Nada, Deming: "
 "revisar si lo que llega esta en control, si p menor a k1 sobre k2 eliminar la inspeccion de "
 "entrada, si p mayor aplicar 100 por ciento, descartar los umbrales fijos sin sustento de costo, "
 "si esta fuera de control usar 100 por ciento o las reglas de Orsini). MISMA FUENTE Deming, "
 "sim_tit 44,7. Actos distintos: el primero OPTIMIZA los puntos de inspeccion (mapa, costo, "
 "eliminar los inutiles); el segundo es la REGLA kp del todo o nada (decidir 0 o 100 por ciento "
 "segun p contra k1 sobre k2). regla_todo_o_nada_2 =D= sus variantes (2530, 2646, 2690). D. "
 "DISCUTIBLE MARCADO: ambos son economia de la inspeccion; quien pese ese marco dira A.")
add(2865, "D",
 "analisis_flujo_proceso (Analisis del Diagrama de Flujo de Proceso, Juran: elaborar el diagrama "
 "completo, dividir en estaciones de trabajo, documentar operaciones secuencia instrumentos y "
 "condiciones por estacion, usarlo como base para auditorias y control) contra "
 "mapa_de_proceso_planificacion_control (Mapa de Proceso para Planificacion de Control, Juran: "
 "reunir al equipo multifuncional, diagramar el flujo completo con interrelaciones, identificar "
 "donde van los sujetos de control, validar el diagrama con todos los responsables). MISMA FUENTE "
 "Juran, sim_tit 64,2. Ambos hacen un diagrama de flujo, pero para fines distintos: el primero "
 "DOCUMENTA las estaciones para auditoria e inspeccion; el segundo identifica los PUNTOS DE "
 "CONTROL con el equipo para la planificacion del control. El cumulo del diagrama de flujo separa "
 "cada nodo (2499, 2728, 2746 D). D. DISCUTIBLE MARCADO fuerte: sim_tit 64,2 y ambos diagraman el "
 "flujo completo; quien lea eso como el mismo mapeo dira A.")
add(2866, "D",
 "concepto_haciendo_la_calidad_cierta (Haciendo la Calidad Cierta, Making Quality Certain, Crosby: "
 "definir de forma simple que significa calidad, asumir un rol activo, reemplazar apagar incendios "
 "por prevencion, comunicacion en ambos sentidos sobre que es calidad) contra "
 "definicion_calidad_conformidad (Calidad como Conformidad con los Requisitos, la Primera "
 "Suposicion Erronea, Crosby: definir requisitos claros y medibles, eliminar terminos subjetivos "
 "como alta calidad o elegancia, comunicar los requisitos con precision, evaluar por si cumple o "
 "no, corregir un requisito poco realista al definirlo, preguntar que requisito evalua quien habla "
 "vago de calidad). MISMA FUENTE Crosby, sim_tit 46,0. El primero es el concepto PARAGUAS de hacer "
 "la calidad cierta (definir, rol activo, prevencion, comunicar); el segundo es UN absoluto, la "
 "definicion de calidad como conformidad (requisitos medibles, sin terminos subjetivos). Cada uno "
 "trae pasos enteros propios (prevencion y rol activo en uno; requisitos medibles y sin subjetivos "
 "en el otro). D. DISCUTIBLE MARCADO: ambos definen y comunican que es calidad; quien lea la "
 "conformidad como contenida en el paraguas dira A.")
add(2867, "D",
 "equipo_mejora_calidad_2 (Equipo de Mejora de Calidad, Quality Improvement Team, Crosby: elegir "
 "al lider con vision de todo el negocio, un representante por area clave, alguien que documente, "
 "frecuencia regular de reuniones, definir hasta donde puede llegar el grupo) contra "
 "establecer_equipo_multifuncional (Formar el grupo correcto para disenar con calidad, Juran: "
 "identificar a quien afecta el resultado, sumar a los duenos de los procesos, incorporar "
 "conocimiento tecnico, contar con quienes pondran en marcha el diseno). FUENTES DISTINTAS, "
 "sim_tit 39,7. Equipos distintos: el QIT permanente del programa de mejora de Crosby (lider, "
 "representantes, cadencia, autoridad) contra el equipo multifuncional de un PROYECTO de diseno de "
 "Juran (afectados, duenos de proceso, especialistas, implementadores). equipo_mejora_calidad_2 "
 "=A= equipo_mejora_calidad (2509, su gemelo) y =D= los demas; establecer_equipo_multifuncional "
 "vive en el cumulo del equipo de diseno. D. DISCUTIBLE MARCADO: ambos forman un equipo con "
 "representantes y especialistas; quien pese esa forma dira A.")
add(2868, "D",
 "concepto_programa_catorce_pasos (Programa de Catorce Pasos para la Mejora de la Calidad, Crosby: "
 "adaptar el programa a la madurez de cada unidad, iniciar con pilotos, documentar resultados "
 "tempranos para seminarios, dar seguimiento por varios anos) contra mejora_calidad_crosby "
 "(Programa de Mejora de Calidad, Crosby: establecer la mejora como politica obligatoria, "
 "implementar un programa estructurado como el de catorce pasos, fomentar la comunicacion interna, "
 "sostenerlo). MISMA FUENTE Crosby, sim_tit 69,9. El primero es la ESTRATEGIA de despliegue del "
 "programa de 14 pasos (adaptar, pilotos, seminarios, anos); el segundo es el programa como "
 "POLITICA (obligatoria, estructurada, comunicacion). Todo el cumulo de los programas de mejora "
 "separa cada variante: concepto =D= sus hermanos (2487, 2510, 2676), mejora_calidad_crosby =D= "
 "los suyos (2583, 2708). D. DISCUTIBLE MARCADO fuerte: sim_tit 69,9 y ambos son el programa "
 "sostenido en el tiempo; quien pese ese nucleo dira A.")
add(2869, "D",
 "graficos_y_diagramas (Graphs and Charts, Juran: determinar rango y escala de los ejes, "
 "seleccionar el tipo de grafico linea barra o pastel, graficar con escalas consistentes, "
 "etiquetar y titular, verificar la integridad grafica, simplificar) contra resumen_de_datos_"
 "graficos (Resumen y Visualizacion Grafica de Datos, Juran: graficar la salida Y contra el orden "
 "temporal, histograma con al menos 40 puntos, diagramas de caja con pocos datos, calcular "
 "tendencia central y dispersion, buscar tendencias o ciclos). MISMA FUENTE Juran, sim_tit 42,5. "
 "Actos distintos: el primero es como PRESENTAR un grafico bien hecho (escala, tipo, integridad, "
 "simplificar); el segundo es RESUMIR y analizar datos con graficos (serie temporal, histograma, "
 "box plot, medidas, buscar tendencias). graficos_y_diagramas =D= herramientas_analisis (2757); "
 "resumen =D= histograma y sus hermanos (2538, 2750). D. DISCUTIBLE MARCADO: ambos son graficos de "
 "datos; quien pese ese tema dira A.")
add(2870, "D",
 "cero_defectos (Cero Defectos, Zero Defects ZD, Crosby: establecer el ZD como compromiso personal "
 "de desempeno, comunicarlo caso por caso, fijar una fecha de lanzamiento el Dia ZD, reconocer el "
 "desempeno alineado, extenderlo a todas las areas, repetir y reforzar) contra dia_cero_defectos_2 "
 "(Dia de Cero Defectos ZD Day y el Compromiso Pledge, Crosby: dia de sugerencias previo, carta "
 "explicativa con el compromiso, realizar el evento con invitados, explicar y firmar el pledge uno "
 "a uno, repartir pines, iniciar la eliminacion de causas de error al dia siguiente). MISMA FUENTE "
 "Crosby, sim_tit 52,9. D POR TRANSITIVIDAD Y CONCEPTO CONTRA EVENTO: cero_defectos =D= "
 "dia_cero_defectos (2772) y dia_cero_defectos_2 =A= dia_cero_defectos (2491), asi que cero_"
 "defectos =D= dia_cero_defectos_2. El primero es el ESTANDAR ZD (compromiso, extender a todo, "
 "reforzar) que solo NOMBRA el Dia ZD como un paso; el segundo ES el evento del Dia ZD. D. "
 "DISCUTIBLE MARCADO: el estandar incluye fijar el Dia ZD; quien lea el evento como contenido a "
 "favor de fusion dira A.")
add(2871, "D",
 "control_estadistico_de_procesos_2 (SPC mediante Graficos de Control, Deming: muestras n 4 o 5, "
 "promedio y rango, limites 3 sigma, graficar, investigar los puntos fuera) contra "
 "control_estadistico_no_implica_cero_defectos (Control Estadistico No Implica Ausencia de "
 "Defectos, Deming: verificar el control con la carta, aceptar que estar en control no es cumplir "
 "especificaciones, intervenir el sistema para reducir el nivel de defectos, distinguir cambiar la "
 "media de reducir la dispersion). MISMA FUENTE Deming, sim_tit 54,1. METODO CONTRA LECCION: el "
 "primero CONSTRUYE y corre la carta; el segundo es la LECCION conceptual de que el control no "
 "implica conformidad y hay que intervenir el sistema. control_estadistico_2 es todo D salvo su "
 "gemelo (2590); control_estadistico_no_implica =A= control_estadistico_del_proceso (2529) y =D= "
 "los demas. D. DISCUTIBLE MARCADO: ambos parten de la carta de control; quien pese ese arranque "
 "comun dira A.")
add(2872, "D",
 "analisis_datos_reporte_estatus (Analisis de Datos y Reporte del Estado, Crosby: registrar cada "
 "resultado de inspeccion, colocar graficos de progreso visibles y explicarlos, generar reportes "
 "de tendencia para el dia a dia y para las decisiones grandes, usar los datos para identificar "
 "que personas o procesos tienen problemas) contra medicion_calidad_2 (Paso 3 Medicion de la "
 "Calidad, Crosby: recolectar datos por area, clasificar los defectos por gravedad causa y "
 "responsabilidad, graficos de tendencia visibles, metas de mejora visibles, que el ingeniero de "
 "calidad revise a diario los defectos mas frecuentes). MISMA FUENTE Crosby, sim_tit 35,3. "
 "Comparten los graficos de tendencia visibles y usar los datos para hallar problemas, pero cada "
 "uno trae su acto propio: medicion_calidad_2 clasifica los defectos por gravedad y fija metas "
 "(la MEDICION, Paso 3); analisis_datos_reporte genera reportes de tendencia para las decisiones "
 "grandes (el REPORTE del estado). medicion_calidad_2 =A= medicion_calidad (2638, su gemelo). D. "
 "DISCUTIBLE MARCADO: comparten los graficos visibles y hallar los problemas; quien pese ese "
 "nucleo dira A.")
add(2873, "D",
 "criticas_muestreo_aceptacion (Por que revisar una muestra de cada lote no basta, Deming: dejar "
 "de usar los planes de muestreo por aceptacion como control final, cambiar la inspeccion de lotes "
 "por el control estadistico en tiempo real, trabajar con proveedores en el origen, calcular "
 "cuanto cuesta seguir con el muestreo) contra muestreo_de_aceptacion (Muestreo de Aceptacion, "
 "Juran: ver si evaluas el lote o el proceso, definir n y c, fijar los riesgos del productor y del "
 "consumidor, seleccionar el plan por atributos o variables, aplicarlo y documentar). FUENTES "
 "DISTINTAS, posturas OPUESTAS, sim_tit 37,5. El primero ARGUMENTA ABANDONAR el muestreo de "
 "aceptacion (pasar a SPC); el segundo enseña COMO hacerlo. criticas es todo D (2623, 2730, 2753, "
 "2767); muestreo =D= sus vecinos (2634, 2702). D. DISCUTIBLE MARCADO: ambos hablan del muestreo "
 "de aceptacion; quien ignore la postura opuesta dira A.")
add(2874, "D",
 "eliminar_slogans_metas (Eliminar Slogans Exhortaciones y Metas Numericas, Punto 10 de Deming: "
 "eliminar carteles lemas y metas que solo exiges a quien ejecuta, calcular que proporcion de los "
 "defectos viene del sistema, cambiar las exhortaciones por acciones tuyas de mejora, trabajar con "
 "los proveedores de forma colaborativa) contra mejora_del_sistema_responsabilidad_gerencial (La "
 "Mejora del Sistema es Tu Responsabilidad, Deming: verificar el control estadistico, si persisten "
 "defectos identificar elementos del sistema como causa raiz, pruebas simples para aislar la "
 "variable comun, implementar el cambio estructural, verificar la reduccion). MISMA FUENTE Deming, "
 "sim_tit 31,1. Actos distintos: el primero es el Punto 10 (quitar los lemas y reemplazarlos por "
 "accion de sistema); el segundo es el PROCEDIMIENTO tecnico de mejora del sistema (carta de "
 "control, aislar la variable comun, cambio estructural). eliminar_slogans =A= "
 "eliminar_slogans_y_exhortaciones (2484, su gemelo) y =D= la postura gerencial (2732); "
 "mejora_del_sistema =D= sus vecinos (2508, 2556, 2656, 2700). D. DISCUTIBLE MARCADO: ambos ligan "
 "los defectos al sistema que el gerente controla; quien pese ese nucleo dira A.")
add(2875, "D",
 "desarrollar_caracteristicas_proceso (Desarrollar las Caracteristicas del Proceso, Juran: listar "
 "los procesos capaces de generar cada caracteristica del producto, evaluar su capacidad actual, "
 "seleccionar el proceso optimo con justificacion, fijar metas de proceso) contra "
 "identificar_caracteristicas_metas_proceso (Identificacion de Caracteristicas y Metas del "
 "Proceso, Juran: descomponer el proceso en caracteristicas especificas, clasificar cada una en "
 "procedimientos metodos equipos materiales personas, organizarlas en la hoja de diseno de "
 "proceso, verificar la cobertura y eliminar redundancias, confirmar los macroprocesos de "
 "soporte). MISMA FUENTE Juran, sim_tit 66,7. Dos pasos distintos del cascadeo de diseno de "
 "proceso: el primero SELECCIONA el proceso (candidatos, capacidad, optimo, metas); el segundo "
 "DESCOMPONE en caracteristicas y las organiza en la hoja de diseno con verificacion "
 "bidireccional. Ambos salieron D contra diseno_de_procesos_por_caracteristicas (2813, 2481), y la "
 "familia del cascadeo separa. Seleccionar el proceso no es descomponer sus caracteristicas en la "
 "hoja. D. DISCUTIBLE MARCADO fuerte: sim_tit 66,7 y ambos son caracteristicas del proceso; quien "
 "los lea como el mismo paso dira A.")

out = io.open("docs/loop/_lote.jsonl", "w", encoding="utf-8", newline="\n")
for x in lote:
    out.write(json.dumps(x, ensure_ascii=False) + "\n")
out.close()
print("escritos %d, %d..%d, clases %s" % (len(lote), lote[0]["puesto"], lote[-1]["puesto"],
      dict(collections.Counter(x["clase"] for x in lote))))
