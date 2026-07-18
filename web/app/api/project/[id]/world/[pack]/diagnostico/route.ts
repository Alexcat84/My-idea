/**
 * POST /api/project/[id]/world/[pack]/diagnostico — Fase 4.5
 * (PREVIEW_MUNDOS_PLAN §4): la entrevista del preview terminó; se redacta y
 * persiste el DIAGNÓSTICO (el escaparate del mundo).
 *
 * - UNA llamada Sonnet (LEY DE CALIDAD §2.3: jamás un modelo menor; si falla,
 *   502 honesto y el usuario reintenta, sin plantilla degradada).
 * - El resumen se persiste en la fila del unlock (resumen_md/resumen_at) y se
 *   relee siempre: el estado [diagnóstico listo].
 * - La sesión del preview NO se cierra (closed_at queda null): la compra
 *   genera el plan DESDE ella sin re-entrevistar. Sí se marca su recorrido
 *   fase 'cerrada' para que la UI no re-abra la entrevista al recargar.
 * - Telemetría §6: preview_completado.
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import catalogo from "@/lib/assets/packs_catalog.json";
import { costoAcumuladoUsd } from "@/lib/costmeter";
import { guardarEstadoSesion, obtenerProyecto, obtenerSesion, registrarBitacora } from "@/lib/db";
import { PACK_CLICKS_PACK } from "@/lib/dbContract";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { materialDiagnostico, redactarDiagnostico } from "@/lib/engine/diagnosticoMundo";
import { cargarGrafo } from "@/lib/engine/graph";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string; promesa: string }>).find(
    (p) => p.clave === pack
  );
  if (!entrada || !(PACK_CLICKS_PACK as readonly string[]).includes(pack)) {
    return NextResponse.json({ error: "ese mundo no existe" }, { status: 404 });
  }

  let body: { session_id?: unknown } = {};
  try {
    const texto = await request.text();
    if (texto.trim().length > 0) body = JSON.parse(texto);
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
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
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  // La sesión del preview: la del body, o la amarrada a la fila del unlock.
  let sessionId = typeof body.session_id === "string" ? body.session_id : null;
  if (!sessionId) {
    const { data: unlockRows } = await supabase
      .from("project_unlocks")
      .select("preview_session_id")
      .eq("project_id", projectId)
      .eq("dominio", pack)
      .limit(1);
    sessionId = (unlockRows?.[0] as { preview_session_id?: string | null } | undefined)?.preview_session_id ?? null;
  }
  if (!sessionId) {
    return NextResponse.json({ error: "no hay un preview de este mundo en curso" }, { status: 409 });
  }

  const sesion = await obtenerSesion(supabase, sessionId);
  if (!sesion || sesion.project_id !== projectId || ((sesion as { dominio?: string }).dominio ?? "core") !== pack) {
    return NextResponse.json({ error: "esa sesion no es el preview de este mundo" }, { status: 409 });
  }
  const estadoPersistido = sesion.estado_recorrido;
  if (!estadoPersistido) {
    return NextResponse.json({ error: "el preview no tiene recorrido que diagnosticar" }, { status: 409 });
  }

  const graph = cargarGrafo();
  const material = materialDiagnostico(
    estadoPersistido.recorrido,
    graph,
    { nombre: entrada.nombre, promesa: entrada.promesa },
    (proyecto.estado_vivo as string | null) ?? null
  );

  let resumen: string;
  let acumulado = estadoPersistido.acumulado;
  try {
    const r = await redactarDiagnostico(createAnthropicClient(), material, acumulado);
    resumen = r.resumen;
    acumulado = r.acumulado;
  } catch (e) {
    // Fallar ruidoso (BANCO §9): sin plantilla degradada. El preview es el
    // vendedor del mundo; un escaparate mediocre vende peor que un reintento.
    console.error("[diagnostico] fallo el redactor:", e);
    return NextResponse.json(
      { error: "no pudimos redactar tu diagnóstico; intenta de nuevo en un momento" },
      { status: 502 }
    );
  }

  const ahoraIso = new Date().toISOString();
  const { error: errPersistir } = await supabase
    .from("project_unlocks")
    .update({ resumen_md: resumen, resumen_at: ahoraIso, preview_session_id: sessionId })
    .eq("project_id", projectId)
    .eq("dominio", pack);
  if (errPersistir) {
    console.error("[diagnostico] no se pudo persistir el resumen:", errPersistir);
    return NextResponse.json({ error: "no pudimos guardar tu diagnóstico; intenta de nuevo" }, { status: 500 });
  }

  // La sesión queda en fase 'cerrada' SIN closed_at: la UI no re-abre la
  // entrevista, y la ruta del plan (que exige closed_at null) puede generar
  // el plan comprado desde ella. El costo del diagnóstico queda acumulado.
  await guardarEstadoSesion(supabase, sessionId, {
    recorrido: { ...estadoPersistido.recorrido, fase: "cerrada", preguntaPendiente: null },
    acumulado,
  });

  await registrarBitacora(supabase, projectId, "preview_completado", { mundo: pack, session_id: sessionId });

  return NextResponse.json({
    project_id: projectId,
    dominio: pack,
    session_id: sessionId,
    resumen,
    resumen_at: ahoraIso,
    costo_usd: costoAcumuladoUsd(acumulado),
  });
}
