Eres el director de diseño de "My Idea", una app en español para emprendedores, modo oscuro, alta industria. Vas a CALIBRAR VISUALMENTE seis piezas de front que YA funcionan en producción: las vistes, no las rediseñas de cero ni les cambias la función o el copy. Entrégame **2–3 OPCIONES por pieza** en HTML autocontenido, cada una en 1240 y 380 px.

## Reglas duras (violarlas invalida la opción)
1. **Sin jerga técnica** (Gantt → "tus fechas de un vistazo", checklist → "tus tareas", línea base → "tus fechas de referencia"). Ante la duda: ¿lo diría alguien que nunca estudió administración?
2. **Sin guiones en texto visible**: ni largos (—), ni medios (–), ni cortos (-) como puntuación o separador. Comas, dos puntos o paréntesis. Aplica también a las notas.md del handoff.
3. **El esfuerzo de una tarea JAMÁS es un número exacto de horas**: rangos (`~1 h`, `~2-4 h`, `una jornada`, `varios días`).
4. **La severidad de un riesgo JAMÁS es puntaje, porcentaje, escala 1-10, semáforo ni heatmap.** En palabras: "probable y dolería mucho". El material canónico manda: la matriz de colores engaña.
5. **Los avisos van en ámbar espejo, jamás rojo ni tono de regaño.**
6. **El copy de este prompt es EXACTO**: puedes jerarquizar y componer, no reescribir.
7. **Ruido cero**: lo que no existe no deja placeholder (sin esfuerzo estimado no hay sección; registro vacío = frase honesta, no tabla vacía).

## PIEZA A — La pregunta de capacidad (dentro del ritual "Ponle fechas a tu camino")
Bloque con: "¿Cuántas horas por semana puedes darle a este espacio?" + 4 chips (`2 a 5 horas` · `5 a 10 horas` · `10 a 20 horas` · `Más de 20 horas`) + "Reparto las semanas según el trabajo que lleva cada tarea, y planeo con el piso de lo que me des: si te sobra tiempo, vas adelantado. Puedes cambiarlo cuando quieras."
Se juega: es LA PREMISA del calendario y hoy parece un bloque más. Debe leerse como la pregunta que manda, sin volverse modal. Diseña también su gemela mínima en la cinta de fechas activas: "Le das 5 a 10 horas por semana · cambiar".

## PIEZA B — El esfuerzo en el detalle de la tarea (cajón lateral)
Sección "Esfuerzo": rango (`~2-4 h`) + píldora `corregir` + al corregir, 4 chips de rango. Variante con espera de terceros: junto al rango va "· depende de terceros" y debajo: "Es un estimado de tu trabajo. Esta tarea depende de respuestas de otros: empiézala temprano, que tu fecha ya trae el colchón de esa espera y el tiempo que ellos tarden no se te cuenta."
Se juega: orientación honesta, y el colchón como aviso útil, no disculpa.

## PIEZA C — El registro de protección (hub del mundo: Riesgos / Seguridad y Personas / Seguridad Digital)
Título: "Registro de {mundo}". Cada fila: detección en una frase ("depende de un solo proveedor") · severidad en palabras ("probable y dolería mucho") · el camino si existe ("El camino: reducirlo." — los cuatro: evitarlo, reducirlo, pasárselo a otro, aceptarlo con los ojos abiertos) · "Protege: #3 · Compra el lote inicial" · "Tu respuesta: Consigue un proveedor alterno y pide su cotización". Estado vacío: "Este registro se llenará con el plan de este mundo: cada cosa que detecte quedará aquí junto a la respuesta que la atiende."
Se juega: es EL artefacto (el registro de riesgos del usuario, en palabras de persona). Serio sin volverse tabla fría ni matriz.

## PIEZA D — El carril y los chips (la costura de la protección)
Carril: en "tus fechas de un vistazo" del núcleo, toggle `Ver protección` (nace apagado); encendido, bajo la banda de cada etapa una sub-fila de ROMBOS: contorno azul = pendiente, relleno verde = hecha; tooltip con mundo y texto. Solo lectura.
Chips en el detalle, dos direcciones: el ítem protegido lleva píldora `Protegida` + "[respuesta] · [mundo]"; la respuesta del mundo lleva SIEMPRE su detección + "Protege: [#N · título]"; si lo protegido se retiró: "la actividad que protegía fue retirada"; la sistémica: "tu negocio entero".

## PIEZA E — El aviso de no-llego (ritual de fechas del mundo)
Bajo la fila de la protección que no alcanza, en ámbar: "Esta protección no llega antes de [#N · actividad]: muévela o acepta el riesgo con los ojos abiertos." La fecha mostrada es la honesta.
Se juega: el momento más delicado de tono del producto. Espejo, no juez.

## PIEZA F — Las fases visuales del Gantt
El diagrama ya es por fases (una barra = una etapa, tres vistas: riel, escalera, cintas). Vara: tratamiento visual de fase (títulos jerarquizados, bandas/separadores, numeración visible) calibrado UNA VEZ y heredado por las tres vistas y el PDF. El carril de la pieza D vive DENTRO de esa jerarquía: vístelo sin deshacerlo.

## Tokens de la casa
Fondo #000 / #0C0C10 · superficie #101014 · hairline rgba(255,255,255,0.08) · acento azul #4D7CFE (planear/navegar) · verde done (solo lo terminado de verdad) · ámbar warn (aviso espejo) · texto #F5F6F8 / dim #A6A7AD. Bordes redondeados suaves, densidad alta sin apretar, tabular-nums en cifras.
