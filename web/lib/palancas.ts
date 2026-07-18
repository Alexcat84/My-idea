/**
 * palancas.ts - FASE B (canon 14, "Tus Numeros"): las TRES PALANCAS.
 *
 * Capa de POLITICA sobre los primitivos inversos de calculadora.ts. Decide
 * a QUE apunta cada palanca (los primitivos solo hacen la aritmetica); es
 * deterministica y CERO LLM, fiel al sello del canon ("los numeros los hace
 * codigo, no la IA"). Los primitivos inversos tienen paridad Python (C1);
 * esta capa de presentacion es solo de la pantalla web, no del CLI.
 *
 * POLITICA (por defecto, ajustable con las constantes de abajo):
 *  - "margen sano" = 30%. Si estas en perdida o por debajo del piso, las
 *    palancas de precio y costo apuntan a LLEGAR al piso. Si ya estas sano,
 *    apuntan a un ESTIRON de +10 puntos sobre tu margen actual.
 *  - La palanca de volumen es honesta: con margen <= 0 va BLOQUEADA (vender
 *    mas agranda la perdida, canon 14); con margen sano muestra el techo de
 *    capacidad que declaraste y la ganancia a ese volumen.
 *  - Recomendada: la de precio cuando el margen es el problema (perdida o
 *    ajuste); la de volumen cuando el margen ya es sano y toca crecer.
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

export const MARGEN_SANO_OBJETIVO = 0.3; // piso de "margen sano" (30% del precio)
export const ESTIRON_SOBRE_ACTUAL = 0.1; // +10 puntos cuando ya estas sano

export type EstadoNumeros = "datos" | "perdida" | "ajuste" | "sano";

function esRango(v: ValorNumerico | null | undefined): v is Rango {
  return typeof v === "object" && v !== null && "min" in v && "max" in v;
}

/** Colapsa un valor (numero o rango) a un escalar representativo, para las
 * DECISIONES de politica (estado, recomendada). El valor que se MUESTRA
 * conserva su rango; solo las ramas logicas usan el punto medio. */
function medio(v: ValorNumerico | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return esRango(v) ? (v.min + v.max) / 2 : v;
}

export interface MargenResultante {
  valor: ValorNumerico | null;
  porcentaje: ValorNumerico | null;
}

export interface Palanca {
  clave: "precio" | "costo" | "volumen";
  bloqueada: boolean;
  razonBloqueo?: string;
  /** El numero objetivo: precio o costo ($) para precio/costo; unidades/mes para volumen. */
  meta: ValorNumerico | null;
  /** El valor de hoy, para el "desde": precio actual, costo actual, o unidades actuales. */
  actual: ValorNumerico | null;
  /** Margen a la meta (palancas precio y costo). */
  margenResultante?: MargenResultante;
  /** Ganancia mensual a la meta de volumen (palanca volumen). */
  gananciaResultante?: number | null;
  /** Ventas/mes para cubrir los fijos al nuevo precio (palanca precio). */
  ventasParaCubrirFijos?: number | null;
  recomendada: boolean;
}

