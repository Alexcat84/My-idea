/**
 * /api/project/[id]/numeros - FASE B (canon 14): Tus Numeros como TABLERO
 * VIVO. GET devuelve el tablero determinista vigente (gratis, instantaneo).
 * POST recalcula, opcionalmente corrige cifras, re-narra con el modelo, y/o
 * activa el potenciador. Tres amarres del fundador:
 *   1. Activacion IDEMPOTENTE (db.activarTusNumeros, WHERE atomico): el ancla
 *      del cobro una vez por idea (ETAPA 2) no marca ni cobra dos veces.
 *   2. Cada version de cifras se INSERTA, jamas se actualiza: la historia no
 *      se reescribe. Re-narrar archiva la anterior como una fila propia.
 *   3. El tope diario de re-narraciones responde en palabras de persona y
 *      JAMAS bloquea el recalculo determinista, gratis e ilimitado por ley.
 */
import { NextResponse } from "next/server";
import type { NumerosProyecto, TipoOferta } from "@/lib/calculadora";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { costoAcumuladoUsd, usoVacio } from "@/lib/costmeter";
import { cobrar, mensajeSaldoInsuficiente, verificarSaldo } from "@/lib/creditos";
import {
  actualizarProyecto,
  activarTusNumeros,
  contarNarracionesHoy,
  historialVersionesNumeros,
  insertarVersionNumeros,
  obtenerProyecto,
  obtenerVersionNumeros,
  registrarBitacora,
  ultimaVersionNumeros,
} from "@/lib/db";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { PRECIOS } from "@/lib/precios";
import { narrarReporte } from "@/lib/engine/reporte";
import { cifrasCambiaron, MENSAJE_TOPE_RENARRACION, TOPE_RENARRACION_DIA, veredictoNumeros } from "@/lib/numerosVivo";
import { armarTablero } from "@/lib/tableroNumeros";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

// Campos numericos que el recolector (canon 14) puede corregir. Cualquier
// otra clave se ignora: el tablero no acepta datos que el motor no conoce.
const CAMPOS_EDITABLES = new Set([
  "costo_materiales_unidad",
  "horas_por_unidad",
  "valor_hora",
  "precio_tentativo",
  "capacidad_semanal",
  "costos_fijos_mensuales",
  "unidades_vendidas",
  "precio_pagado_real",
  "dias_inventario",
  "dias_cobro_clientes",
  "dias_pago_proveedores",
]);

function esNumeroValido(n: unknown): n is number {
  return typeof n === "number" && Number.isFinite(n) && n >= 0;
}

/** Valida y funde las correcciones sobre las cifras vigentes. Solo toca los
 * campos de la lista; preserva unidad/texto_original de lo que ya habia. */
function fundirCifras(
  entrada: unknown,
  existentes: NumerosProyecto
): { numeros: NumerosProyecto; error?: string } {
  if (typeof entrada !== "object" || entrada === null) {
    return { numeros: existentes, error: "'numeros' debe ser un objeto de campo: valor" };
  }
  const fusion: NumerosProyecto = { ...existentes };
  const ts = new Date().toISOString();
  for (const [campo, bruto] of Object.entries(entrada as Record<string, unknown>)) {
    if (!CAMPOS_EDITABLES.has(campo)) continue;
    let valor: number | { min: number; max: number };
    if (esNumeroValido(bruto)) {
      valor = bruto;
    } else if (
      typeof bruto === "object" &&
      bruto !== null &&
      esNumeroValido((bruto as { min?: unknown }).min) &&
      esNumeroValido((bruto as { max?: unknown }).max) &&
      (bruto as { min: number }).min <= (bruto as { max: number }).max
    ) {
      valor = { min: (bruto as { min: number }).min, max: (bruto as { max: number }).max };
    } else {
      return { numeros: existentes, error: `el valor de '${campo}' debe ser un numero >= 0 o un rango {min, max}` };
    }
    const previo = existentes[campo];
    fusion[campo] = {
      valor,
      unidad: previo?.unidad ?? null,
      texto_original: previo?.texto_original ?? null,
      session_id: null,
      updated_at: ts,
    };
  }
  return { numeros: fusion };
}

async function cargarContexto(projectId: string) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return { error: NextResponse.json({ error: "no autenticado" }, { status: 401 }) };
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return { error: NextResponse.json({ error: "idea no encontrada" }, { status: 404 }) };
  return { supabase, user, proyecto };
}

/** Arma el payload de lectura del tablero (deterministico) sobre unas cifras. */
function payloadTablero(numeros: NumerosProyecto, tipoOferta: TipoOferta, unidad: string | null) {
  const tablero = armarTablero(numeros, tipoOferta);
  return { tablero, veredicto: veredictoNumeros(tablero, unidad) };
}

/** Los valores declarados de los campos editables, para PRE-LLENAR el
 * recolector con lo ultimo que dijo el usuario (canon 14: nunca en blanco). */
