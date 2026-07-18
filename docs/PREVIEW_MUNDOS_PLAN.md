# EL PREVIEW DE LOS MUNDOS — Modelo comercial, análisis y plan

Destino: docs/PREVIEW_MUNDOS_PLAN.md. Fase: 4.5. Tag al cierre: web-v1.4.0.
Decisión del fundador (jul 2026), analizada y especificada con el auditor.

## 1. LA DECISIÓN EN UNA FRASE

Los mundos dejan de venderse con candado y pasan a probarse gratis: la
entrevista y su diagnóstico son el escaparate; el PLAN es lo que se compra.
El patrón freemium que ya funciona en el core (organizador gratis → plan
cobra 5) extendido a los siete mundos (preview gratis → plan cobra 3).

## 2. POR QUÉ (el análisis completo)

### 2.1 Los tres problemas del modelo con candado

- **Compra a ciegas**: el usuario paga 3 créditos ANTES de saber si el mundo
  le aporta. La promesa del catálogo es genérica; su proyecto es específico.
- **El reembolso como experiencia de compra**: el cierre honesto post-pago
  (fase 4.3) es correcto pero es un tropiezo con disculpa: cobrar-y-devolver
  siempre sabe peor que no cobrar. Con candado, la incompatibilidad se
  descubre DESPUÉS del dinero.
- **Vitrina sin protagonismo**: siete tarjetas con candado son siete promesas
  abstractas. Nada demuestra valor sobre EL proyecto del usuario.

### 2.2 Lo que el preview resuelve

- El usuario decide con conocimiento: vio QUÉ encontró el motor en SU
  proyecto y QUÉ le estructuraría un plan. La compra deja de ser apuesta.
- La incompatibilidad se confiesa GRATIS y ANTES: el detector corre en el
  preview; el cierre honesto se muda a pre-compra (sin cobro, sin reembolso,
  sin tropiezo). El reembolso queda solo para el caso raro de
  incompatibilidad descubierta a mitad de un plan ya pagado.
- Los mundos ganan protagonismo real: se prueban, no se miran. El usuario
  que completó una entrevista ya invirtió su tiempo: el retorno a comprar
  es natural, no empujado.
- La honestidad se vuelve argumento de venta visible: "este producto me
  dijo gratis que ese mundo aún no era para mí" construye la confianza que
  vende los otros seis.

### 2.3 La economía (números medidos en vuelos, jul 2026)

- Ciclo completo de mundo (brecha + entrevista 5-8 turnos + plan):
  $0.09-0.15 medidos (mundoRiesgos $0.1432, mundoSubproyecto $0.0931).
- El plan es el tramo caro (~$0.04-0.06). La entrevista sola: $0.05-0.09.
  El resumen-diagnóstico (más corto que un plan): ~$0.02-0.03.
- **Costo del preview: ~$0.07-0.12 por usuario por mundo. Redondeo de
  planificación: 10 centavos.**
- La compra que provoca: 3 créditos (≈$3 al precio de catálogo).
- **Punto de equilibrio: 1 compra por cada ~25 previews (4%).** Las tasas
  normales de freemium bien ejecutado (5-15%) dejan el preview como costo
  de adquisición pagado con margen.
- Exposición máxima por proyecto (guardarraíl un-preview-por-mundo):
  7 mundos × ~$0.10 = ~$0.70 en el peor caso absoluto (prueba todo, no
  compra nada), contra $5 ya pagados por el plan core: costo de venta ≤14%
  en el escenario más pesimista.
