/**
 * /api/project/[id]/replantear — Ciclo de replanteamiento, Fase 2 (decisiones
 * del fundador, 27 sep 2026; docs/producto/CICLO_REPLANTEAMIENTO.md).
 *
 * "Replantear mi camino" es la segunda entrada de Manos a la Obra, hermana de
 * "Profundizar mi plan" (/follow). Cuatro pasos y SIN entrevista:
 *   1. tu historia (obligatoria)        } en la pantalla
 *   2. lo que ya construiste            }
 *   3. caminos posibles                 ← ESTA ruta (POST)
 *   4. confirmar y generar              → /api/session/[id]/plan con { camino }
 *
 * El POST es donde nace el ciclo: las mismas puertas que el follow
 * (lib/cicloApertura.ts: cuenta, doble factor, idea realizada, muros del mundo,
 * saldo, RESERVA de precios.ts con la clave plan:{sesión}, fusible y límite
 * diario), y UNA llamada a Sonnet (SYSTEM_CAMINOS) que propone dos o tres
 * caminos, cada uno anclado a conceptos del grafo que el proyecto aún no cubrió
 * (validados por código: jamás un id inventado). Los caminos van dentro del
 * mismo cobro, que ocurre a la ENTREGA del plan.
 *
 * La sesión (tipo 'seguimiento', etiqueta de su plan 'replanteamiento') guarda
 * en estado_recorrido.recorrido.ciclo la historia, lo que se conserva, lo que se
 * suelta y los caminos. Al generar, el camino elegido da la ruta del plan.
 */
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { LecturaFallidaError, mensajeLecturaFallida } from "@/lib/analyticsEntrada";
import { abrirCiclo, consultarSaldoCiclo, realidadDelCiclo } from "@/lib/cicloApertura";
import { MAX_LARGO_TEXTO_USUARIO, mensajeTextoLargo } from "@/lib/constants";
import { llamarClaude, MODEL_SONNET, usoVacio } from "@/lib/costmeter";
import {
  crearSesion,
  dominiosDesbloqueados,
  guardarEstadoSesion,
  nodosCubiertos,
  obtenerSesion,
  obtenerPlanVigenteDe,
  obtenerTareasDePlan,
  type EstadoSesionPersistido,
  type TareaDePlan,
} from "@/lib/db";
import { resolverReserva } from "@/lib/creditos";
import { cargarGrafo } from "@/lib/engine/graph";
import { candidatosSeguimiento } from "@/lib/engine/puertaAvanzada";
import { estadoInicial } from "@/lib/engine/recorrido";
import {
  componerMensajeReplanteamiento,
  planAnteriorParaIA,
  tituloDeNodoPara,
  TOPE_GENERACIONES_CAMINOS,
  validarCaminos,
  type TareaCiclo,
} from "@/lib/engine/replanteamiento";
import { elegir } from "@/lib/i18n/config";
import { idiomaDelProyecto } from "@/lib/i18n/detectarIdioma";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { interpolar } from "@/lib/i18n/interpolar";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { parsearJson } from "@/lib/parseJson";
import { SYSTEM_CAMINOS } from "@/lib/prompts";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";
import { aperturaDeSesion, contextoDeSesion } from "@/lib/engine/memoria";

export const runtime = "nodejs";

/** AUD-09 M22: ¿alcanza el saldo para abrir el ritual? Solo mira. */
export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const dominio = new URL(request.url).searchParams.get("dominio") || "core";
  const supabase = await createClient();
  return consultarSaldoCiclo({ supabase, projectId, dominio, tipo: "replantear", idioma: idiomaDeRequest(request) });
}

/** La sesión previa de ESTE ritual, si es un replanteamiento abierto de esta
 * idea (la lectura va con la sesión y los permisos de quien pide), con su
 * vuelta de caminos. null si no califica. */
async function leerSesionPrevia(supabase: Awaited<ReturnType<typeof createClient>>, projectId: string, id: string) {
  const previa = await obtenerSesion(supabase, id);
  const ciclo = (previa?.estado_recorrido as EstadoSesionPersistido | null | undefined)?.recorrido?.ciclo;
  if (!previa || previa.project_id !== projectId || previa.closed_at || ciclo?.tipo !== "replantear") return null;
  return { id, generacion: ciclo.generacion ?? 1 };
}

