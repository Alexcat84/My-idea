# i18n F4: árabe de derecha a izquierda y tipografías por escritura (pendiente del visto)

Rama `i18n`. F3 aprobada por el fundador (25 sep 2026). Diseño: `DISENO.md §3.5`.

## Árabe (RTL)
- `<html dir="rtl">` en árabe ya venía de F2. Faltaba que el diseño se reflejara: **68 clases
  físicas en 22 archivos** (DISENO estimaba 69 en 24) pasaron a las **lógicas** de Tailwind 4 (`ms/me`,
  `ps/pe`, `start/end`, `text-start/end`, `rounded-s/e`, `border-s/e`), más las de variantes
  arbitrarias de Markdown y DocumentoPapel. Las líneas de tiempo que se centran con
  `-translate-x-1/2` llevan su reflejo `rtl:translate-x-1/2`.
- **Guardia** `lib/i18n/direccion.test.ts`: falla ante cualquier clase de dirección física en `app/`
  (única excepción: el centrado exacto `left-1/2` con su traslación). Escrita en rojo primero.
- Estilos en línea: las líneas de tiempo de la bitácora (pantalla y papel), la barra del stepper,
  las dos líneas punteadas y el borde del panel de la demo en la portada, y el borde de las citas
  pasaron a propiedades lógicas (`insetInlineStart`, `paddingInlineStart`, `borderInlineStart`…). Los
  puntos de la bitácora se centran con `translateX(calc(-50% * var(--sentido)))` (`--sentido` es 1,
  y -1 en árabe; `globals.css`). La espina de los documentos en papel se refleja en CSS.
- **Los gráficos del tiempo** (el Gantt de la pantalla y el del análisis en papel) quedan en
  `dir="ltr"`: el eje del tiempo se lee de izquierda a derecha en todo idioma, como las cifras.
- Las flechas "→" dibujadas en SVG (Mis ideas, Potenciadores) se reflejan en árabe
  (`rtl:-scale-x-100`); las flechas de texto ya las invirtieron los traductores.
- El selector de idioma fijo y su lista van con posición lógica: en árabe, a la izquierda y dentro de
  la pantalla.
- Revisado en el navegador: portada completa (menú, secciones, tarjetas, demo con su línea de
  tiempo), acceso, idea nueva y créditos en árabe, escritorio y móvil.

## Tipografías
- Inter no trae kana, han, hangul, devanagari ni árabe. Una **Noto por escritura** con `next/font`
  (Noto Sans JP, SC, KR, Devanagari y Arabic; el árabe se sumó porque Inter tampoco lo trae), todas
  en la variable `--font-escritura`, **sin precarga**: la clase va en `<html>` solo en su idioma y
  entra detrás de Inter (lo latino y las cifras siguen siendo Inter). Guardia:
  `lib/i18n/tipografias.test.ts`.
- Comprobado en el navegador: en español se descarga solo Inter; en japonés, chino y coreano, su Noto
  (y solo los tramos de caracteres que la página usa); en árabe e hindi, la suya.

## Capturas
Las once versiones de la portada ("Cómo funciona"), de la idea nueva y de créditos, en tres láminas
(se entregan aparte, no se versionan).

## Conocido y no resuelto en F4
- Italiano: "il 8 marzo" en vez de "l'8 marzo" (y "dal 11" por "dall'11") cuando la fecha va tras
  un artículo. Pide que la interpolación sepa el idioma en cada punto de uso (unos 20 textos): queda
  como pulido para F5/F6.
- El verificador `extraccion_identica.ts` era la prueba de F2 ("nada visible cambió") y compara
  contra `main`: hoy da 10 avisos que son cadenas de clases CSS cambiadas a propósito en F4, no
  texto.
