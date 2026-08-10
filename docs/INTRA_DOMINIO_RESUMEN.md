# Cola intra-dominio: pares del mismo dominio para leer

**ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** El veredicto de cada par es **lectura textual** del auditor con visto del fundador. **Un par en esta lista es una cita para leer, no un duplicado.**

Es el otro eje del mismo trabajo: `scripts/gradiente_pares.py` empareja **mundo contra nucleo**, y este empareja **cada dominio contra si mismo**, que es donde viven los racimos. Los conteos de pasos **solo ordenan la cola**; la profundidad y la duplicacion se adjudican leyendo, jamas contando.

## Como se emparejo

Dos senales independientes, y basta con que dispare **cualquiera**:

- **titulo**: `token_sort_ratio` de rapidfuzz, umbral **80**
- **semantica**: coseno sobre `semantic_index.json`, umbral **0.8**

Cada par reporta **las dos**, aunque solo una haya disparado.

**El umbral semantico es 0.8 y no el 0,75 del gradiente a proposito.** Dentro de un dominio la vecindad tematica es **la norma, no la senal**: dos nodos de `quality` hablan de calidad por definicion. La distribucion por dominio esta mas abajo **para que el umbral se pueda recalibrar con datos antes de leer**, no despues.

## La calibracion conocida

**CAZADO.** El par `descubrir_necesidades_cliente` contra `descubrir_necesidades_del_cliente` (los dos en `quality`) esta en la cola: similitud de titulo **87.8**, semantica **0.8102** (disparo por titulo: True, por semantica: True).

## Conteos

**2063 pares** en la cola, sobre **3521 nodos activos** repartidos en **10 dominios**.

| dominio | nodos | pares posibles | en la cola | % de los posibles |
|---|---:|---:|---:|---:|
| compras | 46 | 1035 | **104** | 10.05% |
| core | 1618 | 1308153 | **881** | 0.07% |
| entrega | 47 | 1081 | **127** | 11.75% |
| environmental | 289 | 41616 | **103** | 0.25% |
| exportacion | 141 | 9870 | **87** | 0.88% |
| franquicias | 195 | 18915 | **81** | 0.43% |
| health_safety | 283 | 39903 | **108** | 0.27% |
| quality | 792 | 313236 | **497** | 0.16% |
| risk_management | 55 | 1485 | **56** | 3.77% |
| seguridad_digital | 55 | 1485 | **19** | 1.28% |

## Nuevos contra re-avistados

**El instrumento conoce el trabajo hecho.** Nada se excluye por estar ya visto: se MARCA, con su fuente, y la cola dice que es nuevo y que no.

| estado | pares | que significa |
|---|---:|---|
| **nuevo** | **1910** | ni el par ni sus dos nodos aparecen en lo ya escrito |
| nodo ya avistado | 108 | alguno de los dos nodos ya fue leido en otro par; **el par en si es nuevo** |
| re-avistado | 45 | **el par exacto** ya esta adjudicado o censado |

Fuentes de las marcas, con lo que aporto cada una:

| fuente | entradas |
|---|---:|
| `informe_4_4_ids_casi_identicos` | 19 |
| `informe_4_3_base_mas_2` | 9 |
| `informe_4_2_crosby_duplicados` | 7 |
| `ficha_36_parejas_de_sufijo` | 36 |
| `ficha_citas_intra_dominio_nodos` | 67 |

> **HUECO DECLARADO, y es de cobertura de las marcas, no de la cola.** De los **32 racimos** de `docs/MESA_RACIMOS.md`, **solo dos tienen la lista de miembros escrita** (los puntos de Deming y los cinturones, los dos destapados por la muestra D). Los **30 del censo del cribado** estan registrados **con nombre y tamano pero sin ids de sus miembros** en ningun documento, asi que el instrumento **no puede marcarlos** y no se los inventa. **La consecuencia practica: la columna de re-avistados esta SUBESTIMADA**, y un par marcado como nuevo puede ser miembro de un racimo ya censado. Se cierra escribiendo los miembros de esos 30 racimos, no tocando este instrumento.

