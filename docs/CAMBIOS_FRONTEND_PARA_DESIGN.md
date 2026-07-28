# Cambios de front-end para calibrar (encargo a Claude Design)

Registro **cronológico** de todo cambio visible en la interfaz que se apartó del
canon o lo amplió, para que Design lo calibre después. Cada entrada dice: qué
cambió, por qué, dónde vive, y la captura de referencia en `web/examples/gate-canon/`.

La **matriz** (`MATRIZ_DELTAS_CANON_2.0.md`) lleva el detalle de gobierno; este
archivo es la **línea de tiempo** rápida para el encargo visual. Lo más nuevo
va al final.

---

## 2026-07-23 — PDF del plan visual + pie identificativo
- El "Descargar PDF" del plan conserva la identidad (azul piensa, verde ejecuta,
  puntos con su línea) en papel: se redefinen los tokens para papel en vez de
  aplanar a blanco y negro. Pie con el nombre de la idea, `@page margin 0`.
- Ref: `docs_pdf_portada.png`, `docs_pdf_plan.png`, `docs_pdf_lo_que_hiciste.png`.

## 2026-07-23 — Documentos por fase (Tus documentos)
- Nueva pantalla `?vista=documentos`: Tu Plan, cada Seguimiento y el Expediente
  completo, en `.md` y PDF. Ref: `docs_panel.png`.

## 2026-07-23 — Etiquetas de cara (riel / navegación)
- El usuario ya no ve títulos técnicos ni jerga: toda superficie muestra
  `etiqueta_arbol`. Ref: `gate_etiquetas_riel.png`.

## 2026-07-24 — Marcar hecho sin trampa + stepper con líneas continuas
- El stepper de 5 etapas: conectores **continuos** (antes punteados, se veían
  cortados). Home + header de la idea.
- "Marcar hecho" compromete al instante (fecha de hoy); la fecha se ajusta
  después. (Luego revisado por el gestor de estados, ver abajo.)

## 2026-07-24 — Gestor de estados por tarea (06 Manos a la Obra, 13 Detalle)
- El **ciclo del círculo por toques murió**: el círculo abre un **menú de 5
  estados** (hoja inferior a 380, popover en escritorio), con su punto de color
  y palabra; "Hecha" resaltada.
- Estado nuevo **"no aplica"** con motivo opcional (voz/texto); visual atenuado
  SIN tachar, distinguible por forma.
- Avance "X de N **activas**" (las retiradas fuera del denominador).
- Refs: `estados_checklist.png`, `estados_menu_app.png` (+`_380`),
  `estados_detalle_app.png`.

## 2026-07-24 — Análisis: barras Gantt (corrige la 1.ª errata de vara del canon 11)
- Las barras "Planificado vs. real por etapa" pasaron de **acumuladas**
  (confundían) a **Gantt** (cada etapa arranca donde terminó la anterior; largo
  = duración; línea de tiempo con eje en días).
- Decidido con spike A/B/C: `canon11_barras_spike.png` (+`_380`).
- Ref ganadora: `gantt_analisis_app.png` (+`_380`).

## 2026-07-24 — Control de estado sin botón "Marcar hecho"
- Se retiró el atajo (redundante con el menú). Disparador reforzado (círculo +
  chevron + hover) + **pista de primer uso** que se va tras el primer cambio.
  Menú abre con "Hecha" primera/resaltada.
- Refs: `control_manos_app.png` (+`_380`), `control_menu_app.png` (+`_380`).

## 2026-07-24 — "cambiar fecha" como acción aparte
- En una tarea hecha, la fecha ("hecho el 20 de julio") queda como dato (verde)
  y **"cambiar fecha"** como acción (azul), sin el "·" que los fundía. Fila del
  checklist y cajón de detalle.

## 2026-07-27 — Tus documentos: cintas más visuales + Análisis: dashboard reorganizado
- **Tus documentos:** cada cinta gana un **icono de documento** (una hoja para
  cada fase; hojas apiladas para el Expediente), con estructura de tarjeta
  estándar (icono + título/subtítulo/fecha + acciones) y hover.
  Ref: `docs_cintas_app.png` (+`_380`).
- **Análisis · capa de cumplimiento:** indicadores **reorganizados** en una fila
  de 4 tiles compactas (a tiempo · adelantadas · tardías · desviación media), en
  la misma familia que la capa universal (el color vive en el número).
- **Gantt rediseñado:** la **leyenda numerada** de actividades va arriba (los
  nombres, una vez); abajo el **diagrama limpio** (número + barras base/real)
  con **cuadrícula sutil** y eje de tiempo. El texto ya no parte el diagrama.
  Ref: `gantt_v2_app.png` (+`_380`).
