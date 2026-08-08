# Índice de fusión de exportacion

7 clusters propuestos, 15 nodos de los 158 del pack.

**Borra las líneas de lo que NO debe fundirse. Lo que quede se consolida.**

## La regla del superviviente (vigente)

**Sobrevive el nodo con más historia.** La telemetría es la voz de los caminos reales, y conservar el id más pisado es lo que menos fricción crea con `project_nodes`. El contenido del que proponía el consolidador **no se pierde**: se rescata dentro del superviviente.

Si ningún nodo del cluster tiene historia, manda el propuesto del consolidador. **Tu ojo es la única excepción**: donde discrepes, tacha y escribe cuál debe quedarse.

`visto N` = veces que apareció en el recorrido de alguien. `cosechado N` = veces que se llevó a un plan. Ningún nodo se borra: los absorbidos salen de la selección y su id sigue existiendo.

## 1. 3 nodos · similitud 0.942 · sin historia

> Todos describen el mismo concepto de Incoterms y las mismas obligaciones/costos entre comprador y vendedor.

**Sobrevive: `incoterms_reglas_comerciales_internacionales`** (propuesto)

- [ejecución] **Definición de Términos de Venta (Incoterms)** `definicion_terminos_de_venta` 
- [planificación] **Términos de Comercio Internacional (Incoterms)** `glosario_terminos_incoterms` 
- [planificación] **Incoterms: Términos Comerciales Internacionales (EXW, FCA, FAS, FOB)** `incoterms_reglas_comerciales_internacionales` **← SOBREVIVE**

## 2. 2 nodos · similitud 0.961 · sin historia

> Es la misma cláusula de control de destino exigida en documentos de embarque, solo cambia el nombre.

**Sobrevive: `clausula_antidesviacion`** (propuesto)

- [ejecución] **Declaración de Control de Destino (Antidiversion Clause)** `antidiversion_clause` 
- [ejecución] **Cláusula Antidesviación (Destination Control Statement)** `clausula_antidesviacion`  ·  **CORPORATIVO** **← SOBREVIVE**
    - CORPORATIVO: ...según la Parte 758.6 del EAR Consultar con un abogado, el Departamento de Comercio o el freight forwarder sobre la declaración a...

## 3. 2 nodos · similitud 0.958 · sin historia

> Ambos describen los mismos programas de financiamiento de la SBA para exportadores.

**Sobrevive: `financiamiento_sba_exportacion`** (propuesto)

- [ejecución] **Programas de Financiamiento de la SBA para Exportadores** `financiamiento_sba_exportacion` **← SOBREVIVE**
- [planificación] **Programas de la SBA para Financiamiento de Exportación** `programas_sba_exportacion` 

## 4. 2 nodos · similitud 0.944 · sin historia

> Ambos describen la misma decisión sobre el método de transporte internacional (marítimo, aéreo, multimodal).

**Sobrevive: `seleccion_metodo_transporte_internacional`** (propuesto)

- [ejecución] **Selección del Método de Envío Internacional** `seleccion_metodo_envio_internacional` 
- [ejecución] **Selección del Método de Transporte Internacional** `seleccion_metodo_transporte_internacional` **← SOBREVIVE**

## 5. 2 nodos · similitud 0.943 · sin historia

> Ambas describen la misma metodología de tres pasos para investigar mercados de exportación.

**Sobrevive: `enfoque_paso_a_paso_investigacion_mercado`** (propuesto)

- [validación] **Enfoque Paso a Paso para la Investigación de Mercados de Exportación** `enfoque_paso_a_paso_investigacion_mercado`  ·  **CORPORATIVO** **← SOBREVIVE**
    - CORPORATIVO: ...justificar con datos la elección de mercados meta ante la gerencia o inversionistas Lista corta (3-5) de mercados meta se...
- [validación] **Enfoque Paso a Paso para la Investigación de Mercado** `investigacion_mercado_paso_a_paso` 

## 6. 2 nodos · similitud 0.938 · sin historia

> Ambos describen el mismo acuerdo contractual de licenciamiento de tecnología con fines de internacionalización.

**Sobrevive: `licenciamiento_tecnologico`** (propuesto)

- [planificación] **Licenciamiento de Tecnología como Estrategia de Internacionalización** `licenciamiento_tecnologia` 
- [planificación] **Licenciamiento de Tecnología (Technology Licensing)** `licenciamiento_tecnologico` **← SOBREVIVE**

## 7. 2 nodos · similitud 0.934 · sin historia

> Ambos describen la misma normativa antiboicot de EE.UU. y la misma acción de cumplimiento.

**Sobrevive: `antiboycott_regulations`** (propuesto)

- [ejecución] **Cumplimiento de las Regulaciones Antiboicot** `antiboycott_regulations` **← SOBREVIVE**
- [ejecución] **Regulaciones Antiboicot en el Comercio Exterior** `regulaciones_antiboicot` 

---

## Las tres barandas nuevas en todo el pack

Los detectores corrieron sobre los 158 nodos, no sobre una muestra: son locales y gratis. 8 nodos dieron algún hallazgo.

- **CORPORATIVO**: 7 nodos
- **MATRIZ**: 1 nodos


### 6 nodos con hallazgo que NO están en ningún cluster

Estos no los toca la fusión: son otra decisión, y va aparte.

- **Asistencia de la Agencia de Desarrollo de Negocios de Minorías (MBDA)** `asistencia_agencias_minoritarias_mbda` — CORPORATIVO
- **Autoevaluación Gerencial para la Decisión de Exportar** `autoevaluacion_gerencial_exportacion` — CORPORATIVO
- **Evaluación de la Preparación de la Empresa para Exportar (Export Readiness)** `evaluacion_preparacion_empresa_exportar` — CORPORATIVO
- **Recursos de Agencias Gubernamentales para Exportadores** `recursos_gubernamentales_exportacion` — CORPORATIVO
- **Checklist para Seleccionar un Representante o Distribuidor Extranjero** `seleccion_representante_extranjero` — MATRIZ
- **Misiones Comerciales (Trade Missions)** `trade_missions` — CORPORATIVO