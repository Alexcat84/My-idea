/**
 * i18n F1: MEDICIÓN DEL BUSCADOR MULTILINGÜE. El grafo sigue en español (el
 * índice semántico se hizo con el texto en español de los nodos) y la consulta
 * es el texto del usuario en su idioma. ¿Recupera los mismos nodos una idea
 * escrita en coreano que su versión en español?
 *
 * Método: 20 ideas, la misma en los 11 idiomas (ideas_medicion.json). Cada una
 * pasa por `buscarAfines` (la función de la app), con el grafo real y el
 * dominio por defecto, pidiendo los 10 primeros sin umbral. Por idioma se mide
 * contra el español: el solape de los 10 primeros (|A∩B|/10), si coincide el
 * primero, y cuántos candidatos pasan el umbral MIN_SCORE_SALTO de la app.
 * Con --remedio, además traduce la consulta al español (Claude Haiku) antes de
 * buscar y mide lo mismo.
 *
 * Uso (necesita VOYAGE_API_KEY en el .env raíz; con --remedio, también
 * ANTHROPIC_API_KEY):  npx tsx scripts/i18n/medicion_buscador.ts [--remedio]
 * Escribe docs/i18n/F1_resultados.json.
 */
import "../../lib/loadRootEnv";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { buscarAfines, MIN_SCORE_SALTO } from "../../lib/compass";
import { cargarGrafo } from "../../lib/engine/graph";
import { createAnthropicClient } from "../../lib/anthropicClient";
import { MODEL_HAIKU } from "../../lib/costmeter";

const IDIOMAS = ["es", "en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"] as const;
type Idioma = (typeof IDIOMAS)[number];
const K = 10;

const ideas = JSON.parse(readFileSync(path.join(__dirname, "ideas_medicion.json"), "utf8")) as Array<Record<Idioma, string>>;
const grafo = cargarGrafo();
const conRemedio = process.argv.includes("--remedio");

const dormir = (ms: number) => new Promise((r) => setTimeout(r, ms));

/** buscarAfines devuelve [] si Voyage falla (limite de tasa, red): se reintenta
 * con espera creciente para no confundir una falla con "no encontró nada". */
async function top(texto: string): Promise<{ ids: string[]; scores: number[] }> {
  for (let intento = 1; intento <= 6; intento += 1) {
    const r = await buscarAfines(texto, new Set(), { k: K, minScore: 0, graph: grafo as never });
    if (r.length > 0) return { ids: r.map((c) => c.id), scores: r.map((c) => c.score) };
    await dormir(2000 * intento);
  }
  throw new Error(`Voyage no respondió para: ${texto.slice(0, 40)}`);
}

async function alEspanol(texto: string): Promise<string> {
  const client = createAnthropicClient();
  const resp = await client.messages.create({
    model: MODEL_HAIKU,
    max_tokens: 300,
    system: "Traduce al español el texto del usuario. Responde SOLO con la traducción, sin comillas ni comentarios.",
    messages: [{ role: "user", content: texto }],
  });
  const bloque = resp.content.find((b) => b.type === "text");
  return bloque && bloque.type === "text" ? bloque.text.trim() : texto;
}

const solape = (a: string[], b: string[]) => a.filter((x) => b.includes(x)).length / K;

async function main() {
  const filas: Array<Record<string, unknown>> = [];
  for (const [n, idea] of ideas.entries()) {
    const es = await top(idea.es);
    for (const idioma of IDIOMAS) {
      const r = idioma === "es" ? es : await top(idea[idioma]);
      const fila: Record<string, unknown> = {
        idea: n + 1,
        idioma,
        solape: solape(r.ids, es.ids),
        primero: r.ids[0] === es.ids[0],
        sobreUmbral: r.scores.filter((s) => s >= MIN_SCORE_SALTO).length,
        scoreMax: Number(r.scores[0].toFixed(3)),
      };
      if (conRemedio && idioma !== "es") {
        const traducida = await alEspanol(idea[idioma]);
        const rt = await top(traducida);
        fila.remedio = {
          traducida,
          solape: solape(rt.ids, es.ids),
          primero: rt.ids[0] === es.ids[0],
          sobreUmbral: rt.scores.filter((s) => s >= MIN_SCORE_SALTO).length,
        };
      }
      filas.push(fila);
    }
    process.stdout.write(`idea ${n + 1}/${ideas.length} lista\n`);
  }

  const resumen = IDIOMAS.map((idioma) => {
    const f = filas.filter((x) => x.idioma === idioma);
    const media = (sel: (x: Record<string, unknown>) => number) => Number((f.reduce((t, x) => t + sel(x), 0) / f.length).toFixed(3));
    const base = {
      idioma,
      solapeMedio: media((x) => x.solape as number),
      primeroIgual: media((x) => ((x.primero as boolean) ? 1 : 0)),
      sobreUmbralMedio: media((x) => x.sobreUmbral as number),
      scoreMaxMedio: media((x) => x.scoreMax as number),
    };
    if (!conRemedio || idioma === "es") return base;
    const rem = (sel: (x: { solape: number; primero: boolean; sobreUmbral: number }) => number) =>
      Number((f.reduce((t, x) => t + sel(x.remedio as { solape: number; primero: boolean; sobreUmbral: number }), 0) / f.length).toFixed(3));
    return {
      ...base,
      remedio: {
        solapeMedio: rem((x) => x.solape),
        primeroIgual: rem((x) => (x.primero ? 1 : 0)),
        sobreUmbralMedio: rem((x) => x.sobreUmbral),
      },
    };
  });

  const salida = path.join(__dirname, "..", "..", "..", "docs", "i18n", conRemedio ? "F1_resultados_remedio.json" : "F1_resultados.json");
  writeFileSync(salida, JSON.stringify({ k: K, umbral: MIN_SCORE_SALTO, resumen, filas }, null, 2));
  console.table(resumen.map((r) => ({ ...r, remedio: undefined, ...(r as { remedio?: object }).remedio && { remSolape: (r as { remedio: { solapeMedio: number } }).remedio.solapeMedio } })));
  console.log(`escrito ${salida}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
