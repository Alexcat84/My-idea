# Cambios de front-end para calibrar (encargo a Claude Design)

Registro **cronológico** de todo cambio visible en la interfaz que se apartó del
canon o lo amplió, para que Design lo calibre después. Cada entrada dice: qué
cambió, por qué, dónde vive, y la captura de referencia en `web/examples/gate-canon/`.

La **matriz** (`MATRIZ_DELTAS_CANON_2.0.md`) lleva el detalle de gobierno; este
archivo es la **línea de tiempo** rápida para el encargo visual. Lo más nuevo
va al final.

---

## 2026-07-21 — El login reanuda donde ibas
- Tras iniciar sesión, el usuario vuelve al punto exacto donde se quedó (idea +
  vista), no al home. Copy "seguimos justo donde quedaste".

## 2026-07-22 — El dictado por voz deja de duplicar
- El campo con voz ya no repite ni arrastra la respuesta anterior al dictar de
  nuevo. Afecta a todos los `CampoConVoz` (entrevista, cierre, motivos).

## 2026-07-22 — Recorrido persistido + Tus Números en grilla + zona de peligro
- El recorrido de la idea se guarda y se re-abre donde iba. "Tus Números" pasó a
  una **grilla** legible. La **zona de peligro** (borrar idea) quedó separada y
  con su color de aviso. (Base del PDF del plan que sigue abajo.)

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

## 2026-07-27 — Stepper de línea continua + 6.º hito "Realizado" + tarjetas accionables
- **Stepper (header de la idea + mini del home):** reescrito como **línea
  continua con los puntos al ras** (riel de fondo + tramo recorrido relleno +
  puntos sentados SOBRE la línea, tapándola). Muere el hueco histórico entre el
  círculo y la línea (el reclamo que Design no había resuelto). Referencia del
  fundador: el patrón flexyui.
- **Nuevo 6.º hito "Realizado"** al final del viaje (antes eran 5). Es la
  **celebración**: el **verde de "terminado" solo se enciende ahí**. Mientras el
  usuario trabaja en Manos a la Obra, el nodo Realizado queda **gris** — el viaje
  aún no terminó (antes el stepper se veía "concluido" en verde a mitad de
  camino). Manos a la Obra sigue en verde vivo (ejecución), pero ya no es el
  final. Refs: `stepper_v2_manos_app.png`, `stepper_v2_home_app.png` (+`_380`).
