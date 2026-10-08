/**
 * RE-VALIDACIÓN DEL ESTIMADOR DE BANDAS ANTES DE CAMBIARLE EL MODELO (decisión del fundador, corrida final, 8 oct
 * 2026): SYSTEM_ESTIMACION_BANDA no cambia de modelo sin re-validarse con los casos de su validación original y sin el
 * visto del fundador.
 *
 * Los casos originales: las 36 tareas del spike de la Fase 0 (web/examples/spike_estimacion_items.md, Sonnet 4.6,
 * 97,2 % exacta-o-adyacente). Se recuperan del grafo de hoy por su texto (el reporte las guarda recortadas a 70
 * caracteres); las que ya no se encuentran se reportan, no se inventan.
 *
 * Se mide con el camino de PRODUCCIÓN (SYSTEM_ESTIMACION_BANDA, el lote entero en una llamada, 3 corridas, la
 * mayoría-de-3 de estimacion.ts) y con dos modelos: el de hoy (control) y el candidato. Tres varas:
 *  1. la PUERTA original: concordancia entre las 3 corridas, exacta-o-adyacente > 80 %;
 *  2. el acuerdo de la mayoría de cada modelo con la banda que dio el spike original (exacta-o-adyacente);
 *  3. el acuerdo entre el candidato y el control de hoy, tarea por tarea.
 *
 * Uso (desde web/, con el .env raíz):  npx tsx scripts/revalidar_estimador.ts --candidato claude-sonnet-5-5
 * Escribe docs/corrida_final/<fecha>/revalidacion_estimador.md. Gasta API (6 llamadas de lote).
 */
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { createAnthropicClient } from "../lib/anthropicClient";
import { costoAcumuladoUsd, llamarClaude, MODEL_ESTIMACION, usoVacio, type UsoAcumulado } from "../lib/costmeter";
import { cargarGrafo } from "../lib/engine/graph";
import { construirUserText, parsearLote, votoMayoriaBanda } from "../lib/engine/estimacion";
import { SYSTEM_ESTIMACION_BANDA } from "../lib/prompts";
import type { Banda } from "../lib/dbContract";

cargarEnvRaiz();

const BANDAS: Banda[] = ["S", "M", "L", "XL"];
const idx = (b: Banda) => BANDAS.indexOf(b);
const CORRIDAS = 3;

function arg(nombre: string): string | null {
  const i = process.argv.indexOf(nombre);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
}

interface CasoOriginal {
  label: string;
  dominio: string;
  bandas: Banda[];
  moda: Banda;
}

/** Las filas de "Todas las unidades" del reporte original. */
function casosOriginales(): CasoOriginal[] {
  const md = readFileSync(path.join(ROOT, "web", "examples", "spike_estimacion_items.md"), "utf8");
  const tabla = md.slice(md.indexOf("## Todas las unidades"));
  const out: CasoOriginal[] = [];
  for (const linea of tabla.split("\n")) {
    const c = linea.split("|").map((x) => x.trim());
    if (c.length < 6 || !/^[SMLX]+(\/[SMLX]+){2}$/.test(c[3] ?? "")) continue;
    const bandas = c[3].split("/") as Banda[];
    out.push({ label: c[1], dominio: c[2], bandas, moda: votoMayoriaBanda(bandas)! });
  }
  return out;
}

/** El texto completo de cada caso en el grafo de hoy (todos los nodos, también los deprecados). */
function recuperar(casos: CasoOriginal[]): Array<CasoOriginal & { texto: string | null }> {
  const grafo = cargarGrafo();
  const pasos: string[] = [];
  for (const n of Object.values(grafo)) for (const p of n.pasos_accionables ?? []) pasos.push(p);
  return casos.map((c) => {
    const prefijo = c.label.replace(/…$/, "").trim();
    const exacto = pasos.find((p) => p === c.label);
    const porPrefijo = exacto ?? pasos.find((p) => p.startsWith(prefijo));
    return { ...c, texto: porPrefijo ?? null };
  });
}

async function corridas(modelo: string, textos: string[], acc: UsoAcumulado) {
  const client = createAnthropicClient();
  const userText = construirUserText(textos.map((t) => ({ texto: t })));
  const maxTokens = Math.min(4000, 200 + textos.length * 40);
  const votos: (Banda | null)[][] = textos.map(() => []);
  const esperas: (boolean | null)[][] = textos.map(() => []);
  for (let r = 0; r < CORRIDAS; r += 1) {
    const res = await llamarClaude(client, SYSTEM_ESTIMACION_BANDA, userText, modelo, acc, {
      maxTokens,
      componente: `revalidacion_${modelo}`,
      presupuestoUsd: 5,
    });
    acc = res.acumulado;
    const lote = parsearLote(res.texto);
    textos.forEach((_, i) => {
      const v = lote.find((x) => x.id === i);
      votos[i].push(v?.banda ?? null);
      esperas[i].push(v?.espera ?? null);
    });
  }
  return { votos, esperas, acc };
}

function concordancia(bandas: (Banda | null)[]): "exacta" | "adyacente" | "discordante" | "inválida" {
  if (bandas.some((b) => b === null)) return "inválida";
  const i = (bandas as Banda[]).map(idx);
  const rango = Math.max(...i) - Math.min(...i);
  return rango === 0 ? "exacta" : rango === 1 ? "adyacente" : "discordante";
}
const cerca = (a: Banda | null, b: Banda | null) => a !== null && b !== null && Math.abs(idx(a) - idx(b)) <= 1;