async function soltarSesionPrevia(supabase: Awaited<ReturnType<typeof createClient>>, id: string) {
  const { data: planes } = await supabase.from("plans").select("id").eq("session_id", id).limit(1);
  if ((planes ?? []).length > 0) return;
  await resolverReserva(`plan:${id}`, "liberada");
  const { error } = await supabase.from("sessions").update({ closed_at: new Date().toISOString() }).eq("id", id);
  if (error) console.error("[replantear] no se pudo cerrar la sesión previa:", error);
}

const aTarea = (f: TareaDePlan): TareaCiclo => ({
  id: f.id,
  texto: f.texto,
  nota: f.nota ?? null,
  completed_at: f.completed_at ?? null,
  etapa: f.etapa,
});

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const t = elegir(SERVIDOR_PROYECTO, idioma).follow;

  let body: { historia?: unknown; suelta?: unknown; dominio?: unknown; session_previa?: unknown };
  try {
    body = await request.json();
  } catch {
    body = {};
  }
  const historia = typeof body.historia === "string" ? body.historia.trim() : "";
  const idsSuelta = new Set(Array.isArray(body.suelta) ? body.suelta.filter((x): x is string => typeof x === "string") : []);
  const dominio = typeof body.dominio === "string" && body.dominio ? body.dominio : "core";
  // La historia es OBLIGATORIA (decisión del fundador): sin ella no hay
  // replanteamiento. Se rechaza antes de apartar nada.
  if (!historia) return NextResponse.json({ error: t.historiaObligatoria }, { status: 400 });
  if (historia.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json({ error: mensajeTextoLargo(idioma), limite: MAX_LARGO_TEXTO_USUARIO }, { status: 400 });
  }

  const supabase = await createClient();
  // Volver atrás y pedir caminos otra vez no puede dejar el precio apartado dos
  // veces (con el saldo justo, el segundo intento chocaría con el primero): la
  // sesión anterior de ESTE ritual, si aún no dio su plan, suelta su reserva y
  // se cierra. Solo la de un replanteamiento abierto, de esta idea y de quien
  // pide (la lectura va con su sesión y sus permisos).
  const previa =
    typeof body.session_previa === "string" && body.session_previa
      ? await leerSesionPrevia(supabase, projectId, body.session_previa)
      : null;
  // Decisión del fundador (28 sep 2026): 3 vueltas de caminos por
  // replanteamiento. La 4.ª se dice claro y NO toca nada: la previa conserva sus
  // caminos y su precio apartado, para elegir uno de ellos.
  const generacion = previa ? previa.generacion + 1 : 1;
  if (generacion > TOPE_GENERACIONES_CAMINOS) {
    return NextResponse.json(
      { error: interpolar(t.topeCaminos, { n: TOPE_GENERACIONES_CAMINOS }), tope: true },
      { status: 429 }
    );
  }
  if (previa) await soltarSesionPrevia(supabase, previa.id);
  const apertura = await abrirCiclo({ request, supabase, projectId, dominio, tipo: "replantear", idioma });
  if (!apertura.ok) return apertura.respuesta;
  const { user, proyecto, nombreMundo, sessionIdNueva, soltarReserva } = apertura.ciclo;

  try {
    // El plan VIGENTE del espacio y sus tareas: las hechas son "lo que ya
    // construiste" (paso 2); todas van a la IA como el plan anterior.
    const plan = await obtenerPlanVigenteDe(supabase, projectId, dominio);
    const tareas = plan ? await obtenerTareasDePlan(supabase, projectId, plan.id) : [];
    // Un mundo sin plan propio no tiene nada que replantear: primero se explora.
    if (dominio !== "core" && !plan) {
      await soltarReserva();
      return NextResponse.json({ error: interpolar(t.primeroExplora, { mundo: nombreDeMundo(dominio, idioma) }) }, { status: 409 });
    }
    const hechas = tareas.filter((f) => f.estado === "hecho");
    const conserva = hechas.filter((f) => !idsSuelta.has(f.id)).map(aTarea);
    const suelta = hechas.filter((f) => idsSuelta.has(f.id)).map(aTarea);
    const pendientes = tareas
      .filter((f) => f.estado === "pendiente" || f.estado === "empezado" || f.estado === "en_proceso")
      .map((f) => ({ etapa: f.etapa, texto: f.texto, destacado: f.destacado, estado: f.estado }));
    const planAnterior = plan ? planAnteriorParaIA(plan.contenido_md, tareas, tituloDeNodoPara(cargarGrafo())) : null;

    let bloqueRealidad: string | null;
    try {
      bloqueRealidad = await realidadDelCiclo(supabase, projectId, proyecto, dominio, nombreMundo);
    } catch (e) {
      await soltarReserva();
      if (e instanceof LecturaFallidaError) return NextResponse.json({ error: mensajeLecturaFallida(idioma) }, { status: 503 });
      throw e;
    }
    const mensaje = componerMensajeReplanteamiento({ historia, conserva, suelta, pendientes, bloqueRealidad });

    // Los conceptos que el proyecto AÚN NO cubrió, puntuados por la historia y el
    // estado vivo (la misma vara que la puerta del follow). En un mundo, solo los
    // suyos.
    const graph = cargarGrafo();
    const families = cargarFamilies();
    const cubiertos = await nodosCubiertos(supabase, projectId);
    const estadoVivo = (proyecto.estado_vivo as string | null) ?? null;
    let dominios = ["core"];
    try {
      dominios = await dominiosDesbloqueados(supabase, projectId);
    } catch {
      dominios = ["core"];
    }
    const candidatosIds = candidatosSeguimiento(
      mensaje,
      estadoVivo,
      (proyecto.fase_actual as string | null) ?? "ideacion",
      families,
      graph,
      cubiertos,
      undefined,
      dominio === "core" ? dominios : [dominio]
    );

    const sessionId = await crearSesion(supabase, user.id, projectId, "seguimiento", mensaje, null, dominio, { id: sessionIdNueva });
    const idiomaSalida = idiomaDelProyecto(proyecto);
    const ctx = {
      historia,
      se_conserva: conserva.map((c) => c.texto),
      se_suelta: suelta.map((c) => c.texto),
      plan_anterior: planAnterior,
      realidad: bloqueRealidad,
      estado_vivo: estadoVivo,
      candidatos: candidatosIds.map((id) => ({
        id,
        titulo: graph[id].titulo_concepto,
        fase: graph[id].fase_proyecto,
        resumen: (graph[id].resumen_teorico ?? "").slice(0, 150),
      })),
    };
    let acumulado = usoVacio();
    let caminos: ReturnType<typeof validarCaminos> = [];
    if (candidatosIds.length > 0) {
      try {
        const r = await llamarClaude(createAnthropicClient(), SYSTEM_CAMINOS, JSON.stringify(ctx), MODEL_SONNET, acumulado, {
          maxTokens: 1200,
          componente: "caminos",
          idiomaSalida,
          contexto: contextoDeSesion(aperturaDeSesion(proyecto)),
        });
        acumulado = r.acumulado;
        caminos = validarCaminos(parsearJson(r.texto), candidatosIds);
      } catch (e) {
        console.error("[replantear] la IA no propuso caminos:", e);
      }
    }
    // Menos de dos caminos no es una elección: se dice, y no se cobra nada.
    if (caminos.length < 2) {
      await soltarReserva();
      return NextResponse.json({ error: t.caminosFallidos }, { status: 503 });
    }

    const recorrido = estadoInicial({
      actualId: caminos[0].nodos[0],
      perfilSesion: estadoVivo ?? "",
      textoOriginal: mensaje,
      esSeguimiento: true,
      estadoVivoPrevio: estadoVivo,
      nodosCubiertosPrevios: [...cubiertos],
      dominiosDesbloqueados: dominios,
      dominioSesion: dominio,
      idioma: idiomaSalida,
      ciclo: { tipo: "replantear", historia, conserva, suelta, caminos, caminoElegido: null, generacion },
      // Principio 1 (28 sep 2026): la memoria del proyecto viaja al plan del camino elegido.
      ...aperturaDeSesion(proyecto),
    });
    // Sin entrevista: la sesión queda lista para generar el plan del camino que
    // elija la persona en el paso 4.
    await guardarEstadoSesion(supabase, sessionId, {
      recorrido: { ...recorrido, fase: "listo_para_plan", preguntaPendiente: null },
      acumulado,
    });

    return NextResponse.json({
      session_id: sessionId,
      caminos: caminos.map(({ id, titulo, descripcion }) => ({ id, titulo, descripcion })),
    });
  } catch (e) {
    // Nada se entregó: lo apartado se suelta y el fallo queda en el log.
    await soltarReserva();
    console.error("[replantear] fallo:", e);
    return NextResponse.json({ error: t.caminosFallidos }, { status: 503 });
  }
}
