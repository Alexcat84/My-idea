# PROMPT PARA CLAUDE DESIGN — Refrescar el canon web de My Idea

> Para el fundador: copia de aquí hacia abajo. La lista de archivos que le das a
> Claude Design está en la ÚLTIMA sección de este documento ("Qué le entregas").

---

Ya me entregaste el canon visual de My Idea (11 pantallas, sigue vigente). El
producto **creció cuatro fases desde entonces** y el canon se quedó atrás:
pantallas nuevas nacieron sin mockup, y varias existentes ganaron estados que el
canon no dibuja. Necesito que **refresques el canon a la verdad actual del
producto**, en el mismo formato HTML de siempre.

## 0. La disciplina (esto es lo más importante, léelo dos veces)

Tenemos un instrumento automático que abre tu HTML, recorta cada frame por su
`data-screen-label` y lo pone **al lado de la app real** para comparar. Tu
entrega no es una referencia: **es la vara contra la que se mide el código.**

Por eso:

- **Vas a VER la app actual** (te doy capturas de las 30 pantallas en sus dos
  viewports). Es para que sepas qué hace el producto HOY.
- **Pero NO la calques.** Tu trabajo es diseño con criterio, no fotocopia. Si la
  app actual tiene algo torpe (y lo tiene: mira "Manos a la Obra" a 380, son
  ~3.100px de scroll), tu canon lo resuelve mejor, y esa diferencia se vuelve el
  trabajo que hago yo después. El canon MANDA sobre la app, no al revés.
- **La app cambió por decisiones aprobadas, no por deriva.** Lo nuevo (el bucle
  de seguimiento, los mundos como subproyectos, los cierres) es producto real
  que merece canon. No estás inventando features; les estás dando su vara.

## 1. Qué es My Idea (por si hace falta el recordatorio)

Un espacio de trabajo donde una persona convierte una idea de negocio en un plan
y lo ejecuta. No es un chatbot: es **un árbol que piensa contigo**. El viaje son
5 etapas — **La Chispa · Claridad · La Exploración · Tu Plan · Manos a la Obra** —
y hay **mundos**, paquetes que se activan y funcionan como **subproyectos
completos** dentro del proyecto (su exploración, su plan, su checklist, su
seguimiento y su cierre propios).

## 2. El formato EXACTO (para que el instrumento te lea)

Un archivo HTML **autocontenido por pantalla**, que abra por `file://` **sin
red** (el instrumento lo abre offline). Tal como los que ya entregaste:

- Una galería: un `<section>` con un encabezado (eyebrow azul + título +
  descripción) y luego los frames en `display:flex; flex-wrap:wrap; gap:28px`.
- **Cada frame es un `<div data-screen-label="…">`** de tamaño fijo:
  - **desktop**: `width:1240px`
  - **móvil**: `width:380px`
- Fondo `#000`, `border:1px solid rgba(255,255,255,0.08)`, `border-radius:16px`,
  `overflow:hidden`.

Esqueleto mínimo (el instrumento solo necesita el `data-screen-label`; lo demás
es tu maquetación):

```html
<section style="padding:48px 56px;color:#F5F6F8;font-family:Inter,system-ui,sans-serif">
  <div style="display:flex;flex-direction:column;gap:16px;margin-bottom:36px">
    <div style="font-size:13px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:#4D7CFE">Motor My Idea · Etapa 5 de 5</div>
    <div style="font-size:30px;font-weight:700">Manos a la Obra</div>
    <div style="font-size:15px;color:#A6A7AD;max-width:720px;line-height:1.6">…qué es esta pantalla… Desktop y mobile 380px.</div>
  </div>
  <div style="display:flex;gap:28px;align-items:flex-start;flex-wrap:wrap">
    <div data-screen-label="Manos a la Obra desktop" style="width:1240px;background:#000;border:1px solid rgba(255,255,255,0.08);border-radius:16px;overflow:hidden">
      <!-- … la pantalla … -->
    </div>
    <div data-screen-label="Manos a la Obra mobile 380" style="width:380px;background:#000;border:1px solid rgba(255,255,255,0.08);border-radius:16px;overflow:hidden">
      <!-- … la misma pantalla a 380 … -->
    </div>
  </div>
</section>
```

**Reglas del `data-screen-label`, obligatorias:**

