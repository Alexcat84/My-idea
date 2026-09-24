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
 * ya resuelto en el proyecto I Ching para sus WebViews). Un fallo de red se
 * reintenta y, agotado, LANZA (error honesto, la sesion queda abierta para
 * reintentar). Solo el presupuesto de sesion agotado cae al ensamblado offline.
 *
 * AUD-09 H02, politica del fundador (25 sep 2026): se verifica saldo al
 * empezar y se cobra al final SOLO si se entrego lo prometido. Un plan armado
 * sin IA (el ensamblado offline) NO se cobra: se entrega gratis, marcado como
 * version basica y con un aviso honesto que la pantalla muestra.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { NextResponse } from "next/server";
import { garantizarTerminal } from "@/lib/streamTerminal";
import { createAnthropicClient } from "@/lib/anthropicClient";
import {
  costoAcumuladoUsd,
  MODEL,
  PresupuestoExcedidoError,
  PRESUPUESTO_SESION_USD_DEFAULT,
  registrarUso,
  type UsoAcumulado,
} from "@/lib/costmeter";
import { cobrar, conceptoDelPlan, mensajeSaldoInsuficiente, montoDelPlan, reembolsar, verificarSaldo } from "@/lib/creditos";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { AVISO_2FA, faltaSegundoFactor } from "@/lib/seguridad";
import {
  actualizarProyecto,
  cerrarSesion,
  guardarEstadoSesion,
  guardarPlan,
  insertarChecklist,
  mergeNumerosProyecto,
  obtenerItemsDePlan,
  obtenerPlanCoreVigente,
  mergeTipoOferta,
  obtenerProyecto,
  obtenerSesion,
  registrarBitacora,
  registrarNodos,
  type EstadoSesionPersistido,
  type NodoConTipo,
} from "@/lib/db";
import { derivarChecklist } from "@/lib/engine/checklist";
import { enlazarPlanProteccion } from "@/lib/engine/enlazador";
import { estimarLoteMayoria } from "@/lib/engine/estimacion";
import { armarSnapshot, type FilaChecklistSnapshot } from "@/lib/engine/snapshotProyecto";
import { esMundoProteccion } from "@/lib/espacios";
import { cargarGrafo, conceptosDeRuta, faseDeNodo } from "@/lib/engine/graph";
import { dominiosDelRecorrido } from "@/lib/engine/recorrido";
import { evaluarCalidadSesion } from "@/lib/engine/juezSesion";
import {
  AVISO_VERSION_BASICA,
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
  // ETAPA 2 (la frontera): generar un plan es motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(AVISO_LOGIN, { status: 401 });
  }
  if (await faltaSegundoFactor()) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }

  const sesion = await obtenerSesion(supabase, sessionId);
  if (!sesion) {
    return NextResponse.json({ error: "sesion no encontrada" }, { status: 404 });
  }
  if (sesion.closed_at) {
    return NextResponse.json({ error: "Esta conversación ya terminó. Recarga la página para ver lo último." }, { status: 409 });
  }
  const estadoPersistido = sesion.estado_recorrido as EstadoSesionPersistido | null;
  if (!estadoPersistido) {
    return NextResponse.json(
      { error: "Esta conversación no tiene nada pendiente. Recarga la página para seguir donde quedaste." },
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

  // ETAPA 2 — VERIFICAR antes de abrir el stream (la unidad facturable de
  // esta entrega): core inicial 5, core seguimiento 2, mundo inicial 3 (el
  // preview fue gratis: lo que se compra es EL PLAN), mundo seguimiento 2.
  // 402 limpio antes de gastar un token. El descuento va a la ENTREGA.
  const dominioCobro = ((sesion as { dominio?: string }).dominio ?? "core") as string;
  const conceptoCobro = conceptoDelPlan(dominioCobro, recorrido.esSeguimiento);
  const montoCobro = montoDelPlan(dominioCobro, recorrido.esSeguimiento);
  if (montoCobro > 0) {
    const saldoPlan = await verificarSaldo(user.id, montoCobro);
    if (!saldoPlan.alcanza) {
      return NextResponse.json(
        { error: mensajeSaldoInsuficiente(saldoPlan.creditos, montoCobro), saldo: saldoPlan.creditos },
        { status: 402 }
      );
    }
  }

  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async start(controller) {
      // La garantia del terminal (4 sep 2026): se apunta lo emitido SOLO
      // DESPUES de que el enqueue salga bien. Si el enqueue tira, no se
      // apunta nada, que es justo lo que deja ver el cierre mudo.
      const emitidos: string[] = [];
      let terminalEmitido: string | null = null;
      let causaCierre: unknown = null;
      function enviar(evento: string, data: unknown) {
        controller.enqueue(encoder.encode(`event: ${evento}\ndata: ${JSON.stringify(data)}\n\n`));
        emitidos.push(evento);
        if (evento === "done" || evento === "error") terminalEmitido = evento;
      }
      // ETAPA 2: el cobro aplicado en ESTA entrega (para la red de reembolso
      // del catch). null = aun no se cobra, o el done ya salio.
      let cobroAplicado: { monto: number; concepto: string } | null = null;
      const heartbeat = setInterval(() => controller.enqueue(encoder.encode(": heartbeat\n\n")), INTERVALO_HEARTBEAT_MS);

      try {
        // AUD-09 H05 (PREVIEW_MUNDOS_PLAN §4): el estado vivo ACTUAL del
        // proyecto, leído en el momento del plan. En la compra de un mundo el
        // perfil de la sesión se congeló en el preview; si el proyecto cambió
        // de ciclo desde entonces, el redactor debe ver la realidad de hoy.
        const proyectoParaPlan = await obtenerProyecto(supabase, projectId);
        const estadoVivoActual = (proyectoParaPlan?.estado_vivo as string | null) ?? null;
        if (
          dominioCobro !== "core" &&
          !recorrido.esSeguimiento &&
          estadoVivoActual &&
          !(recorrido.perfilSesion ?? "").includes(estadoVivoActual)
        ) {
          recorrido.perfilSesion = `${recorrido.perfilSesion ?? ""}
Estado actual del proyecto, más reciente que la exploración: ${estadoVivoActual}`.trim();
        }

        const preparacion = prepararPlan(
          recorrido.ruta,
          graph,
          families,
          recorrido.textoOriginal,
          recorrido.perfilSesion,
          recorrido.prioridadDeclarada,
          recorrido.esSeguimiento,
          recorrido.estadoVivoPrevio,
          // AUD-09 M16: la cosecha de un plan de mundo no recoge nodos de otro mundo.
          recorrido.dominiosDesbloqueados ? dominiosDelRecorrido(recorrido) : null
        );

        const { rawTexto, acumulado: acumuladoTrasRedactor, avisoFallback } = await generarTextoPlan(
          client,
          preparacion,
          acumulado,
          (texto) => enviar("delta", { texto }),
          () => enviar("reinicio", { motivo: "reintentando la redaccion" })
        );
        // AUD-09 H02: sin texto del redactor, el plan sale del ensamblado
        // offline. No es lo prometido: no se cobra y se dice en pantalla.
        const versionBasica = rawTexto === null;

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
        if (versionBasica) {
          eventosPlan.push({ tipo: "plan_version_basica", motivo: avisoFallback });
        }
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

        const conceptosTitulos = conceptosDeRuta([...recorrido.ruta, ...resultado.cosechaIds], graph);
        const { estadoVivo, acumulado: acumuladoFinal } = await comprimirEstadoVivo(
          client,
          // AUD-09 H05: el estado anterior es el del proyecto HOY (antes, en la
          // compra de un mundo, llegaba null y la compresión pisaba lo que el
          // ciclo del núcleo había aprendido).
          estadoVivoActual ?? recorrido.estadoVivoPrevio,
          recorrido.perfilSesion,
          conceptosTitulos,
          // El unico camino offline es el techo de la sesion: queda registrado
          // (antes presupuesto_excedido nunca se marcaba en ningun lugar).
          versionBasica ? { ...acumuladoTrasRedactor, presupuesto_excedido: true } : acumuladoTrasRedactor
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
        // Scheduler F1: la estimación NACE con el plan. Se estima la banda de
        // esfuerzo (mayoría-de-3) de cada ítem ANTES de insertarlo. Si la
        // estimación falla, los ítems quedan SIN banda y el plan JAMÁS se
        // bloquea (fallback declarado); el fallo deja síntoma en los eventos.
        const itemsDerivados = derivarChecklist(resultado.markdown);
        let itemsChecklist: Parameters<typeof insertarChecklist>[3] = itemsDerivados;
        let acumuladoTrasEstimacion = acumuladoFinal;
        try {
          const est = await estimarLoteMayoria(client, itemsDerivados, acumuladoFinal);
          acumuladoTrasEstimacion = est.acumulado;
          itemsChecklist = itemsDerivados.map((it, i) => ({
            ...it,
            banda: est.estimaciones[i]?.banda ?? null,
            espera_externa: est.estimaciones[i]?.espera_externa ?? null,
          }));
          const conBanda = est.estimaciones.filter(Boolean).length;
          eventosPlan.push({
            tipo: "estimacion_banda",
            total: itemsDerivados.length,
            con_banda: conBanda,
          });
        } catch (e) {
          // Fallback ruidoso: el plan sigue sin bandas, pero queda el síntoma.
          eventosPlan.push({
            tipo: "estimacion_fallida",
            texto: e instanceof Error ? e.message : String(e),
          });
        }
        // Mundos de proteccion (P2): el ENLACE. Segunda llamada, hermana de la
        // estimacion: el plan ya esta escrito y el usuario ya lo vio; esto solo
        // lo lee y dice que respuesta protege a que actividad del nucleo. Se
        // re-lee el nucleo AHORA (no se reusa el snapshot de la entrevista):
        // el enlace tiene que apuntar a ids que existan en este momento.
        if (esMundoProteccion(dominioSesion)) {
          const planCore = await obtenerPlanCoreVigente(supabase, projectId);
          const filasNucleo = planCore ? await obtenerItemsDePlan(supabase, projectId, planCore) : [];
          const snapshot = armarSnapshot(filasNucleo as unknown as FilaChecklistSnapshot[]);
          const enlace = await enlazarPlanProteccion(
            client,
            itemsDerivados.map((i) => ({ texto: i.texto, etapa: i.etapa })),
            snapshot,
            acumuladoTrasEstimacion
          );
          acumuladoTrasEstimacion = enlace.acumulado;
          itemsChecklist = itemsChecklist.map((it, i) => ({
            ...it,
            protege_item: enlace.enlaces[i]?.protege_item ?? null,
            deteccion: enlace.enlaces[i]?.deteccion ?? null,
            probabilidad: enlace.enlaces[i]?.probabilidad ?? null,
            dolor: enlace.enlaces[i]?.dolor ?? null,
            camino: enlace.enlaces[i]?.camino ?? null,
          }));
          // El costo va MEDIDO al evento (el fundador lo pidio asi), junto con
          // cuantos enlaces se descartaron por apuntar a algo inexistente.
          eventosPlan.push({
            tipo: enlace.fallo ? "enlace_proteccion_fallido" : "enlace_proteccion",
            mundo: dominioSesion,
            total: itemsDerivados.length,
            enlazados: enlace.enlaces.filter(Boolean).length,
            descartados: enlace.descartados,
            costo_usd: Number(enlace.costoUsd.toFixed(4)),
            ...(enlace.fallo ? { texto: enlace.fallo } : {}),
          });
        }
        await insertarChecklist(supabase, projectId, planId, itemsChecklist, dominioSesion,
          resultado.nodosPorEtapa);

        const eventosSesion = [...recorrido.fallbackEvents, ...eventosPlan];
        const { calidad, acumulado: acumuladoConJuez } = await evaluarCalidadSesion(
          client,
          eventosSesion,
          graph,
          acumuladoTrasEstimacion
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
        const faseFinal = faseDeNodo(recorrido.ruta[recorrido.ruta.length - 1], graph);
        const camposProyecto: Record<string, unknown> = { estado_vivo: estadoVivo };
        // La fase del proyecto es la del núcleo: un plan de mundo no la mueve
        // a la fase de su último nodo (AUD-09 H05).
        if (dominioCobro === "core") camposProyecto.fase_actual = faseFinal;
        const titulo = extraerTitulo(resultado.markdown);
        if (titulo && !proyecto?.titulo) camposProyecto.titulo = titulo;
        await actualizarProyecto(supabase, projectId, camposProyecto);

        // ── ETAPA 2 (VIVO): DESCONTAR A LA ENTREGA (docs/FLUJO_TRACKING.md §5,
        // docs/CUENTAS_DISENO.md §5-6). Este punto ES la entrega: el plan ya
        // esta redactado, persistido, con su checklist derivado y la sesion
        // cerrada. Es prerequisito de este cobro que el redactor reintente y,
        // si se agota, LANCE (ver generarTextoPlan): un plan que muere a mitad
        // JAMAS consume creditos. Idempotente por `plan:{sessionId}`: un
        // reintento de la misma entrega no cobra dos veces.
        // Carrera rara (verifico al inicio, otra pestana gasto antes): cobrar
        // devuelve -1 con el plan ya persistido -> ENTREGAR Y REGISTRAR, nunca
        // cobrar de mas ni castigar (la regla sagrada).
        let creditosRestantes: number | null = null;
        if (montoCobro > 0 && !versionBasica) {
          const resultadoCobro = await cobrar(user.id, conceptoCobro, montoCobro, `plan:${sessionId}`);
          if (resultadoCobro === -1) {
            await registrarBitacora(supabase, projectId, "cobro_carrera", {
              session_id: sessionId,
              concepto: conceptoCobro,
              monto: montoCobro,
            });
          } else {
            creditosRestantes = resultadoCobro;
            cobroAplicado = { monto: montoCobro, concepto: conceptoCobro };
          }
        }
        // Fase 4.5 (PREVIEW_MUNDOS_PLAN §5.3): para una sesion de MUNDO, esta
        // entrega es ADEMAS la compra del mundo: se sella plan_pagado_at
        // (idempotente, WHERE IS NULL) + telemetria preview_a_compra (§6).
        // AUD-09, decision del fundador (25 sep 2026): UN SELLO DE PAGO SOLO
        // EXISTE SI HUBO PAGO. Un plan basico (sin IA, no cobrado) no sella la
        // compra: se marca con su propio campo, plan_basico_at (migracion 039),
        // y el mundo ofrece "Generar el plan completo". Tampoco sella la
        // carrera rara (se entrego sin poder cobrar).
        if (dominioSesion !== "core") {
          const ahora = new Date().toISOString();
          if (versionBasica) {
            const { error: errBasico } = await supabase
              .from("project_unlocks")
              .update({ plan_basico_at: ahora })
              .eq("project_id", projectId)
              .eq("dominio", dominioSesion);
            if (errBasico) {
              console.error("[plan] no se pudo marcar el plan basico del mundo (¿falta la migracion 039?):", errBasico);
            }
          } else if (cobroAplicado) {
            const { error: errEscritura1 } = await supabase
              .from("project_unlocks")
              .update({ plan_pagado_at: ahora })
              .eq("project_id", projectId)
              .eq("dominio", dominioSesion)
              .is("plan_pagado_at", null);
            if (errEscritura1) {
              console.error("[app/api/session/[id]/plan/route.ts] update project_unlocks fallo:", errEscritura1);
            }
            // La compra es la primera entrega pagada; un ciclo de seguimiento
            // no es una compra (AUD-09 M36).
            if (!recorrido.esSeguimiento) {
              await registrarBitacora(supabase, projectId, "preview_a_compra", { mundo: dominioSesion });
            }
          }
        }
        enviar("done", {
          project_id: projectId,
          session_id: sessionId,
          markdown: resultado.markdown,
          evaluacion_cobertura: resultado.evaluacionCobertura,
          costo_usd: costoAcumuladoUsd(acumuladoConJuez),
          // El chip refresca su saldo con la entrega (patron del I Ching).
          creditos_restantes: creditosRestantes,
          version_basica: versionBasica,
          aviso: versionBasica ? AVISO_VERSION_BASICA : null,
        });
        cobroAplicado = null; // el done salio: la entrega llego a su dueño
      } catch (e) {
        causaCierre = e;
        // ETAPA 2 — la red del borde del streaming: si algo revento DESPUES
        // de un cobro exitoso y ANTES de que el done llegara, se reembolsa
        // con su log. El usuario JAMAS pierde creditos por un fallo nuestro
        // (si ademas el plan quedo persistido, lo encuentra al recargar:
        // generosidad a favor del usuario, nunca en contra).
        if (cobroAplicado) {
          try {
            await reembolsar(user.id, cobroAplicado.monto, `fallo post-cobro plan:${sessionId} (${cobroAplicado.concepto})`);
          } catch (errRefund) {
            console.error("[plan] FALLO EL REEMBOLSO post-cobro (revisar a mano):", errRefund);
          }
        }
        // Envuelto: si ESTE emit tira (el controller ya roto), su throw
        // escapaba del catch y el finally cerraba EN SILENCIO. Ese era el
        // camino del cierre mudo de la corrida I.
        try {
          enviar("error", { error: e instanceof Error ? e.message : String(e) });
        } catch (errEmit) {
          console.error("[plan] no se pudo emitir el error al cliente:", errEmit);
        }
      } finally {
        clearInterval(heartbeat);
        // NINGUN STREAM TERMINA EN SILENCIO: si no salio done ni error,
        // esto grita por el log del servidor y lo intenta por el canal.
        garantizarTerminal({
          terminalEmitido,
          emitidos,
          causa: causaCierre,
          sessionId,
          projectId,
          enviar,
        });
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
