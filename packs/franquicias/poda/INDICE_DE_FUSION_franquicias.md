# Índice de fusión de franquicias

13 clusters propuestos, 26 nodos de los 214 del pack.

**Borra las líneas de lo que NO debe fundirse. Lo que quede se consolida.**

## La regla del superviviente (vigente)

**Sobrevive el nodo con más historia.** La telemetría es la voz de los caminos reales, y conservar el id más pisado es lo que menos fricción crea con `project_nodes`. El contenido del que proponía el consolidador **no se pierde**: se rescata dentro del superviviente.

Si ningún nodo del cluster tiene historia, manda el propuesto del consolidador. **Tu ojo es la única excepción**: donde discrepes, tacha y escribe cuál debe quedarse.

`visto N` = veces que apareció en el recorrido de alguien. `cosechado N` = veces que se llevó a un plan. Ningún nodo se borra: los absorbidos salen de la selección y su id sigue existiendo.

## 1. 2 nodos · similitud 0.959 · sin historia

> Describen las mismas estrategias (Home-Sweet-Home, Spiking, etc.) para mezclar ubicaciones corporativas y franquiciadas.

**Sobrevive: `mix_ubicaciones_corporativas_franquicia`** (propuesto)

- [planificación] **Estrategias de Ubicación: Mix Franquicia-Corporativo** `estrategia_ubicacion_franquicia_corporativa` 
- [planificación] **Estrategia de Mezcla entre Ubicaciones Corporativas y de Franquicia** `mix_ubicaciones_corporativas_franquicia` **← SOBREVIVE**

## 2. 2 nodos · similitud 0.943 · sin historia

> Mismo principio de apalancamiento: no existe número mínimo de franquicias para ser rentable.

**Sobrevive: `principio_apalancamiento_numero_magico`** (propuesto)

- [validación] **El 'Número Mágico': Rentabilidad desde la Primera Franquicia** `leverage_una_sola_franquicia` 
- [planificación] **Principio del Apalancamiento: No Existe un 'Número Mágico' de Franquicias** `principio_apalancamiento_numero_magico` **← SOBREVIVE**

## 3. 2 nodos · similitud 0.936 · sin historia

> Mismo tema y misma acción: evaluar la efectividad y costos de la publicidad impresa en franquicias.

**Sobrevive: `publicidad_impresa_franquicia`** (propuesto)

- [ejecución] **Evaluación de la Publicidad Impresa en Franquicias** `publicidad_impresa_franquicia` **← SOBREVIVE**
- [ejecución] **Publicidad Impresa en la Venta de Franquicias** `publicidad_impresa_para_franquicias` 

## 4. 2 nodos · similitud 0.933 · sin historia

> Mismo ciclo de venta-calidad de franquicia descrito con palabras casi idénticas y la misma acción de balancear venta selectiva con soporte.

**Sobrevive: `ciclo_ventas_calidad_franquicia`** (propuesto)

- [ejecución] **Ciclo de Venta-Calidad de la Franquicia** `ciclo_venta_calidad_franquicia` 
- [ejecución] **Ciclo de Ventas-Calidad de la Franquicia** `ciclo_ventas_calidad_franquicia` **← SOBREVIVE**

## 5. 2 nodos · similitud 0.925 · sin historia

> Mismos criterios para seleccionar consultor de franquicias, misma acción de evaluación.

**Sobrevive: `seleccion_consultor_franquicias`** (propuesto)

- [planificación] **Criterios para Elegir un Consultor de Franquicias** `criterios_seleccion_consultor_franquicia` 
- [planificación] **Selección de un Consultor de Franquicias** `seleccion_consultor_franquicias` **← SOBREVIVE**

## 6. 2 nodos · similitud 0.923 · sin historia

> Misma acción: definir metas personales a 5 años antes de elegir estrategia de crecimiento.

**Sobrevive: `definir_meta_a_5_anos_antes_de_franquiciar`** (propuesto)

- [ideación] **Definición de Objetivos Personales para Elegir Estrategia de Crecimiento** `definicion_objetivos_personales_expansion` 
- [ideación] **Definir la Meta Personal a 5 Años Antes de Elegir Estrategia de Crecimiento** `definir_meta_a_5_anos_antes_de_franquiciar` **← SOBREVIVE**

## 7. 2 nodos · similitud 0.923 · sin historia

> Misma advertencia y acción: no copiar la estructura legal/financiera de competidores al franquiciar.

**Sobrevive: `evitar_copia_estructura_competencia`** (propuesto)

- [planificación] **Diferenciación en la Estructura Legal de la Franquicia** `diferenciacion_estructura_legal_franquicia` 
- [planificación] **Evitar Copiar la Estructura Legal/Financiera de Competidores** `evitar_copia_estructura_competencia` **← SOBREVIVE**

