# Brief de diseño — Espacios (pestañas-fichero + hub del mundo + caras del espacio)

La campaña **"Espacios"** ya está **implementada y en producción** (Claude Code, bajo
dirección del fundador). Este brief es para que Design **calibre la vara visual** de tres
piezas nuevas y **vigile un riesgo** concreto. Estado actual capturado por el gate
(`web/scripts/gate_beta.ts`, prefijos `espacios_*`, dos viewports).

## El modelo (para anclar el diseño)

Un proyecto = el viaje **core** ("Tu viaje") + sus **mundos**; cada uno es un ESPACIO.

- **Nivel 1 — los espacios**: **pestañas-fichero** (folders con icono + nombre; "Tu
  viaje" + cada mundo + un "+"). El core lleva una brújula; cada mundo, su icono.
- **Nivel 2 — las caras de un espacio**: un **selector segmentado** (píldora con
  indicador que se desliza) con tres caras, **una a la vez**: **Plan** · **Manos a la
  obra** · **Tu avance**.

## EL RIESGO A VIGILAR (lo que el fundador pidió explícito)

**Dos niveles de navegación horizontal** en la misma pantalla: las **pestañas de espacio**
(arriba) y la **píldora de caras** (debajo). El riesgo es que se confundan. Regla dura:
**distinguibles por FORMA siempre, también a 380** — el folder es **angular** (esquinas
superiores redondeadas, "se levanta"); la píldora es **redonda** (cápsula con slider). El
color no basta: la forma los separa. Design valida que a 380 (donde ambos pueden hacer
scroll horizontal) el usuario nunca dude cuál es cuál.

## Qué calibrar (pedimos el pulido de la vara)

1. **Las pestañas-fichero** (`CambiadorEspacios`): que se sientan expedientes de un mismo
   proyecto; la activa levantada (borde superior de acento) conectando con el contenido.
   Tamaño de icono, separación, cuánto se "levanta", nombre debajo vs. al lado.
2. **La píldora de caras** (`SelectorCara`): el slider, los iconos (Plan=documento,
   Manos=check, Tu avance=hitos), el tamaño; que a 380 no se sienta apretada.
3. **"Tu avance"** (`LineaAvance`): la línea de hitos sobria (punto lleno verde =
   alcanzado; hueco gris = por llegar). Que se lea como historia de hitos, **no**
   estadística (eso vive en Análisis). La animada con constelación es la Celebración
   grande, del proyecto — esta es sobria a propósito.

## Reglas de la casa (no negociables)

- **Modo oscuro**, tokens de la casa; hairlines, no cajas pesadas.
- **Ley de color:** azul piensa/estructura (el slider activo, la pestaña activa); **verde**
  ejecuta/celebra (hitos alcanzados, cierre); gris = lo que falta. **Nunca rojo.**
  Distinción por **forma** además de color.
- **Sin jerga** (BANCO §7.1, diccionario de la casa): es **"Tu avance"**, jamás
  "timeline"/"Gantt". "Manos a la obra", "Plan".
- **Sin guiones largos** en copy visible; cifras `tabular-nums`.

## Entrega esperada

- Opciones/ajustes en **HTML autocontenido** (dos viewports, 1240 y 380), con notas del
  manejo del color y de la **distinción de los dos niveles a 380**.
- Referencia del estado actual: las capturas `espacios_*` del gate.
