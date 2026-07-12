// Fase 3.0.1: "vuelo" del cerebro web completo, vía HTTP real contra un
// `next dev` corriendo en local -- no llamadas de funcion in-process, sino
// las mismas rutas que usaria un cliente real, incluyendo el streaming SSE
// de /api/session/[id]/plan. Seis verificaciones:
//   0. (Fase 3.1) Caso sintetico, sin API: el verificador de numeros
//      huerfanos SI dispara el flag ante un numero inyectado.
//   1. Organizer (capa gratuita) con la idea del "sonar" para ciegos.
//   2. Sesion completa de macetas (entrevista real turno a turno + plan
//      streaming por SSE). Incluye una respuesta calibrada (Fase 2.8/2.9)
//      que dispara un salto semantico real, y verifica que la ruta lo
//      registre, que el ensamblado del plan no reviente con 23514 (el
//      bug real de la migracion 012), que project_nodes persista
//      tipo='salto', y (Fase 3.1) que sessions.decisiones tenga la
//      bitacora de decision_turno con el score de cada salto y que la
//      procedencia por etapa del plan haya validado.
//   3. Reporte digital -- fijos=200, precio=13 -> equilibrio esperado 16
//      (ceil(200/13)), vocabulario sin "pieza", y (Fase 3.1) 0 numeros
//      huerfanos en sessions.decisiones.
//   4. Guardian GIGO -- los mismos numeros contaminados del caso real de
//      Motor v2.2 (costo=200 leido como budget mensual, horas=4 leidas
//      como meses, precio=13) deben abortar la narracion, no producir un
//      margen de -2976.9% narrado con confianza.
//
// Autenticacion: inicia sesion como el dev user (scripts/setup_dev_user.py)
// usando @supabase/ssr con un cookie-jar en memoria -- el mismo mecanismo
// de cookies que usan las rutas reales (lib/supabase/server.ts), asi que
// las llamadas HTTP llevan una sesion identica a la de un usuario real
// logueado (proxy.ts/allowlist de Fase 3.0 item 9 todavia no existen, asi
// que cualquier usuario autenticado pasa el chequeo de las rutas).
//
// Uso: con `pnpm dev` corriendo en otra terminal (puerto 3000),
//   npx tsx scripts/vuelo.ts
// Costo real: llamadas reales a Anthropic (Haiku+Sonnet) y Voyage AI.
// Transcripcion + costos guardados en examples/fase3_0_vuelo_web.txt.
import { createClient } from "@supabase/supabase-js";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, consumirSSE, getJson, patchJson, postJson, ROOT } from "./_shared/http";
import { verificarNumerosHuerfanos } from "../lib/verificadorHuerfanos";

cargarEnvRaiz();

// Fase 3.1: cliente service-role para verificar directamente lo que
// quedo persistido en Supabase (project_nodes.tipo, sessions.decisiones)
// -- un cliente autenticado como usuario normal no puede ver esto por
// RLS, y estas son verificaciones de auditoria, no parte del flujo real
// de un usuario.
const supabaseAdmin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

const MAX_TURNOS_SEGURIDAD = 20;

const lineasTranscripcion: string[] = [];
function log(linea: string = "") {
  console.log(linea);
  lineasTranscripcion.push(linea);
}

function separador(titulo: string) {
  log("");
  log("=".repeat(78));
  log(`  ${titulo}`);
  log("=".repeat(78));
}

// ---------------------------------------------------------------------------
// Fase 1: organizer -- la idea real del "sonar" para ciegos ya presente en
// el dataset de pruebas de este proyecto (capa gratuita, una sola llamada).
// ---------------------------------------------------------------------------
async function faseOrganizerSonar(cookie: string) {
  separador("FASE 1: organizer (capa gratuita) -- idea del sonar para ciegos");
  const texto =
    "Tengo una idea de una app que ayuda a personas ciegas a guiarse por sonidos con un sensor tipo sonar y alertas en tiempo real";
  const inicio = Date.now();
  const r = await postJson(cookie, "/api/organizer", { texto });
  log(`project_id: ${r.project_id}`);
  log(`costo_usd: ${r.costo_usd}`);
  log(`tiempo: ${Date.now() - inicio}ms`);
  log("--- markdown (primeras 500 chars) ---");
  log(String(r.markdown).slice(0, 500));
  if (typeof r.markdown !== "string" || !r.markdown.includes("# Organizador de tu idea")) {
    throw new Error("organizer: markdown no tiene el formato esperado");
  }
  return { costoUsd: Number(r.costo_usd) };
}

// ---------------------------------------------------------------------------
// Fase 2: sesion completa de macetas de cemento, entrevista real turno a
// turno (silencioso multi-hop incluido) hasta agotar preguntas o llegar a
// MAX_TURNOS_SEGURIDAD, despues ensambla el plan por SSE.
// ---------------------------------------------------------------------------
const RESPUESTAS_MACETAS = [
  "Hago macetas de cemento decorativas, chicas y medianas, las vendo a tiendas de plantas y directo por Instagram.",
  // Hotfix v2.2.2: query de referencia de la Fase 2.8/2.9 -- calibrada
  // para disparar un salto semantico real a "Hoja de Trabajo de
  // Estimacion de Costos" (MIN_SCORE_SALTO en prototipo_motor.py se
  // calibro especificamente con este score, 0.474, para que este salto
  // SIGA pasando el umbral). Ver examples/fase2_8_macetas_navegacion_libre.txt
  // linea 100 y docs/audits/AUD-03. Antes de este hotfix, vuelo.ts nunca
  // ejercitaba el camino de persistencia de un salto real.
  "Cobro por pieza pero no he calculado bien cuanto me cuesta en minutos y materiales hacer cada maceta.",
  "Llevo dos meses vendiendo, ya tengo unas 15 ventas reales, sobre todo por Instagram y una tienda de plantas que me las revende.",
  "Lo que mas me preocupa es no saber si el precio que cobro de verdad me deja ganancia una vez que cuento mi tiempo.",
  "Cada maceta me cuesta como 68 en materiales -- cemento, moldes, pintura -- y le dedico un par de horas entre mezclar, moldear y pulir.",
  "Valoro mi hora de trabajo en unos 17, aunque nunca lo habia puesto en numeros asi.",
  "Las vendo en 85 cada una, mas o menos, dependiendo del tamano.",
  "Puedo hacer unas 10 a la semana trabajando en mis ratos libres, sin descuidar mi otro trabajo.",
  "Tengo costos fijos como de 200 al mes: renta de un rincon del taller de un amigo y las herramientas que voy comprando.",
  "No he hablado con clientes de forma organizada, solo veo que la gente compra por Instagram, nunca les he preguntado directamente por que.",
  "Mi plan es ir a mercados locales de fin de semana para validar si la gente las compra en persona, no solo en redes.",
  "Si, tiene sentido, sigamos con lo que sigue.",
  "Claro, cuentame que sigue.",
  "Si, estoy de acuerdo con eso.",
  "Me gustaria tambien vender a traves de una pagina web propia mas adelante, pero por ahora es solo Instagram y la tienda.",
  "No he calculado un punto de equilibrio antes, nunca lo habia pensado en esos terminos.",
  "Si, eso resume bien mi situacion actual.",
  "Continuemos, quiero ver el plan completo.",
  "De acuerdo, sigamos.",
];

