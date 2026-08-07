# Índice de fusión de quality

66 clusters propuestos, 156 nodos de los 896 del pack.

**Borra las líneas de lo que NO debe fundirse. Lo que quede se consolida.**

## Antes de empezar: el propuesto no siempre es el que la gente pisa

El `←  propuesto` es del consolidador, que juzga por CONTENIDO y no ve la
telemetría. Cruzándolo con `project_nodes`:

| | clusters |
|---|---:|
| el propuesto **es** el más visitado | 22 |
| el propuesto **no es** el más visitado | 20 |
| ningún nodo del cluster tiene historia | 24 |

En 20 de 66 hay que decidir a mano. El caso más caro es el **cluster 49**: se
propone conservar uno y el más pisado es `costo_de_calidad_3`, con 15 visitas.
Y en el **cluster 1**, el propuesto tiene *visto 1* mientras `costo_de_mala_calidad_copq`
lleva *visto 10 · cosechado 9*.

Mi lectura: cuando discrepan, **manda la telemetría** para elegir superviviente
y el contenido del propuesto se rescata dentro de él. Pero la decisión es tuya
cluster a cluster, y por eso van los dos datos juntos en cada línea.

Cada nodo trae su telemetría: `visto N` = veces que apareció en el recorrido de alguien, `cosechado N` = veces que se llevó a un plan. Un nodo con historia no se borra nunca (su id sobrevive); pero si es el que la gente pisa, probablemente sea el que debe quedarse como superviviente.

## 1. 7 nodos · similitud 0.967 · **4 con historia**

> Los siete nodos describen el mismo indicador COPQ: costos que desaparecerían si no hubiera fallos, con distintos matices de medición pero misma acción de cuantificar.

- [validación] **Costo de Mala Calidad (Cost of Poor Quality - COPQ)** `costo_de_mala_calidad_3`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...rar el COPQ resultante con las expectativas previas de la gerencia Identificar los 'pocos vitales' segmentos que concentr...
- [ejecución] **Costo de la Mala Calidad — COPQ (Costos que Desaparecerían sin Fallos)** `costo_de_mala_calidad_copq`  ·  visto 10 · cosechado 9 
- [validación] **Costo de la Mala Calidad — COPQ (Cómo se Mide)** `costo_de_mala_calidad_copq_2`  ·  visto 8 · cosechado 7 
- [ideación] **Costo de la Mala Calidad — COPQ (Incumplimiento de Requisitos)** `costo_de_mala_calidad_copq_3`  ·  visto 1 · cosechado 1 · **CORPORATIVO** 
    - CORPORATIVO: ...stos totales- y constituyen una oportunidad mayor para la alta dirección de mejorar la rentabilidad sin recortar funciones esen...
- [validación] **Costo de la Mala Calidad (En Promedio 15% de los Ingresos)** `costo_de_mala_calidad_copq_4`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...al y sirve como herramienta clave para justificar ante la gerencia la asignación de recursos a mejora de calidad. Los cos...
- [validación] **Costo de la Mala Calidad (Cost of Poor Quality - COPQ)** `costo_mala_calidad_copq`  ·  visto 1 · cosechado 1 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...le representar una cifra mucho mayor a la esperada por la alta dirección y es clave para justificar inversión en breakthrough....
- [validación] **Costo de la Calidad Pobre (COPQ / COP3)** `costo_pobre_calidad`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...para dimensionar su impacto Presentar los hallazgos a la alta dirección como justificación para iniciativas de mejora Cuando s...

## 2. 6 nodos · similitud 0.952 · **6 con historia**

> Los seis nodos son la misma definición central de Crosby: calidad = conformidad con los requisitos, rechazando nociones subjetivas.

- [ideación] **Calidad como Conformidad con los Requisitos (Rechazo de Definiciones Subjetivas)** `conformance_to_requirements`  ·  visto 2 · cosechado 2 
- [ideación] **Calidad como Conformidad a los Requisitos** `definicion_calidad_como_conformidad`  ·  visto 2 
- [ideación] **Calidad como Conformidad con los Requisitos (La Primera Suposición Errónea)** `definicion_calidad_conformidad`  ·  visto 13 · cosechado 13 
- [ideación] **Calidad como Conformidad con los Requisitos (El Ejemplo del Cadillac)** `definicion_calidad_conformidad_requisitos`  ·  visto 2 · cosechado 2 
- [ideación] **Definición de Calidad como Conformidad a los Requisitos** `definicion_calidad_conformidad_requisitos_2`  ·  visto 3 · cosechado 3 · **CORPORATIVO** 
    - CORPORATIVO: ...sobre si un producto o servicio es 'de calidad' Cuando el equipo de calidad y el de manufactura/operaciones tienen conflic...
- [ideación] **Definición de Calidad como Conformidad con los Requisitos** `definicion_calidad_conformidad_requisitos_3`  ·  visto 2 · cosechado 2 

## 3. 4 nodos · similitud 0.957 · **2 con historia**

> Los cuatro nodos describen el mismo concepto de Crosby: Zero Defects como actitud/estándar, no programa motivacional.

- [ejecución] **Cero Defectos (Zero Defects - ZD)** `cero_defectos`  ·  visto 16 · cosechado 11 **←  propuesto**
- [ejecución] **Zero Defects (ZD) como Actitud de Prevención** `cero_defectos_zd`  ·  visto 13 · cosechado 12 
- [ejecución] **Concepto de Zero Defects (Cero Defectos)** `concepto_zero_defects` 
- [planificación] **Programa de Cero Defectos (Zero Defects)** `programa_zero_defects`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...ino un estándar de desempeño dirigido principalmente a la gerencia. Su premisa es que los defectos no son inevitables y q...

## 4. 4 nodos · similitud 0.935 · **4 con historia**

> Las cuatro versiones describen la misma herramienta de Crosby con las mismas cinco etapas de madurez.

