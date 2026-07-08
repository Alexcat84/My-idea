// Fase 3.0.1: genera web/lib/testFixtures/compass_refs.json UNA sola vez.
// Embebe las 2 queries de referencia de la Fase 2.9 con Voyage y guarda los
// vectores, para que la calibracion del umbral sea verificable OFFLINE (en
// clones limpios, CI y auditorias) sin key ni red.
//
// IMPORTANTE: el body del request (model, input_type, output_dimension) debe
// ser IDENTICO al de embedQuery en web/lib/compass.ts. Si compass.ts usa
// parametros distintos a los de abajo, copiar los de compass.ts aqui antes
// de correr. (Fase 3.0.1: compass.ts SI envia output_dimension=index.dimension
// -- sin este campo Voyage devuelve el default de 1024, no los 512 que usa
// semantic_index.json, y el coseno contra el indice real quedaria roto por
// mismatch de dimension. Se lee aqui del propio semantic_index.json para
// quedar sincronizado con compass.ts sin duplicar un numero a mano.)
//
// Uso (desde la raiz del repo, con VOYAGE_API_KEY en el .env raiz):
//   node web/scripts/gen_compass_fixture.mjs
import { mkdirSync, writeFileSync, existsSync, readFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";

const ROOT = path.resolve(import.meta.dirname, "..", "..");
const ENV_PATH = path.join(ROOT, ".env");
if (existsSync(ENV_PATH)) process.loadEnvFile(ENV_PATH);

const KEY = process.env.VOYAGE_API_KEY;
if (!KEY) {
  console.error("Falta VOYAGE_API_KEY (en el .env raiz o en el ambiente).");
  process.exit(1);
}

const MODEL = "voyage-4-lite";
const QUERY_POSITIVA = "no he calculado bien cuanto me cuesta cada pieza";
const QUERY_NEGATIVA = "mi resina hace burbujas y mi QR grabado con laser se borra";

const INDEX_PATH = path.join(ROOT, "web", "lib", "assets", "semantic_index.json");
if (!existsSync(INDEX_PATH)) {
  console.error(`Falta ${INDEX_PATH} -- correr scripts/build_semantic_index_voyage.py primero.`);
  process.exit(1);
}
const { dimension: OUTPUT_DIMENSION, model: INDEX_MODEL } = JSON.parse(readFileSync(INDEX_PATH, "utf-8"));
if (INDEX_MODEL !== MODEL) {
  console.error(`El modelo del indice (${INDEX_MODEL}) no coincide con MODEL=${MODEL} de este generador.`);
  process.exit(1);
}

async function embed(texto) {
  const res = await fetch("https://api.voyageai.com/v1/embeddings", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${KEY}`,
    },
    body: JSON.stringify({ input: [texto], model: MODEL, input_type: "query", output_dimension: OUTPUT_DIMENSION }),
  });
  if (!res.ok) {
    throw new Error(`Voyage ${res.status}: ${await res.text()}`);
  }
  const data = await res.json();
  return data.data[0].embedding;
}

const fixture = {
  model: MODEL,
  generado: new Date().toISOString(),
  nota: "Vectores de referencia Fase 2.9 para calibracion offline de MIN_SCORE_SALTO. Regenerar SOLO si cambia el modelo o la dimension del indice.",
  query_positiva: { texto: QUERY_POSITIVA, embedding: await embed(QUERY_POSITIVA) },
  query_negativa: { texto: QUERY_NEGATIVA, embedding: await embed(QUERY_NEGATIVA) },
};

const outDir = path.join(ROOT, "web", "lib", "testFixtures");
mkdirSync(outDir, { recursive: true });
const outPath = path.join(outDir, "compass_refs.json");
writeFileSync(outPath, JSON.stringify(fixture, null, 2) + "\n", { encoding: "utf-8" });
console.log(`Fixture escrito: ${outPath}`);
console.log(`  dim=${fixture.query_positiva.embedding.length}, model=${MODEL}`);
