# Matriz de deltas — canon 2.0 (v1.3.0) vs app en producción

Amarre 2 de la adopción del canon 2.0. Sirve para **decidir el orden de la FASE B**:
qué pantalla ya calza, cuál tiene un delta menor de pulido, y cuál es trabajo grande.

El **veredicto visual final de cada par es del fundador**: aquí clasifico y cito la
evidencia (el par app-vs-canon del gate); el fundador abre el par y confirma.

- **Fecha:** 2026-07-17.
- **Gate:** `web/scripts/gate_canon.ts`, dos viewports (1240 / 380), EXIT=0, 70 capturas
  en `web/examples/gate-canon/`.
- **Numeración:** el gate numera 00–13 en el orden del recorrido; el canon numera 01–14.
  La columna "Par" usa el prefijo del gate; ver el mapa al pie.
- **Señal de cambio Design v1→2.0:** conteo de fragmentos que Design tocó entre canon v1
  y 2.0 (más alto = más rediseño). Es señal secundaria: mucho de eso es CSS, no delta visible.

## La matriz

| # canon | Pantalla | Clase | Par (evidencia) | Qué difiere (concreto) | Confianza |
|---|---|---|---|---|---|
| 01 | Home / Mis ideas | **Delta menor** | `00_home` (+`_380`) | placeholder acortado ("…o en qué punto estás con ella" recortado en la app); la meta line del canon **combina** invitación + sello ("Una pregunta te espera · última acción ayer 21:26"), la app muestra solo uno; mayúscula "Una/una pregunta". Estructura calza. | ✅ visto en el par |
| 02 | La Chispa | **Calza** | `01_chispa` (+`_380`) | diff v1→2.0 = 14 (el más bajo). Momento sagrado. | ⏳ por confirmar en par |
| 03 | Claridad | **Calza / delta menor** | `02_claridad` (+`_380`) | diff 38. Frase + lo que tienes + lo que asumes. | ⏳ por confirmar |
| 04 | La Exploración | **Delta (móvil) — FUERA de esta FASE B** | `03_exploracion`, `03b_oferta_honesta`, `04a_plan_en_camino` (+`_380`) | desktop calza; el riel móvil de la app es un **Acordeón**, el canon 04 pide **hoja inferior "Recorrido"** a 380. Encolado al programa móvil (ver abajo). | 🟡 parcial |
| 05 | Tu Plan | **Delta menor** | `04_tu_plan` (+`_380`) | Tus Números **duplicado** (fila-CTA + tarjeta del grid; el canon lo pone solo como fila); paso 01 con doble "PASOS" y **sin la caja "ENTREGABLE" rotulada**; copy beta ("Gratis durante la beta · un toque lo activa" vs "gratis en beta"). Estructura calza. | ✅ visto en el par |
| 06 | Manos a la Obra | **Delta nuevo** (gestor de estados) | `05_manos` (+`_380`) | el círculo dejó de ciclar por toques: ahora abre un MENÚ de 5 estados (hoja/popover). Nuevo estado "no aplica" con motivo. El avance pasa a "X de N activas". Implementado, vara pendiente. | ⏳ por confirmar |
| 07 | Potenciadores y Créditos | **Delta** | `z_potenciadores_SOLOCANON` (el gate no maneja `/potenciadores` como par) | existe `/potenciadores` (centro de créditos); layout, candados beta y tratamiento visual van contra el canon 07. El **catálogo de packs** NO se alinea al dibujo: `precios.ts` no lo define, así que los bundles (5/12/30 app vs 10/30/75 dibujo) son **decisión pendiente del fundador (ETAPA 2)**; la pantalla lee de `precios.ts` con `$ —` deshabilitado donde falte definición. La activación de potenciadores vive en el grid de Tu Plan. | 🟡 parcial |
| 08 | Mundos Activos | **Calza / delta menor** | `10_mundo_activo`, `10b_mundo_ritual`, `10c_mundo_cierre` (+`_380`) | subproyecto con follow + acta de cierre, implementado (v1.3.2 / 4.2). | ⏳ por confirmar |
| 09 | La Celebración | **Calza / delta menor** | `09_celebracion_cumplimiento`, `09b_celebracion_ritmo` (+`_380`) | timeline azul→verde, dos variantes (3.8). | ⏳ por confirmar |
| 10 | Modo y Fechas | **Calza** | `06_modo`, `07_baseline` (+`_380`) | elección de modo + ritual de fechas (3.8). | ⏳ por confirmar |
| 11 | Análisis del Proyecto | **Calza / delta menor** | `08_analisis` (+`_380`) | capa universal + cumplimiento por mundo (v1.4). | ⏳ por confirmar |
| 12 | El cierre honesto | **Trabajo** | `z_cierre_camino_SOLOCANON`, `z_cierre_mundo_SOLOCANON` (sin par de app) | canon **nuevo**; la app tiene la UI del cierre de la 4.3. Reemplazarla por el diseño canon 12 y **adaptar las salidas core** (primera exploración sin plan → "Volver a mi idea") + el reembolso. | 🟡 solo-canon |
| 13 | Detalle de actividad | **Delta nuevo** (gestor de estados) | `13_detalle` (+`_380`) | los chips de estado suman "no aplica" con su motivo editable (texto/voz); marcar hecho compromete al acto. Implementado, vara pendiente. | ⏳ por confirmar |
| 14 | Tus Números | **HECHO** (web-v1.3.0-numeros) | `numeros_perdida_{app,canon}`, `numeros_sano_{app,canon}` (+`_380`) | Construido y cerrado (C1–C6): calculadora inversa con paridad, pantalla canon 14, tablero vivo (cifras editables, recálculo gratis, cobro 1 vez por idea idempotente, versiones append-only, re-narración que archiva). Vuelo y par del gate verdes, auditados. | ✅ hecho |

