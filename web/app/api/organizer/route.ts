/**
 * POST /api/organizer - Fase 3.0: port de modo_gratis/organizador_gratuito
 * en engine/prototipo_motor.py. Capa gratuita: UNA llamada Haiku que
 * organiza sin instruir, sin entrevista. Persiste projects/sessions/plans
 * igual que el CLI (el modo --gratis tambien persiste, no es efimero).
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import {
  costoAcumuladoUsd,
  llamarClaude,
  MODEL_HAIKU,
  PRESUPUESTO_SESION_USD_DEFAULT,
  usoVacio,
  type UsoAcumulado,
} from "@/lib/costmeter";
import { actualizarProyecto, cerrarSesion, crearProyecto, crearSesion, FASES, guardarPlan } from "@/lib/db";
import { cargarEntrySeeds, cargarGrafo } from "@/lib/engine/graph";
import { construirMarkdown, type OrganizadorData } from "@/lib/engine/organizador";
import { parsearJson } from "@/lib/parseJson";
import { SYSTEM_ORGANIZADOR } from "@/lib/prompts";
import { MENSAJE_LIMITE, verificarLimiteDiario } from "@/lib/rateLimit";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido, se esperaba JSON" }, { status: 400 });
  }
  const texto = (body as { texto?: unknown } | null)?.texto;
  if (typeof texto !== "string" || texto.trim().length === 0) {
    return NextResponse.json({ error: "falta 'texto'" }, { status: 400 });
  }
  if (texto.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'texto' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
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

  const limite = await verificarLimiteDiario(user.id);
  if (!limite.permitido) {
    return NextResponse.json({ error: MENSAJE_LIMITE }, { status: 429 });
  }

  const graph = cargarGrafo();
  const entrySeeds = cargarEntrySeeds();
  const puertas = entrySeeds.map((s) => ({
    id: s,
    fase: graph[s].fase_proyecto,
    titulo: graph[s].titulo_concepto,
    resumen: graph[s].resumen_teorico.slice(0, 150),
  }));

  const projectId = await crearProyecto(supabase, user.id, texto);
  const sessionId = await crearSesion(supabase, user.id, projectId, "gratuito", texto);

  const client = createAnthropicClient();
  let acumulado: UsoAcumulado = usoVacio();
  let data: OrganizadorData;
  try {
    const resultado = await llamarClaude(
      client,
      SYSTEM_ORGANIZADOR,
      JSON.stringify({ texto_usuario: texto, puertas }),
      MODEL_HAIKU,
      acumulado,
      { maxTokens: 600, componente: "organizador" }
    );
    acumulado = resultado.acumulado;
    data = parsearJson<OrganizadorData>(resultado.texto);
  } catch (e) {
    await cerrarSesion(
      supabase,
      projectId,
      sessionId,
      [],
      costoAcumuladoUsd(acumulado),
      acumulado.presupuesto_excedido,
      acumulado.uso_por_componente,
      PRESUPUESTO_SESION_USD_DEFAULT
    );
    return NextResponse.json(
      { error: `fallo el organizador con IA: ${e instanceof Error ? e.message : String(e)}`, project_id: projectId },
      { status: 502 }
    );
  }

  const markdown = construirMarkdown(data);
  await guardarPlan(supabase, user.id, sessionId, "organizador", markdown, 0, []);
  await cerrarSesion(
    supabase,
    projectId,
    sessionId,
    [],
    costoAcumuladoUsd(acumulado),
    acumulado.presupuesto_excedido,
    acumulado.uso_por_componente,
    PRESUPUESTO_SESION_USD_DEFAULT
  );
  if (typeof data.etapa_detectada === "string" && (FASES as readonly string[]).includes(data.etapa_detectada)) {
    await actualizarProyecto(supabase, projectId, { fase_actual: data.etapa_detectada });
  }

  return NextResponse.json({
    project_id: projectId,
    markdown,
    data,
    costo_usd: costoAcumuladoUsd(acumulado),
  });
}
