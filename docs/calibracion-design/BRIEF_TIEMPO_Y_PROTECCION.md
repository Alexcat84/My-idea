# Brief de diseño — El tiempo y la protección (Scheduler + Mundos de protección)

Calibración visual sobre **front YA funcional y en producción** (tags
`web-v2.3.0-beta` y `web-v2.4.0-beta`). Nada de esto es función nueva: CD
**viste** lo que ya existe, no lo rediseña de cero ni lo reordena. Pedimos
**2–3 OPCIONES** por pieza, HTML autocontenido, modo oscuro, 1240 y 380 px.

**El reparto de siempre:** el front se aplica bajo dirección del fundador; lo
que CD calibre se pone encima. Lo que no convenza se deja y se anota, jamás se
rompe la función ni las reglas de abajo.

## Por qué este encargo existe (el contexto en tres líneas)

El producto ganó **el sentido del tiempo con capacidad real** (el calendario
respira según las horas que el usuario declara) y **los mundos de protección**
(Riesgos, HSEQ y Seguridad Digital se aplican SOBRE las actividades reales del
plan: "estos son tus riesgos y aquí sus mitigaciones"). Las superficies nacieron
funcionales; ahora necesitan leerse con el peso que tienen.

## Reglas NO negociables (violarlas invalida la opción)

1. **Sin jerga.** Gantt → "tus fechas de un vistazo" · checklist → "tus tareas" ·
   línea base → "tus fechas de referencia" · preview → "el diagnóstico". Ante la
   duda: ¿lo diría alguien que nunca estudió administración?
2. **Sin guiones largos ni medios** en ningún texto visible. Comas, dos puntos o
   paréntesis.
3. **Jamás un número de horas exacto** en el esfuerzo de una tarea: se habla en
   RANGOS (`~1 h`, `~2-4 h`, `una jornada`, `varios días`).
4. **La severidad de un riesgo jamás es un puntaje, un porcentaje ni un color de
   matriz.** Se dice en palabras (`probable y dolería mucho`). Regla del propio
   material canónico: "la matriz de colores te engaña". Nada de semáforos de
   riesgo, escalas 1-10 ni heatmaps.
5. **Ámbar espejo, jamás rojo ni regaño.** Los avisos (tardía, no-llego) informan
   sin culpar; el tono es de espejo que muestra, no de juez.
6. **El carril de protección nace DENTRO de la jerarquía visual de fase**
   (anidado bajo la banda de su etapa). La calibración lo viste sin deshacerlo.
7. **Ruido cero.** Lo que no existe no deja placeholder: sin banda no hay sección
   de esfuerzo; sin protección no aparece el toggle; el registro vacío dice
   honesto que se llenará, no pinta una tabla rota.

## PIEZA A — La pregunta de capacidad (el ritual de fechas)

**Qué es:** dentro del ritual "Ponle fechas a tu camino" de CADA espacio, un
bloque pregunta *"¿Cuántas horas por semana puedes darle a este espacio?"* con
cuatro chips (`2 a 5 horas` · `5 a 10 horas` · `10 a 20 horas` · `Más de 20
horas`) y la línea: *"Reparto las semanas según el trabajo que lleva cada tarea,
y planeo con el piso de lo que me des: si te sobra tiempo, vas adelantado.
Puedes cambiarlo cuando quieras."* Cambiar el chip **replanifica las fechas a la
vista**.

**Lo que se juega:** es **la premisa del calendario entero** y hoy se lee como
un bloque más del ritual. Merece leerse como la pregunta que manda, sin volverse
un modal ni interrumpir. Su gemela reducida vive en la cinta de "fechas
activas": *"Le das 5 a 10 horas por semana · cambiar"*.

**Par de referencia (post-corrida del gate):** `07b_capacidad_20mas` y
`07c_capacidad_2a5` — el MISMO plan con dos capacidades; la comparación es el
punto: el calendario debe VERSE distinto.

## PIEZA B — El esfuerzo en el detalle de la tarea

**Qué es:** en el cajón del detalle, la sección "Esfuerzo": el rango en palabras
(`~2-4 h`), la píldora `corregir`, y al corregir los cuatro chips de rango. Si
la tarea depende de terceros, junto al rango va `· depende de terceros` y la
explicación: *"Es un estimado de tu trabajo. Esta tarea depende de respuestas de
otros: empiézala temprano, que tu fecha ya trae el colchón de esa espera y el
tiempo que ellos tarden no se te cuenta."*

