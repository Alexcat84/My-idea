// scripts/spike_estimacion.ts — FASE 0 del Scheduler Inteligente: el SPIKE de
// estimación. La PUERTA de toda la campaña.
//
// Toma ~36 tareas REALES del grafo (concepto + pasos_accionables +
// entregable_esperado), variadas entre dominios/fases; el modelo del motor
// clasifica cada una en banda S/M/L/XL + espera_externa, 3 veces; mide la
// concordancia INTER-CORRIDA y saca un reporte .md con la MATRIZ DE DISCORDANTES
// para el juicio del fundador (PM certificado = estándar de oro).
//
// PUERTA: >80% exacta-o-adyacente → abre F1. Menos → iterar el prompt (abajo) o
// degradar a 3 bandas y re-medir. NO toca producción: solo lee el grafo (asset
// local) y llama al LLM. NO escribe en Supabase.
//
// Uso:  npx tsx scripts/spike_estimacion.ts   (necesita ANTHROPIC_API_KEY)
// Costo real esperado: <$1 (≈108 llamadas cortas con el system cacheado).
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { createAnthropicClient } from "../lib/anthropicClient";
import { costoAcumuladoUsd, llamarClaude, MODEL, usoVacio, type UsoAcumulado } from "../lib/costmeter";
import { cargarGrafo, type Grafo, type NodoGrafo } from "../lib/engine/graph";

cargarEnvRaiz();

const BANDAS = ["S", "M", "L", "XL"] as const;
type Banda = (typeof BANDAS)[number];
const idxBanda = (b: Banda) => BANDAS.indexOf(b);

const CORRIDAS = 3;
const OBJETIVO_TAREAS = 36; // 30-40, variadas

// El prompt del spike. Si la puerta no abre, ESTA es la palanca (o degradar a 3
// bandas fusionando L+XL). Bandas por RANGOS, JAMÁS horas numéricas.
const SYSTEM = [
  "Eres un estimador de esfuerzo para un plan de negocio de una persona sola.",
  "Clasificas UNA tarea en una BANDA de esfuerzo, con RANGOS honestos, JAMÁS un",
  "número de horas.",
  "",
  "Bandas (elige EXACTAMENTE una):",
  "- S: cabe en una sentada de una hora o menos.",
  "- M: dos a cuatro horas.",
  "- L: una jornada completa de trabajo.",
  "- XL: varios días de trabajo.",
  "",
  "Además: ¿la tarea DEPENDE de terceros y por eso arrastra tiempo de ESPERA",
  "(aunque el esfuerzo propio sea poco)? Ejemplo: 'envía correos y espera",
  "respuestas' es poco esfuerzo pero tiene espera externa. Devuelve espera_externa.",
  "",
  "Responde SOLO un objeto JSON, sin una palabra más, con esta forma EXACTA:",
  '{"banda":"S","espera_externa":false}',
  "PROHIBIDO devolver horas numéricas o cualquier texto fuera del JSON.",
].join("\n");

function tareaUserText(n: NodoGrafo): string {
  const pasos = (n.pasos_accionables ?? []).map((p) => `- ${p}`).join("\n");
  return [
    `Tarea: ${n.titulo_concepto}`,
    `Pasos accionables:\n${pasos || "- (sin pasos)"}`,
    `Entregable esperado: ${n.entregable_esperado ?? ""}`,
  ].join("\n\n");
}

/** Selección VARIADA y determinista: nodos con pasos+entregable, ordenados por
 * (dominio, fase, id) y tomados a paso constante para cubrir dominios y fases
 * (no un bloque contiguo de un solo mundo). */
function seleccionarTareas(grafo: Grafo): NodoGrafo[] {
  const validos = Object.values(grafo)
    .filter((n) => (n.pasos_accionables?.length ?? 0) > 0 && (n.entregable_esperado?.trim() ?? "") !== "")
    .sort((a, b) =>
      `${a.dominio ?? "core"}|${a.fase_proyecto}|${a.node_id}`.localeCompare(
        `${b.dominio ?? "core"}|${b.fase_proyecto}|${b.node_id}`
      )
    );
  if (validos.length <= OBJETIVO_TAREAS) return validos;
  const paso = validos.length / OBJETIVO_TAREAS;
  const out: NodoGrafo[] = [];
  for (let i = 0; i < OBJETIVO_TAREAS; i += 1) out.push(validos[Math.floor(i * paso)]);
  return out;
}

interface Corrida {
  banda: Banda | null;
  espera: boolean | null;
}

function parsear(texto: string): Corrida {
  const m = texto.match(/\{[\s\S]*\}/);
  if (!m) return { banda: null, espera: null };
  try {
    const o = JSON.parse(m[0]) as { banda?: string; espera_externa?: boolean };
    const banda = (BANDAS as readonly string[]).includes(o.banda ?? "") ? (o.banda as Banda) : null;
    const espera = typeof o.espera_externa === "boolean" ? o.espera_externa : null;
    return { banda, espera };
  } catch {
    return { banda: null, espera: null };
  }
}