async function faseSesionMacetas(cookie: string) {
  separador("FASE 2: sesion completa de macetas de cemento (HTTP + SSE)");
  const textoInicial =
    "Hago y vendo macetas de cemento decorativas, ya tengo ventas reales por Instagram, pero no se si el precio que cobro de verdad me deja ganancia.";

  let costoUsd = 0;
  let idx = 0;
  const siguienteRespuesta = () => RESPUESTAS_MACETAS[Math.min(idx++, RESPUESTAS_MACETAS.length - 1)];

  log(`Entrada inicial: "${textoInicial}"`);
  let r = await postJson(cookie, "/api/session/start", { texto: textoInicial });
  log(`project_id: ${r.project_id}, session_id: ${r.session_id}`);
  costoUsd = Number(r.costo_usd ?? 0);

  const projectId = String(r.project_id);
  const sessionId = String(r.session_id);
  let turnos = 0;
  const nodosSalto: Array<{ id: string; titulo: string }> = [];
  // Fase 3.2: el "árbol que piensa" de la UI se alimenta EXACTAMENTE de
  // estos nodos_nuevos -- acumularlos todos permite verificar al final
  // que los eventos mostrados == la ruta persistida, 1:1 y en orden.
  const eventosArbol: Array<{ id: string; modo: string }> = [];

  function registrarNodosNuevos(nodosNuevos: unknown) {
    if (!Array.isArray(nodosNuevos)) return;
    for (const n of nodosNuevos as Array<{ id: string; titulo: string; modo: string }>) {
      eventosArbol.push({ id: n.id, modo: n.modo });
      if (n.modo === "salto") nodosSalto.push({ id: n.id, titulo: n.titulo });
    }
  }
  // /api/session/start puede hacer multi-hop silencioso ANTES de la
  // primera pregunta (igual que /turn) -- si no se registra aqui, un
  // salto real ocurrido en el arranque nunca se contabiliza.
  registrarNodosNuevos(r.nodos_nuevos);

  while (r.tipo === "pregunta" && turnos < MAX_TURNOS_SEGURIDAD) {
    turnos++;
    const pregunta = String(r.pregunta);
    const respuesta = siguienteRespuesta();
    log(`\n[turno ${turnos}] PREGUNTA: ${pregunta}`);
    log(`[turno ${turnos}] RESPUESTA: ${respuesta}`);
    r = await postJson(cookie, `/api/session/${sessionId}/turn`, { respuesta });
    costoUsd = Number(r.costo_usd ?? costoUsd);
    if (Array.isArray(r.nodos_nuevos) && r.nodos_nuevos.length > 0) {
      log(`  nodos nuevos: ${(r.nodos_nuevos as Array<{ titulo: string; modo: string }>).map((n) => `${n.titulo} [${n.modo}]`).join(", ")}`);
    }
    registrarNodosNuevos(r.nodos_nuevos);
  }
  registrarNodosNuevos(r.nodos_nuevos);

  log(`\nInterprete se detuvo tras ${turnos} turno(s). tipo final: ${r.tipo}`);
  if (r.tipo === "salio") {
    throw new Error("la sesion de macetas termino en 'salio' (el interprete decidio salir) -- revisar guion de respuestas");
  }
  log(`costo acumulado hasta aqui: $${costoUsd.toFixed(4)}`);

  separador("FASE 2b: ensamblando el plan (SSE streaming)");
  const inicioPlan = Date.now();
  const resPlan = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resPlan.ok) {
    throw new Error(`POST /api/session/${sessionId}/plan -> ${resPlan.status}`);
  }

  let markdownFinal = "";
  let costoUsdPlan = costoUsd;
  let evaluacionCobertura: unknown = null;
  let deltas = 0;
  const avisos: string[] = [];
  const erroresSSE: string[] = [];

  await consumirSSE(resPlan, ({ evento, data }) => {
    if (evento === "delta") {
      deltas++;
      process.stdout.write(".");
    } else if (evento === "aviso") {
      avisos.push(String((data as { mensaje?: string })?.mensaje ?? ""));
      log(`\n[aviso] ${(data as { mensaje?: string })?.mensaje}`);
    } else if (evento === "error") {
      erroresSSE.push(JSON.stringify(data));
      log(`\n[error SSE] ${JSON.stringify(data)}`);
    } else if (evento === "done") {
      const d = data as { markdown: string; costo_usd: number; evaluacion_cobertura: unknown };
      markdownFinal = d.markdown;
      costoUsdPlan = d.costo_usd;
      evaluacionCobertura = d.evaluacion_cobertura;
    }
  });
  process.stdout.write("\n");

  log(`SSE: ${deltas} deltas de texto recibidos, ${avisos.length} aviso(s), tiempo total: ${Date.now() - inicioPlan}ms`);
  log(`evaluacion_cobertura: ${JSON.stringify(evaluacionCobertura)}`);
  log(`costo_usd (sesion completa, incluye el plan): $${costoUsdPlan.toFixed(4)}`);
  log("--- plan generado (completo) ---");
  log(markdownFinal);

  if (erroresSSE.length > 0) {
    throw new Error(
      `el ensamblado del plan reporto error(es) SSE -- esto es exactamente como se manifesto el bug de la ` +
      `migracion 012 (23514, project_nodes_tipo_check) en vivo: ${erroresSSE.join(" | ")}`
    );
  }
  if (!markdownFinal || markdownFinal.length < 100) {
    throw new Error("el plan generado esta vacio o sospechosamente corto");
  }

  separador("FASE 2c (Hotfix v2.2.2): verificando persistencia real de saltos semanticos");
  if (nodosSalto.length === 0) {
    throw new Error(
      "la sesion de macetas no produjo ningun salto semantico real -- la query de referencia " +
        "(Fase 2.8/2.9, 'cobro por pieza pero no he calculado bien...') dejo de disparar el salto a " +
        "'Hoja de Trabajo de Estimacion de Costos'; revisar MIN_SCORE_SALTO o el guion de RESPUESTAS_MACETAS"
    );
  }
  log(`saltos detectados en la ruta: ${nodosSalto.map((n) => `${n.titulo} (${n.id})`).join(", ")}`);

  for (const nodo of nodosSalto) {
    const { data: fila, error } = await supabaseAdmin
      .from("project_nodes")
      .select("tipo")
      .eq("project_id", projectId)
      .eq("node_id", nodo.id)
      .limit(1)
      .single();
    if (error || !fila) {
      throw new Error(`no se encontro la fila de project_nodes para el salto a '${nodo.id}': ${error?.message}`);
    }
    if (fila.tipo !== "salto") {
      throw new Error(`el nodo '${nodo.id}' llego por salto pero quedo persistido con tipo='${fila.tipo}' (se esperaba 'salto')`);
    }
    log(`  OK: project_nodes.tipo='salto' persistido correctamente para '${nodo.id}'`);
  }

  separador("FASE 2d (Fase 3.1): verificando la bitacora de decisiones (caja de vidrio)");
  const { data: filaSesion, error: errorSesion } = await supabaseAdmin
    .from("sessions")
    .select("decisiones")
    .eq("id", sessionId)
    .limit(1)
    .single();
  if (errorSesion || !filaSesion) {
    throw new Error(`no se encontro la fila de sessions para verificar decisiones: ${errorSesion?.message}`);
  }
  const decisiones = (filaSesion.decisiones ?? []) as Array<Record<string, unknown>>;
  const turnosDecision = decisiones.filter((d) => d.tipo === "decision_turno");
  const turnosSaltoConScore = turnosDecision.filter((d) => {
    const decision = d.decision as { es_salto?: boolean; camino?: string[] } | undefined;
    if (!decision?.es_salto) return false;
    const destino = decision.camino?.[0];
    const saltosPosibles = (d.saltos_posibles as Array<{ id: string; afinidad: number }>) ?? [];
    return saltosPosibles.some((sp) => sp.id === destino && typeof sp.afinidad === "number");
  });
  log(`decision_turno persistidos: ${turnosDecision.length}, con salto+score verificable: ${turnosSaltoConScore.length}`);
  if (turnosSaltoConScore.length !== nodosSalto.length) {
    throw new Error(
      `se esperaban ${nodosSalto.length} decision_turno con salto+score en sessions.decisiones, se encontraron ${turnosSaltoConScore.length}`
    );
  }
  log(`OK: los ${nodosSalto.length} saltos quedaron en la bitacora con su score de afinidad.`);

  const procedenciaInvalida = decisiones.filter((d) => d.tipo === "procedencia_invalida");
  if (procedenciaInvalida.length > 0) {
    throw new Error(`se encontraron eventos procedencia_invalida inesperados: ${JSON.stringify(procedenciaInvalida)}`);
  }
  log("OK: procedencia por etapa valida (sin eventos procedencia_invalida en la bitacora).");

  separador("FASE 2e (Fase 3.2): eventos del arbol == ruta persistida, 1:1 y en orden");
  const { data: filaRuta, error: errorRuta } = await supabaseAdmin
    .from("sessions")
    .select("ruta")
    .eq("id", sessionId)
    .limit(1)
    .single();
  if (errorRuta || !filaRuta) {
    throw new Error(`no se pudo leer sessions.ruta para verificar el arbol: ${errorRuta?.message}`);
  }
  const rutaPersistida = (filaRuta.ruta ?? []) as Array<{ node_id: string; tipo: string }>;
  const arbolStr = eventosArbol.map((n) => `${n.id}[${n.modo}]`).join(" -> ");
  const rutaStr = rutaPersistida.map((n) => `${n.node_id}[${n.tipo}]`).join(" -> ");
  log(`eventos del arbol (${eventosArbol.length}): ${arbolStr}`);
  log(`ruta persistida  (${rutaPersistida.length}): ${rutaStr}`);
  if (arbolStr !== rutaStr) {
    throw new Error(
      "los eventos que la UI mostraria en el arbol NO coinciden 1:1 con sessions.ruta -- la animacion dejaria de ser verdad"
    );
  }
  log("OK: el arbol que piensa muestra EXACTAMENTE la ruta persistida (misma secuencia, mismos modos).");

  return { costoUsd: costoUsdPlan, projectId, saltosVerificados: nodosSalto.length };
}

