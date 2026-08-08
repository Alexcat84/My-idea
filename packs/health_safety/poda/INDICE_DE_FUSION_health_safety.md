# Índice de fusión de health_safety

27 clusters propuestos, 57 nodos de los 332 del pack.

**Borra las líneas de lo que NO debe fundirse. Lo que quede se consolida.**

## La regla del superviviente (vigente)

**Sobrevive el nodo con más historia.** La telemetría es la voz de los caminos reales, y conservar el id más pisado es lo que menos fricción crea con `project_nodes`. El contenido del que proponía el consolidador **no se pierde**: se rescata dentro del superviviente.

Si ningún nodo del cluster tiene historia, manda el propuesto del consolidador. **Tu ojo es la única excepción**: donde discrepes, tacha y escribe cuál debe quedarse.

`visto N` = veces que apareció en el recorrido de alguien. `cosechado N` = veces que se llevó a un plan. Ningún nodo se borra: los absorbidos salen de la selección y su id sigue existiendo.

## 1. 3 nodos · similitud 0.924 · **2 con historia**

> Los tres describen el mismo par conceptual de fallas activas y condiciones latentes.

**Sobrevive: `fallas_activas_condiciones_latentes`** (telemetría)

- [validación] **Fallas Activas y Condiciones Latentes** `fallas_activas_condiciones_latentes`  ·  visto 1 · cosechado 1 **← SOBREVIVE**
- [validación] **Fallas Activas vs. Condiciones Latentes** `fallas_activas_condiciones_latentes_2`  ·  visto 1 · cosechado 1 
- [validación] **Fallos Activos y Condiciones Latentes** `fallos_activos_condiciones_latentes` 

## 2. 3 nodos · similitud 0.923 · **1 con historia**

> Los tres describen la misma acción de evaluar periódicamente el programa de seguridad con indicadores leading/lagging.

**Sobrevive: `evaluacion_mejora_programa`** (telemetría)

- [validación] **Evaluación y Mejora del Programa de Seguridad y Salud** `evaluacion_mejora_programa`  ·  visto 3 · cosechado 3 **← SOBREVIVE**
- [validación] **Evaluación y Mejora del Programa de Seguridad (Verificación Inicial y Anual)** `evaluacion_mejora_programa_3` 
- [ejecución] **Evaluación Periódica del Programa de Seguridad** `evaluacion_periodica_programa_seguridad` 

## 3. 3 nodos · similitud 0.907 · sin historia

> Las tres describen el mismo cambio de paradigma (seguridad como presencia de capacidades vs ausencia de fallos), solo con distinto énfasis narrativo, sin implicar acciones distintas.

**Sobrevive: `safety_i_safety_ii`** (propuesto)

- [planificación] **Resiliencia y Safety Differently (Safety-II)** `resiliencia_organizacional` 
- [planificación] **Safety I versus Safety II** `safety_i_safety_ii` **← SOBREVIVE**
- [planificación] **Safety II: Seguridad como Capacidad de Éxito** `safety_ii_resiliencia` 

## 4. 2 nodos · similitud 0.958 · sin historia

> Ambos describen los mismos criterios de diseño de recordatorios contra omisiones.

**Sobrevive: `diseno_recordatorios_efectivos_2`** (propuesto)

- [ejecución] **Diseño de Recordatorios Efectivos contra Omisiones** `diseno_recordatorios_efectivos` 
- [ejecución] **Diseño de Recordatorios Efectivos para Prevenir Omisiones** `diseno_recordatorios_efectivos_2` **← SOBREVIVE**

## 5. 2 nodos · similitud 0.951 · sin historia

> Ambos describen el mismo modelo regulatorio del Safety Case surgido del Informe Cullen.

**Sobrevive: `safety_case_evaluacion_formal`** (propuesto)

- [planificación] **Evaluación Formal de Seguridad (Safety Case)** `formal_safety_assessment_safety_case` 
- [planificación] **Safety Case y Evaluación Formal de Seguridad (FSA)** `safety_case_evaluacion_formal` **← SOBREVIVE**

