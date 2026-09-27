# ARQUITECTURA DEL BUCLE DE TRACKING — My Idea
El flujo canónico del bucle de seguimiento. Estado: al día con el código tras la
Fase 2 del ciclo de replanteamiento (27 sep 2026,
`docs/producto/CICLO_REPLANTEAMIENTO.md`). La tabla del §7 dice qué existe.

## 0. EL PRINCIPIO RECTOR
El proyecto tiene UNA sola verdad (lo persistido) y DOS espejos que la leen:
- **El Análisis** es el espejo para el humano.
- **Los ciclos (profundizar y replantear) son el espejo para el motor.**
Ambos beben de la misma agua: `analytics.ts`. Si el humano puede ver que la
etapa 2 tardó tres semanas de más, el motor que regenera el plan TIENE que
saberlo también. Un motor que replanifica sin conocer la desviación no es un
director de proyectos: es un generador con amnesia.

## 1. EL BUCLE COMPLETO (el ciclo de vida de un plan)

```
[1] PLAN nace (core o mundo)
      -> checklist derivado (ítems con etapa, orden, destacado)
[2] MODO DEL CAMINO (primera vez por idea)
      -> "A mi ritmo": sin fechas base
      -> "Con fechas": sugeridor determinístico -> ritual -> baseline
         confirmada (plans.baseline_confirmada_at)
[3] EJECUCIÓN (semanas; cero API, cero costo)
      -> estados de un toque + "Marcar hecho" con completed_at real
      -> notas por ítem
      -> replanificaciones (fecha_base_original preserva la historia)
[4] SEÑALES ACUMULADAS (nadie las pide; se acumulan solas)
      -> cumplimiento por ítem (a tiempo / adelantada / tardía)
      -> desviación media, ritmo, racha, días sin avance
[5] DOS ENTRADAS en Manos a la Obra (§2), cada una con su ritual:
      a. "Profundizar mi plan" (todo va bien, ir más hondo): 3 tarjetas
         -> 1 "Tu avance": ¿el checklist ya refleja lo que hiciste?
            (adaptada al avance real, §4)
         -> 2 qué más pasó (texto/voz, opcional)
         -> 3 el enfoque del siguiente tramo ("No estoy seguro" es opción
            legítima: el motor decide)
         -> entrevista nueva de seguimiento, luego el plan
      b. "Replantear mi camino" (algo cambió o se rompió): 4 pasos, sin
         entrevista
         -> 1 tu historia (OBLIGATORIA, texto/voz, preguntas de ayuda)
         -> 2 lo que ya construiste: cada tarea hecha, "me sigue sirviendo"
            o "ya no aplica"
         -> 3 caminos posibles: 2 o 3, propuestos por la IA (SYSTEM_CAMINOS),
            cada uno anclado a conceptos del grafo aún no cubiertos
         -> 4 confirmar y generar (resumen, precio, promesa de cobro)
[6] EL CICLO COMPONE para el motor (los dos):
      estados + notas + lo que escribió la persona
      + EL BLOQUE DE REALIDAD (§3)
      + EL PLAN ANTERIOR (etapas y tareas con su estado, regla 8-ter)
      + al replantear: historia, lo que se conserva, lo que se suelta y el
        camino elegido (regla 8-quater)
[7] EL MOTOR REGENERA
      -> plan nuevo que PARTE de lo que pasó y construye encima del anterior:
         no repite lo hecho, no vuelve a proponer lo retirado ni lo soltado,
         asume las desviaciones sin regaño ("la etapa 2 tomó más de lo
         previsto; este ciclo asume tu ritmo real")
      -> la cosecha del vecindario excluye lo que el proyecto ya cubrió
[8] NUEVO CICLO
      -> checklist nuevo: al profundizar, todo nace pendiente; al replantear,
         lo que "me sigue sirviendo" entra HECHO, con su fecha y su nota
         (`checklist_items.heredado_de`, migración 047; no cuenta dos veces)
      -> el plan anterior queda en la Historia de Manos a la Obra (núcleo y
         cada mundo) con sus tareas hechas y lo que la persona contó
      -> lo escrito queda en la bitácora (evento `ciclo_profundizado` o
         `ciclo_replanteado`) y de ahí en el Expediente
      -> el sugeridor de fechas del ciclo N+1 usa el ritmo personal
         (multiplicador del Scheduler F4)
      -> vuelta a [3]
[9] CIERRE: "Marcar como realizada" -> Celebración -> Analytics final
```

