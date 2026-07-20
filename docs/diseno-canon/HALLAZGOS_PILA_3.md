# Hallazgos de la PILA 3 — verificación contra la app viva (sin rediseños)

Base de la verificación: las 19 capturas del lote (`capturas/`) más las 30 del
refresco anterior. Donde no hay captura nueva, no afirmo nada: una vara que el
instrumento no mira es decoración, y aquí solo reporto lo que vi.

## Confirmado (calza con el canon, no tocar)

- **Home, Chispa, Claridad, Exploración, Tu Plan, Manos a la Obra**: la
  estructura, el orden de bloques y la regla de color calzan con el canon 2.0
  en las capturas disponibles (claridad y plan aparecen en las capturas del
  gate y de la fila).
- **Tus Números, pérdida y sano** (`numeros_perdida_app`, `numeros_sano_app`):
  veredicto de una frase con su color, tiles, barra de la verdad con la
  lectura en prosa, palancas con la 3 apagada en pérdida y "tu meta" en sano,
  escenarios, faltantes, guardián ámbar. Calza con el canon 14, incluidas las
  piezas nuevas (sello HOY, corregir gratis, ciclo de caja, versiones
  anteriores) que ahora tienen vara en el 19.
- **Modo lectura** (`numeros_lectura_app`): banda superior con fecha absoluta y
  "Volver a hoy", sin edición. Calza con el 19.
- **La compuerta** (`beta_compuerta_app`): tarjeta azul, CTA "Sacar mis números
  · 2 créditos", la ley visible. Calza con el 18.
- **El chip de saldo** (`beta_ideas_chip_app`): pill discreta junto al header,
  presente en /ideas y en las pantallas de idea.

## Visto raro (defectos o residuos en la app; el canon ya trae la vara)

1. **Acentos faltantes en Tus Números.** Las capturas muestran "Los numeros
   de", "mas de lo que cobras", "todavia", "aqui te dire", "perdida",
   "Guardian de datos", "asesoria fiscal", "Dias que tardas". El canon 19 los
   trae correctos; el detector de adopción los va a marcar. Es el hallazgo más
   repetido del lote.
2. **El tachado sigue vivo en la app** (`preview_fila_app`, `preview_bloqueado_app`):
   las tarjetas aún dicen "su plan: ~~3 créditos~~ · gratis en beta". Con la
   ETAPA 2 los precios son vivos: la vara nueva es el 16/07 (sin tachados).
3. **Chip en cero pintado de azul** (`beta_ideas_chip_app`): la app muestra "0
   créditos" con el mismo azul del saldo positivo. El canon 20 define cara gris
   para el cero (informar sin presionar ni alarmar).
4. **El wordmark del login** (`login_form_app`): "My Idea" todo en blanco. El
   canon 15 usa la marca bicolor canónica (My blanco + Idea azul). Decisión
   para el gate: o la app adopta el bicolor o se declara el blanco como
   variante de la puerta.
5. **Texto de siembra del test filtrado** (`beta_fila_app`): la etapa se llama
   "valida" en minúscula y su entregable es "Material del gate.". Es dato de
   siembra, no defecto de UI; se anota para que nadie lo tome como copy real.
6. **La barra de la verdad en pérdida** pinta "Cobras" en verde aunque el
   veredicto sea pérdida: correcto según el canon (lo que entra es verde; la
   pérdida es el pedazo ámbar que sobresale). No es defecto: se confirma la
   regla.
7. **"Tus Numeros · 2 creditos" en el header de la app** sin acentos (capturas
   de números): mismo caso que el punto 1.

## Sin captura en este lote (no se afirma nada)

- Mundos Activos (08), La Celebración (09), Modo y Fechas (10), Análisis (11),
  El cierre honesto (12), Detalle de actividad (13): sin captura nueva en la
  carpeta del encargo. Sus varas 2.0 siguen vigentes; el gate de dos viewports
  es quien confirma.

## Lo móvil 380

Las capturas 380 del lote confirman que la app renderiza columnas apiladas
correctas en fila, compuerta, login y números. El programa 380 profundo ya
está encolado aparte: los frames 380 de este lote siguen la vara existente
(replanteo, no colapso) sin rehacer los del canon 2.0.
