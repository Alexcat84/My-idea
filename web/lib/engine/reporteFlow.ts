/**
 * reporteFlow.ts - Fase 3.0: version RESUMIBLE de la mini-entrevista de
 * modo_reporte (--reporte) en prototipo_motor.py. El CLI la corre como un
 * while bloqueante dentro de un solo proceso; aqui cada llamada avanza
 * exactamente un paso (una pregunta respondida) y devuelve el estado
 * completo para que la ruta lo persista en projects.estado_reporte
 * (migration 010) entre una pregunta y la siguiente -- mismo patron que
 * recorrido.ts para el bucle principal de entrevista.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { detectarInconsistenciaGigo, calcularReporte, type NumerosProyecto, type TipoOferta } from "../calculadora";
import { type UsoAcumulado } from "../costmeter";
import { MAX_PREGUNTAS_REPORTE, PREGUNTA_TIPO_OFERTA, type CampoNumericoProyecto } from "./constants";
import {
  camposEsencialesPorTipo,
  clasificarOferta,
  detectarNoAplica,
  extraerNumero,
  narrarReporte,
  preguntasPorTipo,
  reporteGigoInconsistente,
  unidadDeclaradaCampo,
} from "./reporte";

export type FaseReporte = "clasificando_oferta" | "preguntando" | "reclasificando_molde";

export interface EstadoReporte {
  fase: FaseReporte;
  tipoOferta: string | null;
  unidadVenta: string | null;
  faltantesEsenciales: CampoNumericoProyecto[];
  idx: number;
  noAplicaCount: number;
  moldeCambiado: boolean;
}

interface TipoOfertaActualizado {
  tipoOferta: string;
  unidadVenta: string | null;
}

export type ResultadoPasoReporte =
  | {
      tipo: "pregunta";
      estado: EstadoReporte;
      pregunta: string;
      acumulado: UsoAcumulado;
      numeros: NumerosProyecto;
      tipoOfertaActualizado: TipoOfertaActualizado | null;
    }
  | {
      tipo: "reporte_listo";
      contenido: string;
      acumulado: UsoAcumulado;
      numeros: NumerosProyecto;
      tipoOfertaActualizado: TipoOfertaActualizado | null;
    };

async function generarContenidoReporte(
  client: Anthropic,
  numeros: NumerosProyecto,
  tipoOferta: string | null,
  acumulado: UsoAcumulado
): Promise<{ contenido: string; acumulado: UsoAcumulado }> {
  const gigo = detectarInconsistenciaGigo(numeros, tipoOferta as TipoOferta);
  if (gigo.inconsistente) {
    return { contenido: reporteGigoInconsistente(gigo.motivo ?? "", numeros), acumulado };
  }
  const resultados = calcularReporte(numeros, tipoOferta as TipoOferta);
  const r = await narrarReporte(client, resultados, numeros, tipoOferta as TipoOferta, acumulado);
  return { contenido: r.contenido, acumulado: r.acumulado };
}

function calcularFaltantes(
  tipoOferta: string | null,
  numeros: NumerosProyecto
): CampoNumericoProyecto[] {
  const camposEsenciales = camposEsencialesPorTipo(tipoOferta);
  return camposEsenciales.filter((c) => !(c in numeros)).slice(0, MAX_PREGUNTAS_REPORTE);
}

/** Primer paso: si el proyecto no tiene tipo_oferta, pregunta que vende
 * antes que nada. Si ya lo tiene (o cuando la clasificacion inicial ya se
 * proceso), arma la lista de campos faltantes y pregunta el primero, o
 * genera el reporte de una vez si no falta nada. */
export async function iniciarReporte(
  client: Anthropic,
  numeros: NumerosProyecto,
  tipoOferta: string | null,
  unidadVenta: string | null,
  acumulado: UsoAcumulado
): Promise<ResultadoPasoReporte> {
  if (!tipoOferta) {
    const estado: EstadoReporte = {
      fase: "clasificando_oferta",
      tipoOferta: null,
      unidadVenta,
      faltantesEsenciales: [],
      idx: 0,
      noAplicaCount: 0,
      moldeCambiado: false,
    };
    return {
      tipo: "pregunta",
      estado,
      pregunta: PREGUNTA_TIPO_OFERTA,
      acumulado,
      numeros,
      tipoOfertaActualizado: null,
    };
  }
  return continuarConTipoConocido(client, numeros, tipoOferta, unidadVenta, 0, false, acumulado);
}

async function continuarConTipoConocido(
  client: Anthropic,
  numeros: NumerosProyecto,
  tipoOferta: string | null,
  unidadVenta: string | null,
  noAplicaCount: number,
  moldeCambiado: boolean,
  acumulado: UsoAcumulado
): Promise<ResultadoPasoReporte> {
  const faltantesEsenciales = calcularFaltantes(tipoOferta, numeros);
  if (faltantesEsenciales.length === 0) {
    const { contenido, acumulado: acumuladoFinal } = await generarContenidoReporte(client, numeros, tipoOferta, acumulado);
    return { tipo: "reporte_listo", contenido, acumulado: acumuladoFinal, numeros, tipoOfertaActualizado: null };
  }
  const preguntas = preguntasPorTipo(tipoOferta, unidadVenta);
  const estado: EstadoReporte = {
    fase: "preguntando",
    tipoOferta,
    unidadVenta,
    faltantesEsenciales,
    idx: 0,
    noAplicaCount,
    moldeCambiado,
  };
  return {
    tipo: "pregunta",
    estado,
    pregunta: preguntas[faltantesEsenciales[0]],
    acumulado,
    numeros,
    tipoOfertaActualizado: null,
  };
}

/** Avanza un paso dado el estado persistido y la respuesta del usuario a
 * estado.pregunta (la pregunta actual, reconstruible por el llamador). */