- **LEY DE CALIDAD (decisión del fundador, no negociable): el análisis
  corre SIEMPRE en el modelo de calidad plena (Sonnet), incluido el
  preview.** El preview es el vendedor del mundo: la primera probada
  gratuita de la calidad de la casa; degradarlo a un modelo menor
  ahorraría centavos y costaría el posicionamiento entero ("calidad de
  consultor, no app común y corriente"). Haiku queda donde siempre estuvo:
  papeles de apoyo (organizador, juez, resúmenes internos), jamás el
  análisis que el usuario lee como juicio sobre SU proyecto. Si algún día
  los costos aprietan, la palanca es el precio o el guardarraíl de
  volumen, nunca la calidad del análisis.

### 2.4 Por qué el candado de secuencia (mundos solo tras el plan core)

- Metodológico: los mundos LEEN el proyecto (estado vivo + fase + checklist).
  Sin plan core no hay materia prima: la brecha entraría ciega y el preview
  sería genérico: exactamente lo que el producto no es.
- Comercial: el viaje tiene orden. Primero tu proyecto (el compromiso de 5),
  luego sus dimensiones (los upsells de 3). El usuario con plan core ya
  demostró intención y ya tiene contexto rico que hace brillar los previews.

## 3. LA LÍNEA QUE PROTEGE EL DINERO

**El preview es diagnóstico, jamás plan encubierto.** Dice lo que HAY y lo
que un plan estructuraría; nunca lo que HARÍAS. Prohibido en el resumen:
pasos accionables, "Esta semana", secuencias de ejecución, entregables por
etapa. Permitido: los temas encontrados en el proyecto, los huecos que el
dominio cubriría, el veredicto de compatibilidad, la promesa concreta de
qué contendría el plan. Si el preview resuelve, nadie compra; si el preview
demuestra, compran los que tienen razones. Esta frontera se verifica en el
vuelo (asserts sobre el resumen: cero imperativos de ejecución).

## 4. LA MÁQUINA DE ESTADOS (cuatro, cada uno con su cara)

```
[bloqueado]   pre-plan-core. "Se abre con tu plan." (candado de secuencia)
     │  se genera el plan core
     ▼
[abierto]     vitrina invitante. "Explóralo gratis." Entrar arranca la
     │        entrevista del mundo (brecha elige puerta, como siempre).
     │  entrevista completada
     ▼
[diagnóstico listo]   EL ESTADO PROTAGONISTA. Chip "Listo para generar tu
     │        plan". El resumen persiste y se relee. CTA permanente:
     │        "Generar mi plan de [mundo] · 3 créditos" (beta: tachado).
     │        Evento 'preview_completado_sin_compra' en bitácora (gancho de
     │        notificación futura, capa post-beta).
     │  compra (cobro A LA ENTREGA, patrón de la casa)
     ▼
[plan comprado]   el mundo completo actual: plan, checklist, fechas,
              seguimiento, cierre. Chip vigente.
```

- Incompatibilidad detectada en el preview → cierre honesto GRATIS (canon
  12, sin chip de reembolso: no hubo cobro).
- Un preview por mundo por proyecto. Re-correr la entrevista requiere
  compra O cambio de ciclo del proyecto (realidad nueva amerita mirada
  nueva: además es el gancho honesto de re-visita).
- La sesión del preview PERSISTE completa: la compra genera el plan DESDE
  ella sin re-entrevistar (un click al valor). Si el proyecto cambió de
  ciclo entre preview y compra, el plan se genera con el estado vivo ACTUAL.

## 5. PLAN DE IMPLEMENTACIÓN (fase 4.5)

1. **Esquema**: evolución del unlock (propuesta: preview_at, resumen
   persistido con su versión, plan_pagado_at asumiendo la semántica del
   unlock actual). Migración nueva respetando 020-024 reservadas. Los
   mundos activados de sesiones previas migran con gracia (con plan =
   comprados).
2. **Motor**: la entrevista del mundo ya existe (brecha + intérprete +
   murallas): se reusa intacta. Pieza nueva: el REDACTOR DEL DIAGNÓSTICO
   (prompt nuevo con paridad Python↔TS): entrada = recorrido del preview +
   estado vivo; salida = el resumen punto-a-punto con la frontera del §3
   como regla dura + la voz de la casa (tuteo condicional, acentos, cero
   jerga, espejo). El detector de incompatibilidad corre aquí (pre-compra).
3. **Cobro**: el punto de cobro del mundo se MUDA del unlock a la entrega
   del plan (ancla ETAPA 2 actualizada; verificar-al-inicio /
   descontar-a-la-entrega). El precio no cambia: 3 créditos.
4. **UI**: la fila de potenciadores y la sección del mundo reflejan los
   cuatro estados. Implementación sobria con piezas existentes; la vara
   del preview no existe en el canon → anotar en la matriz "implementado,
   vara pendiente" y pedir el frame a Design en el próximo lote (patrón
   ciclo-de-caja). El estado [diagnóstico listo] usa el timestamp híbrido
   en su sello.
5. **Vuelo** (los dos caminos + las regresiones):
   - Feliz: plan core → vitrina abierta → preview de mundo compatible →
     resumen SIN pasos accionables (assert de la frontera §3) → compra →
     plan del mundo desde la sesión persistida sin re-entrevistar →
     checklist/fechas/seguimiento intactos.
   - Espejo: preview de mundo incompatible → cierre honesto gratis, cero
     cobro, cero reembolso, evento en bitácora.
   - Regresiones: un-preview-por-mundo (repetir sin comprar no re-corre);
     candado pre-plan-core intacto; el flujo comprado conserva TODA la
     paridad de las fases 4.1-4.3 (fechas, análisis, follow, cierre).
6. **Telemetría sembrada**: eventos preview_iniciado / preview_completado /
   preview_a_compra por mundo en bitácora: la tasa de conversión por mundo
   es EL dato comercial de la beta (qué mundos venden, cuáles necesitan
   mejores puertas o mejor promesa).
7. Suites verdes en clon limpio, gate de la fila en sus estados, commits
   "Preview mundos:", tag web-v1.4.0. Merge tras auditoría.

## 6. LO QUE NO CAMBIA (por si la fase tienta)

- El precio del plan de mundo (3) y del seguimiento (2): intactos.
- La ley del ledger: ninguna afirmación de dinero sin evento.
- La ley del cobro: verificar al inicio, descontar a la entrega.
- Las murallas de dominio, la paridad de trato, el cierre soberano.
- Las notificaciones NO se construyen (solo su evento gancho).
- El catálogo de bundles sigue siendo decisión pendiente del fundador.
- La calidad del modelo: el análisis es Sonnet siempre (ley del §2.3);
  ninguna fase futura la degrada por costo.

## 7. MÉTRICAS DE ÉXITO (para juzgar la fase con la beta)

- Tasa preview→compra por mundo (umbral de salud: >4% cubre costos;
  esperado sano: 5-15%).
- Incompatibilidades confesadas en preview vs post-compra (esperado: casi
  todas pre-compra: el reembolso debe volverse pieza de museo).
- Previews releídos y regresos al estado [diagnóstico listo] (mide si el
  gancho de re-visita funciona sin notificaciones).
