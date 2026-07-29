# Brief de diseño — Los PDFs (Tu Plan y Expediente completo)

**Qué es:** lo que el usuario se lleva impreso o en PDF. Dos documentos que aún
**no ha calibrado Design**:
- **Tu Plan** (el plan con el que arrancó). Estado actual: `plan_pdf_v2.png`.
- **Expediente completo** (todo el desarrollo, de la idea al cierre). Estado
  actual: `expediente_pdf_v2.png`.
Detalles ya resueltos que conviene ver: `riel_v3.png` (el riel de puntos) y
`lote3_tabla_fechas.png` (la tabla de fechas).

**De dónde salen:** ambos se arman con `web/app/ui/DocumentoPapel.tsx` (el
markdown del servidor renderizado con el lenguaje de la casa) + la hoja de
impresión en `web/app/globals.css` (`@media print`: tokens de PAPEL, pie propio,
acordeones abiertos). El `.md` y el PDF salen del MISMO texto: una sola verdad.
La bitácora impresa tiene su propio brief (`BRIEF_BITACORA.md`).

## Qué hay que diseñar

Volver estos documentos un **entregable bello**, no "la app pintada de blanco".
Portada, jerarquía, ritmo, la tabla, el pie, los colores de fecha. Que dé gusto
descargarlo, imprimirlo y compartirlo.

## Anatomía actual (respetarla, embellecerla)

**Identidad en papel** (tokens de papel en `globals.css @media print`):
superficies claras, tinta oscura, pero la **identidad se conserva**: azul
piensa, verde ejecuta, ámbar guardián. `-webkit-print-color-adjust: exact`.

**Tu Plan:**
- Encabezado: eyebrow "Generado de tu recorrido · plan completo" + título + intro
  + "Descargar PDF / .md".
- Cada **Etapa**: título con **punto azul**; sus **pasos** en un **riel de puntos**
  (línea vertical + puntos ENCIMA, la línea atraviesa su centro); "Entregable" y
  "Esta semana" en negrita.
- Sección "¿Puede sostenerse tu idea?" con su riel de viñetas.
- **Pie repetido** por página: "[idea] · Tu Plan" a la izquierda, "My Idea" a la
  derecha, bajo una hairline.

**Expediente completo:** portada (# idea + generado + "Empezaste" + "Estado") +
**índice** + secciones en orden: tu idea tal cual / tu idea ordenada / cada plan
y seguimiento / **"Tu avance"** (o "Lo que hiciste" si ya cerró) con una **tabla**
(columna Acción + columna "Cuándo": fecha en **verde** si hecho, **azul** si
previsto) + Tus Números / cada mundo / **"Tu progreso hasta aquí"** (o "Cómo te
fue" si cerró) / por qué la cerró / **"La secuencia de tu viaje"** (la bitácora).

## Restricciones (no negociables)

- **Tokens de PAPEL** de `globals.css @media print` (no inventar colores nuevos).
  Identidad conservada; **nunca rojo**; el verde de "terminado" solo en el cierre.
- **El riel/línea atraviesa el centro de los puntos** (reclamo previo; ver
  `riel_v3.png`).
- **El pie no debe tapar el texto:** el margen inferior se reserva por página en
  `@page` (ya corregido). Design puede rediseñar el pie, respetando esa banda.
- **Sin guiones largos.** **Sin jerga, nodos, grafos ni mecánica del motor.**
- Los **motivos del usuario** se citan entre comillas, tal cual.
- Pensado para **A4/carta**; que pagine bien (títulos no huérfanos, bloques que
  no se parten a la mitad).

## Historia (para no repetir)

Ya se resolvió a mano: el pie que tapaba texto (margen por página), el riel que
quedaba a un lado (ahora espina que atraviesa), las fechas en desorden (ahora
tabla con columna "Cuándo"), y las claves de sección según estado ("Tu avance"
vs "Lo que hiciste", "Tu progreso" vs "Cómo te fue"). Design pule desde aquí.

Entrega esperada: mockups del PDF de **Tu Plan** y del **Expediente** (portada +
una página interior de cada uno como mínimo), en la identidad de papel, listos
para implementar en `DocumentoPapel` + la hoja de impresión.
