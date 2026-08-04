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

## 1c. Restructuración "TODO SEPARADO" (COMPLETA — T0..T7, cerrada 2026-08-04)

**Plan/contrato: `docs/PLAN_TODO_SEPARADO.md`** (aprobado por fundador y auditor, 6
decisiones cerradas). Cada espacio se mide/registra/documenta solo; el mundo es espejo
TOTAL del core (su análisis con Gantt, su calendario, su modo de fechas y línea base);
única vista global = Expediente. **Cerrada con el veredicto del fundador y el tag
`web-v2.2.0-beta`.** Matriz de las 8 tandas — **todas ✓, en producción (main):**

- **T0 gobierno** ✓ · **T1 eliminar nivel general** ✓ (murió "La idea completa",
  `IdeaCompleta.tsx` borrado, barras cross-mundo muertas) · **T2 "Tu avance"→solo hitos** ✓.
- **T3 paridad de fechas por mundo** ✓ (migración `project_modos` aplicada; B5 no-arrastre;
  `capaCumplimientoDe` extraída con golden; hub del mundo con su modo/ritual; Gantt del mundo).
- **T4 vistas scopeables** ✓ (Análisis del mundo con su Gantt; los cuatro accesos del espacio).
- **T5 seis tarjetas hermanas** ✓ (`TarjetaAcceso` único, contrato que lo blinda).
- **T6 calendario etiquetado `[Espacio]`** ✓ (feed que crece con los mundos; UID intacto).
- **T7 documentos en dos recuadros** ✓ ("Reportes globales" + "Reportes de {espacio}").
- **Cierre** ✓: corrida única del fundador (vuelo `faseTodoSeparado` 16/16 + gate del frente
  entero) + veredicto visual; merge de cierre + tag `web-v2.2.0-beta`.

Notas de método (para memoria): la migración `project_modos` la aplicó el fundador; B5
bendecido (cada espacio sella SU baseline, el core no arrastra); golden test antes de
extraer `capaCumplimientoDe`. **Pendiente SOLO la calibración visual de Design (§2).**

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
  - **Estado del frente: COMPLETO Y EN PRODUCCIÓN (tag `web-v2.2.0-beta`).** La
    restructuración "todo separado" (T3c-2..T7) está entera y funcional; este encargo
    queda **consolidado como la SPEC VISUAL pendiente** — la calibración de CD sobre TODOS
    sus pares del frente, capturados por el gate (§3): hub + su **modo/ritual** de fechas
    del mundo, **Análisis del mundo con su Gantt**, los **cuatro accesos** scopeados, las
    **seis tarjetas hermanas** (`TarjetaAcceso` uniforme), el **calendario etiquetado**
    `[Espacio]`, y los **documentos en dos recuadros**. El front no espera a Design: lo que
    CD calibre se aplica encima. Pares en `web/examples/gate-canon/` (`espacios_*`).
- **NOTA (no pedido) — el "viernes compartido" del sugeridor de fechas:** en modo
  fechas, todos los ítems regulares de una etapa caen el mismo día (el viernes de su
  semana): es **doctrina** (la fecha es el compromiso de entrega de la etapa, no una
  agenda diaria — BANCO §7.1). Si en la beta el fundador ve confusión con ese día
  compartido, la palanca es **de presentación (CD)** —agrupar, un encabezado de
  "entrega de la etapa", lo que sea visual— **jamás del sugeridor** (escalonar sería
  precisión inventada). Se anota aquí para tenerlo a mano; NO es un encargo abierto.
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
