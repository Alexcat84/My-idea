/**
 * POST /api/organizer/stream — Fase 3.2: el mismo organizador gratuito
 * del POST JSON, pero por SSE para alimentar el "árbol que piensa" con
 * eventos REALES (regla de oro del brief: la animación es verdad, no
 * teatro). Cada evento `seccion` se emite cuando la clave de esa sección
 * aparece en el stream crudo del modelo — es decir, cuando el modelo
 * literalmente empezó a escribirla; prohibido cualquier progreso
 * simulado. Persiste exactamente igual que la variante JSON (que sigue
 * existiendo para vuelo.ts/probar.ts).
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
  MODEL_HAIKU,
  PRESUPUESTO_SESION_USD_DEFAULT,
  registrarUso,
  usoVacio,
  type UsoAcumulado,
} from "@/lib/costmeter";
import { actualizarProyecto, cerrarSesion, crearSesion, FASES, guardarPlan, obtenerProyecto } from "@/lib/db";
import { nacerIdea } from "@/lib/nacerIdea";
import { cargarEntrySeeds, cargarGrafo } from "@/lib/engine/graph";
import {
  construirMarkdown,
  limpiarOrganizador,
  MAX_TOKENS_ORGANIZADOR,
  seccionesOrganizador,
  type OrganizadorData,
} from "@/lib/engine/organizador";
import { parsearJson } from "@/lib/parseJson";
import { SYSTEM_ORGANIZADOR } from "@/lib/prompts";
import { garantizarTerminal } from "@/lib/streamTerminal";
import { identidadLimite, mensajeFusible, mensajeLimite, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { createClient } from "@/lib/supabase/server";
import type Anthropic from "@anthropic-ai/sdk";

const INTERVALO_HEARTBEAT_MS = 15_000;

// Reintento del organizador (gancho freemium: la ruta que menos puede fallar).
// 3 intentos con backoff corto para hipos transitorios de la API.
const BACKOFFS_MS = [0, 1000, 3000];

/** El modelo cortó por tope de tokens: truncación determinística. Reintentar
 * el mismo texto no ayuda — hay que acortarlo. */
