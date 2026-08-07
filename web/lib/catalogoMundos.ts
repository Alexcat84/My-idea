/**
 * catalogoMundos — la ÚNICA puerta al catálogo de mundos.
 *
 * Antes cada pantalla importaba packs_catalog.json y hacía su propio `.find`
 * o su propio `.map`, y `ideas.ts` llegó a guardar una COPIA de los nombres
 * ("espejo de packs_catalog", decía su comentario). Una copia de nombres es
 * una copia que se separa: basta un mundo nuevo para que una pantalla lo
 * nombre y otra lo llame por su clave.
 *
 * Aquí viven las dos operaciones, que NO son la misma:
 *
 *   mundosVisibles()  — los que se LISTAN al usuario. Respeta `oculto`.
 *   mundo(clave)      — la resolución por clave. NO respeta `oculto`.
 *
 * La diferencia es deliberada. Un mundo oculto no aparece en ninguna vitrina,
 * pero si el fundador lo camina durante su mini-gate tiene que ver su nombre y
 * su promesa de verdad, no un hueco ni un "mundo desconocido". Ocultar es no
 * ofrecerlo; no es romperlo.
 *
 * La publicación es un interruptor del fundador: se quita `oculto` del pack en
 * packs_catalog.json y el mundo entra al catálogo. Nada más.
 *
 * AQUÍ NO HAY PRECIOS. El catálogo los llevaba y envejecieron en silencio
 * (decían 3 y 2 cuando se cobraban 5), porque quien cobra y quien pinta leen
 * precios.ts. Se quitaron en vez de alinearlos: dos copias del mismo número se
 * separan otra vez. Para el precio de un mundo, PRECIOS.mundo_activar.
 */
import catalogo from "./assets/packs_catalog.json";

export type Mundo = {
  clave: string;
  nombre: string;
  promesa: string;
  /** Ausente o false = publicado. true = existe y funciona, pero no se ofrece. */
  oculto?: boolean;
};

/** Todos, publicados u ocultos. Para resolver por clave, jamás para listar. */
export const MUNDOS: readonly Mundo[] = (catalogo as { packs: Mundo[] }).packs;

/**
 * Los que se le muestran al usuario. Esta es la lista de las vitrinas.
 *
 * `incluirOcultos` es la PUERTA DEL MINI-GATE, no una publicación. Un mundo
 * oculto no tiene tarjeta, y sin tarjeta no hay por dónde empezar su preview:
 * ocultarlo dejaría al propio fundador sin poder caminarlo antes de decidir si
 * lo publica, que es justo lo contrario de lo que se busca. Con la puerta
 * abierta el mundo aparece MARCADO como sin publicar, para que nadie confunda
 * un paseo de prueba con un mundo en venta.
 */
export function mundosVisibles(incluirOcultos = false): Mundo[] {
  return incluirOcultos ? [...MUNDOS] : MUNDOS.filter((m) => !m.oculto);
}

/** Resolución por clave: funciona también para los ocultos (ver cabecera). */
export function mundo(clave: string | null | undefined): Mundo | undefined {
  if (!clave) return undefined;
  return MUNDOS.find((m) => m.clave === clave);
}

/** El nombre de cara de un mundo, o su clave si no está en el catálogo. */
export function nombreDeMundo(clave: string): string {
  return mundo(clave)?.nombre ?? clave;
}

/** ¿Está publicado? Útil para los avisos del mini-gate, no para esconder. */
export function estaPublicado(clave: string): boolean {
  return !!mundo(clave) && !mundo(clave)!.oculto;
}
