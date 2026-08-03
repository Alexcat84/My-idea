# Plan — "La idea completa": el nivel GENERAL sobre los espacios

Estado: **propuesta, pendiente del visto del fundador y del auditor.** 0 líneas de
código hasta la aprobación. (Redactado 2026-08-03. Sucede a la campaña "Espacios"
Fase 3, tag `web-v2.0.0-beta`.)

## 0. La tensión que lo motiva

Tras la Fase 3, hay control **específico por espacio** (el core y cada mundo tienen
su Plan · Manos · "Tu avance" con hitos + estadísticas + bitácora) — simétrico en el
hub ([`ManosALaObra.tsx:1361`](../web/app/ui/ManosALaObra.tsx#L1361)). Pero el nivel
que llamamos "general" **es en realidad el core**: el cuerpo del Análisis del proyecto
(ritmo, racha, series, cumplimiento) es **solo core**
([`analytics.ts:476-478`](../web/lib/analytics.ts#L476)); la sección "Tu proyecto
completo" (Fase 3, tanda 4) **declara la composición** (core + N mundos, suma de X de
N) pero **no es un agregado real** de ritmo/racha/timeline.

Diagnóstico del fundador (exacto): *el core juega dos papeles* — es un espacio (con
sus vistas) **y** el implícito "proyecto". Falta un nivel **por encima** de los
espacios que sea de verdad "la idea completa, unificada".

## 1. El modelo (refinado por el fundador)

- **El núcleo (core) NO es un espacio más ni una card igual.** Es el corazón de la
  idea, **marcado como tal**, con **sus propios registros** (plan, manos, avance,
  bitácora). Pero **sí cuenta dentro del total** general.
- **Encima del núcleo hay un control GENERAL** que **se activa cuando aparece otro
  mundo** (misma regla de RUIDO CERO que ya dispara el cambiador,
  [`IdeaView.tsx:860`](../web/app/idea/[id]/IdeaView.tsx#L860)). Solo-core: no existe
  el nivel general; estás en tu núcleo y punto.
- **"Lo general" = el AGREGADO de toda la idea**, COMPARTIDO: total, ritmo unificado,
  racha unificada y timeline unificada. Es la **suma de los espacios**, y como la
  partición de la Fase 3 es exacta, esa suma **no dobla conteo**.
- **Cada espacio conserva sus registros propios**; lo de arriba es lo general.

## 2. Garantías (para el auditor)

- **Agregado sin doble conteo.** El total de la idea = Σ de la partición exacta (cada
  acción en exactamente un espacio, Fase 3). Ninguna acción se cuenta dos veces;
  ninguna se omite. El núcleo es un sumando más del total (aunque en la UI vaya
  distinguido).
- **Lo POR ETAPA no se unifica** (a propósito). "Etapa 1" significa cosas distintas en
  cada espacio; sumarlas mentiría, y ya el motor evita esa colisión
  ([`analytics.ts:472-475`](../web/lib/analytics.ts#L472)). El agregado solo une lo
  **agnóstico al espacio** (total, ritmo = hechas/semanas, racha = sobre fechas
  unidas, timeline). Los gráficos por etapa se quedan **por espacio**, en cada hub.
- **Ruido cero.** El nivel general (pantalla + control) **solo existe con ≥1 mundo**.
  Un proyecto solo-core se ve idéntico a hoy.
- **Una fuente, muchas lecturas.** El agregado es una LECTURA derivada de los mismos
  datos (partición + analytics ya calculado); cero registros paralelos.

## 3. Qué ya sirve / qué falta

**Ya sirve (la base ya está puesta):**
- La **partición exacta** (Fase 3): habilita el agregado honesto.
- `analytics.universal` (registros del núcleo) + `analytics.mundos[]` (cada mundo) ya
  separados; `analyticsDeMundo` y `resumenEspacioMd` reusables.
- `proyectoTieneMundos` / `mundosParaObra.length > 0` = el disparador de ruido cero.
- `CambiadorEspacios` = el control de espacios; el control general cuelga aquí.
- `rachaMasLarga` (analytics.ts, privado) = ya calcula la racha sobre una lista de
  fechas; el agregado la reusa sobre la unión.
- La **bitácora global** (todas las entradas, etiquetadas por espacio) = la timeline
  unificada, ya como dato.

**Falta (lo nuevo):**
- Una función pura **`agregadoDeIdea`** (el motor del nivel general).
- La pantalla **"La idea completa"** y su **control** en el cambiador (ruido cero).
- Registrar el vocabulario en el **BANCO §7.1** antes de pintar.

## 4. El agregado — contrato de `agregadoDeIdea`

Función PURA nueva en `analytics.ts` (cero LLM, cero costo). Firma tentativa:
`agregadoDeIdea(entrada: EntradaAnalytics, analytics: Analytics): AgregadoIdea`.

Devuelve:
- `duracionTotalDias`: de la chispa (proyecto) a `fin` (realizada o ahora).
- `total: { hechas, total }`: **Σ** de `accionesVigente` de cada espacio (núcleo +
  cada mundo) — cada acción de su plan vigente activo, contada una vez.
- `ritmoUnificado`: `total.hechas / semanas(duracionTotalDias)` (recalculado, **no** la
  suma de ritmos por espacio, que tendrían denominadores distintos).
- `rachaUnificada`: `rachaMasLarga(unión de completed_at contados)` — la constancia de
  toda la idea, sobre las fechas de las acciones que entran al total.
- `espacios: Array<{ dominio; nombre; nucleo: boolean; hechas; total; cerrado }>` — el
  desglose (núcleo primero, marcado), para las tarjetas.
- La **timeline unificada** se toma de la bitácora global existente (no se recalcula).

**Dominio de ritmo/racha — CERRADO: vigente-activo.** Las tres métricas del agregado
(total, ritmo, racha) salen del **MISMO universo**: las acciones **activas del plan
vigente** de cada espacio. **Por qué:** así son **auditables entre sí** (la racha y el
ritmo miden sobre exactamente lo que suma el total); el histórico (ciclos viejos) ya
vive en la bitácora y en la línea "frente a tu plan inicial" del cumplimiento.

**Precisión de la racha unificada (tanda 1):** la unión de `completed_at` respeta la
**vigencia POR ESPACIO** — de cada espacio entran solo los ítems de su plan vigente
(`grupoVigente` por dominio en los mundos; el plan vigente del core para el núcleo).
Luego se aplica `rachaMasLarga` sobre esa unión. **Test a mano obligatorio:** un caso
donde una fecha de un MUNDO **extiende** una racha que el core solo no tendría (la
prueba de que la unión es real, no la racha del core disfrazada).

## 5. Las tandas (commits "Idea completa:")

### Tanda 0 — Gobierno (antes de pintar)
- **Enmienda BANCO §7.1**: fija el vocabulario — *el núcleo es el corazón (marcado,
  con registros propios) y cuenta en el total; el nivel GENERAL aparece con ≥1 mundo y
  es el agregado compartido de toda la idea, suma sin doble conteo; lo por-etapa no se
  unifica.* El banco lidera; la pantalla lo sigue.

### Tanda 1 — El agregado (motor puro + tests)
- `agregadoDeIdea` en `analytics.ts` (contrato §4).
- Tests (cálculo a mano ANTES del assert, regla AGENTS.md): **sin doble conteo**
  (Σ espacios = total, cada acción una vez); ritmo unificado = hechas/semanas; racha
  unificada sobre la unión; el borde solo-core (agregado trivial, la pantalla lo gatea).
- Sin migración, sin cambio de API.

### Tanda 2 — La pantalla "La idea completa" + el control (ruido cero)
- Vista nueva `?vista=idea` en el despacho de `IdeaView.tsx` (patrón de `?vista=analisis`).
- Componente nuevo `IdeaCompleta.tsx`: la **banda general** (tiles del agregado, reusa
  `Tile`) + la **timeline unificada** + el **núcleo distinguido** (con sus registros
  propios y link a su hub) + las **tarjetas de mundo** (instantánea + link). Reusa
  `EstadisticasEspacio`/`resumenEspacioMd` donde aplique.
- **El control**: una entrada **"La idea completa"** al frente de `CambiadorEspacios`,
  distinguida (es el agregado, no un espacio), gated por `≥1 mundo` (ruido cero). Al
  seleccionarla → `?vista=idea`.
- Navegación en `IdeaView` (irAIdeaCompleta), deep-link, "Volver" coherente.
- **Documento**: por defecto, "La idea completa" enlaza al **Expediente/Análisis
  global** ya existentes como su documento unificado (el Expediente ya trae el núcleo +
  cada mundo completos, Fase 3 tanda 5). Sin documento nuevo. (Ver decisión abierta 3.)

### Cierre — verificación
- Extender `gate_beta.ts`: capturar `?vista=idea` (el nivel general) en dos viewports,
  y confirmar que **NO aparece** en un proyecto solo-core (ruido cero, ambos sentidos).
- Suites verdes en clon limpio; tag menor. Autopush a staging por tanda; **merge a main
  solo con autorización del fundador.**
- **Vuelo**: la navegación gana una entrada/vista, pero no toca la contabilidad de
  dinero; el vuelo de dinero no aplica. (Se anota.)

## 6. Archivos que se tocan (referencia)
- **Motor (puro, testeado):** `web/lib/analytics.ts` (`agregadoDeIdea`) + `analytics.test.ts`.
- **UI:** nuevo `web/app/ui/IdeaCompleta.tsx`; `web/app/ui/CambiadorEspacios.tsx` (la
  entrada general); `web/app/idea/[id]/IdeaView.tsx` (vista + navegación).
- **Gobierno:** `docs/BANCO_DE_TEXTOS.md §7.1`.
- **Verificación:** `web/scripts/gate_beta.ts`.
- **Migración:** **ninguna.**

## 7. Fuera de alcance
- Unificar lo **por etapa** (se queda por espacio, a propósito).
- Un documento nuevo de "idea completa" (default: reusar el Expediente; ver decisión 3).
- ETAPA 3 (pasarelas) y las varas de Design de la Fase 3 (encargo aparte).

## 8. Decisiones CERRADAS (visto del fundador, 2026-08-03)
1. **El control** = una **entrada al frente del cambiador, distinguida**. **Jamás un
   tercer riel de navegación.**
2. **Qué se unifica** = total + ritmo + racha + timeline. **Lo por-etapa jamás.**
3. **Documento** = **reusar el Expediente/Análisis global**, sin documento nuevo (dos
   documentos casi-iguales esperan divergir; no se crean por crear).
4. **Dominio de ritmo/racha** = **vigente-activo**, con el porqué documentado (§4): las
   tres métricas salen del mismo universo que el total → auditables entre sí; el
   histórico ya vive en la bitácora y en "frente a tu plan inicial".