## 2. LAS PUERTAS (un solo lugar, dos entradas)
- Los ciclos viven en **Manos a la Obra** y en ningún otro sitio, con **dos
  entradas separadas** (decisión del fundador, 27 sep 2026): **"Profundizar mi
  plan"** y **"Replantear mi camino"**. En el núcleo y en cada mundo abierto.
- La pantalla del plan es un DOCUMENTO, no una puerta: se lee, se descarga,
  se navega a Manos. Ningún botón de "ajustar el plan" ahí: ajustar sin
  haber ejecutado es regenerar, y regenerar no es el producto.
- Las dos entradas están SIEMPRE disponibles (ver sección 4) mientras la idea
  o el mundo sigan abiertos, porque el seguimiento es un acto de ejecución,
  no de lectura.
- Las dos pasan por las mismas puertas del servidor (`lib/cicloApertura.ts`:
  cuenta real, doble factor, idea realizada, muros del mundo, saldo, reserva,
  fusible y límite diario): `POST /api/project/[id]/follow` y
  `POST /api/project/[id]/replantear`.

## 3. EL BLOQUE DE REALIDAD (lo que el follow DEBE entregar al motor)
Calculado por `analytics.ts` (la única fuente; jamás recalcular aparte),
compacto y determinístico, adjunto al mensaje del follow:

- **Resumen de cumplimiento** (solo si hubo baseline confirmada):
  a tiempo / adelantadas / tardías con conteos, y desviación media en días.
- **Las tardías que importan**: los 3-5 ítems más desviados, con sus días
  de retraso y su etapa (el motor debe saber DÓNDE se atora el usuario).
- **Replanificaciones**: cuántos ítems movieron su fecha y cuáles (señal de
  que la línea base original era irreal o que la vida cambió).
- **Ritmo real**: acciones por semana, racha más larga, días desde el
  último avance (un usuario que no toca el checklist en 30 días es un
  contexto distinto al que avanza a diario).
- **Modo del camino**: si es "a mi ritmo", el bloque lleva SOLO duraciones
  y ritmo, sin lenguaje de cumplimiento (no se juzga contra fechas que el
  usuario eligió no tener).
- **Ciclo**: número de ciclo, fecha del plan vigente, días de vida del plan.

Regla de tono para el motor (espejo, jamás regaño, también puertas adentro):
el prompt del follow instruye que las desviaciones se ASUMEN y ajustan el
plan, nunca se reprochan. "Vas tarde" está prohibido; "este ciclo asume tu
ritmo real" es el canon.

## 4. EL CASO AVANCE-CERO (decisión de producto)
Ninguna de las dos entradas exige avance mínimo. Razón: la realidad cambia antes de
ejecutar (el proveedor quebró, el local se perdió, apareció un competidor,
el usuario se enfermó), y replanificar ante eso es método legítimo, no
abuso. PERO el ritual se ADAPTA al avance:
- Profundizar, con avance > 0: la tarjeta 1 ("Tu avance") muestra el
  progreso del checklist.
- Profundizar, con avance = 0: la tarjeta 1 cambia de pregunta: no "llevas 0
  de 28" (absurdo y desmoralizante) sino "¿Aún no arrancas? Cuéntame qué
  cambió desde que armamos el plan". Misma puerta, encuadre honesto.
- Replantear, sin nada hecho: el paso 2 lo dice con una línea amable y deja
  seguir; la historia sigue siendo obligatoria.
El anti-abuso no es un gate artificial: es el precio del seguimiento (el de
`precios.ts`) más el límite diario vigente. Regenerar por deporte cuesta;
replanificar por realidad vale cada crédito.

## 5. EL COBRO (dónde encaja cuando el frente de cuentas despierte)

**El principio que gobierna (palabra del fundador, 2026-07-17):** *el crédito
paga el trabajo del motor. Toda acción que invoca la API para pensar cobra su
precio de catálogo; el cálculo determinístico y el registro de avance son
gratis, siempre.* Aplicado:
- Plan core (La Exploración): **10**
- Profundizar mi plan (concepto `seguimiento`): **5** · en un mundo
  (`mundo_seguimiento`): **5**
- Replantear mi camino (concepto `replanteamiento`): **5** · en un mundo
  (`mundo_replanteamiento`): **5**. Los caminos del paso 3 van dentro de ese
  mismo cobro (y cuentan para el fusible y el límite diario). Claves propias
  para poder moverlas por separado cuando se mida su coste real (abajo).
