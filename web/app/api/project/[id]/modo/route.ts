/**
 * PATCH /api/project/[id]/modo — el modo del camino POR ESPACIO ("todo separado",
 * migration 032). body {modo_camino?: 'ritmo'|'fechas', capacidad_semanal?,
 * dominio?}. Valida contra MODO_CAMINO / CAPACIDAD_SEMANAL (dbContract), persiste
 * en project_modos (project_id, dominio) y deja rastro en la bitácora del proyecto
 * (tipo 'modo_camino', payload {de, a, dominio}). `dominio` por defecto 'core'
 * (compat con el interruptor del core, que llama sin dominio). El core DUAL-LEE su
 * modo actual (project_modos ó projects.modo_camino) para el `de` de la bitácora.
 *
 * Cada espacio elige su modo por su cuenta. Pausar (→'ritmo') JAMÁS borra las
 * fechas ya puestas en los ítems de ese espacio: solo silencia.
 *
 * Scheduler F2: la CAPACIDAD (cuántas horas por semana le da el usuario a ESTE
 * espacio) vive en la misma fila porque es la misma decisión: cómo lleva el
 * tiempo de este espacio. Puede venir sola (el usuario la corrige después, sin
 * tocar el modo) o junto al modo. Cambiarla deja rastro propio
 * ('capacidad_semanal', payload {de, a, dominio}): es lo que explica por qué el
 * calendario se recalculó distinto.
 */
import { NextResponse } from "next/server";
import { CAPACIDAD_SEMANAL, MODO_CAMINO, type CapacidadSemanal, type ModoCamino } from "@/lib/dbContract";
import { ESPACIO_CORE, esEspacioCore } from "@/lib/espacios";
import {
  guardarCapacidadEspacio,
  guardarModoEspacio,
  obtenerCapacidadesPorEspacio,
  obtenerModosPorEspacio,
  obtenerProyecto,
  registrarBitacora,
} from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { modo_camino?: unknown; dominio?: unknown; capacidad_semanal?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  if (body.modo_camino !== undefined) {
    if (typeof body.modo_camino !== "string" || !(MODO_CAMINO as readonly string[]).includes(body.modo_camino)) {
      return NextResponse.json(
        { error: `modo_camino inválido; usa uno de: ${MODO_CAMINO.join(", ")}` },
        { status: 400 }
      );
    }
  }
  if (body.capacidad_semanal !== undefined) {
    if (
      typeof body.capacidad_semanal !== "string" ||
      !(CAPACIDAD_SEMANAL as readonly string[]).includes(body.capacidad_semanal)
    ) {
      return NextResponse.json(
        { error: `capacidad_semanal inválida; usa una de: ${CAPACIDAD_SEMANAL.join(", ")}` },
        { status: 400 }
      );
    }
  }
  if (body.modo_camino === undefined && body.capacidad_semanal === undefined) {
    return NextResponse.json({ error: "nada que actualizar: manda modo_camino y/o capacidad_semanal" }, { status: 400 });
  }
  const nuevo = body.modo_camino as ModoCamino | undefined;
  const nuevaCapacidad = body.capacidad_semanal as CapacidadSemanal | undefined;
  const dominio = typeof body.dominio === "string" && body.dominio ? body.dominio : ESPACIO_CORE;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  // Modo actual del espacio (dual-read del core en la transición).
  const modos = await obtenerModosPorEspacio(supabase, projectId);
  const anterior = modos[dominio] ?? (esEspacioCore(dominio) ? proyecto.modo_camino ?? null : null);

  if (nuevo !== undefined && anterior !== nuevo) {
    await guardarModoEspacio(supabase, projectId, dominio, nuevo);
    await registrarBitacora(supabase, projectId, "modo_camino", { de: anterior, a: nuevo, dominio });
  }

  // Scheduler F2: la capacidad del espacio. Se guarda con el modo VIGENTE (el
  // recién puesto si vino en el mismo cuerpo), porque modo_camino es NOT NULL.
  let capacidadAnterior: CapacidadSemanal | null = null;
  if (nuevaCapacidad !== undefined) {
    const caps = await obtenerCapacidadesPorEspacio(supabase, projectId);
    capacidadAnterior = caps[dominio] ?? null;
    if (capacidadAnterior !== nuevaCapacidad) {
      await guardarCapacidadEspacio(supabase, projectId, dominio, nuevaCapacidad, nuevo ?? anterior ?? "fechas");
      await registrarBitacora(supabase, projectId, "capacidad_semanal", {
        de: capacidadAnterior,
        a: nuevaCapacidad,
        dominio,
      });
    }
  }

  return NextResponse.json({
    modo_camino: nuevo ?? anterior,
    capacidad_semanal: nuevaCapacidad ?? capacidadAnterior,
    dominio,
  });
}
