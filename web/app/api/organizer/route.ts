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
import { parsearJson } from "@/lib/parseJson";
import { SYSTEM_ORGANIZADOR } from "@/lib/prompts";
import { createClient } from "@/lib/supabase/server";

interface OrganizadorData {
  idea_en_una_frase?: string;
  etapa_detectada?: string;
  lo_que_ya_tienes_claro?: string[];
  lo_que_estas_asumiendo_sin_saberlo?: string[];
  areas_que_cubriria_tu_plan_completo?: string[];
}

function construirMarkdown(data: OrganizadorData): string {
  const out: string[] = [
    "# Organizador de tu idea",
    "",
    `**En una frase:** ${data.idea_en_una_frase ?? ""}`,
    "",
    `**Etapa detectada:** ${data.etapa_detectada ?? ""}`,
    "",
    "## Lo que ya tienes claro",
  ];
  for (const b of data.lo_que_ya_tienes_claro ?? []) out.push(`- ${b}`);
  out.push("", "## Lo que estás asumiendo sin saberlo");
  for (const b of data.lo_que_estas_asumiendo_sin_saberlo ?? []) out.push(`- ${b}`);
  out.push("", "## Áreas que cubriría tu plan completo");
  for (const b of data.areas_que_cubriria_tu_plan_completo ?? []) out.push(`- ${b}`);
  return out.join("\n");
}

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
