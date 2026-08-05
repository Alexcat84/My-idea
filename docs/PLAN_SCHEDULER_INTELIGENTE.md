# Plan de implementación — Campaña "SCHEDULER INTELIGENTE"

**Visión original del fundador (PM).** Un programador de fechas que entienda la
complejidad y el alcance de cada tarea y sugiera fechas que RESPIREN según la
capacidad real del usuario, cuando pide "Con fechas" — sin traicionar la
honestidad de la casa.

- **Spec / factibilidad:** [`docs/SCHEDULER_INTELIGENTE.md`](SCHEDULER_INTELIGENTE.md)
  (investigación, arquitectura de 3 capas, riesgos). Este doc es el **plan de
  ejecución** por fases.
- **Cadencia:** checkpoint por fase · merge con el visto del fundador · commits
  `Scheduler:` · autopush a staging.
- **Base:** main `943ce0d` (tras el sugeridor honesto: chapa "esta semana" +
  orden por fecha). El **sugeridor actual NO muere**: queda como fallback
  documentado cuando falten bandas.

## Anclajes verificados (yo, contra main 943ce0d — no de memoria)

1. **El grafo YA sabe qué implica cada tarea.** `lib/engine/graph.ts` define
   `pasos_accionables?: string[]` y `entregable_esperado?: string` por nodo, y
   `lib/engine/planRedactor.ts:57-58` los lee (`pasos: n.pasos_accionables`,
   `entregable: n.entregable_esperado`). → **La Capa 1 (estimación) tiene su
   materia prima sin inventar nada.**
2. **`project_modos` es la casa de la capacidad por espacio** (migración 032:
   `(project_id, dominio, modo_camino)` con RLS). → añadir `capacidad_semanal`
   ahí es natural; ya es el hogar del "cómo se lleva" cada espacio.
3. **La Capa 3 (aprendizaje) está embrionaria:** `diaDominante` y
   `cadenciaRealSemanas` viven en `lib/fechasBase.ts`. El multiplicador por banda
   se suma a esa capa, no la inventa.
4. **La bitácora tiene el molde `{tipo, payload}`** (ruta `/modo` escribe
   `tipo:'modo_camino', payload`): `banda_corregida {de, a}` calza sin tabla nueva.

## Arquitectura — tres capas honestas (resumen del spec)

- **Capa 1 — ESTIMACIÓN (LLM, una vez, al nacer el plan):** cada acción → una
  **banda** S/M/L/XL (rangos honestos, JAMÁS horas numéricas) + **espera externa**
  sí/no. El usuario puede corregir (su corrección es oro de calibración).
- **Capa 2 — EMPAQUETADO (determinístico, puro, testeable a mano):** bandas +
  capacidad semanal del espacio + reglas duras (etapas = puertas; dentro de la
  etapa se llenan semanas contra la capacidad) → fechas que respiran. Cero IA en
  runtime: mismo input → mismas fechas.
- **Capa 3 — APRENDIZAJE:** `diaDominante` + `cadenciaReal` + el **multiplicador
  personal por banda** (M reales vs estimadas), aplicado SOLO en recálculos.

---

## FASE 0 — EL SPIKE DE ESTIMACIÓN (la puerta de todo; SIN tocar producción)

La factibilidad de TODA la campaña depende de que el modelo clasifique en bandas
con concordancia alta. Se mide ANTES de construir nada.

- **`scripts/spike_estimacion.ts`** (script, no producción): toma **30-40 tareas
  reales** de los planes del fundador (concepto + `pasos_accionables` +
  `entregable_esperado`), **variadas entre etapas y mundos**. El modelo del motor
  clasifica cada una en **banda S/M/L/XL + espera_externa sí/no**.
  - **Prompt de sistema con las bandas por RANGOS:** "S: cabe en una sentada de
    ≤1 h; M: 2-4 h; L: una jornada; XL: varios días". **Prohibido devolver horas
    numéricas.**
  - **3 corridas por tarea**; mide **concordancia inter-corrida** (% banda exacta,
    % adyacente) y saca un **reporte `.md`** con la **matriz de discordantes** para
    el juicio del fundador (**PM certificado = estándar de oro**).
