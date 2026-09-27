# El ciclo de replanteamiento: cómo funciona HOY (Fase 1, solo lectura)

Rediseño pedido por el fundador el 27 sep 2026. Este documento describe el ciclo tal como está en
el código (`main` en `cb51a22e`), sin cambiar nada. La Fase 2 (el flujo nuevo) espera el visto del
fundador.

## La respuesta corta
- **Es un solo ciclo para dos cosas distintas.** La misma puerta sirve para **profundizar** cuando
  nada se rompió y para **replantear** cuando la realidad cambió el camino. No hay ningún parámetro,
  ruta ni regla del prompt que las distinga: el servidor solo recibe `detalles`, `enfoque` y
  `dominio` (`web/app/api/project/[id]/follow/route.ts:111-120`).
- **La tarjeta se llama "Ciclo de profundización"** y su descripción habla de replantear: "¿La
  realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás." Adentro, el ritual
  se titula "Continuar mi idea · N de 3".
- **El paso 1 trata el checklist como la historia** ("Tu checklist es tu historia: ¿ya refleja lo
  que hiciste?"), que es justo el error del diagnóstico: el checklist dice qué se hizo, no qué pasó.

## 1. Los pasos, en orden

**La entrada.** Solo desde Manos a la Obra (una sola puerta; el antiguo "Ajustar el plan" del plan
se quitó). Tarjeta "Ciclo de profundización", en móvil sobre el checklist y en escritorio en la
columna lateral; cada mundo tiene la suya ("¿La realidad te cambió el plan de {{mundo}}?…"). Con la
idea realizada la tarjeta desaparece y lo dice ("el ciclo de profundización vuelve si la reabres").

**Paso 0 (invisible): el saldo.** Al abrir, la app pregunta si alcanza el saldo (5 créditos). No
aparta nada ni gasta el límite diario.

**Paso 1 de 3.**
- Si no hay nada hecho: "¿Aún no arrancas? Cuéntame qué cambió desde que armamos el plan." (con el
  ejemplo del proveedor que falla) y el botón "Te cuento".
- Si hay algo hecho: **"Tu checklist es tu historia: ¿ya refleja lo que hiciste?"**, "Llevas N de M
  acciones hechas. Ajusta arriba lo que haga falta. De eso compongo el «qué ha pasado», sin que lo
  redactes dos veces." y el botón "Así va, sigamos". **No hay campo para escribir**: la persona
  corrige el checklist de arriba.

**Paso 2 de 3.** "¿Algo más que deba saber?", "Lo que pasó fuera del checklist: una sorpresa, un
cambio, algo que descubriste. Opcional." Un campo con texto y dictado, **opcional**.

**Paso 3 de 3.** "¿Hacia dónde profundizamos?" Un campo opcional ("Lo que más me interesa ahora
es…") y dos botones: "Continuar mi idea · 5 créditos" o "No estoy seguro". Nota: "Se descuentan al
entregarse. Si algo falla, no se cobra nada."

**Después.** Enviar abre una **entrevista nueva de seguimiento**, turno por turno, como la
exploración, y termina en la oferta de siempre ("Generar mi plan · 5 créditos"), con la tarjeta
opcional "¿Algo más que quieras que tu plan tome en cuenta?".

## 2. Qué recibe la IA

**El mensaje compuesto (sin IA)**, que se guarda como el mensaje de entrada de la sesión:
1. "Desde el último plan, este es mi avance real:"
2. Las tareas del plan vigente agrupadas por estado (HECHO, EN PROCESO, APENAS EMPEZADO, SIN
   EMPEZAR), cada una con su nota; las retiradas con su motivo y la orden "NO las vuelvas a proponer".
3. "Además: …" con lo escrito en el paso 2.
4. **El bloque "Mi realidad medida"**: número de ciclo, días del plan, hechas/total, ritmo por
   semana, racha, días sin avanzar, retiradas con motivo, duración real por etapa y, en modo fechas,
   puntualidad y fechas movidas (en modo a mi ritmo: "no hay nada que medir contra un calendario").
5. "Lo que más me interesa profundizar ahora: …" o "No estoy seguro de hacia dónde profundizar;
   guíame según mi avance."

**Las llamadas a la IA:**
- **La puerta de entrada** (Haiku, `SYSTEM_PUERTA_AVANZADA`): con el estado vivo del proyecto, el
  mensaje compuesto y hasta 30 conceptos del grafo que el proyecto **aún no ha cubierto**, elige por
  dónde retomar y redacta un perfil de sesión.
- **La entrevista** (Haiku, el intérprete de siempre), que excluye los conceptos ya cubiertos.
- **El plan** (Sonnet, `SYSTEM_PLAN`): recibe el mensaje compuesto, el perfil, el recorrido nuevo,
  material de apoyo del grafo, `es_seguimiento: true` y el estado vivo anterior.
- **No recibe**: el texto del plan anterior, las fechas de cada tarea, la bitácora ni los números
  (estos van solo al armado final del plan).

## 3. El prompt

El `SYSTEM_PLAN` le dice que **continúe, no que empiece de cero**:
- Regla 8: "Si recibes es_seguimiento=true, abre el plan con UNA linea que reconozca el avance del
  proyecto desde la ultima sesion… No repitas acciones ya cubiertas antes… basta con no asumir que el
  usuario empieza de cero."
- Regla 8-bis: el bloque de realidad es "el tiempo real de esta persona"; "El plan nuevo DEBE partir
  de ahi" (si una etapa tomó el triple, el ciclo nuevo asume ese ritmo), con el tono de espejo: jamás
  regaño; y en modo a mi ritmo, prohibido hablar de retrasos o calendario.
- El único "desde cero" está en el mensaje compuesto, cuando la persona retiró todas las tareas.

## 4. Qué pasa con el plan anterior
- **Se conserva, no se sobrescribe**: el plan nuevo es otra fila, con la etiqueta `seguimiento`, y
  pasa a ser el vigente (el último de su espacio). No hay número de ciclo ni estado "archivado": el
  orden es la fecha.
- En pantalla, los planes anteriores del núcleo quedan en el acordeón **"Historia (N)"** de Manos a
  la Obra, solo como texto ("Plan seguimiento · …", con la etiqueta cruda). Los mundos no tienen esa
  Historia.
- La bitácora y el Expediente muestran cada ciclo como "Seguimiento N" ("Contaste qué pasó y
  recalculé tu plan").

## 5. Qué pasa con las tareas hechas
- **No se trasladan.** El plan nuevo trae un checklist nuevo, todo en "pendiente", armado solo con
  el texto del plan nuevo.
- Las tareas del plan anterior (hechas, en proceso, retiradas, con sus notas y fechas) **quedan en la
  base, bajo el plan viejo**, pero **dejan de verse y de poder editarse** en Manos a la Obra. La
  Historia muestra solo el texto del plan viejo, no el estado de sus tareas.
- Siguen contando para el análisis, para el ritmo personal del calendario y en la bitácora.
- `docs/FLUJO_TRACKING.md` dice "hechos preservados, pendientes reordenados" y "lo hecho, intacto en
  Historia": en el código solo quedan guardadas en la base; ni se reordenan ni se ven en la Historia.

## 6. Precio y cobro
- **5 créditos** (`seguimiento` en el núcleo, `mundo_seguimiento` en un mundo, `web/lib/precios.ts`).
- **Al enviar el ritual** se verifica el saldo, se **aparta** el precio (2 horas) y se gasta un
  arranque del límite diario. Cualquier rechazo posterior suelta lo apartado.
- **Se cobra solo al entregar el plan** con IA. Sin plan (la entrevista termina sin plan) o con un
  plan armado sin IA, no se cobra. Si algo falla después del cobro, se reembolsa.

## 7. ¿Se usa también para profundizar sin que nada se haya roto?
**Sí: es el mismo ciclo para las dos cosas.** Hablan de profundizar el título de la tarjeta ("Ciclo
de profundización"), el paso 3 ("¿Hacia dónde profundizamos?"), el botón "Así va, sigamos" y el
mensaje a la IA ("Lo que más me interesa profundizar ahora"). Hablan de replantear la descripción de
la tarjeta ("¿La realidad te cambió el plan?"), el paso 1 sin avance, la regla 8-bis ("replanifica")
y la bitácora ("recalculé tu plan"). `docs/FLUJO_TRACKING.md §4` lo confirma: no exige un mínimo de
avance, "replanificar ante eso es método legítimo".
(No confundir con el "Seguimos explorando" de la entrevista: eso es seguir preguntando antes del plan,
no un ciclo aparte.)

## 8. Otros hallazgos que la Fase 2 debería tener en cuenta
- **La historia de la persona no queda registrada**: el ritual no escribe nada en la bitácora; su
  mensaje vive en la sesión y ninguna pantalla lo lee.
- **El texto del paso 2 y del paso 3 tiene tope de 4.000 caracteres**, como las respuestas.
- **El material de apoyo puede repetir conceptos ya cubiertos** en ciclos anteriores: la regla 8 dice
  que el material "ya excluye lo cubierto", pero eso solo vale para el recorrido nuevo, no para el
  material de apoyo (`cosecharVecindario` solo excluye el recorrido actual). Contradicción menor entre
  prompt y código.
- **`FLUJO_TRACKING.md §7` está desactualizado**: dice que el bloque de realidad, el caso sin avance y
  el cobro del seguimiento no existen, y los tres están hechos.
- **El mensaje compuesto y el bloque de realidad van en español**; el plan sale en el idioma de la
  idea.

## 9. Cómo separar las dos entradas (propuesta para la Fase 2)
Como el ciclo hoy sirve para las dos cosas, propongo **dos entradas** en Manos a la Obra:
- **"Replantear mi camino"**: el flujo nuevo de cuatro pasos (tu historia, lo que ya construiste,
  caminos posibles, confirmar y generar), para cuando algo cambió o se rompió.
- **"Profundizar mi plan"**: el ciclo de hoy, más liviano, para cuando todo va bien y se quiere ir
  más hondo. Su paso 1 deja de decir que el checklist es la historia y pasa a ser "Tu avance: ¿el
  checklist ya refleja lo que hiciste?", con el mismo precio y el mismo cobro de hoy.

Las dos llevan su propia etiqueta en la base (para la bitácora, el Expediente y la Historia) y su
propia línea en la bitácora. Esto lo decide el fundador antes de empezar la Fase 2.
