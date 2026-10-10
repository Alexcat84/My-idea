/**
 * NUMEROS POR CODIGO (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 2). Las cifras de la persona
 * le llegan al redactor hechas y etiquetadas por codigo, en dos bloques del payload:
 *  - numeros_de_la_persona: cada cifra guardada (numeros_proyecto + los de la sesion) con lo que dijo tal cual, su
 *    ALCANCE leido de su propia frase (canal, periodo, tamaño, si incluye su tiempo) y lo que NO es;
 *  - calculos: lo que la calculadora ya hizo (costo por unidad, margen, punto de equilibrio) y lo que falta para hacerlo.
 * La regla del redactor: esas son las unicas cifras del negocio que puede usar, con su alcance, y no deduce otras.
 * Casos reales: "12 macetas al mes por Instagram" leido como venta total (M2A-f006-1, M2B-f002-2, M3A-f014-1); un costo
 * con la hora incluida leido como costo de materiales (aad2749d, c6e51feec).
 */
import {
  costoUnitarioTotal,
  margenUnitario,
  puntoEquilibrioUnidadesMes,
  type NumerosProyecto,
  type TipoOferta,
  type ValorNumerico,
} from "../calculadora";
import { esCostoQueIncluyeTiempo } from "./interprete";

/** Que es cada campo, en palabras llanas, y lo que nunca es por si mismo. */
const CAMPOS: Record<string, { que: string; noEs: string[] }> = {
  unidades_vendidas: { que: "unidades que dijo que vende", noEs: [] },
  costo_materiales_unidad: { que: "costo de materiales por unidad", noEs: ["no incluye su tiempo de trabajo"] },
  horas_por_unidad: { que: "horas de trabajo por unidad", noEs: [] },
  valor_hora: { que: "lo que vale su hora de trabajo", noEs: [] },
  precio_tentativo: { que: "precio al que vende o piensa vender cada unidad", noEs: ["no es lo que le queda: eso es el margen"] },
  precio_pagado_real: { que: "precio que un cliente le pagó de verdad", noEs: [] },
  capacidad_semanal: { que: "unidades que puede hacer por semana", noEs: ["no es lo que vende: es lo que podría hacer"] },
  costos_fijos_mensuales: { que: "costos fijos del mes (los paga aunque no venda)", noEs: [] },
};

const ETIQUETA_FALTA: Record<string, string> = {
  costo_materiales_unidad: "costo de materiales por unidad",
  horas_por_unidad: "horas por unidad",
  valor_hora: "valor de su hora",
  precio_tentativo: "precio por unidad",
  costos_fijos_mensuales: "costos fijos del mes",
};

export interface Alcance {
  canal: string | null;
  periodo: string | null;
  tamano: string | null;
  incluyeTiempo: boolean;
}

const CANALES =
  /\b(?:por|en|a través de|via|vía)\s+((?:la |el |su |mi |una |un |las |los )?(?:instagram|facebook|tiktok|whatsapp|mercado ?libre|amazon|etsy|shopify|internet|línea|linea|redes(?: sociales)?|(?:mi |su |la )?(?:web|página|pagina)|tienda(?:s)?(?: de [\p{L} ]+?)?|feria(?:s)?(?: [\p{L}]+)?|mercado(?:s)?(?: [\p{L}]+)?|bazar(?:es)?))(?=[\s,.;:)]|$)/iu;
const MARCAS: Record<string, string> = {
  instagram: "Instagram", facebook: "Facebook", tiktok: "TikTok", whatsapp: "WhatsApp", amazon: "Amazon", etsy: "Etsy",
  shopify: "Shopify", "mercado libre": "Mercado Libre", mercadolibre: "Mercado Libre",
};
const PERIODOS = /\b(al mes|por mes|cada mes|mensual(?:es)?|a la semana|por semana|cada semana|semanal(?:es)?|al día|al dia|por día|por dia|diari[oa]s?|al año|al ano|por año|por ano|anual(?:es)?)\b/iu;
const TAMANOS = /\b(chic[oa]s?|pequeñ[oa]s?|median[oa]s?|grandes?)\b/iu;

/** El alcance que dice la propia frase de la persona. Lo que la frase no dice queda en null. */
export function alcanceDe(texto: string | null | undefined): Alcance {
  const t = (texto ?? "").trim();
  const canal = t.match(CANALES)?.[1]?.replace(/^(?:su |mi )/i, "") ?? null;
  return {
    canal: canal ? (MARCAS[canal.toLowerCase()] ?? canal) : null,
    periodo: t.match(PERIODOS)?.[1]?.toLowerCase() ?? null,
    tamano: t.match(TAMANOS)?.[1]?.toLowerCase() ?? null,
    incluyeTiempo: esCostoQueIncluyeTiempo(t),
  };
}