- [planificación] **Quality Management Maturity Grid (Evaluación sin Ser Experto)** `quality_management_maturity_grid`  ·  visto 2 · cosechado 2 · **CORPORATIVO** 
    - CORPORATIVO: ...d, ubicar el estado actual de la gestión de calidad de su organización en una de cinco etapas de madurez, evaluadas a través...
- [validación] **Quality Management Maturity Grid (Las Cinco Etapas de Madurez)** `quality_management_maturity_grid_2`  ·  visto 1 · cosechado 1 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...), evaluando seis categorías: comprensión y actitud de la gerencia, estatus de la organización de calidad, manejo de prob...
- [validación] **Quality Management Maturity Grid (Rejilla de Madurez en Gestión de Calidad)** `quality_management_maturity_grid_3`  ·  visto 2 · cosechado 2 · **CORPORATIVO** 
    - CORPORATIVO: ...que el retroceso es posible Comunicar el diagnóstico a la alta dirección para generar conciencia (Awakening) antes de pedir com...
- [validación] **Rejilla de Madurez de Gestión de Calidad (Quality Management Maturity Grid)** `rejilla_madurez_gestion_calidad`  ·  visto 11 · cosechado 11 · **CORPORATIVO** 
    - CORPORATIVO: ...inicia un diagnóstico organizacional de calidad Cuando la gerencia desconoce en qué nivel de madurez se encuentra su sist...

## 5. 3 nodos · similitud 0.960 · sin historia

> Los tres describen el mismo proceso de certificación/registro por tercera parte de sistemas de calidad tipo ISO 9000/9001.

- [ejecución] **Certificación/Registro del Sistema de Gestión de Calidad ISO 9000** `certificacion_iso_9000` 
- [validación] **Certificación y Registro de Sistemas de Calidad (Auditorías de Tercera Parte)** `certificacion_registro_sistema_calidad` **←  propuesto**
- [ejecución] **Certificación y Registro de Sistemas de Calidad (ISO 9001/9002)** `certificacion_registro_sistemas_calidad` 

## 6. 3 nodos · similitud 0.949 · sin historia

> Misma herramienta (Customer Needs Spreadsheet) descrita tres veces con distinto nombre

- [planificación] **Hoja de Cálculo de Necesidades del Cliente (Customer Needs Spreadsheet)** `customer_needs_spreadsheet` **←  propuesto**
- [ideación] **Customer Needs Spreadsheet** `hoja_de_necesidades_del_cliente` 
- [planificación] **Hoja de Necesidades del Cliente (Customer Needs Spreadsheet)** `hoja_necesidades_cliente` 

## 7. 3 nodos · similitud 0.948 · **2 con historia**

> Los tres nodos son la misma distinción de Deming entre causas comunes (sistema/gerencia) y causas especiales (asignables).