## Recall contra lo declarado, que es el dato duro de calibracion

**Las parejas ya escritas en los documentos son la unica verdad conocida que existe para este eje.** Si el instrumento no las caza, la cola tiene agujeros, y eso hay que saberlo ANTES de leerla, no despues.

| | |
|---|---:|
| parejas declaradas que son **intra-dominio** | **60** |
| de esas, **cazadas** por la cola | **45** |
| **perdidas** | **15** |
| **recall** | **75%** |

(2 parejas declaradas mas **cruzan dominio** y por definicion no le tocan a este instrumento: `proteccion_propiedad_intelectual` con `proteccion_propiedad_intelectual_2`, `seleccion_canal_distribucion` con `seleccion_canales_distribucion`.)

**Las 15 perdidas, con sus dos senales**, para que se vea cuanto falta y no cuanto se cree que falta:

| dominio | pareja | titulo | semantica | de donde viene la marca |
|---|---|---:|---:|---|
| environmental | `triple_bottom_line` con `triple_bottom_line_2` | 40.4 | 0.7961 | informe 4.3 base mas _2 calcados; ficha, las 36 parejas de sufijo vivo |
| quality | `accion_correctiva_4` con `accion_correctiva_sistematica` | 67.6 | 0.789 | informe 4.2 pasos duplicados de Crosby |
| franquicias | `cadencia_seguimiento_prospectos` con `gestion_seguimiento_prospectos` | 41.7 | 0.7887 | informe 4.4 ids casi identicos |
| quality | `design_for_six_sigma_dmadv` con `design_for_six_sigma_dmadv_2` | 61.1 | 0.7795 | ficha, las 36 parejas de sufijo vivo |
| franquicias | `velocidad_crecimiento_franquicia` con `velocidad_crecimiento_franquicia_2` | 43.9 | 0.7783 | ficha, las 36 parejas de sufijo vivo |
| quality | `programa_make_certain` con `programa_make_certain_2` | 47.5 | 0.7679 | ficha, las 36 parejas de sufijo vivo |
| quality | `definiciones_operacionales` con `definiciones_operacionales_3` | 61.0 | 0.7592 | ficha, las 36 parejas de sufijo vivo |
| quality | `validacion_sistema_medicion` con `validacion_sistema_medicion_2` | 65.0 | 0.756 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `cultura_justa` con `cultura_justa_3` | 50.6 | 0.7365 | ficha, las 36 parejas de sufijo vivo |
| quality | `desarrollar_caracteristicas_proceso` con `desarrollar_caracteristicas_proceso_2` | 44.0 | 0.7365 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `defensas_en_profundidad` con `defensas_en_profundidad_3` | 61.0 | 0.7335 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `cultura_justa` con `cultura_justa_2` | 40.4 | 0.7169 | ficha, las 36 parejas de sufijo vivo |
| quality | `definiciones_operacionales` con `definiciones_operacionales_4` | 42.1 | 0.7087 | ficha, las 36 parejas de sufijo vivo |
| environmental | `responsabilidad_extendida_productor` con `responsabilidad_extendida_productor_2` | 44.2 | 0.6268 | ficha, las 36 parejas de sufijo vivo |
| quality | `planificacion_estrategica_despliegue` con `planificacion_estrategica_despliegue_2` | 39.2 | 0.615 | informe 4.3 base mas _2 calcados; ficha, las 36 parejas de sufijo vivo |

**Lo que estas perdidas dicen, y es lo mas util de este resumen:**

- **La familia de ids no la cazan estas dos senales.** Casi todas las perdidas son parejas de **sufijo `_N`**: se llaman parecido pero no lo bastante para el umbral de titulo, y hablan de lo mismo pero por debajo del umbral semantico. **Su detector no es este: es la regla del sufijo**, que este mismo instrumento ya computa y publica arriba con sus 36 parejas.
- **Bajar el umbral no las rescata gratis.** La perdida mas alta esta en **0.7961** de semantica; bajar el corte hasta ahi ensancharia la cola en todos los dominios a la vez. La distribucion de abajo dice cuanto.
- **Hay perdidas que NO son de sufijo, y esas si duelen**: `accion_correctiva_4` con `accion_correctiva_sistematica`, `cadencia_seguimiento_prospectos` con `gestion_seguimiento_prospectos`. **Son parejas ya adjudicadas que estas dos senales no ven**, y son el argumento para no leer esta cola como si fuera exhaustiva.

