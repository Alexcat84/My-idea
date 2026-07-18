/**
 * palancas.ts - FASE B (canon 14, "Tus Numeros"): las TRES PALANCAS.
 *
 * Capa de POLITICA sobre los primitivos inversos de calculadora.ts. Decide
 * a QUE apunta cada palanca (los primitivos solo hacen la aritmetica); es
 * deterministica y CERO LLM, fiel al sello del canon ("los numeros los hace
 * codigo, no la IA"). Los primitivos inversos tienen paridad Python (C1);
 * esta capa de presentacion es solo de la pantalla web, no del CLI.
 *
 * POLITICA DEL FUNDADOR (2026-07-17), ajustable con datos de la beta:
 *  - En PERDIDA o AJUSTE (margen por debajo del piso), las palancas de precio
 *    y costo son un ARREGLO: apuntan a LLEGAR al piso de margen sano. El copy
 *    puede sonar a recomendacion firme ("sube el precio a X").
 *  - Ya SANO, son un TEST, no un decreto: un empujon modesto (~10%) que el
 *    usuario prueba, no una orden. El copy debe sonar a experimento ("prueba
 *    subiendo a X, ~10%: con tus ventas de hoy serian +$Y al mes").
 *  - La palanca de volumen es honesta: con margen <= 0 va BLOQUEADA (vender
 *    mas agranda la perdida, canon 14); con margen positivo muestra el techo
 *    de capacidad declarado y su ganancia.
 *  - Recomendada: la de precio cuando el margen es el problema (perdida o
 *    ajuste); la de volumen cuando el margen ya es sano y toca crecer.
 *
 * REDONDEO HUMANO (amarre del fundador): TODA cifra recomendada que llega a
 * la pantalla se muestra redonda ($435, no $434.78; $27, no $26.6), y el
 * margen resultante se RECALCULA sobre el numero redondo, para que lo que se
 * ve sea verdad y no una aproximacion. La matematica intermedia es exacta;
 * el redondeo ocurre una vez, aqui, antes de recomputar el margen mostrado.
 */
import {
  costoMaximoParaMargenObjetivo,
  costoUnitarioTotal,
  margenConCosto,
  margenConPrecio,
  margenUnitario,
  precioParaMargenObjetivo,
  techoIngresoCapacidad,
  unidadesParaGananciaObjetivo,
  type NumerosProyecto,
  type Rango,
  type TipoOferta,
  type ValorNumerico,
} from "./calculadora";

// Politica del fundador (2026-07-17). Constantes con nombre a proposito:
// se mueven aqui, con datos de la beta, sin tocar la logica.
export const PISO_MARGEN_SANO = 0.3; // margen (fraccion del precio) que define "sano"
export const TEST_PRECIO_SANO = 0.1; // empujon de ~10% para el test de precio/costo ya sano

export type EstadoNumeros = "datos" | "perdida" | "ajuste" | "sano";
export type ModoPalanca = "arreglo" | "test";

function esRango(v: ValorNumerico | null | undefined): v is Rango {
  return typeof v === "object" && v !== null && "min" in v && "max" in v;
}

/** Colapsa un valor (numero o rango) a un escalar representativo, para las
 * DECISIONES de politica (estado, recomendada) y el redondeo mostrado. */
function medio(v: ValorNumerico | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return esRango(v) ? (v.min + v.max) / 2 : v;
}

/**
 * Redondeo humano de una cifra recomendada (amarre del fundador). El paso
 * crece con la magnitud: centavos no, numeros "de tienda" si. Ej. 26.6 -> 27,
 * 434.78 -> 435, 385 -> 385, 3900 -> 3900.
 */
export function redondearHumano(n: number): number {
  const abs = Math.abs(n);
  const paso = abs < 30 ? 1 : abs < 1000 ? 5 : 50;
  return Math.round(n / paso) * paso;
}

