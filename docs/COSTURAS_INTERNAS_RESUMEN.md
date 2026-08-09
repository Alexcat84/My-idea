# Costuras internas: nodos con texto repetido DENTRO de si mismos

**ESTE INSTRUMENTO CITA, NO JUZGA.** Hermano chico de `scripts/gradiente_pares.py`. **Un nodo en esta lista es una cita para leer, no una costura probada.** El veredicto es **lectura textual** del auditor con visto del fundador.

La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos` (puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97). **No son duplicados entre nodos: son un solo nodo al que le sobran pasos.**

## Las dos señales

| señal | que caza | umbral |
|---|---|---:|
| **pareja de pasos** | el paso repetido casi literal (`token_sort_ratio`) | **80** |
| **alineacion de bloques** | la secuencia que vuelve a empezar, y **donde** | **45** |

**Basta con que dispare cualquiera, y se reportan las dos siempre**, como en el hermano mayor: el auditor necesita ver por que entro cada nodo.

### Por que hacen falta las dos, medido

**Con la señal de pareja sola, y en cualquier umbral, la calibracion no entra.** La mejor pareja interna de `plan_mejora_procesos` es **60.0** y la de `economia_circular` **54.7**; bajar el umbral hasta ahi caza **856 nodos, el 24 por ciento del catalogo**.

> **Una baranda que caza lo correcto no es estricta, esta rota.**

El motivo es que esas dos costuras son **parafrasis con cola distinta**, no copias. La señal de bloques las pone en los **puestos 7 y 32 de 567** y **acierta el corte exacto en las dos**.

## La calibracion conocida

**CAZADO** `plan_mejora_procesos`: pareja **60.0**, bloque **56.7** con el corte **tras el paso 10**.

**CAZADO** `economia_circular_como_modelo_de_negocio`: pareja **54.7**, bloque **49.7** con el corte **tras el paso 5**.

## Conteos

**110 nodos** en la cola, sobre 3521 activos.

| dominio | nodos |
|---|---:|
| core | 66 |
| quality | 24 |
| exportacion | 6 |
| seguridad_digital | 5 |
| health_safety | 4 |
| franquicias | 3 |
| environmental | 2 |

## Distribucion, para calibrar

| percentil | mejor pareja interna | alineacion de bloques |
|---|---:|---:|
| p50 | 50.5 | 45.9 |
| p90 | 57.6 | 50.3 |
| p99 | 66.6 | 76.1 |
| maximo | 92.8 | 80.2 |

Nodos evaluados por bloques (6 pasos o mas): **173**.

## Los veinte primeros

| # | dominio | nodo | pasos | pareja | bloque | corte | entro por |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | core | `coeficiente_viral` | 16 | 92.8 | 74.7 | 11 | pareja y bloque |
| 2 | core | `viral_loop_marketing` | 30 | 89.9 | 65.9 | 17 | pareja y bloque |
| 3 | quality | `diseno_de_procesos_por_caracteristicas` | 5 | 86.6 | 0.0 |  | pareja |
| 4 | core | `ratios_eficiencia_inventario` | 8 | 85.1 | 48.3 | 4 | pareja y bloque |
| 5 | core | `producto_minimo_viable` | 22 | 85.0 | 80.2 | 18 | pareja y bloque |
| 6 | quality | `tipos_innovacion_i_ii` | 6 | 84.1 | 0.0 |  | pareja |
| 7 | core | `dso_dpo_gestion_capital_trabajo` | 4 | 81.5 | 0.0 |  | pareja |
| 8 | quality | `control_estadistico_metodo_medicion` | 6 | 80.9 | 0.0 |  | pareja |
| 9 | core | `decision_de_vender_startup` | 34 | 79.2 | 69.3 | 30 | bloque |
| 10 | core | `transicion_producto_a_experiencia` | 12 | 71.0 | 60.1 | 7 | bloque |
| 11 | core | `lienzo_modelo_negocio` | 17 | 66.0 | 59.2 | 13 | bloque |
| 12 | core | `cultura_de_experiencia` | 12 | 65.8 | 50.2 | 5 | bloque |
| 13 | quality | `estratificacion_datos` | 7 | 63.6 | 48.2 | 4 | bloque |
| 14 | quality | `viaje_diagnostico_remedial` | 8 | 63.5 | 46.7 | 4 | bloque |
| 15 | quality | `planificacion_recoleccion_datos` | 16 | 63.4 | 52.3 | 11 | bloque |
| 16 | core | `gestion_libro_abierto_obm` | 10 | 63.2 | 45.1 | 4 | bloque |
| 17 | seguridad_digital | `csf_funcion_govern` | 7 | 62.0 | 48.5 | 3 | bloque |
| 18 | core | `analisis_tco_roi_b2b` | 9 | 61.9 | 48.9 | 6 | bloque |
| 19 | core | `plan_gestion_riesgos` | 6 | 61.9 | 50.3 | 3 | bloque |
| 20 | core | `wizard_of_oz_testing` | 6 | 61.4 | 47.4 | 3 | bloque |

La cola completa, con los dos pasos de cada pareja, en `COSTURAS_INTERNAS.jsonl`.
