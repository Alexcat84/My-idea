/**
 * PRUEBA DE COHERENCIA (construccion 7, decision del fundador, 28 sep 2026). Corre UNA vez, en la CORRIDA FINAL, junto
 * con el vuelo completo y con el fundador midiendo el saldo de la API al inicio y al final. Nunca antes.
 *
 * Tres personas sinteticas (lib/coherencia/nucleo.ts) recorren, cada una en su proyecto nuevo, el nucleo (hasta su
 * plan: sin plan no se abre ningun mundo) y los 10 mundos del catalogo uno tras otro (mundo tras mundo), hasta la
 * oferta del plan del mundo, sin comprarlo. Responde por ellas un actor (Haiku) fiel a su retrato. Al final:
 *  - un juez ciego (Sonnet) lee cada pregunta mostrada, con su base si salio del adaptador, mezclada con las trampas
 *    plantadas de antemano, y la cuenta va contra el umbral del fundador (dictaminar);
 *  - mundo tras mundo: el contexto con que abrio cada mundo trae lo que la persona conto en el anterior;
 *  - el coste de cada sesion (sessions.costo_usd), el ahorro del cache por llamada y lo que gasto el propio arnes.
 *
 * Uso (desde web/, con el .env raiz y VUELO_BASE_URL en el entorno del shell):
 *   npx tsx scripts/coherencia.ts                  # dice lo que haria y cuanto costaria; no gasta nada
 *   npx tsx scripts/coherencia.ts --confirmo-gasto # corre
 * Sale con codigo 1 si no cumple el umbral o si algo falla.
 */
import { createClient } from "@supabase/supabase-js";
import Anthropic from "@anthropic-ai/sdk";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, consumirSSE, postJson, ROOT } from "./_shared/http";
import { costoAcumuladoUsd, llamarClaude, MODEL, MODEL_HAIKU, usoVacio, type RegistroLlamada, type UsoAcumulado } from "../lib/costmeter";
import {
  PERSONAS,
  ahorroCache,
  arrastraLoAnterior,
  construirLote,
  contar,
  dictaminar,
  leerVeredictos,
  pedidoAlJuez,
  sumarMetricas,
  SYSTEM_JUEZ_COHERENCIA,
  systemActor,
  type Metricas,
  type Persona,
  type PreguntaReal,
} from "../lib/coherencia/nucleo";

cargarEnvRaiz();

const MAX_TURNOS_NUCLEO = 16;
const MAX_TURNOS_MUNDO = 12;
/** El coste medido del vuelo del 27 sep 2026 (docs/vuelos/2026-09-28_mundo11): la vara del "antes". */
const ANTES = { turno_interprete_usd: 0.1352039 / 13, sesion_nucleo_con_plan_usd: 0.3024, turnos_nucleo: 13 };

interface Turno {
  espacio: string;
  sesion: string;
  pregunta: string;
  respuesta: string | null;
}

function catalogo(): string[] {
  const c = JSON.parse(readFileSync(path.join(ROOT, "web", "lib", "assets", "packs_catalog.json"), "utf8")) as {
    packs: Array<{ clave: string }>;
  };
  return c.packs.map((p) => p.clave);
}

function precondiciones(): string[] {
  const faltan: string[] = [];
  for (const v of ["ANTHROPIC_API_KEY", "VUELO_DEV_PASSWORD", "SUPABASE_SERVICE_ROLE_KEY", "NEXT_PUBLIC_SUPABASE_URL", "NEXT_PUBLIC_SUPABASE_ANON_KEY"]) {
    if (!process.env[v]?.trim()) faltan.push(`falta ${v} en el entorno`);
  }
  if (!process.env.VUELO_BASE_URL?.trim()) faltan.push("falta VUELO_BASE_URL en el entorno del shell (el .env no basta: se lee al cargar el modulo)");
  const mundos = catalogo();
  if (!mundos.includes("primer_equipo") || mundos.length !== 10) {
    faltan.push(`el catalogo tiene ${mundos.length} mundos (${mundos.join(", ")}): hacen falta los 10, con primer_equipo (puente-forja fundida)`);
  }
  return faltan;
}

