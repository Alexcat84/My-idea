# Acta de integración del mundo 11, Primer Equipo (`primer_equipo`)

**Estado:** integrado en el catálogo y **OCULTO** (`"oculto": true` en `web/lib/assets/packs_catalog.json`) hasta el
visto del fundador. Rama de trabajo `puente-forja`, fundida en main con el requisito del fundador del 28 sep 2026
(todo en main antes de la auditoría final y de su recorrido).

Los libros se nombran por su clave de la forja. Los títulos completos viven solo en lo interno (`fuente` de cada nodo,
`dataset/metadata/fuentes_canonicas.json`, `docs/internos/INVENTARIO_FUENTES.md`). Las cifras llevan su commit o su
fichero; `PF` es `docs/PUENTE_FORJA.md` y `RM` es `docs/saneamiento/resultados/M11/README.md`.

## 1. Censo por libro

471 nodos extraídos (`docs/puente_forja/fases_mundo11.jsonl`), 465 integrados (`dataset/nodos`, dominio
`primer_equipo`, ninguno deprecado) y 6 aparcados en la forja.

| Libro (clave de la forja) | Extraídos | Integrados | Aparcado |
|---|---|---|---|
| `scott_radical_candor` | 142 | 141 | `manejar_contacto_fisico_regla_platino` |
| `zhuo_manager` | 136 | 135 | `aprovechar_formacion_reglada` |
| `grove_high_output` | 92 | 91 | `diagnosticar_nivel_motivacion_reaccion_aumento_salario` |
| `smart_who` | 59 | 58 | `distinguir_perfil_guepardo_cordero` |
| `gerber_emyth` | 22 | 21 | `responder_4_preguntas_estandares_objetivo_estrategico` |
| `marquet_turn_the_ship` | 20 | 19 | `acoger_inspectores_externos_fuente_aprendizaje` |
| **Total** | **471** | **465** | **6** |

- `gestion_negocio` (`gerber_emyth`, 22) y `produccion` (`grove_high_output`, 22) pasaron a `primer_equipo`
  (d1e38511). Seis nodos de la forja fueron al mundo 10 y dos son de la propia forja (PF:333).
- **Fases de los 465:** ejecución 266, planificación 148, validación 38, ideación 13.
- **Aparcados:** `docs/puente_forja/aparcados_mundo11.json`, con la ficha `m11-aparcados-reextraccion`
  (`docs/PENDIENTES.md`). Cinco quedaron aislados, sin una arista real. El sexto no es una puerta legítima.

## 2. Certificación del contenido (paso 3)

**Umbral del fundador, fijado antes de medir:** en la muestra ciega final, 0 invenciones y 0 contrarios; matices
perdidos, calcos y coherencia, como mucho 1 por cada 5 nodos. Todas las trampas van sin marca y bajo ids reales.

