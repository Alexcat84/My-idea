/**
 * Juez de fidelidad por la API (decision del fundador, 9 oct 2026): el mismo juez ciego, la misma relectura de las
 * trampas no cazadas y el mismo arbitro que en la primera medicion A/B corrieron como subagentes del entorno de
 * desarrollo, ahora como llamadas directas a la API de Anthropic con la clave del .env raiz, para que se paguen con el
 * saldo de la API. Mismas instrucciones (docs/producto/JUEZ_FIDELIDAD.md), mismos textos de encargo, mismo modelo
 * (Opus 5.5, el que heredaban los subagentes). Diferencia declarada: el paquete va dentro del mensaje en lugar de que
 * el juez lo abra con una herramienta de lectura.
 *
 * Por cada version: (1) un juez por paquete; (2) una relectura de cada trampa que el juez no cazo; (3) un arbitro por
 * paquete REAL con hallazgos. Escribe veredictos_<V>/fNNN.json, fNNN_relectura.json, arbitro_fNNN.json y resumen.json.
 * Reanudable: lo que ya esta escrito no se vuelve a pedir. Tope duro de gasto: --tope (USD, estimado con el precio
 * declarado abajo; la cifra oficial es la consola del fundador).
 *
 * DOS JUECES (--dos-jueces, regla de cierre del fundador, 9 oct 2026): dos jueces independientes por paquete (la misma
 * instruccion, dos llamadas que no se ven entre si). Un hallazgo solo pasa al arbitro si lo encuentran los dos:
 * coinciden si, normalizadas (sin acentos, minusculas, solo letras y cifras), una afirmacion contiene a la otra o
 * comparten un tramo seguido de al menos 20 caracteres que cubre al menos la mitad de la mas corta. La trampa esta
 * cazada si la caza cualquiera de los dos (o la relectura).
 *
 * Uso (desde web/, con el .env raiz): npx tsx scripts/corrida_final_juez_api.ts --dir <juez_ab2> [--versiones A,B] [--tope 25] [--paralelo 6] [--dos-jueces]
 */
import Anthropic from "@anthropic-ai/sdk";
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz } from "./_shared/http";
import { Presupuesto, reservaDeLlamada } from "../lib/presupuestoGuion";

cargarEnvRaiz();

const MODELO = "claude-opus-5-5";
// Precio por millon de tokens [entrada, salida] usado SOLO para el tope de este guion (estimado, declarado).
const PRECIO: [number, number] = [5, 25];
const RUBRICA = readFileSync(path.resolve(import.meta.dirname, "..", "..", "docs", "producto", "JUEZ_FIDELIDAD.md"), "utf8");

const arg = (n: string) => {
  const i = process.argv.indexOf(n);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
};

type Hallazgo = { clase: string; afirmacion: string; por_que?: string; nodo?: string | null };
type Veredicto = { paquete: string; hallazgos: Hallazgo[]; afirmaciones_leidas?: number };
type Clave = { paquete: string; origen: string; trampa?: { tipo: string; frase: string; nodo: string | null } };

let gastado = 0;
let presupuesto = new Presupuesto(25);
// Tope de salida de cada llamada: es tambien lo que reserva el presupuesto, asi que no se pone por lo alto sin motivo.
const MAX_SALIDA = 20000;

const ENCARGO_JUEZ =
  "Eres un juez ciego de fidelidad. Tienes SOLO las instrucciones (sistema) y tu paquete (abajo); no hay nada más. Sigue las instrucciones al pie de la letra: lee la salida ENTERA, frase por frase, divide en afirmaciones, coteja cada una contra los nodos y el contexto, y marca solo contrario, invencion y procedencia (afirmación exacta, porqué, nodo). Fíjate también en causas y hechos del negocio de la persona que nadie dio. Sé exigente en las dos direcciones. Devuelve SOLO el JSON pedido, sin texto alrededor.";