## 6. 2 nodos · similitud 0.949 · sin historia

> Ambos plantean la misma crítica a fijar metas de reducción de accidentes en vez de gestionar procesos.

**Sobrevive: `metas_de_seguridad_correctas`** (propuesto)

- [planificación] **Establecer Metas de Seguridad como Programa de Fitness a Largo Plazo** `establecer_metas_seguridad_correctas` 
- [planificación] **Establecer Metas de Seguridad Correctas: Gestión de Procesos vs. Resultados Negativos** `metas_de_seguridad_correctas` **← SOBREVIVE**

## 7. 2 nodos · similitud 0.948 · sin historia

> Ambos describen el mismo modelo de barreras y defensas tipo Swiss Cheese.

**Sobrevive: `modelo_barreras_defensas`** (propuesto)

- [planificación] **Modelo de Barreras y Defensas (Swiss Cheese)** `modelo_barreras_defensas` **← SOBREVIVE**
- [planificación] **Modelo de Barreras (Swiss Cheese)** `modelo_barreras_swiss_cheese` 

## 8. 2 nodos · similitud 0.942 · sin historia

> Ambos critican el mismo enfoque de seguridad basada en comportamiento por culpar al individuo.

**Sobrevive: `critica_behavior_based_safety`** (propuesto)

- [planificación] **Crítica a los Programas de Seguridad Basados en Comportamiento** `critica_behavior_based_safety` **← SOBREVIVE**
- [validación] **Riesgos de los Programas de Seguridad Basados en Comportamiento** `riesgos_programas_seguridad_conductual` 

## 9. 2 nodos · similitud 0.941 · **2 con historia**

> Ambos describen el mismo proceso de evaluar severidad, probabilidad y exposición para priorizar peligros.

**Sobrevive: `caracterizacion_priorizacion_peligros`** (telemetría)

- [planificación] **Caracterización y Priorización de Peligros (Evaluación de Riesgo)** `caracterizacion_priorizacion_peligros`  ·  visto 2 · cosechado 2 · **MATRIZ** **← SOBREVIVE**
    - MATRIZ: ...ita justificar el orden de implementación de controles Matriz de riesgos priorizada con peligros clasificados por severidad y...
- [planificación] **Caracterización y Priorización de Peligros** `priorizacion_caracterizacion_peligros`  ·  visto 2 · cosechado 2 

## 10. 2 nodos · similitud 0.937 · **1 con historia**

> Ambos describen el mismo requisito de protección contra caídas desde más de 4 pies.

**Sobrevive: `elevated_surfaces_fall_protection`** (telemetría)

- [ejecución] **Protección contra Caídas en Superficies Elevadas (Medidas y Sistemas)** `elevated_surfaces_fall_protection`  ·  visto 3 · cosechado 3 **← SOBREVIVE**
- [ejecución] **Protección contra Caídas en Superficies Elevadas (Requisito desde 4 Pies)** `superficies_elevadas_proteccion_caidas` *(el consolidador proponía este; su contenido se rescata)*

## 11. 2 nodos · similitud 0.935 · **2 con historia**

> Ambos describen el mismo proceso de seleccionar e implementar la jerarquía de controles; la separación planificación/ejecución es solo el momento, no una acción distinta.

**Sobrevive: `prevencion_control_peligros`** (telemetría)

- [planificación] **Prevención y Control de Peligros (Jerarquía de Controles)** `prevencion_control_peligros`  ·  visto 4 · cosechado 3 **← SOBREVIVE**
- [ejecución] **Prevención y Control de Peligros mediante Jerarquía de Controles** `prevencion_control_peligros_2`  ·  visto 3 · cosechado 2 *(el consolidador proponía este; su contenido se rescata)*

## 12. 2 nodos · similitud 0.934 · **1 con historia**

> Ambos describen la misma acción de reunir información existente sobre peligros antes de controlarlos.

**Sobrevive: `identificacion_recopilacion_informacion_peligros`** (telemetría)