export async function avanzarReporte(
  client: Anthropic,
  estado: EstadoReporte,
  numeros: NumerosProyecto,
  respuesta: string,
  acumulado: UsoAcumulado
): Promise<ResultadoPasoReporte> {
  if (estado.fase === "clasificando_oferta") {
    const r = await clasificarOferta(client, respuesta, acumulado);
    // Igual que Python: si la clasificacion falla, tipo_oferta queda null
    // (nunca se fuerza a "producto_fisico") -- las tablas de consulta
    // (camposEsencialesPorTipo/preguntasPorTipo) ya tratan null como ese
    // default, y calculadora.ts trata null igual que producto_fisico/
    // servicio en cada formula, asi que el resultado numerico no cambia.
    const tipoOferta = r.tipo;
    const unidadVenta = r.unidad ?? estado.unidadVenta;
    const tipoOfertaActualizado: TipoOfertaActualizado | null = r.tipo
      ? { tipoOferta: r.tipo, unidadVenta }
      : null;
    const resultado = await continuarConTipoConocido(client, numeros, tipoOferta, unidadVenta, 0, false, r.acumulado);
    return { ...resultado, tipoOfertaActualizado: resultado.tipoOfertaActualizado ?? tipoOfertaActualizado };
  }

  if (estado.fase === "reclasificando_molde") {
    const r = await clasificarOferta(client, respuesta, acumulado);
    if (r.tipo && r.tipo !== estado.tipoOferta) {
      const unidadVenta = r.unidad ?? estado.unidadVenta;
      const resultado = await continuarConTipoConocido(client, numeros, r.tipo, unidadVenta, 0, true, r.acumulado);
      return { ...resultado, tipoOfertaActualizado: { tipoOferta: r.tipo, unidadVenta } };
    }
    // Sin cambio de tipo: seguimos con la MISMA lista, avanzando un campo.
    const siguienteIdx = estado.idx + 1;
    if (siguienteIdx >= estado.faltantesEsenciales.length) {
      const tipoOferta = estado.tipoOferta;
      const { contenido, acumulado: acumuladoFinal } = await generarContenidoReporte(
        client,
        numeros,
        tipoOferta,
        r.acumulado
      );
      return { tipo: "reporte_listo", contenido, acumulado: acumuladoFinal, numeros, tipoOfertaActualizado: null };
    }
    const preguntas = preguntasPorTipo(estado.tipoOferta, estado.unidadVenta);
    const nuevoEstado: EstadoReporte = { ...estado, fase: "preguntando", idx: siguienteIdx, moldeCambiado: true };
    return {
      tipo: "pregunta",
      estado: nuevoEstado,
      pregunta: preguntas[estado.faltantesEsenciales[siguienteIdx]],
      acumulado: r.acumulado,
      numeros,
      tipoOfertaActualizado: null,
    };
  }

  // fase === "preguntando"
  const campo = estado.faltantesEsenciales[estado.idx];
  if (detectarNoAplica(respuesta)) {
    const noAplicaCount = estado.noAplicaCount + 1;
    if (noAplicaCount >= 2 && !estado.moldeCambiado) {
      const nuevoEstado: EstadoReporte = { ...estado, noAplicaCount, fase: "reclasificando_molde" };
      return {
        tipo: "pregunta",
        estado: nuevoEstado,
        pregunta: PREGUNTA_TIPO_OFERTA,
        acumulado,
        numeros,
        tipoOfertaActualizado: null,
      };
    }
    const siguienteIdx = estado.idx + 1;
    if (siguienteIdx >= estado.faltantesEsenciales.length) {
      const tipoOferta = estado.tipoOferta;
      const { contenido, acumulado: acumuladoFinal } = await generarContenidoReporte(client, numeros, tipoOferta, acumulado);
      return { tipo: "reporte_listo", contenido, acumulado: acumuladoFinal, numeros, tipoOfertaActualizado: null };
    }
    const preguntas = preguntasPorTipo(estado.tipoOferta, estado.unidadVenta);
    const nuevoEstado: EstadoReporte = { ...estado, noAplicaCount, idx: siguienteIdx };
    return {
      tipo: "pregunta",
      estado: nuevoEstado,
      pregunta: preguntas[estado.faltantesEsenciales[siguienteIdx]],
      acumulado,
      numeros,
      tipoOfertaActualizado: null,
    };
  }

  const valor = extraerNumero(respuesta);
  const numerosActualizados = { ...numeros };
  if (valor !== null) {
    numerosActualizados[campo] = {
      valor,
      unidad: unidadDeclaradaCampo(campo, estado.tipoOferta, estado.unidadVenta),
      texto_original: respuesta,
      session_id: null,
      updated_at: new Date().toISOString(),
    };
  }
  const siguienteIdx = estado.idx + 1;
  if (siguienteIdx >= estado.faltantesEsenciales.length) {
    const tipoOferta = estado.tipoOferta;
    const { contenido, acumulado: acumuladoFinal } = await generarContenidoReporte(
      client,
      numerosActualizados,
      tipoOferta,
      acumulado
    );
    return {
      tipo: "reporte_listo",
      contenido,
      acumulado: acumuladoFinal,
      numeros: numerosActualizados,
      tipoOfertaActualizado: null,
    };
  }
  const preguntas = preguntasPorTipo(estado.tipoOferta, estado.unidadVenta);
  const nuevoEstado: EstadoReporte = { ...estado, idx: siguienteIdx };
  return {
    tipo: "pregunta",
    estado: nuevoEstado,
    pregunta: preguntas[estado.faltantesEsenciales[siguienteIdx]],
    acumulado,
    numeros: numerosActualizados,
    tipoOfertaActualizado: null,
  };
}
