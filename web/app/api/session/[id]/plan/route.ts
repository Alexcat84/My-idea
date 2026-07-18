/**
 * POST /api/session/[id]/plan - Fase 3.0: port de ensamblar_plan (el
 * redactor) en engine/prototipo_motor.py, con streaming SSE (Server-Sent
 * Events) en vez de una llamada bloqueante -- el boton "Generar mi plan"
 * de la UI es permanente (no depende de que el interprete haya decidido
 * "generar_plan"), asi que esta ruta trabaja con la ruta/perfil_sesion
 * actuales de la sesion sea cual sea su fase.
 *
 * Igual que en el CLI, el material principal es la ruta conversada, mas
 * una cosecha silenciosa del vecindario del grafo (cosecharVecindario).
 * La llamada a Claude se transmite por texto (heartbeat cada 15s para
 * sobrevivir a proxies/Vercel mientras el modelo "piensa" -- mismo patron
 * ya resuelto en el proyecto I Ching para sus WebViews). Si la llamada
 * falla (red o presupuesto), cae al ensamblado offline sin narrar, igual
 * que el CLI.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { NextResponse } from "next/server";
import { createAnthropicClient } from "@/lib/anthropicClient";
import {
  costoAcumuladoUsd,
  MODEL,
  PresupuestoExcedidoError,
  PRESUPUESTO_SESION_USD_DEFAULT,
  registrarUso,
  type UsoAcumulado,
} from "@/lib/costmeter";
import {
  actualizarProyecto,
  cerrarSesion,
  guardarEstadoSesion,
  guardarPlan,
  insertarChecklist,
  mergeNumerosProyecto,
  mergeTipoOferta,
  obtenerProyecto,
  obtenerSesion,
  registrarBitacora,
  registrarNodos,
  type EstadoSesionPersistido,
  type NodoConTipo,
} from "@/lib/db";
import { derivarChecklist } from "@/lib/engine/checklist";
import { cargarGrafo } from "@/lib/engine/graph";
import { evaluarCalidadSesion } from "@/lib/engine/juezSesion";
import {
  comprimirEstadoVivo,
  extraerTitulo,
  filtrarDeltaAntesDeAutodeclaracion,
  finalizarPlan,
  prepararPlan,
  type PreparacionPlan,
} from "@/lib/engine/planRedactor";
import { SYSTEM_PLAN } from "@/lib/prompts";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

const INTERVALO_HEARTBEAT_MS = 15_000;

// Reintento del redactor (hermano del fix del organizador). El plan se genera
// en el momento de MAYOR inversion emocional del usuario -- acaba de terminar su
// entrevista -- y pronto sera un momento PAGADO (5 creditos): un hipo transitorio
// de la API no puede costarle su plan. El SDK reintenta la conexion inicial pero
// NO un fallo a mitad de stream: eso lo cubre esta red.
const BACKOFFS_PLAN_MS = [0, 1000, 3000];

async function generarTextoPlan(
  client: Anthropic,
  preparacion: PreparacionPlan,
  acumulado: UsoAcumulado,
  onDelta: (texto: string) => void,
  /** Un intento previo pinto etapas en el arbol de espera y murio: el cliente
   * debe DESCARTARLAS antes de que el intento nuevo pinte las suyas (el texto
   * nuevo no es el mismo). Anunciar una sola vez, la leccion del organizador. */
  onReinicio: () => void
): Promise<{ rawTexto: string | null; acumulado: UsoAcumulado; avisoFallback: string | null }> {
  if (costoAcumuladoUsd(acumulado) >= PRESUPUESTO_SESION_USD_DEFAULT) {
    return { rawTexto: null, acumulado, avisoFallback: "presupuesto de sesion ya excedido, ensamblo sin narrar" };
  }
  let ultimoError: unknown = null;
  for (let intento = 0; intento < BACKOFFS_PLAN_MS.length; intento += 1) {
    if (BACKOFFS_PLAN_MS[intento] > 0) {
      await new Promise((r) => setTimeout(r, BACKOFFS_PLAN_MS[intento]));
      onReinicio();
    }
    try {
      const stream = client.messages.stream({
        model: MODEL,
        max_tokens: 5000,
        system: [{ type: "text", text: SYSTEM_PLAN, cache_control: { type: "ephemeral" } }],
        messages: [{ role: "user", content: JSON.stringify(preparacion.payload) }],
      });
      // Nunca reenviar el marcador ===JSON=== ni lo que sigue -- es la
      // autodeclaracion de cobertura interna (regla 11 de SYSTEM_PLAN), no
      // contenido para mostrar en vivo. Filtro NUEVO por intento: es con estado.
      const filtro = filtrarDeltaAntesDeAutodeclaracion(onDelta);
      stream.on("text", filtro.onChunk);
      const mensajeFinal = await stream.finalMessage();
      filtro.finalizar();
      const nuevoAcumulado = registrarUso(acumulado, MODEL, mensajeFinal.usage, "plan");
      const rawTexto = mensajeFinal.content
        .filter((b): b is Anthropic.TextBlock => b.type === "text")
        .map((b) => b.text)
        .join("");
      return { rawTexto, acumulado: nuevoAcumulado, avisoFallback: null };
    } catch (e) {
      // El presupuesto no es un hipo: reintentar solo quemaria mas. Es el UNICO
      // caso que sigue ensamblando offline, que para eso existe.
      if (e instanceof PresupuestoExcedidoError) {
        return { rawTexto: null, acumulado, avisoFallback: `fallo el redactor con IA, ensamblo offline: ${e.message}` };
      }
      ultimoError = e;
      console.error(`[plan] intento ${intento + 1}/${BACKOFFS_PLAN_MS.length} fallo:`, e);
    }
  }
  // Agotados los reintentos: LANZA. Antes se degradaba en silencio a un
  // ensamblado offline -- un plan mecanico, sin narracion, entregado como si
  // nada en el momento que mas le importa al usuario (y que pronto le cuesta 5
  // creditos). Es mejor decirlo y ofrecerle reintentar SOLO la redaccion: su
  // sesion y su recorrido ya estan persistidos, la entrevista no se repite.
  console.error("[plan] redactor agotado tras reintentos", { ultimoError });
  throw ultimoError instanceof Error ? ultimoError : new Error(String(ultimoError));
}

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: sessionId } = await params;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }

  const sesion = await obtenerSesion(supabase, sessionId);
  if (!sesion) {
    return NextResponse.json({ error: "sesion no encontrada" }, { status: 404 });
  }
  if (sesion.closed_at) {
    return NextResponse.json({ error: "la sesion ya esta cerrada" }, { status: 409 });
  }
  const estadoPersistido = sesion.estado_recorrido as EstadoSesionPersistido | null;
  if (!estadoPersistido) {
    return NextResponse.json(
      { error: "la sesion no tiene un turno pendiente; llama a /api/session/start primero" },
      { status: 409 }
    );
  }

  const graph = cargarGrafo();
  const families = cargarFamilies();
  const client = createAnthropicClient();
  const { recorrido, acumulado } = estadoPersistido;
  const projectId = sesion.project_id;

  // Phase 3.7.2 (la oferta honesta): "¿Algo mas que quieras que tu plan
  // tome en cuenta?" — el texto opcional viaja al redactor por el mismo
  // canal que todo lo que el usuario conto (el perfil de sesion) y queda
  // en la bitacora como contexto_final_usuario.
  let contextoFinal: string | null = null;
  try {
    const body = (await request.json()) as { contexto_final?: string };
    const texto = (body?.contexto_final ?? "").trim();
    if (texto) contextoFinal = texto.slice(0, 2000);
  } catch {
    // sin body: el camino clasico
  }
  if (contextoFinal) {
    recorrido.perfilSesion = `${recorrido.perfilSesion ?? ""}
Antes de armar el plan, pidio tomar en cuenta: ${contextoFinal}`.trim();
  }

  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async start(controller) {
      function enviar(evento: string, data: unknown) {
        controller.enqueue(encoder.encode(`event: ${evento}\ndata: ${JSON.stringify(data)}\n\n`));
      }
      const heartbeat = setInterval(() => controller.enqueue(encoder.encode(": heartbeat\n\n")), INTERVALO_HEARTBEAT_MS);

      try {
        const preparacion = prepararPlan(
          recorrido.ruta,
          graph,
          families,
          recorrido.textoOriginal,
          recorrido.perfilSesion,
          recorrido.prioridadDeclarada,
          recorrido.esSeguimiento,
          recorrido.estadoVivoPrevio,
          recorrido.dominiosDesbloqueados ?? null
        );

        const { rawTexto, acumulado: acumuladoTrasRedactor, avisoFallback } = await generarTextoPlan(
          client,
          preparacion,
          acumulado,
          (texto) => enviar("delta", { texto }),
          () => enviar("reinicio", { motivo: "reintentando la redaccion" })
        );
        if (avisoFallback) enviar("aviso", { mensaje: avisoFallback });

        // Fase 3.1 (caja de vidrio): eventos propios del ensamblado del
        // plan (autodeclaracion_fallida, coherencia_cobertura_corregida,
        // procedencia_invalida, numero_huerfano) -- antes de esta fase
        // esta ruta nunca pasaba un registrarEvento, asi que ninguno de
        // estos eventos llegaba a persistirse (a diferencia de Python,
        // que ya los acumulaba en fallback_events desde el hotfix v2.2.1).
        const eventosPlan: Record<string, unknown>[] = [];
        if (contextoFinal) {
          eventosPlan.push({ tipo: "contexto_final_usuario", texto: contextoFinal });
        }
        const proyectoParaPlan = await obtenerProyecto(supabase, projectId);
        const numerosParaPlan = {
          ...((proyectoParaPlan?.numeros_proyecto as Record<string, unknown>) ?? {}),
          ...recorrido.numerosDetectadosSesion,
        };
        const resultado = finalizarPlan(
          rawTexto,
          preparacion,
          recorrido.ruta,
          families,
          recorrido.textoOriginal,
          (e) => eventosPlan.push(e),
          numerosParaPlan
        );

        const conceptosTitulos = [...recorrido.ruta, ...resultado.cosechaIds]
          .filter((nid) => nid in graph)
          .map((nid) => graph[nid].titulo_concepto);
        const { estadoVivo, acumulado: acumuladoFinal } = await comprimirEstadoVivo(
          client,
          recorrido.estadoVivoPrevio,
          recorrido.perfilSesion,
          conceptosTitulos,
          acumuladoTrasRedactor
        );

        const nodosConTipo: NodoConTipo[] = [
          ...recorrido.ruta.map((nid, i) => ({ node_id: nid, tipo: recorrido.modos[i] })),
          ...resultado.cosechaIds.map((nid) => ({ node_id: nid, tipo: "cosechado" as const })),
        ];
        await registrarNodos(supabase, projectId, sessionId, nodosConTipo);
        await mergeNumerosProyecto(supabase, projectId, recorrido.numerosDetectadosSesion);
        await mergeTipoOferta(supabase, projectId, recorrido.tipoOfertaSesion, recorrido.unidadVentaSesion);

        const etiquetaDb = recorrido.esSeguimiento
          ? "seguimiento"
          : resultado.evaluacionCobertura.es_completa
            ? "completo"
            : "inicial";
        const totalConceptos = recorrido.ruta.length + resultado.cosechaIds.length;
        const familiasPresentes = [
          ...new Set([...recorrido.ruta, ...resultado.cosechaIds].map((nid) => families[nid] ?? "general")),
        ]
          .filter((f) => f !== "general")
          .sort();
        // Fase 3.5: el plan hereda la procedencia de dominio de su sesión
        // (core para todo lo normal; el pack cuando la sesión es de mundo).
        const dominioSesion = ((sesion as { dominio?: string }).dominio ?? "core") as string;
        const planId = await guardarPlan(
          supabase,
          user.id,
          sessionId,
          etiquetaDb,
          resultado.markdown,
          totalConceptos,
          familiasPresentes,
          dominioSesion
        );
        // Fase 3.3: todo plan de entrevista (inicial|completo|seguimiento)
        // deriva su checklist determinístico; organizador y reporte_numeros
        // nunca pasan por esta ruta.
        await insertarChecklist(supabase, projectId, planId, derivarChecklist(resultado.markdown), dominioSesion);

        const eventosSesion = [...recorrido.fallbackEvents, ...eventosPlan];
        const { calidad, acumulado: acumuladoConJuez } = await evaluarCalidadSesion(
          client,
          eventosSesion,
          graph,
          acumuladoFinal
        );

        const rutaConModos = recorrido.ruta.map((nid, i) => ({ node_id: nid, tipo: recorrido.modos[i] }));
        await cerrarSesion(
          supabase,
          projectId,
          sessionId,
          rutaConModos,
          costoAcumuladoUsd(acumuladoConJuez),
          acumuladoConJuez.presupuesto_excedido,
          acumuladoConJuez.uso_por_componente,
          PRESUPUESTO_SESION_USD_DEFAULT,
          eventosSesion,
          calidad ?? undefined
        );
        await guardarEstadoSesion(supabase, sessionId, {
          recorrido: { ...recorrido, fase: "cerrada", preguntaPendiente: null },
          acumulado: acumuladoConJuez,
        });

        const proyecto = await obtenerProyecto(supabase, projectId);
        const faseFinal = graph[recorrido.ruta[recorrido.ruta.length - 1]]?.fase_proyecto ?? "ideacion";
        const camposProyecto: Record<string, unknown> = { estado_vivo: estadoVivo, fase_actual: faseFinal };
        const titulo = extraerTitulo(resultado.markdown);
        if (titulo && !proyecto?.titulo) camposProyecto.titulo = titulo;
        await actualizarProyecto(supabase, projectId, camposProyecto);

        // ── ANCLA para la ETAPA 2 del frente de cuentas (docs/FLUJO_TRACKING.md §5)
        // Aqui, y NO antes, se cablea el consumo de creditos del plan: el
        // patron es verificar saldo al inicio y DESCONTAR A LA ENTREGA. Este
        // punto es la entrega: el plan ya esta redactado, persistido, con su
        // checklist derivado y la sesion cerrada. Es prerequisito de ese cobro
        // que el redactor reintente y, si se agota, LANCE (ver generarTextoPlan):
        // un plan que muere a mitad jamas debe consumir creditos, y uno
        // ensamblado offline en silencio no es lo que el usuario pago.
        // Fase 4.5 (PREVIEW_MUNDOS_PLAN §5.3): para una sesion de MUNDO, este
        // es ADEMAS el punto de cobro del mundo entero: el preview fue gratis
        // y lo que se compra es EL PLAN (precios.ts: mundo_activar, 3
        // creditos; el nombre del concepto lo reconcilia la ETAPA 2). En beta
        // no se cobra; se sella plan_pagado_at (idempotente, WHERE IS NULL) y
        // queda la telemetria preview_a_compra (§6).
        if (dominioSesion !== "core") {
          await supabase
            .from("project_unlocks")
            .update({ plan_pagado_at: new Date().toISOString() })
            .eq("project_id", projectId)
            .eq("dominio", dominioSesion)
            .is("plan_pagado_at", null);
          await registrarBitacora(supabase, projectId, "preview_a_compra", { mundo: dominioSesion });
        }
        enviar("done", {
          project_id: projectId,
          session_id: sessionId,
          markdown: resultado.markdown,
          evaluacion_cobertura: resultado.evaluacionCobertura,
          costo_usd: costoAcumuladoUsd(acumuladoConJuez),
        });
      } catch (e) {
        enviar("error", { error: e instanceof Error ? e.message : String(e) });
      } finally {
        clearInterval(heartbeat);
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
    },
  });
}
