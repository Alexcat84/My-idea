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
import { createAnthropicClient } from "@/lib/anthropicClient";
import { responderResultadoTurno } from "@/lib/apiSesion";
import catalogo from "@/lib/assets/packs_catalog.json";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { usoVacio } from "@/lib/costmeter";
import { mensajeSaldoInsuficiente, verificarSaldo } from "@/lib/creditos";
import { crearSesion, dominiosDesbloqueados, nodosCubiertos, obtenerProyecto } from "@/lib/db";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { AVISO_2FA, faltaSegundoFactor } from "@/lib/seguridad";
import { PRECIOS } from "@/lib/precios";
import { cargarEntrySeeds, cargarGrafo, cargarPreguntasCache, etiquetaArbol } from "@/lib/engine/graph";
import { analyticsDeMundo, calcularAnalytics } from "@/lib/analytics";
import { cargarEntradaAnalytics } from "@/lib/analyticsEntrada";
import { construirBloqueRealidad, construirBloqueRealidadMundo } from "@/lib/engine/bloqueRealidad";
import { candidatosSeguimiento, seleccionarPuertaAvanzada } from "@/lib/engine/puertaAvanzada";
import { avanzarTurno, estadoInicial } from "@/lib/engine/recorrido";
import {
  componerMensajeSeguimiento,
  itemsDelUltimoPlanDe,
  type FilaChecklist,
} from "@/lib/engine/seguimientoComposer";
import { identidadLimite, MENSAJE_FUSIBLE, MENSAJE_LIMITE, verificarFusibleGlobal, verificarLimiteDiario } from "@/lib/rateLimit";
import { cargarFamilies } from "@/lib/readiness";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

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
  for (const [campo, valor] of [
    ["detalles", detalles],
    ["enfoque", enfoque],
  ] as const) {
    if (valor && valor.length > MAX_LARGO_TEXTO_USUARIO) {
      return NextResponse.json(
        { error: `'${campo}' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
        { status: 400 }
      );
    }
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  // ETAPA 2 (la frontera): el seguimiento es motor pagado; cuenta real.
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(AVISO_LOGIN, { status: 401 });
  }
  if (await faltaSegundoFactor()) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
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
      return NextResponse.json({ error: "ese mundo no existe" }, { status: 404 });
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
        { error: `El mundo "${nombreMundo}" aún no está activado para esta idea.` },
        { status: 403 }
      );
    }
    // Un mundo cerrado no se replanifica: se reabre primero. El cierre es
    // reversible de un toque, así que esto no encierra a nadie.
    if ((unlock[0] as { completado_at?: string | null }).completado_at) {
      return NextResponse.json(
        { error: `Diste "${nombreMundo}" por completado. Reábrelo si quieres seguir trabajándolo.` },
        { status: 409 }
      );
    }
  }

  // ── ANCLA para la ETAPA 2 del frente de cuentas (rama cuentas-y-creditos)
  // Aqui, y NO antes, va la VERIFICACION de saldo del follow: 2 creditos, TANTO
  // core como mundo. La fuente de verdad es precios.ts (seguimiento: 2,
  // mundo_seguimiento: 2) + FLUJO_TRACKING §5 ("2 core / 2 mundo"). Este es el
  // punto correcto porque, en el caso mundo, el mundo ya se valido (existe, esta
  // activado y esta abierto): verificar antes cobraria un 403 o un 404. El
  // patron es el del plan (session/[id]/plan:309): verificar saldo al inicio y
  // DESCONTAR A LA ENTREGA — el descuento va al final de esta ruta, no aqui.
  //
  // Correccion 2026-07-17: un comentario anterior aqui decia "el follow core no
  // cobra creditos: es el bucle del viaje principal". Eso divergia de precios.ts
  // (seguimiento: 2) y nadie lo autorizo; el seguimiento core cuesta 2, igual
  // que el de mundo.
  //
  // Pre-beta: fusible global ANTES de cobrar creditos y de tocar la API.
  const fusible = await verificarFusibleGlobal(user.email);
  if (!fusible.permitido) {
    return NextResponse.json({ error: MENSAJE_FUSIBLE }, { status: 503 });
  }
  const limite = await verificarLimiteDiario(identidadLimite(user.id, request), user.email);
  if (!limite.permitido) {
    return NextResponse.json({ error: MENSAJE_LIMITE }, { status: 429 });
  }

  // ETAPA 2 — VERIFICAR al inicio (no cobrar): el seguimiento cuesta 2 (core
  // o mundo, precios.ts). El descuento ocurre a la entrega del plan del ciclo.
  const montoFollow = PRECIOS[dominio === "core" ? "seguimiento" : "mundo_seguimiento"];
  const saldoFollow = await verificarSaldo(user.id, montoFollow);
  if (!saldoFollow.alcanza) {
    return NextResponse.json(
      { error: mensajeSaldoInsuficiente(saldoFollow.creditos, montoFollow), saldo: saldoFollow.creditos },
      { status: 402 }
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
    return NextResponse.json({ error: "no pudimos leer tu checklist" }, { status: 500 });
  }
  const items = itemsDelUltimoPlanDe((filas ?? []) as unknown as FilaChecklist[], dominio);
  // Un mundo sin checklist propio no tiene nada que seguir: primero se explora.
  if (dominio !== "core" && items.length === 0) {
    return NextResponse.json(
      { error: `Primero explora "${nombreMundo}" — su seguimiento nace de su plan.` },
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
  const entradaAnalytics = await cargarEntradaAnalytics(supabase, projectId, proyecto);
  const analytics = calcularAnalytics(entradaAnalytics);
  let bloqueRealidad: string | null;
  if (dominio === "core") {
    bloqueRealidad = construirBloqueRealidad(analytics);
  } else {
    const aMundo = analyticsDeMundo(entradaAnalytics, dominio);
    bloqueRealidad = aMundo ? construirBloqueRealidadMundo(aMundo, analytics, nombreMundo) : null;
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
      return NextResponse.json(
        { error: `Ya recorriste todas las puertas de "${nombreMundo}".` },
        { status: 409 }
      );
    }
  }

  // El mensaje compuesto es el mensaje_entrada de la sesión: bitácora.
  // La sesión nace con el dominio del mundo: su plan lo hereda y deriva su
  // checklist con él (session/[id]/plan:260), encadenado en el grupo del mundo.
  const sessionId = await crearSesion(supabase, user.id, projectId, "seguimiento", mensaje, null, dominio);

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
  });

  // Igual que session/start: la puerta vive en la ruta desde estadoInicial
  // y el diff de nodos nuevos no la incluye — se antepone para el árbol.
  const nodoPuerta = {
    id: puerta.puertaId,
    etiqueta: etiquetaArbol(puerta.puertaId, graph),
    modo: "conversado" as const,
  };

  // ── ANCLA para la ETAPA 2 del frente de cuentas: el DESCUENTO de los 2
  // creditos del follow de mundo va aqui (solo si dominio !== "core"). Este es
  // el punto de entrega: la sesion existe, la puerta esta elegida y el primer
  // turno esta listo para el usuario. Ni un credito antes: un follow que muere
  // en el camino no se cobra.
  return responderResultadoTurno(supabase, projectId, sessionId, resultado, resultado.acumulado, [nodoPuerta]);
}
