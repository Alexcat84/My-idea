/**
 * boton.ts — el lenguaje de botón de la casa (decisiones del fundador, ago 2026).
 *
 * DOS CARRILES, y solo dos:
 *
 *  1. EL HÉROE (`BotonHeroe`, app/ui/BotonHeroe.tsx). Animado, con la chispa.
 *     Reservado a los momentos que ABREN CAMINO: explorar las suposiciones,
 *     armar el plan, comprar el plan de un mundo. UNO por pantalla, jamás dos:
 *     si hay dos héroes, no hay ninguno.
 *
 *  2. EL ESTÁNDAR (`BOTON_ESTANDAR`). Todo lo demás: guardar, cancelar, enviar,
 *     continuar, entrar, volver. Por decisión explícita del fundador, el
 *     secundario usa EL MISMO estilo y la MISMA animación que el principal:
 *     dentro de una página todos los botones son iguales. La jerarquía no la
 *     carga el color de un botón contra otro, la carga el héroe contra el
 *     resto.
 *
 * EL AZUL ES TINTA, NO MANCHA: el acento relleno bajo texto blanco se lee
 * lavado (una superficie grande de color saturado peleando con el blanco). El
 * mismo azul como borde y texto sobre fondo tenue se lee limpio. Cuando un
 * héroe SÍ se llena de azul al pasar el ratón, su texto invierte a NEGRO, que
 * es la única forma de que un relleno azul no se lave.
 *
 * Aquí vive solo el COLOR y el comportamiento; el tamaño, el radio y el peso
 * los pone cada sitio, porque dependen de dónde esté el botón.
 */

/** El botón de todos los días. También el de "cancelar": todos iguales. */
export const BOTON_ESTANDAR = "border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20";

/** Alias histórico: antes de ago 2026 el secundario era un contorno neutro. Se
 * mantiene el nombre para que ningún sitio quede a medias, pero apunta al
 * MISMO estilo (esa es justamente la decisión). */
export const BOTON_SECUNDARIO = BOTON_ESTANDAR;
export const BOTON_PRIMARIO = BOTON_ESTANDAR;