export interface MargenResultante {
  valor: ValorNumerico | null;
  porcentaje: ValorNumerico | null;
}

export interface Palanca {
  clave: "precio" | "costo" | "volumen";
  /** "arreglo" (llegar al piso, copy firme) o "test" (empujon ~10%, copy de experimento). */
  modo: ModoPalanca;
  bloqueada: boolean;
  razonBloqueo?: string;
  /** El numero objetivo YA REDONDEADO: precio o costo ($) para precio/costo;
   * unidades/mes para volumen. */
  meta: ValorNumerico | null;
  /** El valor de hoy, para el "desde": precio actual, costo actual. */
  actual: ValorNumerico | null;
  /** Margen a la meta REDONDEADA (palancas precio y costo). */
  margenResultante?: MargenResultante;
  /** Ganancia mensual a la meta de volumen, ya redondeada (palanca volumen). */
  gananciaResultante?: number | null;
  /** Ventas/mes para cubrir los fijos al nuevo precio (palanca precio). */
  ventasParaCubrirFijos?: number | null;
  recomendada: boolean;
}

export interface Palancas {
  estado: EstadoNumeros;
  /** El piso de margen sano (30%) que define el estado. */
  pisoMargenSanoPct: number;
  precio: Palanca;
  costo: Palanca;
  volumen: Palanca;
}

function valorCampo(numeros: NumerosProyecto, campo: string): ValorNumerico | null {
  const entry = numeros[campo];
  if (!entry || entry.valor === null || entry.valor === undefined) return null;
  return entry.valor;
}

/**
 * Construye las tres palancas del canon 14 a partir de numeros_proyecto.
 * `opciones` permite mover el piso y el empujon del test sin tocar el codigo
 * (defaults PISO_MARGEN_SANO / TEST_PRECIO_SANO). Nunca inventa cifras: cada
 * numero sale de un primitivo de calculadora.ts, y lo mostrado va redondo.
 */