const esRango = (v: unknown): v is { min: number; max: number } =>
  typeof v === "object" && v !== null && "min" in v && "max" in v;
const num = (x: number) => (Number.isInteger(x) ? String(x) : String(Math.round(x * 100) / 100));
const textoValor = (v: ValorNumerico) => (esRango(v) ? `de ${num(v.min)} a ${num(v.max)}` : num(v as number));

export interface FilaNumero {
  campo: string;
  que: string;
  valor: string;
  lo_que_dijo: string | null;
  alcance: string[];
  que_no_es: string[];
}

/** Cada cifra guardada de la persona, etiquetada. Los campos que no conoce no entran. */
export function numerosDeLaPersona(numeros: unknown): FilaNumero[] {
  const n = (numeros && typeof numeros === "object" ? numeros : {}) as Record<string, { valor?: unknown; unidad?: unknown; texto_original?: unknown }>;
  const filas: FilaNumero[] = [];
  for (const [campo, def] of Object.entries(CAMPOS)) {
    const c = n[campo];
    if (!c || c.valor === null || c.valor === undefined) continue;
    if (typeof c.valor !== "number" && !esRango(c.valor)) continue;
    const dijo = typeof c.texto_original === "string" && c.texto_original.trim() ? c.texto_original.trim() : null;
    const a = alcanceDe(dijo);
    const alcance: string[] = [];
    if (a.canal) alcance.push(`canal: ${a.canal}`);
    if (a.periodo) alcance.push(`período: ${a.periodo}`);
    if (a.tamano) alcance.push(`tamaño: ${a.tamano}`);
    if (a.incluyeTiempo) alcance.push("incluye su tiempo");
    const noEs = [...def.noEs];
    if (campo === "unidades_vendidas" && a.canal) noEs.push(`no es su venta total por todos sus canales: es solo lo de ${a.canal}`);
    if (a.tamano) noEs.push(`no vale para otros tamaños: es de las ${a.tamano}`);
    if (campo === "costo_materiales_unidad" && a.incluyeTiempo) {
      noEs.splice(noEs.indexOf("no incluye su tiempo de trabajo"), 1);
      noEs.push("no es solo materiales: según lo que dijo, incluye su tiempo");
    }
    const unidad = typeof c.unidad === "string" && c.unidad.trim() ? ` ${c.unidad.trim()}` : "";
    filas.push({ campo, que: def.que, valor: textoValor(c.valor as ValorNumerico) + unidad, lo_que_dijo: dijo, alcance, que_no_es: noEs });
  }
  return filas;
}

export interface Calculo {
  que: string;
  estado: "calculado" | "pendiente";
  valor?: string;
  como: string;
  falta?: string[];
}

/** Lo que la calculadora ya hizo con sus cifras, y lo que falta para lo demás. */
export function calculosDelPlan(numeros: unknown, tipoOferta?: TipoOferta): Calculo[] {
  const n = (numeros && typeof numeros === "object" ? numeros : {}) as NumerosProyecto;
  const falta = (xs: string[]) => xs.map((x) => ETIQUETA_FALTA[x] ?? x);
  const costo = costoUnitarioTotal(n, tipoOferta);
  const margen = margenUnitario(n, tipoOferta);
  const equilibrio = puntoEquilibrioUnidadesMes(n, tipoOferta);
  const pct = (p: ValorNumerico | null) =>
    p === null ? "" : esRango(p) ? ` (${num(p.min)} a ${num(p.max)} % del precio)` : ` (${num(p as number)} % del precio)`;
  const comoCosto = tipoOferta === "digital" ? "costo variable por unidad" : "materiales + horas por unidad × valor de su hora";
  return [
    costo.valor !== null
      ? { que: "costo por unidad", estado: "calculado", valor: textoValor(costo.valor), como: comoCosto }
      : { que: "costo por unidad", estado: "pendiente", como: comoCosto, falta: falta(costo.insumos_faltantes) },
    margen.valor !== null
      ? { que: "margen por unidad", estado: "calculado", valor: textoValor(margen.valor) + pct(margen.porcentaje), como: "precio - costo por unidad" }
      : { que: "margen por unidad", estado: "pendiente", como: "precio - costo por unidad", falta: falta(margen.insumos_faltantes) },
    equilibrio.valor !== null
      ? { que: "punto de equilibrio", estado: "calculado", valor: `${textoValor(equilibrio.valor)} unidades al mes`, como: "costos fijos del mes / margen por unidad, hacia arriba" }
      : { que: "punto de equilibrio", estado: "pendiente", como: "costos fijos del mes / margen por unidad", falta: falta(equilibrio.insumos_faltantes) },
  ];
}