- [planificación] **Recopilación y Revisión de Información sobre Peligros** `identificacion_recopilacion_informacion_peligros`  ·  visto 3 · cosechado 3 · **DATO LOCAL** **← SOBREVIVE**
    - DATO LOCAL: ...les de equipos, SDS, reportes de inspección, registros OSHA 300/301, resultados de monitoreo de exposición, JHAs)...
- [planificación] **Recopilación de Información Existente sobre Peligros** `recopilacion_informacion_peligros`  ·  **DATO LOCAL** · **CORPORATIVO** 
    - DATO LOCAL: ...S), reportes de autoinspección, registros de lesiones (OSHA 300/301), resultados de monitoreo de exposición, progr...
    - CORPORATIVO: ...información sobre peligros del sitio, disponible para el equipo de seguridad...

## 13. 2 nodos · similitud 0.934 · sin historia

> Ambos describen la misma técnica HEART para evaluar y reducir errores humanos.

**Sobrevive: `heart_metodo_evaluacion_error_humano`** (propuesto)

- [ejecución] **HEART: Evaluación y Reducción de Errores Humanos** `heart_evaluacion_probabilidad_error` 
- [planificación] **HEART: Human Error Assessment and Reduction Technique** `heart_metodo_evaluacion_error_humano` **← SOBREVIVE**

## 14. 2 nodos · similitud 0.926 · sin historia

> Ambos describen el mismo concepto de rechazar soluciones superficiales tras un accidente.

**Sobrevive: `abandonar_arreglos_rapidos`** (propuesto)

- [ejecución] **Abandonar la Falacia del Arreglo Rápido** `abandonar_arreglos_rapidos` **← SOBREVIVE**
- [ejecución] **Abandonar la falacia del arreglo rápido (Quick Fix)** `abandonar_la_falacia_del_arreglo_rapido` 

## 15. 2 nodos · similitud 0.925 · **2 con historia**

> El proceso de verificar, inspeccionar y mantener los controles es el mismo; la distinción por industria (general/construcción) no cambia la acción a realizar.

**Sobrevive: `seguimiento_efectividad_controles`** (telemetría)

- [ejecución] **Seguimiento de la Efectividad de los Controles (Industria General)** `seguimiento_efectividad_controles`  ·  visto 3 · cosechado 3 **← SOBREVIVE**
- [ejecución] **Seguimiento de la Efectividad de los Controles (Construcción)** `seguimiento_efectividad_controles_2`  ·  visto 2 · cosechado 1 

## 16. 2 nodos · similitud 0.923 · sin historia

> Ambos describen el mismo sesgo de persistir con un plan pese a señales de cambio de situación.

**Sobrevive: `plan_continuation_bias`** (propuesto)

- [validación] **Continuación de Plan (Plan Continuation)** `continuacion_de_plan` 
- [ejecución] **Sesgo de Continuación del Plan (Plan Continuation)** `plan_continuation_bias` **← SOBREVIVE**

## 17. 2 nodos · similitud 0.922 · **1 con historia**

> Ambos describen la misma acción de inspeccionar regularmente el sitio para identificar peligros.

**Sobrevive: `inspeccion_lugar_trabajo_peligros`** (telemetría)

- [ejecución] **Inspección del Lugar de Trabajo para Identificar Peligros de Seguridad** `inspeccion_lugar_trabajo_peligros`  ·  visto 2 · cosechado 2 · **CORPORATIVO** **← SOBREVIVE**
    - CORPORATIVO: ...uipos y áreas de trabajo Incluir a los trabajadores en el equipo de inspección Documentar hallazgos con fotos o videos par...
- [ejecución] **Inspección Regular del Sitio de Trabajo para Identificar Peligros** `inspeccion_sitio_peligros`  ·  **CORPORATIVO** *(el consolidador proponía este; su contenido se rescata)*
    - CORPORATIVO: ...iderar inspecciones periódicas Incluir trabajadores en el equipo de inspección Documentar hallazgos con fotos/video y chec...

## 18. 2 nodos · similitud 0.919 · sin historia

> Ambos comparan el mismo dilema entre abordar a la persona o la situación en la gestión de errores.