### Deltas aceptados del frente 14 (veredicto del fundador, 2026-07-17)

- **"Números que faltan" refleja los faltantes REALES del motor** (días de cobro/inventario/pago), no los ítems ilustrativos del dibujo (tiempo, puesto, merma). **Delta aceptado a favor de la app:** el canon ilustra, el motor confiesa. Un faltante inventado sería una mentira bonita; el real es una guía honesta.
- **Escenarios:** ganancia **NETA de fijos** (como el canon: techo sano $3.900 = 30×170−1.200). La fila "Tu ritmo de hoy" (volumen actual) aparece **solo si el usuario declaró `unidades_vendidas`**; sin ese dato, las dos honestas (pesimista y capacidad plena). Jamás se inventa la base.
- **Historial de versiones (2026-07-18):** el tablero PROMETÍA "tus versiones anteriores quedan guardadas con su fecha" pero no había puerta para verlas. Ahora: el presente lleva su sello ("Tus números de HOY · calculado con tus cifras del [fecha híbrida]"), una sección "Versiones anteriores" lista las pasadas (fecha híbrida + veredicto + margen del snapshot, la hora solo desambigua gemelas del mismo día), y al tocar una se VISITA en modo lectura (banda con el momento absoluto, sin editar: el pasado se visita, no se edita). El "gratis" pasó a la entrada ("Corregir mis cifras · gratis"). **La comparación lado a lado queda en backlog post-beta**, condicionada a telemetría (si alguien alterna versiones repetidamente, se construye con evidencia). Sin vara de Design: mismo estatus que "Tu ciclo de caja".
- **El preview de los mundos (fase 4.5, 2026-07-18):** el modelo comercial cambió (docs/PREVIEW_MUNDOS_PLAN.md): los mundos se prueban gratis y lo que se compra es el PLAN. La fila de potenciadores en sus cuatro estados ([bloqueado] "Se abre con tu plan" / [abierto] "Explóralo gratis" / [diagnóstico listo] / [plan comprado]) y el ESCAPARATE de la sección del mundo (diagnóstico + CTA de compra) son **implementados, vara pendiente de Design**: el canon 07/08 dibuja el modelo con candado, ya superado. El próximo encargo a Design pide los frames con `web/examples/gate-canon/preview_fila_app.png` y `preview_escaparate_app.png` como referencia real.
- **Sección "Tu ciclo de caja" (la puerta de los faltantes, 2026-07-18):** el canon 14 dibujó la PREGUNTA (los días de cobro/inventario/pago en "Números que faltan") pero **no la RESPUESTA** (la sección que muestra el ciclo computado en palabras de persona). Se implementó como estado-sin-vara legítimo: faltantes tocables que abren el recolector en su campo, los campos del ciclo opcionales, y al darlos el tablero estrena "Tu ciclo de caja" ("tu dinero tarda ~N días en volver a tu bolsillo"). **Estado: implementado, vara pendiente de Design.** El próximo encargo a Design pide el frame, con `web/examples/gate-canon/numeros_sano_app.png` como captura real de referencia. El par del gate lo documenta mientras tanto.
- **Gestor de estados por tarea (decisión del fundador, 2026-07-24):** dos pantallas cambian de facto, 06 (Manos a la Obra) y 13 (Detalle). (1) El **ciclo del círculo por toques MURIÓ**: adivinar no es elegir. El círculo (con su etiqueta) abre un **menú de los 5 estados** — hoja inferior a 380, popover en escritorio — cada uno con su punto de color y su palabra, el actual marcado. "Hecha" compromete al acto con hoy (ley vigente); "Marcar hecho" permanece como atajo. (2) Estado nuevo **"no aplica"** (migration 030, con `no_aplica_motivo`): la tarea que el usuario retira porque no corre para su idea, con un **motivo opcional** (texto o voz, "para tu propia memoria"). Visual: hecha = tachada (trofeo); no aplica = **atenuada SIN tachar**, distinguible por FORMA (una barra dentro del círculo, ni verde ni rojo). (3) **Cuentas honestas**: el avance pasa a **"X de N activas"** (las retiradas salen del denominador y **jamás cuentan como tardías**); tienen línea propia en el Análisis, en el acta y en el expediente, con su motivo en la voz del usuario; el bloque de realidad del follow las reporta aparte y el plan de seguimiento **no las compone como pendientes**. Reversible con historia en `project_bitacora` (retirar y reactivar dejan rastro; el motivo viejo se conserva). **Estado: implementado, vara pendiente de Design.** Referencia real para el encargo: `web/examples/gate-canon/estados_menu_app.png`, `estados_menu_app_380.png` y `estados_detalle_app.png`.

