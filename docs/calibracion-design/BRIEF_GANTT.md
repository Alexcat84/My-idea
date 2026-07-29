# Brief de diseño — El Gantt del Análisis

**Dónde vive:** pantalla de Análisis del proyecto (canon 11), dentro de la
**capa de cumplimiento** (solo aparece en modo fechas). Título actual:
"Planificado vs. real por etapa".
**Estado actual a mejorar:** `web/examples/gate-canon/gantt_v2_app.png` (+`_380`).
**Componente:** `web/app/ui/AnalisisProyecto.tsx` (bloque del Gantt).

## Qué debe comunicar (el trabajo del gráfico)

Para cada **etapa** del viaje, comparar lo **planificado** contra lo **real**:
- Cuándo se planeó que empezara/terminara (la línea base).
- Cuándo empezó/terminó de verdad.
- El **corrimiento en cascada**: si una etapa se estira, empuja el arranque de
  las siguientes (no son barras independientes: forman una secuencia).
- Si una etapa terminó **a tiempo o tardía** (tardía = ámbar, jamás roja).

## El dato disponible (ya calculado, cero LLM)

`analytics.ts` entrega por etapa: `baseInicio`, `baseFin`, `realInicio`,
`realFin` (en días desde la chispa; `null` en lo real si la etapa aún no tiene
acción hecha). El eje de tiempo va en días.

## La meta del fundador

> "Más detallado y **visual**, más **representativo**, PERO **no tan complicado
> para los usuarios**. Al final debe entenderlo una persona."

Es decir: que se lea de un vistazo la historia "planeaba esto, pasó esto, aquí se
corrió". Nada de un diagrama de gestión de proyectos denso.

## Restricciones (no negociables)

- **Colores fijos por token** (`web/app/tokens.css`): base/plan azul
  `--accent #4d7cfe`, real a tiempo verde `--done #3fb950`, tardía ámbar
  `--warn #e0a64a`. Fondo negro. Gris para lo que falta.
- **Una sola escala/eje** (nunca dos ejes). Marcas finas; cuadrícula recesiva;
  etiquetas directas solo donde ayudan (no un número en cada punto).
- **Los nombres de actividad NO deben partir el diagrama** (aprendizaje del
  fundador): la solución vigente los sube a una leyenda numerada arriba y deja
  el diagrama limpio abajo. Se puede conservar o mejorar, no romper.
- **Dos viewports** (1240 y 380). En 380 no puede desbordar de lado.
- **Sin jerga ni mecánica interna.**

## Historia (para no repetir)

Ya hubo un rediseño (barras redondeadas gruesas + días en la leyenda + banda
ámbar) que el fundador **revirtió** por sentirlo de más; el actual `gantt_v2` es
la base limpia acordada. Design propone **desde aquí**, buscando el punto entre
"soso" y "recargado".

## Direcciones sugeridas (Design elige)

- Plan como **riel/fantasma** y real como el trazo protagonista sobre él.
- Un marcador de **"hoy"** si aporta.
- La cascada legible como escalones que se encadenan.
- Micro-etiqueta de días por etapa (plan Nd · real Md) sin saturar.
- Interacción (hover con el detalle de la etapa) si el medio lo permite.

Entrega esperada: mockups en 1240 y 380, en la identidad de la casa, listos para
que Claude Code los implemente bajo la dirección del fundador.
