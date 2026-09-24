/**
 * tableroNumeros.ts - FASE B (canon 14, "Tus Numeros"): arma el TABLERO
 * completo (el payload determinista que pinta la pantalla) desde
 * numeros_proyecto. CERO LLM: reune calculadora.ts (tiles, escenarios,
 * equilibrio, GIGO) y palancas.ts (los tres caminos) y deriva lo que falta
 * para el canon 14 (la barra de la verdad, la lista de faltantes). La
 * narracion en prosa (el veredicto calido, las notas) la agrega la ruta con
 * una llamada al modelo; aqui SOLO viven los numeros, que los hace codigo.
 */
import {
  calcularReporte,
  costoUnitarioTotal,
  detectarInconsistenciaGigo,
  margenUnitario,
  puntoEquilibrioUnidadesMes,
  type NumerosProyecto,
  type ReporteCalculado,
  type ResultadoGigo,
  type TipoOferta,
  type ValorNumerico,
  type Rango,
} from "./calculadora";
import { construirPalancas, gananciaNetaDeFijos, type EstadoNumeros, type Palancas } from "./palancas";

function esRango(v: ValorNumerico | null | undefined): v is Rango {
  return typeof v === "object" && v !== null && "min" in v && "max" in v;
}
function medio(v: ValorNumerico | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return esRango(v) ? (v.min + v.max) / 2 : v;
}

export interface BarraVerdad {
  /** Ancho % de la barra de costo, relativo a la mayor de las dos. */
  costoPct: number | null;
  /** Ancho % de la barra de precio, relativo a la mayor de las dos. */
  precioPct: number | null;
  /** true si el costo supera al precio (pinta la barra de costo en ambar). */
  enPerdida: boolean;
}

/** La barra de la verdad del canon 14: costo vs precio, ambas escaladas a la
 * mayor, para que el hueco (o el margen) se vea de un vistazo. */
export function barraVerdad(costo: number | null, precio: number | null): BarraVerdad {
  if (costo === null || precio === null || (costo <= 0 && precio <= 0)) {
    return { costoPct: null, precioPct: null, enPerdida: false };
  }
  const mayor = Math.max(costo, precio);
  const pct = (x: number) => Math.round((x / mayor) * 1000) / 10;
  return { costoPct: pct(costo), precioPct: pct(precio), enPerdida: costo > precio };
}

export interface FilaEscenario {
  nombre: string;
  sub: string;
  /** GANANCIA NETA del mes: contribucion (unidades x margen) MENOS los fijos,
   * ya redondeada. Es lo que el canon llama "Ganancia del mes" (el techo sano
   * de kits da $3.900 = 30 x 170 - 1.200), no la contribucion a secas. */
  ganancia: number | null;
  /** AUD-09 M43: por qué no hay cifra, en palabras (solo cuando faltan los
   * fijos: sin ellos no hay ganancia NETA que mostrar). */
  sinCifra?: string;
}

/**
 * Las filas de la tabla de escenarios (canon 14). Ganancia NETA de fijos.
 * La fila "Tu ritmo de hoy" (el volumen ACTUAL declarado) aparece SOLO si el
 * usuario declaro unidades_vendidas: jamas se inventa una base (el canon
 * ilustra, el motor confiesa). Sin ese dato, quedan las dos honestas
 * (pesimista y capacidad plena).
 */