**Lo que se juega:** que el rango se lea como orientación honesta (no promesa) y
el colchón como **aviso útil**, no disculpa ni regaño. Canon de partida: la
pantalla 13 (Detalle de actividad).

**Pares:** `13_detalle` y `13b_detalle_espera`.

## PIEZA C — El registro de protección (el hub del mundo)

**Qué es:** en el hub de un mundo de protección, la herramienta canónica
instanciada. Cada fila: la **detección** en una frase ("depende de un solo
proveedor"), la **severidad en palabras** ("probable y dolería mucho"), el
**camino** cuando existe ("El camino: reducirlo." — los cuatro: evitarlo,
reducirlo, pasárselo a otro, aceptarlo con los ojos abiertos), *"Protege: #N ·
[título de la actividad]"* y *"Tu respuesta: …"*. Estado vacío honesto: *"Este
registro se llenará con el plan de este mundo: cada cosa que detecte quedará
aquí junto a la respuesta que la atiende."*

**Lo que se juega:** es EL artefacto del mundo de protección (el risk register
del usuario, en palabras de persona). Hoy es una lista de cintas; merece leerse
como un registro serio sin volverse una tabla fría ni una matriz. También es
documento descargable (.md/PDF), en el recuadro "Reportes de {espacio}" con su
chip.

**Pares:** `14_proteccion_registro` y `14b_proteccion_documentos`.

## PIEZA D — El carril y los chips (la costura)

**Qué es (carril):** en "tus fechas de un vistazo" del núcleo, el toggle
`Ver protección` (solo existe si hay protecciones; nace apagado) despliega bajo
la banda de cada etapa una sub-fila con **rombos**: contorno azul = pendiente,
relleno verde = hecha; el title lleva mundo y texto. Solo lectura: jamás cuenta
en las medidas.

**Qué es (chips):** en el detalle, las dos direcciones del enlace. El ítem del
núcleo protegido: píldora `Protegida` + *"[respuesta] · [mundo]"*. La respuesta
del mundo: su detección SIEMPRE visible + *"Protege: [#N · título]"*; si lo
protegido se retiró, se dice: *"la actividad que protegía fue retirada"*; la
sistémica dice *"tu negocio entero"*.

**Pares:** `14c_proteccion_carril` y `14d_proteccion_chip`.

## PIEZA E — El aviso de no-llego (el ritual del mundo)

**Qué es:** cuando la capacidad no alcanza para entregar una protección antes de
la actividad que protege, bajo esa fila del ritual aparece, en ámbar: *"Esta
protección no llega antes de [#N · actividad]: muévela o acepta el riesgo con
los ojos abiertos."* La fecha mostrada es la honesta; el aviso es la verdad, no
un error.

**Lo que se juega:** el momento más delicado de tono del producto. Aviso serio
sin alarma; espejo, no juez.

**Par:** `14e_proteccion_no_llega`.

## PIEZA F — Las fases visuales del Gantt (la ficha del fundador)

El Gantt ya es por fases en datos y geometría (una barra = una etapa; un cálculo
y un componente sirven a las tres vistas: Análisis del núcleo, análisis de
mundo, PDF). **La vara:** tratamiento visual de fase (títulos jerarquizados,
bandas/separadores, numeración visible) **calibrado UNA vez y heredado por las
tres vistas**, más lo que CD proponga encima. El carril de la pieza D vive
DENTRO de esa jerarquía. Complementa `BRIEF_GANTT.md` (las tres vistas ya
calibradas: riel, escalera, cintas).

## Entrega

- 2–3 opciones por pieza (A–F), HTML autocontenido modo oscuro, 1240 y 380 px.
- Los textos de este brief son EXACTOS: se pueden reordenar y jerarquizar, no
  reescribir (el copy es del banco de la casa).
- Los colores de la casa: fondo #000/#0C0C10, superficie #101014, acento azul
  #4D7CFE, verde done, ámbar warn. Referencia completa en
  `docs/diseno-canon/REGLAS_Y_TOKENS.md`.
