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
