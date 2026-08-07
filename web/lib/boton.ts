/**
 * boton.ts — el lenguaje de botón de la casa (decisión del fundador, ago 2026).
 *
 * EL AZUL ES TINTA, NO MANCHA. El acento (#4d7cfe) relleno bajo texto blanco se
 * lee lavado, casi celeste: es una superficie grande de color saturado peleando
 * con el blanco encima. El mismo azul como BORDE Y TEXTO sobre un fondo tenue
 * se lee limpio y serio. El fundador lo señaló con el botón "Mover fecha" del
 * calendario, que ya usaba este tratamiento, y mandó llevarlo a todo el frente.
 *
 * La jerarquía no se pierde, se hereda del calendario, que ya la tenía:
 *   PRIMARIO   = azul de tinta  (este)
 *   SECUNDARIO = contorno neutro (border-hairline / border-white/15)
 *
 * Aquí vive solo el COLOR: cada botón conserva su tamaño, su radio y su peso,
 * que dependen de dónde esté. Un botón nuevo se escribe con esta constante y
 * hereda la decisión sin que nadie tenga que recordarla.
 */
export const BOTON_PRIMARIO = "border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20";

/** El secundario de la casa: contorno neutro, sin color. */
export const BOTON_SECUNDARIO = "border border-white/15 text-dim hover:border-accent/60 hover:text-ink";