class OrganizadorTruncado extends Error {}

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

  // AUD-09 M28: ordenar una idea que YA existe (su organizador falló antes y
  // quedó sin Claridad). Se reusa la misma idea en vez de crear otra; solo si es
  // del usuario (RLS) y si de verdad no tiene su Claridad.
  const idPedido = (body as { project_id?: unknown } | null)?.project_id;
  let ideaExistente: string | null = null;
  if (typeof idPedido === "string" && idPedido) {
    if (!(await obtenerProyecto(supabase, idPedido))) {
      return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
    }
    const { data: sesionesIdea } = await supabase.from("sessions").select("id").eq("project_id", idPedido);
    const ids = ((sesionesIdea ?? []) as Array<{ id: string }>).map((s) => s.id);
    const { data: organizadores } = ids.length
      ? await supabase.from("plans").select("id").in("session_id", ids).eq("etiqueta", "organizador")
      : { data: [] };
    if ((organizadores ?? []).length > 0) {
      return NextResponse.json({ error: t.yaOrdenada }, { status: 409 });
    }
    ideaExistente = idPedido;
  }

  // Pre-beta: fusible global ANTES de cobrar creditos y de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    return NextResponse.json({ error: mensajeFusible(idioma) }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    return NextResponse.json({ error: mensajeLimite(limite.limite, idioma) }, { status: 429 });
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

  const projectId = ideaExistente ?? (await nacerIdea(supabase, user.id, texto, idioma)).projectId;
  const sessionId = await crearSesion(supabase, user.id, projectId, "gratuito", texto);

  const client = createAnthropicClient();
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      // AUD-09 H08: ningún stream termina en silencio (la misma garantía que la
      // ruta del plan). Se apunta lo emitido para que el finally sepa si ya
      // salió un evento final.
      const emitidos: string[] = [];
      let terminalEmitido: string | null = null;
      function enviar(evento: string, data: unknown) {
        controller.enqueue(encoder.encode(`event: ${evento}\ndata: ${JSON.stringify(data)}\n\n`));
        emitidos.push(evento);
        if (evento === "done" || evento === "error") terminalEmitido = evento;
      }
      const heartbeat = setInterval(() => controller.enqueue(encoder.encode(": heartbeat\n\n")), INTERVALO_HEARTBEAT_MS);

      let acumulado: UsoAcumulado = usoVacio();
      // Las secciones se anuncian una sola vez aunque haya reintentos: el
      // árbol conserva lo que ya encendió.
      const anunciadas = new Set<string>();
      // Los nombres de las secciones se pintan en el árbol: idioma de la interfaz.
      const secciones = seccionesOrganizador(idioma);

      const cerrar = () =>
        cerrarSesion(
          supabase,
          projectId,
          sessionId,
          [],
          costoAcumuladoUsd(acumulado),
          acumulado.presupuesto_excedido,
          acumulado.uso_por_componente,
          PRESUPUESTO_SESION_USD_DEFAULT
        );

      // Un intento: consume el stream (encendiendo las secciones REALES del
      // árbol), cobra el uso y devuelve los datos. Lanza OrganizadorTruncado
      // si el modelo cortó por tope (reintentar el mismo texto no ayudaría).
      async function intentarOrganizar(): Promise<OrganizadorData> {
        const claudeStream = client.messages.stream({
          model: MODEL_HAIKU,
          max_tokens: MAX_TOKENS_ORGANIZADOR,
          system: [{ type: "text", text: SYSTEM_ORGANIZADOR, cache_control: { type: "ephemeral" } }],
          messages: [{ role: "user", content: JSON.stringify({ texto_usuario: texto, puertas }) }],
        });
        let crudo = "";
        claudeStream.on("text", (delta) => {
          crudo += delta;
          for (const { clave, label } of secciones) {
            if (!anunciadas.has(clave) && crudo.includes(`"${clave}"`)) {
              anunciadas.add(clave);
              enviar("seccion", { clave, label });
            }
          }
        });
        const mensajeFinal = await claudeStream.finalMessage();
        acumulado = registrarUso(acumulado, MODEL_HAIKU, mensajeFinal.usage, "organizador");
        if (mensajeFinal.stop_reason === "max_tokens") throw new OrganizadorTruncado();
        const textoModelo = mensajeFinal.content
          .filter((b): b is Anthropic.TextBlock => b.type === "text")
          .map((b) => b.text)
          .join("");
        return parsearJson<OrganizadorData>(textoModelo);
      }

      try {
        enviar("inicio", { project_id: projectId });

        // Reintento con backoff corto: el organizador es la primera impresión
        // de un usuario nuevo y su única pieza gratis. Un hipo transitorio de
        // la API no puede costarle un usuario a la beta; la truncación (tope)
        // sí es determinística y no se reintenta.
        let data: OrganizadorData | null = null;
        let truncado = false;
        let ultimoError: unknown = null;
        for (let intento = 0; intento < BACKOFFS_MS.length; intento++) {
          if (BACKOFFS_MS[intento] > 0) await new Promise((r) => setTimeout(r, BACKOFFS_MS[intento]));
          try {
            data = await intentarOrganizar();
            break;
          } catch (e) {
            ultimoError = e;
            if (e instanceof OrganizadorTruncado) {
              truncado = true;
              break;
            }
            console.error(`[organizer] intento ${intento + 1}/${BACKOFFS_MS.length} falló:`, e);
          }
        }

        if (!data) {
          // Agotados los reintentos (o truncación): registro el error REAL
          // para que Vercel lo vea (fin del punto ciego) y devuelvo palabras
          // de persona — precisas si fue el tope. El texto ya está guardado;
          // la UI ofrece "Intentar de nuevo" sin re-teclear.
          console.error("[organizer] fallo definitivo", { projectId, truncado, error: ultimoError });
          await cerrar().catch(() => {});
          enviar("error", {
            error: truncado ? t.truncado : t.noPudimosOrganizar,
            project_id: projectId,
            reintentable: true,
          });
          return;
        }

        // La puerta SSE no pasa por el punto único de limpieza de
        // llamarClaude: se limpia aquí, antes del markdown y del cliente.
        data = limpiarOrganizador(data);
        const markdown = construirMarkdown(data);
        await guardarPlan(supabase, user.id, sessionId, "organizador", markdown, 0, []);
        await cerrar();
        if (typeof data.etapa_detectada === "string" && (FASES as readonly string[]).includes(data.etapa_detectada)) {
          await actualizarProyecto(supabase, projectId, { fase_actual: data.etapa_detectada });
        }
        enviar("done", { project_id: projectId, markdown, data, costo_usd: costoAcumuladoUsd(acumulado) });
      } catch (e) {
        // Fallo fuera del bucle (p.ej. persistencia): registrar y misma red.
        console.error("[organizer] error inesperado", { projectId, error: e });
        await cerrar().catch(() => {});
        enviar("error", {
          error: t.noPudimosOrganizar,
          project_id: projectId,
          reintentable: true,
        });
      } finally {
        clearInterval(heartbeat);
        garantizarTerminal({ terminalEmitido, emitidos, sessionId, projectId, enviar });
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