**Sobrevive: `enfoque_situacional_vs_personal`** (propuesto)

- [ejecución] **Enfoque Situacional vs. Personal en la Gestión de Errores** `enfoque_situacional_vs_personal` **← SOBREVIVE**
- [ideación] **Enfoque Situacional vs. Enfoque Personal en Gestión de Errores** `enfoque_situacional_vs_personal_2` 

## 19. 2 nodos · similitud 0.916 · sin historia

> Ambos describen el mismo procedimiento de bloqueo y etiquetado para controlar energías peligrosas.

**Sobrevive: `lockout_tagout_procedures`** (propuesto)

- [planificación] **Procedimientos de Bloqueo y Etiquetado (Control de Energías Peligrosas)** `lockout_tagout_procedures` **← SOBREVIVE**
- [ejecución] **Procedimientos de Bloqueo y Etiquetado (Procedimiento Escrito)** `procedimientos_lockout_tagout` 

## 20. 2 nodos · similitud 0.915 · **1 con historia**

> Ambos describen la misma acción de investigar incidentes y casi accidentes para hallar causas raíz.

**Sobrevive: `investigacion_incidentes`** (telemetría)

- [ejecución] **Investigación de Incidentes y Casi Accidentes** `investigacion_incidentes`  ·  visto 2 · cosechado 2 · **DATO LOCAL** **← SOBREVIVE**
    - DATO LOCAL: ...si accidente en el lugar de trabajo Al recibir reporte OSHA 300/301 Informe de investigación de incidente con caus...
- [ejecución] **Investigación de Incidentes y Cuasi-Accidentes** `investigacion_incidentes_2`  ·  **DATO LOCAL** 
    - DATO LOCAL: ...da la organización Cumplir con los plazos de reporte a OSHA (8h fatalidad, 24h hospitalización/amputación) Cuando...

## 21. 2 nodos · similitud 0.914 · **2 con historia**

> Ambos describen la misma distinción entre accidentes individuales y organizacionales.

**Sobrevive: `accidentes_individuales_vs_organizacionales`** (telemetría)

- [ideación] **Distinción entre Accidentes Individuales y Organizacionales** `accidentes_individuales_vs_organizacionales`  ·  visto 2 · cosechado 2 **← SOBREVIVE**
- [ideación] **Diferenciación entre Accidente Individual y Accidente Organizacional** `diferenciacion_accidente_individual_organizacional`  ·  visto 1 · cosechado 1 

## 22. 2 nodos · similitud 0.912 · **1 con historia**

> Es el mismo marco de 7 elementos de OSHA descrito dos veces con distinto nivel de detalle en el título.

**Sobrevive: `programa_seguridad_salud_ocupacional`** (telemetría)

- [planificación] **Programa de Seguridad y Salud Ocupacional (Marco de 7 Elementos)** `programa_seguridad_salud_ocupacional`  ·  visto 4 · cosechado 4 · **DATO LOCAL** **← SOBREVIVE**
    - DATO LOCAL: ...7 Elementos) Marco flexible y proactivo propuesto por OSHA para gestionar la seguridad y salud en el trabajo, apl...
- [planificación] **Programa de Seguridad y Salud Ocupacional** `programa_seguridad_salud_ocupacional_2`  ·  **DATO LOCAL** · **CORPORATIVO** 
    - DATO LOCAL: ...por accidentes o mejorar el cumplimiento normativo de OSHA Documento de programa de seguridad y salud implementad...
    - CORPORATIVO: ...a moral del personal. Obtener el compromiso visible de la gerencia con la seguridad y salud laboral Establecer mecanismos...

## 23. 2 nodos · similitud 0.908 · sin historia

> Ambos describen el mismo ciclo de culpa derivado del supuesto de libre albedrío.

**Sobrevive: `ciclo_de_culpa_2`** (propuesto)

- [ejecución] **El Ciclo de la Culpa (Blame Cycle)** `ciclo_de_culpa_2` **← SOBREVIVE**
- [ideación] **El Ciclo de Culpa (El Supuesto del Agente Libre)** `ciclo_de_culpa_blame_cycle` 

