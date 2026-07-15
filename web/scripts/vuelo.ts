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
// Fase 1b: organizer con una idea REAL larga y multi-dominio (auditor HSEQ).
// Regresion permanente del bug que la sesion de fundador cazo en produccion:
// max_tokens 600 truncaba el JSON del organizador ante una idea rica -> parseo
// roto -> fallo. Los vuelos usaban solo ideas cortas y limpias y nunca lo
// tocaron. Si el tope vuelve a quedar corto, postJson lanza (502) y el vuelo
// cae aqui, antes de que sorprenda a un usuario nuevo.
// ---------------------------------------------------------------------------
const IDEA_LARGA_HSEQ =
  "Quisiera crear un auditor HSEQ virtual, y tambien que sea una app. La idea es crear " +
  "una base de conocimiento con las normas actuales: cada base tendria el contenido " +
  "completo de la norma (ISO 9001 de calidad, ISO 14001 ambiental, ISO 45001 de " +
  "seguridad y salud en el trabajo), mas las explicaciones que recibi durante las clases " +
  "que tome en Bogota. Tengo todo el material para convertirlo en un banco de " +
  "conocimiento. La idea es que un auditor especialista en cualquiera de estas areas, o " +
  "en todas a la vez, pueda usar la herramienta para registrar sus hallazgos en tiempo " +
  "real en la app, y recibir la clausula exacta de lo que aplica, en base al analisis " +
  "interno que la herramienta hace del hallazgo. Ademas quiero que genere el informe de " +
  "auditoria automaticamente, con las no conformidades clasificadas, las observaciones y " +
  "las oportunidades de mejora, para que el auditor no lo redacte desde cero. Mas " +
  "adelante me gustaria que soporte auditorias integradas de los tres sistemas a la vez, " +
  "control de acciones correctivas con fechas y responsables, y un panel para que la " +
  "empresa vea el estado de cierre de cada hallazgo. No se si cobrar por suscripcion a " +
  "las empresas o por auditor, ni cuanto costaria mantener las normas actualizadas.";

async function faseOrganizerIdeaLarga(cookie: string) {
  separador("FASE 1b: organizer con idea larga multi-dominio (regresion tope de tokens)");
  log(`largo del texto: ${IDEA_LARGA_HSEQ.length} chars`);
  const inicio = Date.now();
  const r = await postJson(cookie, "/api/organizer", { texto: IDEA_LARGA_HSEQ });
  log(`project_id: ${r.project_id}`);
  log(`costo_usd: ${r.costo_usd}`);
  log(`tiempo: ${Date.now() - inicio}ms`);
  // El markdown bien formado PRUEBA que el JSON no se trunco ni fallo el parseo.
  if (typeof r.markdown !== "string" || !r.markdown.includes("# Organizador de tu idea")) {
    throw new Error("organizer idea larga: markdown mal formado (posible truncacion por tope)");
  }
  const data = r.data as { idea_en_una_frase?: string; areas_que_cubriria_tu_plan_completo?: string[] } | undefined;
  if (!data?.idea_en_una_frase || !Array.isArray(data.areas_que_cubriria_tu_plan_completo)) {
    throw new Error("organizer idea larga: JSON incompleto (truncado antes de cerrar las listas)");
  }
  log(`OK -- frase: "${String(data.idea_en_una_frase).slice(0, 90)}..."`);
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
// Fase 2j (Fase 4.0): EL BUCLE DE TRACKING SE CIERRA. Lo que ningun test
// unitario puede probar: que el BLOQUE DE REALIDAD (§3) llega de verdad al
// motor y que el plan resultante lo usa SIN regañar (regla 8-bis: es prompt, y
// los prompts solo se prueban volando). DOS ciclos, por adenda del auditor:
//   (1) modo FECHAS con la desviacion ya sembrada por la fase 2i -> el bloque
//       debe traer cumplimiento y el plan debe asumirlo sin reproche;
//   (2) el espejo en modo A MI RITMO -> ni el bloque ni el plan pueden hablar
//       de cumplimiento: no se juzga contra fechas que el usuario no tiene.
// Cierra con el ACTA (§8) completa: cerrar con motivo, verlo en Celebracion,
// Analisis e informe, reabrir, y confirmar que sobrevive en la bitacora.
// ---------------------------------------------------------------------------

/** Frases que el §3 / regla 8-bis PROHIBEN en un plan de seguimiento: el tono
 * es espejo, jamas regaño. Se comparan sin acentos y en minusculas. */
const REGANOS = ["vas tarde", "te atrasaste", "no cumpliste", "deberias haber", "vas retrasado", "incumpliste"];
/** Vocabulario de cumplimiento: prohibido cuando el usuario va "a mi ritmo". */
const VOCES_CUMPLIMIENTO = ["a tiempo", "tardia", "adelantada", "desviacion", "dias tarde"];

const sinAcentos = (s: string) => s.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();

/** El mensaje_entrada de la ULTIMA sesion de seguimiento: lo que el motor
 * recibio DE VERDAD (la bitacora, no nuestra suposicion). */
async function ultimoMensajeSeguimiento(projectId: string): Promise<string> {
  const { data, error } = await supabaseAdmin
    .from("sessions")
    .select("mensaje_entrada, created_at")
    .eq("project_id", projectId)
    .eq("tipo", "seguimiento")
    .order("created_at", { ascending: false })
    .limit(1);
  if (error || !data?.length) throw new Error(`no se encontro la sesion de seguimiento: ${error?.message}`);
  return String((data[0] as { mensaje_entrada: string }).mensaje_entrada ?? "");
}

/** Un ciclo de seguimiento completo, hasta el plan. Devuelve su markdown. */
async function correrCicloSeguimiento(cookie: string, projectId: string, enfoque: string | null) {
  const rf = await postJson(cookie, `/api/project/${projectId}/follow`, {
    detalles: "El proveedor de cemento subio precios a mitad de camino.",
    enfoque,
  });
  const sessionId = String(rf.session_id);
  let r: Record<string, unknown> = rf;
  let turnos = 0;
  while (r.tipo === "pregunta" && turnos < 6) {
    turnos += 1;
    r = await postJson(cookie, `/api/session/${sessionId}/turn`, {
      respuesta: "Con eso te cuento lo importante; arma el plan con lo que ya sabes.",
    });
  }
  let markdown = "";
  const res = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({}),
  });
  await consumirSSE(res, ({ evento, data }) => {
    if (evento === "done") markdown = String((data as { markdown: string }).markdown ?? "");
    if (evento === "error") throw new Error(`el plan de seguimiento fallo: ${JSON.stringify(data)}`);
  });
  if (!markdown) throw new Error("el plan de seguimiento no devolvio markdown");
  return { markdown, costoUsd: Number(r.costo_usd ?? 0) };
}

