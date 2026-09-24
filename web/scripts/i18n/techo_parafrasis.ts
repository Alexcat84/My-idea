/**
 * i18n F1, referencia: el TECHO del solape. Una traducción al español es una
 * paráfrasis del original, así que ni una traducción perfecta daría solape 1.
 * Aquí se mide cuánto solapa una paráfrasis en español (Claude Haiku) con la
 * idea original en español. Uso: npx tsx scripts/i18n/techo_parafrasis.ts
 */
import "../../lib/loadRootEnv";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { buscarAfines, MIN_SCORE_SALTO } from "../../lib/compass";
import { cargarGrafo } from "../../lib/engine/graph";
import { createAnthropicClient } from "../../lib/anthropicClient";
import { MODEL_HAIKU } from "../../lib/costmeter";

const K = 10;
const ideas = JSON.parse(readFileSync(path.join(__dirname, "ideas_medicion.json"), "utf8")) as Array<{ es: string }>;
const grafo = cargarGrafo();
const dormir = (ms: number) => new Promise((r) => setTimeout(r, ms));

async function top(texto: string) {
  for (let i = 1; i <= 6; i += 1) {
    const r = await buscarAfines(texto, new Set(), { k: K, minScore: 0, graph: grafo as never });
    if (r.length > 0) return r;
    await dormir(2000 * i);
  }
  throw new Error("Voyage no respondió");
}

async function main() {
  const client = createAnthropicClient();
  const filas: Array<{ parafrasis: string; solape: number; primero: boolean; sobreUmbral: number }> = [];
  for (const idea of ideas) {
    const resp = await client.messages.create({
      model: MODEL_HAIKU,
      max_tokens: 300,
      system: "Reformula en español el texto del usuario con otras palabras, conservando exactamente el sentido. Responde SOLO con la reformulación.",
      messages: [{ role: "user", content: idea.es }],
    });
    const b = resp.content.find((x) => x.type === "text");
    const parafrasis = b && b.type === "text" ? b.text.trim() : idea.es;
    const a = await top(idea.es);
    const p = await top(parafrasis);
    const ids = a.map((c) => c.id);
    filas.push({
      parafrasis,
      solape: p.filter((c) => ids.includes(c.id)).length / K,
      primero: p[0].id === a[0].id,
      sobreUmbral: p.filter((c) => c.score >= MIN_SCORE_SALTO).length,
    });
  }
  const media = (f: (x: (typeof filas)[number]) => number) => Number((filas.reduce((t, x) => t + f(x), 0) / filas.length).toFixed(3));
  const resumen = { solapeMedio: media((x) => x.solape), primeroIgual: media((x) => (x.primero ? 1 : 0)), sobreUmbralMedio: media((x) => x.sobreUmbral) };
  writeFileSync(path.join(__dirname, "..", "..", "..", "docs", "i18n", "F1_techo_parafrasis.json"), JSON.stringify({ resumen, filas }, null, 2));
  console.log(resumen);
}
main().catch((e) => { console.error(e); process.exit(1); });