- **Tarjetas del aside de Manos a la Obra** ("Análisis del proyecto", "Tus
  documentos"): antes la tarjeta entera era el botón y parecía informativa.
  Ahora llevan su **botón de acción abajo** ("Ver análisis" / "Abrir
  documentos"), como la de "Marcar como realizada". Ref: `stepper_v2_manos_app.png`.

## 2026-07-27 — Lote visual: stepper, barra, botones, ritmo, tiles y Gantt
- **Stepper — el verde solo en la celebración:** el punto de la etapa ACTUAL
  (incluida Manos a la Obra) ya NO es verde; es **azul con un anillo estático +
  halo pulsante** ("la punta viva del recorrido"). El verde queda EXCLUSIVO del
  6.º hito Realizado. Azul = recorrido, gris = lo que falta, verde = final.
  Los 6 hitos coinciden con el proceso real de idea a proyecto (los add-ons son
  opcionales y llevan su propia barra). Refs: `lote_analisis_app.png` (header).
- **Acordeón homogéneo (Manos):** TODAS las etapas son acordeón con su chevron
  (antes la 1 y 2 eran secciones planas sin chevron). Abren por defecto hasta la
  primera con pendientes; el resto plegadas. Ref: `lote_manos_app.png`.
- **Barra de avance protagonista:** más gruesa (h-3.5, redondeada) y con el
  **porcentaje** grande como segundo visual. Ref: `lote_manos_app.png`.
- **Acciones como botones (píldoras):** "cambiar" (modo), "Recalcular
  pendientes", "cambiar fecha", "Poner fechas ahora" dejaron de ser texto azul
  suelto (se confundía con texto normal) y ahora se ven como pequeños botones.
- **Panel Ritmo más visual:** cada métrica en una fila con icono en chip +
  etiqueta pequeña + valor en bold (antes lista dt/dd). Mismo tamaño, más lectura.
- **Estadísticos centrados y más visuales:** los tiles (capa universal y
  cumplimiento) van **centrados**, con el número grande y el color en la cifra.
- **Gantt:** el rediseño (barras redondeadas gruesas + días en la leyenda) se
  REVIRTIÓ por decisión del fundador (2026-07-28); vuelve al `gantt_v2` (leyenda
  numerada solo con nombres + dos barras finas base/real + cuadrícula + eje). A
  partir de esa base, los cambios del Gantt los hará **Claude Design**. Ref:
  `gantt_v2_app.png`.

## 2026-07-28 — Ajustes de checklist, documentos y PDF
- **Conteos del acordeón alineados:** el `X/N` de cada etapa se movió a una
  columna a la derecha (junto al chevron), `tabular-nums`; antes lo empujaba el
  largo del nombre y bailaban. Ref: `lote2_manos_app.png`.
- **"cambiar fecha" a la derecha** de la fila (acción), separado de la fecha
  (dato, a la izquierda). Ref: `lote2_manos_app.png`.
- **Panel Ritmo con color:** los tres iconos en chip de color (azul/verde/ámbar)
  y el texto justificado (etiqueta izquierda, valor derecha). Ref: `lote2_manos_app.png`.
- **Documentos:** los dos botones PDF ahora son la MISMA píldora azul marcada
  (antes uno era azul lleno y el otro plano); iconos de documento CON color (hoja
  azul suave por fase, expediente azul lleno). Ref: `lote2_documentos_app.png`.
- **PDF — el pie ya no tapa el texto:** el margen se movió a `@page` (top+bottom
  por página); el bottom reserva la banda del pie. Antes el pie fijo se montaba
  sobre el texto de las páginas intermedias. **(Verificar en un PDF real.)**
- **PDF — rieles en las etapas 1-5:** las listas numeradas (pasos de cada Etapa)
  ganan su línea/riel a la izquierda, como las viñetas. Antes solo la tenían las
  viñetas (p. ej. "¿Puede sostenerse tu idea?").
- **PDF — colores de fecha:** "hecho el X" en **verde** (cumplimiento) y
  "previsto para el X" en **azul** (planificación). El retraso no se castiga:
  nunca rojo. Ref: `lote2_expediente_print.png`.
- **PDF — resumen honesto:** el resumen se titula "Tu progreso hasta aquí"
  mientras el proyecto está en marcha; solo dice "Cómo te fue" cuando ya se
  cerró. PENDIENTE para Design: hacer ese resumen **más visual**.

## 2026-07-28 (b) — Correcciones del fundador sobre lo anterior
- **"cambiar fecha" ABAJO A LA IZQUIERDA:** pasó de la derecha de la fila a
  debajo del texto (abajo-izquierda). El texto de la actividad recupera todo su
  ancho como protagonista; el botón no le roba espacio. Ref: `lote3_manos_app.png`.
- **PDF, riel corregido:** se quitó la línea sola que se había metido en las
  listas numeradas (se veía "inventada") y ahora los pasos de cada Etapa usan el
  MISMO riel de puntos que las viñetas (línea + puntos encima, sin el número).
  **Puntos más grandes (10px) y línea más gruesa (2px)** en TODO el riel.
  Refs: `lote3_riel_ol.png`.
- **PDF, fechas ORDENADAS en tabla:** "Lo que hiciste" pasó de fechas colgando
  al final de cada línea (un desorden) a una **tabla** con columna "Acción" y
  columna **"Cuándo"** (la fecha en su columna, verde si hecho / azul si
  previsto). Ref: `lote3_tabla_fechas.png`.

## 2026-07-28 (c) — Segunda ronda de correcciones
- **"cambiar fecha" ABAJO A LA DERECHA** (no izquierda): el fundador lo aclaró
  con una flecha. Debajo del texto, alineado a la derecha. Ref: `lote4_cambiar_fecha.png`.
- **PDF, riel ALINEADO sin complicar:** los puntos más grandes/línea más gruesa
  quedaban MAL alineados respecto a la línea. Se revierte a la config EXACTA que
  ya funciona en "¿Puede sostenerse tu idea?" (punto de 6px sobre línea de 1px,
  bien centrado). La comparten viñetas y pasos. Ref: `lote4_riel_ol.png`.
- **Claves de sección por estado (expediente):** cada punto de control con su
  clave según el estado. En marcha (aún hay pendientes): el registro es **"Tu
  avance"** y el resumen **"Tu progreso hasta aquí"**. Al cerrar: **"Lo que
  hiciste"** y **"Cómo te fue"**. No se habla en pasado hasta que se termina.