| Tanda o muestra | Commit | Semilla | Trampas | Resultado |
|---|---|---|---|---|
| `m11-limpieza` | 9b25fdc2 | | con nombre visible (fallo de método declarado, RM:22-24) | 5.452 correcciones en 471 nodos; guarda de voz de 2.651 faltas a 0 |
| `m11-glosario` | 9b25fdc2 | | | 130 en 80 nodos |
| `m11-limites` | 9b25fdc2 | | 1 de 1 | 21 en 19 nodos |
| Primera muestra ciega | 9b25fdc2 | 20261004 | 3 de 3 | 57 defectos en 19 de 25 nodos: auditoría completa |
| `m11-auditoria` | c02ea2ec | 20261005 | 24 de 24 | 952 marcados; 842 campos corregidos en 372 nodos |
| `m11-barrido` | c02ea2ec | | 1 de 1 | 37 en 25 nodos |
| Muestra final 1 | 29cda13f | 20261006 | 4 de 4 | 0 duros, 23 blandos: NO CUMPLE (23 en 15 nodos) |
| `m11-pase2` | 29cda13f | 20261008 | 26 de 28 (2 de matiz escapan, declarado) | 673 en 335 nodos |
| `m11-salida` | 29cda13f | | 1 de 1 | 15 en 3 nodos |
| Muestra final 2 | 6ad26049 | 20261009 | 3 de 4 | 0 duros, 11 blandos: NO CUMPLE (11 en 8 nodos) |
| `m11-pase3` | 6ad26049 | 20261011 | 33 de 38 | 186 en 141 nodos |
| Muestra final 3 | 6ad26049 | 20261012 | 4 de 4 | 0 duros, 11 blandos: NO CUMPLE (11 en 5 nodos) |
| `m11-pase4` y su barrido | 090c4f3f | 20261013 | 22 de 23 y 1 de 1 | 355 en 172 nodos y 10 en 7 |
| Muestra final 4 | 090c4f3f | 20261014 | 4 de 4 | 1 invención, 5 blandos: NO CUMPLE (4 en 4 nodos) |
| `m11-pase5` | fe6955a3 | 20261016 | 25 de 26 (fallo de método declarado) | 2.356 cláusulas cotejadas; 32 en 27 nodos |
| Muestra final 5 | fe6955a3 | 20261017 | 3 de 4 | 1 contrario, 7 blandos: NO CUMPLE (8 en 7 nodos) |
| `m11-pase6`, doble lectura | 6af06a64 | 20261018 | 47 de 47, 0 fugas | 35 en 30 nodos |
| **Muestra final 6** | **6af06a64** | **20261019** | **4 de 4** | **0 duros, 2 blandos de 10: CUMPLE** |

- **Evolución de las seis muestras finales:** blandos 23, 11, 11, 5, 7 y 2; duros 0, 0, 0, 1, 1 y 0 (RM:159). Por la
  regla de parada, el mundo 11 queda certificado con la muestra 6.
- **Reproducibilidad:** las dieciocho tandas `m11-*` (`docs/saneamiento/tandas/`), aplicadas en orden sobre el pack
  importado, reproducen exacta la copia limpia (RM:160-163). Una tanda más, `m11-voz-catalogo` (2 correcciones),
  arregló dos nodos del catálogo (4bc0fec6).

## 3. Fases y puentes al núcleo (paso 4, 5c840410)

- **Ciega de fases:** semilla 20261021, escrita antes de sortear (08b5ca7f), con un lector independiente. Coinciden 17
  de 20. Un árbitro resolvió las 3 discrepancias; dos cambian el registro, con corrección declarada
  (`organizar_jornada_entrevistas_candidato` y `montar_reunion_gran_debate` pasan a ejecución) (PF:409-419).
- **Relectura de los puentes:** de 15, se sostienen 13 y 2 no. De 4 sustituciones propuestas, un verificador
  independiente aprueba 3 y rechaza 1 (PF:421-432).

## 4. Duplicados, aristas, puentes y puertas (pasos 5 y 8, d247a7dc y 46d2c5dd)

- **Duplicados leídos:** se compararon los 471 nodos contra los 3.169 vivos del catálogo.
  - 106 pares superan el umbral: 76 del núcleo, 18 de calidad, 7 de franquicias, 4 de compras y 1 de seguridad y salud.
  - Otros 13 caen en la franja.
  - Los 119 veredictos son "continúa": hubo 1 desacuerdo, resuelto, y 0 nodos retirados
    (`dataset/metadata/veredictos_aduana.json`, PF:444-448).
- **Aristas internas:**
  - Se propusieron 502 y se leyeron a ciegas con trampas sin marca en cada ronda, todas cazadas: 412 se sostienen, 84
    son débiles y 6 no se sostienen.
  - Entraron 450 (PF:457-464), aplicadas con `scripts/aplicar_aristas_internas.py`: recíprocas, idempotentes, sin
    ciclos y con su porqué.
  - Con las de la extracción, el mundo tiene hoy 668 aristas internas de `nodos_siguientes`.
- **Puentes al núcleo:** 21 puentes sobre 19 anclas del núcleo, todas vivas. Ninguna ancla pasa de 2, conforme a la ley
  del ancla. Se rechazaron 3.