export function construirEscenariosFilas(
  numeros: NumerosProyecto,
  reporte: ReporteCalculado,
  margenUnit: ValorNumerico | null,
  fijos: ValorNumerico | null
): FilaEscenario[] {
  // AUD-09 M43: sin fijos no hay ganancia NETA. Antes se tomaban como 0 y la
  // fila mostraba la contribución bajo "Ganancia" (la palanca de volumen ya
  // daba null en el mismo caso: dos cifras para lo mismo, H12).
  const f = medio(fijos);
  const neto = (contrib: number | null): number | null =>
    contrib === null || f === null ? null : gananciaNetaDeFijos(contrib, f);
  const sinFijos = f === null ? { sinCifra: "falta tu gasto fijo del mes" } : {};
  const esc = reporte.escenarios as unknown as Record<string, unknown>;
  const filas: FilaEscenario[] = [];
  if ("pesimista" in esc) {
    const p = esc.pesimista as { unidades_mes?: number; margen_mensual?: number | null } | null;
    const b = esc.base as { unidades_mes?: number; margen_mensual?: number | null } | null;
    if (p) filas.push({ nombre: "Pesimista", sub: `${p.unidades_mes} al mes`, ganancia: neto(p.margen_mensual ?? null), ...sinFijos });
    const uv = medio(valorCampo(numeros, "unidades_vendidas"));
    const mu = medio(margenUnit);
    if (uv !== null && mu !== null) {
      filas.push({ nombre: "Tu ritmo de hoy", sub: `${uv} al mes`, ganancia: neto(uv * mu), ...sinFijos });
    }
    if (b) filas.push({ nombre: "A capacidad plena", sub: `${b.unidades_mes} al mes`, ganancia: neto(b.margen_mensual ?? null), ...sinFijos });
  } else {
    for (const [k, etq] of [["50%", "mitad de tu meta"], ["100%", "tu meta"], ["200%", "el doble"]] as const) {
      const e = esc[k] as { unidades?: number; margen_total?: number | null } | null;
      if (e) filas.push({ nombre: etq, sub: `${e.unidades} al mes`, ganancia: neto(e.margen_total ?? null), ...sinFijos });
    }
  }
  return filas;
}

/** Los insumos que faltan, agregados y sin repetir, a traves de todos los
 * sub-calculos (mismo criterio que reporteOffline). */
export function faltantesDeReporte(reporte: ReporteCalculado): string[] {
  const set = new Set<string>();
  for (const r of Object.values(reporte)) {
    for (const f of (r as { insumos_faltantes?: string[] }).insumos_faltantes ?? []) set.add(f);
  }
  return [...set].sort();
}

export interface Tablero {
  estado: EstadoNumeros;
  /** Tiles "de un vistazo". */
  costoUnitario: ValorNumerico | null;
  precio: ValorNumerico | null;
  margen: ValorNumerico | null;
  margenPct: ValorNumerico | null;
  fijos: ValorNumerico | null;
  puntoEquilibrio: number | Rango | null;
  puntoEquilibrioNota?: string;
  barra: BarraVerdad;
  palancas: Palancas;
  reporte: ReporteCalculado;
  escenariosFilas: FilaEscenario[];
  /** El ciclo de conversión de efectivo en días (CCE), o null si faltan los
   * datos de cobro/inventario/pago. Cuando NO es null, la pantalla gana su
   * sección "Tu ciclo de caja": la recompensa visible de haberlos dado. */
  cicloDias: number | null;
  faltantes: string[];
  gigo: ResultadoGigo;
}

function valorCampo(numeros: NumerosProyecto, campo: string): ValorNumerico | null {
  const entry = numeros[campo];
  if (!entry || entry.valor === null || entry.valor === undefined) return null;
  return entry.valor;
}

/**
 * Arma el tablero determinista completo. `opciones` se pasa tal cual a las
 * palancas (piso/test ajustables). No lanza ante datos faltantes: cada pieza
 * reporta lo suyo (null + faltantes), fiel a como narra el guardian.
 */
export function armarTablero(
  numeros: NumerosProyecto,
  tipoOferta?: TipoOferta,
  opciones?: { pisoMargenSano?: number; testPrecioSano?: number }
): Tablero {
  const reporte = calcularReporte(numeros, tipoOferta);
  const palancas = construirPalancas(numeros, tipoOferta, opciones);
  const costoUnitario = costoUnitarioTotal(numeros, tipoOferta).valor;
  const precio = valorCampo(numeros, "precio_tentativo");
  const margen = margenUnitario(numeros, tipoOferta);
  const equilibrio = puntoEquilibrioUnidadesMes(numeros, tipoOferta);

  return {
    estado: palancas.estado,
    costoUnitario,
    precio,
    margen: margen.valor,
    margenPct: margen.porcentaje,
    fijos: valorCampo(numeros, "costos_fijos_mensuales"),
    puntoEquilibrio: equilibrio.valor,
    puntoEquilibrioNota: equilibrio.nota,
    barra: barraVerdad(medio(costoUnitario), medio(precio)),
    palancas,
    reporte,
    escenariosFilas: construirEscenariosFilas(numeros, reporte, margen.valor, valorCampo(numeros, "costos_fijos_mensuales")),
    cicloDias: typeof reporte.ciclo_conversion_efectivo.valor === "number" ? reporte.ciclo_conversion_efectivo.valor : null,
    faltantes: faltantesDeReporte(reporte),
    gigo: detectarInconsistenciaGigo(numeros, tipoOferta),
  };
}
