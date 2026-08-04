# Pendientes — My Idea

Lista viva de lo que queda por hacer. Se actualiza al cerrar o abrir frentes.
(Última actualización: agosto 2026.)

## 1. Campaña "Espacios" — Fase 3 (COMPLETA, en staging)

**Plan y contrato: `docs/PLAN_ESPACIOS_FASE3.md`** (Opción A "dentro de Tu avance";
garantías de fuente única / partición exacta / sin doble conteo / ruido cero).
Las 5 tandas cerradas; tandas 1-4 en main, tanda 5 en staging (pendiente del visto
para main + tag de la campaña).

- **T1 — la fuente etiquetada** ✓: `EntradaBitacora.dominio` ("core" | mundo | null
  no-derivable), partición exacta, estampado de `payload.dominio` en los writes.
- **T2 — estadísticas por espacio** ✓: `analyticsDeMundo` pintado en "Tu avance"
  (core y cada mundo), tiles reusados, test de no doble conteo.
- **T3 — bitácora por espacio** ✓: filtro en servidor con `bitacoraDeEspacio`, reuso
  de `LineaBitacora`/`BitacoraPapel`, descarga .md/PDF scopeada.
- **T4 — Análisis global + etiquetas + ruido cero** ✓: "Tu proyecto completo" (suma
  declarada), etiqueta de espacio como DATO estructural (murió el sufijo de texto).
- **T5 — documentos por espacio** ✓: "Reporte de {mundo}" (plan+seguimientos+avance+
  cómo te fue+secuencia, del mismo armador), Expediente completado por-mundo (acciones
  + cómo te fue), etiqueta de espacio en los documentos.

## 1b. "La idea completa" (nivel general) — ANULADA por "Todo separado"

El frente "La idea completa" (tag `web-v2.1.0-beta`) fue **anulado** por el veredicto
"todo separado": muere el nivel general (no hay análisis ni medida global; la única vista
global es el Expediente). Se elimina en la tanda 1 de la restructuración. (El plan
`docs/PLAN_IDEA_COMPLETA.md` queda como archivo histórico.)

## 1c. Restructuración "TODO SEPARADO" (APROBADA, EN CURSO)

**Plan/contrato: `docs/PLAN_TODO_SEPARADO.md`** (aprobado por fundador y auditor, 6
decisiones cerradas). Cada espacio se mide/registra/documenta solo; el mundo es espejo
TOTAL del core (su análisis con Gantt, su calendario, su modo de fechas y línea base);
única vista global = Expediente. 8 tandas (T0 gobierno · T1 eliminar nivel general · T2
"Tu avance"→hitos · **T3 paridad de fechas por mundo, con migración `project_modos`** · T4
vistas scopeables · T5 seis accesos/acciones uniformes · T6 calendario etiquetado · T7
documentos en dos recuadros · cierre). Tag propuesto `web-v2.2.0-beta`.

- **Migración T3** (`project_modos`): la aplica el fundador; se le entrega el SQL y se
  espera su "aplicada" antes del vuelo de esa tanda.
- **B5 bendecido:** cada espacio sella SU baseline en SU ritual; el core deja de arrastrar
  los mundos (con dual-read de transición del modo del core).
- **Golden test obligatorio** antes de extraer `capaCumplimientoDe` de `calcularAnalytics`.

## 2. Claude Design (encargos)

- **Centro de créditos v4** (alta industria, modelo de consumible): brief y prompt v2
  listos (`docs/calibracion-design/BRIEF_CREDITOS.md`, `PROMPT_CREDITOS_CD.md`).
  Esperando opciones de CD.