**Resumen:** 2 trabajos (14 Tus Números, 12 Cierre honesto), 2 deltas de peso
(04 Exploración móvil, 07 Potenciadores/packs), 3 deltas menores de pulido
(01 Home, 05 Tu Plan, 13 Detalle), 6 que calzan y solo hay que confirmar en el par
(02, 03, 06, 08, 09, 10, 11).

## Decisión de tablero (2026-07-17): la web primero, lo móvil como programa propio

El fundador revisó las 70 capturas del gate. La gran mayoría bien; las **móviles
confirman la deuda conocida** (la web a 380 está apretada, no es experiencia móvil de
verdad). Decisión: **la prioridad es el motor con sus visuales WEB completos**. Todo
trabajo **específicamente-380** se ataca **como programa propio cuando la web esté full**
(la antesala de la APK), con el canon 380 ya dibujado como vara esperando.

En consecuencia, **fuera de esta FASE B** (encolados con su canon, no borrados):
- **04 La Exploración móvil** (hoja inferior "Recorrido" a 380).
- Cualquier ajuste que sea solo del viewport 380 en las demás pantallas.

El **gate sigue capturando en dos viewports**: la evidencia 380 se acumula gratis y la
deuda queda medida, pero no se arregla ahora.

## Orden vigente de la FASE B (2026-07-17)

1. **Tus Números (14)** completo — C2→C6 (en curso; C1 hecho).
2. **El cierre honesto (12)** — web.
3. **Potenciadores y Créditos (07)** — web; packs = decisión pendiente (ETAPA 2).
4. **Pulido menor** — Tu Plan (05), Home (01), Detalle (13).
5. **Confirmar los que calzan** — 02, 03, 06, 08, 09, 10, 11.
6. Tag `web-v1.3.0`.

## Orden recomendado inicial (previo a la decisión de tablero, conservado como registro)

1. **Tus Números (canon 14) — trabajo grande, prioridad 1.** Es la "frenada" del fundador.
   Calculadora inversa (`precioParaMargenObjetivo`, `costoMaximoParaEquilibrio`,
   `unidadesParaCubrirFijos`, `margenConPrecio`) con paridad Python↔TS y tests calculados
   a mano (caso real −$410); pantalla `/idea/[id]/numeros`; **tablero vivo** (cifras editables
   siempre, recálculo determinístico gratis/ilimitado, cobro de 2 créditos **una vez por idea**
   como ancla ETAPA 2, versiones con fecha que no se reescriben, archivar el reporte narrado
   viejo); recolector que **pre-llena de la entrevista**; GIGO cruzando entrevista vs recolector.
   Vuelo: correr → corregir una cifra → re-correr → verificar que el resultado cambia, la versión
   vieja persiste y **no hubo doble cobro**.
2. **El cierre honesto (canon 12) — trabajo.** Reemplazar la UI del cierre 4.3 por el diseño
   canon; adaptar salidas core (primera exploración sin plan → "Volver a mi idea"); el reembolso.