const ENCARGO_RELECTURA =
  "Eres un juez ciego de fidelidad. Tienes SOLO las instrucciones (sistema) y tu paquete (abajo); no hay nada más. Sigue las instrucciones al pie de la letra. Lee la salida ENTERA, frase por frase, sin saltarte ninguna sección: divide en afirmaciones, coteja cada una contra los nodos y el contexto, y marca solo contrario, invencion y procedencia, con la afirmación exacta, el porqué y el nodo. Presta especial atención a cualquier frase que contradiga lo que enseña un nodo (por ejemplo, que diga que un paso no hace falta cuando un nodo lo pide). Sé exigente en las dos direcciones. Devuelve SOLO el JSON pedido, sin texto alrededor.";
const ENCARGO_ARBITRO =
  'Eres el ÁRBITRO del juez de fidelidad de la salida (My Idea). Un juez ciego marcó hallazgos y tú decides, con evidencia, si cada uno se sostiene antes de que cuente. No busques hallazgos nuevos. Tienes SOLO la rúbrica (sistema), el paquete y los hallazgos del juez (abajo). Para CADA hallazgo: ubica la frase completa en `salida` (con la oración anterior y la siguiente), busca en `nodos` (todo su texto) y en `contexto` lo que la sostenga aunque sea con otras palabras, y aplica la rúbrica: ¿se sostiene como contrario / invencion / procedencia, o es sostenida u operativa? Sé justo en las dos direcciones: un hecho o una causa que nadie dio es invención aunque sea plausible; un consejo práctico no lo es; algo que la persona contó no es invención.\nDevuelve SOLO este JSON:\n{"paquete": "fNNN", "arbitrajes": [{"afirmacion": "...", "clase_juez": "...", "veredicto": "SOSTENIDO" | "DESCARTADO", "clase_final": "contrario|invencion|procedencia|sostenida|operativa", "evidencia": "con node_id o cita del contexto", "razon": "una o dos frases"}]}';

function jsonDe(texto: string): unknown {
  const ini = texto.indexOf("{");
  const fin = texto.lastIndexOf("}");
  if (ini < 0 || fin < ini) throw new Error(`sin JSON en la respuesta: ${texto.slice(0, 200)}`);
  return JSON.parse(texto.slice(ini, fin + 1));
}

async function pedir(client: Anthropic, encargo: string, cuerpo: string): Promise<unknown> {
  for (let intento = 1; ; intento++) {
    // Topes (decision del fundador, 10 oct 2026): la llamada reserva su peor caso ANTES de lanzarse; el tope se cumple
    // aunque haya llamadas en paralelo (lib/presupuestoGuion.ts).
    const reserva = presupuesto.reservar(reservaDeLlamada(RUBRICA.length + encargo.length + cuerpo.length + 2, MAX_SALIDA, PRECIO));
    let msg;
    try {
      msg = await client.messages
        .stream({ model: MODELO, max_tokens: MAX_SALIDA, system: RUBRICA, messages: [{ role: "user", content: `${encargo}\n\n${cuerpo}` }] })
        .finalMessage();
    } catch (e) {
      presupuesto.liberar(reserva);
      if (intento >= 3) throw e;
      console.log(`  reintento ${intento}: ${String(e).slice(0, 160)}`);
      continue;
    }
    presupuesto.cerrar(reserva, (msg.usage.input_tokens * PRECIO[0] + msg.usage.output_tokens * PRECIO[1]) / 1e6);
    gastado = presupuesto.gastado;
    try {
      return jsonDe(msg.content.flatMap((b) => (b.type === "text" ? [b.text] : [])).join(""));
    } catch (e) {
      if (intento >= 3) throw e;
      console.log(`  reintento ${intento}: ${String(e).slice(0, 160)}`);
    }
  }
}

async function enParalelo<T>(tareas: Array<() => Promise<T>>, n: number): Promise<void> {
  let i = 0;
  await Promise.all(
    Array.from({ length: n }, async () => {
      while (i < tareas.length) await tareas[i++]();
    })
  );
}

const normal = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
/** La trampa esta cazada si algun hallazgo cita una parte reconocible de su frase. */
function cazada(frase: string, hallazgos: Hallazgo[]): boolean {
  const f = normal(frase);
  return hallazgos.some((h) => {
    const a = normal(h.afirmacion ?? "");
    return a.length >= 12 && (f.includes(a) || a.includes(f) || f.includes(a.slice(0, 30)) || a.includes(f.slice(0, 30)));
  });
}

