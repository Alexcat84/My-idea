/**
 * MEDICION DEL AHORRO EN EL CACHE DEL ANCLAJE DE PROTECCION (decision del fundador, corrida final, 8 oct 2026).
 *
 * "Mide el ahorro con la misma sesion antes y despues": toma una sesion REAL de un mundo de proteccion (la de la prueba
 * de coherencia que mas costo) y repite sus anclajes con SUS entradas (la foto del proyecto, el snapshot y la pregunta
 * de cada turno), con la ficha cambiando en cada turno como paso de verdad, de dos maneras:
 *   ANTES:   la foto y la ficha juntas en el bloque de 1 hora (lo que hacia la app hasta hoy);
 *   DESPUES: la foto en el bloque de 1 hora y la ficha aparte, sin cache (la correccion).
 * Reporta el coste real de cada modo (lo que cobra la API, con su cache) y el ahorro.
 *
 * Uso (desde web/, con el .env raiz):
 *   npx tsx scripts/corrida_final_medir_anclaje.ts <session_id> [turnos=8] --confirmo-gasto
 */
import Anthropic from "@anthropic-ai/sdk";
import { createClient } from "@supabase/supabase-js";
import { cargarEnvRaiz } from "./_shared/http";
import { costoAcumuladoUsd, usoVacio, type UsoAcumulado } from "../lib/costmeter";
import { anclarPregunta } from "../lib/engine/reformuladorProteccion";
import { textoFichaActual, type FichaContexto } from "../lib/engine/memoria";

cargarEnvRaiz();

async function main() {
  const [sesionId, turnosArg] = process.argv.slice(2).filter((a) => !a.startsWith("--"));
  const turnos = Number(turnosArg ?? 8);
  if (!sesionId) throw new Error("uso: <session_id> [turnos] --confirmo-gasto");
  const sb = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, { auth: { persistSession: false } });
  const { data, error } = await sb.from("sessions").select("estado_recorrido").eq("id", sesionId).limit(1);
  if (error || !data?.length) throw new Error(`no encuentro la sesion: ${error?.message}`);
  const rec = (data[0].estado_recorrido as { recorrido?: Record<string, unknown> }).recorrido ?? {};
  const foto = String(rec.contextoProyecto ?? "");
  const snapshot = String(rec.snapshotNucleo ?? "");
  const ficha = (rec.ficha ?? {}) as FichaContexto;
  const preguntas = ((rec.fallbackEvents ?? []) as Array<{ tipo?: string; de?: string }>)
    .filter((e) => e.tipo === "anclaje_proteccion" && e.de)
    .map((e) => String(e.de))
    .slice(0, turnos);
  if (!foto || !snapshot || preguntas.length === 0) throw new Error("la sesion no trae foto, snapshot o anclajes");
  console.log(`sesion ${sesionId}: foto ${foto.length} car., snapshot ${snapshot.length} car., ${preguntas.length} anclajes`);
  if (!process.argv.includes("--confirmo-gasto")) {
    console.log("No se ha gastado nada: pasa --confirmo-gasto.");
    return;
  }
  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  // la ficha de cada turno: la real, con la marca del turno (asi cambia en cada turno como en la sesion de verdad)
  const fichaDe = (k: number) => ({ ...(ficha as object), turno_de_la_sesion: k }) as unknown as FichaContexto;

  const correr = async (modo: "antes" | "despues") => {
    let acc: UsoAcumulado = usoVacio();
    const porLlamada: number[] = [];
    for (const [k, p] of preguntas.entries()) {
      const variable = textoFichaActual(fichaDe(k));
      const antesUsd = costoAcumuladoUsd(acc);
      const contexto = modo === "antes" ? [foto, variable].join("\n\n") : { fijo: foto, variable };
      const r = await anclarPregunta(client, p, snapshot, acc, { presupuestoUsd: 50 }, contexto);
      acc = r.acumulado;
      porLlamada.push(costoAcumuladoUsd(acc) - antesUsd);
    }
    return { total: costoAcumuladoUsd(acc), porLlamada, uso: acc.uso };
  };

  const antes = await correr("antes");
  const despues = await correr("despues");
  const f = (n: number) => `$${n.toFixed(4)}`;
  console.log(`\nANTES   (foto + ficha en el bloque de 1 hora): ${f(antes.total)} | por llamada ${antes.porLlamada.map(f).join(" ")}`);
  console.log(`  uso: ${JSON.stringify(antes.uso)}`);
  console.log(`DESPUES (foto en cache, ficha aparte):          ${f(despues.total)} | por llamada ${despues.porLlamada.map(f).join(" ")}`);
  console.log(`  uso: ${JSON.stringify(despues.uso)}`);
  console.log(`AHORRO: ${f(antes.total - despues.total)} (${(100 * (1 - despues.total / antes.total)).toFixed(1)} %) en ${preguntas.length} anclajes`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