3. **La Exploración móvil (canon 04) — delta de peso.** El riel como hoja inferior "Recorrido"
   a 380 (hoy Acordeón).
4. **Potenciadores y Créditos (canon 07) — delta.** Layout, candados beta y tratamiento
   visual contra el canon 07. El **catálogo de packs NO se alinea al dibujo** (repetiría el
   drift de precios que ya cerramos: el canon refleja precios, jamás los define). `precios.ts`
   no define bundles de compra, así que 5/12/30 (app) vs 10/30/75 (dibujo) son **decisión
   pendiente del fundador para la ETAPA 2**: la pantalla lee de `precios.ts` con `$ —`
   deshabilitado donde falte definición. La compra en dinero queda a ETAPA 2.
5. **Deltas menores de pulido — Tu Plan (05), Home (01), Detalle (13).** Un commit de pulido
   cada uno o agrupados.
6. **Confirmar los que calzan — Chispa (02), Claridad (03), Manos (06), Modo (10),
   Análisis (11), Mundos (08), Celebración (09).** Abrir el par, confirmar, tocar solo lo que difiera.

Al cerrar los seis: tag `web-v1.3.0`.

## Lote 3 adoptado (2026-07-19): las varas pendientes ya tienen dueño

La entrega `entrega-lote3-beta` de Design se adoptó completa (22 HTML en el
canon, 1067 tildes, cero faltas; tabla de créditos citando `precios.ts`
textual; 32 labels únicos y disjuntos). Todo lo que estaba "implementado,
vara pendiente" quedó con vara:

| Pieza | Vara nueva |
|---|---|
| Login por código (2 pasos + estados) | `15_login.html` |
| Fila de potenciadores en 4 estados | `16_fila_potenciadores.html` |
| Escaparate del mundo (diagnóstico) | `17_escaparate_del_mundo.html` |
| Compuerta de Tus Números | `18_compuerta_tus_numeros.html` |
| Tablero vivo completo (ciclo de caja, versiones, modo lectura, recolector) | `19_tablero_vivo_tus_numeros.html` |
| Chip de saldo + estado 402 (cero en gris; 402 en azul) | `20_chip_saldo_y_402.html` |
| Landing con sesión | `21_landing_con_sesion.html` |
| Riel de redacción | `22_riel_de_redaccion.html` |
| Potenciadores y Créditos (post-4.5, precios vivos) | `07_potenciadores_y_creditos.html` (v2; v1 en `_archivo/lote2-pre-beta/`) |

Defectos de la app cazados por Design (HALLAZGOS_PILA_3) y corregidos en la
misma adopción: acentos del copy de Tus Números (23 correcciones + veredicto
y palancas), chip en cero ahora gris, wordmark bicolor en el login. El
"tachado vivo" era captura vieja (muerto desde la ETAPA 2). Además la
adopción cazó un falso positivo del detector de acentos (verbos en -cionó) y
lo corrigió con test.

### Estado-sin-vara nuevo: el botón "Continuar con Google" (2026-07-19)

Decisión del fundador: el login ofrece Google además del código (réplica de
la lógica del I Ching, con allowlist post-auth y adopción del anónimo en
`/auth/callback`). El canon `15_login.html` NO lo contempla — el botón se
implementó con los tokens de la casa (glifo oficial, borde hairline, divisor
"o"). ~~Implementado, vara pendiente de Design (encargo lote 4).~~
**Resuelto: lote 4 adoptado (abajo).**

## Lote 4 adoptado (2026-07-19): el canon queda en 24 pantallas

La entrega `entrega-lote4-beta` se adoptó completa: acentos LIMPIO (canon a
1360 tildes, cero faltas), precios exactos citando `precios.ts` (packs
5/$4.99 · 15/$14.99 · 30/$29.99, costos 2/3/5, cortesía 20), 32
`data-screen-label` únicos y disjuntos.

| Pieza | Vara nueva |
|---|---|
| Centro de cuenta (/cuenta), 8 estados incl. candado 423 y activada-correo | `23_centro_de_cuenta.html` |
| Desafío del login (app / correo / rescate) | `24_desafio_dos_pasos.html` |
| Login con Google + no-invitado de dos puertas | `15_login.html` v2 (v1 en `_archivo/lote3-beta/`) |
| Potenciadores con catálogo decidido + tabla de costos | `07_potenciadores_y_creditos.html` v3 (v2 archivada) |