async function faseBucleTracking(cookie: string, projectId: string) {
  separador("FASE 2j (Fase 4.0): el bucle de tracking -- bloque de realidad, dos ciclos, y el acta");
  let costoUsd = 0;

  // ---- CICLO 1: modo FECHAS, con la desviacion sembrada por la fase 2i ----
  const rModoF = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "fechas" });
  if (rModoF.modo_camino !== "fechas") throw new Error("no se pudo volver a modo fechas");

  const c1 = await correrCicloSeguimiento(cookie, projectId, "Quiero cerrar el costo real por pieza.");
  costoUsd += c1.costoUsd;

  const msg1 = await ultimoMensajeSeguimiento(projectId);
  if (!msg1.includes("Mi realidad medida")) {
    throw new Error("el BLOQUE DE REALIDAD no llego al motor: el mensaje de seguimiento no lo trae");
  }
  for (const senal of ["Ritmo:", "Cumplimiento contra las fechas"]) {
    if (!msg1.includes(senal)) throw new Error(`el bloque de realidad no trae '${senal}' en modo fechas`);
  }
  log("OK: el BLOQUE DE REALIDAD llego al motor con cumplimiento (modo fechas), auditable en la bitacora.");

  const p1 = sinAcentos(c1.markdown);
  const reganos1 = REGANOS.filter((r) => p1.includes(r));
  if (reganos1.length > 0) {
    throw new Error(`el plan de seguimiento REGAÑA (regla 8-bis violada): ${reganos1.join(", ")}`);
  }
  log("OK: el plan de seguimiento asume la desviacion SIN regañar (cero frases prohibidas).");

  // ---- CICLO 2 (espejo): modo A MI RITMO -> cero lenguaje de cumplimiento ----
  const rModoR = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "ritmo" });
  if (rModoR.modo_camino !== "ritmo") throw new Error("no se pudo pasar a modo ritmo");

  const c2 = await correrCicloSeguimiento(cookie, projectId, null);
  costoUsd += c2.costoUsd;

  const msg2 = await ultimoMensajeSeguimiento(projectId);
  if (!msg2.includes("Mi realidad medida")) throw new Error("el bloque de realidad no llego en modo ritmo");
  if (msg2.includes("Cumplimiento contra las fechas")) {
    throw new Error("BLINDAJE ROTO: el bloque habla de cumplimiento en modo 'a mi ritmo' (§3)");
  }
  if (!msg2.includes("a mi ritmo")) throw new Error("el bloque no declara el modo 'a mi ritmo'");
  log("OK: en 'a mi ritmo' el bloque NO menciona cumplimiento (aunque la baseline vieja siga existiendo).");

  const p2 = sinAcentos(c2.markdown);
  const voces = VOCES_CUMPLIMIENTO.filter((v) => p2.includes(v));
  if (voces.length > 0) {
    throw new Error(`el plan a-mi-ritmo habla de cumplimiento (§3 violado): ${voces.join(", ")}`);
  }
  log("OK: el plan del ciclo a-mi-ritmo no juzga contra fechas que el usuario no tiene.");

  // ---- EL ACTA (§8): cerrar al ~75% con motivo, verlo, reabrir, y que sobreviva ----
  // Los dos ciclos de seguimiento dejaron un checklist NUEVO (0 hechas): cerrar
  // ahi probaria el mecanismo pero no el escenario que pidio el auditor. Se
  // siembra ~75% para que el espejo del acta muestre numeros REALES y los
  // pendientes queden como testigos honestos (§8). Cero API: solo PATCH.
  const clActa = (await getJson(cookie, `/api/project/${projectId}/checklist`)) as Record<string, unknown>;
  const planesActa = clActa.planes as Array<{
    dominio: string;
    etapas: Array<{ items: Array<{ id: string; estado: string }> }>;
  }>;
  const itemsActa = planesActa
    .filter((p) => p.dominio === "core")
    .at(-1)!
    .etapas.flatMap((e) => e.items);
  const objetivo75 = Math.round(itemsActa.length * 0.75);
  for (const it of itemsActa.slice(0, objetivo75)) {
    await patchJson(cookie, `/api/project/${projectId}/checklist`, { item_id: it.id, estado: "hecho" });
  }
  const pendientesEsperados = itemsActa.length - objetivo75;
  log(`Sembrado para el acta: ${objetivo75} de ${itemsActa.length} acciones hechas (~75%).`);

  const MOTIVO = "La cierro aqui porque ya valide el precio y el canal; el resto lo decide el mercado.";
  const rReal = await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "realizar", motivo: MOTIVO });
  if (!rReal.realizada_at) throw new Error("realizar no sello realizada_at");
  if (rReal.cierre_motivo !== MOTIVO) throw new Error("realizar no devolvio el motivo");

  const an = await getJson(cookie, `/api/project/${projectId}/analisis`);
  if (an.cierre_motivo !== MOTIVO) throw new Error("el analisis no expone el motivo del cierre");
  const informe = String(an.informe_md ?? "");
  if (!informe.includes("## Acta de cierre")) throw new Error("el informe exportado no trae la seccion 'Acta de cierre'");
  if (!informe.includes(MOTIVO)) throw new Error("el acta del informe no cita el motivo literal del usuario");
  const hitosC = an.hitosCelebracion as Array<{ tipo: string }>;
  if (!hitosC.some((h) => h.tipo === "realizada")) throw new Error("la celebracion no trae el hito realizada");
  const u = (an.analytics as { universal: { accionesVigente: { hechas: number; total: number } } }).universal;
  // El espejo del acta debe reflejar el ~75% REAL, no un cierre vacio.
  if (u.accionesVigente.hechas !== objetivo75 || u.accionesVigente.total !== itemsActa.length) {
    throw new Error(
      `el espejo del acta no refleja lo sembrado: dice ${u.accionesVigente.hechas} de ` +
        `${u.accionesVigente.total}, se esperaba ${objetivo75} de ${itemsActa.length}`
    );
  }
  const pct = Math.round((u.accionesVigente.hechas / u.accionesVigente.total) * 100);
  if (!informe.includes(`**${objetivo75} de ${itemsActa.length}**`)) {
    throw new Error("el informe no trae las acciones al cerrar con los numeros reales");
  }
  // §8: los pendientes al cierre NO se tocan (testigos honestos en la Historia).
  const clTrasCierre = (await getJson(cookie, `/api/project/${projectId}/checklist`)) as Record<string, unknown>;
  const itemsTras = (clTrasCierre.planes as typeof planesActa)
    .filter((p) => p.dominio === "core")
    .at(-1)!
    .etapas.flatMap((e) => e.items);
  const pendientesReales = itemsTras.filter((i) => i.estado !== "hecho").length;
  if (pendientesReales !== pendientesEsperados) {
    throw new Error(
      `el cierre TOCO los pendientes (§8 violado): quedaron ${pendientesReales}, se esperaban ${pendientesEsperados}`
    );
  }
  log(
    `OK: acta de cierre -- cerrado al ${pct}% (${u.accionesVigente.hechas} de ${u.accionesVigente.total}); ` +
      `motivo en analisis + celebracion + informe; los ${pendientesReales} pendientes quedaron intactos.`
  );

  // reabrir NO borra el motivo (la historia no se reescribe)
  const rReab = await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "reabrir" });
  if (rReab.realizada_at !== null) throw new Error("reabrir no puso realizada_at a null");
  const { data: proyRe } = await supabaseAdmin
    .from("projects")
    .select("cierre_motivo")
    .eq("id", projectId)
    .single();
  if ((proyRe as { cierre_motivo: string | null } | null)?.cierre_motivo !== MOTIVO) {
    throw new Error("BORRO EL MOTIVO al reabrir (§8 violado: la historia no se reescribe)");
  }
  const { data: bit } = await supabaseAdmin
    .from("project_bitacora")
    .select("tipo, payload")
    .eq("project_id", projectId)
    .eq("tipo", "realizada");
  const eventos = (bit ?? []) as Array<{ payload: { accion: string; motivo: string | null } }>;
  if (!eventos.some((e) => e.payload?.motivo === MOTIVO)) {
    throw new Error("la bitacora no registro el motivo del cierre");
  }
  if (!eventos.some((e) => e.payload?.accion === "reabrir")) {
    throw new Error("la bitacora no registro el reabrir");
  }
  log(`OK: reabrir NO borro el motivo; la bitacora conserva la secuencia (${eventos.length} eventos 'realizada').`);

  return { costoUsd };
}