1. **Termina en el viewport**: `"… desktop"` o `"… mobile 380"`. El instrumento
   elige el frame por ese sufijo.
2. **Si una etiqueta es PREFIJO de otra, difieren desde el principio, no al
   final.** Ya nos cruzó un par: `"1a mobile 380"` vivía dentro de
   `"1a mobile 380 recorrido abierto"` y el instrumento se llevó el equivocado.
   Nómbralos `"Exploracion 380"` y `"Exploracion 380 recorrido abierto"` de forma
   que el sufijo de viewport quede al final pero sin que uno contenga al otro.

**Fuentes:** Inter. Si la incrustas, hazlo como `data:` URI (el instrumento abre
offline; un `<link>` a Google Fonts NO carga). Si no, deja un stack de sistema
(`Inter, system-ui, sans-serif`) — la app usa Inter y el fallback es aceptable.

**Cada pantalla, SIEMPRE en los dos viewports** (1240 y 380). Ni un frame sin su
par de 380: el instrumento mira los dos, y una vara que no se mira es decoración.

## 3. Tokens (obligatorios)

| Token | Valor |
|---|---|
| Azul primario (piensa) | `#4D7CFE` |
| Verde ejecución (ejecuta) | `#3FB950` |
| Ámbar guardián | `#E0A64A` |
| Matiz de los mundos | `#3A9B8F` |
| Fondo base | `#0A0A0C` / `#000000` |
| Superficie 1 (tarjetas) | `#101013` |
| Superficie 2 (campos, hover) | `#17171B` / `#141419` |
| Texto | `#F5F6F8` |
| Texto dim | `#A6A7AD` |
| Hairline | `rgba(255,255,255,0.08)` |

**La regla de color es de SIGNIFICADO: el azul piensa, el verde ejecuta.** Azul =
exploración, planeación, navegación, el anillo "pensando". Verde = acción sobre
el mundo real (etapa 5, el progreso del checklist, "esta semana", los X/N). El
ámbar es **solo** el guardián de datos. El matiz de los mundos (`#3A9B8F`) no es
ni azul ni verde. Los estados completados se distinguen también por **FORMA**
(check lleno, texto tachado), nunca solo por color.

## 4. La voz

Palabras de persona, jamás de máquina. Nada de regaños (si el usuario va tarde,
se dice sin juzgar: tono espejo). **Sin cifras inventadas** (si hay un número, es
del usuario). Cero jerga. "Manos a la Obra", nunca "En marcha". El mundo se nombra
como el usuario lo conoce ("Calidad y Confianza"), jamás por su clave técnica.

## 5. Las pantallas — refrescar las 11 y dibujar lo nuevo

Te doy, junto a cada una, la captura de la app actual para que veas el estado de
hoy (nombre del archivo entre paréntesis). **Refresca** con tu criterio; donde
diga NUEVO, **diseña desde cero**.

### A. Refrescar (existen, verifica contra la captura actual)

1. **Home / Mis ideas** (`00_home_app`, `_380`) — la cinta por idea ahora lleva
   un **sello de fecha** ("última acción · ayer 21:26"), y las realizadas
   reposan al final con su distintivo "Proyecto".
2. **La Chispa** (`01_chispa_app`, `_380`) — el micrófono es sagrado.
3. **Claridad** (`02_claridad_app`, `_380`).
4. **La Exploración** (`03_exploracion_app`, `_380`) — el riel del árbol (la
   línea desciende y toca cada punto), la oferta honesta (`03b_oferta_honesta_app`),
   la tarjeta intermedia antes del plan (`04a_plan_en_camino_app`).
5. **Tu Plan** (`04_tu_plan_app`, `_380`).
6. **Manos a la Obra** (`05_manos_app`, `_380`) — **la que más creció.** Hoy
   contiene, además del checklist: la elección de modo (`06_modo_app`), el ritual
   de línea base (`07_baseline_app`), el ritual "Contar qué pasó" (3 tarjetas), y
   "Marcar como realizada" con su acta de cierre. A 380 es un scroll de 3.100px:
   **replantéalo** (etapas plegables, y todo lo que hoy cae al fondo — análisis,
   cerrar, ritmo — necesita jerarquía).
7. **Potenciadores** (`07`, en Manos y en su página) — el candado se retiró: ahora
   es **"Activar · beta"** (gratis durante la beta, el precio del catálogo va
   tachado). Refréscalo.