- **PUERTA:** **>80% exacta-o-adyacente → abre F1**; menos → **itera el prompt** o
  **degrada a 3 bandas** y re-mide.
- **Costo real reportado** (<$1 esperado). **La corrida en vivo la dispara el
  fundador** (llama al LLM).
- **CHECKPOINT:** el reporte al fundador; su veredicto abre F1.

## FASE 1 — LA ESTIMACIÓN NACE CON EL PLAN

1. **Migración 033** (SQL al fundador; se espera su "aplicada" antes del vuelo):
   - `checklist_items` += `banda text NULL`, `espera_externa boolean NULL`.
   - `project_modos` += `capacidad_semanal text NULL` (chips `'2-5'|'5-10'|'10-20'|'20+'`).
   - CHECK nombrados (patrón dbContract): `banda IN ('S','M','L','XL')`,
     `capacidad_semanal IN ('2-5','5-10','10-20','20+')`. Bloque en
     `my_idea_check_migraciones.sql`. Arrays en `dbContract.ts` (+ test que parsea).
2. **Al nacer TODO plan nuevo (core y mundo):** una **llamada batch de estimación**
   (JSON estricto `id → {banda, espera_externa}`) **DESPUÉS del plan** (la **prosa
   del plan NO se toca**); persistida en los ítems. **Fallo de la llamada = ítems
   sin banda** (fallback declarado, **jamás bloquea el plan**).
3. **El detalle de la tarea** muestra la banda como **rango honesto** ("~2-4 h")
   con **selector de corrección** → evento bitácora **`banda_corregida {de, a}`**
   (telemetría de oro).
4. **Planes viejos sin banda:** **sin rango mostrado, cero invención.**
- **Tests:** el parser del batch, la persistencia, el evento de corrección.
- **CHECKPOINT.**

## FASE 2 — LA CAPACIDAD Y EL EMPAQUETADO (el corazón)

1. **El ritual de fechas de CADA espacio** gana la pregunta: **"¿Cuántas horas por
   semana puedes darle a este espacio?"** (chips, **default `5-10`**, editable
   después desde el panel de fechas). Se guarda en
   `project_modos.capacidad_semanal` del espacio.
2. **`lib/empaquetado.ts` PURO:**
   - **Input:** `items(banda, espera_externa, etapa, destacado)` + capacidad + ancla
     (`plan.created_at`) + `diaDominante`.
   - Constantes **nombradas** `HORAS_MEDIA = {S:1, M:3, L:8, XL:16}` (con comentario).
   - **Reglas:** etapas como **puertas** (la N+1 arranca donde el empaquetado cerró
     la N); dentro de la etapa se **llenan semanas contra la capacidad** (overflow →
     semana siguiente); la **entrega de cada tarea = el `diaDominante` (viernes
     default) de SU semana empaquetada**; la **destacada = el lunes de la primera
     semana de su etapa**.
   - **Determinístico; tests con aritmética A MANO:** el usuario de 3 h vs el de
     20 h sobre el mismo plan (los dos calendarios calculados a mano); una etapa que
     **desborda a 2 semanas**; **regresión del caso sin bandas → `sugerirFechasBase`
     actual como fallback INTACTO**.
3. **"Con fechas" y "Recalcular pendientes"** usan el empaquetado **cuando hay
   bandas**; el **Gantt honesto ya dibuja lo que salga**.
- **Vuelo:** la fase de fechas con la contabilidad nueva a mano.
- **ADDENDUM (verificación de la tubería de calendario):** el vuelo incluye el
  **assert de punta a punta** — tras empaquetar, el **ICS/feed exporta las fechas
  empaquetadas tal cual**: una tarea **S** y una **XL** de la misma etapa caen en
  **semanas distintas** si la capacidad lo dicta, y sus eventos las reflejan con su
  **UID estable** y su **etiqueta de espacio**. **Cero trabajo nuevo esperado** (el
  calendario lee `fecha_base`, donde el empaquetado escribe): el assert existe para
  **custodiar esa herencia gratuita, no suponerla**.