function cifrasDeclaradas(numeros: NumerosProyecto): Record<string, number | { min: number; max: number }> {
  const out: Record<string, number | { min: number; max: number }> = {};
  for (const campo of CAMPOS_EDITABLES) {
    const v = numeros[campo]?.valor;
    if (v !== null && v !== undefined) out[campo] = v as number | { min: number; max: number };
  }
  return out;
}

/** Resumen de una version para la lista "Versiones anteriores": fecha +
 * veredicto + margen, TODO del snapshot guardado (cero recalculo). El
 * diferenciador de la fila es el contenido, no el reloj. */
function resumenVersion(
  v: { id: string; created_at: string; calculo: unknown | null },
  vigente: boolean
) {
  const c = (v.calculo ?? {}) as { veredicto?: { tono?: string }; margen?: unknown };
  return { id: v.id, fecha: v.created_at, tono: c.veredicto?.tono ?? null, margen: c.margen ?? null, vigente };
}

export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const ctx = await cargarContexto(projectId);
  if ("error" in ctx) return ctx.error;
  const { supabase, proyecto } = ctx;

  // ETAPA 2 — la compuerta del canon 07: sin activacion, el tablero no se
  // muestra. La pantalla pinta la compuerta ("Sacar mis numeros · 2
  // creditos") y el POST {activar:true} verifica saldo, activa y cobra.
  if (proyecto.tus_numeros_activado_at == null) {
    return NextResponse.json({
      project_id: projectId,
      titulo: proyecto.titulo,
      unidad: proyecto.unidad_venta ?? null,
      activado: false,
      compuerta: true,
      costo: PRECIOS.tus_numeros,
    });
  }

  // VISITAR una version pasada (?version=<id>): modo LECTURA. Se devuelve su
  // snapshot inmutable tal cual quedo, sin recalcular. Editar el pasado no
  // existe: el que corrige es siempre el presente.
  const versionId = new URL(request.url).searchParams.get("version");
  if (versionId) {
    const version = await obtenerVersionNumeros(supabase, projectId, versionId);
    if (!version || !version.calculo) {
      return NextResponse.json({ error: "esa version no existe" }, { status: 404 });
    }
    const calculo = version.calculo as Record<string, unknown> & { veredicto?: unknown };
    return NextResponse.json({
      project_id: projectId,
      titulo: proyecto.titulo,
      unidad: proyecto.unidad_venta ?? null,
      historico: true,
      tablero: calculo, // el snapshot ES el tablero (calculo = {...tablero, veredicto})
      veredicto: calculo.veredicto ?? null,
      cifras_fecha: version.created_at,
    });
  }

  const numeros: NumerosProyecto = proyecto.numeros_proyecto ?? {};
  const tipoOferta = (proyecto.tipo_oferta ?? null) as TipoOferta;
  const { tablero, veredicto } = payloadTablero(numeros, tipoOferta, proyecto.unidad_venta ?? null);
  const ultima = await ultimaVersionNumeros(supabase, projectId);
  const historialRaw = await historialVersionesNumeros(supabase, projectId);
  // La primera (mas reciente) es la VIGENTE: la que se ve arriba. La UI lista
  // solo las pasadas; la vigente vive en el tablero principal, no como fila.
  const historial = historialRaw.map((v, i) => resumenVersion(v, i === 0));

  return NextResponse.json({
    project_id: projectId,
    titulo: proyecto.titulo,
    unidad: proyecto.unidad_venta ?? null,
    tablero,
    veredicto,
    numeros_declarados: cifrasDeclaradas(numeros),
    narracion: ultima?.narracion ?? null,
    narracion_at: ultima?.narracion_at ?? null,
    cifras_fecha: ultima?.created_at ?? null,
    activado: proyecto.tus_numeros_activado_at != null,
    historial,
  });
}

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { numeros?: unknown; tipo_oferta?: unknown; narrar?: unknown; activar?: unknown } = {};
  try {
    const texto = await request.text();
    if (texto.trim().length > 0) body = JSON.parse(texto);
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
  }

  const ctx = await cargarContexto(projectId);
  if ("error" in ctx) return ctx.error;
  const { supabase, user, proyecto } = ctx;

  // ETAPA 2 (la frontera): Tus Numeros es motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(AVISO_LOGIN, { status: 401 });
  }

  const tipoOferta = (proyecto.tipo_oferta ?? null) as TipoOferta;
  const unidad = proyecto.unidad_venta ?? null;

  // ETAPA 2 — la compuerta: sin activacion no hay tablero. Activar cuesta
  // tus_numeros (2), UNA vez por idea; despues, recalculos y correcciones
  // son gratis por ley.
  const yaActivado = proyecto.tus_numeros_activado_at != null;
  if (!yaActivado && body.activar !== true) {
    return NextResponse.json(
      { compuerta: true, costo: PRECIOS.tus_numeros, error: "Tus Números se activa una vez por idea." },
      { status: 409 }
    );
  }

  // 1) Corregir cifras (opcional): funde y valida sobre lo vigente.
  let numeros: NumerosProyecto = proyecto.numeros_proyecto ?? {};
  if (body.numeros !== undefined) {
    const { numeros: fundidas, error } = fundirCifras(body.numeros, numeros);
    if (error) return NextResponse.json({ error }, { status: 400 });
    numeros = fundidas;
  }

  // 2) Activacion (ETAPA 2, VIVO): verificar >=2 al activar; consumir 2 a la
  //    entrega de ESTE primer tablero (la respuesta de este request), UNA vez
  //    por idea. Idempotente doble: activarTusNumeros (WHERE IS NULL atomico)
  //    + la clave `numeros:{projectId}` en el ledger. La carrera rara
  //    (verifico y otra pestana gasto antes): entregar y registrar.
  let activadoAhora = false;
  let activadoAt = proyecto.tus_numeros_activado_at ?? null;
  let creditosRestantes: number | null = null;
  if (body.activar === true) {
    if (!yaActivado) {
      const saldoNum = await verificarSaldo(user.id, PRECIOS.tus_numeros);
      if (!saldoNum.alcanza) {
        return NextResponse.json(
          { error: mensajeSaldoInsuficiente(saldoNum.creditos, PRECIOS.tus_numeros), saldo: saldoNum.creditos },
          { status: 402 }
        );
      }
    }
    const r = await activarTusNumeros(supabase, projectId);
    activadoAhora = r.activadoAhora;
    activadoAt = r.activadoAt;
    if (activadoAhora) {
      const resultadoCobro = await cobrar(user.id, "tus_numeros", PRECIOS.tus_numeros, `numeros:${projectId}`);
      if (resultadoCobro === -1) {
        await registrarBitacora(supabase, projectId, "cobro_carrera", {
          concepto: "tus_numeros",
          monto: PRECIOS.tus_numeros,
        });
      } else {
        creditosRestantes = resultadoCobro;
      }
    }
  }

  // 3) Recalculo determinista: SIEMPRE, gratis, sin tope ni bloqueo.
  const { tablero, veredicto } = payloadTablero(numeros, tipoOferta, unidad);

  // Persistencia de cifras: si cambiaron respecto de la ultima version,
  // guarda las nuevas como vigentes en projects.
  const ultima = await ultimaVersionNumeros(supabase, projectId);
  const hayCambio = body.numeros !== undefined && cifrasCambiaron(numeros, ultima?.numeros);
  if (hayCambio) {
    await actualizarProyecto(supabase, projectId, { numeros_proyecto: numeros });
  }

  // 4) Re-narracion (opcional): el modelo escribe la prosa. El guardian GIGO
  //    manda: con datos inconsistentes no se narra una conclusion confiable.
  //    El tope diario responde en palabras y NO toca el recalculo de arriba.
  let narracion: string | null = null;
  let narracionAt: string | null = null;
  let limiteAlcanzado = false;
  let mensaje: string | null = null;
  if (body.narrar === true) {
    if (tablero.gigo.inconsistente) {
      mensaje = "No narro una conclusión con estos datos: revisa el guardián de datos y corrige la cifra que no cuadra.";
    } else {
      const hoy = await contarNarracionesHoy(supabase, projectId);
      if (hoy >= TOPE_RENARRACION_DIA) {
        limiteAlcanzado = true;
        mensaje = MENSAJE_TOPE_RENARRACION;
      } else {
        const client = createAnthropicClient();
        const r = await narrarReporte(client, tablero.reporte, numeros, tipoOferta, usoVacio());
        narracion = r.contenido;
        narracionAt = new Date().toISOString();
        void costoAcumuladoUsd(r.acumulado); // presupuesto propio del reporte, no el de sesion
      }
    }
  }

  // 5) INSERT de version (jamas UPDATE): cuando cambiaron las cifras o cuando
  //    hubo una narracion nueva. La fila es un snapshot inmutable.
  let cifrasFecha = ultima?.created_at ?? null;
  if (hayCambio || narracion !== null) {
    const calculoSnapshot = { ...tablero, veredicto };
    await insertarVersionNumeros(supabase, projectId, {
      numeros,
      tipoOferta,
      calculo: calculoSnapshot,
      narracion,
      narracionAt,
    });
    cifrasFecha = new Date().toISOString();
  }

  const historialRaw = await historialVersionesNumeros(supabase, projectId);
  const historial = historialRaw.map((v, i) => resumenVersion(v, i === 0));

  return NextResponse.json({
    project_id: projectId,
    titulo: proyecto.titulo,
    unidad,
    tablero,
    veredicto,
    numeros_declarados: cifrasDeclaradas(numeros),
    narracion: narracion ?? (hayCambio ? null : ultima?.narracion ?? null),
    narracion_at: narracionAt ?? (hayCambio ? null : ultima?.narracion_at ?? null),
    cifras_fecha: cifrasFecha,
    activado: activadoAt != null,
    activado_ahora: activadoAhora,
    limite_relecturas: limiteAlcanzado,
    creditos_restantes: creditosRestantes,
    mensaje,
    historial,
  });
}