- Plan de un mundo (su preview es gratis): **5**
- **Tus Números: incluido en el plan** (activación una vez por idea, sin cobro),
  con sus recálculos determinísticos ilimitados y sus re-narraciones (con el
  límite diario como freno). Corregir cifras y recalcular **jamás** cobra. Tus
  Números **no tiene "seguimiento"**: no es un plan, es una calculadora viva.

> **Corrección de la AUD-09 (25 sep 2026):** esta lista decía 5 / 2 / 3 / 2 y
> "Tus Números: 2", las cifras de antes del Catálogo congruente. Se alinea con
> `web/lib/precios.ts`, la única fuente (ver `AGENTS.md`).
- Gratis siempre: el organizador (Claridad), marcar avance en el checklist,
  mover fechas, escribir notas, y todo cálculo de la calculadora determinística.

La fuente de verdad de las cifras es `web/lib/precios.ts`; este documento y el
canon visual las **reflejan**, jamás las definen (ver `AGENTS.md`).

- Los dos ciclos cobran, core y mundo, al precio de su concepto en
  `precios.ts` (`conceptoDelPlan(dominio, true, esReplanteamiento)`).
- El patrón, VIVO desde la ETAPA 2: al abrir el ritual la pantalla pregunta
  si alcanza (GET de `follow` o de `replantear`, que solo mira); al empezar
  (el POST) se verifica el saldo y se APARTA el precio con la clave
  `plan:{sesión}` (migración 042); se DESCUENTA A LA ENTREGA del plan nuevo
  (`session/[id]/plan`, idempotente por esa clave); cero cobro si el sistema
  falla a mitad, y lo apartado se suelta. Al replantear, volver atrás y pedir
  caminos otra vez suelta la reserva de la vuelta anterior, con un tope de 3
  vueltas por replanteamiento (decisión del fundador, 28 sep 2026): la 4.ª se
  rechaza con un mensaje claro y la vuelta anterior queda intacta para elegir.
- **Cómo medir el coste real** (pedido del fundador): cada sesión guarda su
  `costo_usd` y su desglose por componente (`costo_desglose`); la de un
  replanteamiento incluye sus caminos. En el SQL Editor:

  ```sql
  SELECT p.etiqueta, COALESCE(s.dominio, 'core') AS espacio, p.created_at,
         s.costo_usd, s.costo_desglose
  FROM plans p JOIN sessions s ON s.id = p.session_id
  WHERE p.etiqueta IN ('seguimiento', 'replanteamiento')
  ORDER BY p.created_at DESC
  LIMIT 20;
  ```
  Con 1 crédito = 1 USD como ancla del ledger, `costo_usd` se compara
  directo contra los 5 créditos de cada ciclo.
- **Solo se cobra lo entregado (decisión del fundador, 25 sep 2026):** un
  plan armado sin IA (el ensamblado sin narrar, cuando la conversación llegó
  a su tope de trabajo) se entrega gratis, marcado como versión básica y con
  un aviso honesto en pantalla. El detalle vive en `docs/ANALISIS_PRECIOS.md`
  §4, "Cuándo se cobra: solo lo entregado".

## 6. REGLAS TRANSVERSALES
- `analytics.ts` es la única calculadora del tiempo: Análisis, Celebración,
  follow y (futuro) notificaciones leen de ahí. Prohibido duplicar lógica.
- La historia no se reescribe: replanificar preserva la original; el ciclo
  nuevo no borra el cumplimiento del viejo (el Análisis muestra la vida
  completa del proyecto, ciclo a ciclo).
- La baseline vigente es la del último plan con baseline confirmada; las
  históricas se conservan para el Análisis.
- El modo del camino es reversible y cada cambio queda en project_bitacora.

## 7. ESTADO ACTUAL vs OBJETIVO (los huecos, verificados jul 2026)
Verificado contra el código el 27 sep 2026 (Fase 2 del ciclo de
replanteamiento). Esta tabla decía que el bloque de realidad, el caso sin
avance y el cobro del follow no existían: los tres ya estaban hechos.

