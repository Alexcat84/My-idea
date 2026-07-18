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
import { construirPalancas, type EstadoNumeros, type Palancas } from "./palancas";

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
  puntoEquilibrio: number | Rango | null;
  puntoEquilibrioNota?: string;
  barra: BarraVerdad;
  palancas: Palancas;
  reporte: ReporteCalculado;
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
    puntoEquilibrio: equilibrio.valor,
    puntoEquilibrioNota: equilibrio.nota,
    barra: barraVerdad(medio(costoUnitario), medio(precio)),
    palancas,
    reporte,
    faltantes: faltantesDeReporte(reporte),
    gigo: detectarInconsistenciaGigo(numeros, tipoOferta),
  };
}
