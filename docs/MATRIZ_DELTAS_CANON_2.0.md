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
| 04 | La Exploración | **Delta (móvil)** | `03_exploracion`, `03b_oferta_honesta`, `04a_plan_en_camino` (+`_380`) | desktop calza; el riel móvil de la app es un **Acordeón**, el canon 04 pide **hoja inferior "Recorrido"** a 380. | 🟡 parcial |
| 05 | Tu Plan | **Delta menor** | `04_tu_plan` (+`_380`) | Tus Números **duplicado** (fila-CTA + tarjeta del grid; el canon lo pone solo como fila); paso 01 con doble "PASOS" y **sin la caja "ENTREGABLE" rotulada**; copy beta ("Gratis durante la beta · un toque lo activa" vs "gratis en beta"). Estructura calza. | ✅ visto en el par |
| 06 | Manos a la Obra | **Calza** (reorganizado 4.3.2) | `05_manos` (+`_380`) | el replanteo del 380 ya se hizo esta sesión: "contar qué pasó" arriba, plegables, modo compacto. | ⏳ por confirmar |
| 07 | Potenciadores y Créditos | **Delta** | `z_potenciadores_SOLOCANON` (el gate no maneja `/potenciadores` como par) | existe `/potenciadores` (centro de créditos); layout, candados beta y tratamiento visual van contra el canon 07. El **catálogo de packs** NO se alinea al dibujo: `precios.ts` no lo define, así que los bundles (5/12/30 app vs 10/30/75 dibujo) son **decisión pendiente del fundador (ETAPA 2)**; la pantalla lee de `precios.ts` con `$ —` deshabilitado donde falte definición. La activación de potenciadores vive en el grid de Tu Plan. | 🟡 parcial |
| 08 | Mundos Activos | **Calza / delta menor** | `10_mundo_activo`, `10b_mundo_ritual`, `10c_mundo_cierre` (+`_380`) | subproyecto con follow + acta de cierre, implementado (v1.3.2 / 4.2). | ⏳ por confirmar |
| 09 | La Celebración | **Calza / delta menor** | `09_celebracion_cumplimiento`, `09b_celebracion_ritmo` (+`_380`) | timeline azul→verde, dos variantes (3.8). | ⏳ por confirmar |
| 10 | Modo y Fechas | **Calza** | `06_modo`, `07_baseline` (+`_380`) | elección de modo + ritual de fechas (3.8). | ⏳ por confirmar |
| 11 | Análisis del Proyecto | **Calza / delta menor** | `08_analisis` (+`_380`) | capa universal + cumplimiento por mundo (v1.4). | ⏳ por confirmar |
| 12 | El cierre honesto | **Trabajo** | `z_cierre_camino_SOLOCANON`, `z_cierre_mundo_SOLOCANON` (sin par de app) | canon **nuevo**; la app tiene la UI del cierre de la 4.3. Reemplazarla por el diseño canon 12 y **adaptar las salidas core** (primera exploración sin plan → "Volver a mi idea") + el reembolso. | 🟡 solo-canon |
| 13 | Detalle de actividad | **Delta menor** | `13_detalle` (+`_380`) | construido en 4.3.2; canon nuevo. Comparar y ajustar deltas, **no rehacer**. | ⏳ por confirmar |
| 14 | Tus Números | **Trabajo grande** | `z_numeros_perdida_SOLOCANON`, `z_numeros_sano_SOLOCANON` (sin par de app) | **no existe** `/idea/[id]/numeros` ni la calculadora inversa. Toda la pantalla + el tablero vivo (cifras editables, recálculo determinístico gratis, cobro de 2 créditos **una vez por idea**, versiones con fecha, archivar el reporte narrado viejo). | ✅ cierto: nada construido |

**Resumen:** 2 trabajos (14 Tus Números, 12 Cierre honesto), 2 deltas de peso
(04 Exploración móvil, 07 Potenciadores/packs), 3 deltas menores de pulido
(01 Home, 05 Tu Plan, 13 Detalle), 6 que calzan y solo hay que confirmar en el par
(02, 03, 06, 08, 09, 10, 11).

## Orden recomendado de la FASE B (el fundador decide)

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

## Decisiones pendientes (no las toma la FASE B)

- **Catálogo de packs del centro de créditos (07):** `precios.ts` **no** define bundles de
  compra (solo precios por concepto; `packs_catalog.json` es de mundos, no de bundles). Hoy
  hay 5/12/30 hardcodeados en `/potenciadores` y el dibujo de Design propone 10/30/75.
  **Ninguno está autorizado.** La FASE B **no** alinea al dibujo (eso repetiría el drift de
  precios): implementa la pantalla leyendo de `precios.ts`, con `$ —` deshabilitado donde falte
  definición. **El fundador decide el catálogo en la ETAPA 2** (frente cuentas-y-créditos).

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
