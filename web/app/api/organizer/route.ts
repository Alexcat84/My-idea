/**
 * POST /api/organizer - Fase 3.0: port de modo_gratis/organizador_gratuito
 * en engine/prototipo_motor.py. Capa gratuita: UNA llamada Haiku que
 * organiza sin instruir, sin entrevista. Persiste projects/sessions/plans
 * igual que el CLI (el modo --gratis tambien persiste, no es efimero).
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_SESION } from "@/lib/i18n/mensajes/servidorSesion";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { MAX_LARGO_IDEA, mensajeIdeaLarga } from "@/lib/constants";
import {
  costoAcumuladoUsd,
  llamarClaude,
  MODEL_HAIKU,
  PRESUPUESTO_SESION_USD_DEFAULT,
  usoVacio,
  type UsoAcumulado,
} from "@/lib/costmeter";
import { actualizarProyecto, cerrarSesion, crearSesion, FASES, guardarPlan } from "@/lib/db";
import { nacerIdea } from "@/lib/nacerIdea";
import { idiomaDePlantilla } from "@/lib/i18n/detectarIdioma";
import { cargarEntrySeeds, cargarGrafo } from "@/lib/engine/graph";
import { construirMarkdown, limpiarOrganizador, MAX_TOKENS_ORGANIZADOR, type OrganizadorData } from "@/lib/engine/organizador";
import { parsearJson } from "@/lib/parseJson";
import { SYSTEM_ORGANIZADOR } from "@/lib/prompts";
import { identidadLimite, mensajeFusible, mensajeLimite, mensajeServicioNoDisponible, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_SESION, idioma).organizador;
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: r.cuerpoInvalidoJson }, { status: 400 });
  }
  const texto = (body as { texto?: unknown } | null)?.texto;
  if (typeof texto !== "string" || texto.trim().length === 0) {
    return NextResponse.json({ error: r.faltaTexto }, { status: 400 });
  }
  if (texto.length > MAX_LARGO_IDEA) {
    return NextResponse.json(
      { error: mensajeIdeaLarga(idioma), limite: MAX_LARGO_IDEA },
      { status: 400 }
    );
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }

  // Pre-beta: fusible global ANTES de cobrar creditos y de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    return NextResponse.json({ error: fusible.caido ? mensajeServicioNoDisponible(idioma) : mensajeFusible(idioma) }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    return NextResponse.json(
      { error: limite.caido ? mensajeServicioNoDisponible(idioma) : mensajeLimite(limite.limite, idioma) },
      { status: limite.caido ? 503 : 429 }
    );
  }

  const graph = cargarGrafo();
  // OP-C-01: CON el grafo, o sea por LA PUERTA UNICA. `cargarEntrySeeds` ya
  // filtra por `esOfrecible` cuando lo recibe; sin el devuelve la lista cruda del
  // asset, y una semilla que la pasada fundio abriria el recorrido entero por un
  // nodo que ya no se ofrece.
  const entrySeeds = cargarEntrySeeds(graph);
  const puertas = entrySeeds.map((s) => ({
    id: s,
    fase: graph[s].fase_proyecto,
    titulo: graph[s].titulo_concepto,
    resumen: graph[s].resumen_teorico.slice(0, 150),
  }));

  const { projectId, idioma: idiomaIdea } = await nacerIdea(supabase, user.id, texto, idioma);
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
      { maxTokens: MAX_TOKENS_ORGANIZADOR, componente: "organizador", idiomaSalida: idiomaIdea }
    );
    acumulado = resultado.acumulado;
    data = parsearJson<OrganizadorData>(resultado.texto);
  } catch (e) {
    console.error("[organizer:json] falló", { projectId, error: e });
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
      // AUD-09 B07a: el detalle del error va al log (arriba), nunca al cliente.
      { error: t.noPudeOrganizar, project_id: projectId },
      { status: 502 }
    );
  }

  const limpio = limpiarOrganizador(data);
  // i18n F5 (D2): la Claridad es un documento de la idea: en su idioma.
  const markdown = construirMarkdown(limpio, idiomaDePlantilla(idiomaIdea, idioma));
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