| Pieza | Estado |
|---|---|
| Ciclos en Manos a la Obra, núcleo y mundos | ✓ dos entradas: Profundizar mi plan y Replantear mi camino |
| "Ajustar el plan" en la pantalla del plan | ✓ eliminado: la pantalla del plan es un documento |
| El ciclo consume estados + notas + texto | ✓ `componerMensajeSeguimiento` / `componerMensajeReplanteamiento` |
| El ciclo consume el BLOQUE DE REALIDAD (§3) | ✓ `realidadDelCiclo` (lib/cicloApertura.ts) sobre `analytics.ts` |
| Ritual adaptado a avance-cero (§4) | ✓ la tarjeta 1 cambia de pregunta sin avance |
| Cobro de los ciclos (§5) | ✓ vivo: reserva al empezar, descuento a la entrega |
| El redactor recibe el plan anterior | ✓ `plan_anterior` en el payload (regla 8-ter de SYSTEM_PLAN) |
| La cosecha excluye lo ya cubierto | ✓ `cosecharVecindario(..., excluir)` en TS y en Python (la regla 8 lo prometía) |
| Lo que escribe la persona queda registrado | ✓ evento `ciclo_profundizado` / `ciclo_replanteado`, pintado en la bitácora, el Expediente y la Historia |
| Lo hecho no se pierde | ✓ la Historia muestra las hechas de cada plan anterior; al replantear, lo que sirve entra hecho (`heredado_de`) |
| Sugeridor N+1 aprende del ritmo real | ✓ multiplicador personal del Scheduler F4 |
| Acta de cierre (§8) | ✓ `project_actas` (migración 040) y `cierre_motivo` |

## 8. EL ACTA DE CIERRE (adenda del fundador: el cierre es soberano y ahora
también documentado)

Cerrar una idea es un acto del usuario, no un premio del sistema: no exige el
100% del checklist y nunca lo exigirá. Pero un cierre sin memoria del porqué
pierde la mitad de la historia. El acta la conserva.

- **Persistencia**: `projects.cierre_motivo` (text, null). El evento
  `realizada` de `project_bitacora` amplía su payload a `{accion, motivo}`.
- **El diálogo de "Marcar como realizada"** se vuelve un mini-ritual honesto
  de dos elementos:
  (a) **el espejo del momento**: "Llevas X de N acciones (Z%)" con sus números
      reales, sin juicio;
  (b) **campo OPCIONAL** (texto/voz): "¿Por qué la cierras aquí? (para tu
      propia memoria)".
  Cero fricción: se puede cerrar sin escribir nada, como hoy.
- **Dónde aparece el motivo** (donde la historia se cuenta): bajo el hito
  REALIZADA del timeline de la Celebración (discreto, en la voz del usuario),
  en el Análisis, y en el informe `.md` exportado, que cuando el proyecto está
  realizado gana su sección **"Acta de cierre"** (estado final, motivo del
  usuario, y las estadísticas completas).
- **Reabrir NO borra el motivo** (la historia no se reescribe): queda en la
  bitácora. Si el usuario vuelve a cerrar después, el motivo nuevo se registra
  junto al anterior; el Análisis puede mostrar la secuencia.
