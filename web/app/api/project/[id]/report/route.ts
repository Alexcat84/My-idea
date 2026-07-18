/**
 * POST /api/project/[id]/report - Fase 3.0: port de modo_reporte
 * (--reporte PROJECT_ID) en engine/prototipo_motor.py. Inventario de
 * numeros_proyecto/tipo_oferta, mini-entrevista deterministica
 * parametrizada por tipo_oferta con el guardian GIGO de mold-abort-and-
 * switch (reporteFlow.ts), calculadora.ts (Motor v2.2) calcula todo lo
 * posible, y una llamada Sonnet narra los resultados YA CALCULADOS
 * (nunca genera cifras nuevas). Presupuesto propio ($0.10), independiente
 * del presupuesto de sesion de la entrevista principal.
 *
 * Igual que el spec de Fase 3.0 pide: la mini-entrevista se devuelve
 * pregunta por pregunta al cliente (no se corre en bucle server-side como
 * el CLI) -- cada llamada a esta ruta es un paso, con el progreso
 * persistido en projects.estado_reporte (migration 010) entre pasos.
 */
import { NextResponse } from "next/server";
import type { NumerosProyecto } from "@/lib/calculadora";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { costoAcumuladoUsd, PRESUPUESTO_REPORTE_USD, usoVacio } from "@/lib/costmeter";
import { actualizarProyecto, cerrarSesion, crearSesion, guardarPlan, obtenerProyecto } from "@/lib/db";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { avanzarReporte, iniciarReporte } from "@/lib/engine/reporteFlow";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: unknown = {};
  try {
    const texto = await request.text();
    if (texto.trim().length > 0) body = JSON.parse(texto);
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
  }
  const respuesta = (body as { respuesta?: unknown } | null)?.respuesta;
  if (respuesta !== undefined && (typeof respuesta !== "string" || respuesta.trim().length === 0)) {
    return NextResponse.json({ error: "'respuesta' debe ser un string no vacio" }, { status: 400 });
  }
  if (typeof respuesta === "string" && respuesta.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'respuesta' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
      { status: 400 }
    );
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  // ETAPA 2 (la frontera): motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(AVISO_LOGIN, { status: 401 });
  }

  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "proyecto no encontrado" }, { status: 404 });
  }

  const client = createAnthropicClient();
  const numeros: NumerosProyecto = proyecto.numeros_proyecto ?? {};

  let resultado;
  if (respuesta === undefined) {
    if (proyecto.estado_reporte) {
      return NextResponse.json(
        { error: "ya hay una entrevista de reporte en curso; envia 'respuesta' para continuarla" },
        { status: 409 }
      );
    }
    resultado = await iniciarReporte(client, numeros, proyecto.tipo_oferta ?? null, proyecto.unidad_venta ?? null, usoVacio());
  } else {
    if (!proyecto.estado_reporte) {
      return NextResponse.json(
        { error: "no hay una entrevista de reporte en curso; llama sin 'respuesta' para iniciarla" },
        { status: 409 }
      );
    }
    resultado = await avanzarReporte(
      client,
      proyecto.estado_reporte.estado,
      numeros,
      respuesta,
      proyecto.estado_reporte.acumulado
    );
  }

  const camposProyecto: Record<string, unknown> = { numeros_proyecto: resultado.numeros };
  if (resultado.tipoOfertaActualizado) {
    camposProyecto.tipo_oferta = resultado.tipoOfertaActualizado.tipoOferta;
    if (resultado.tipoOfertaActualizado.unidadVenta) {
      camposProyecto.unidad_venta = resultado.tipoOfertaActualizado.unidadVenta;
    }
  }

  if (resultado.tipo === "pregunta") {
    camposProyecto.estado_reporte = { estado: resultado.estado, acumulado: resultado.acumulado };
    await actualizarProyecto(supabase, projectId, camposProyecto);
    return NextResponse.json({
      project_id: projectId,
      tipo: "pregunta",
      pregunta: resultado.pregunta,
      costo_usd: costoAcumuladoUsd(resultado.acumulado),
    });
  }

  camposProyecto.estado_reporte = null;
  await actualizarProyecto(supabase, projectId, camposProyecto);

  const sessionId = await crearSesion(
    supabase,
    user.id,
    projectId,
    "reporte",
    "generacion de reporte de sostenibilidad"
  );
  await guardarPlan(supabase, user.id, sessionId, "reporte_numeros", resultado.contenido, 0, []);
  await cerrarSesion(
    supabase,
    projectId,
    sessionId,
    [],
    costoAcumuladoUsd(resultado.acumulado),
    resultado.acumulado.presupuesto_excedido,
    resultado.acumulado.uso_por_componente,
    PRESUPUESTO_REPORTE_USD,
    resultado.eventos
  );

  return NextResponse.json({
    project_id: projectId,
    session_id: sessionId,
    tipo: "reporte",
    contenido: resultado.contenido,
    costo_usd: costoAcumuladoUsd(resultado.acumulado),
  });
}