// ---------------------------------------------------------------------------
// Fase 2k (Fase 4.1): PARIDAD DE MUNDOS. El escenario que la auditoria
// (docs/AUDITORIA_PARIDAD_MUNDOS.md) dejo sin cubrir, de punta a punta:
//   1. Un mundo activado DESPUES de confirmada la baseline core (health_safety:
//      ningun otro fase lo toca) -- su checklist nace sin fechas.
//   2. Recalcular: sus items entran al MISMO ritual y baseline del proyecto
//      (V3a). Por HTTP se ejercita lo que el ritual hace al aceptar: POST
//      /baseline con los item_id DEL MUNDO.
//   3. Se completan con fechas CONOCIDAS -> cumplimiento deterministico.
//   4. El Analisis los cuenta en su desglose por dominio (V3b), con los
//      conteos calculados A MANO aqui.
//   5. El follow core NO toma sus items, aunque sean los mas recientes (V4):
//      el escenario exacto del hallazgo, que en los vuelos previos no se
//      manifestaba por suerte del orden.
// ---------------------------------------------------------------------------
async function faseParidadMundos(cookie: string, projectId: string) {
  separador("FASE 2k (Fase 4.1): paridad de mundos -- fechas, cumplimiento por dominio y follow limpio");
  let costoUsd = 0;
  const MUNDO = "health_safety";

  // El bucle de tracking (2j) dejo el modo en 'ritmo': se restituye 'fechas',
  // que es el modo donde el cumplimiento existe.
  const rModo = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "fechas" });
  if (rModo.modo_camino !== "fechas") throw new Error("no se pudo restituir el modo 'fechas'");

  // La baseline core viene confirmada de la fase 2i: sin eso, "post-baseline"
  // no significaria nada.
  const anPrevio = await getJson(cookie, `/api/project/${projectId}/analisis`);
  if (!anPrevio.tiene_baseline) throw new Error("la fase 2i debio dejar la baseline core confirmada");
  log("OK: punto de partida -- baseline core confirmada y modo 'fechas'.");

  // ── 1. El mundo, activado AHORA (post-baseline) ──
  const resUnlock = await fetch(`${BASE_URL}/api/project/${projectId}/world/${MUNDO}/unlock`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resUnlock.ok) throw new Error(`unlock de ${MUNDO} respondio ${resUnlock.status}`);
  const resStart = await fetch(`${BASE_URL}/api/project/${projectId}/world/${MUNDO}/start`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resStart.ok) throw new Error(`start de ${MUNDO} respondio ${resStart.status}`);
  let rw = (await resStart.json()) as Record<string, unknown>;
  const sidMundo = String(rw.session_id);
  const RESPUESTAS: string[] = [
    "Trabajo con cemento y polvo todo el dia, sin mascarilla ni guantes decentes; se que algun dia me va a pasar factura.",
    "Nunca he escrito que puede lastimarme ni he preparado nada para una emergencia.",
    "Quiero proteger mi salud sin frenar la produccion.",
    "Con eso me basta por ahora.",
  ];
  let t = 0;
  while (rw.tipo === "pregunta" && t < MAX_TURNOS_SEGURIDAD) {
    rw = await postJson(cookie, `/api/session/${sidMundo}/turn`, {
      respuesta: RESPUESTAS[Math.min(t, RESPUESTAS.length - 1)],
    });
    t += 1;
  }
  const resPlanW = await fetch(`${BASE_URL}/api/session/${sidMundo}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({}),
  });
  await consumirSSE(resPlanW, ({ evento, data }) => {
    if (evento === "done") costoUsd = Number((data as { costo_usd?: number }).costo_usd ?? 0);
    if (evento === "error") throw new Error(`el plan de ${MUNDO} fallo: ${JSON.stringify(data)}`);
  });
  log(`OK: '${MUNDO}' activado y explorado DESPUES de la baseline core.`);

  // ── 2. Su checklist nace SIN fechas (el hueco que V3a cierra) ──
  const cl = (await getJson(cookie, `/api/project/${projectId}/checklist`)) as Record<string, unknown>;
  type Grupo = { dominio: string; plan_id: string; etapas: Array<{ items: Array<Record<string, unknown>> }> };
  const grupos = cl.planes as Grupo[];
  const gMundo = grupos.filter((g) => g.dominio === MUNDO).at(-1);
  if (!gMundo) throw new Error(`el mundo ${MUNDO} no dejo checklist`);
  const itemsMundo = gMundo.etapas.flatMap((e) => e.items);
  if (itemsMundo.length < 4) throw new Error(`el mundo dejo solo ${itemsMundo.length} items: muy pocos para el escenario`);
  if (itemsMundo.some((i) => i.fecha_base)) throw new Error("los items del mundo nacieron con fecha: imposible");
  const gCore = grupos.filter((g) => g.dominio === "core").at(-1)!;
  log(`OK: los ${itemsMundo.length} items de '${MUNDO}' nacen SIN fecha base (post-baseline).`);

  // ── 3. Recalcular: los items del MUNDO entran al ritual del proyecto (V3a) ──
  // Fechas base CONOCIDAS, en el pasado, para que el cumplimiento sea exacto.
  const dia = (offset: number) => new Date(Date.now() + offset * 86_400_000).toISOString();
  const BASES = [dia(-20), dia(-20), dia(-10)]; // 3 items fechados; el resto sin tocar
  const aFechar = itemsMundo.slice(0, 3);
  const rBase = await postJson(cookie, `/api/project/${projectId}/baseline`, {
    plan_id: gCore.plan_id, // la baseline es DEL PROYECTO; el plan del mundo no se sella
    fechas: aFechar.map((it, k) => ({ item_id: it.id as string, fecha: BASES[k], origen: "sugerida" })),
  });
  if (!rBase || (rBase as { error?: string }).error) throw new Error(`/baseline rechazo los items de mundo: ${JSON.stringify(rBase)}`);

  const cl2 = (await getJson(cookie, `/api/project/${projectId}/checklist`)) as Record<string, unknown>;
  const itemsMundo2 = (cl2.planes as Grupo[]).filter((g) => g.dominio === MUNDO).at(-1)!.etapas.flatMap((e) => e.items);
  const conFecha = itemsMundo2.filter((i) => i.fecha_base);
  if (conFecha.length !== 3) throw new Error(`se fecharon ${conFecha.length} items de mundo, se esperaban 3 (V3a roto)`);
  log("OK: los items del MUNDO reciben fecha base por el ritual del proyecto (V3a).");

  // ── 4. Completarlos con fechas conocidas -> cumplimiento deterministico ──
  // A MANO: base -20d, hecho -20d -> dif 0  -> A TIEMPO
  //         base -20d, hecho -12d -> dif +8 -> TARDIA
  //         base -10d, hecho -15d -> dif -5 -> ADELANTADA
  const REALES = [dia(-20), dia(-12), dia(-15)];
  for (const [k, it] of aFechar.entries()) {
    await patchJson(cookie, `/api/project/${projectId}/checklist`, {
      item_id: it.id as string,
      estado: "hecho",
      completed_at: REALES[k],
    });
  }
  log("OK: 3 items del mundo completados con fechas conocidas (1 a tiempo, 1 tardia, 1 adelantada).");

  // ── 5. El Analisis los cuenta en su desglose por dominio (V3b) ──
  const an = (await getJson(cookie, `/api/project/${projectId}/analisis`)) as Record<string, unknown>;
  const cumpl = (an.analytics as { cumplimiento: { porDominio: Array<Record<string, number | string>> } | null }).cumplimiento;
  if (!cumpl) throw new Error("el analisis perdio la capa de cumplimiento");
  const delMundo = cumpl.porDominio.find((d) => d.dominio === MUNDO);
  if (!delMundo) throw new Error(`el desglose por dominio NO incluye '${MUNDO}' (V3b roto): ${JSON.stringify(cumpl.porDominio)}`);
  if (delMundo.aTiempo !== 1 || delMundo.tardias !== 1 || delMundo.adelantadas !== 1 || delMundo.total !== 3) {
    throw new Error(
      `conteos del mundo != calculo a mano (1/1/1 de 3): ${JSON.stringify(delMundo)}`
    );
  }
  const delCore = cumpl.porDominio.find((d) => d.dominio === "core");
  if (!delCore) throw new Error("el desglose perdio el core");
  if (cumpl.porDominio[0].dominio !== "core") throw new Error("el core debe ir primero en el desglose");
  log(`OK: Analisis con desglose por dominio -- ${MUNDO}: ${delMundo.aTiempo} a tiempo, ${delMundo.adelantadas} adelantadas, ${delMundo.tardias} tardias (conteos a mano); core aparte con ${delCore.total}.`);

  // ── 6. El follow core NO toma los items del mundo (V4) ──
  // Los del mundo son AHORA los mas recientes del proyecto: el escenario exacto
  // del hallazgo. Antes de 4.1, el follow habria compuesto con ellos.
  const textosMundo = itemsMundo2.map((i) => String(i.texto));
  const rf = await postJson(cookie, `/api/project/${projectId}/follow`, {
    detalles: "Sigo con lo mio.",
    enfoque: null,
  });
  costoUsd += Number(rf.costo_usd ?? 0);
  const { data: sesF } = await supabaseAdmin
    .from("sessions")
    .select("mensaje_entrada")
    .eq("id", String(rf.session_id))
    .single();
  const mensaje = String((sesF as { mensaje_entrada: string }).mensaje_entrada ?? "");
  const colados = textosMundo.filter((tx) => tx.length > 25 && mensaje.includes(tx));
  if (colados.length > 0) {
    throw new Error(
      `V4 ROTO: el follow core compuso con ${colados.length} item(s) del mundo '${MUNDO}': "${colados[0].slice(0, 60)}…"`
    );
  }
  const itemsCoreVig = gCore.etapas.flatMap((e) => e.items).map((i) => String(i.texto));
  if (!itemsCoreVig.some((tx) => tx.length > 25 && mensaje.includes(tx))) {
    throw new Error("el follow core no compuso con NINGUN item core: la seleccion quedo vacia");
  }
  log("OK: el follow core compone con items CORE aunque los del mundo sean los mas recientes (V4).");

  return { costoUsd };
}

// ---------------------------------------------------------------------------
// Fase 3: reporte digital -- fijos=200, precio=13, variable~0 -> equilibrio
// esperado ceil(200/13)=16. Vocabulario esperado: "usuario(s)"/"suscripcion",
// nunca "pieza".
// ---------------------------------------------------------------------------
/** El mensaje_entrada de la ultima sesion de seguimiento DE UN DOMINIO: lo que
 * el motor recibio de verdad para ESE subproyecto (la bitacora, no nuestra
 * suposicion). Fase 4.2: ya no hay un solo follow, hay uno por mundo activo. */
async function ultimoMensajeSeguimientoDe(projectId: string, dominio: string): Promise<string> {
  const { data, error } = await supabaseAdmin
    .from("sessions")
    .select("mensaje_entrada, created_at")
    .eq("project_id", projectId)
    .eq("tipo", "seguimiento")
    .eq("dominio", dominio)
    .order("created_at", { ascending: false })
    .limit(1);
  if (error || !data?.length) {
    throw new Error(`no se encontro sesion de seguimiento de dominio '${dominio}': ${error?.message}`);
  }
  return String((data[0] as { mensaje_entrada: string }).mensaje_entrada ?? "");
}

type GrupoChecklist = {
  dominio: string;
  plan_id: string;
  etapas: Array<{ items: Array<Record<string, unknown>> }>;
};

async function gruposChecklist(cookie: string, projectId: string): Promise<GrupoChecklist[]> {
  const cl = (await getJson(cookie, `/api/project/${projectId}/checklist`)) as Record<string, unknown>;
  return cl.planes as GrupoChecklist[];
}

const grupoVigenteDe = (grupos: GrupoChecklist[], dominio: string) =>
  grupos.filter((g) => g.dominio === dominio).at(-1);

// ---------------------------------------------------------------------------
// Fase 2L (Fase 4.2): EL MUNDO COMO SUBPROYECTO COMPLETO. La 4.1 le dio al
// mundo fechas y cumplimiento; le faltaba lo que hace de un tramo un
// subproyecto: seguimiento propio y un final propio.
//
//   1. Desviacion sembrada en SUS items -> su follow recibe SU cumplimiento y
//      NO el del core (la regla que el bloque de mundo existe para cumplir).
//   2. Su plan nuevo la asume sin regañar (regla 8-bis), y regenera SOLO el
//      plan del mundo: el plan core no se toca.
//   3. Cierre del mundo al ~70% con motivo -> chip, bitacora, timeline de la
//      Celebracion y desglose del Analisis, con los conteos calculados A MANO.
//   4. Reabrir preserva el motivo (la historia no se reescribe).
//   5. §3 jerarquia honesta: completar mundos -- TODOS -- no cierra la idea.
//
// El espejo de la 4.1 (el follow CORE no toma items de mundo) sigue verde en la
// fase 2k, que corre justo antes sobre este mismo proyecto y con los items del
// mundo siendo los mas recientes: el escenario exacto del hallazgo V4.
// ---------------------------------------------------------------------------
async function faseMundoSubproyecto(cookie: string, projectId: string) {
  separador("FASE 2L (Fase 4.2): el mundo como subproyecto -- su seguimiento, su cumplimiento y su cierre");
  let costoUsd = 0;
  const MUNDO = "health_safety";
  const NOMBRE = "Seguridad y Personas";
  const dia = (offset: number) => new Date(Date.now() + offset * 86_400_000).toISOString();

  // El cumplimiento solo existe en modo fechas; la 2k lo dejo asi.
  const rModo = await patchJson(cookie, `/api/project/${projectId}/modo`, { modo_camino: "fechas" });
  if (rModo.modo_camino !== "fechas") throw new Error("no se pudo restituir el modo 'fechas'");

  // ── 1. Desviacion sembrada en los items DEL MUNDO ──
  // La 2k dejo 3 items del mundo fechados y hechos: dif 0, +8, -5.
  // Aqui se anaden 2 tardias GRANDES, con textos propios del mundo:
  //   base -30d, hecho -18d -> +12 (tardia)
  //   base -30d, hecho -21d ->  +9 (tardia)
  // A MANO, el mundo queda: 1 a tiempo, 1 adelantada, 3 tardias (total 5);
  // desviacion media = (0 + 8 - 5 + 12 + 9) / 5 = 24/5 = +4.8 dias.
  const gruposPrevios = await gruposChecklist(cookie, projectId);
  const gMundoPrevio = grupoVigenteDe(gruposPrevios, MUNDO);
  if (!gMundoPrevio) throw new Error(`la fase 2k debio dejar checklist de '${MUNDO}'`);
  const gCorePrevio = grupoVigenteDe(gruposPrevios, "core")!;
  const itemsMundo = gMundoPrevio.etapas.flatMap((e) => e.items);
  const yaFechados = itemsMundo.filter((i) => i.fecha_base);
  if (yaFechados.length !== 3) {
    throw new Error(`se esperaban los 3 items fechados por la 2k, hay ${yaFechados.length}`);
  }
  const nuevos = itemsMundo.filter((i) => !i.fecha_base).slice(0, 2);
  if (nuevos.length !== 2) throw new Error("el mundo no tiene 2 items libres para sembrar la desviacion");
  await postJson(cookie, `/api/project/${projectId}/baseline`, {
    plan_id: gCorePrevio.plan_id, // la baseline es DEL PROYECTO; el plan del mundo no se sella
    fechas: nuevos.map((it) => ({ item_id: it.id as string, fecha: dia(-30), origen: "sugerida" })),
  });
  const REALES = [dia(-18), dia(-21)];
  for (const [k, it] of nuevos.entries()) {
    await patchJson(cookie, `/api/project/${projectId}/checklist`, {
      item_id: it.id as string,
      estado: "hecho",
      completed_at: REALES[k],
    });
  }
  const textosTardiosMundo = nuevos.map((i) => String(i.texto));
  log(`OK: desviacion sembrada en los items de '${MUNDO}' -- a mano queda 1 a tiempo, 1 adelantada, 3 tardias (de 5).`);

  // El cumplimiento CORE, para poder probar que NO se cuela en el mundo.
  const anPrevio = (await getJson(cookie, `/api/project/${projectId}/analisis`)) as Record<string, unknown>;
  const cumplCore = (anPrevio.analytics as {
    cumplimiento: { tardiasTop: Array<{ texto: string }>; porDominio: Array<Record<string, unknown>> } | null;
  }).cumplimiento;
  if (!cumplCore) throw new Error("el analisis perdio la capa de cumplimiento");
  const delMundoPrevio = cumplCore.porDominio.find((d) => d.dominio === MUNDO);
  if (
    !delMundoPrevio ||
    delMundoPrevio.aTiempo !== 1 ||
    delMundoPrevio.adelantadas !== 1 ||
    delMundoPrevio.tardias !== 3 ||
    delMundoPrevio.total !== 5
  ) {
    throw new Error(
      `el desglose del mundo != calculo a mano (1 a tiempo / 1 adelantada / 3 tardias de 5): ${JSON.stringify(delMundoPrevio)}`
    );
  }
  if (delMundoPrevio.desviacionMediaDias !== 4.8) {
    throw new Error(`la desviacion media del mundo != 4.8 calculado a mano: ${delMundoPrevio.desviacionMediaDias}`);
  }
  log("OK: el Analisis cuenta el cumplimiento del mundo con los conteos a mano (1/1/3 de 5, +4.8 dias).");

  // ── 2. SU follow: su cumplimiento, jamas el del core ──
  const rf = await postJson(cookie, `/api/project/${projectId}/follow`, {
    detalles: "Compre las mascarillas pero el polvo sigue igual de bravo.",
    enfoque: null,
    dominio: MUNDO,
  });
  costoUsd += Number(rf.costo_usd ?? 0);
  const sidFollow = String(rf.session_id);

  const msg = await ultimoMensajeSeguimientoDe(projectId, MUNDO);
  if (!msg.includes(`Mi realidad medida en «${NOMBRE}»`)) {
    throw new Error(`el bloque del mundo no se presenta como suyo: ${msg.slice(0, 200)}`);
  }
  if (!msg.includes("1 a tiempo, 1 adelantadas, 3 tardías (de 5 con fecha)")) {
    throw new Error(`el bloque no lleva el cumplimiento DEL MUNDO calculado a mano: ${msg}`);
  }
  if (!msg.includes("desviación media de +4.8 días")) {
    throw new Error("el bloque no lleva la desviacion media del mundo (+4.8)");
  }
  // La regla que este bloque existe para cumplir: NUNCA las tardanzas del core.
  const coreColado = cumplCore.tardiasTop
    .map((t) => t.texto)
    .filter((tx) => tx.length > 25 && msg.includes(tx));
  if (coreColado.length > 0) {
    throw new Error(
      `el bloque del mundo lleva tardias del CORE como si fueran suyas: "${coreColado[0].slice(0, 60)}…"`
    );
  }
  // Y sus propias tardias SI, con nombre y apellido.
  if (!textosTardiosMundo.some((tx) => msg.includes(tx.slice(0, 40)))) {
    throw new Error("el bloque no dice DONDE se atora el usuario en este mundo");
  }
  // UNA sola linea del proyecto, y rotulada.
  const lineasContexto = msg.split("\n").filter((l) => l.includes("Contexto de mi proyecto"));
  if (lineasContexto.length !== 1) {
    throw new Error(`el bloque del mundo debe traer UNA linea de contexto global, trae ${lineasContexto.length}`);
  }
  if (!lineasContexto[0].includes("NO de este mundo")) {
    throw new Error("la linea de contexto no se rotula como del proyecto y no del mundo");
  }
  log("OK: el follow del MUNDO recibe SU cumplimiento (1/1/3, +4.8) y NO el del core; una sola linea de contexto.");

  // Sus items, no los del core: el espejo de V4 en la otra direccion.
  const textosCore = gCorePrevio.etapas.flatMap((e) => e.items).map((i) => String(i.texto));
  const coreEnMensaje = textosCore.filter((tx) => tx.length > 25 && msg.includes(tx));
  if (coreEnMensaje.length > 0) {
    throw new Error(`el follow del mundo compuso con items CORE: "${coreEnMensaje[0].slice(0, 60)}…"`);
  }
  if (!itemsMundo.map((i) => String(i.texto)).some((tx) => tx.length > 25 && msg.includes(tx))) {
    throw new Error("el follow del mundo no compuso con NINGUN item suyo: la seleccion quedo vacia");
  }
  log("OK: compone con SUS items; ni uno del core se cuela (el espejo del hallazgo V4).");

  // ── 3. Su plan nuevo: asume la desviacion sin regañar, y es SOLO suyo ──
  let r: Record<string, unknown> = rf;
  let turnos = 0;
  while (r.tipo === "pregunta" && turnos < MAX_TURNOS_SEGURIDAD) {
    turnos += 1;
    r = await postJson(cookie, `/api/session/${sidFollow}/turn`, {
      respuesta: "Con eso te cuento lo importante; arma el plan con lo que ya sabes.",
    });
  }
  let markdown = "";
  const resPlan = await fetch(`${BASE_URL}/api/session/${sidFollow}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({}),
  });
  await consumirSSE(resPlan, ({ evento, data }) => {
    if (evento === "done") {
      markdown = String((data as { markdown: string }).markdown ?? "");
      costoUsd += Number((data as { costo_usd?: number }).costo_usd ?? 0);
    }
    if (evento === "error") throw new Error(`el plan del mundo fallo: ${JSON.stringify(data)}`);
  });
  const reganos = REGANOS.filter((x) => sinAcentos(markdown).includes(x));
  if (reganos.length > 0) {
    throw new Error(`el plan del mundo REGAÑA (regla 8-bis violada): ${reganos.join(", ")}`);
  }
  log("OK: el plan nuevo del mundo asume su desviacion SIN regañar (regla 8-bis).");

  const gruposTras = await gruposChecklist(cookie, projectId);
  const gMundoNuevo = grupoVigenteDe(gruposTras, MUNDO)!;
  if (gMundoNuevo.plan_id === gMundoPrevio.plan_id) {
    throw new Error("el follow del mundo no genero un ciclo nuevo: su plan vigente no cambio");
  }
  const gCoreTras = grupoVigenteDe(gruposTras, "core")!;
  if (gCoreTras.plan_id !== gCorePrevio.plan_id) {
    throw new Error("el follow del MUNDO regenero tambien el plan CORE: debia regenerar SOLO el suyo");
  }
  const otrosMundos = ["quality", "seguridad_digital", "risk_management"];
  for (const otro of otrosMundos) {
    const antes = grupoVigenteDe(gruposPrevios, otro);
    const despues = grupoVigenteDe(gruposTras, otro);
    if (antes && despues && antes.plan_id !== despues.plan_id) {
      throw new Error(`el follow de '${MUNDO}' toco el plan de '${otro}'`);
    }
  }
  log("OK: regenero SOLO el plan del mundo (checklist encadenado en su grupo); core y los otros mundos, intactos.");

  // ── 4. El cierre del mundo al ~70%, con motivo ──
  const itemsNuevos = gMundoNuevo.etapas.flatMap((e) => e.items);
  const objetivo70 = Math.round(itemsNuevos.length * 0.7);
  for (const it of itemsNuevos.slice(0, objetivo70)) {
    await patchJson(cookie, `/api/project/${projectId}/checklist`, { item_id: it.id as string, estado: "hecho" });
  }
  const pendientesEsperados = itemsNuevos.length - objetivo70;
  const MOTIVO_MUNDO = "Ya tengo el equipo y el protocolo escrito; el resto lo hare cuando contrate a alguien.";
  const rCerrar = await postJson(cookie, `/api/project/${projectId}/world/${MUNDO}/completar`, {
    accion: "completar",
    motivo: MOTIVO_MUNDO,
  });
  if (!rCerrar.completado_at) throw new Error("completar no sello completado_at");
  if (rCerrar.cierre_motivo !== MOTIVO_MUNDO) throw new Error("completar no devolvio el motivo");
  log(`Sembrado para el cierre: ${objetivo70} de ${itemsNuevos.length} acciones del mundo (~70%).`);

  // El chip: /api/idea es lo que la UI lee de verdad.
  const detalle = (await getJson(cookie, `/api/idea/${projectId}`)) as Record<string, unknown>;
  const mundoUI = (detalle.mundos as Array<{ dominio: string; completado_at: string | null; cierre_motivo: string | null }>)
    .find((m) => m.dominio === MUNDO);
  if (!mundoUI?.completado_at) throw new Error("la UI no ve el mundo como completado (no hay chip)");
  if (mundoUI.cierre_motivo !== MOTIVO_MUNDO) throw new Error("la UI no recibe el motivo del cierre del mundo");

  // Los pendientes del mundo, intactos: testigos, no basura.
  const itemsTrasCierre = grupoVigenteDe(await gruposChecklist(cookie, projectId), MUNDO)!.etapas.flatMap((e) => e.items);
  const pendientesReales = itemsTrasCierre.filter((i) => i.estado !== "hecho").length;
  if (pendientesReales !== pendientesEsperados) {
    throw new Error(
      `el cierre del mundo TOCO sus pendientes: quedaron ${pendientesReales}, se esperaban ${pendientesEsperados}`
    );
  }

  // La bitacora del proyecto.
  const { data: bitM } = await supabaseAdmin
    .from("project_bitacora")
    .select("tipo, payload")
    .eq("project_id", projectId)
    .eq("tipo", "mundo_completado");
  const eventosM = (bitM ?? []) as Array<{ payload: { mundo: string; accion: string; motivo: string | null } }>;
  if (!eventosM.some((e) => e.payload?.mundo === MUNDO && e.payload?.motivo === MOTIVO_MUNDO)) {
    throw new Error("la bitacora no registro el cierre del mundo con su motivo");
  }

  // El timeline de la Celebracion del proyecto y el desglose del Analisis.
  const an = (await getJson(cookie, `/api/project/${projectId}/analisis`)) as Record<string, unknown>;
  const hitos = an.hitosCelebracion as Array<{ tipo: string; dominio?: string; subtitulo?: string }>;
  const hitoCierre = hitos.find((h) => h.tipo === "mundo_completado" && h.dominio === MUNDO);
  if (!hitoCierre) throw new Error("el timeline de la Celebracion no trae el hito del mundo completado");
  if (hitoCierre.subtitulo !== MOTIVO_MUNDO) throw new Error("el hito del cierre perdio el motivo discreto");
  const iActivado = hitos.findIndex((h) => h.tipo === "mundo" && h.dominio === MUNDO);
  const iCerrado = hitos.findIndex((h) => h.tipo === "mundo_completado" && h.dominio === MUNDO);
  if (iActivado === -1 || iCerrado < iActivado) throw new Error("el hito del cierre no va despues del de su activacion");
  const mundosAn = (an.analytics as { mundos: Array<{ dominio: string; completadoAt: string | null }> }).mundos;
  if (!mundosAn.find((m) => m.dominio === MUNDO)?.completadoAt) {
    throw new Error("el Analisis no refleja el mundo como completado en su desglose");
  }
  log(
    `OK: cierre del mundo al ${Math.round((objetivo70 / itemsNuevos.length) * 100)}% -- chip en la UI, motivo en bitacora, ` +
      `hito en el timeline y desglose del Analisis; sus ${pendientesReales} pendientes intactos.`
  );

  // ── 5. §3 JERARQUIA HONESTA: ni un mundo ni TODOS cierran la idea ──
  const { data: proyTrasMundo } = await supabaseAdmin
    .from("projects")
    .select("realizada_at")
    .eq("id", projectId)
    .single();
  if ((proyTrasMundo as { realizada_at: string | null } | null)?.realizada_at) {
    throw new Error("§3 VIOLADO: completar un mundo cerro la idea");
  }
  for (const otro of otrosMundos) {
    await postJson(cookie, `/api/project/${projectId}/world/${otro}/completar`, { accion: "completar" });
  }
  const { data: proyTrasTodos } = await supabaseAdmin
    .from("projects")
    .select("realizada_at")
    .eq("id", projectId)
    .single();
  if ((proyTrasTodos as { realizada_at: string | null } | null)?.realizada_at) {
    throw new Error("§3 VIOLADO: completar TODOS los mundos cerro la idea sola");
  }
  log("OK: §3 -- ni un mundo ni TODOS los mundos cierran la idea: el cierre del proyecto es un acto aparte.");

  // Un mundo cerrado no se replanifica a ciegas: se reabre primero (409).
  const resCerrado = await fetch(`${BASE_URL}/api/project/${projectId}/follow`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({ dominio: MUNDO, detalles: "algo mas" }),
  });
  if (resCerrado.status !== 409) {
    throw new Error(`el follow de un mundo COMPLETADO respondio ${resCerrado.status}, se esperaba 409`);
  }
  log("OK: el follow de un mundo completado responde 409 (reabrelo primero), sin gastar un arranque.");

  // El acta del proyecto DICE como quedaron los mundos (§3), sin esconder nada.
  const rReal = await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "realizar", motivo: null });
  if (!rReal.realizada_at) throw new Error("no se pudo cerrar el proyecto para leer su acta");
  const anActa = (await getJson(cookie, `/api/project/${projectId}/analisis`)) as Record<string, unknown>;
  const informe = String(anActa.informe_md ?? "");
  if (!informe.includes(`- ${NOMBRE}:`)) {
    throw new Error(`el acta del proyecto no dice como quedo '${NOMBRE}': ${informe.slice(0, 400)}`);
  }
  if (!informe.includes(`${NOMBRE}: **${objetivo70} de ${itemsNuevos.length}**`)) {
    throw new Error("el acta no trae el avance REAL del mundo al cerrar");
  }
  if (!/completado el \d{4}-\d{2}-\d{2}/.test(informe)) {
    throw new Error("el acta no dice que el mundo quedo completado, con su fecha");
  }
  if (informe.includes(MUNDO)) throw new Error("el acta nombra el mundo por su clave tecnica");
  log(`OK: el acta del proyecto dice como quedo cada mundo ("${NOMBRE}: ${objetivo70} de ${itemsNuevos.length}, completado").`);
  await postJson(cookie, `/api/project/${projectId}/realizar`, { accion: "reabrir" });

  // ── 6. Reabrir el mundo NO borra su motivo ──
  const rReabrir = await postJson(cookie, `/api/project/${projectId}/world/${MUNDO}/completar`, { accion: "reabrir" });
  if (rReabrir.completado_at !== null) throw new Error("reabrir el mundo no puso completado_at a null");
  if (rReabrir.cierre_motivo !== MOTIVO_MUNDO) throw new Error("reabrir devolvio el motivo cambiado");
  const { data: unlockRe } = await supabaseAdmin
    .from("project_unlocks")
    .select("completado_at, cierre_motivo")
    .eq("project_id", projectId)
    .eq("dominio", MUNDO)
    .single();
  const fila = unlockRe as { completado_at: string | null; cierre_motivo: string | null } | null;
  if (fila?.completado_at !== null) throw new Error("reabrir no persistio completado_at = null");
  if (fila?.cierre_motivo !== MOTIVO_MUNDO) {
    throw new Error("BORRO EL MOTIVO al reabrir el mundo (la historia no se reescribe)");
  }
  log("OK: reabrir el mundo NO borro su motivo; la bitacora conserva la secuencia completa.");

  return { costoUsd };
}

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
    costos.organizerIdeaLarga = (await faseOrganizerIdeaLarga(cookie)).costoUsd;
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
    costos.bucleTracking = (await faseBucleTracking(cookie, macetas.projectId)).costoUsd;
    costos.paridadMundos = (await faseParidadMundos(cookie, macetas.projectId)).costoUsd;
    costos.mundoSubproyecto = (await faseMundoSubproyecto(cookie, macetas.projectId)).costoUsd;
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
  log("  1b. organizer idea larga multi-dominio (regresion tope de tokens 600->1500): OK");
  log("  2. sesion de macetas + plan streaming: OK");
  log("  2j. bucle de tracking (Fase 4.0): bloque de realidad al motor en DOS ciclos (fechas con desviacion / a-mi-ritmo sin cumplimiento), plan sin regaño, acta de cierre completa y motivo que sobrevive al reabrir: OK");
  log("  2L. el mundo como subproyecto (Fase 4.2): su follow recibe SU cumplimiento (1/1/3 de 5, +4.8 dias) y NO el del core, con UNA linea de contexto rotulada; su plan nuevo asume la desviacion sin regañar y regenera SOLO el suyo; cierre al 70% con motivo -> chip, bitacora, hito en el timeline y desglose; ni un mundo ni TODOS cierran la idea (§3); reabrir preserva el motivo: OK");
  log("  2k. paridad de mundos (Fase 4.1): mundo activado POST-baseline recibe fechas por el ritual del proyecto (V3a), su cumplimiento aparece en el desglose por dominio del Analisis con conteos a mano (V3b), y el follow core NO toma sus items aunque sean los mas recientes (V4): OK");
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

  separador("VUELO COMPLETO: 14/14 verificaciones OK");
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
