# AUD-07 · Fase P1-HSEQ: Saneamiento de los Dominios Específicos

**Estado: cerrado. Tag `hseq-sanitized-v1`.** Saneamiento completo de los
tres dominios aislados en `packs/` (environmental, health_safety,
quality), generados por `scripts/pipeline_dominio.py` desde 10 libros.
Mismo estándar Gate 0 que el core recorrió en la Fase 1, ejecutado con
los 7 scripts del auditor (`scripts/hseq/`) más dos piezas nacidas de la
evidencia en vivo (paso 3b y paso 7). El core (`dataset/nodos/`) quedó
intocado, como mandaba la regla de piedra; ninguna operación cruzó
dominios.

## Resultado final

```
GATE 0 HSEQ: VERDE (los tres dominios)
  environmental: 311 nodos | health_safety: 332 | quality: 896 (total 1539)
  0 referencias rotas · simetría 100% · títulos únicos · ids ASCII ·
  dominio estampado correcto · alcanzabilidad 100% desde las semillas
```

## Números por checkpoint

| Paso | Resultado |
|---|---|
| 0 · Censo | 1557 nodos reales (314/336/907); 6 archivos de bookkeeping movidos de `nodos/` a `metadata/` (reconcilia el conteo 1554 vs 1563: eran esos 6 no-nodos más imprecisión del spot-check) |
| 1 · ASCII | 14 ids transliterados (6/2/6), 25 nodos con referencias reescritas, originales en `ids_alias` |
| 2 · Dedup | 132 grupos candidatos → **15 aprobados** (11%), 17 nodos absorbidos → 312/332/896. Decisión commiteada ANTES de la fusión (trazabilidad CAPA); +1 fusión posterior (par mentoría, ver hallazgos) → 311 env |
| 2b · Cosmético | 8 keepers renombrados a su base sin sufijo (ej. `trilogia_de_juran_2` → `trilogia_de_juran`) |
| 3 · Reparación | 26 reparadas por cadena/alias/fuzzy; 254 podadas (5.1%/8.1%/8.0% — escalado al usuario por superar el umbral del 3%) |
| 3b · Re-match semántico | 191 fantasmas únicos → **86 auto** (≥0.70) + **78 por revisión de significado** (banda 0.55–0.70; ~24 con destino corregido fuera del top-3 del embedding) + **27 poda definitiva**. Recuperación: 86% |
| 4 · Simetría | 632 nodos completados; estado: 0 rotas / 0 asimétricas |
| 5 · Semillas + títulos | 7 semillas aprobadas por el usuario por dominio; 39 grupos de título duplicado diferenciados por contenido (84 títulos); par mentoría fusionado |
| 6 · Puentes | 20 propuestas core↔dominio por dominio (embeddings), **solo propuesta** en `metadata/bridges_propuestos.json`, cero escritura al master |
| 7 · Alcanzabilidad | 147 aristas de conexión (28/32/87), una por cluster-fuente de huérfanos (condensación SCC), cada una registrada con padre/hijo/score (min 0.44, medio 0.65–0.71, max 0.97) |

## Semillas aprobadas (decisión de producto del usuario)

- **environmental**: `eco_efectividad`, `auditoria_energetica_sistematica`,
  `programa_reciclaje_integral`, `cinco_pasos_eco_efectividad`,
  `metricas_impacto_ambiental`, `sistema_gestion_ambiental`,
  `codigo_conducta_proveedores`
- **health_safety**: `cultura_justa`, `identificacion_evaluacion_peligros`,
  `participacion_trabajadores`, `prevencion_control_peligros`,
  `evaluacion_mejora_programa`, `fallas_activas_condiciones_latentes`,
  `identificacion_peligros_salud` (swap del usuario: entra higiene
  ocupacional, sale la segunda puerta de cultura)
- **quality**: `accion_correctiva`, `mejora_continua_del_proceso`,
  `programa_mejora_calidad_14_pasos`, `control_estadistico_de_procesos`,
  `costo_de_calidad`, `trilogia_de_juran`, `medicion_calidad`

## Puentes propuestos (selección humana pendiente de 10-15; NO escritos)

Top 5 por dominio (lista completa de 20 en cada
`packs/<dominio>/metadata/bridges_propuestos.json`):

**environmental** — `validar_posicionamiento_con_analistas↔voces_externas_credibles` (0.853),
`metodo_valor_presente_neto↔monetizacion_npv_caso_negocio` (0.841),
`calidad_de_ejecucion_proceso_innovacion↔optimizacion_almacenes_distribucion` (0.834),
`…↔implementar_estrategias_reduccion_emisiones` (0.829),
`…↔establecimiento_metas_publicas` (0.829)

**health_safety** — `calidad_de_ejecucion_proceso_innovacion↔racional_mantenimiento_preventivo_correctivo` (0.830),
`diseno_imperfeccion_intencional↔confusion_de_modos_automatizacion` (0.822),
`diseno_imperfeccion_intencional↔cultura_narrativas_variedad_requerida` (0.820),
`calidad_de_ejecucion_proceso_innovacion↔evaluacion_mejora_programa_2` (0.810),
`second_wind_energia_mental↔fatigue_performance_effects` (0.798)