8. **Mundos Activos** (`10_mundo_activo_app`, `_380`) — el mundo es un
   **SUBPROYECTO**: su sección tiene su propio checklist, su ritual "Contar qué
   pasó" (`10b_mundo_ritual_app`) y su cierre "Marcar este mundo como completado"
   (`10c_mundo_cierre_app`), con chip verde **"Completado"**.
9. **La Celebración** (`09_celebracion_cumplimiento_app`, `09b_celebracion_ritmo_app`,
   `_380`) — el timeline del viaje, en sus dos variantes (con cumplimiento / a mi
   ritmo). El hito de mundo se lee "Mundo activado: Calidad y Confianza" con el
   matiz `#3A9B8F`. Es el momento emocional del producto.
10. **Modo y Fechas** (`06_modo_app`, `07_baseline_app`, `_380`).
11. **Análisis del Proyecto** (`08_analisis_app`, `_380`) — ahora con la fila
    **"Cumplimiento por mundo"**.

### B. NUEVO — diseñar desde cero

12. **El cierre honesto** — cuando el motor decide que un camino no lleva a
    ningún lado (o que un mundo no es para esta idea), la pantalla **jamás queda
    muda**: muestra el porqué en palabras de persona y **dos salidas** (volver a
    Manos a la Obra / ver los otros mundos). Si era un mundo, dice que se devolvió
    la activación. Hoy existe en código pero sin canon.
13. **Explorar actividad** (lo pidió el fundador) — hoy cada acción del checklist
    es una fila con "marcar hecho" y nada más. Queremos poder **abrir una
    actividad** y, DENTRO, ver sus ajustes (su fecha, su nota, marcarla hecha),
    en vez de tener todo al ras de la fila. Es una pantalla (o panel) de **detalle
    de ítem** que no existe: diséñala. Cómo se abre desde la fila, qué muestra
    dentro, cómo se cierra.

## 6. Lo que NO debes hacer (errores que este proyecto ya pagó)

- **No diseñes con texto corto y bonito.** Los mockups viejos usaban ítems como
  "Habla con 5 cafeterías"; el producto real genera frases de **tres líneas**
  ("Escribe en una hoja las dos o tres cosas que, si resultan falsas, harían que
  todo tu modelo no funcione"). **Diseña con el texto largo y feo**, que es el
  de verdad. Si solo funciona con texto corto, no funciona.
- **No dejes ningún frame sin su 380.**
- **No cambies los nombres de las 5 etapas ni de los mundos.**
- **No rompas la regla del azul y el verde** para que algo "se vea mejor".
- **No metas nada que dependa de la red** (fuentes, imágenes remotas): abre offline.

## 7. Qué me devuelves, además del HTML

Una nota corta con **las decisiones que tomaste**: qué replanteaste de la app
actual y por qué, qué colapsaste o mandaste a un segundo nivel en móvil, y qué
recortaste. Esa nota vale tanto como los frames: es lo que evita que la
implementación reinterprete tu criterio.

---

## Qué le entregas a Claude Design (para el fundador)

Súbele estos archivos del repo. Los tres primeros son "cómo lo llevamos hoy"; el
resto es la vara de estilo, la voz y las reglas del producto nuevo.

1. **Las 30 capturas de la app actual** — `web/examples/gate-canon/*_app*.png`.
   Son las 11 pantallas (y sus estados) en los dos viewports, tal como se ven
   hoy. Es lo que Design debe VER para saber qué hace el producto ahora.
2. **El canon actual** — los 11 HTML de `docs/diseno-canon/*.html`. Su lenguaje
   visual a evolucionar y, de paso, el formato exacto a replicar.
3. **`docs/diseno-canon/REGLAS_Y_TOKENS.md`** — el registro de tokens y las
   reglas de color.
4. **`docs/BANCO_DE_TEXTOS.md`** — la voz, el copy vigente y las fronteras.
5. **`docs/FLUJO_TRACKING.md`** — describe los comportamientos NUEVOS que piden
   canon: el bucle de seguimiento (§1-4), el acta de cierre (§8) y los mundos
   como subproyectos con su follow y su cierre (§9).

> Nota: la APK tiene su propio encargo aparte (`docs/PROMPT_CANON_APK.md`); ese
> es el caparazón nativo. ESTE prompt es solo el canon **web**.