async function actor(client: Anthropic, p: Persona, historial: Turno[], pregunta: string, acc: UsoAcumulado) {
  const conversacion = historial
    .filter((t) => t.respuesta)
    .slice(-8)
    .map((t) => `Pregunta: ${t.pregunta}\nTu respuesta: ${t.respuesta}`)
    .join("\n\n");
  const texto = `${conversacion ? `Lo que ya respondiste:\n${conversacion}\n\n` : ""}Nueva pregunta: ${pregunta}`;
  return llamarClaude(client, systemActor(p), texto, MODEL_HAIKU, acc, { maxTokens: 300, componente: "arnes_actor" });
}

async function plan(cookie: string, sessionId: string): Promise<number> {
  const res = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, { method: "POST", headers: { Cookie: cookie } });
  if (!res.ok) throw new Error(`plan ${sessionId} -> ${res.status}`);
  let costo: number | null = null;
  const errores: string[] = [];
  await consumirSSE(res, ({ evento, data }) => {
    if (evento === "done") costo = Number((data as { costo_usd?: number }).costo_usd ?? 0);
    if (evento === "error") errores.push(JSON.stringify(data));
  });
  if (errores.length > 0 || costo === null) throw new Error(`plan ${sessionId}: ${errores.join(" | ") || "sin evento done"}`);
  return costo;
}

/** Conduce una sesion ya abierta hasta la oferta del plan (o su cierre). */
async function conducir(
  cookie: string,
  client: Anthropic,
  p: Persona,
  espacio: string,
  primera: Record<string, unknown>,
  historial: Turno[],
  acc: { uso: UsoAcumulado },
  maxTurnos: number
): Promise<{ sesion: string; fin: string; turnos: Turno[] }> {
  const sesion = String(primera.session_id);
  const turnos: Turno[] = [];
  let r = primera;
  while (r.tipo === "pregunta" && turnos.length < maxTurnos) {
    const pregunta = String(r.pregunta);
    const a = await actor(client, p, [...historial, ...turnos], pregunta, acc.uso);
    acc.uso = a.acumulado;
    const respuesta = a.texto.trim();
    turnos.push({ espacio, sesion, pregunta, respuesta });
    try {
      r = await postJson(cookie, `/api/session/${sesion}/turn`, { respuesta });
    } catch (e) {
      // un 502 error_temporal se reintenta una vez con la misma respuesta
      console.warn(`  [${espacio}] turno fallido, reintento: ${e instanceof Error ? e.message : e}`);
      r = await postJson(cookie, `/api/session/${sesion}/turn`, { respuesta });
    }
  }
  if (r.tipo === "pregunta") turnos.push({ espacio, sesion, pregunta: String(r.pregunta), respuesta: null });
  return { sesion, fin: String(r.tipo), turnos };
}

interface FilaSesion {
  id: string;
  costo_usd: number | null;
  created_at: string;
  estado_recorrido: {
    recorrido?: { contextoProyecto?: string | null; fallbackEvents?: Array<Record<string, unknown>>; dominioSesion?: string };
    acumulado?: { llamadas?: RegistroLlamada[] };
  } | null;
}

