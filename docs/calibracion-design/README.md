# Paquete de calibración para Claude Design

**Fecha del encargo:** 2026-07-29
**Última calibración de Design:** Lote 4 (2026-07-19). **Todo lo posterior está
SIN calibrar.**

Este documento es el manifiesto del encargo: qué calibrar, con qué archivos, y
las dos piezas nuevas que además necesitan diseño (el Gantt y la bitácora).

---

## 1. Qué es esta calibración

Desde el Lote 4, el fundador dirigió una tanda de cambios de front-end
(implementados por Claude Code) que **cambiaron o ampliaron el canon**. Están
todos registrados, con su porqué, en `docs/CAMBIOS_FRONTEND_PARA_DESIGN.md` (la
línea de tiempo) y `docs/MATRIZ_DELTAS_CANON_2.0.md` (el gobierno).

**El encargo a Design:** tomar esos cambios ya funcionando y **pulirlos
visualmente** hasta el estándar de la casa, y **diseñar de cero** las dos piezas
nuevas (Gantt y bitácora) con briefs propios. Claude Code sigue implementando
bajo la dirección del fundador; Design calibra la vara visual.

## 2. Las reglas de la casa (no negociables)

- **La vara es el archivo, no el recuerdo.** El canon vive en
  `docs/diseno-canon/*.html`. Los tokens de color/tipografía en
  `web/app/tokens.css`. La voz y las fronteras en `docs/BANCO_DE_TEXTOS.md`.
- **Ley de color:** azul piensa, verde ejecuta/celebra, ámbar guardián (nunca
  rojo para el usuario). Gris = lo que falta.
- **Sin guiones largos** (— –) en copy visible.
- **Confidencialidad:** el usuario JAMÁS ve nodos, grafos, conteos internos ni
  mecánica del motor. Todo se nombra con la etiqueta de cara.
- **Dos viewports siempre:** escritorio (1240) y móvil (380).

## 3. Cambios SIN calibrar (resumen; el detalle en el log)

Ordenados de más viejo a más nuevo. Cada uno con su captura de `app` (estado
actual) para comparar contra el canon.

| # | Cambio | Capturas (en `web/examples/gate-canon/`) |
|---|--------|------|
| 1 | Gestor de estados por tarea (menú de 5 estados, no aplica) | `estados_checklist_app`, `estados_menu_app`, `estados_detalle_app` (+`_380`) |
| 2 | Control sin botón "Marcar hecho" + pista de primer uso | `control_manos_app`, `control_menu_app` (+`_380`) |
| 3 | Stepper de línea continua + 6.º hito "Realizado" (verde solo al final) | `stepper_v2_manos_app`, `stepper_v2_home_app` (+`_380`) |
| 4 | Manos a la Obra: acordeón homogéneo, barra con %, acciones como botones, panel Ritmo con iconos | `lote_manos_app`, `lote3_manos_app`, `lote4_cambiar_fecha` (+`_380`) |
| 5 | Tus documentos: cintas con icono, botones PDF consistentes | `docs_cintas_app`, `lote2_documentos_app` (+`_380`) |
| 6 | Análisis: tiles centrados, capa de honestidad "frente a tu plan inicial" | `lote_analisis_app` (+`_380`) |
| 7 | Oferta de cascada al mover una fecha (detalle) | `cascada_oferta` |
| 8 | PDF: tabla de fechas + riel de puntos (espina que atraviesa) | `lote3_tabla_fechas`, `riel_v3`, `lote2_expediente_print` |

## 4. Las dos piezas NUEVAS que necesitan diseño (briefs aparte)

- **El Gantt del Análisis** → `BRIEF_GANTT.md`. Estado actual: `gantt_v2_app`
  (+`_380`). El fundador lo quiere **más visual y representativo, pero simple**
  para el usuario. Claude Code revirtió el rediseño anterior a este `gantt_v2`;
  desde esta base, Design propone.
- **La bitácora del cliente (página en vivo)** → `BRIEF_BITACORA.md`. Estado
  actual: `bitapage_pagina` (la página), `bitapage_panel` (el botón "Ver"). Es
  una primera versión funcional (línea de tiempo con barra + puntos); Design la
  vuelve bella.

## 5. El paquete de archivos a subir

**Documentos de gobierno (texto):**
- `docs/CAMBIOS_FRONTEND_PARA_DESIGN.md`
- `docs/MATRIZ_DELTAS_CANON_2.0.md`
- `docs/BANCO_DE_TEXTOS.md`
- `docs/calibracion-design/README.md` (este archivo)
- `docs/calibracion-design/BRIEF_GANTT.md`
- `docs/calibracion-design/BRIEF_BITACORA.md`

**El canon de referencia (la vara):**
- Toda la carpeta `docs/diseno-canon/` (los `*.html` y `REGLAS_Y_TOKENS.md`).

**Los tokens vivos:**
- `web/app/tokens.css`

**Las capturas del estado ACTUAL** (las de la tabla de §3 y §4; están todas en
`web/examples/gate-canon/`). Las clave para esta ronda:
`stepper_v2_manos_app(_380)`, `stepper_v2_home_app(_380)`, `lote_manos_app(_380)`,
`lote_analisis_app(_380)`, `docs_cintas_app(_380)`, `gantt_v2_app(_380)`,
`cascada_oferta`, `lote3_tabla_fechas`, `riel_v3`, `bitapage_pagina`,
`bitapage_panel`, `estados_menu_app(_380)`, `control_manos_app(_380)`.

## 6. Prioridades

1. **Gantt** (pieza nueva, el fundador la espera con ganas). Ver `BRIEF_GANTT.md`.
2. **Bitácora** (pieza nueva, es casi una página propia). Ver `BRIEF_BITACORA.md`.
3. Calibración fina del resto (stepper, Manos, Análisis, documentos, PDF).