async function main() {
  const candidato = arg("--candidato");
  if (!candidato) throw new Error("falta --candidato <modelo>");
  const control = MODEL_ESTIMACION;
  const casos = recuperar(casosOriginales());
  const vivos = casos.filter((c) => c.texto !== null);
  console.log(`Casos originales: ${casos.length}; recuperados en el grafo de hoy: ${vivos.length}.`);
  let acc = usoVacio();
  const textos = vivos.map((c) => c.texto as string);
  const ctl = await corridas(control, textos, acc);
  acc = ctl.acc;
  const cnd = await corridas(candidato, textos, acc);
  acc = cnd.acc;

  const filas = vivos.map((c, i) => {
    const mCtl = votoMayoriaBanda(ctl.votos[i].filter((b): b is Banda => b !== null));
    const mCnd = votoMayoriaBanda(cnd.votos[i].filter((b): b is Banda => b !== null));
    return {
      c,
      ctl: ctl.votos[i],
      cnd: cnd.votos[i],
      mCtl,
      mCnd,
      concCtl: concordancia(ctl.votos[i]),
      concCnd: concordancia(cnd.votos[i]),
      esperaCnd: cnd.esperas[i].every((e) => e !== null && e === cnd.esperas[i][0]),
    };
  });
  const n = filas.length;
  const pct = (x: number) => `${x}/${n} (${((x / n) * 100).toFixed(1)} %)`;
  const puerta = (k: "concCtl" | "concCnd") => filas.filter((f) => f[k] === "exacta" || f[k] === "adyacente").length;
  const vsOriginal = (k: "mCtl" | "mCnd") => filas.filter((f) => cerca(f[k], f.c.moda)).length;
  const exactaOriginal = (k: "mCtl" | "mCnd") => filas.filter((f) => f[k] === f.c.moda).length;
  const cndVsCtl = filas.filter((f) => cerca(f.mCnd, f.mCtl)).length;
  const cndIgualCtl = filas.filter((f) => f.mCnd === f.mCtl).length;
  const pasaPuerta = puerta("concCnd") / n > 0.8;

  const L: string[] = [];
  L.push("# Re-validación del estimador de bandas antes de cambiarle el modelo");
  L.push("");
  L.push(`Fecha: ${new Date().toISOString()} · casos originales ${casos.length}, recuperados ${n} · coste real: $${costoAcumuladoUsd(acc).toFixed(4)}`);
  L.push("");
  L.push(`Camino de producción: SYSTEM_ESTIMACION_BANDA, el lote entero en una llamada, ${CORRIDAS} corridas por modelo.`);
  L.push(`Control: \`${control}\` (el de hoy). Candidato: \`${candidato}\`.`);
  L.push("");
  L.push("| Vara | Control | Candidato |");
  L.push("|---|---|---|");
  L.push(`| Puerta original: concordancia entre corridas, exacta-o-adyacente (> 80 %) | ${pct(puerta("concCtl"))} | ${pct(puerta("concCnd"))} |`);
  L.push(`| Mayoría igual a la banda del spike original | ${pct(exactaOriginal("mCtl"))} | ${pct(exactaOriginal("mCnd"))} |`);
  L.push(`| Mayoría a una banda o menos de la del spike original | ${pct(vsOriginal("mCtl"))} | ${pct(vsOriginal("mCnd"))} |`);
  L.push("");
  L.push(`Candidato frente al control de hoy, tarea por tarea: igual ${pct(cndIgualCtl)}; a una banda o menos ${pct(cndVsCtl)}.`);
  L.push(`espera_externa concorde en las 3 corridas del candidato: ${pct(filas.filter((f) => f.esperaCnd).length)}.`);
  L.push("");
  L.push(`**Puerta del candidato:** ${pasaPuerta ? "PASA (> 80 %)" : "NO PASA (≤ 80 %)"}. El cambio de modelo espera el visto del fundador.`);
  L.push("");
  const perdidos = casos.filter((c) => c.texto === null);
  if (perdidos.length) {
    L.push("## Casos que ya no están en el grafo de hoy (no se inventan)");
    for (const p of perdidos) L.push(`- ${p.label} (${p.dominio}; banda original ${p.moda})`);
    L.push("");
  }
  L.push("## Caso por caso");
  L.push("");
  L.push("| Tarea | Spike original | Control (3 corridas) | Candidato (3 corridas) |");
  L.push("|---|---|---|---|");
  for (const f of filas) {
    const v = (xs: (Banda | null)[]) => xs.map((b) => b ?? "?").join("/");
    L.push(`| ${f.c.label.replace(/\|/g, "/")} | ${f.c.bandas.join("/")} | ${v(f.ctl)} | ${v(f.cnd)} |`);
  }
  const fecha = new Date().toISOString().slice(0, 10);
  const dir = path.join(ROOT, "docs", "corrida_final", fecha);
  mkdirSync(dir, { recursive: true });
  writeFileSync(path.join(dir, "revalidacion_estimador.md"), L.join("\n") + "\n", "utf8");
  console.log(L.slice(0, 14).join("\n"));
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