## 24. 2 nodos · similitud 0.907 · sin historia

> Ambos describen la misma acción de establecer un procedimiento de intercambio de información sobre peligros entre contratistas.

**Sobrevive: `establecer_comunicacion_efectiva_hostempleador`** (propuesto)

- [planificación] **Establecimiento de Comunicación Efectiva entre Contratistas** `establecer_comunicacion_efectiva_contratistas` 
- [ejecución] **Establecer Comunicación Efectiva entre Empleador Anfitrión y Contratistas** `establecer_comunicacion_efectiva_hostempleador` **← SOBREVIVE**

## 25. 2 nodos · similitud 0.906 · sin historia

> Ambos describen la misma teoría clásica de la manzana podrida (Old View).

**Sobrevive: `bad_apple_theory`** (propuesto)

- [ideación] **Teoría de la Manzana Podrida (Bad Apple Theory)** `bad_apple_theory` **← SOBREVIVE**
- [ideación] **Old View o Teoría de la Manzana Podrida** `old_view_bad_apple_theory` 

## 26. 2 nodos · similitud 0.905 · **2 con historia**

> Ambos describen la misma acción de implementar controles según prioridades del plan.

**Sobrevive: `implementacion_controles`** (telemetría)

- [ejecución] **Implementación de Controles en el Lugar de Trabajo** `implementacion_controles`  ·  visto 3 · cosechado 2 **← SOBREVIVE**
- [ejecución] **Implementación de Controles Seleccionados en el Sitio** `implementacion_controles_2`  ·  visto 3 · cosechado 2 *(el consolidador proponía este; su contenido se rescata)*

## 27. 2 nodos · similitud 0.904 · sin historia

> Ambos describen el mismo fenómeno de normalización de la desviación de Vaughan, uno solo extiende su implicación regulatoria.

**Sobrevive: `normalizacion_de_la_desviacion`** (propuesto)

- [ejecución] **Normalización de la Desviación** `normalizacion_de_la_desviacion` **← SOBREVIVE**
- [validación] **Normalización de la Desviación y Fallas Regulatorias** `regulador_fallas_sistemicas` 

---

## Las tres barandas nuevas en todo el pack

Los detectores corrieron sobre los 332 nodos, no sobre una muestra: son locales y gratis. 57 nodos dieron algún hallazgo.

- **DATO LOCAL**: 34 nodos
- **CORPORATIVO**: 24 nodos
- **MATRIZ**: 3 nodos


### 48 nodos con hallazgo que NO están en ningún cluster

Estos no los toca la fusión: son otra decisión, y va aparte.