async function main() {
  const confirmado = process.argv.includes("--confirmo-gasto");
  const mundos = catalogo();
  console.log("PRUEBA DE COHERENCIA");
  console.log(`  personas: ${PERSONAS.map((p) => p.id).join(", ")}`);
  console.log(`  por persona: nucleo con su plan + ${mundos.length} mundos hasta la oferta del plan (sin comprarlo)`);
  console.log(`  recorridos: ${PERSONAS.length} x ${mundos.length + 1} = ${PERSONAS.length * (mundos.length + 1)}; planes: ${PERSONAS.length} (del nucleo)`);
  console.log(`  contra: ${BASE_URL}`);
  const faltan = precondiciones();
  if (faltan.length > 0) {
    for (const f of faltan) console.error(`  NO: ${f}`);
    process.exit(1);
  }
  if (!confirmado) {
    console.log("\nNo se ha gastado nada. Para correrla: --confirmo-gasto (ver docs/producto/CORRIDA_FINAL.md).");
    process.exit(0);
  }

  const inicio = new Date().toISOString();
  const client = new Anthropic();
  const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  // la memoria (migracion 049) tiene que estar aplicada: sin ella no hay mundo tras mundo que medir
  const { error: sinMemoria } = await admin.from("projects").select("memoria").limit(1);
  if (sinMemoria) throw new Error(`projects.memoria no existe (migracion 049 sin aplicar): ${sinMemoria.message}`);

  const cookie = await autenticarComoDevUser();
  const arnes = { uso: usoVacio() };
  const informe: Record<string, unknown>[] = [];
  const todasMetricas: Metricas[] = [];
  const llamadasApp: RegistroLlamada[] = [];
  const continuidad: Array<{ persona: string; de: string; a: string; arrastra: boolean }> = [];

  for (const p of PERSONAS) {
    console.log(`\n== ${p.id} ==`);
    const historial: Turno[] = [];
    const inicioNucleo = await postJson(cookie, "/api/session/start", { texto: p.idea });
    const projectId = String(inicioNucleo.project_id);
    const nucleo = await conducir(cookie, client, p, "core", inicioNucleo, historial, arnes, MAX_TURNOS_NUCLEO);
    historial.push(...nucleo.turnos);
    if (nucleo.fin !== "listo_para_plan") throw new Error(`${p.id}: el nucleo termino en '${nucleo.fin}', sin plan no hay mundos`);
    await plan(cookie, nucleo.sesion);
    console.log(`  nucleo: ${nucleo.turnos.length} turnos y su plan`);

    const sesionesMundo: Array<{ mundo: string; sesion: string; turnos: Turno[] }> = [];
    for (const mundo of mundos) {
      const primera = await postJson(cookie, `/api/project/${projectId}/world/${mundo}/start`, {});
      const m = await conducir(cookie, client, p, mundo, primera, historial, arnes, MAX_TURNOS_MUNDO);
      historial.push(...m.turnos);
      sesionesMundo.push({ mundo, sesion: m.sesion, turnos: m.turnos });
      console.log(`  ${mundo}: ${m.turnos.length} turnos, fin ${m.fin}`);
    }

    // lo guardado: eventos del adaptador, contexto de apertura, costes y llamadas
    const { data: filas, error } = await admin
      .from("sessions")
      .select("id, costo_usd, created_at, estado_recorrido")
      .eq("project_id", projectId);
    if (error || !filas) throw new Error(`${p.id}: no se pudieron leer las sesiones: ${error?.message}`);
    const porId = new Map((filas as FilaSesion[]).map((f) => [f.id, f]));
    const baseDe = new Map<string, string>();
    for (const f of filas as FilaSesion[]) {
      for (const e of f.estado_recorrido?.recorrido?.fallbackEvents ?? []) {
        if (e.tipo === "adaptacion_pregunta" && typeof e.a === "string" && typeof e.de === "string") baseDe.set(e.a, e.de);
      }
      llamadasApp.push(...(f.estado_recorrido?.acumulado?.llamadas ?? []));
    }

    let anterior: { mundo: string; turnos: Turno[] } | null = null;
    for (const s of sesionesMundo) {
      if (anterior) {
        const ctx = porId.get(s.sesion)?.estado_recorrido?.recorrido?.contextoProyecto ?? null;
        const respuestas = anterior.turnos.map((t) => t.respuesta ?? "").filter(Boolean);
        continuidad.push({ persona: p.id, de: anterior.mundo, a: s.mundo, arrastra: arrastraLoAnterior(ctx, respuestas) });
      }
      anterior = s;
    }

    const reales: PreguntaReal[] = historial.map((t) => ({ sesion: t.sesion, espacio: t.espacio, pregunta: t.pregunta, base: baseDe.get(t.pregunta) ?? null }));
    const { items, clave } = construirLote(p.id, reales);
    const j = await llamarClaude(client, SYSTEM_JUEZ_COHERENCIA, pedidoAlJuez(p, items), MODEL, arnes.uso, {
      maxTokens: 12000,
      componente: "arnes_juez",
    });
    arnes.uso = j.acumulado;
    const veredictos = leerVeredictos(j.texto);
    const metricas = contar(veredictos, clave);
    todasMetricas.push(metricas);
    const sesiones = [nucleo.sesion, ...sesionesMundo.map((s) => s.sesion)].map((id) => ({
      id,
      espacio: id === nucleo.sesion ? "core" : sesionesMundo.find((s) => s.sesion === id)!.mundo,
      turnos: historial.filter((t) => t.sesion === id && t.respuesta).length,
      costo_usd: Number(porId.get(id)?.costo_usd ?? 0),
    }));
    informe.push({ persona: p.id, projectId, metricas, dictamen: dictaminar(metricas), sesiones, items, clave, veredictos, historial });
    console.log(`  juez: ${JSON.stringify(dictaminar(metricas))}`);
  }

  const total = sumarMetricas(todasMetricas);
  const dictamen = dictaminar(total);
  const continuidadOk = continuidad.every((c) => c.arrastra);
  const cache = ahorroCache(llamadasApp);
  const turnosLlamadas = llamadasApp.filter((l) => l.componente === "turnos");
  const fin = new Date().toISOString();
  const resumen = {
    ventana: { inicio, fin },
    dictamen,
    continuidad_mundo_tras_mundo: { ok: continuidadOk, fallos: continuidad.filter((c) => !c.arrastra) },
    metricas: total,
    coste: {
      app_usd: informe.flatMap((i) => i.sesiones as Array<{ costo_usd: number }>).reduce((a, s) => a + s.costo_usd, 0),
      arnes_usd: costoAcumuladoUsd(arnes.uso),
      cache: cache,
      turno_interprete_antes_usd: ANTES.turno_interprete_usd,
      turno_interprete_ahora_usd: turnosLlamadas.length ? turnosLlamadas.reduce((a, l) => a + l.usd, 0) / turnosLlamadas.length : null,
    },
  };

  const dir = path.join(ROOT, "docs", "coherencia", inicio.slice(0, 10));
  mkdirSync(dir, { recursive: true });
  writeFileSync(path.join(dir, "datos.json"), JSON.stringify({ resumen, informe }, null, 1));
  const lineas = [
    `# Prueba de coherencia, ${inicio}`,
    "",
    `**Dictamen:** ${dictamen.cumple && continuidadOk ? "CUMPLE" : "NO CUMPLE"}`,
    ...dictamen.motivos.map((m) => `- ${m}`),
    ...(continuidadOk ? [] : [`- mundo tras mundo: ${continuidad.filter((c) => !c.arrastra).length} apertura(s) sin lo del espacio anterior`]),
    "",
    `Ventana: ${inicio} a ${fin}`,
    "",
    "| Persona | Preguntas | Papel | Contexto | Adaptadas fieles | Trampas |",
    "|---|---|---|---|---|---|",
    ...informe.map((i) => {
      const m = i.metricas as Metricas;
      return `| ${i.persona} | ${m.preguntasReales} | ${m.desajustesPapel} | ${m.desajustesContexto} | ${m.adaptadasFieles} de ${m.adaptadasReales} | ${m.trampasCazadas} de ${m.trampas} |`;
    }),
    "",
    "## Coste",
    "",
    `- Dentro de la app (sessions.costo_usd): ${resumen.coste.app_usd.toFixed(4)} USD`,
    `- El arnes (actor y juez): ${resumen.coste.arnes_usd.toFixed(4)} USD`,
    `- Cache: con cache ${cache.conCache.toFixed(4)} USD, sin cache ${cache.sinCache.toFixed(4)} USD, ahorro ${cache.ahorro.toFixed(4)} USD`,
    `- Turno del interprete: antes ${ANTES.turno_interprete_usd.toFixed(4)} USD, ahora ${resumen.coste.turno_interprete_ahora_usd?.toFixed(4) ?? "sin datos"} USD`,
    "",
    "| Persona | Espacio | Turnos | USD |",
    "|---|---|---|---|",
    ...informe.flatMap((i) => (i.sesiones as Array<{ espacio: string; turnos: number; costo_usd: number }>).map((s) => `| ${i.persona} | ${s.espacio} | ${s.turnos} | ${s.costo_usd.toFixed(4)} |`)),
  ];
  writeFileSync(path.join(dir, "informe.md"), lineas.join("\n") + "\n");
  console.log(`\n${lineas.slice(0, 4).join("\n")}\nInforme: ${dir}`);
  process.exit(dictamen.cumple && continuidadOk ? 0 : 1);
}

main().catch((e) => {
  console.error("LA PRUEBA DE COHERENCIA FALLO:", e);
  process.exit(1);
});
