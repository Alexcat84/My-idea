/**
 * reporte.ts - Fase 3.0: port de las funciones deterministicas y de IA de
 * modo_reporte (--reporte) en engine/prototipo_motor.py: la
 * mini-entrevista parametrizada por tipo_oferta/unidad_venta, el
 * guardian GIGO textual (numeros ya marcados inconsistentes por
 * calculadora.ts), el respaldo offline, y la narracion final con Sonnet.
 * calculadora.ts (Motor v2.2, ya portado) hace todo el calculo numerico;
 * este modulo es la capa de lenguaje alrededor de esos resultados.
 */
import type Anthropic from "@anthropic-ai/sdk";
import type { NumerosProyecto, ReporteCalculado, TipoOferta } from "../calculadora";
import { llamarClaude, MODEL, MODEL_HAIKU, PRESUPUESTO_REPORTE_USD, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_CLASIFICAR_OFERTA, SYSTEM_REPORTE } from "../prompts";
import { elegir, LOCALE_BASE, type Locale } from "../i18n/config";
import { interpolar } from "../i18n/interpolar";
import { REPORTE } from "../i18n/mensajes/reporte";
import { MOTOR } from "../i18n/mensajes/motor";
import {
  CAMPOS_ESENCIALES_POR_TIPO,
  FRASES_NO_APLICA_MOLDE,
  TIPOS_OFERTA_VALIDOS,
  type CampoNumericoProyecto,
} from "./constants";

/** Deterministico (sin LLM): true si la respuesta indica que la pregunta
 * actual no encaja con el tipo de oferta del usuario. */
export function detectarNoAplica(texto: string | null | undefined): boolean {
  const t = (texto ?? "").trim().toLowerCase();
  return FRASES_NO_APLICA_MOLDE.some((f) => t.includes(f));
}

/** Tres plantillas parametrizadas por unidad_venta (la palabra literal
 * del usuario: pieza, cliente, pack, suscripcion...). */
export function preguntasPorTipo(
  tipoOferta: string | null | undefined,
  unidadVenta: string | null | undefined,
  idioma: Locale = LOCALE_BASE
): Record<string, string> {
  const t = elegir(REPORTE, idioma);
  const u = unidadVenta || t.unidadPorOmision;
  // producto_fisico y default (tipo_oferta null: proyectos pre-v2.2)
  const plantillas: Record<string, string> =
    tipoOferta === "servicio"
      ? t.preguntas.servicio
      : tipoOferta === "digital"
        ? t.preguntas.digital
        : t.preguntas.productoFisico;
  return Object.fromEntries(Object.entries(plantillas).map(([campo, p]) => [campo, interpolar(p, { u })]));
}

/** Guardian GIGO (a): cada campo capturado en la mini-entrevista guarda
 * la unidad que la PREGUNTA misma establecio -- deterministico, no
 * depende de que el usuario la repita. */
export function unidadDeclaradaCampo(
  campo: CampoNumericoProyecto,
  tipoOferta: string | null | undefined,
  unidadVenta: string | null | undefined,
  /** i18n F5: el idioma de la idea (el de las plantillas). */
  idioma: Locale = LOCALE_BASE
): string {
  const t = elegir(MOTOR, idioma).unidadCampo;
  const u = unidadVenta || t.unidad;
  if (campo === "costos_fijos_mensuales") return t.porMes;
  if (campo === "valor_hora") return t.porHora;
  if (campo === "unidades_vendidas") return tipoOferta === "digital" ? interpolar(t.alMes, { u }) : u;
  return interpolar(t.porUnidad, { u });
}

/** Extractor deterministico (SIN LLM) de un numero en lenguaje natural:
 * '$8', '8 dolares', '8.5', 'unos 8'. null si no hay numero reconocible o
 * el usuario dijo que no sabe. Las comas se tratan como separador de
 * miles, no decimal. */
export function extraerNumero(texto: string): number | null {
  const t = texto.trim().toLowerCase();
  if (!t) return null;
  const frasesNoSabe = ["no se", "no sé", "no lo se", "no lo sé", "ni idea", "no tengo idea", "no idea"];
  if (frasesNoSabe.some((p) => t.includes(p))) return null;
  const m = t.match(/\$?\s*(\d[\d,]*\.?\d*)/);
  if (!m) return null;
  const n = Number(m[1].replace(/,/g, ""));
  return Number.isNaN(n) ? null : n;
}

export interface ResultadoClasificarOferta {
  tipo: string | null;
  unidad: string | null;
  acumulado: UsoAcumulado;
}

/** Reclasifica tipo_oferta/unidad_venta a partir de una frase libre.
 * Llamada barata a Haiku; si falla, devuelve (null, null) y el llamador
 * sigue con el tipo por defecto (producto_fisico). */
export async function clasificarOferta(
  client: Anthropic,
  texto: string,
  acumulado: UsoAcumulado,
  /** i18n F5: la unidad de venta se muestra: en el idioma de la idea. */
  idiomaSalida: string | null = null
): Promise<ResultadoClasificarOferta> {
  try {
    const r = await llamarClaude(client, SYSTEM_CLASIFICAR_OFERTA, texto, MODEL_HAIKU, acumulado, {
      maxTokens: 150,
      componente: "turnos",
      presupuestoUsd: PRESUPUESTO_REPORTE_USD,
      idiomaSalida,
    });
    const data = parsearJson<{ tipo_oferta?: string; unidad_venta?: string }>(r.texto);
    const tipo = data.tipo_oferta && TIPOS_OFERTA_VALIDOS.has(data.tipo_oferta) ? data.tipo_oferta : null;
    const unidad = data.unidad_venta ? String(data.unidad_venta).trim() : null;
    return { tipo, unidad, acumulado: r.acumulado };
  } catch {
    return { tipo: null, unidad: null, acumulado };
  }
}