- **Cuatro Áreas Primarias de Riesgo en Tecnologías Peligrosas** `areas_riesgo_primario` — MATRIZ
- **Supervisión de Primera Línea con Autonomía (Auftragssystem)** `auftragssystem_supervision_autonoma` — CORPORATIVO
- **Autoinspección del Lugar de Trabajo** `autoinspeccion_lugar_de_trabajo` — DATO LOCAL
- **Educación y Capacitación en Seguridad y Salud Ocupacional** `capacitacion_educacion_seguridad` — DATO LOCAL
- **Clasificación de Sistemas según su Nivel de Seguridad (Unsafe, Safer, Safe, Ultra-safe)** `clasificacion_sistemas_por_nivel_seguridad` — CORPORATIVO
- **Cláusula de Deber General (General Duty Clause)** `clausula_deber_general_osha` — DATO LOCAL
- **Liderazgo y Compromiso de la Gerencia en Seguridad** `compromiso_gerencial_seguridad` — CORPORATIVO
- **El Modelo del Iceberg de Costos Ocultos de los Accidentes** `costos_ocultos_accidentes_iceberg` — CORPORATIVO
- **No Existe una 'Verdad Absoluta' en la Investigación** `critica_ground_truth_investigacion` — CORPORATIVO
- **Componentes de la Cultura de Seguridad** `cultura_de_seguridad_componentes` — CORPORATIVO
- **Cultura Justa (Just Culture)** `cultura_justa_organizacional` — CORPORATIVO
- **Derecho del Trabajador a Rechazar Trabajo Peligroso** `derecho_rechazo_trabajo_peligroso` — DATO LOCAL
- **Diseño de un Departamento de Seguridad Efectivo** `diseno_departamento_seguridad_efectivo` — CORPORATIVO
- **Educación y Entrenamiento en Seguridad** `educacion_entrenamiento_seguridad` — DATO LOCAL
- **Programa de Ergonomía Laboral** `ergonomia_laboral` — DATO LOCAL
- **Seguridad en Escaleras Fijas (Stairways)** `escaleras_fijas_seguridad` — DATO LOCAL
- **Escapar de la Trampa del Proveedor Pasivo de Seguridad** `escape_trampa_proveedor_pasivo` — CORPORATIVO
- **Evaluación y Mejora del Programa de Seguridad (Elemento del Programa)** `evaluacion_mejora_programa_2` — DATO LOCAL
- **Evitar el Lenguaje Juzgador en Investigaciones** `evitar_lenguaje_juzgador` — CORPORATIVO
- **Identificación y Evaluación de Peligros (Industria General)** `identificacion_evaluacion_peligros` — DATO LOCAL
- **Identificación y Evaluación de Peligros (Construcción)** `identificacion_evaluacion_peligros_2` — DATO LOCAL · CORPORATIVO
- **Identificación de Peligros para la Salud (Construcción)** `identificacion_peligros_salud_2` — DATO LOCAL
- **Plan de Control de Infecciones** `infection_control_plan` — DATO LOCAL
- **Ingeniería de una Cultura de Aprendizaje Organizacional** `ingenieria_cultura_aprendizaje` — CORPORATIVO
- **Jerarquía de Controles de Peligros** `jerarquia_controles` — DATO LOCAL
- **Liderazgo Gerencial en Seguridad y Salud** `liderazgo_gerencial_seguridad` — CORPORATIVO
- **Los Tres Motores de la Seguridad: Compromiso, Competencia y Conocimiento** `motores_de_seguridad_3cs` — CORPORATIVO
- **Plan de Acción de Emergencia (Emergency Action Plan)** `plan_de_accion_de_emergencia` — DATO LOCAL
- **Plan de Control de Infecciones en el Lugar de Trabajo** `plan_de_control_de_infecciones` — DATO LOCAL
- **Planes Estatales OSHA (State Plans)** `planes_estatales_osha` — DATO LOCAL
- **Prevención de Violencia en el Lugar de Trabajo** `prevencion_violencia_laboral` — DATO LOCAL
- **Programa de Consulta en Sitio de OSHA (On-Site Consultation)** `programa_consulta_osha_onsite` — DATO LOCAL
- **Programa de Protección al Denunciante (Whistleblower Protection)** `programa_proteccion_denunciantes` — DATO LOCAL · CORPORATIVO
- **Programas Cooperativos de OSHA (Asociaciones Estratégicas, Alianzas, VPP)** `programas_cooperativos_osha` — DATO LOCAL
- **Recursos Educativos y de Capacitación de OSHA** `recursos_educativos_osha` — DATO LOCAL
- **Recursos Externos de Apoyo en Seguridad (Aseguradoras, Asociaciones, SBDC)** `recursos_externos_seguridad` — DATO LOCAL
- **Registro y Reporte de Lesiones y Enfermedades Ocupacionales** `registro_reporte_lesiones` — DATO LOCAL
- **Seguridad como Responsabilidad Hacia Abajo, No Rendición de Cuentas Hacia Arriba** `responsabilidad_hacia_abajo_vs_rendicion_de_cuentas` — CORPORATIVO
- **Revisión de Aplicabilidad de Estándares OSHA** `revision_aplicabilidad_estandares_osha` — DATO LOCAL
- **Mantenimiento como Mayor Fuente de Fallas Humanas** `riesgo_actividades_mantenimiento` — MATRIZ
- … y 8 más (en el JSON)