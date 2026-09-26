/**
 * POST /api/project/[id]/follow — Fase 3.3: port de modo_seguir
 * (engine/prototipo_motor.py línea 2801), el hueco que jamás se había
 * portado. El ritual de 3 tarjetas del frontend (checklist actualizado +
 * detalles + enfoque) entra aquí; el handler:
 *
 *   a. lee estados+notas del checklist del ÚLTIMO plan y compone el
 *      mensaje "qué ha pasado" con componerMensajeSeguimiento — ese texto
 *      queda auditable como mensaje_entrada de la sesión (bitácora);
 *   b. transcribe la entrada de modo_seguir: sesión tipo 'seguimiento',
 *      puerta por seleccionar_puerta_avanzada (cualquier nodo no cubierto,
 *      estado_vivo como contexto del intérprete), visitados = cubiertos ∪
 *      ruta (nodosCubiertosPrevios), y devuelve el primer turno igual que
 *      session/start. La conversación sigue por /turn y /plan sin cambios;
 *      el plan resultante sale con etiqueta 'seguimiento' (ya cableado) y
 *      deriva SU checklist — el bucle queda encadenado.
 *
 * Cobra 1 arranque del límite diario: es una sesión de entrevista nueva,
 * mismo perfil de costo que session/start.
 *
 * Fase 4.2 — FOLLOW DE MUNDO. El ritual dejó de vivir una sola vez: cada mundo
 * activo tiene el suyo, y la ruta recibe `dominio`. Lo que se mueve con él:
 *   - los ítems que componen el mensaje (los de ESE mundo, itemsDelUltimoPlanDe);
 *   - el bloque de realidad (el cumplimiento DE ESE MUNDO contra SUS fechas, más
 *     una línea de contexto global — jamás las tardanzas del core como suyas);
 *   - la puerta, amurallada a los nodos del mundo;
 *   - la sesión, que nace con dominio=mundo → su plan hereda el dominio y deriva
 *     checklist con él (la ruta del plan ya lo hace sola), encadenado dentro del
 *     grupo de ese mundo. Regenera SOLO el plan del mundo.
 * Lo que NO se mueve: la cosecha del vecindario, que sigue amurallada a
 * core+unlocks igual que en el plan original del mundo (world/start:122).
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import catalogo from "@/lib/assets/packs_catalog.json";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { MAX_LARGO_TEXTO_USUARIO, mensajeTextoLargo } from "@/lib/constants";
import { usoVacio } from "@/lib/costmeter";
import { mensajeSaldoInsuficiente, reservarCreditos, resolverReserva, verificarSaldo } from "@/lib/creditos";
import { obtenerModosPorEspacio, crearSesion, dominiosDesbloqueados, nodosCubiertos, obtenerProyecto } from "@/lib/db";
import { idiomaDelProyecto } from "@/lib/i18n/detectarIdioma";
import { avisoLogin, esInvitadoInvisible } from "@/lib/identidad";
import { aviso2FA, faltaSegundoFactor } from "@/lib/seguridad";
import { conceptoDelPlan, PRECIOS } from "@/lib/precios";
import { cargarEntrySeeds, cargarGrafo, cargarPreguntasCache, etiquetaArbol } from "@/lib/engine/graph";
import { analyticsDeMundo, calcularAnalytics } from "@/lib/analytics";
import { cargarEntradaAnalytics, LecturaFallidaError, mensajeLecturaFallida } from "@/lib/analyticsEntrada";
import { construirBloqueRealidad, construirBloqueRealidadMundo } from "@/lib/engine/bloqueRealidad";
import { candidatosSeguimiento, seleccionarPuertaAvanzada } from "@/lib/engine/puertaAvanzada";
import { avanzarTurno, estadoInicial } from "@/lib/engine/recorrido";
import {
  componerMensajeSeguimiento,
  itemsDelUltimoPlanDe,
  type FilaChecklist,
} from "@/lib/engine/seguimientoComposer";
import { identidadLimite, mensajeFusible, mensajeLimite, mensajeServicioNoDisponible, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

/**
 * AUD-09 M22: ¿alcanza el saldo para el ritual de este espacio? El canon §5
 * pide rechazar ANTES de que el usuario escriba su "qué pasó"; Manos a la Obra
 * pregunta aquí antes de abrir el formulario. Solo mira: no gasta el límite del
 * día ni aparta créditos (eso lo hace el POST, al empezar de verdad).
 */