export function camposEsencialesPorTipo(tipoOferta: string | null | undefined): CampoNumericoProyecto[] {
  return CAMPOS_ESENCIALES_POR_TIPO[tipoOferta ?? ""] ?? CAMPOS_ESENCIALES_POR_TIPO.producto_fisico;
}

/** Guardian GIGO (Motor v2.2): cuando detectarInconsistenciaGigo marca
 * los numeros como probablemente mal capturados, el reporte NO narra
 * ninguna conclusion financiera -- 100% deterministico a proposito, para
 * no arriesgar que el narrador intente "ser creativo" con datos que ya
 * sabemos que estan rotos. */
export function reporteGigoInconsistente(motivo: string, numeros: NumerosProyecto, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(REPORTE, idioma);
  const partes: string[] = [
    t.tusNumerosHoy,
    "",
    t.gigo.algoNoCuadra,
    "",
    `> ${motivo}`,
    "",
    t.gigo.noVoyACalcular,
    "",
    t.gigo.losNumerosQueDiste,
    "",
  ];
  for (const [campo, entry] of Object.entries(numeros)) {
    if (entry.valor !== null && entry.valor !== undefined) {
      partes.push(`- ${campo}: ${JSON.stringify(entry.valor)}`);
    }
  }
  partes.push("", t.gigo.losQueTeFaltanComo, "", t.gigo.revisa);
  return partes.join("\n");
}

/** Respaldo sin IA (fallo de red/presupuesto): los numeros crudos del
 * modulo, sin narracion. */
export function reporteOffline(resultados: ReporteCalculado, idioma: Locale = LOCALE_BASE): string {
  const t = elegir(REPORTE, idioma);
  const partes: string[] = [t.tusNumerosHoy, ""];
  const { costo_unitario: costo, margen, punto_equilibrio: equilibrio, capacidad } = resultados;
  if (costo.valor !== null) partes.push(interpolar(t.offline.costo, { valor: JSON.stringify(costo.valor) }));
  if (margen.valor !== null) {
    partes.push(
      interpolar(t.offline.margen, { valor: JSON.stringify(margen.valor), porcentaje: String(JSON.stringify(margen.porcentaje)) })
    );
  }
  if (equilibrio.valor !== null) partes.push(interpolar(t.offline.equilibrio, { valor: JSON.stringify(equilibrio.valor) }));
  if (capacidad.ingreso !== null) {
    partes.push(
      interpolar(t.offline.techo, {
        ingreso: JSON.stringify(capacidad.ingreso),
        unidades: String(JSON.stringify(capacidad.unidades_mes)),
      })
    );
  }
  const faltantes = new Set<string>();
  for (const r of Object.values(resultados)) {
    for (const f of (r as { insumos_faltantes?: string[] }).insumos_faltantes ?? []) faltantes.add(f);
  }
  if (faltantes.size > 0) {
    partes.push("", t.offline.losQueTeFaltan, "");
    for (const f of [...faltantes].sort()) partes.push(`- ${f}`);
  }
  return partes.join("\n");
}

export interface ResultadoNarracion {
  contenido: string;
  acumulado: UsoAcumulado;
  /** AUD-09 M20: true si la IA no narró y el contenido es el ensamblado sin
   * narrar. Quien llama decide qué hacer, pero nunca lo presenta como narración. */
  sinIA: boolean;
}

/** UNA llamada Sonnet narra los resultados YA CALCULADOS por
 * calculadora.ts (nunca genera cifras nuevas). Respaldo offline si falla
 * la llamada o si el presupuesto propio del reporte ($0.10) ya se agoto. */
export async function narrarReporte(
  client: Anthropic,
  resultados: ReporteCalculado,
  numeros: NumerosProyecto,
  tipoOferta: TipoOferta,
  acumulado: UsoAcumulado,
  idioma: Locale = LOCALE_BASE,
  /** i18n F5: el idioma de la idea, en que narra la IA. */
  idiomaSalida: string | null = null
): Promise<ResultadoNarracion> {
  const payload = {
    resultados,
    numeros_proyecto_declarados: Object.fromEntries(Object.entries(numeros).map(([c, v]) => [c, v.valor])),
    tipo_oferta: tipoOferta ?? null,
  };
  try {
    const r = await llamarClaude(client, SYSTEM_REPORTE, JSON.stringify(payload), MODEL, acumulado, {
      maxTokens: 1800,
      componente: "reporte",
      presupuestoUsd: PRESUPUESTO_REPORTE_USD,
      idiomaSalida,
    });
    return { contenido: r.texto.trim() + elegir(MOTOR, idioma).reporteDisclaimer, acumulado: r.acumulado, sinIA: false };
  } catch (e) {
    // AUD-09 M20: antes este catch era mudo. Deja rastro y se marca.
    console.error("[reporte] la narracion con IA fallo; queda el ensamblado sin narrar:", e);
    return { contenido: reporteOffline(resultados, idioma) + elegir(MOTOR, idioma).reporteDisclaimer, acumulado, sinIA: true };
  }
}