Hallazgos de Design (HALLAZGOS_PILA_3 del lote 4) adjudicados:
- **H1 (dígitos sin tilde) y H2 (13 X)**: falsos positivos de lectura del
  PNG — el fuente tiene la tilde y el placeholder tiene 12 X exactas (el
  acento de la í a 13px parece punto; el letter-spacing engaña el conteo).
- **H3 (colisión móvil al confirmar borrado)**: real, corregido — la
  confirmación baja a su propia línea en 380 (`w-full` + `flex-wrap`).
- **H4 (guion largo del no-invitado)**: real, corregido con el copy del
  canon 15 v2, que además muestra el correo intentado (el callback de
  Google ahora lo devuelve en `?correo=`).
- **H5 (My idea vs My Idea)**: real — /ideas y /cuenta decían "My idea";
  unificado a "My Idea" (la grafía del canon).
- **H6 (escenarios con nombres inventados en 07)**: real — el blurb decía
  "prudente, esperado y optimista"; el tablero real dice Pesimista /
  A capacidad plena. Corregido al copy del canon ("ventas" incluido).
- **H7 (piezas del 07 ausentes en la app)**: real — la app estaba DETRÁS
  de la vara del lote 3: se añadieron la tabla "Lo que cuesta cada cosa"
  (leyendo de precios.ts), el chip verde "cortesía de bienvenida" y el chip
  de mundos "Explóralo gratis" con su pie "El preview es gratis · su plan".

## Decisiones pendientes (no las toma la FASE B)

- ~~**Catálogo de packs del centro de créditos (07)**: decisión pendiente del fundador.~~
  **Resuelto (2026-07-19)**: packs 5/$4.99 · 15/$14.99 · 30/$29.99 en `precios.ts` (`PACKS`),
  1 crédito = 1 USD invariable, sin descuento por volumen. Ver "Lote 4 adoptado" arriba.

- **La cortesía del lanzamiento público (post-beta): DECISIÓN PENDIENTE del fundador**
  (aclaración de gobierno, 2026-07-20). `CORTESIA_BETA = 20` (`web/lib/creditos.ts`) es la
  política de la **BETA CERRADA** (solo invitados de `beta_allowlist`), **no** la política de
  bienvenida del usuario nuevo tras el lanzamiento público. Confundir ambas sería autorizar por
  omisión un monto que nadie decidió para producción. Candidata preliminar del fundador (no
  autorizada): organizador gratis + 5 créditos de bienvenida = exactamente el costo de un plan
  completo (`PRECIOS.plan_completo`); se calibra con la telemetría real de esta beta antes de
  fijarse. Mientras no haya decisión, el código de producción no otorga cortesía a nadie fuera
  de la allowlist (la frontera de la beta sigue siendo la puerta). Ver
  `docs/BANCO_DE_TEXTOS.md` para el copy vigente y esta fila para el estado de la decisión.

## Mapa gate → canon

| Prefijo gate | Canon | Estado del par |
|---|---|---|
| `00_home` | 01 Home / Mis ideas | app + canon |
| `01_chispa` | 02 La Chispa | app + canon |
| `02_claridad` | 03 Claridad | app + canon |
| `03_exploracion`, `03b_oferta_honesta`, `04a_plan_en_camino` | 04 La Exploración | app + canon |
| `04_tu_plan` | 05 Tu Plan | app + canon |
| `05_manos` | 06 Manos a la Obra | app + canon |
| `06_modo`, `07_baseline` | 10 Modo y Fechas | app + canon |
| `08_analisis` | 11 Análisis del Proyecto | app + canon |
| `09_celebracion_cumplimiento`, `09b_celebracion_ritmo` | 09 La Celebración | app + canon (2 variantes) |
| `10_mundo_activo`, `10b_mundo_ritual`, `10c_mundo_cierre` | 08 Mundos Activos | app + canon (3 estados) |
| `13_detalle` | 13 Detalle de actividad | app + canon |
| `z_potenciadores_SOLOCANON` | 07 Potenciadores y Créditos | solo canon (`/potenciadores` no lo maneja el gate) |
| `z_cierre_camino_SOLOCANON`, `z_cierre_mundo_SOLOCANON` | 12 El cierre honesto | solo canon (app tiene UI 4.3) |
| `z_numeros_perdida_SOLOCANON`, `z_numeros_sano_SOLOCANON` | 14 Tus Números | solo canon (no hay pantalla) |