## Distribucion de la similitud semantica, por dominio

**Esta es la tabla para recalibrar el umbral antes de leer.** Si un dominio tiene el p99 por encima del umbral, ese dominio va a inundar la cola de vecinos legitimos y conviene subirle el corte.

| dominio | comparaciones | media | p50 | p90 | p99 | p99.9 | maximo | sobre el umbral |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| compras | 1035 | 0.6732 | 0.6739 | 0.8000 | 0.8646 | 0.8868 | 0.8877 | 104 |
| core | 1308153 | 0.4381 | 0.4323 | 0.5614 | 0.6845 | 0.7842 | 0.9334 | 871 |
| entrega | 1081 | 0.6711 | 0.6630 | 0.8073 | 0.8839 | 0.9089 | 0.9283 | 127 |
| environmental | 41616 | 0.5253 | 0.5236 | 0.6405 | 0.7464 | 0.8294 | 0.9022 | 102 |
| exportacion | 9870 | 0.5623 | 0.5571 | 0.6759 | 0.7936 | 0.8724 | 0.9432 | 87 |
| franquicias | 18915 | 0.5870 | 0.5917 | 0.6898 | 0.7717 | 0.8709 | 0.9309 | 80 |
| health_safety | 39903 | 0.5210 | 0.5205 | 0.6443 | 0.7504 | 0.8295 | 0.9058 | 106 |
| quality | 313236 | 0.5071 | 0.5059 | 0.6253 | 0.7294 | 0.8174 | 0.9629 | 488 |
| risk_management | 1485 | 0.6756 | 0.6829 | 0.7684 | 0.8353 | 0.8843 | 0.9042 | 56 |
| seguridad_digital | 1485 | 0.6052 | 0.6057 | 0.7125 | 0.8096 | 0.8840 | 0.9136 | 18 |

## Los treinta pares de similitud mas alta

Ordenados por la senal MAS FUERTE de las dos, normalizando el titulo a 0 a 1. Por eso hay filas con semantica baja y titulo alto: entraron por el titulo.

