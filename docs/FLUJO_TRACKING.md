# ARQUITECTURA DEL BUCLE DE TRACKING — My Idea
El flujo canónico que el sistema DEBE cumplir. Destino: docs/ del repo.
Estado: la Fase 3.8 construyó las piezas; este documento define cómo se
conectan. Los huecos actuales están marcados al final.

## 0. EL PRINCIPIO RECTOR
El proyecto tiene UNA sola verdad (lo persistido) y DOS espejos que la leen:
- **El Análisis** es el espejo para el humano.
- **El follow (ciclo de profundización) es el espejo para el motor.**
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
[5] EL RITUAL (la única puerta: Manos a la Obra, "Contar qué pasó")
      -> tarjeta 1: el checklist como está (adaptada al avance real)
      -> tarjeta 2: qué pasó (texto/voz libre)
      -> tarjeta 3: el enfoque del siguiente tramo ("No estoy seguro" es
         opción legítima: el motor decide)
[6] EL FOLLOW COMPONE para el motor:
      estados + notas + texto libre del usuario
      + EL BLOQUE DE REALIDAD (sección 3 de este doc)  <- el hueco actual
[7] EL MOTOR REGENERA
      -> ruta nueva desde la realidad, plan nuevo que PARTE de lo que pasó
      -> hechos preservados, pendientes reordenados, desviaciones asumidas
         sin regaño ("la etapa 2 tomó más de lo previsto; este ciclo asume
         tu ritmo real")
[8] NUEVO CICLO
      -> checklist encadenado (lo hecho, intacto en Historia)
      -> nueva baseline: el sugeridor del ciclo N+1 aprende del ritmo REAL
         del ciclo N (velocidad y patrón de días del usuario)
      -> vuelta a [3]
[9] CIERRE: "Marcar como realizada" -> Celebración -> Analytics final
```

## 2. LAS PUERTAS (regla de una sola puerta)
- La ÚNICA puerta al ritual es **Manos a la Obra -> "Contar qué pasó"**.
- La pantalla del plan es un DOCUMENTO, no una puerta: se lee, se descarga,
  se navega a Manos. Ningún botón de "ajustar el plan" ahí: ajustar sin
  haber ejecutado es regenerar, y regenerar no es el producto.
- El ritual está SIEMPRE disponible (ver sección 4), pero vive donde vive
  la ejecución, porque el seguimiento es un acto de ejecución, no de lectura.

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
El ritual NO exige avance mínimo. Razón: la realidad cambia antes de
ejecutar (el proveedor quebró, el local se perdió, apareció un competidor,
el usuario se enfermó), y replanificar ante eso es método legítimo, no
abuso. PERO el ritual se ADAPTA al avance:
- Con avance > 0: tarjeta 1 muestra el checklist y su progreso, como hoy.
- Con avance = 0: tarjeta 1 cambia de pregunta: no "llevas 0 de 28"
  (absurdo y desmoralizante) sino "¿Aún no arrancas? Cuéntame qué cambió
  desde que armamos el plan". Misma puerta, encuadre honesto.
El anti-abuso no es un gate artificial: es el precio (2 créditos cuando el
cobro despierte) más el límite diario vigente. Regenerar por deporte cuesta;
replanificar por realidad vale cada crédito.

## 5. EL COBRO (dónde encaja cuando el frente de cuentas despierte)
- El follow es un punto de cobro del canon: 2 créditos (core) / 2 (mundo).
- Patrón aprobado: verificar saldo al INICIO del ritual (rechazo limpio
  antes de que el usuario escriba su "qué pasó"), descontar A LA ENTREGA
  del plan nuevo (RPC consumir_creditos con idempotencia), cero cobro si
  el sistema falla a mitad.
- Hoy los chips de créditos son display; ETAPA 2 de cuentas los vuelve
  reales. Este documento no cambia eso: solo fija DÓNDE se cablea.

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
| Pieza | Estado |
|---|---|
| Ritual en Manos a la Obra | ✓ existe, lugar correcto |
| "Ajustar el plan" en la pantalla del plan | ✗ puerta duplicada y prematura: ELIMINAR |
| Follow consume estados + notas + texto | ✓ existe |
| Follow consume el BLOQUE DE REALIDAD (§3) | ✗ NO existe: el motor replanifica ciego al tiempo |
| Ritual adaptado a avance-cero (§4) | ✗ NO existe: hoy diría "0 de 28" |
| Sugeridor N+1 aprende del ritmo real | parcial (patrón de día sí; velocidad no) |
| Cobro del follow | dormido (ETAPA 2 de cuentas, por diseño) |
| Acta de cierre (§8) | ✗ NO existe: hoy se cierra sin memoria del porqué |

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

`POST /api/project/[id]/follow` recibe `dominio`. Sin él, es el follow de siempre
(core). Con él, **todo lo que depende del dominio se mueve con él**:

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

El follow de mundo cuesta **2 créditos**, con el patrón de siempre: **verificar
al inicio, descontar a la entrega**. Las dos anclas están en
`follow/route.ts`, en sus puntos exactos — la verificación **después** de validar
el mundo (verificar antes cobraría un 403), el descuento en la entrega del primer
turno. El follow **core no cuesta créditos**: es el bucle del viaje principal.
