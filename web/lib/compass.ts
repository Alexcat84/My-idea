/**
 * compass.ts - Fase 3.0: port de la brujula semantica (buscar_afines en
 * prototipo_motor.py), pero con Voyage AI en runtime en vez de
 * sentence-transformers (Python-only, no viaja a la web).
 *
 * El indice de los 1266 nodos (web/lib/assets/semantic_index.json) se
 * genero UNA vez con scripts/build_semantic_index_voyage.py
 * (input_type="document"). En cada turno, esta funcion hace UNA llamada
 * corta a Voyage para embeber solo la respuesta del usuario
 * (input_type="query", ~$0.0001/turno) y calcula similitud coseno en
 * memoria contra el indice ya cargado -- sin dependencias nativas, apto
 * para una funcion serverless.
 *
 * Red de seguridad (igual que Fase 2.8 en Python): sin VOYAGE_API_KEY, o
 * si la llamada falla por cualquier razon, la brujula se desactiva
 * SILENCIOSAMENTE (un aviso en el log, nunca un error visible al
 * usuario) y el motor sigue funcionando solo con navegacion local --
 * exactamente el mismo fallback que ya existe en el CLI.
 *
 * MIN_SCORE_SALTO recalibrado para voyage-4-lite: el espacio de similitud
 * de un proveedor de embeddings distinto no es comparable en escala
 * absoluta al de sentence-transformers. Recalibrado contra los mismos 2
 * casos de referencia de la Fase 2.9 (ver
 * scripts/build_semantic_index_voyage.py, seccion de recalibracion):
 *   'no he calculado bien cuanto me cuesta cada pieza' -> hoja_estimacion_costos
 *     score=0.3507 (debe PASAR)
 *   'mi resina hace burbujas y mi QR grabado con laser se borra' -> alfabetizacion_en_materiales_maliciosos
 *     score=0.2581 (debe quedar EXCLUIDO)
 * Umbral elegido: 0.30 (entre ambos, con margen simetrico ~0.05 hacia
 * cada lado). Con sentence-transformers el umbral original era 0.42 --
 * los numeros no son comparables entre proveedores, solo el ORDEN
 * relativo importa, y ese orden se preservo.
 */
import semanticIndexJson from "./assets/semantic_index.json";

export const MIN_SCORE_SALTO = 0.3;
export const MAX_SALTOS_POSIBLES_OFRECIDOS = 8;

const VOYAGE_MODEL = "voyage-4-lite";
const VOYAGE_URL = "https://api.voyageai.com/v1/embeddings";
const DOMINIOS_DESBLOQUEADOS_DEFECTO = ["core"];

interface SemanticIndexShape {
  model: string;
  dimension: number;
  ids: string[];
  embeddings: number[][];
}

const index = semanticIndexJson as SemanticIndexShape;

let avisoImpreso = false;

function avisar(motivo: string) {
  if (!avisoImpreso) {
    avisoImpreso = true;
    console.warn(`  (brujula semantica no disponible, navegacion solo local: ${motivo})`);
  }
}

/** Equivalente a _cargar_brujula() + el .encode() de la query en Python,
 * combinados: una sola llamada a Voyage por turno. Devuelve null (nunca
 * lanza) si la brujula no esta disponible por cualquier motivo -- el
 * llamador debe tratar null exactamente como "sin candidatos". */
async function embedQuery(texto: string): Promise<number[] | null> {
  const apiKey = process.env.VOYAGE_API_KEY;
  if (!apiKey) {
    avisar("falta VOYAGE_API_KEY");
    return null;
  }
  try {
    const resp = await fetch(VOYAGE_URL, {
      method: "POST",
      headers: { Authorization: `Bearer ${apiKey}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        input: [texto],
        model: VOYAGE_MODEL,
        input_type: "query",
        output_dimension: index.dimension,
      }),
    });
    if (!resp.ok) {
      throw new Error(`Voyage respondio ${resp.status}`);
    }
    const data = await resp.json();
    return data.data[0].embedding as number[];
  } catch (e) {
    avisar(String(e));
    return null;
  }
}

function coseno(a: number[], b: number[]): number {
  let dot = 0;
  let normA = 0;
  let normB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  const denom = Math.sqrt(normA) * Math.sqrt(normB);
  return denom ? dot / denom : 0;
}

export interface CandidatoAfin {
  id: string;
  score: number;
}

export interface NodoConDominio {
  dominio?: string;
  [key: string]: unknown;
}

export interface BuscarAfinesOpts {
  k?: number;
  minScore?: number;
  graph?: Record<string, NodoConDominio>;
  dominiosDesbloqueados?: string[];
}

/**
 * Top-k nodos de TODO el grafo mas afines semanticamente a `texto`,
 * excluyendo `excluidos`. Devuelve [] si la brujula no esta disponible o
 * si `texto` esta vacio -- misma firma de comportamiento que
 * buscar_afines() en Python (nunca lanza, nunca bloquea el turno).
 */
export async function buscarAfines(
  texto: string,
  excluidos: Set<string>,
  opts: BuscarAfinesOpts = {}
): Promise<CandidatoAfin[]> {
  if (!texto || !texto.trim()) return [];
  const query = await embedQuery(texto);
  if (!query) return [];

  const k = opts.k ?? 5;
  const minScore = opts.minScore ?? 0.0;
  const dominios = opts.dominiosDesbloqueados ?? DOMINIOS_DESBLOQUEADOS_DEFECTO;

  const puntuados = index.ids
    .map((id, i) => ({ id, score: coseno(query, index.embeddings[i]) }))
    .sort((a, b) => b.score - a.score);

  const resultados: CandidatoAfin[] = [];
  for (const { id, score } of puntuados) {
    if (excluidos.has(id)) continue;
    if (opts.graph && opts.graph[id] && !dominios.includes(opts.graph[id].dominio ?? "core")) continue;
    if (score < minScore) break; // orden descendente: nada mas adelante supera el umbral
    resultados.push({ id, score });
    if (resultados.length >= k) break;
  }
  return resultados;
}