- **Los ítems pendientes al cierre no se tocan**: ni cambian de estado ni se
  marcan. Quedan como testigos honestos en la Historia (las notas por ítem ya
  existen para documentar casos puntuales como "no se pudo ejecutar completa,
  entregable aceptable").

## 9. LOS MUNDOS COMO SUBPROYECTOS COMPLETOS (Fase 4.2)

Decisión del fundador: **cada mundo tiene su propio seguimiento y su propio
cierre, con los mismos parámetros que el viaje principal**. Un mundo se
exploraba, se planificaba y se ejecutaba con su checklist, pero no podía ni
replanificarse ni terminar: quedaba abierto para siempre.

La regla que ordena toda la fase: **un mundo es un subproyecto, no una versión
recortada del viaje principal.** De ahí sale todo lo demás — el mismo ritual, la
misma capa de métricas, el mismo tipo de acta.

### 9.1 El follow de mundo

`POST /api/project/[id]/follow` (profundizar) y `POST /api/project/[id]/replantear`
reciben `dominio`. Sin él, es el ciclo del núcleo. Con él, **todo lo que depende
del dominio se mueve con él** (al replantear, los caminos se anclan a conceptos
de ese mundo y el plan anterior es el del mundo):

| Qué | Cómo |
|---|---|
| Los ítems del mensaje | `itemsDelUltimoPlanDe(filas, dominio)` — los del último plan **de ese mundo** |
| El bloque de realidad | `construirBloqueRealidadMundo` — el cumplimiento **del mundo** contra **sus** fechas, más **UNA** línea de contexto global, rotulada |
| La puerta | `seleccionarPuertaAvanzada` amurallada a los nodos del mundo |
| La sesión | nace con `dominio=mundo` → su plan hereda el dominio y deriva checklist con él, encadenado en el grupo de ese mundo |

**Lo que NO se mueve, a propósito:** la cosecha del vecindario sigue amurallada a
`core + unlocks`, igual que en el plan original del mundo (`world/start:122`). El
mundo no vive en el vacío: se construye sobre la idea.

**Por qué la puerta la elige el intérprete y no `evaluacionBrecha`** (que es lo
que hace `world/start`): en un seguimiento el mensaje **ya trae la realidad
medida**, y esa es justo la señal con la que se debe elegir por dónde entrar. Es
el mismo trato que recibe el core. Con un guardián: sin candidatos del mundo,
`seleccionarPuertaAvanzada` caería a `entrySeeds[0]` — un nodo **core** — y el
plan del mundo saldría explorando el viaje principal. Antes que eso, un 409 que
dice la verdad.

**La regla que el bloque de mundo existe para cumplir:** jamás presentarle al
motor las tardanzas del core como si fueran del mundo. Del proyecto entra una
sola línea, y va rotulada ("Contexto de mi proyecto (NO de este mundo)"). Sin esa
línea el motor planificaría el mundo como si el resto de la vida del usuario no
existiera; con más de una, volvería a confundirlos.

El caso **avance-cero** (§4) y el **tono 8-bis** ("este ciclo asume tu ritmo
real") aplican igual: son del ritual, no del core.

### 9.2 El cierre de mundo (el acta en miniatura)

Espejo exacto del §8, porque los parámetros son los mismos:

- **Persistencia**: `project_unlocks.completado_at` + `cierre_motivo`
  (migración 026). Sin tabla nueva: la fila del unlock **es** la presencia del
  mundo en la idea, y su ciclo de vida completo cabe en ella. El evento
  `mundo_completado` de `project_bitacora` lleva `{mundo, accion, motivo}`.
- **No exige el checklist al 100%**, el motivo es **opcional** (texto/voz), y el
  espejo del momento dice "X de N acciones de este mundo".
- **Reversible** ("Reabrir este mundo"), y **reabrir no borra el motivo**.
- **Los ítems pendientes quedan intactos**: testigos, no basura.
- **Dónde aparece**: chip verde "Completado" en su sección y en la fila de
  potenciadores; su hito en el timeline de la Celebración del proyecto
  ("Mundo completado: Calidad y Confianza", con el matiz de los mundos `#3A9B8F`
  y su motivo discreto); y el desglose por dominio del Análisis.
- **Sobrio a propósito**: el cierre de un mundo es **un momento, no la fiesta**.
  La Celebración grande — la constelación, el timeline con pulso, "aquí acaba tu
  idea y nace tu proyecto" — sigue siendo **exclusiva del proyecto**.

### 9.3 La jerarquía honesta

Las dos direcciones, y ninguna es simétrica:

- **Cerrar el PROYECTO con mundos abiertos es legítimo** — la soberanía del
  usuario manda. Y por eso mismo el acta **lo dice**: "Calidad y Confianza: 3 de
  5 (60%), abierta". No se esconde lo que el usuario decidió.
- **Completar los mundos NO cierra el proyecto**, ni siquiera completándolos
  todos. El cierre del proyecto es un acto aparte, del usuario, en su pantalla.
  La ruta de cierre de mundo **jamás toca** `projects.realizada_at`.

### 9.4 El cobro (cuando la ETAPA 2 despierte)

El follow cobra su precio de `precios.ts`, **tanto core como mundo**
(`seguimiento` y `mundo_seguimiento`; §5 arriba), con el patrón de siempre:
**verificar al inicio, descontar a la entrega**. La verificación está en
`lib/cicloApertura.ts` (compartida por `follow` y `replantear`), **después** de
validar el mundo (verificar antes cobraría un 403); el descuento, en la entrega
del plan del ciclo (`session/[id]/plan`), no en el primer turno (corrección de
la AUD-09: este párrafo decía "2 créditos" y "el descuento en la entrega del
primer turno"). Replantear un mundo cobra `mundo_replanteamiento`.

> **Errata corregida (2026-07-17):** una versión anterior de esta línea decía
> "el follow core no cuesta créditos: es el bucle del viaje principal". Fue un
> **drift mío de la Fase 4.2** — nadie autorizó esa política, contradecía el §5
> de este mismo documento y `precios.ts`, y se propagó: se coló en un comentario
> de `follow/route.ts` y, al entregarle este documento a Design, en la tabla del
> `REGLAS_Y_TOKENS.md` del canon 2.0 ("Seguimiento core: Gratis"). Las tres
> corregidas a la vez. El seguimiento core cobra su precio de catálogo, igual que
> el de mundo (entonces 2; hoy el de `precios.ts`).