/** El tramo seguido mas largo que comparten dos textos (en caracteres). */
function tramoComun(a: string, b: string): number {
  let mejor = 0;
  let previa = new Array<number>(b.length + 1).fill(0);
  for (let i = 1; i <= a.length; i++) {
    const fila = new Array<number>(b.length + 1).fill(0);
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) {
        fila[j] = previa[j - 1] + 1;
        if (fila[j] > mejor) mejor = fila[j];
      }
    }
    previa = fila;
  }
  return mejor;
}

/** Dos hallazgos de jueces distintos son el mismo (regla escrita antes de medir). */
function coinciden(x: string, y: string): boolean {
  const a = normal(x);
  const b = normal(y);
  if (!a || !b) return false;
  if (a.includes(b) || b.includes(a)) return true;
  const tramo = tramoComun(a, b);
  return tramo >= 20 && tramo >= Math.min(a.length, b.length) / 2;
}

async function version(client: Anthropic, dir: string, v: string, paralelo: number, dosJueces: boolean) {
  const dirP = path.join(dir, `paquetes_${v}`);
  const dirV = path.join(dir, `veredictos_${v}`);
  mkdirSync(dirV, { recursive: true });
  const claves = (JSON.parse(readFileSync(path.join(dir, `claves_${v}`, "claves.json"), "utf8")) as { claves: Clave[] }).claves;
  const porPaquete = new Map(claves.map((c) => [c.paquete, c]));
  const paquetes = readdirSync(dirP).filter((f) => f.endsWith(".json")).map((f) => f.replace(".json", "")).sort();
  const leer = (f: string) => readFileSync(path.join(dirP, `${f}.json`), "utf8");
  const veredicto = (f: string, sufijo = "") => JSON.parse(readFileSync(path.join(dirV, `${f}${sufijo}.json`), "utf8")) as Veredicto;

  // 1. Un juez por paquete (dos, independientes, con --dos-jueces).
  const sufijos = dosJueces ? ["_j1", "_j2"] : [""];
  await enParalelo(
    paquetes.flatMap((f) =>
      sufijos.map((s) => async () => {
        const salida = path.join(dirV, `${f}${s}.json`);
        if (existsSync(salida)) return;
        const r = (await pedir(client, ENCARGO_JUEZ, `Tu paquete (${f}):\n${leer(f)}`)) as Veredicto;
        r.paquete = f;
        writeFileSync(salida, JSON.stringify(r, null, 2), "utf8");
        console.log(`${v} juez${s} ${f}: ${r.hallazgos?.length ?? 0} hallazgos | $${gastado.toFixed(3)}`);
      })
    ),
    paralelo
  );
  // Con dos jueces, lo que llega al arbitro es solo lo que encontraron los dos (fNNN.json = las coincidencias).
  if (dosJueces) {
    for (const f of paquetes) {
      const j1 = veredicto(f, "_j1").hallazgos ?? [];
      const j2 = veredicto(f, "_j2").hallazgos ?? [];
      const comunes = j1.flatMap((h) => {
        const otro = j2.find((g) => coinciden(h.afirmacion ?? "", g.afirmacion ?? ""));
        return otro ? [{ ...h, clase_juez2: otro.clase, afirmacion_juez2: otro.afirmacion, por_que_juez2: otro.por_que }] : [];
      });
      writeFileSync(path.join(dirV, `${f}.json`), JSON.stringify({ paquete: f, hallazgos: comunes, juez1: j1.length, juez2: j2.length }, null, 2), "utf8");
    }
  }

  // 2. Relectura de las trampas no cazadas.
  const trampas: Record<string, { tipo: string; cazada_juez: boolean; cazada_relectura: boolean | null }> = {};
  for (const f of paquetes) {
    const c = porPaquete.get(f);
    if (c?.origen !== "trampa" || !c.trampa) continue;
    const enJuez = sufijos.some((s) => cazada(c.trampa!.frase, veredicto(f, s).hallazgos ?? []));
    let enRelectura: boolean | null = null;
    if (!enJuez) {
      const salida = path.join(dirV, `${f}_relectura.json`);
      if (!existsSync(salida)) {
        const r = (await pedir(client, ENCARGO_RELECTURA, `Tu paquete (${f}):\n${leer(f)}`)) as Veredicto;
        r.paquete = f;
        writeFileSync(salida, JSON.stringify(r, null, 2), "utf8");
      }
      enRelectura = cazada(c.trampa.frase, veredicto(f, "_relectura").hallazgos ?? []);
      console.log(`${v} relectura ${f}: trampa ${enRelectura ? "cazada" : "NO cazada"} | $${gastado.toFixed(3)}`);
    }
    trampas[f] = { tipo: c.trampa.tipo, cazada_juez: enJuez, cazada_relectura: enRelectura };
  }

  // 3. Un arbitro por paquete REAL con hallazgos.
  const reales = paquetes.filter((f) => porPaquete.get(f)?.origen === "real");
  await enParalelo(
    reales.map((f) => async () => {
      const hallazgos = veredicto(f).hallazgos ?? [];
      const salida = path.join(dirV, `arbitro_${f}.json`);
      if (hallazgos.length === 0 || existsSync(salida)) return;
      const r = (await pedir(
        client,
        ENCARGO_ARBITRO.replace("fNNN", f),
        `El paquete (${f}):\n${leer(f)}\n\nLos hallazgos del juez:\n${JSON.stringify(veredicto(f), null, 2)}`
      )) as { paquete: string; arbitrajes: Array<{ veredicto: string; clase_final: string }> };
      r.paquete = f;
      writeFileSync(salida, JSON.stringify(r, null, 2), "utf8");
      console.log(`${v} arbitro ${f}: ${r.arbitrajes.filter((a) => a.veredicto === "SOSTENIDO").length} de ${r.arbitrajes.length} sostenidos | $${gastado.toFixed(3)}`);
    }),
    paralelo
  );

  // Resumen.
  const porPlan = reales.map((f) => {
    const hallazgos = veredicto(f).hallazgos ?? [];
    const arb = existsSync(path.join(dirV, `arbitro_${f}.json`))
      ? (JSON.parse(readFileSync(path.join(dirV, `arbitro_${f}.json`), "utf8")) as { arbitrajes: Array<{ veredicto: string; clase_final: string; afirmacion: string }> }).arbitrajes
      : [];
    const sostenidos = arb.filter((a) => a.veredicto === "SOSTENIDO");
    return { paquete: f, hallazgos: hallazgos.length, sostenidos: sostenidos.map((a) => ({ clase: a.clase_final, afirmacion: a.afirmacion })) };
  });
  const sost = porPlan.flatMap((p) => p.sostenidos);
  const resumen = {
    version: v,
    modelo: MODELO,
    dos_jueces: dosJueces,
    hallazgos_brutos: porPlan.reduce((s, p) => s + p.hallazgos, 0),
    sostenidos: sost.length,
    por_clase: { contrario: sost.filter((s) => s.clase === "contrario").length, invencion: sost.filter((s) => s.clase === "invencion").length, procedencia: sost.filter((s) => s.clase === "procedencia").length },
    planes_con_sostenidos: porPlan.filter((p) => p.sostenidos.length > 0).length,
    planes: reales.length,
    trampas,
    por_plan: porPlan,
  };
  writeFileSync(path.join(dirV, "resumen.json"), JSON.stringify(resumen, null, 2), "utf8");
  console.log(`${v}: ${resumen.sostenidos} sostenidos (${JSON.stringify(resumen.por_clase)}) en ${resumen.planes_con_sostenidos} de ${resumen.planes} planes; trampas ${JSON.stringify(trampas)}`);
}

async function main() {
  const dir = arg("--dir");
  if (!dir) throw new Error("uso: --dir <juez_ab2> [--versiones A,B] [--tope 25] [--paralelo 6]");
  presupuesto = new Presupuesto(Number(arg("--tope") ?? 25));
  const paralelo = Number(arg("--paralelo") ?? 6);
  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY, maxRetries: 4 });
  const dosJueces = process.argv.includes("--dos-jueces");
  for (const v of (arg("--versiones") ?? "A,B").split(",")) await version(client, dir, v, paralelo, dosJueces);
  console.log(`LISTO: gastado estimado $${gastado.toFixed(4)} (${MODELO}, ${PRECIO.join("/")} por millon)`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