- [ejecución] **Causas Comunes y Causas Especiales de Variación** `causas_comunes_causas_especiales`  ·  visto 1 · cosechado 1 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...s son fallas inherentes al sistema (responsabilidad de la gerencia, aproximadamente 94% de los problemas), mientras que l...
- [ejecución] **Causas Comunes vs Causas Especiales de Variación** `causas_comunes_vs_especiales`  ·  visto 2 · cosechado 1 · **CORPORATIVO** 
    - CORPORATIVO: ...de Variación Las causas comunes son responsabilidad de la gerencia y provienen del diseño del sistema (mal diseño de prod...
- [ejecución] **Distinción entre Causas Comunes y Causas Especiales de Variación** `distincion_causas_comunes_especiales_3`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...es decir, del sistema mismo, y son responsabilidad de la gerencia. Las causas especiales son atribuibles a un trabajador...

## 8. 3 nodos · similitud 0.946 · sin historia

> Los tres describen la misma técnica de Value Stream Mapping con el mismo propósito y alcance.

- [planificación] **Mapeo de Flujo de Valor (De la Concepción a la Comercialización)** `mapeo_flujo_valor` 
- [planificación] **Mapeo de Flujo de Valor (Valor Agregado y No Agregado)** `mapeo_flujo_valor_2` 
- [ejecución] **Value Stream Mapping (Distinguir Valor de Desperdicio)** `value_stream_mapping_2` 

## 9. 3 nodos · similitud 0.944 · sin historia

> Las tres versiones describen la misma técnica de normalizar datos para comparar unidades distintas de forma justa.

- [ejecución] **Normalización de Datos en Benchmarking (Comparación Justa)** `normalizacion_datos_benchmarking` **←  propuesto**
- [ejecución] **Normalización de Datos en Benchmarking (Conversión a Forma Comparable)** `normalizacion_datos_benchmarking_2` 
- [ejecución] **Normalización de Datos para Comparaciones Justas** `normalizacion_de_datos` 

## 10. 3 nodos · similitud 0.935 · **1 con historia**

> Los tres describen el mismo concepto de sistema estable y la misma conclusión sobre responsabilidad gerencial de la variación.

- [validación] **Sistema Estable y Responsabilidad de la Gerencia sobre la Variación** `sistema_estable_causas_comunes`  ·  visto 7 · cosechado 7 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...Sistema Estable y Responsabilidad de la Gerencia sobre la Variación Cuando un proceso muestra variación...
- [validación] **Concepto de Sistema Estable** `sistema_estable_deming`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...ble determina si la responsabilidad de mejora recae en la gerencia (sistema) o en el trabajador individual. Recolectar da...
- [validación] **Sistema Estable y Responsabilidad de la Variación** `sistema_estable_variacion`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...e, la responsabilidad de mejorar el resultado recae en la gerencia, no en los trabajadores, ya que estos no pueden supera...

## 11. 3 nodos · similitud 0.925 · **1 con historia**

> Mismo mecanismo ECR para que empleados reporten causas de error, repetido tres veces

- [ejecución] **Eliminación de Causas de Error (Error-Cause Removal, ECR)** `eliminacion_causas_error_3` **←  propuesto**
- [ejecución] **Eliminación de Causas de Error (Error Cause Removal - ECR)** `eliminacion_causas_error_4`  ·  visto 8 · cosechado 7 · **CORPORATIVO** 
    - CORPORATIVO: ...de error que enfrentan en su trabajo diario, para que la gerencia las elimine de forma sistemática. Es un paso clave pos...
- [ejecución] **Sistema ECR (Error Cause Removal)** `programa_ecr_causa_de_error` 

## 12. 3 nodos · similitud 0.922 · **1 con historia**

> Mismo concepto de poka-yoke/mistake-proofing con los mismos cinco principios

- [ejecución] **Error-Proofing del Proceso (Poka-Yoke)** `errores_a_prueba_poka_yoke` 
- [ejecución] **Mistake Proofing / Poka-Yoke** `mistake_proofing_poka_yoke` **←  propuesto**
- [ejecución] **Mistake Proofing (Poka-Yoke)** `mistake_proofing_poka_yoke_2`  ·  visto 2 · cosechado 2 

## 13. 3 nodos · similitud 0.921 · sin historia

> Las tres describen la misma metodología DFSS/DMADV de cinco fases para diseño sin defectos

- [planificación] **Design for Six Sigma (DFSS) y Metodología DMADV** `design_for_six_sigma_dfss` **←  propuesto**
- [planificación] **Design for Six Sigma (DFSS)** `dfss_metodologia` 
- [planificación] **DMADV / Design for Six Sigma (DFSS)** `dmadv_design_for_six_sigma` 

## 14. 3 nodos · similitud 0.920 · sin historia

> Los tres nodos describen la misma técnica lean de 6 pasos (sort, set in order, shine/sweep, standardize, sustain, safety) para organizar el lugar de trabajo.

- [ejecución] **Metodología 6S para Lugares de Trabajo** `6s_lugar_trabajo` 
- [ejecución] **6S – Organización del Lugar de Trabajo** `6s_workplace_organization` 
- [ejecución] **Metodología 6S (Sort, Set in order, Shine, Standardize, Sustain, Safety)** `metodologia_6s` **←  propuesto**

## 15. 3 nodos · similitud 0.904 · **2 con historia**

> Los tres describen el mismo modelo de Crosby de costo de calidad compuesto por prevención, evaluación y fallas.

- [planificación] **El Costo de la Calidad (Prevención, Evaluación y Fallas)** `costo_de_calidad_5`  ·  visto 1 · cosechado 1 
- [planificación] **Costo de la Calidad (Cost of Quality - COQ)** `costo_de_calidad_6`  ·  visto 5 · cosechado 5 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...garantía posteriormente. La medición del COQ permite a la gerencia visualizar en términos financieros el impacto real de...
- [validación] **Costo de la Calidad como Medida Objetiva** `costo_de_la_calidad` 

## 16. 2 nodos · similitud 0.974 · **1 con historia**

> Mismo gráfico de cinco números (mín, Q1, mediana, Q3, máx) para comparar dispersión de datos.

- [ejecución] **Boxplot (Diagrama de Caja)** `boxplot_resumen_datos`  ·  visto 2 · cosechado 2 
- [ejecución] **Diagrama de Caja (Box Plot)** `diagrama_caja` **←  propuesto**

## 17. 2 nodos · similitud 0.970 · **2 con historia**

> Mismo quinto paso del programa de Crosby: comunicar el costo de la no calidad a los empleados.

- [ejecución] **Conciencia de Calidad (Paso 5)** `conciencia_calidad`  ·  visto 21 · cosechado 21 **←  propuesto**
- [ejecución] **Paso Cinco: Conciencia de Calidad** `conciencia_de_calidad`  ·  visto 5 · cosechado 5 

## 18. 2 nodos · similitud 0.968 · sin historia

> Misma comparación entre sistemas push y pull con la misma definición y consecuencias.

- [ejecución] **Sistemas Pull versus Push** `pull_vs_push_systems` 
- [ejecución] **Sistemas Pull versus Push en Producción** `sistema_pull_push` **←  propuesto**

## 19. 2 nodos · similitud 0.963 · sin historia

> Mismos cinco principios del programa de auditoría de calidad descritos igual, solo con distinto pilar.

- [planificación] **Principios del Programa de Auditoría de Calidad (Los Cinco Principios)** `principios_auditoria_calidad` **←  propuesto**
- [validación] **Principios del Programa de Auditoría de Calidad (Hechos y Actitud de Servicio)** `principios_del_programa_de_auditoria_de_calidad` 

## 20. 2 nodos · similitud 0.956 · sin historia

> Misma distinción entre características clave de producto (salidas) y de proceso (entradas).

- [planificación] **Identificación de Características Clave de Producto y Proceso** `caracteristicas_clave_producto_proceso` 
- [planificación] **Características Clave de Producto y Proceso (KPC)** `key_process_product_characteristics` **←  propuesto**

## 21. 2 nodos · similitud 0.956 · **1 con historia**

> Mismo principio de diseño de redundancia en paralelo para reducir probabilidad de falla, mismo cálculo pi².

- [planificación] **Uso de Redundancia en Diseño para Mejorar la Confiabilidad** `redundancia_diseno_confiabilidad` 
- [planificación] **Uso de Redundancia en el Diseño de Componentes Críticos** `redundancia_en_diseno`  ·  visto 2 · cosechado 2 **←  propuesto**

## 22. 2 nodos · similitud 0.954 · **1 con historia**

> Misma clasificación de las cuatro escalas de medición (razón, intervalo, ordinal, nominal) con los mismos ejemplos.

- [planificación] **Tipos de Escalas de Medición de Datos** `tipos_de_escalas_de_medicion` **←  propuesto**
- [planificación] **Tipos de Escalas de Medición** `tipos_escalas_medicion`  ·  visto 1 · cosechado 1 

## 23. 2 nodos · similitud 0.951 · **2 con historia**

> Misma definición de calidad como aptitud para el propósito, misma idea repetida

- [ideación] **Definición de Calidad como 'Fitness for Purpose'** `definicion_calidad_fitness_for_purpose`  ·  visto 8 · cosechado 8 **←  propuesto**
- [ideación] **Calidad como 'Fitness for Purpose'** `definicion_fitness_for_purpose`  ·  visto 3 · cosechado 3 · **CORPORATIVO** 
    - CORPORATIVO: ...dad y necesita establecer qué significa 'calidad' para su organización o producto Documento de definición de 'fitness for pur...

## 24. 2 nodos · similitud 0.950 · **2 con historia**

> Misma idea de identificar riesgos antes de gestionarlos, con la misma definición de riesgo

- [planificación] **Identificación de Riesgos Operacionales** `gestion_riesgo_identificacion`  ·  visto 1 · cosechado 1 
- [validación] **Identificación de Riesgos** `identificacion_de_riesgos`  ·  visto 2 · cosechado 2 **←  propuesto**

## 25. 2 nodos · similitud 0.949 · **1 con historia**

> Ambos describen el mismo modelo que grafica costos de falla vs evaluación/prevención para hallar el punto óptimo.

- [planificación] **Costo Óptimo de Calidad** `costo_optimo_calidad` 
- [validación] **Modelo de Costo Óptimo de Calidad** `modelo_costo_optimo_calidad`  ·  visto 1 · cosechado 1 **←  propuesto**

## 26. 2 nodos · similitud 0.948 · **2 con historia**

> Mismo paso del programa de calidad (medir estado actual incluyendo áreas no productivas) con distinto pilar asignado.

- [planificación] **Medición de la Calidad (Paso 3)** `medicion_calidad`  ·  visto 21 · cosechado 9 **←  propuesto**
- [ejecución] **Paso Tres: Medición de Calidad** `medicion_de_calidad`  ·  visto 1 

## 27. 2 nodos · similitud 0.947 · sin historia

> Ambos describen la misma auditoría periódica del sistema de control de calidad y por qué se deteriora.

- [validación] **Auditoría del Sistema de Control de Calidad (Por Qué se Deteriora)** `auditoria_sistema_control_calidad` 
- [ejecución] **Auditoría del Sistema de Control de Calidad (Verificación Periódica)** `auditoria_sistema_control_calidad_2`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...rsonal o cambios significativos en los procesos Cuando la alta dirección requiere garantías sobre el estado del sistema de cali...

## 28. 2 nodos · similitud 0.946 · sin historia

> Mismo caso de Deming sobre eliminar firmas/revisiones redundantes y diluir responsabilidad

- [ejecución] **Eliminación de firmas duplicadas y asignación de responsabilidad única** `eliminacion_de_firmas_duplicadas_responsabilidad_unica` 
- [ejecución] **Eliminación de Firmas y Revisiones Redundantes en Procesos Administrativos** `eliminacion_firmas_redundantes` **←  propuesto**

## 29. 2 nodos · similitud 0.942 · sin historia

> Ambos describen el mismo sistema de KPIs vinculado a metas estratégicas con los mismos criterios de diseño.

- [ejecución] **Medir el Progreso con Indicadores Clave de Desempeño (KPI)** `medir_progreso_kpi` 
- [ejecución] **Sistema de Medición con Indicadores Clave de Desempeño (KPI)** `sistema_medicion_kpi`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...onales y se requiere monitorear su cumplimiento Cuando la alta dirección necesita información oportuna para la toma de decision...

## 30. 2 nodos · similitud 0.942 · sin historia

> Mismo hallazgo sobre el impacto del manejo de quejas en la lealtad, con las mismas estadísticas del 70%

- [ejecución] **Gestión de Quejas y su Impacto en la Fidelización** `gestion_de_quejas_y_fidelizacion` 
- [ejecución] **Sistema Organizado de Manejo de Quejas** `sistema_manejo_quejas` **←  propuesto**

## 31. 2 nodos · similitud 0.938 · sin historia

> Mismo concepto de los ocho desperdicios de Ohno, con la misma lista de tipos de desperdicio.

- [planificación] **Los Ocho Desperdicios de Ohno (Lean)** `ocho_desperdicios` 
- [ejecución] **Los Ocho Desperdicios de Lean (Ohno)** `ocho_desperdicios_lean`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...iente de procesos, inventario, movimiento, defectos, y recursos humanos/creatividad subutilizados. Los practicantes Lean deben...

## 32. 2 nodos · similitud 0.937 · **1 con historia**

> Mismo enfoque de operaciones ante problemas esporádicos y crónicos usando mejora y planificación de calidad

- [planificación] **Enfoque en la Mejora Continua en Operaciones** `enfoque_mejora_continua_operaciones`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...requiere una cultura de calidad positiva, apoyada por el departamento de calidad como socio interno de operaciones. Diagnostica...
- [ejecución] **Enfoque de Mejora Continua en Operaciones** `mejora_continua_operaciones`  ·  visto 1 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...nterdepartamentales Dar soporte técnico continuo desde el departamento de calidad a operaciones Cuando una organización necesita...

## 33. 2 nodos · similitud 0.930 · **1 con historia**

> Misma metáfora de Crosby (ballet vs hockey) para describir los mismos dos estilos de gestión de calidad

- [planificación] **Estilo Gerencial: Ballet (Prevención) vs. Hockey (Detección)** `crosby_estilo_ballet_vs_hockey`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...isis constante' resolviendo problemas repetidos Cuando la alta dirección exige que la función de calidad prevenga en lugar de s...
- [ideación] **Estilo Gerencial: Ballet (Prevención) vs Hockey (Detección)** `estilo_gerencial_ballet_vs_hockey`  ·  visto 1 · cosechado 1 

## 34. 2 nodos · similitud 0.930 · **1 con historia**

> Mismo modelo DMAIC de Six Sigma descrito con las mismas fases y origen

- [ejecución] **Modelo de Mejora DMAIC de Six Sigma** `dmaic_six_sigma` 
- [ejecución] **Modelo Six Sigma DMAIC** `six_sigma_dmaic`  ·  visto 2 · cosechado 2 **←  propuesto**

## 35. 2 nodos · similitud 0.928 · **1 con historia**

> Mismo modelo Juran de Quality by Design, primer proceso de la Trilogía

- [ideación] **Modelo Juran de Calidad por Diseño (Quality by Design)** `juran_quality_by_design`  ·  visto 1 · cosechado 1 
- [planificación] **Modelo Universal de Quality by Design (Juran)** `modelo_quality_by_design_juran` **←  propuesto**

## 36. 2 nodos · similitud 0.926 · sin historia

> Mismo mecanismo de impacto de la calidad en ingresos (premium, liderazgo), el segundo solo añade la relación con costos

- [validación] **Impacto de la Calidad en los Ingresos** `impacto_calidad_en_ingresos` 
- [validación] **Impacto de la Calidad en Ingresos y Costos** `impacto_calidad_ingresos_costos`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...o se necesita justificar una inversión en calidad ante la alta dirección enfocada en crecimiento de ingresos Al construir un ca...

## 37. 2 nodos · similitud 0.925 · **1 con historia**

> Mismo programa de catorce pasos de Crosby descrito con la misma estructura y propósito.

- [ejecución] **Los Catorce Pasos de Mejora de Calidad de Crosby** `programa_catorce_pasos_crosby`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...ista de casillas a marcar. Establecer el compromiso de la gerencia (management commitment) Formar equipos de mejora de ca...
- [ejecución] **Programa de Mejora de Calidad (Los Catorce Pasos)** `programa_de_mejora_de_calidad`  ·  visto 3 · cosechado 3 · **CORPORATIVO** 
    - CORPORATIVO: ...ionales temporales. Obtener el compromiso explícito de la alta dirección con la mejora de calidad Formar un equipo de mejora de...

## 38. 2 nodos · similitud 0.924 · **2 con historia**

> Mismo punto de equilibrio de calidad (k1/k2) y misma regla todo-o-nada de inspección de Deming.

- [planificación] **Punto de Equilibrio de Calidad y Regla Todo-o-Nada en Inspección** `punto_equilibrio_calidad`  ·  visto 2 
- [planificación] **Punto de Equilibrio de Calidad (Break-even Quality) para Decisiones de Inspección** `punto_equilibrio_calidad_inspeccion`  ·  visto 2 · cosechado 2 **←  propuesto**

## 39. 2 nodos · similitud 0.922 · **2 con historia**

> Contenido idéntico sobre usar histogramas y curva de probabilidad para evaluar capacidad de proceso; solo cambia la etiqueta de tipo.

- [validación] **Análisis de Capacidad de Proceso mediante Histogramas** `analisis_capacidad_procesos`  ·  visto 1 · cosechado 1 **←  propuesto**
- [ejecución] **Análisis de Histogramas para Capacidad de Proceso** `histograma_analisis`  ·  visto 1 · cosechado 1 

## 40. 2 nodos · similitud 0.922 · **1 con historia**

> Ambos describen el mismo enfoque estadístico para tolerancias interactuantes frente a la suma tradicional conservadora.

- [planificación] **Límites de Especificación para Dimensiones Interactuantes (Stack-up de Tolerancias)** `limites_especificacion_dimensiones_interactuantes`  ·  visto 1 
- [planificación] **Tolerancia Estadística para Dimensiones Interactuantes** `tolerancia_estadistica_dimensiones_interactuantes` **←  propuesto**

## 41. 2 nodos · similitud 0.922 · **2 con historia**

> Mismo concepto sobre cuándo el perfeccionismo es desperdicio versus cuándo es necesario, con los mismos ejemplos.

- [planificación] **Perfeccionismo como Desperdicio de Valor (Cuándo la Perfección Sí Vale)** `perfeccionismo_vs_valor`  ·  visto 1 · cosechado 1 
- [ejecución] **Perfeccionismo como Desperdicio de Valor (Contextos Críticos vs Desperdicio)** `perfeccionismo_vs_valor_2`  ·  visto 1 · cosechado 1 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...n mejora perceptible en la satisfacción del cliente Si el equipo de diseño tiende a sobre-especificar productos más allá d...

## 42. 2 nodos · similitud 0.922 · **1 con historia**

> Ambos son el mismo punto de Deming sobre el propósito del liderazgo: mejorar el sistema, no señalar culpables.

- [ejecución] **Objetivo del Liderazgo (Deming)** `aim_of_leadership`  ·  visto 2 · cosechado 2 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...métodos Cuando un líder busca mejorar el desempeño de su equipo Cuando se detectan fallas recurrentes atribuidas errón...
- [ejecución] **Liderazgo Orientado a Mejorar el Sistema** `liderazgo_para_mejora_continua` 

## 43. 2 nodos · similitud 0.920 · **1 con historia**

> Mismo punto de Crosby sobre el supervisor como clave y su necesidad de entrenamiento

- [ejecución] **Entrenamiento de Supervisores (Paso 8 de Crosby)** `entrenamiento_supervisores_2`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...to ZD a los supervisores antes de que lo repliquen con su equipo Resolver dudas individuales de los supervisores con el...
- [ejecución] **Entrenamiento de Supervisores (El Supervisor como Clave)** `entrenamiento_supervisores_calidad`  ·  visto 3 · cosechado 3 **←  propuesto**

## 44. 2 nodos · similitud 0.918 · **1 con historia**

> Mismo modelo de evaluación Shingo con las mismas cuatro dimensiones y puntajes

- [validación] **Evaluación de Madurez mediante Escalas Shingo** `evaluacion_madurez_shingo`  ·  **MATRIZ** 
    - MATRIZ: ...os procesos y comportamientos clave de la organización Puntuar cada dimensión (cultura, mejora continua, alineación,...
- [validación] **Modelo Shingo de Evaluación de Excelencia Operacional** `modelo_shingo_evaluacion_excelencia`  ·  visto 2 · cosechado 2 · **MATRIZ** **←  propuesto**
    - MATRIZ: ...procesos, alineación, resultados) Aplicar la matriz de puntuación diferenciando roles (liderazgo senior, gerentes, asoci...

## 45. 2 nodos · similitud 0.917 · **1 con historia**

> Mismo fenómeno (necesidades ocultas/vacíos de conocimiento del cliente) con el mismo ejemplo del Walkman

- [ideación] **Descubrimiento de Necesidades Ocultas del Cliente** `descubrir_necesidades_ocultas` **←  propuesto**
- [ideación] **Vacíos en el Conocimiento del Cliente** `vacios_conocimiento_cliente`  ·  visto 8 · cosechado 8 

## 46. 2 nodos · similitud 0.917 · sin historia

> Ambos plantean la misma idea de Crosby: la calidad es gratis, lo que cuesta es el incumplimiento.

- [ideación] **Quality is Free (La Calidad es Gratis)** `concepto_quality_is_free`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...idades de no-calidad como referencia base. Comunicar a la alta dirección que invertir en prevención reduce estos costos y mejor...
- [validación] **El Costo de la Calidad (Por Qué la Calidad es Gratis)** `costo_de_calidad_crosby`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...económicamente un programa de mejora de calidad Cuando la gerencia no percibe la gravedad del problema de calidad Un info...

## 47. 2 nodos · similitud 0.915 · sin historia

> Mismo primer punto de Deming sobre falta de constancia de propósito y ausencia de plan a largo plazo

- [ideación] **Falta de Constancia de Propósito (La Enfermedad Más Incapacitante)** `falta_de_constancia_de_proposito`  ·  **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...aración formal de constancia de propósito aprobada por la alta dirección...
- [planificación] **Falta de Constancia de Propósito (Ausencia de Plan a Largo Plazo)** `falta_de_constancia_de_proposito_2` 

## 48. 2 nodos · similitud 0.914 · **2 con historia**

> Mismo problema (defectos raros) y misma solución (cartas/gráficos de control) descritos igual

- [ejecución] **Detección de Defectos Extremadamente Raros mediante Cartas de Control** `deteccion_defectos_raros_control_estadistico`  ·  visto 2 · cosechado 2 **←  propuesto**
- [ejecución] **Uso de Gráficos de Control para Detectar Defectos Raros** `graficos_control_defectos_raros`  ·  visto 1 · cosechado 1 

## 49. 2 nodos · similitud 0.913 · **2 con historia**

> Ambos describen el mismo concepto del costo de calidad como suma de gastos por hacer las cosas mal (scrap, rework, garantías, inspección).

- [ejecución] **Paso 4: Costo de la Calidad** `costo_de_calidad_3`  ·  visto 15 · cosechado 15 · **CORPORATIVO** 
    - CORPORATIVO: ...erencia (2.5%-4% de ventas) Presentar los resultados a la alta dirección como base para justificar el programa de mejora Establ...
- [validación] **Costo de Calidad (Cost of Quality)** `costo_de_calidad_4`  ·  visto 4 · cosechado 4 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...resentar las cifras al equipo de mejora de calidad y a la gerencia para generar conciencia real del impacto financiero Us...

## 50. 2 nodos · similitud 0.911 · sin historia

> Ambos tratan la misma idea de que la superioridad de calidad afecta la cuota de mercado solo si es percibida claramente.

- [validación] **Relación entre Calidad y Cuota de Mercado** `relacion_calidad_cuota_mercado` 
- [validación] **Superioridad de Calidad y Participación de Mercado** `superioridad_calidad_market_share` **←  propuesto**

## 51. 2 nodos · similitud 0.911 · **2 con historia**

> Ambos describen el mismo tercer punto de Deming: dejar de depender de la inspección masiva porque no construye calidad.

- [ejecución] **Abolición de la Inspección Masiva como Estrategia de Calidad** `abolir_inspeccion_masiva`  ·  visto 2 
- [ejecución] **Cesar la Dependencia de la Inspección Masiva** `cese_dependencia_inspeccion_masiva`  ·  visto 1 · cosechado 1 **←  propuesto**

## 52. 2 nodos · similitud 0.907 · **2 con historia**

> Mismo fenómeno de sesgo por muestreo mecánico frente al aleatorio, descrito desde dos ángulos del mismo hecho

- [ejecución] **Distorsión por Muestreo Mecánico** `distorsion_muestreo_mecanico`  ·  visto 2 · cosechado 2 
- [planificación] **Muestreo Aleatorio vs Muestreo Mecánico** `muestreo_aleatorio_vs_mecanico`  ·  visto 1 · cosechado 1 **←  propuesto**

## 53. 2 nodos · similitud 0.907 · sin historia

> Misma decisión de aptitud para el uso, solo varía la traducción del término en inglés (Purpose/Use)

- [ejecución] **Decisión de Aptitud para el Uso (Fitness for Purpose)** `decision_aptitud_para_uso` 
- [ejecución] **Decisión de Aptitud para el Uso (Fitness for Use)** `decision_aptitud_uso` **←  propuesto**

## 54. 2 nodos · similitud 0.907 · **1 con historia**

> Ambos describen las mismas cuatro categorías de costos de calidad (apreciación, fallo interno, fallo externo, prevención), uno aplicado a un caso concreto.

- [validación] **Los cuatro costos de calidad: apreciación, fallo interno, fallo externo y prevención** `costos_de_calidad_cuatro_categorias` 
- [planificación] **Los Cuatro Costos de la Calidad** `cuatro_costos_de_calidad`  ·  visto 5 · cosechado 4 **←  propuesto**

## 55. 2 nodos · similitud 0.906 · **1 con historia**

> Ambos describen el mismo ciclo iterativo PDSA de Shewhart/Deming.

- [ejecución] **Ciclo Plan-Do-Study-Act (PDSA / Ciclo de Shewhart-Deming)** `ciclo_pdsa` **←  propuesto**
- [ejecución] **Ciclo PDSA (Plan-Do-Study-Act)** `pdsa_shewhart_cycle`  ·  visto 1 · cosechado 1 

## 56. 2 nodos · similitud 0.905 · **2 con historia**

> Ambos describen la misma condición de Deming: el método de medición (instrumento+operador) debe estar en control estadístico para ser válido.

- [ejecución] **Control Estadístico del Método de Prueba (Instrumento y Operador)** `control_estadistico_de_metodo_de_prueba`  ·  visto 1 · cosechado 1 
- [ejecución] **Control Estadístico del Método de Medición (Condición de Validez)** `control_estadistico_metodo_medicion`  ·  visto 6 · cosechado 6 **←  propuesto**

## 57. 2 nodos · similitud 0.904 · **2 con historia**

> Mismo marco conceptual (planificación, control, mejora de Juran) descrito con las mismas tres fases.

- [ideación] **La Trilogía de Juran: Planificación, Control y Mejora** `juran_trilogy`  ·  visto 1 · cosechado 1 
- [planificación] **Trilogía de Juran (Planificación, Control y Mejora)** `trilogia_de_juran`  ·  visto 10 · cosechado 1 **←  propuesto**

## 58. 2 nodos · similitud 0.903 · **2 con historia**

> Mismo llamado a involucrar al sindicato tempranamente en el programa de calidad

- [ejecución] **Involucramiento del Sindicato en el Programa de Calidad** `involucramiento_sindical`  ·  visto 1 · cosechado 1 
- [planificación] **Involucramiento del Sindicato en Programas de Calidad** `involucramiento_sindical_calidad`  ·  visto 12 · cosechado 12 · **CORPORATIVO** **←  propuesto**
    - CORPORATIVO: ...lita la identificación de personas clave para integrar el equipo de mejora. Convocar a representantes sindicales para expl...

## 59. 2 nodos · similitud 0.902 · sin historia

> Mismo sistema de normas ISO 9000, descrito con distinto énfasis pero mismo referente

- [planificación] **Familia de Normas ISO 9000** `familia_normas_iso_9000` **←  propuesto**
- [planificación] **Sistema de Gestión de Calidad ISO 9000/9001** `iso_9000_sistema_gestion_calidad`  ·  **CORPORATIVO** 
    - CORPORATIVO: ...ares internacionales de gestión de calidad creados por el Comité Técnico 176 de ISO, aplicables a cualquier producto, s...

## 60. 2 nodos · similitud 0.902 · sin historia

> Ambos explican el mismo concepto de takt time como ritmo de demanda que guía el cálculo y diseño de producción.

- [planificación] **Takt Time y Producción en Flujo** `takt_time` **←  propuesto**
- [ejecución] **Takt Time y Gestión de la Demanda** `takt_time_demand` 

## 61. 2 nodos · similitud 0.902 · **1 con historia**

> Ambos explican la acción correctiva como troubleshooting de no conformidades esporádicas, distinguiéndola de los problemas crónicos.

- [ejecución] **Acción Correctiva (Esporádica vs Crónica)** `accion_correctiva`  ·  visto 8 · cosechado 4 **←  propuesto**
- [ejecución] **Acción Correctiva: Diagnóstico y Remedio de Problemas Esporádicos** `accion_correctiva_diagnostico_remedio` 

## 62. 2 nodos · similitud 0.902 · sin historia

> Mismo concepto de QFD como matrices que traducen necesidades del cliente en características técnicas.

- [planificación] **Despliegue de la Función de Calidad (QFD)** `qfd_matriz` **←  propuesto**
- [planificación] **Quality Function Deployment (QFD) - Matriz de Planificación de Calidad** `qfd_matriz_calidad` 

## 63. 2 nodos · similitud 0.901 · sin historia

> Ambos describen el mismo mecanismo sensor-comparador(umpire)-actuador del control de calidad.

- [ejecución] **El Bucle de Retroalimentación (Feedback Loop) en Control de Calidad** `bucle_retroalimentacion_control` **←  propuesto**
- [ejecución] **Ciclo de Retroalimentación de Control (Sensor-Estándar-Actuador)** `ciclo_de_retroalimentacion_control` 

## 64. 2 nodos · similitud 0.901 · sin historia

> Mismo concepto de diseño para factores críticos y reducción de error humano, solo cambia la fase asignada

- [ejecución] **Diseño para Factores Críticos y Error Humano** `diseno_para_factores_criticos` 
- [planificación] **Diseño para Factores Críticos y Reducción de Error Humano** `diseno_para_factores_criticos_y_error_humano` **←  propuesto**

## 65. 2 nodos · similitud 0.901 · **1 con historia**

> Ambos describen el mismo sexto paso del programa de Crosby: un método sistemático para resolver problemas identificados.

- [ejecución] **Paso Seis: Acción Correctiva** `accion_correctiva_3` **←  propuesto**
- [ejecución] **Acción Correctiva (Corrective Action)** `accion_correctiva_5`  ·  visto 5 · cosechado 5 

## 66. 2 nodos · similitud 0.901 · **2 con historia**

> Misma herramienta (principio de Pareto, pocos vitales/muchos útiles) para priorizar problemas.

- [ejecución] **Análisis de Pareto** `analisis_pareto`  ·  visto 2 · cosechado 2 
- [validación] **Análisis de Pareto para Priorización de Problemas** `analisis_pareto_priorizacion`  ·  visto 1 · cosechado 1 **←  propuesto**

---

## Las tres barandas nuevas en todo el pack

Los detectores corrieron sobre los 896 nodos, no sobre una muestra: son locales y gratis. 209 nodos dieron algún hallazgo.

- **CORPORATIVO**: 197 nodos
- **MATRIZ**: 9 nodos
- **DATO LOCAL**: 4 nodos


### 168 nodos con hallazgo que NO están en ningún cluster

Estos no los toca la fusión: son otra decisión, y va aparte.

- **Acción Correctiva Sistemática (Paso 6 de Crosby)** `accion_correctiva_sistematica` — CORPORATIVO
- **Adaptaciones Sectoriales de ISO 9000 (cGMP y ISO/TS 16949)** `adaptaciones_sectoriales_iso` — DATO LOCAL
- **Adoptar e Instituir el Liderazgo (Punto 7)** `adopcion_liderazgo` — CORPORATIVO
- **Alineación Estratégica y Despliegue de Objetivos de Calidad** `alineacion_estrategica_despliegue` — CORPORATIVO
- **Análisis de Tendencias con Gráficos de Control (Cause-Effect Charting)** `analisis_causa_efecto_indicadores_calidad` — CORPORATIVO
- **Análisis de Datos y Reporte de Estatus** `analisis_datos_reporte_estatus` — CORPORATIVO
- **Aseguramiento de la Participación de la Alta Dirección** `aprobacion_alta_direccion` — CORPORATIVO
- **Auditoría de Negocio (Business Audit)** `auditoria_negocio` — CORPORATIVO
- **Auditorías Gerenciales Periódicas** `auditorias_gerenciales_periodicas` — CORPORATIVO
- **Ausencia de Valor Verdadero en Mediciones** `ausencia_valor_verdadero` — CORPORATIVO
- **Planificación del Autocontrol (Self-Control) en Servicios** `autocontrol_planificacion_servicio` — CORPORATIVO
- **Autocontrol (Self-Control) y Controlabilidad** `autocontrol_y_controlabilidad` — CORPORATIVO
- **Benchmarking: Definición y Proceso** `benchmarking_proceso` — CORPORATIVO
- **Ruptura Cultural (Breakthrough in Culture)** `breakthrough_cultural` — CORPORATIVO
- **Ruptura en el Desempeño Actual (Breakthrough in Current Performance)** `breakthrough_desempeno_actual` — CORPORATIVO
- **Buenas Prácticas de Manufactura Actuales (cGMP)** `buenas_practicas_manufactura_cgmp` — DATO LOCAL
- **Sistema de Calificación de Compradores (Buyer Rating)** `buyer_rating_system` — CORPORATIVO
- **Reacción en Cadena: Calidad, Productividad, Costos y Mercado** `cadena_reaccion_calidad_productividad` — CORPORATIVO
- **Cálculo del Retorno de Inversión (ROI) en Calidad** `calculo_roi_calidad` — CORPORATIVO
- **Cambio de Actitudes Gerenciales mediante Pares y Pilotos** `cambio_actitud_gerencial` — CORPORATIVO
- **Eliminación del Carryover de Características Propensas a Fallas** `carryover_fallas_producto` — CORPORATIVO
- **Caso Práctico: Definición Operacional de una 'Arruga'** `caso_definicion_arruga` — CORPORATIVO
- **Comunicación Catch Ball para Despliegue de Metas** `catch_ball_comunicacion` — CORPORATIVO
- **Categorías de Brechas en el Desempeño de Materiales Entrantes** `categorias_de_material_entrante` — CORPORATIVO
- **Certificación de Belts en Six Sigma** `certificacion_belts_six_sigma` — CORPORATIVO
- **Las Cinco Suposiciones Erróneas sobre la Calidad** `cinco_suposiciones_erroneas_calidad` — CORPORATIVO
- **Círculos de Calidad (La Gerencia Debe Actuar)** `circulos_calidad_qc` — CORPORATIVO
- **Clasificación de Seriedad (Seriousness Classification)** `clasificacion_seriedad` — CORPORATIVO
- **Clasificación de Seriedad de Defectos (Características y Defectos por Gravedad)** `clasificacion_seriedad_defectos` — CORPORATIVO
- **Comité Ad Hoc para el Programa Cero Defectos (Paso 7)** `comite_cero_defectos` — CORPORATIVO
- **Riesgo de comprar solo por el precio más bajo** `compra_por_precio_mas_bajo_como_error` — CORPORATIVO
- **Comprensión y Priorización de Brechas de Desempeño** `comprension_brechas_desempeno` — CORPORATIVO
- **Paso Uno: Compromiso de la Dirección** `compromiso_gerencial_calidad` — CORPORATIVO
- **Concepto de Autocontrol (Self-Control) del Trabajador** `concepto_autocontrol` — CORPORATIVO
- **Haciendo la Calidad Cierta (Making Quality Certain)** `concepto_haciendo_la_calidad_cierta` — CORPORATIVO
- **Consejo de Calidad (Liderazgo y Selección de Proyectos — Juran)** `consejo_de_calidad` — CORPORATIVO
- **Consejo de Calidad (Red Autogestionada de Profesionales — Crosby)** `consejo_de_calidad_2` — CORPORATIVO
- **Consejo de Calidad y Rol del Director de Calidad** `consejo_de_calidad_y_rol_del_director` — CORPORATIVO
- **Formar un Consejo Ejecutivo de Calidad** `consejo_ejecutivo_calidad` — CORPORATIVO
- **Paso 13: Consejos de Calidad (Quality Councils)** `consejos_de_calidad` — CORPORATIVO
- … y 128 más (en el JSON)