- **Espacios + La idea completa (encargo ACUMULADO, front funcional ya en su sitio):**
  `docs/calibracion-design/BRIEF_ESPACIOS.md` listo (dos niveles de navegación
  explícitos). Calibración visual de CD sobre las superficies del frente **tras "todo
  separado"** (el nivel general SE ELIMINA del encargo):
  - hub + **cambiador** de espacios (pestañas-fichero, la activa levantada);
  - las **3 caras** (Plan · Manos a la obra · **Tu avance = solo la línea de hitos**);
  - **las seis tarjetas hermanas** por espacio (Mi bitácora · Tu calendario · Análisis ·
    Tus documentos · Marcar realizada/Cerrar · Contar qué pasó), mismo formato de tarjeta;
  - el **Análisis por mundo** (con su Gantt) y el **modo de fechas/ritual en el hub del
    mundo** (paridad total);
  - el **calendario etiquetado** (`[Espacio]` en cada actividad) y los **documentos en dos
    recuadros** (Global + del espacio);
  - las **varas previas** que quedan: chips de etiqueta en la bitácora global y las fichas
    de Reporte por mundo. (Muere del encargo: la banda "Lo general" y el desglose "Tu
    proyecto completo".)
  - **Estado del frente (staging):** el modo/ritual del mundo (T3c-2), el **Análisis del
    mundo con su Gantt** (T4a) y **los cuatro accesos scopeados** del espacio (T4b) ya
    están funcionales; sus pares de gate para calibrar están en §3 (`espacios_*_mundo`).
    Pendientes del propio "todo separado": T5 (seis tarjetas hermanas uniformes), T6
    (calendario con `[Espacio]`), T7 (documentos en dos recuadros).
- **PDF Expediente · interiores (DIFERIDO post-beta):** el diseño YA existe
  (`_entrega-claude-design/Entrega-desing 20260729/entrega2/pdf-expediente-interiores/`:
  Tus Números, un mundo, "Cómo te fue", "La secuencia de tu viaje"). **Cuando sea el
  momento: pedirle a CD regenerar esas 4 páginas en HTML LIMPIO (sin imágenes
  embebidas / blobs)** para poder implementarlas; las HTML entregadas están pesadas y
  no se pueden leer bien tal cual.

## 3. Verificación en vivo (necesita `pnpm dev` + Supabase real; la corre el fundador/auditor)

- **Vuelo de dinero** (`web/scripts/vuelo_beta.ts`): la contabilidad nueva del Catálogo
  congruente (siembra 30 → plan −10 → Tus Números 0 → mundo −5 → seguimiento −5 →
  seguimiento de mundo −5 = 5). **NO corrido en vivo.**
- **Gate** (`web/scripts/gate_beta.ts`): capturas en dos viewports de `/creditos`, el
  cambiador, el hub y las **3 caras**, **más (Fase 3 T4-T5)** la **bitácora global con
  etiquetas** (`?vista=bitacora`), el Análisis del núcleo (`?vista=analisis`) y los
  **reportes por mundo** (`?vista=documentos`). **NO corrido en vivo** → verificar al
  ejecutarlo (la siembra del mundo con plan y las esperas nuevas).
- **Gate — "todo separado" (T3c-2/T4), pares nuevos del ESPACIO** (referencia para el
  encargo de Design; el run en vivo y el veredicto los da el fundador). Al ejecutar
  `gate_beta` se generan en `web/examples/gate-canon/` (tracked en staging, excluidos del
  release a main por patrón):
  - `espacios_hub_mundo_ritual` — el hub del mundo con **su** modo/ritual de fechas
    scopeado (T3c-2, paridad con el núcleo).
  - `espacios_analisis_mundo` — el **Análisis del mundo** a pantalla completa con **su
    Gantt** (`porEtapa`) sellado (T4a, el "pair B"): quality activada en el pasado, su
    baseline sellada, 1/1/1 de 3 a mano.
  - `espacios_bitacora_mundo` · `espacios_calendario_mundo` · `espacios_documentos_mundo`
    — los otros **tres accesos scopeados** del espacio (T4b), misma tarjeta que el núcleo.
  Vara para Design: los **cuatro accesos del espacio** con formato de tarjeta UNIFORME (la
  vara de las seis hermanas de T5 llega después; aquí no hay formato nuevo que deshacer).
- **Veredicto visual del fundador** sobre el conjunto de Espacios y sobre el centro de
  créditos (cuando pruebe en producción).
- **Auditoría**: Catálogo congruente y Espacios quedan en revisión del auditor.

## 4. Pasarelas y cuenta — ETAPA 3 (dormido a propósito)

- **Compra con dinero** (RevenueCat / Stripe / Play): la compra "se abre pronto"; el
  catálogo de packs muestra el estado deshabilitado hasta la ETAPA 3.
- **Siembra manual de créditos** (mientras): el fundador otorga créditos desde Supabase
  (`otorgar_creditos`, origen `siembra_beta`) — documentado en `docs/BETA_CUENTAS_README.md §2.f`.
- **2FA/TOTP + dominio de correo propio**: dormido (anclas listas).

## 5. Backlog / afinar

- **Ajustes visuales de Espacios** que salgan de la prueba del fundador (grosor del eje y
  tamaño de nodos de "Tu avance", cuánto se "levanta" la pestaña activa, el segmentado).
- **Varas de Design de la Fase 3** (calibración visual, front funcional ya en su sitio):
  las estadísticas por espacio (T2), la bitácora por espacio (T3), los chips de etiqueta
  en la bitácora global (T4), el desglose "Tu proyecto completo" del Análisis (T4) y las
  fichas de Reporte por mundo en Documentos (T5). Encargo a CD si el fundador quiere pulir.
- **Píldora-humana** en las fechas: backlog post-beta (de la fidelidad al canon).
- La **decoración de papel** de los interiores del Expediente (ver §2, ligado al pedido a CD).
- **`cumplimiento-desglose-core-multiciclo`** (analytics): la fila "core" de
  `cumplimientoPorDominio` cuenta ítems de cualquier ciclo, mientras los tiles globales
  cuentan solo el plan baseline vigente. No es doble conteo; criterio distinto que puede
  no cuadrar con varios ciclos. Arreglo NO es de una línea (pasar el id del baseline a
  `cumplimientoPorDominio`). Nombrado en `docs/PLAN_ESPACIOS_FASE3.md §6`; **jamás
  arreglar "de paso"**.

## Hecho recientemente (para no reabrirlo por error)

- **Calendario**: modo con-fechas + recordatorios + `.ics` universal (webcal) EN PRODUCCIÓN.
  El **Google Calendar Nivel 1 se RETIRÓ** a favor del webcal universal (no reabrir).
- **Catálogo congruente** (precios 10/5, Tus Números incluido, beta sin cortesía): EN PRODUCCIÓN.
- **Espacios** Fase 1+2 + las 3 caras (Plan · Manos a la obra · Tu avance): EN PRODUCCIÓN.