## 8. 2 nodos · similitud 0.919 · sin historia

> Ambos tratan la misma acción: contratar/elegir un abogado especializado en franquicias por su complejidad regulatoria.

**Sobrevive: `eleccion_abogado_franquicias`** (propuesto)

- [planificación] **Contratación de Asesoría Legal Especializada en Franquicias** `contratacion_abogado_franquicia` 
- [planificación] **Elección de un Abogado Especializado en Franquicias** `eleccion_abogado_franquicias` **← SOBREVIVE**

## 9. 2 nodos · similitud 0.918 · sin historia

> Mismo concepto de definir estructura de proveedores aprobados vs designados, misma acción de control de compras.

**Sobrevive: `estructura_proveedores_aprobados_designados`** (propuesto)

- [planificación] **Definir Estructura de Proveedores (Aprobados vs. Designados)** `estructura_proveedores_aprobados_designados` **← SOBREVIVE**
- [planificación] **Ventas de Productos y Estructura de Proveedores (Aprobados/Designados)** `ventas_productos_markup_proveedores` 

## 10. 2 nodos · similitud 0.918 · sin historia

> Ambos describen la misma acción de desarrollar el manual de operaciones como documento central del sistema.

**Sobrevive: `desarrollar_manual_operaciones`** (propuesto)

- [ejecución] **Desarrollo del Manual de Operaciones de Franquicia** `desarrollar_manual_operaciones` **← SOBREVIVE**
- [planificación] **Desarrollo del Manual de Operaciones** `manual_operaciones_desarrollo` 

## 11. 2 nodos · similitud 0.905 · sin historia

> Es el mismo concepto de 'Award vs Sale' en la calificación de candidatos a franquiciados, con texto casi idéntico.

**Sobrevive: `calificacion_prospectos_award`** (propuesto)

- [ejecución] **Calificación de Candidatos a Franquiciados (The Award)** `calificacion_candidatos_franquicia` 
- [ejecución] **Calificación de Prospectos: Concepto de 'Award' vs. 'Sale'** `calificacion_prospectos_award` **← SOBREVIVE**

## 12. 2 nodos · similitud 0.904 · sin historia

> Ambos describen el mismo análisis comparativo de estrategias de crecimiento (franquiciar vs. unidades propias vs. capital externo) antes de decidir franquiciar.

**Sobrevive: `decision_franquiciar_vs_expansion_propia`** (propuesto)

- [planificación] **Análisis de Estrategia de Crecimiento: Franquicia vs. Crecimiento Corporativo** `analisis_estrategia_crecimiento_franquicia_vs_corporativo` 
- [ideación] **Decisión Estratégica: Franquiciar vs. Expansión con Unidades Propias vs. Capital Externo** `decision_franquiciar_vs_expansion_propia` **← SOBREVIVE**

## 13. 2 nodos · similitud 0.903 · sin historia

> Ambos describen la misma acción de diseñar el mensaje de marketing balanceando contenido racional y emocional.

**Sobrevive: `mensaje_marketing_franquicia`** (propuesto)

- [planificación] **Balancear el Mensaje Emocional y el Racional en el Marketing** `mensaje_emocional_racional` 
- [ejecución] **Diseño del Mensaje de Marketing de Franquicia (Contenido y Emoción)** `mensaje_marketing_franquicia` **← SOBREVIVE**

---

## Las tres barandas nuevas en todo el pack

Los detectores corrieron sobre los 214 nodos, no sobre una muestra: son locales y gratis. 8 nodos dieron algún hallazgo.

- **CORPORATIVO**: 8 nodos


### 8 nodos con hallazgo que NO están en ningún cluster

Estos no los toca la fusión: son otra decisión, y va aparte.

- **Construcción del Equipo para el Lanzamiento de la Franquicia** `construccion_equipo_franquicia` — CORPORATIVO
- **Costos de Preparación para Crear la Nueva Entidad de Franquicia** `costos_preparacion_franquicia` — CORPORATIVO
- **Criterio 'Bazooka o Peashooter' para Elegir el Equipo Profesional** `criterio_bazooka_peashooter` — CORPORATIVO
- **El Efecto Palo de Hockey en el Crecimiento de Franquicias** `efecto_palo_hockey` — CORPORATIVO
- **Posicionamiento frente a Competidores** `posicionamiento_vs_competidores` — CORPORATIVO
- **Agenda de la Primera Llamada de Ventas** `proceso_primera_llamada` — CORPORATIVO
- **Programa de Cumplimiento para Mitigar Riesgo de Litigio** `programa_cumplimiento_legal` — CORPORATIVO
- **Rechazar Prospectos No Calificados con Delicadeza** `rechazo_gentil_prospecto` — CORPORATIVO