- **CHECKPOINT + gate:** ritual con la pregunta · detalle con rangos · Gantt
  respirando por capacidad.

## FASE 3 — LAS ESPERAS EXTERNAS

En el empaquetado, **`espera_externa=true`** fija **inicio temprano en su etapa** y
**entrega +1 semana de lead** (constante nombrada **`LEAD_ESPERA_SEMANAS = 1`**). El
detalle lo dice en persona: *"esta tarea espera respuesta de terceros: empiézala
temprano"*. **Tests a mano del corrimiento.** **CHECKPOINT.**

## FASE 4 — EL MULTIPLICADOR PERSONAL

**`factorPorBanda`** (completed_at reales vs banda estimada, **por espacio**, mínimo
**3 muestras por banda**) aplicado **en los RECÁLCULOS** (**jamás re-fecha lo no
tocado**); se suma a `diaDominante`/`cadenciaReal` como el aprendizaje de la casa.
**Tests:** el usuario cuyas **M** tardan el doble → su recálculo lo refleja; sin
muestras suficientes → **factor 1 (cero invención)**. **CHECKPOINT.**

## CIERRE

- **BANCO §7.1 — doctrina del scheduler:** *"las bandas son rangos honestos del
  grafo, corregibles por el usuario; el empaquetado es determinístico y se audita a
  mano; la capacidad es por espacio; el aprendizaje solo re-fecha lo que el usuario
  pide recalcular."*
- **Matriz de PENDIENTES al día**; **encargo de Design** (la pregunta de capacidad,
  los rangos en el detalle, la corrección de banda); **tag menor**.
- **El sugeridor viejo queda como fallback documentado, jamás muere.**

## Riesgos y mitigaciones (del spec §4)

1. **Consistencia del LLM al estimar** → bandas gruesas (4 opciones) + el SPIKE F0.
2. **Falsa precisión percibida** → SIEMPRE rangos ("~2-4 h") + derecho a corregir.
3. **Fricción de UX** → una sola pregunta con chips + default sensato + editable.
4. **Coste** → centavos por plan, una vez; el empaquetado es gratis.
5. **El sugeridor actual NO muere** → fallback si falta la banda (planes viejos).

## Archivos críticos (previstos)

- Spike: `web/scripts/spike_estimacion.ts` (+ reporte en `web/examples/`).
- Migración: `supabase/migrations/my_idea_033_scheduler.sql`, `my_idea_check_migraciones.sql`,
  `web/lib/dbContract.ts` (+ `.test.ts`).
- Estimación: la ruta/composer del plan (batch tras el plan), `web/lib/engine/…`.
- Empaquetado: `web/lib/empaquetado.ts` (+ `.test.ts`) — puro, aritmética a mano.
- Capacidad/UI: `web/app/ui/ManosALaObra.tsx` (la pregunta en el ritual, el detalle
  con rangos + corrección), `web/app/api/project/[id]/modo/route.ts` (capacidad).
- Fechas: `web/lib/fechasBase.ts` (fallback intacto), Capa 3 (`factorPorBanda`).
- Verificación: `web/scripts/vuelo.ts` (fase de fechas + addendum ICS), `gate_beta.ts`.

## Verificación (regla de la casa)

1. **F0 primero, sin producción:** el spike + su reporte; puerta >80%.
2. **Migración 033** aplicada por el fundador; `check_migraciones` verde.
3. **Empaquetado con aritmética A MANO** en los comentarios antes del assert
   (regla AGENTS.md); el caso 3h vs 20h calculado a mano.
4. **Regresión:** sin bandas → `sugerirFechasBase` actual, intacto.
5. **Vuelo + addendum ICS** (fechas empaquetadas → eventos con UID estable + etiqueta).
6. **Gate** de la pregunta, los rangos y el Gantt respirando; costos reales; tag menor.