export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const dominio = new URL(request.url).searchParams.get("dominio") || "core";
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(avisoLogin(idioma), { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  }
  const costo = PRECIOS[dominio === "core" ? "seguimiento" : "mundo_seguimiento"];
  const saldo = await verificarSaldo(user.id, costo);
  if (!saldo.alcanza) {
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(saldo.creditos, costo, saldo.apartados, idioma), saldo: saldo.creditos },
      { status: 402 }
    );
  }
  return NextResponse.json({ alcanza: true, costo });
}

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_PROYECTO, idioma).follow;

  let body: { detalles?: unknown; enfoque?: unknown; dominio?: unknown };
  try {
    body = await request.json();
  } catch {
    body = {};
  }
  const detalles = typeof body.detalles === "string" ? body.detalles : null;
  const enfoque = typeof body.enfoque === "string" ? body.enfoque : null;
  // Fase 4.2: sin dominio, el follow es el de siempre (el viaje core).
  const dominio = typeof body.dominio === "string" && body.dominio ? body.dominio : "core";
  for (const valor of [detalles, enfoque]) {
    if (valor && valor.length > MAX_LARGO_TEXTO_USUARIO) {
      return NextResponse.json(
        { error: mensajeTextoLargo(idioma), limite: MAX_LARGO_TEXTO_USUARIO },
        { status: 400 }
      );
    }
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  // ETAPA 2 (la frontera): el seguimiento es motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(avisoLogin(idioma), { status: 401 });
  }
  if (await faltaSegundoFactor()) {
    return NextResponse.json(aviso2FA(idioma), { status: 403 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  }
  // AUD-09 (tanda 5): con la idea REALIZADA no se paga un seguimiento del
  // núcleo, igual que un mundo completado no se replanifica. Cerrar es
  // reversible de un toque, así que esto no encierra a nadie. Va antes del
  // saldo y de los límites: nadie gasta nada en un rechazo.
  if (dominio === "core" && proyecto.realizada_at) {
    return NextResponse.json(
      { error: t.ideaRealizada },
      { status: 409 }
    );
  }

  // Fase 4.2: el mundo debe existir, estar activado y estar ABIERTO. Igual que
  // world/start, esto va ANTES de cobrar el arranque: nadie quema una consulta
  // en un 403.
  const entradaCatalogo = (catalogo.packs as Array<{ clave: string; nombre: string }>).find(
    (p) => p.clave === dominio
  );
  let nombreMundo = "";
  if (dominio !== "core") {
    if (!entradaCatalogo) {
      return NextResponse.json({ error: r.mundoNoExiste }, { status: 404 });
    }
    nombreMundo = entradaCatalogo.nombre;
    const { data: unlock } = await supabase
      .from("project_unlocks")
      .select("id, completado_at")
      .eq("project_id", projectId)
      .eq("dominio", dominio)
      .limit(1);
    if (!unlock || unlock.length === 0) {
      return NextResponse.json(
        { error: interpolar(r.mundoNoActivado, { mundo: nombreDeMundo(dominio, idioma) }) },
        { status: 403 }
      );
    }
    // Un mundo cerrado no se replanifica: se reabre primero. El cierre es
    // reversible de un toque, así que esto no encierra a nadie.
    if ((unlock[0] as { completado_at?: string | null }).completado_at) {
      return NextResponse.json(
        { error: interpolar(t.mundoCompletado, { mundo: nombreDeMundo(dominio, idioma) }) },
        { status: 409 }
      );
    }
  }

  // ── ANCLA para la ETAPA 2 del frente de cuentas (rama cuentas-y-creditos)
  // Aqui, y NO antes, va la VERIFICACION de saldo del follow, TANTO core como
  // mundo, al precio de precios.ts (seguimiento y mundo_seguimiento; la unica
  // fuente, FLUJO_TRACKING §5 la refleja). Este es el
  // punto correcto porque, en el caso mundo, el mundo ya se valido (existe, esta
  // activado y esta abierto): verificar antes cobraria un 403 o un 404. El
  // patron es el del plan (session/[id]/plan:309): verificar saldo al inicio y
  // DESCONTAR A LA ENTREGA — el descuento va al final de esta ruta, no aqui.
  //
  // Correccion 2026-07-17: un comentario anterior aqui decia "el follow core no
  // cobra creditos: es el bucle del viaje principal". Eso divergia de precios.ts
  // y nadie lo autorizo; el seguimiento core cobra su precio, igual que el de
  // mundo.
  //

  // ETAPA 2 — VERIFICAR al inicio (no cobrar): el seguimiento cobra su precio
  // de precios.ts (core o mundo). El descuento ocurre a la entrega del plan del ciclo.
  const montoFollow = PRECIOS[dominio === "core" ? "seguimiento" : "mundo_seguimiento"];
  const saldoFollow = await verificarSaldo(user.id, montoFollow);
  if (!saldoFollow.alcanza) {
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(saldoFollow.creditos, montoFollow, 0, idioma), saldo: saldoFollow.creditos },
      { status: 402 }
    );
  }

  // AUD-09 M25 (decisión del fundador, 25 sep 2026): RESERVA al empezar, con
  // la clave del cobro de la sesión que va a nacer (id generado aquí). Si otra
  // sesión ya apartó el saldo, 402 antes de crear nada ni gastar el límite. Todo
  // rechazo posterior de esta ruta suelta la reserva.
  const sessionIdNueva = crypto.randomUUID();
  const claveReserva = `plan:${sessionIdNueva}`;
  const reserva = await reservarCreditos(user.id, claveReserva, conceptoDelPlan(dominio, true), montoFollow);
  if (!reserva.reservado) {
    const ahora = await verificarSaldo(user.id, montoFollow, claveReserva);
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(ahora.creditos, montoFollow, ahora.apartados, idioma), saldo: ahora.creditos },
      { status: 402 }
    );
  }
  const soltarReserva = () => resolverReserva(claveReserva, "liberada");

  // AUD-09 (tanda 2): fusible y límite diario DESPUÉS del saldo (un rechazo por
  // saldo ya no gasta el arranque del día) y siempre antes de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    await soltarReserva();
    return NextResponse.json({ error: fusible.caido ? mensajeServicioNoDisponible(idioma) : mensajeFusible(idioma) }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    await soltarReserva();
    return NextResponse.json(
      { error: limite.caido ? mensajeServicioNoDisponible(idioma) : mensajeLimite(limite.limite, idioma) },
      { status: limite.caido ? 503 : 429 }
    );
  }

  // (a) El checklist del último plan DEL DOMINIO (por fecha de inserción) con
  // estados y notas — la historia real del avance, sin que el usuario la
  // redacte.
  //
  // Fase 4.1 (V4, auditoría de paridad de mundos): el filtro de dominio NO es
  // decorativo. La consulta tomaba el plan del ítem más reciente FUERA CUAL
  // FUERA su dominio: si el usuario acababa de explorar un mundo, "Contar qué
  // pasó" componía su "mi avance real" con el checklist del MUNDO mientras el
  // bloque de realidad llevaba cumplimiento core — el mensaje y el bloque
  // describiendo dominios distintos. En el vuelo no se manifestó por suerte del
  // orden. Fase 4.2: el ancla que quedó aquí ya es código — el dominio entra por
  // el body y manda sobre los ítems, el bloque y la puerta.
  // no_aplica_motivo llega con la 030: se reintenta sin ella si aún no está.
  const COLS_FOLLOW = "plan_id, dominio, etapa, texto, destacado, estado, nota, created_at";
  const leerFollow = (cols: string) =>
    supabase
      .from("checklist_items")
      .select(cols)
      .eq("project_id", projectId)
      .order("created_at", { ascending: false })
      .order("etapa", { ascending: true })
      .order("orden", { ascending: true });
  let { data: filas, error: errorItems } = await leerFollow(`${COLS_FOLLOW}, no_aplica_motivo`);
  if (errorItems) ({ data: filas, error: errorItems } = await leerFollow(COLS_FOLLOW));
  if (errorItems) {
    await soltarReserva();
    return NextResponse.json({ error: r.noPudimosLeerChecklist }, { status: 500 });
  }
  const items = itemsDelUltimoPlanDe((filas ?? []) as unknown as FilaChecklist[], dominio);
  // Un mundo sin checklist propio no tiene nada que seguir: primero se explora.
  if (dominio !== "core" && items.length === 0) {
    await soltarReserva();
    return NextResponse.json(
      { error: interpolar(t.primeroExplora, { mundo: nombreDeMundo(dominio, idioma) }) },
      { status: 409 }
    );
  }

  // Fase 4.0 §3 (docs/FLUJO_TRACKING.md): el BLOQUE DE REALIDAD. Antes el
  // follow solo mandaba lo que el usuario MARCO; el motor replanificaba ciego
  // al tiempo. Ahora lee el mismo analytics.ts que el Analisis: cumplimiento,
  // donde se atora, replanificaciones y ritmo real.
  //
  // Fase 4.2: el bloque de un MUNDO se mide con la misma vara pero con SUS
  // datos (analyticsDeMundo: sus items, contra sus fechas, desde su unlock), y
  // del proyecto solo lleva una linea de contexto rotulada.
  // AUD-09 M18: una lectura fallida se dice (503), no se pinta en cero.
  let entradaAnalytics: Awaited<ReturnType<typeof cargarEntradaAnalytics>>;
  try {
    entradaAnalytics = await cargarEntradaAnalytics(supabase, projectId, proyecto);
  } catch (e) {
    await soltarReserva();
    if (e instanceof LecturaFallidaError) return NextResponse.json({ error: mensajeLecturaFallida(idioma) }, { status: 503 });
    throw e;
  }
  const analytics = calcularAnalytics(entradaAnalytics);
  let bloqueRealidad: string | null;
  if (dominio === "core") {
    bloqueRealidad = construirBloqueRealidad(analytics);
  } else {
    const aMundo = analyticsDeMundo(entradaAnalytics, dominio);
    // AUD-09 M10: el modo del MUNDO (project_modos), no el del núcleo.
    const modoMundo = (await obtenerModosPorEspacio(supabase, projectId))[dominio] ?? null;
    bloqueRealidad = aMundo ? construirBloqueRealidadMundo(aMundo, analytics, nombreMundo, modoMundo) : null;
  }

  const mensaje = componerMensajeSeguimiento({ items, detalles, enfoque, bloqueRealidad });

  // (b) Entrada de modo_seguir, línea por línea.
  const graph = cargarGrafo();
  const entrySeeds = cargarEntrySeeds();
  const preguntasCache = cargarPreguntasCache();
  const families = cargarFamilies();

  const cubiertos = await nodosCubiertos(supabase, projectId);
  const estadoVivoPrevio = (proyecto.estado_vivo as string | null) ?? null;
  // Fase 3.5: core + unlocks; solo-core si la 016 aún no está aplicada.
  let dominios = ["core"];
  try {
    dominios = await dominiosDesbloqueados(supabase, projectId);
  } catch {
    dominios = ["core"];
  }

  // Fase 4.2: la PUERTA de un follow de mundo se amuralla a los nodos de ese
  // mundo. La cosecha del vecindario NO (más abajo): sigue con core+unlocks,
  // igual que el plan original del mundo. Elegir la puerta con el intérprete —
  // y no con la semilla determinística de evaluacionBrecha, como en
  // world/start — es deliberado: en un seguimiento el mensaje YA trae la
  // realidad medida, y esa es justo la señal con la que se debe elegir por
  // dónde entrar. Es el mismo trato que recibe el core.
  const dominiosPuerta = dominio === "core" ? dominios : [dominio];
  if (dominio !== "core") {
    const hayPuerta = candidatosSeguimiento(
      mensaje,
      estadoVivoPrevio,
      (proyecto.fase_actual as string | null) ?? "ideacion",
      families,
      graph,
      cubiertos,
      undefined,
      dominiosPuerta
    );
    // Sin candidatos del mundo, seleccionarPuertaAvanzada caería a entrySeeds[0]
    // — un nodo CORE — y el plan del mundo saldría explorando el viaje
    // principal. Antes que eso, se dice la verdad.
    if (hayPuerta.length === 0) {
      await soltarReserva();
      return NextResponse.json(
        { error: interpolar(t.puertasRecorridas, { mundo: nombreDeMundo(dominio, idioma) }) },
        { status: 409 }
      );
    }
  }

  // El mensaje compuesto es el mensaje_entrada de la sesión: bitácora.
  // La sesión nace con el dominio del mundo: su plan lo hereda y deriva su
  // checklist con él (session/[id]/plan:260), encadenado en el grupo del mundo.
  const sessionId = await crearSesion(supabase, user.id, projectId, "seguimiento", mensaje, null, dominio, { id: sessionIdNueva });

  const client = createAnthropicClient();
  const acumulado = usoVacio();

  const puerta = await seleccionarPuertaAvanzada(
    client,
    mensaje,
    estadoVivoPrevio,
    (proyecto.fase_actual as string | null) ?? "ideacion",
    families,
    graph,
    cubiertos,
    entrySeeds,
    acumulado,
    dominiosPuerta
  );

  const estado = estadoInicial({
    actualId: puerta.puertaId,
    perfilSesion: puerta.perfilSesion,
    textoOriginal: mensaje,
    esSeguimiento: true,
    estadoVivoPrevio,
    nodosCubiertosPrevios: [...cubiertos],
    dominiosDesbloqueados: dominios,
    // Fase 4.3: un follow de mundo es una sesion de mundo. Misma regla.
    dominioSesion: dominio,
    idioma: idiomaDelProyecto(proyecto),
  });

  const resultado = await avanzarTurno({
    client,
    graph,
    families,
    preguntasCache,
    estado,
    respuestaUsuario: null,
    acumulado: puerta.acumulado,
    dbSessionId: sessionId,
    idioma,
  });

  // Igual que session/start: la puerta vive en la ruta desde estadoInicial
  // y el diff de nodos nuevos no la incluye — se antepone para el árbol.
  const nodoPuerta = {
    id: puerta.puertaId,
    etiqueta: etiquetaArbol(puerta.puertaId, graph, idioma),
    modo: "conversado" as const,
  };

  // El follow NO cobra aqui (corregido en la AUD-09: este comentario decia que el
  // descuento iba en este punto). El cobro del seguimiento, core o mundo, ocurre
  // a la ENTREGA de su plan, en session/[id]/plan: un follow que muere en el
  // camino no se cobra.
  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado, [nodoPuerta], [], idioma);
}
