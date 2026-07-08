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
import {
  CAMPOS_ESENCIALES_POR_TIPO,
  FRASES_NO_APLICA_MOLDE,
  REPORTE_DISCLAIMER,
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
  unidadVenta: string | null | undefined
): Record<string, string> {
  const u = unidadVenta || "unidad";
  if (tipoOferta === "servicio") {
    return {
      costo_materiales_unidad: `¿Cuánto te cuesta directamente cada ${u} (insumos, materiales que uses, etc.)? Un número aproximado sirve; si no tienes, responde 0.`,
      horas_por_unidad: `¿Cuántas horas de trabajo te toma cada ${u}?`,
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: `¿A qué precio cobras (o cobrarías) cada ${u}?`,
      capacidad_semanal: `¿Cuántas veces de ${u} puedes atender en una semana normal?`,
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    };
  }
  if (tipoOferta === "digital") {
    return {
      costos_fijos_mensuales:
        "¿Cuánto gastas al mes en costos fijos de infraestructura (hosting, APIs, herramientas, suscripciones)?",
      costo_materiales_unidad: `¿Tienes algún costo variable por cada ${u} (por ejemplo, costo de API por uso)? Si es prácticamente cero, responde 0.`,
      precio_tentativo: `¿A qué precio o ingreso promedio vendes (o venderías) cada ${u}?`,
      unidades_vendidas: `¿Cuántas de ${u} tienes hoy, o cuál sería una meta mensual realista?`,
    };
  }
  // producto_fisico y default (tipo_oferta null: proyectos pre-v2.2)
  return {
    costo_materiales_unidad: `¿Cuánto gastas en materiales por ${u}, más o menos? Un número aproximado sirve.`,
    horas_por_unidad: `¿Cuántas horas de trabajo te toma cada ${u}, de principio a fin?`,
    valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
    precio_tentativo: `¿A qué precio venderías (o vendes) cada ${u}?`,
    capacidad_semanal: `¿Cuántas de ${u} puedes producir en una semana normal?`,
    costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
  };
}

/** Guardian GIGO (a): cada campo capturado en la mini-entrevista guarda
 * la unidad que la PREGUNTA misma establecio -- deterministico, no
 * depende de que el usuario la repita. */
export function unidadDeclaradaCampo(
  campo: CampoNumericoProyecto,
  tipoOferta: string | null | undefined,
  unidadVenta: string | null | undefined
): string {
  const u = unidadVenta || "unidad";
  if (campo === "costos_fijos_mensuales") return "por mes";
  if (campo === "valor_hora") return "por hora";
  if (campo === "unidades_vendidas") return tipoOferta === "digital" ? `${u}/mes` : u;
  return `por ${u}`;
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
  acumulado: UsoAcumulado
): Promise<ResultadoClasificarOferta> {
  try {
    const r = await llamarClaude(client, SYSTEM_CLASIFICAR_OFERTA, texto, MODEL_HAIKU, acumulado, {
      maxTokens: 150,
      componente: "turnos",
      presupuestoUsd: PRESUPUESTO_REPORTE_USD,
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
export function reporteGigoInconsistente(motivo: string, numeros: NumerosProyecto): string {
  const partes: string[] = [
    "## Tus números hoy",
    "",
    "Antes de calcular nada, encontré algo que no cuadra en estos números:",
    "",
    `> ${motivo}`,
    "",
    "No voy a calcular margen ni punto de equilibrio con estos datos: el resultado " +
      "sería una cifra que suena precisa pero está mal, y eso es peor que no tener el " +
      "cálculo. Prefiero decírtelo con honestidad.",
    "",
    "## Los números que diste",
    "",
  ];
  for (const [campo, entry] of Object.entries(numeros)) {
    if (entry.valor !== null && entry.valor !== undefined) {
      partes.push(`- ${campo}: ${JSON.stringify(entry.valor)}`);
    }
  }
  partes.push(
    "",
    "## Los números que te faltan (y cómo conseguirlos)",
    "",
    "Revisa si alguno de los números de arriba está en una unidad distinta a la que " +
      "esperaba el reporte (por ejemplo, un gasto mensual anotado como costo por unidad, " +
      "o un plazo en meses anotado como horas), corrígelo, y vuelve a generar el reporte " +
      "con la cifra corregida."
  );
  return partes.join("\n");
}

/** Respaldo sin IA (fallo de red/presupuesto): los numeros crudos del
 * modulo, sin narracion. */
export function reporteOffline(resultados: ReporteCalculado): string {
  const partes: string[] = ["## Tus números hoy", ""];
  const { costo_unitario: costo, margen, punto_equilibrio: equilibrio, capacidad } = resultados;
  if (costo.valor !== null) partes.push(`- Costo por unidad: ${JSON.stringify(costo.valor)}`);
  if (margen.valor !== null) partes.push(`- Margen por unidad: ${JSON.stringify(margen.valor)} (${JSON.stringify(margen.porcentaje)}%)`);
  if (equilibrio.valor !== null) partes.push(`- Punto de equilibrio: ${JSON.stringify(equilibrio.valor)} unidades/mes`);
  if (capacidad.ingreso !== null) {
    partes.push(`- Techo de ingreso mensual: ${JSON.stringify(capacidad.ingreso)} (${JSON.stringify(capacidad.unidades_mes)} unidades/mes)`);
  }
  const faltantes = new Set<string>();
  for (const r of Object.values(resultados)) {
    for (const f of (r as { insumos_faltantes?: string[] }).insumos_faltantes ?? []) faltantes.add(f);
  }
  if (faltantes.size > 0) {
    partes.push("", "## Los números que te faltan", "");
    for (const f of [...faltantes].sort()) partes.push(`- ${f}`);
  }
  return partes.join("\n");
}

export interface ResultadoNarracion {
  contenido: string;
  acumulado: UsoAcumulado;
}

/** UNA llamada Sonnet narra los resultados YA CALCULADOS por
 * calculadora.ts (nunca genera cifras nuevas). Respaldo offline si falla
 * la llamada o si el presupuesto propio del reporte ($0.10) ya se agoto. */
export async function narrarReporte(
  client: Anthropic,
  resultados: ReporteCalculado,
  numeros: NumerosProyecto,
  tipoOferta: TipoOferta,
  acumulado: UsoAcumulado
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
    });
    return { contenido: r.texto.trim() + REPORTE_DISCLAIMER, acumulado: r.acumulado };
  } catch {
    return { contenido: reporteOffline(resultados) + REPORTE_DISCLAIMER, acumulado };
  }
}