export interface Palancas {
  estado: EstadoNumeros;
  margenObjetivoPct: number;
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
 * `opciones.margenSano` permite mover el piso sin tocar el codigo (default
 * MARGEN_SANO_OBJETIVO). Nunca inventa cifras: cada numero sale de un
 * primitivo de calculadora.ts.
 */
export function construirPalancas(
  numeros: NumerosProyecto,
  tipoOferta?: TipoOferta,
  opciones?: { margenSano?: number }
): Palancas {
  const margenSano = opciones?.margenSano ?? MARGEN_SANO_OBJETIVO;

  const costoActual = costoUnitarioTotal(numeros, tipoOferta).valor;
  const precioActual = valorCampo(numeros, "precio_tentativo");
  const margen = margenUnitario(numeros, tipoOferta);
  const margenPctMedio = medio(margen.porcentaje);
  const margenValMedio = medio(margen.valor);

  let estado: EstadoNumeros;
  if (margenPctMedio === null) estado = "datos";
  else if (margenValMedio !== null && margenValMedio <= 0) estado = "perdida";
  else if (margenPctMedio < margenSano * 100) estado = "ajuste";
  else estado = "sano";

  // Objetivo de las palancas precio/costo: llegar al piso si estas por
  // debajo; un estiron sobre tu margen actual si ya estas sano.
  const margenObjetivoFrac =
    estado === "sano" && margenPctMedio !== null
      ? Math.min(0.95, margenPctMedio / 100 + ESTIRON_SOBRE_ACTUAL)
      : margenSano;
  const margenObjetivoPct = Math.round(margenObjetivoFrac * 1000) / 10;

  // Palanca precio: sube el precio a X para alcanzar el margen objetivo.
  const precioMeta = precioParaMargenObjetivo(numeros, margenObjetivoFrac, tipoOferta).valor;
  const margenAlPrecio =
    precioMeta !== null && !esRango(precioMeta) ? margenConPrecio(numeros, precioMeta, tipoOferta) : null;
  const margenAlPrecioMedio = margenAlPrecio ? medio(margenAlPrecio.valor) : null;
  const fijos = valorCampo(numeros, "costos_fijos_mensuales");
  const fijosMedio = medio(fijos);
  const ventasParaCubrirFijos =
    margenAlPrecioMedio !== null && margenAlPrecioMedio > 0 && fijosMedio !== null
      ? Math.ceil(fijosMedio / margenAlPrecioMedio)
      : null;
  const precio: Palanca = {
    clave: "precio",
    bloqueada: false,
    meta: precioMeta,
    actual: precioActual,
    margenResultante: margenAlPrecio
      ? { valor: margenAlPrecio.valor, porcentaje: margenAlPrecio.porcentaje }
      : { valor: null, porcentaje: null },
    ventasParaCubrirFijos,
    recomendada: estado === "perdida" || estado === "ajuste",
  };

  // Palanca costo: baja el costo a Y para alcanzar el margen objetivo al
  // precio de hoy.
  const costoMeta = costoMaximoParaMargenObjetivo(numeros, margenObjetivoFrac).valor;
  const margenAlCosto =
    costoMeta !== null && !esRango(costoMeta) ? margenConCosto(numeros, costoMeta) : null;
  const costo: Palanca = {
    clave: "costo",
    bloqueada: false,
    meta: costoMeta,
    actual: costoActual,
    margenResultante: margenAlCosto
      ? { valor: margenAlCosto.valor, porcentaje: margenAlCosto.porcentaje }
      : { valor: null, porcentaje: null },
    recomendada: false,
  };

  // Palanca volumen: honesta. Con margen <= 0, bloqueada (vender mas agranda
  // la perdida). Con margen positivo, apunta al techo de capacidad declarado.
  let volumen: Palanca;
  if (estado === "perdida" || margenValMedio === null || margenValMedio <= 0) {
    volumen = {
      clave: "volumen",
      bloqueada: true,
      razonBloqueo:
        "Con el margen en rojo, el volumen agranda la perdida. Primero arregla el margen; cuando este en verde, aqui va cuantas unidades al mes necesitas para tu meta.",
      meta: null,
      actual: null,
      recomendada: false,
    };
  } else {
    const techo = techoIngresoCapacidad(numeros);
    const techoUnidades = techo.unidades_mes;
    const techoUnidadesMedio = medio(techoUnidades);
    let ganancia: number | null = null;
    if (techoUnidadesMedio !== null && margenValMedio !== null && fijosMedio !== null) {
      ganancia = Math.round(techoUnidadesMedio * margenValMedio - fijosMedio);
    }
    volumen = {
      clave: "volumen",
      bloqueada: false,
      meta: techoUnidades,
      actual: null,
      gananciaResultante: ganancia,
      recomendada: estado === "sano",
    };
  }

  // Garantia: exactamente una recomendada. Si el volumen es la recomendada,
  // el precio deja de serlo.
  if (volumen.recomendada) {
    precio.recomendada = false;
  }
  if (!precio.recomendada && !volumen.recomendada) {
    // estado "datos" u otros bordes: recae en precio como la mas directa.
    precio.recomendada = true;
  }

  return { estado, margenObjetivoPct, precio, costo, volumen };
}

/** Unidades/mes para cubrir los fijos (el punto de equilibrio "para no
 * perder" del tile del canon). Reexport comodo: es unidadesParaGananciaObjetivo(0). */
export function unidadesParaNoPerder(numeros: NumerosProyecto, tipoOferta?: TipoOferta): number | Rango | null {
  return unidadesParaGananciaObjetivo(numeros, 0, tipoOferta).valor;
}