export function construirPalancas(
  numeros: NumerosProyecto,
  tipoOferta?: TipoOferta,
  opciones?: { pisoMargenSano?: number; testPrecioSano?: number }
): Palancas {
  const piso = opciones?.pisoMargenSano ?? PISO_MARGEN_SANO;
  const test = opciones?.testPrecioSano ?? TEST_PRECIO_SANO;

  const costoActual = costoUnitarioTotal(numeros, tipoOferta).valor;
  const precioActual = valorCampo(numeros, "precio_tentativo");
  const margen = margenUnitario(numeros, tipoOferta);
  const margenPctMedio = medio(margen.porcentaje);
  const margenValMedio = medio(margen.valor);
  const fijosMedio = medio(valorCampo(numeros, "costos_fijos_mensuales"));

  let estado: EstadoNumeros;
  if (margenPctMedio === null) estado = "datos";
  else if (margenValMedio !== null && margenValMedio <= 0) estado = "perdida";
  else if (margenPctMedio < piso * 100) estado = "ajuste";
  else estado = "sano";

  const esArreglo = estado === "perdida" || estado === "ajuste";
  const modo: ModoPalanca = esArreglo ? "arreglo" : "test";

  // ── Palanca precio ────────────────────────────────────────────────────
  // Arreglo: precio para llegar al piso. Test (ya sano): empujon de ~10%.
  let precioMetaExacto: ValorNumerico | null = null;
  if (esArreglo) {
    precioMetaExacto = precioParaMargenObjetivo(numeros, piso, tipoOferta).valor;
  } else if (estado === "sano" && precioActual !== null && !esRango(precioActual)) {
    precioMetaExacto = (precioActual as number) * (1 + test);
  }
  let precioMeta: ValorNumerico | null = precioMetaExacto;
  let margenAlPrecio = null;
  if (precioMeta !== null && !esRango(precioMeta)) {
    precioMeta = redondearHumano(precioMeta as number);
    margenAlPrecio = margenConPrecio(numeros, precioMeta as number, tipoOferta);
  }
  const margenAlPrecioMedio = margenAlPrecio ? medio(margenAlPrecio.valor) : null;
  const ventasParaCubrirFijos =
    margenAlPrecioMedio !== null && margenAlPrecioMedio > 0 && fijosMedio !== null
      ? Math.ceil(fijosMedio / margenAlPrecioMedio)
      : null;
  const precio: Palanca = {
    clave: "precio",
    modo,
    bloqueada: false,
    meta: precioMeta,
    actual: precioActual,
    margenResultante: margenAlPrecio
      ? { valor: margenAlPrecio.valor, porcentaje: margenAlPrecio.porcentaje }
      : { valor: null, porcentaje: null },
    ventasParaCubrirFijos,
    recomendada: esArreglo,
  };

  // ── Palanca costo ─────────────────────────────────────────────────────
  let costoMetaExacto: ValorNumerico | null = null;
  if (esArreglo) {
    costoMetaExacto = costoMaximoParaMargenObjetivo(numeros, piso).valor;
  } else if (estado === "sano" && costoActual !== null && !esRango(costoActual)) {
    costoMetaExacto = (costoActual as number) * (1 - test);
  }
  let costoMeta: ValorNumerico | null = costoMetaExacto;
  let margenAlCosto = null;
  if (costoMeta !== null && !esRango(costoMeta)) {
    costoMeta = redondearHumano(costoMeta as number);
    margenAlCosto = margenConCosto(numeros, costoMeta as number);
  }
  const costo: Palanca = {
    clave: "costo",
    modo,
    bloqueada: false,
    meta: costoMeta,
    actual: costoActual,
    margenResultante: margenAlCosto
      ? { valor: margenAlCosto.valor, porcentaje: margenAlCosto.porcentaje }
      : { valor: null, porcentaje: null },
    recomendada: false,
  };

  // ── Palanca volumen ───────────────────────────────────────────────────
  // Honesta: con margen <= 0, bloqueada. Con margen positivo, el techo de
  // capacidad declarado y su ganancia (ambos redondos).
  let volumen: Palanca;
  if (margenValMedio === null || margenValMedio <= 0) {
    volumen = {
      clave: "volumen",
      modo,
      bloqueada: true,
      razonBloqueo:
        "Con el margen en rojo, el volumen agranda la perdida. Primero arregla el margen; cuando este en verde, aqui va cuantas unidades al mes necesitas para tu meta.",
      meta: null,
      actual: null,
      recomendada: false,
    };
  } else {
    const techoUnidadesMedio = medio(techoIngresoCapacidad(numeros).unidades_mes);
    let metaUnidades: number | null = null;
    let ganancia: number | null = null;
    if (techoUnidadesMedio !== null) {
      metaUnidades = redondearHumano(techoUnidadesMedio);
      if (fijosMedio !== null) ganancia = redondearHumano(metaUnidades * margenValMedio - fijosMedio);
    }
    volumen = {
      clave: "volumen",
      modo,
      bloqueada: false,
      meta: metaUnidades,
      actual: null,
      gananciaResultante: ganancia,
      recomendada: estado === "sano",
    };
  }

  // Garantia: exactamente una recomendada.
  if (volumen.recomendada) precio.recomendada = false;
  if (!precio.recomendada && !volumen.recomendada) precio.recomendada = true;

  return { estado, pisoMargenSanoPct: piso * 100, precio, costo, volumen };
}

/** Unidades/mes para cubrir los fijos (el punto de equilibrio "para no
 * perder" del tile del canon). Reexport comodo: unidadesParaGananciaObjetivo(0). */
export function unidadesParaNoPerder(numeros: NumerosProyecto, tipoOferta?: TipoOferta): number | Rango | null {
  return unidadesParaGananciaObjetivo(numeros, 0, tipoOferta).valor;
}