// ---------------------------------------------------------------------------
// Fase 2f (Fase 3.3): el bucle completo del checklist contra Supabase real.
// checklist derivado -> PATCH estados -> follow (mensaje compuesto auditable,
// puerta avanzada fuera de lo ya cubierto) -> plan 'seguimiento' -> checklist
// encadenado del plan nuevo.
// ---------------------------------------------------------------------------
const RESPUESTAS_SEGUIMIENTO = [
  "Subí el precio a 250 y las ventas se mantuvieron; ya sé mi costo real por pieza: 130 incluyendo mi hora a 50.",
  "Vendo unas 12 macetas al mes por Instagram, y el proveedor nuevo me baja el cemento un 20%.",
  "Mi duda ahora es si producir por lotes de 10 o seguir por pedido; por pedido no me atraso, pero pierdo el descuento de materiales.",
  "Sí: tengo dos clientes mayoristas interesados que me pidieron precio por docena, todavía no les respondo.",
  "Puedo dedicarle unas 15 horas a la semana; el resto lo cubre mi hermana cuando hay pedidos grandes.",
  "De acuerdo, con eso es suficiente por ahora.",
];

interface ItemVuelo {
  id: string;
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean;
  estado: string;
  nota: string | null;
}

async function faseChecklistSeguimiento(cookie: string, projectId: string) {
  separador("FASE 2f (Fase 3.3): checklist -> PATCH -> follow -> plan seguimiento encadenado");

  // --- 1. el checklist derivado del plan de macetas ---
  const cl1 = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const planes1 = cl1.planes as Array<{ plan_id: string; dominio: string; etapas: Array<{ etapa: number; items: ItemVuelo[] }> }>;
  const resumen1 = cl1.resumen as Record<string, { total: number; hechos: number }>;
  if (planes1.length !== 1) {
    throw new Error(`se esperaba exactamente 1 plan con checklist (el de macetas), hay ${planes1.length}`);
  }
  const items1 = planes1[0].etapas.flatMap((e) => e.items);
  log(`checklist derivado: ${items1.length} items en ${planes1[0].etapas.length} etapa(s), dominio '${planes1[0].dominio}'`);
  if (items1.length < 5) {
    throw new Error(`checklist sospechosamente corto (${items1.length} items) para un plan completo`);
  }
  if (planes1[0].dominio !== "core") {
    throw new Error(`dominio esperado 'core', llego '${planes1[0].dominio}'`);
  }
  for (const etapa of planes1[0].etapas) {
    const destacados = etapa.items.filter((i) => i.destacado);
    if (destacados.length !== 1 || !etapa.items[etapa.items.length - 1].destacado) {
      throw new Error(`etapa ${etapa.etapa}: se esperaba exactamente 1 destacado y al final (hay ${destacados.length})`);
    }
  }
  if (items1.some((i) => i.estado !== "pendiente")) {
    throw new Error("todos los items recien derivados deben nacer 'pendiente'");
  }
  if (resumen1.core?.total !== items1.length || resumen1.core?.hechos !== 0) {
    throw new Error(`resumen inconsistente: ${JSON.stringify(resumen1)} vs ${items1.length} items, 0 hechos`);
  }
  log("OK: estructura del checklist (1 destacado por etapa, al final; todos pendientes; resumen consistente).");

  // --- 2. PATCH: avance real de un toque ---
  const primero = items1[0];
  const rHecho = await patchJson(cookie, `/api/project/${projectId}/checklist`, {
    item_id: primero.id,
    estado: "hecho",
    nota: "quedó lista la tabla de costos por pieza",
  });
  if ((rHecho.item as { estado?: string })?.estado !== "hecho") {
    throw new Error(`PATCH no dejo el item en 'hecho': ${JSON.stringify(rHecho)}`);
  }
  const destacado1 = items1.find((i) => i.destacado)!;
  await patchJson(cookie, `/api/project/${projectId}/checklist`, { item_id: destacado1.id, estado: "a_medias" });
  log(`OK: '${primero.texto.slice(0, 50)}…' -> hecho (con nota); destacado etapa 1 -> a_medias.`);

  // Contrato: estado invalido debe rechazarse con 400 (jamas 23514 en vivo).
  const resInvalido = await fetch(`${BASE_URL}/api/project/${projectId}/checklist`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({ item_id: primero.id, estado: "terminado" }),
  });
  if (resInvalido.status !== 400) {
    throw new Error(`estado invalido 'terminado' debio dar 400, dio ${resInvalido.status}`);
  }
  log("OK: estado fuera de CHECKLIST_ESTADO rechazado con 400.");

  // --- 3. follow: el ritual de 3 tarjetas -> sesion de seguimiento ---
  const { data: nodosAntes } = await supabaseAdmin
    .from("project_nodes")
    .select("node_id")
    .eq("project_id", projectId);
  const cubiertosAntes = new Set((nodosAntes ?? []).map((n: { node_id: string }) => n.node_id));
  log(`nodos cubiertos antes del follow: ${cubiertosAntes.size}`);

  let rf = await postJson(cookie, `/api/project/${projectId}/follow`, {
    detalles: "Conseguí un proveedor de cemento más barato y una feria local en agosto.",
    enfoque: "el precio y el margen",
  });
  const followSessionId = String(rf.session_id);
  log(`follow session_id: ${followSessionId}, tipo primer turno: ${rf.tipo}`);

  const nodosFollow = (rf.nodos_nuevos ?? []) as Array<{ id: string; titulo: string; modo: string }>;
  if (nodosFollow.length === 0) {
    throw new Error("follow no devolvio nodos_nuevos -- el arbol de la UI arrancaria vacio (bug del gate en start, reincidente)");
  }
  const puerta = nodosFollow[0];
  if (cubiertosAntes.has(puerta.id)) {
    throw new Error(
      `la puerta avanzada '${puerta.id}' YA estaba cubierta por sesiones previas -- paridad con modo_seguir rota (visitados = cubiertos ∪ ruta)`
    );
  }
  log(`OK: puerta avanzada '${puerta.titulo}' (${puerta.id}) fuera de lo ya cubierto.`);

  // Bitacora: el mensaje compuesto quedo auditable en sessions.mensaje_entrada.
  const { data: filaFollow, error: errFollow } = await supabaseAdmin
    .from("sessions")
    .select("tipo, mensaje_entrada")
    .eq("id", followSessionId)
    .limit(1)
    .single();
  if (errFollow || !filaFollow) {
    throw new Error(`no se pudo leer la sesion de follow: ${errFollow?.message}`);
  }
  if (filaFollow.tipo !== "seguimiento") {
    throw new Error(`sessions.tipo esperado 'seguimiento', llego '${filaFollow.tipo}'`);
  }
  const mensajeEntrada = String(filaFollow.mensaje_entrada ?? "");
  for (const fragmento of [
    "Desde el último plan, este es mi avance real:",
    "HECHO (1):",
    "(nota: quedó lista la tabla de costos por pieza)",
    "A MEDIAS (1):",
    "Además: Conseguí un proveedor de cemento más barato",
    "Lo que más me interesa profundizar ahora: el precio y el margen",
  ]) {
    if (!mensajeEntrada.includes(fragmento)) {
      throw new Error(`la bitacora (mensaje_entrada) no contiene el fragmento esperado: "${fragmento}"\n---\n${mensajeEntrada}`);
    }
  }
  log("OK: mensaje compuesto auditable en la bitacora (estados, nota, detalles y enfoque presentes).");

  // --- 4. la entrevista de seguimiento hasta el plan ---
  let idxSeg = 0;
  let turnosSeg = 0;
  let costoSeg = Number(rf.costo_usd ?? 0);
  while (rf.tipo === "pregunta" && turnosSeg < MAX_TURNOS_SEGURIDAD) {
    turnosSeg++;
    const respuesta = RESPUESTAS_SEGUIMIENTO[Math.min(idxSeg++, RESPUESTAS_SEGUIMIENTO.length - 1)];
    log(`\n[seguimiento turno ${turnosSeg}] PREGUNTA: ${rf.pregunta}`);
    log(`[seguimiento turno ${turnosSeg}] RESPUESTA: ${respuesta}`);
    rf = await postJson(cookie, `/api/session/${followSessionId}/turn`, { respuesta });
    costoSeg = Number(rf.costo_usd ?? costoSeg);
  }
  if (rf.tipo !== "listo_para_plan") {
    throw new Error(`la sesion de seguimiento no llego a listo_para_plan (tipo final: ${rf.tipo} tras ${turnosSeg} turnos)`);
  }
  log(`\nlisto_para_plan tras ${turnosSeg} turno(s) de seguimiento.`);

  const resPlanSeg = await fetch(`${BASE_URL}/api/session/${followSessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resPlanSeg.ok) {
    throw new Error(`POST plan de seguimiento -> ${resPlanSeg.status}`);
  }
  let markdownSeg = "";
  await consumirSSE(resPlanSeg, ({ evento, data }) => {
    if (evento === "delta") process.stdout.write(".");
    else if (evento === "done") {
      const d = data as { markdown: string; costo_usd: number };
      markdownSeg = d.markdown;
      costoSeg = d.costo_usd;
    } else if (evento === "error") {
      throw new Error(`error SSE en plan de seguimiento: ${JSON.stringify(data)}`);
    }
  });
  process.stdout.write("\n");
  if (!markdownSeg || markdownSeg.length < 100) {
    throw new Error("el plan de seguimiento esta vacio o sospechosamente corto");
  }

  const { data: filaPlanSeg, error: errPlanSeg } = await supabaseAdmin
    .from("plans")
    .select("id, etiqueta")
    .eq("session_id", followSessionId)
    .limit(1)
    .single();
  if (errPlanSeg || !filaPlanSeg) {
    throw new Error(`no se encontro el plan de la sesion de seguimiento: ${errPlanSeg?.message}`);
  }
  if (filaPlanSeg.etiqueta !== "seguimiento") {
    throw new Error(`plans.etiqueta esperada 'seguimiento', llego '${filaPlanSeg.etiqueta}'`);
  }
  log(`OK: plan persistido con etiqueta 'seguimiento' (${filaPlanSeg.id}).`);

  // --- 5. el bucle queda encadenado: el plan nuevo derivo SU checklist ---
  const cl2 = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const planes2 = cl2.planes as Array<{ plan_id: string; etapas: Array<{ items: ItemVuelo[] }> }>;
  const resumen2 = cl2.resumen as Record<string, { total: number; hechos: number }>;
  if (planes2.length !== 2) {
    throw new Error(`tras el plan de seguimiento se esperaban 2 planes con checklist, hay ${planes2.length}`);
  }
  const itemsNuevo = planes2.find((p) => p.plan_id === filaPlanSeg.id)?.etapas.flatMap((e) => e.items) ?? [];
  if (itemsNuevo.length === 0) {
    throw new Error("el plan de seguimiento NO derivo checklist -- el bucle quedo roto");
  }
  if ((resumen2.core?.hechos ?? 0) < 1) {
    throw new Error(`el resumen perdio los hechos previos: ${JSON.stringify(resumen2)}`);
  }
  log(`OK: checklist encadenado (${itemsNuevo.length} items nuevos del plan de seguimiento; hechos previos preservados).`);

  return { costoUsd: costoSeg };
}

// ---------------------------------------------------------------------------
// Fase 2g (Fase 3.5): mundos detras de flags. SIEMPRE verifica el muro
// (sin unlock -> 403) y la idempotencia del unlock. El ciclo positivo
// (start -> turnos -> plan dominio=quality -> checklist del dominio) se
// autodetecta: solo corre si la linea de ensamblaje (integrar_packs.py)
// ya metio nodos de packs al grafo web; antes de eso, start con unlock
// debe responder 503 en palabras de persona.
// ---------------------------------------------------------------------------
async function faseMundos(cookie: string, projectId: string) {
  separador("FASE 2g (Fase 3.5): mundos HSEQ -- el muro, el unlock y el ciclo");

  // El grafo web tiene nodos de packs? (post-linea-de-ensamblaje)
  const grafoRes = await fetch(`${BASE_URL}/api/projects`, { headers: { Cookie: cookie } });
  void grafoRes; // el grafo no se expone por API; se detecta via el 503/200 del start

  // 1. Prueba negativa: sin fila en project_unlocks, /start = 403.
  const sinUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/quality/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (sinUnlock.status !== 403) {
    throw new Error(`start sin unlock debio responder 403 (el muro), respondio ${sinUnlock.status}`);
  }
  log("OK: sin unlock, el mundo no existe (403 con palabras de persona).");

  // 2. Pack inexistente -> 404.
  const packFalso = await fetch(`${BASE_URL}/api/project/${projectId}/world/finanzas/unlock`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (packFalso.status !== 404) {
    throw new Error(`unlock de pack inexistente debio dar 404, dio ${packFalso.status}`);
  }
  log("OK: pack fuera del catalogo rechazado (404).");

  // 3. Unlock real (stub de creditos) + idempotencia.
  const u1 = await postJson(cookie, `/api/project/${projectId}/world/quality/unlock`, {});
  if (u1.ok !== true || u1.dominio !== "quality") {
    throw new Error(`unlock fallo: ${JSON.stringify(u1)}`);
  }
  log(`OK: unlock de quality con ${u1.creditos} creditos (stub).`);
  const u2 = await postJson(cookie, `/api/project/${projectId}/world/quality/unlock`, {});
  if (u2.ya_estaba_activo !== true) {
    throw new Error(`el segundo unlock debio ser idempotente: ${JSON.stringify(u2)}`);
  }
  log("OK: unlock idempotente (23505 absorbido).");

  // Verificar la fila real en Supabase.
  const { data: filaUnlock, error: errUnlock } = await supabaseAdmin
    .from("project_unlocks")
    .select("dominio, creditos_pagados")
    .eq("project_id", projectId)
    .eq("dominio", "quality")
    .single();
  if (errUnlock || !filaUnlock) {
    throw new Error(`no se encontro la fila de project_unlocks: ${errUnlock?.message}`);
  }
  log(`OK: fila persistida (creditos_pagados=${filaUnlock.creditos_pagados}).`);

  // 4. Con unlock: pre-integracion 503; post-integracion, ciclo completo.
  const conUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/quality/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (conUnlock.status === 503) {
    log("OK: mundo activado pero contenido en preparacion (503) -- la linea de");
    log("    ensamblaje (integrar_packs.py) aun no corre; el ciclo positivo de");
    log("    esta fase se completara cuando existan bridges_aprobados x3.");
    return { costoUsd: 0, cicloCompleto: false };
  }
  if (!conUnlock.ok) {
    throw new Error(`start con unlock respondio ${conUnlock.status} (se esperaba 200 o 503 pre-integracion)`);
  }

  // ---- ciclo positivo (grafo ya integrado) ----
  let rw = (await conUnlock.json()) as Record<string, unknown>;
  const worldSessionId = String(rw.session_id);
  let costoW = Number(rw.costo_usd ?? 0);
  log(`world session: ${worldSessionId}, tipo: ${rw.tipo}`);
  let turnosW = 0;
  const RESPUESTAS_MUNDO = [
    "Mis clientes se quejan de piezas con burbujas y acabados irregulares entre lotes.",
    "Reviso cada pieza al final, pero no tengo un registro de que falla ni cuando.",
    "Me interesa un proceso simple para detectar el defecto antes de hornear la pieza.",
    "Con eso me basta por ahora.",
  ];
  while (rw.tipo === "pregunta" && turnosW < MAX_TURNOS_SEGURIDAD) {
    turnosW++;
    const respuesta = RESPUESTAS_MUNDO[Math.min(turnosW - 1, RESPUESTAS_MUNDO.length - 1)];
    log(`[mundo turno ${turnosW}] ${rw.pregunta}`);
    rw = await postJson(cookie, `/api/session/${worldSessionId}/turn`, { respuesta });
    costoW = Number(rw.costo_usd ?? costoW);
  }
  if (rw.tipo !== "listo_para_plan") {
    throw new Error(`la sesion de mundo no llego a listo_para_plan (tipo: ${rw.tipo})`);
  }
  const resPlanW = await fetch(`${BASE_URL}/api/session/${worldSessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  let mdW = "";
  await consumirSSE(resPlanW, ({ evento, data }) => {
    if (evento === "done") {
      const d = data as { markdown: string; costo_usd: number };
      mdW = d.markdown;
      costoW = d.costo_usd;
    }
  });
  if (!mdW) throw new Error("el plan del mundo salio vacio");
  const { data: planW } = await supabaseAdmin
    .from("plans")
    .select("id, etiqueta, dominio")
    .eq("session_id", worldSessionId)
    .single();
  if (planW?.dominio !== "quality") {
    throw new Error(`plans.dominio esperado 'quality', llego '${planW?.dominio}'`);
  }
  const clW = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const resumenW = clW.resumen as Record<string, { total: number }>;
  if (!resumenW.quality || resumenW.quality.total === 0) {
    throw new Error(`el checklist del mundo no aparece agrupado por dominio: ${JSON.stringify(resumenW)}`);
  }
  log(`OK: ciclo completo del mundo (plan dominio=quality, checklist quality con ${resumenW.quality.total} items).`);
  return { costoUsd: costoW, cicloCompleto: true };
}

// ---------------------------------------------------------------------------
// Fase 2g-bis (Fase v1.3.2): los tres mundos nuevos. Murallas negativas de
// exportacion y franquicias (sin unlock -> 403: el dominio no existe para el
// motor) + ciclo positivo COMPLETO de seguridad_digital (unlock -> start con
// semilla del mapeo de brecha -> turnos -> plan dominio=seguridad_digital ->
// checklist agrupado). El unlock de seguridad_digital requiere la migración
// 017 aplicada (CHECK de project_unlocks ampliado): si el CHECK viejo lo
// rechaza, se corta con el mensaje exacto de qué pegar en el SQL Editor.
// ---------------------------------------------------------------------------
async function faseMundosNuevos(cookie: string, projectId: string) {
  separador("FASE 2g-bis (v1.3.2): mundos nuevos -- murallas x2 + ciclo de seguridad_digital");

  // 1. Murallas negativas: sin unlock, exportacion y franquicias = 403.
  for (const dominio of ["exportacion", "franquicias"]) {
    const sinUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/${dominio}/start`, {
      method: "POST",
      headers: { Cookie: cookie },
    });
    if (sinUnlock.status !== 403) {
      throw new Error(`start de '${dominio}' sin unlock debio responder 403 (la muralla), respondio ${sinUnlock.status}`);
    }
    log(`OK: muralla de '${dominio}' en pie (403 sin unlock).`);
  }

  // 2. Unlock de seguridad_digital -- aqui muerde el CHECK de la migracion 017.
  const resUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/seguridad_digital/unlock`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resUnlock.ok) {
    const cuerpo = await resUnlock.text();
    throw new Error(
      `unlock de seguridad_digital respondio ${resUnlock.status} -- si el cuerpo huele a 23514, ` +
        `falta aplicar my_idea_017_mundos_nuevos.sql en el SQL Editor de Supabase (los CHECK de la 016 ` +
        `solo aceptan los packs HSEQ). Cuerpo: ${cuerpo.slice(0, 300)}`
    );
  }
  const u = (await resUnlock.json()) as Record<string, unknown>;
  if (u.ok !== true || u.dominio !== "seguridad_digital") {
    throw new Error(`unlock de seguridad_digital fallo: ${JSON.stringify(u)}`);
  }
  log(`OK: unlock de seguridad_digital con ${u.creditos} creditos (migracion 017 viva).`);

  // 3. Ciclo positivo completo.
  const conUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/seguridad_digital/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!conUnlock.ok) {
    throw new Error(`start de seguridad_digital con unlock respondio ${conUnlock.status} (se esperaba 200 post-integracion)`);
  }
  let rw = (await conUnlock.json()) as Record<string, unknown>;
  const worldSessionId = String(rw.session_id);
  let costoW = Number(rw.costo_usd ?? 0);
  log(`world session: ${worldSessionId}, tipo: ${rw.tipo}`);
  const RESPUESTAS_SEGURIDAD_DIGITAL = [
    "Me preocupan sobre todo las contrasenas y quien puede entrar a mis cuentas, quiero ordenar eso ya. Hoy guardo los datos de mis clientes en un Excel sin clave y en el celular.",
    "Uso la misma contrasena para el correo, Instagram y el banco, y no tengo verificacion en dos pasos.",
    "No tengo copias de seguridad; si pierdo el celular pierdo los pedidos y los contactos.",
    "Me preocupa que me roben la cuenta de Instagram porque es mi canal principal de ventas.",
    "Con eso me basta por ahora.",
  ];
  let turnosW = 0;
  while (rw.tipo === "pregunta" && turnosW < MAX_TURNOS_SEGURIDAD) {
    turnosW++;
    const respuesta = RESPUESTAS_SEGURIDAD_DIGITAL[Math.min(turnosW - 1, RESPUESTAS_SEGURIDAD_DIGITAL.length - 1)];
    log(`[seguridad_digital turno ${turnosW}] ${rw.pregunta}`);
    rw = await postJson(cookie, `/api/session/${worldSessionId}/turn`, { respuesta });
    costoW = Number(rw.costo_usd ?? costoW);
  }
  if (rw.tipo !== "listo_para_plan") {
    throw new Error(`la sesion de seguridad_digital no llego a listo_para_plan (tipo: ${rw.tipo})`);
  }
  const resPlanW = await fetch(`${BASE_URL}/api/session/${worldSessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  let mdW = "";
  await consumirSSE(resPlanW, ({ evento, data }) => {
    if (evento === "done") {
      const d = data as { markdown: string; costo_usd: number };
      mdW = d.markdown;
      costoW = d.costo_usd;
    }
  });
  if (!mdW) throw new Error("el plan de seguridad_digital salio vacio");
  const { data: planW } = await supabaseAdmin
    .from("plans")
    .select("id, etiqueta, dominio")
    .eq("session_id", worldSessionId)
    .single();
  if (planW?.dominio !== "seguridad_digital") {
    throw new Error(`plans.dominio esperado 'seguridad_digital', llego '${planW?.dominio}'`);
  }
  const clW = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const resumenW = clW.resumen as Record<string, { total: number }>;
  if (!resumenW.seguridad_digital || resumenW.seguridad_digital.total === 0) {
    throw new Error(`el checklist de seguridad_digital no aparece agrupado por dominio: ${JSON.stringify(resumenW)}`);
  }
  log(`OK: ciclo completo del mundo nuevo (plan dominio=seguridad_digital, checklist con ${resumenW.seguridad_digital.total} items).`);
  return { costoUsd: costoW };
}

// ---------------------------------------------------------------------------
// Fase 2g-ter (Fase v1.4): el 7.º mundo, "Riesgos Bajo Control". Muralla
// negativa de risk_management (sin unlock -> 403) + ciclo positivo COMPLETO
// (unlock 3 créditos -> start con la semilla del mapeo de brecha -> turnos ->
// plan dominio=risk_management -> checklist agrupado). El unlock muerde el
// CHECK de la migración 019 (project_unlocks ampliado al 7.º pack): si el
// CHECK viejo lo rechaza, se corta con el mensaje exacto para el SQL Editor.
// ---------------------------------------------------------------------------
async function faseMundoRiesgos(cookie: string, projectId: string) {
  separador("FASE 2g-ter (v1.4): Riesgos Bajo Control -- muralla + unlock 3 creditos + ciclo");

  // 1. Muralla negativa: sin unlock, risk_management = 403 (no existe para el motor).
  const sinUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/risk_management/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (sinUnlock.status !== 403) {
    throw new Error(`start de 'risk_management' sin unlock debio responder 403 (la muralla), respondio ${sinUnlock.status}`);
  }
  log("OK: muralla de 'risk_management' en pie (403 sin unlock).");

  // 2. Unlock -- aqui muerde el CHECK de la migracion 019.
  const resUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/risk_management/unlock`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resUnlock.ok) {
    const cuerpo = await resUnlock.text();
    throw new Error(
      `unlock de risk_management respondio ${resUnlock.status} -- si el cuerpo huele a 23514, ` +
        `falta aplicar my_idea_019_mundo_riesgos.sql en el SQL Editor de Supabase (los CHECK de la 017 ` +
        `no aceptan risk_management). Cuerpo: ${cuerpo.slice(0, 300)}`
    );
  }
  const u = (await resUnlock.json()) as Record<string, unknown>;
  if (u.ok !== true || u.dominio !== "risk_management") {
    throw new Error(`unlock de risk_management fallo: ${JSON.stringify(u)}`);
  }
  if (Number(u.creditos) !== 3) {
    throw new Error(`el unlock de risk_management debio cobrar 3 creditos, cobro ${u.creditos}`);
  }
  log(`OK: unlock de risk_management con ${u.creditos} creditos (migracion 019 viva).`);

  // La fila real: creditos_pagados = 3 (canon del catalogo).
  const { data: fila, error: errFila } = await supabaseAdmin
    .from("project_unlocks")
    .select("creditos_pagados")
    .eq("project_id", projectId)
    .eq("dominio", "risk_management")
    .single();
  if (errFila || fila?.creditos_pagados !== 3) {
    throw new Error(`fila de project_unlocks risk_management con creditos_pagados!=3: ${JSON.stringify(fila)} ${errFila?.message ?? ""}`);
  }

  // 3. Ciclo positivo completo -- la brecha elige la semilla del 7.º mundo.
  const conUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/risk_management/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!conUnlock.ok) {
    throw new Error(`start de risk_management con unlock respondio ${conUnlock.status} (se esperaba 200 post-integracion)`);
  }
  let rw = (await conUnlock.json()) as Record<string, unknown>;
  const worldSessionId = String(rw.session_id);
  let costoW = Number(rw.costo_usd ?? 0);
  log(`world session: ${worldSessionId}, tipo: ${rw.tipo}`);
  log(`[risk_management brecha] primera pregunta (semilla del mapeo, cero LLM): ${rw.pregunta}`);
  const RESPUESTAS_RIESGOS = [
    "Mi mayor riesgo es que dependo de un solo proveedor de resina; si sube el precio o desaparece, no puedo producir ni entregar. Quiero aprender a verlo venir a tiempo.",
    "Nunca he escrito una lista de lo que podria salir mal; voy apagando incendios cuando ya pasaron.",
    "No tengo un colchon de dinero ni un proveedor alterno; si algo falla, se me para la produccion entera.",
    "Quiero anticipar los golpes antes de que ocurran y decidir con calma, no a las carreras.",
    "Con eso me basta por ahora.",
  ];
  let turnosW = 0;
  while (rw.tipo === "pregunta" && turnosW < MAX_TURNOS_SEGURIDAD) {
    turnosW++;
    const respuesta = RESPUESTAS_RIESGOS[Math.min(turnosW - 1, RESPUESTAS_RIESGOS.length - 1)];
    log(`[risk_management turno ${turnosW}] ${rw.pregunta}`);
    rw = await postJson(cookie, `/api/session/${worldSessionId}/turn`, { respuesta });
    costoW = Number(rw.costo_usd ?? costoW);
  }
  if (rw.tipo !== "listo_para_plan") {
    throw new Error(`la sesion de risk_management no llego a listo_para_plan (tipo: ${rw.tipo})`);
  }
  const resPlanW = await fetch(`${BASE_URL}/api/session/${worldSessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  let mdW = "";
  await consumirSSE(resPlanW, ({ evento, data }) => {
    if (evento === "done") {
      const d = data as { markdown: string; costo_usd: number };
      mdW = d.markdown;
      costoW = d.costo_usd;
    }
  });
  if (!mdW) throw new Error("el plan de risk_management salio vacio");
  const { data: planW } = await supabaseAdmin
    .from("plans")
    .select("id, etiqueta, dominio")
    .eq("session_id", worldSessionId)
    .single();
  if (planW?.dominio !== "risk_management") {
    throw new Error(`plans.dominio esperado 'risk_management', llego '${planW?.dominio}'`);
  }
  const clW = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const resumenW = clW.resumen as Record<string, { total: number }>;
  if (!resumenW.risk_management || resumenW.risk_management.total === 0) {
    throw new Error(`el checklist de risk_management no aparece agrupado por dominio: ${JSON.stringify(resumenW)}`);
  }
  log(`OK: ciclo completo del 7.o mundo (plan dominio=risk_management, checklist con ${resumenW.risk_management.total} items).`);
  return { costoUsd: costoW };
}

// ---------------------------------------------------------------------------
// Fase 2h (Fase 3.6): el contrato que la UI de convergencia consume.
// GET /api/idea/[id] debe traer lo que las pantallas nuevas pintan:
// unlocks (fila real de project_unlocks), mundos con su plan (post ciclo
// positivo), historial de planes core anteriores (acordeon Historia), y
// el checklist agrupado con el grupo vigente al final (orden cronologico).
// ---------------------------------------------------------------------------
async function faseContratoUI(cookie: string, projectId: string, cicloMundoCompleto: boolean) {
  separador("FASE 2h (Fase 3.6): contrato de la UI -- /api/idea con unlocks, mundos e historial");

  const d = await getJson(cookie, `/api/idea/${projectId}`);

  const unlocks = (d.unlocks ?? []) as string[];
  if (!unlocks.includes("quality")) {
    throw new Error(`/api/idea no reporta el unlock de quality: ${JSON.stringify(unlocks)}`);
  }
  log(`OK: unlocks = ${JSON.stringify(unlocks)} (fila real de project_unlocks).`);

  const historial = (d.historial ?? []) as Array<{ etiqueta: string; created_at: string; contenido_md: string }>;
  if (historial.length < 1) {
    throw new Error("historial vacio: el plan de macetas anterior al de seguimiento debia estar ahi (acordeon Historia)");
  }
  if (!historial.every((h) => h.contenido_md && h.created_at)) {
    throw new Error("entradas de historial sin contenido o fecha");
  }
  log(`OK: historial con ${historial.length} plan(es) core anteriores, releibles.`);

  const plan = d.plan as { etiqueta: string } | null;
  if (plan?.etiqueta !== "seguimiento") {
    throw new Error(`el plan vigente de la vista debia ser el de seguimiento (core), llego '${plan?.etiqueta}'`);
  }
  log("OK: el plan de la vista es el ultimo CORE (los planes de mundos no lo tapan).");

  const mundos = (d.mundos ?? []) as Array<{ dominio: string; plan: { contenido_md: string } | null }>;
  const mundoQuality = mundos.find((m) => m.dominio === "quality");
  if (!mundoQuality) {
    throw new Error("mundos no incluye quality pese al unlock");
  }
  if (cicloMundoCompleto && !mundoQuality.plan?.contenido_md) {
    throw new Error("tras el ciclo positivo, el plan del mundo quality debia venir en mundos[]");
  }
  log(`OK: seccion de mundo quality ${mundoQuality.plan ? "con su plan" : "activa (sin plan aun)"}.`);

  // El grupo vigente de cada dominio debe ser el ULTIMO (orden cronologico).
  const cl = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const planes = cl.planes as Array<{ dominio: string; etapas: Array<{ items: ItemVuelo[] }> }>;
  const gruposCore = planes.filter((p) => p.dominio === "core");
  if (gruposCore.length < 2) {
    throw new Error(`se esperaban >=2 grupos core (macetas + seguimiento), hay ${gruposCore.length}`);
  }
  const vigente = gruposCore.at(-1)!;
  const itemsVigente = vigente.etapas.flatMap((e) => e.items);
  if (itemsVigente.some((i) => i.estado !== "pendiente")) {
    throw new Error("el grupo core VIGENTE (el del plan de seguimiento) debia venir todo pendiente -- el orden cronologico del GET esta roto");
  }
  log("OK: grupo vigente = ultimo cronologico (la pantalla Manos a la Obra pinta el checklist correcto).");

  return { costoUsd: 0 };
}

// ---------------------------------------------------------------------------
// Fase 2i (Fase 3.8): el sentido del tiempo, dos ciclos sobre el proyecto de
// macetas -- cero LLM, cero costo. (a) modo a-mi-ritmo: completed_at real,
// analisis con capa universal SOLA. (b) modo fechas: baseline con fechas
// PASADAS controladas (a tiempo / tardia / adelantada), analisis con capa de
// cumplimiento coherente, realizar -> celebracion, reabrir.
// Requiere la migracion 018 aplicada en Supabase.
// ---------------------------------------------------------------------------
async function faseSentidoDelTiempo(cookie: string, projectId: string) {
  separador("FASE 2i (Fase 3.8): el sentido del tiempo -- modo, timeline real, baseline, analisis, celebracion");

  // Postgres devuelve timestamptz como "...+00:00" (sin milisegundos); es el
  // MISMO instante que el ISO "...Z" que enviamos. Comparar por valor, no por
  // representacion de texto.
  const mismaFecha = (a: unknown, b: string) =>
    typeof a === "string" && new Date(a).getTime() === new Date(b).getTime();

  const grupoVigenteCore = (cl: Record<string, unknown>) => {
    const planes = cl.planes as Array<{ dominio: string; plan_id: string; etapas: Array<{ items: Array<Record<string, unknown>> }> }>;
    return planes.filter((p) => p.dominio === "core").at(-1)!;
  };

  // ---- (a) modo A MI RITMO: solo fechas reales, sin cumplimiento ----
  const rModoRitmo = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "ritmo" });
  if (rModoRitmo.modo_camino !== "ritmo") throw new Error(`/modo no persistio 'ritmo': ${JSON.stringify(rModoRitmo)}`);
  log("OK: modo del camino = 'ritmo' (persistido).");

  const cl0 = await getJson(cookie, `/api/project/${projectId}/checklist`);
  const vig0 = grupoVigenteCore(cl0);
  const items = vig0.etapas.flatMap((e) => e.items) as Array<{ id: string; etapa: number; destacado: boolean }>;
  if (items.length < 3) throw new Error(`el plan vigente necesita >=3 items para el vuelo del tiempo, hay ${items.length}`);

  // completed_at real (pasado) de un toque
  const rHecho = await patchJson(cookie, `/api/project/${projectId}/checklist`, {
    item_id: items[0].id,
    estado: "hecho",
    completed_at: "2026-06-01T12:00:00.000Z",
  });
  if (!mismaFecha((rHecho.item as { completed_at?: string }).completed_at, "2026-06-01T12:00:00.000Z")) {
    throw new Error(`completed_at no se persistio: ${JSON.stringify(rHecho.item)}`);
  }
  log("OK: timeline real -- completed_at pasado persistido (para todos, sin fechas base).");

  const anRitmo = await getJson(cookie, `/api/project/${projectId}/analisis`);
  if (anRitmo.tiene_baseline !== false) throw new Error("a-mi-ritmo NO debe tener capa de cumplimiento");
  const uRitmo = (anRitmo.analytics as { universal: { accionesHechas: number } }).universal;
  if (uRitmo.accionesHechas < 1) throw new Error("la capa universal no conto la accion completada");
  log(`OK: analisis a-mi-ritmo -- capa universal sola (acciones=${uRitmo.accionesHechas}, cumplimiento=null).`);

  // ---- (b) modo FECHAS: baseline con fechas pasadas controladas ----
  const rModoFechas = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "fechas" });
  if (rModoFechas.modo_camino !== "fechas") throw new Error("/modo no persistio 'fechas'");
  log("OK: modo del camino = 'fechas'.");

  // Fechas base PASADAS a proposito, para poder producir las 3 clases de
  // cumplimiento con completed_at tambien pasado (nunca futuro).
  const fechas = [
    { item_id: items[0].id, fecha: "2026-06-01T12:00:00.000Z", origen: "sugerida" }, // completed 06-01 = a tiempo
    { item_id: items[1].id, fecha: "2026-06-05T12:00:00.000Z", origen: "sugerida" }, // completed 06-12 = tardia
    { item_id: items[2].id, fecha: "2026-06-20T12:00:00.000Z", origen: "sugerida" }, // completed 06-12 = adelantada
  ];
  const rBaseline = await postJson(cookie, `/api/project/${projectId}/baseline`, {
    plan_id: vig0.plan_id,
    fechas,
  });
  if (rBaseline.ok !== true) throw new Error(`/baseline no confirmo: ${JSON.stringify(rBaseline)}`);
  log(`OK: linea base sellada (${rBaseline.confirmadas} fechas, baseline_confirmada_at=${rBaseline.baseline_confirmada_at}).`);

  // completed_at de item[1] (tardia: 06-12 > 06-05) y item[2] (adelantada: 06-12 < 06-20)
  await patchJson(cookie, `/api/project/${projectId}/checklist`, {
    item_id: items[1].id,
    estado: "hecho",
    completed_at: "2026-06-12T12:00:00.000Z",
  });
  await patchJson(cookie, `/api/project/${projectId}/checklist`, {
    item_id: items[2].id,
    estado: "hecho",
    completed_at: "2026-06-12T12:00:00.000Z",
  });

  const anFechas = await getJson(cookie, `/api/project/${projectId}/analisis`);
  if (anFechas.tiene_baseline !== true) throw new Error("modo fechas con baseline: la capa de cumplimiento debia existir");
  const c = (anFechas.analytics as { cumplimiento: { aTiempo: number; adelantadas: number; tardias: number; totalConFecha: number } }).cumplimiento;
  // a mano: item0 06-01 vs base 06-01 -> a tiempo; item1 06-12 vs 06-05 (+7) -> tardia; item2 06-12 vs 06-20 (-8) -> adelantada
  if (c.aTiempo < 1 || c.tardias < 1 || c.adelantadas < 1) {
    throw new Error(`las 3 clases de cumplimiento debian aparecer: ${JSON.stringify(c)}`);
  }
  if (c.totalConFecha !== 3) throw new Error(`totalConFecha esperado 3, llego ${c.totalConFecha}`);
  log(`OK: analisis con cumplimiento -- ${c.aTiempo} a tiempo, ${c.adelantadas} adelantadas, ${c.tardias} tardias (calculado de lo persistido).`);

  // ---- realizar -> celebracion -> reabrir ----
  const rReal = await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "realizar" });
  if (!rReal.realizada_at) throw new Error("realizar no sello realizada_at");
  const anCeleb = await getJson(cookie, `/api/project/${projectId}/analisis`);
  const hitos = anCeleb.hitosCelebracion as Array<{ tipo: string }>;
  if (!hitos.some((h) => h.tipo === "realizada")) throw new Error("el timeline de celebracion no incluye el hito 'realizada'");
  if (!hitos.some((h) => h.tipo === "accion")) throw new Error("el timeline de celebracion no incluye hitos de accion");
  log(`OK: realizada -> celebracion (timeline de ${hitos.length} hitos con acciones y REALIZADA).`);

  const rReab = await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "reabrir" });
  if (rReab.realizada_at !== null) throw new Error("reabrir no puso realizada_at a null");
  log("OK: reabrir puso realizada_at a null (la idea vuelve a estar viva).");

  return { costoUsd: 0 };
}

// ---------------------------------------------------------------------------
// Fase 3: reporte digital -- fijos=200, precio=13, variable~0 -> equilibrio
// esperado ceil(200/13)=16. Vocabulario esperado: "usuario(s)"/"suscripcion",
// nunca "pieza".
// ---------------------------------------------------------------------------
async function faseReporteDigital(cookie: string) {
  separador("FASE 3: reporte digital -- equilibrio esperado 16 (ceil(200/13))");
  const textoInicial = "Tengo una app de suscripcion mensual para llevar el registro de gastos personales.";
  const start = await postJson(cookie, "/api/session/start", { texto: textoInicial });
  const projectId = String(start.project_id);
  log(`project_id: ${projectId}`);
  let costoUsd = Number(start.costo_usd ?? 0);

  const RESPUESTAS = [
    "Es una app de suscripcion mensual, cada usuario paga una cuota fija cada mes, no vendo piezas ni nada fisico.",
    "200", // costos_fijos_mensuales
    "0", // costo variable (casi cero, tipico de software)
    "13", // precio_tentativo
    "20", // unidades_vendidas / meta mensual
  ];
  let idx = 0;
  let r = await postJson(cookie, `/api/project/${projectId}/report`, {});
  while (r.tipo === "pregunta") {
    const pregunta = String(r.pregunta);
    const respuesta = RESPUESTAS[Math.min(idx++, RESPUESTAS.length - 1)];
    log(`\nPREGUNTA: ${pregunta}`);
    log(`RESPUESTA: ${respuesta}`);
    r = await postJson(cookie, `/api/project/${projectId}/report`, { respuesta });
    costoUsd = Number(r.costo_usd ?? costoUsd);
  }

  if (r.tipo !== "reporte") {
    throw new Error(`fase 3: se esperaba tipo='reporte', se obtuvo '${r.tipo}'`);
  }
  const contenido = String(r.contenido);
  log("\n--- contenido del reporte ---");
  log(contenido);
  log(`\ncosto_usd: $${Number(r.costo_usd).toFixed(4)}`);

  const menionaDieciseis = /\b16\b/.test(contenido);
  const mencionaPieza = /\bpieza[s]?\b/i.test(contenido);
  log(`\nContiene '16': ${menionaDieciseis}`);
  log(`Contiene 'pieza'/'piezas' (NO deberia): ${mencionaPieza}`);
  if (!menionaDieciseis) {
    throw new Error("fase 3: el reporte NO menciona el equilibrio esperado de 16 unidades/mes");
  }
  if (mencionaPieza) {
    throw new Error("fase 3: el reporte usa vocabulario de 'pieza', incorrecto para una oferta digital");
  }

  separador("FASE 3b (Fase 3.1): verificando que el reporte del 16 no tenga numeros huerfanos");
  const sessionIdReporte = String(r.session_id);
  const { data: filaSesionReporte, error: errorSesionReporte } = await supabaseAdmin
    .from("sessions")
    .select("decisiones")
    .eq("id", sessionIdReporte)
    .limit(1)
    .single();
  if (errorSesionReporte || !filaSesionReporte) {
    throw new Error(`no se encontro la fila de sessions del reporte para verificar huerfanos: ${errorSesionReporte?.message}`);
  }
  const huerfanosReporte = ((filaSesionReporte.decisiones ?? []) as Array<Record<string, unknown>>).filter(
    (d) => d.tipo === "numero_huerfano"
  );
  if (huerfanosReporte.length > 0) {
    throw new Error(
      `el reporte del 16 (nunca deberia inventar cifras) disparo numero_huerfano: ${JSON.stringify(huerfanosReporte)}`
    );
  }
  log("OK: el verificador de numeros huerfanos paso limpio en el reporte del 16 (0 flags).");

  return { costoUsd: Number(r.costo_usd) };
}

// ---------------------------------------------------------------------------
// Fase 4: guardian GIGO -- reproduce el caso real de Motor v2.2 (costo
// mensual leido como costo por pieza, meses leidos como horas): el reporte
// NO debe narrar un margen ni un punto de equilibrio con estos datos.
// ---------------------------------------------------------------------------
async function faseGuardianGigo(cookie: string) {
  separador("FASE 4: guardian GIGO -- numeros contaminados del caso real de Motor v2.2");
  const textoInicial = "Vendo un producto fisico que fabrico yo mismo, una pieza a la vez.";
  const start = await postJson(cookie, "/api/session/start", { texto: textoInicial });
  const projectId = String(start.project_id);
  log(`project_id: ${projectId}`);
  let costoUsd = Number(start.costo_usd ?? 0);

  // Mismos 6 campos esenciales de producto_fisico/servicio, con los
  // valores EXACTOS del caso real que motivo detectarInconsistenciaGigo:
  // costo_materiales_unidad=200 (era presupuesto MENSUAL), horas_por_unidad=4
  // (eran MESES de desarrollo), valor_hora=50, precio_tentativo=13 ->
  // margen = 13 - (200 + 4*50) = 13 - 400 = -387 -> margen_pct = -2976.9%.
  const RESPUESTAS = [
    "Es un producto fisico, lo fabrico yo mismo y lo vendo por pieza.",
    "200", // costo_materiales_unidad (contaminado: era presupuesto mensual)
    "4", // horas_por_unidad (contaminado: eran meses de desarrollo)
    "50", // valor_hora
    "13", // precio_tentativo
    "5", // capacidad_semanal
    "200", // costos_fijos_mensuales
  ];
  let idx = 0;
  let r = await postJson(cookie, `/api/project/${projectId}/report`, {});
  while (r.tipo === "pregunta") {
    const pregunta = String(r.pregunta);
    const respuesta = RESPUESTAS[Math.min(idx++, RESPUESTAS.length - 1)];
    log(`\nPREGUNTA: ${pregunta}`);
    log(`RESPUESTA: ${respuesta}`);
    r = await postJson(cookie, `/api/project/${projectId}/report`, { respuesta });
    costoUsd = Number(r.costo_usd ?? costoUsd);
  }

  if (r.tipo !== "reporte") {
    throw new Error(`fase 4: se esperaba tipo='reporte', se obtuvo '${r.tipo}'`);
  }
  const contenido = String(r.contenido);
  log("\n--- contenido del reporte (debe ser el guardian GIGO, sin narracion) ---");
  log(contenido);
  log(`\ncosto_usd: $${Number(r.costo_usd).toFixed(4)}`);

  const tieneAvisoGigo = contenido.includes("no cuadra en estos números") || contenido.includes("No voy a calcular margen");
  const narraMargenConfiado = /-2976/.test(contenido) === false && /margen.{0,20}-\d{3,}/i.test(contenido);
  log(`\nMuestra el aviso del guardian GIGO: ${tieneAvisoGigo}`);
  if (!tieneAvisoGigo) {
    throw new Error("fase 4: el guardian GIGO NO se activo -- el reporte no muestra el aviso esperado");
  }
  if (narraMargenConfiado) {
    throw new Error("fase 4: el reporte narro un margen absurdo con confianza en vez de abortar");
  }

  return { costoUsd: Number(r.costo_usd) };
}

// ---------------------------------------------------------------------------
// Fase 0 (Fase 3.1): caso sintetico -- ningun API real, solo confirma que
// el verificador de numeros huerfanos SI dispara el flag ante un numero
// inyectado fuera de material, antes de gastar dinero en las fases reales.
// ---------------------------------------------------------------------------
function faseSanidadVerificadorHuerfanos() {
  separador("FASE 0 (Fase 3.1): caso sintetico -- numero inyectado fuera de material");
  const permitidos = new Set([13, 100, 200, 16]);
  const textoContaminado =
    "Tu margen por unidad es de $13 (100%). Con costos fijos de $200/mes, tu punto de equilibrio es de 16 " +
    "unidades/mes. Si escalas, podrias llegar a vender 4500 unidades el proximo trimestre.";
  const eventos: Record<string, unknown>[] = [];
  const huerfanos = verificarNumerosHuerfanos(textoContaminado, permitidos, (e) => eventos.push(e));
  if (huerfanos.length !== 1 || huerfanos[0].valor !== "4500") {
    throw new Error(`el caso sintetico deberia disparar exactamente 1 numero_huerfano (4500), obtuvo: ${JSON.stringify(huerfanos)}`);
  }
  log(`OK: numero inyectado (4500) detectado como huerfano -- contexto: "${huerfanos[0].contexto}"`);
}

async function main() {
  separador("VUELO Fase 3.0.1 -- cerebro web completo vía HTTP real");
  log(`BASE_URL: ${BASE_URL}`);
  log(`Fecha: ${new Date().toISOString()}`);

  faseSanidadVerificadorHuerfanos();

  const cookie = await autenticarComoDevUser();
  log("Autenticado como dev user.");

  const costos: Record<string, number> = {};
  let saltosVerificados = 0;
  try {
    costos.organizer = (await faseOrganizerSonar(cookie)).costoUsd;
    const macetas = await faseSesionMacetas(cookie);
    costos.macetas = macetas.costoUsd;
    saltosVerificados = macetas.saltosVerificados;
    costos.checklistSeguimiento = (await faseChecklistSeguimiento(cookie, macetas.projectId)).costoUsd;
    const mundos = await faseMundos(cookie, macetas.projectId);
    costos.mundos = mundos.costoUsd;
    costos.mundosNuevos = (await faseMundosNuevos(cookie, macetas.projectId)).costoUsd;
    costos.mundoRiesgos = (await faseMundoRiesgos(cookie, macetas.projectId)).costoUsd;
    costos.contratoUI = (await faseContratoUI(cookie, macetas.projectId, mundos.cicloCompleto)).costoUsd;
    costos.sentidoDelTiempo = (await faseSentidoDelTiempo(cookie, macetas.projectId)).costoUsd;
    costos.reporteDigital = (await faseReporteDigital(cookie)).costoUsd;
    costos.guardianGigo = (await faseGuardianGigo(cookie)).costoUsd;
  } catch (e) {
    separador("VUELO FALLIDO");
    log(String(e instanceof Error ? e.stack : e));
    escribirTranscripcion();
    process.exit(1);
  }

  separador("RESUMEN DE COSTOS REALES");
  let total = 0;
  for (const [fase, costo] of Object.entries(costos)) {
    log(`  ${fase}: $${costo.toFixed(4)}`);
    total += costo;
  }
  log(`  TOTAL: $${total.toFixed(4)}`);

  separador("RESUMEN DE VERIFICACIONES");
  log("  0. caso sintetico: verificador de numeros huerfanos dispara el flag: OK");
  log("  1. organizer (capa gratuita): OK");
  log("  2. sesion de macetas + plan streaming: OK");
  log(`  3. salto semantico real persistido sin 23514, con bitacora+score, procedencia valida (Fase 3.1): OK (${saltosVerificados} salto(s))`);
  log("  4. eventos del arbol que piensa == ruta persistida 1:1 (Fase 3.2): OK");
  log("  5. bucle de checklist: derivado -> PATCH -> follow (bitacora+puerta avanzada) -> plan seguimiento encadenado (Fase 3.3): OK");
  log("  6. mundos HSEQ: muro 403 sin unlock, unlock idempotente con creditos, y 503/ciclo segun integracion (Fase 3.5): OK");
  log("  7. mundos nuevos v1.3.2: murallas 403 de exportacion/franquicias + ciclo completo de seguridad_digital (migracion 017): OK");
  log("  7-bis. Riesgos Bajo Control (v1.4): muralla 403 + unlock 3 creditos (migracion 019) + ciclo completo dominio=risk_management: OK");
  log("  8. contrato de la UI de convergencia: unlocks + historial + mundos + grupo vigente (Fase 3.6): OK");
  log("  9. sentido del tiempo (Fase 3.8): modo, completed_at real, baseline con 3 clases de cumplimiento, celebracion+reabrir: OK");
  log("  10. reporte digital (equilibrio esperado 16), sin numeros huerfanos: OK");
  log("  11. guardian GIGO (numeros contaminados): OK");

  separador("VUELO COMPLETO: 13/13 verificaciones OK");
  escribirTranscripcion();
}

function escribirTranscripcion() {
  const outDir = path.join(ROOT, "examples");
  mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "fase3_0_vuelo_web.txt");
  writeFileSync(outPath, lineasTranscripcion.join("\n") + "\n", { encoding: "utf-8" });
  console.log(`\nTranscripcion guardada en ${outPath}`);
}

main();
