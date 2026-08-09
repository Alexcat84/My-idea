# Cola de pares nucleo-mundo para leer

**ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** El veredicto de cada par es **lectura textual** del auditor con visto del fundador. **Un par en esta lista es una cita para leer, no una violacion.**

La vara esta en `docs/GRADIENTE_NUCLEO_MUNDO.md`: el nucleo es suficiente, el mundo es exponencial respecto de esa base, y una violacion **jamas** se arregla empobreciendo el nucleo.

Los conteos de pasos que aparecen en la salida **solo ordenan la cola**. La profundidad se adjudica leyendo `pasos_accionables` y `entregable_esperado`, jamas contando.

## Como se emparejo

Dos senales independientes, y basta con que dispare **cualquiera**:

- **titulo**: `token_sort_ratio` de rapidfuzz, umbral **80**
- **semantica**: coseno sobre `semantic_index.json`, umbral **0.75**

Cada par reporta **las dos**, aunque solo una haya disparado.

## La calibracion conocida

**CAZADO.** El par `plan_gestion_calidad` (nucleo) contra `sistema_gestion_calidad` (quality) esta en la cola: similitud de titulo **83.6**, semantica **0.7797** (disparo por titulo: True, por semantica: True).

## Conteos

**346 pares** en la cola, sobre 1618 nodos de nucleo y 1903 de mundo.

| mundo | pares |
|---|---:|
| quality | 174 |
| risk_management | 44 |
| franquicias | 37 |
| compras | 36 |
| environmental | 20 |
| exportacion | 17 |
| entrega | 9 |
| health_safety | 6 |
| seguridad_digital | 3 |

## Distribucion de la similitud semantica

Sobre **3079054** comparaciones mundo-contra-nucleo:

| percentil | coseno |
|---|---:|
| p50 | 0.3965 |
| p75 | 0.4541 |
| p90 | 0.5083 |
| p95 | 0.5417 |
| p99 | 0.6070 |
| p99.9 | 0.6859 |
| maximo | 0.8936 |

Media 0.3991. **Por encima del umbral 0.75: 342 comparaciones.**

**Lectura de esta distribucion para calibrar**: el umbral 0.75 esta muy por encima del p99.9 (0.6859), asi que la senal semantica solo caza la cola extrema. Es deliberadamente selectiva: la cola es para LEER, y una cola de miles de pares no se lee. Si el auditor quiere mas cobertura, bajar a 0.70 o 0.65 la ensancha; el instrumento acepta `--umbral-semantico`.

## Los veinte pares de similitud mas alta del catalogo entero

Ordenados por la senal MAS FUERTE de las dos, normalizando el titulo a 0-1. Por eso hay filas con semantica baja y titulo alto: entraron por el titulo, y se ven las dos columnas para que quede claro por cual.

| # | mundo | nodo del mundo | nodo del nucleo | titulo | semantica | pasos M/N |
|---:|---|---|---|---|---:|---:|
| 1 | quality | `evaluacion_de_factores_de_riesgo` | `matriz_probabilidad_impacto` | 43.0 | 0.8936 | 4/5 |
| 2 | risk_management | `cuan_probable_y_cuanto_doleria` | `matriz_probabilidad_impacto` | 25.8 | 0.8934 | 4/5 |
| 3 | seguridad_digital | `getting_started_supply_chain_risk_management` | `supply_chain_management_systems` | 88.0 | 0.7319 | 6/4 |
| 4 | risk_management | `manten_viva_tu_lista_de_riesgos` | `registro_de_riesgos` | 62.3 | 0.8736 | 4/6 |
| 5 | franquicias | `manejo_objeciones_venta_franquicia` | `prevencion_objeciones_vs_manejo` | 48.8 | 0.8726 | 4/6 |
| 6 | environmental | `biomimicry_diseno` | `biomimicry_conexiones_naturales` | 49.5 | 0.8647 | 4/4 |
| 7 | risk_management | `haz_tu_lista_de_lo_que_puede_fallar` | `registro_de_riesgos` | 73.7 | 0.864 | 4/6 |
| 8 | environmental | `cradle_to_cradle_concepto` | `diseno_para_sostenibilidad_cradle_to_cradle` | 58.9 | 0.8606 | 4/4 |
| 9 | quality | `constraint_management` | `teoria_de_restricciones` | 65.3 | 0.8562 | 5/3 |
| 10 | quality | `constraint_management` | `cinco_pasos_enfoque_restricciones` | 56.9 | 0.8533 | 5/5 |
| 11 | risk_management | `guarda_lo_que_aprendiste_de_cada_golpe` | `captura_conocimiento_mercado` | 85.3 | 0.4096 | 4/7 |
| 12 | environmental | `desperdicio_es_alimento` | `diseno_para_sostenibilidad_cradle_to_cradle` | 38.5 | 0.8493 | 6/4 |
| 13 | quality | `brainstorming` | `brainstorming_divergente` | 50.0 | 0.8482 | 7/8 |
| 14 | seguridad_digital | `getting_started_risk_assessment` | `resource_assessment` | 84.3 | 0.6022 | 7/5 |
| 15 | quality | `sistema_medicion_kpi` | `medicion_monitoreo_desempeno` | 48.4 | 0.8406 | 6/5 |
| 16 | quality | `auditoria_calidad` | `quality_audit` | 54.8 | 0.8405 | 4/4 |
| 17 | risk_management | `evalua_la_gravedad_sin_autoengano` | `matriz_probabilidad_impacto` | 29.6 | 0.8394 | 4/5 |
| 18 | quality | `brainstorming` | `brainstorming_efectivo` | 51.4 | 0.8391 | 7/4 |
| 19 | risk_management | `revisa_tus_riesgos_con_un_ritmo` | `registro_de_riesgos` | 49.1 | 0.837 | 4/6 |
| 20 | quality | `sistema_gestion_calidad` | `plan_gestion_calidad` | 83.6 | 0.7797 | 4/5 |

La cola completa, con los titulos de los dos lados, en `GRADIENTE_PARES.jsonl`.
