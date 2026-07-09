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
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, consumirSSE, postJson, ROOT } from "./_shared/http";
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

  function registrarNodosSalto(nodosNuevos: unknown) {
    if (!Array.isArray(nodosNuevos)) return;
    for (const n of nodosNuevos as Array<{ id: string; titulo: string; modo: string }>) {
      if (n.modo === "salto") nodosSalto.push({ id: n.id, titulo: n.titulo });
    }
  }
  // /api/session/start puede hacer multi-hop silencioso ANTES de la
  // primera pregunta (igual que /turn) -- si no se registra aqui, un
  // salto real ocurrido en el arranque nunca se contabiliza.
  registrarNodosSalto(r.nodos_nuevos);

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
    registrarNodosSalto(r.nodos_nuevos);
  }
  registrarNodosSalto(r.nodos_nuevos);

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

  return { costoUsd: costoUsdPlan, projectId, saltosVerificados: nodosSalto.length };
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
  log("  4. reporte digital (equilibrio esperado 16), sin numeros huerfanos: OK");
  log("  5. guardian GIGO (numeros contaminados): OK");

  separador("VUELO COMPLETO: 6/6 verificaciones OK");
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