| # | dominio | nodo a | nodo b | titulo | semantica | pasos a/b | estado |
|---:|---|---|---|---:|---:|---:|---|
| 1 | quality | `capacidad_de_proceso` | `capacidad_del_proceso` | 97.6 | 0.7876 | 4/4 | nuevo |
| 2 | quality | `control_estadistico_de_procesos` | `control_estadistico_del_proceso` | 97.3 | 0.8809 | 10/4 | nuevo |
| 3 | exportacion | `carta_de_credito_letter_of_credit` | `letters_of_credit` | 97.2 | 0.8993 | 5/6 | nuevo |
| 4 | quality | `programa_de_mejora_de_calidad` | `programa_mejora_calidad_14_pasos` | 69.7 | 0.9629 | 6/7 | nuevo |
| 5 | quality | `planificacion_de_la_inspeccion` | `planificacion_inspeccion` | 94.7 | 0.8749 | 5/4 | re-avistado |
| 6 | exportacion | `export_administration_regulations` | `regulaciones_exportacion_ear` | 64.5 | 0.9432 | 6/4 | nuevo |
| 7 | core | `customer_discovery_cuatro_fases` | `customer_discovery_overview` | 80.7 | 0.9334 | 4/4 | nuevo |
| 8 | core | `cumplimiento_magnuson_moss` | `regla_disponibilidad_previa_venta` | 31.7 | 0.9324 | 4/3 | nuevo |
| 9 | franquicias | `gestion_terminacion_franquiciado` | `terminacion_franquiciado_causas` | 57.1 | 0.9309 | 5/4 | nuevo |
| 10 | quality | `eliminacion_causas_error` | `eliminacion_causas_error_2` | 93.0 | 0.8119 | 4/6 | re-avistado |
| 11 | entrega | `calcular_peso_dimensional_antes_cotizar` | `medir_paquete_redondeando_hacia_arriba` | 37.2 | 0.9283 | 5/5 | nuevo |
| 12 | core | `contratos_de_servicio_garantia` | `diferenciacion_garantia_contrato_servicio` | 48.7 | 0.9258 | 3/4 | nuevo |
| 13 | exportacion | `export_administration_regulations` | `licencia_exportacion_regulaciones` | 38.9 | 0.9231 | 6/6 | nuevo |
| 14 | quality | `mantener_las_ganancias` | `sostener_las_ganancias` | 92.3 | 0.8886 | 5/5 | re-avistado |
| 15 | core | `clasificacion_garantia_full_limited` | `cumplimiento_magnuson_moss` | 35.9 | 0.9179 | 4/4 | nuevo |
| 16 | core | `gestion_sindicato_inversores` | `manejo_syndicate_inversion` | 58.4 | 0.9174 | 4/4 | nuevo |
| 17 | core | `asignacion_agil_de_recursos` | `presupuesto_agil_innovacion` | 40.7 | 0.916 | 4/4 | nuevo |
| 18 | core | `cumplimiento_magnuson_moss` | `evitar_terminos_enganosos_garantia` | 35.7 | 0.9154 | 4/3 | nuevo |
| 19 | core | `producto_unico_superior` | `ventaja_competitiva_producto` | 36.5 | 0.9143 | 8/4 | nuevo |
| 20 | seguridad_digital | `csf_funcion_recover` | `funcion_recover_restauracion` | 59.3 | 0.9136 | 6/4 | nuevo |
| 21 | quality | `accion_correctiva_5` | `accion_correctiva_6` | 45.4 | 0.9127 | 6/4 | nuevo |
| 22 | core | `cumplimiento_magnuson_moss` | `regla_divulgacion_garantia` | 34.0 | 0.9124 | 4/3 | nuevo |
| 23 | quality | `desarrollar_controles_transferir_operaciones` | `desarrollo_de_controles_de_proceso` | 91.1 | 0.8442 | 5/6 | nuevo |
| 24 | franquicias | `deteccion_franquicia_inadvertida` | `prevenir_franquicias_inadvertidas` | 37.4 | 0.9099 | 4/4 | nuevo |
| 25 | entrega | `calcular_peso_dimensional_antes_cotizar` | `conocer_limites_peso_tamano_courier` | 47.3 | 0.9091 | 5/5 | nuevo |
| 26 | core | `seleccion_canal_distribucion` | `seleccion_canal_fisico` | 90.7 | 0.7111 | 5/4 | nuevo |
| 27 | quality | `innovacion_tipo_ii` | `tipos_innovacion_i_ii` | 51.5 | 0.9069 | 5/6 | nodo ya avistado |
| 28 | entrega | `acolchado_segun_forma` | `adaptar_empaque_segun_tipo_de_articulo` | 50.0 | 0.9068 | 5/5 | nuevo |
| 29 | quality | `relacion_largo_plazo_proveedor_unico` | `relaciones_largo_plazo_con_proveedores` | 46.3 | 0.9063 | 4/4 | re-avistado |
| 30 | quality | `sistema_responsabilidad_gerencial` | `sistema_responsabilidad_gerencial_2` | 90.6 | 0.8677 | 5/5 | re-avistado |

La cola completa, con los titulos de los dos lados y las marcas de procedencia, en `INTRA_DOMINIO_PARES.jsonl`.

## Que hacer con el tamano de esta cola

**Si la cola sale grande, no es un fallo del instrumento: es el tamano del problema.** El paso de lectura lo deciden el auditor y el fundador, como se hizo con la franja bajo el umbral. Las palancas, en orden de menor a mayor perdida de cobertura: **subir el umbral semantico** (la distribucion de arriba dice cuanto), **leer por dominio** en vez de por cola global, y **ordenar por senal** dejando la cola larga para tandas posteriores. **Lo que no se puede hacer es podarla en silencio**: si se corta, se escribe donde se corto y cuanto quedo sin mirar.