async function main() {
  const client = createAnthropicClient();
  let acumulado: UsoAcumulado = usoVacio();
  const tareas = seleccionarTareas(cargarGrafo());
  console.log(`Spike de estimación: ${tareas.length} tareas × ${CORRIDAS} corridas (modelo ${MODEL}).`);

  const filas: Array<{ tarea: NodoGrafo; corridas: Corrida[]; clase: string; esperaConcorde: boolean }> = [];
  for (const [i, t] of tareas.entries()) {
    const corridas: Corrida[] = [];
    for (let c = 0; c < CORRIDAS; c += 1) {
      const r = await llamarClaude(client, SYSTEM, tareaUserText(t), MODEL, acumulado, {
        maxTokens: 60,
        componente: "spike_estimacion",
        presupuestoUsd: 5,
      });
      acumulado = r.acumulado;
      corridas.push(parsear(r.texto));
    }
    const bandas = corridas.map((c) => c.banda).filter((b): b is Banda => b !== null);
    let clase: string;
    if (bandas.length < CORRIDAS) {
      clase = "inválida"; // el modelo no devolvió JSON/banda parseable en alguna corrida
    } else {
      const idxs = bandas.map(idxBanda);
      const rango = Math.max(...idxs) - Math.min(...idxs);
      clase = rango === 0 ? "exacta" : rango === 1 ? "adyacente" : "discordante";
    }
    const esperas = corridas.map((c) => c.espera);
    const esperaConcorde = esperas.every((e) => e !== null && e === esperas[0]);
    filas.push({ tarea: t, corridas, clase, esperaConcorde });
    console.log(`  [${i + 1}/${tareas.length}] ${t.titulo_concepto.slice(0, 46).padEnd(46)} → ${bandas.join("/") || "?"} (${clase})`);
  }

  const n = filas.length;
  const cuenta = (cl: string) => filas.filter((f) => f.clase === cl).length;
  const exacta = cuenta("exacta");
  const adyacente = cuenta("adyacente");
  const discordante = cuenta("discordante");
  const invalida = cuenta("inválida");
  const pctExactaOAdy = n ? ((exacta + adyacente) / n) * 100 : 0;
  const esperaOk = filas.filter((f) => f.esperaConcorde).length;
  const costo = costoAcumuladoUsd(acumulado);
  const puerta = pctExactaOAdy > 80;

  const pct = (x: number) => ((x / n) * 100).toFixed(1);
  const L: string[] = [];
  L.push("# Spike de estimación — Fase 0 del Scheduler Inteligente");
  L.push("");
  L.push(`Modelo: \`${MODEL}\` · ${n} tareas × ${CORRIDAS} corridas · costo real: **$${costo.toFixed(4)}**`);
  L.push("");
  L.push("## Concordancia inter-corrida");
  L.push(`- **Exacta** (las 3 corridas, misma banda): ${exacta}/${n} (${pct(exacta)}%)`);
  L.push(`- **Adyacente** (a lo sumo 1 banda de distancia): ${adyacente}/${n} (${pct(adyacente)}%)`);
  L.push(`- **Discordante** (2+ bandas de distancia): ${discordante}/${n} (${pct(discordante)}%)`);
  if (invalida) L.push(`- **Inválida** (el modelo no devolvió JSON parseable en alguna corrida): ${invalida}/${n}`);
  L.push(`- **espera_externa concorde** (las 3 corridas iguales): ${esperaOk}/${n} (${pct(esperaOk)}%)`);
  L.push("");
  L.push(
    `## PUERTA — exacta-o-adyacente = **${pctExactaOAdy.toFixed(1)}%** → ${
      puerta ? "✅ **ABRE F1** (>80%)" : "❌ **NO abre** (<80%): iterar el prompt del spike o degradar a 3 bandas (fusionar L+XL) y re-medir"
    }`
  );
  L.push("");
  L.push("## Matriz de DISCORDANTES (para el juicio del fundador — PM certificado = estándar de oro)");
  L.push("");
  const problematicas = filas.filter((f) => f.clase === "discordante" || f.clase === "inválida");
  if (problematicas.length === 0) {
    L.push("_Ninguna: todas cayeron en exacta o adyacente._");
  } else {
    L.push("| Tarea | Dominio / Fase | Corrida 1 | Corrida 2 | Corrida 3 |");
    L.push("|---|---|---|---|---|");
    for (const f of problematicas) {
      const b = f.corridas.map((c) => c.banda ?? "?");
      L.push(
        `| ${f.tarea.titulo_concepto.replace(/\|/g, "/")} | ${f.tarea.dominio ?? "core"} / ${f.tarea.fase_proyecto} | ${b[0]} | ${b[1]} | ${b[2]} |`
      );
    }
  }
  L.push("");
  L.push("## Todas las tareas (referencia)");
  L.push("");
  L.push("| Tarea | Dominio | Bandas (3 corridas) | Clase | Espera concorde |");
  L.push("|---|---|---|---|---|");
  for (const f of filas) {
    const b = f.corridas.map((c) => c.banda ?? "?").join("/");
    L.push(
      `| ${f.tarea.titulo_concepto.replace(/\|/g, "/")} | ${f.tarea.dominio ?? "core"} | ${b} | ${f.clase} | ${f.esperaConcorde ? "sí" : "no"} |`
    );
  }

  const outDir = path.join(ROOT, "web", "examples");
  mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "spike_estimacion.md");
  writeFileSync(outPath, L.join("\n") + "\n", { encoding: "utf-8" });

  console.log("");
  console.log(`Reporte: ${outPath}`);
  console.log(`Exacta-o-adyacente: ${pctExactaOAdy.toFixed(1)}%  ·  espera concorde: ${pct(esperaOk)}%  ·  costo: $${costo.toFixed(4)}`);
  console.log(puerta ? "PUERTA ✅ ABRE F1 (>80%)" : "PUERTA ❌ NO abre (<80%): itera el prompt o degrada a 3 bandas");
}

main().catch((e) => {
  console.error(e instanceof Error ? e.stack : e);
  process.exit(1);
});