- **Puertas:** 19, repartidas en ideación 2, validación 3, planificación 5 y ejecución 9
  (`web/lib/assets/packs_entry_seeds.json`). Primero fueron 17:
  - 11 propuestas, verificadas a ciegas con 2 de 2 trampas: 10 precisas y 1 no corresponde (PF:466-477).
  - Sus preguntas pasaron 3 rondas con 6 de 6 trampas. La primera dio 10 adecuadas y 7 flojas; tras corregir el
    generador (ahora ve la condición y el entregable del nodo), 17 de 17 adecuadas (PF:479-483).
  - En el paso 8, desde esas 17 puertas solas `gerber_emyth` alcanzaba 2 de 21 y `marquet_turn_the_ship` 18 de 19.
    Entraron 2 puertas con condición precisa (`hacer_trabajo_futuro_imaginar_negocio` y
    `repartir_decision_cercanos_hechos`), verificadas con 4 de 4 trampas. Con ellas: 21 de 21 y 19 de 19.
- **Alcance desde las puertas del propio mundo:** 95,91 %. Hay 19 nodos (10 de `scott_radical_candor`, 7 de
  `zhuo_manager`, 1 de `smart_who` y 1 de `grove_high_output`) que solo se alcanzan por los puentes del núcleo
  (PF:504-517).
- **Gate 0 de la integración:**
  - 2 componentes, cobertura del 99,95 %, alcanzabilidad dirigida del 100 %, 3.634 activos y 103 semillas
    (PF:497-498).
  - La primera corrida real había dado 259 componentes. Lo impide desde entonces `scripts/seco_gate0_pack.py`, que corre
    el Gate 0 de grafo completo en el seco, con su prueba.
- **Jurisdicción y vigencia:** 2 entradas de jurisdicción, las dos de clase B (`evitar_preguntas_ilegales_entrevista`
  en US y `conducir_llamadas_referencia` en CA), y 2 de vigencia, volcadas a `dataset/metadata/jurisdiccion.json` y
  `vigencia.json`.

## 5. Etiquetas, contrato y catálogo (pasos 6 y 7)

- **Etiquetas del riel en los diez idiomas:** traducidas y revisadas por un segundo modelo.
  - 6 evidentes aplicadas: 1 en alemán, 2 en italiano, 1 en chino, 1 en coreano y 1 en hindi.
  - 56 discutibles en `docs/i18n/M11_DISCUTIBLES_RIEL.md`.
  - Una etiqueta española se corrigió por fidelidad.
- **Base:** la migración 048, con los 4 CHECK de dominio, la aplicó el fundador el 28 sep 2026 y está en main
  (b72090c9).
- **Catálogo:** `primer_equipo` con `"oculto": true`, y su nombre y promesa en once idiomas y en el glosario.
  - Semillas y mapa de brecha horneados: 19 semillas en `packs_entry_seeds.json` y el mapa en `brecha_semillas.json`.
  - La promesa del mundo la decide el fundador en su recorrido.

## 6. Vuelo

- **Primera corrida (733ee641):** la fase del mundo 11 pasó con 5 turnos y 30 ítems. El vuelo cayó después en la 2k
  por falta de saldo del dev user (402), no por el producto.
- **Segunda corrida (df957590):** exportada en `docs/vuelos/2026-09-28_mundo11`. El mundo 11 pasó con 6 turnos y 29
  ítems, entrando por la puerta `crear_tarjeta_puntuacion_puesto`. La caída en la 2L era del arnés, no del mundo; su
  arreglo está en 099101d4.
- **El vuelo completo** pasa a la corrida final, junto con la prueba de coherencia (`docs/producto/CORRIDA_FINAL.md`).

## 7. Lo que queda

- El visto del fundador para mostrar el mundo (quitar `oculto`), tras su recorrido sobre main.
- La ficha `m11-aparcados-reextraccion`: los 6 nodos aparcados.
- Las 56 etiquetas discutibles del riel.
- Las 347 preguntas base del mundo 11 no tienen todavía su versión neutral: se generan en la corrida final junto con
  las del resto del catálogo. Hasta entonces, el adaptador usa la plantilla neutral como salida segura.