**quality** — `brainstorming_efectivo↔brainstorming` (0.885),
`data_integrity_forecasting↔criterios_seleccion_proyectos_calidad` (0.870),
`calidad_de_ejecucion_proceso_innovacion↔mejora_continua_del_proceso` (0.857),
`pruning_portafolio↔roi_proyectos_calidad` (0.855),
`metas_objetivos_smart_innovacion↔definir_metas_smart_de_proyecto` (0.855)

Nota de lectura: `calidad_de_ejecucion_proceso_innovacion` aparece como
polo core de 12 de los 60 puentes — nodo-puente natural o embedding
demasiado genérico; juzgar par por par en la selección humana.

## Hallazgos de auditoría cruzada resueltos en el camino

1. **Bug en los scripts del auditor (encontrado antes de correr nada):**
   los 7 scripts leían `node["titulo"]`, pero todo nodo (core y packs)
   usa `titulo_concepto`. Sin el fix, paso 0 habría marcado los 1557
   nodos como sin título y el dedup habría agrupado todo bajo un solo
   título vacío. 12 ocurrencias corregidas en 4 scripts.
2. **39 grupos de título duplicado** (hallazgo del auditor, confirmado
   exacto): resueltos por diferenciación leída del contenido — paréntesis
   sectorial para los gemelos OSHA3885/3886 (industria general vs
   construcción), énfasis de contenido para el resto. Jamás fusión.
3. **Par mentoría** (hallazgo del auditor con premisa corregida): los
   títulos NO estaban vacíos, pero el instinto era correcto — la lectura
   de contenido confirmó duplicado genuino (misma fuente, mismo staircase
   model de IKEA) que la revisión de dedup había rechazado por score sin
   lectura cercana. El texto dijo fusión: fusionado con mecánica completa
   y nota de reversión en `dedup_decisiones.json`.

## Lecciones del corpus (para el registro del proyecto)

1. **La similitud de título es señal poco confiable en corpus
   mono-disciplina.** El core (13 libros de disciplinas distintas) casi
   no tenía choques de título entre conceptos diferentes; estos packs
   (2-5 libros de LA MISMA disciplina) chocan de nombre constantemente
   entre conceptos legítimamente distintos (5 nodos "Acción Correctiva"
   con similitud de contenido 0.005–0.104: Crosby-definición,
   Crosby-paso-6 y Juran-esporádico-vs-crónico). Toda decisión de
   dedup/diferenciación se tomó leyendo `resumen_teorico` y
   `pasos_accionables`, nunca por nombre.
2. **Lección de pipeline (pendiente de implementar):**
   `pipeline_dominio.py` necesita, para cualquier libro futuro, un diseño
   de DOS pasadas — pasada 1 extrae todos los nodos del libro; pasada 2
   teje aristas viendo el catálogo real de ids ya extraídos. El core
   nació con ~25% de referencias rotas por esta ceguera (generación por
   chunks sin estado); estos dominios nacieron con ~8% porque el modelo
   mejoró, pero la cura estructural es la segunda pasada, no un modelo
   más listo.
3. **El re-match semántico recuperó 86% de los fantasmas** — muy por
   encima del 25-50% estimado, porque el corpus mono-disciplina SÍ
   contenía la mayoría de los conceptos troncales bajo otro nombre (el
   mismo fenómeno que hizo poco confiable el título en dedup, jugando a
   favor). El top-3 del embedding también falló varias veces (ej.
   `medicion_impacto_ambiental` no listó a `metricas_impacto_ambiental`);
   ~24 aprobaciones fueron overrides por búsqueda dirigida + lectura.
4. **Candidatos a fusión futura, con datos:** varios pares diferenciados
   en el checkpoint 5 son solape de chunk del mismo libro con ángulos
   delgados (ej. `defensas_en_profundidad`/_2, los pares lockout y
   superficies elevadas de SMALL_BUSINESS, `falta_de_constancia_de_
   proposito`/_2). Se diferenciaron por instrucción explícita (jamás
   fusión mecánica); cuando estos dominios tengan tráfico real, la lista
   de nodos-jamás-tocados de la caja de vidrio dirá con evidencia si
   merecen fusión.

## Trazabilidad

Toda decisión quedó en `packs/<dominio>/metadata/`:
`ascii_renombrados.json`, `dedup_candidatos.json`, `dedup_decisiones.json`
(commiteado antes de la fusión), `renombres_cosmeticos.json`,
`aristas_reparadas.json`, `aristas_resemantizadas.json` (191 fantasmas
con candidatos, scores, banda y veredicto), `titulos_diferenciados.json`,
`entry_seeds.json`, `bridges_propuestos.json`,
`aristas_conexion_gate0.json` (147 aristas una a una).
