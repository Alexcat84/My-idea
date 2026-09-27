// i18n F2: la prueba de que la extracción no cambió ningún texto visible.
//
// Toma el diff del código (web/app, web/lib y web/proxy.ts, sin pruebas, sin los
// assets sincronizados (prompts de la IA y grafo: no son texto de pantalla) ni el
// propio lib/i18n) contra la base, junta cada texto que SALIÓ de una línea
// (cadenas entre comillas, piezas fijas de las plantillas `...${x}...` y texto
// suelto de JSX) y exige que cada uno esté, letra por letra, en algún texto de
// los catálogos en español (lib/i18n/mensajes). Un texto que salió de un archivo
// pero sigue en una línea agregada del mismo archivo no se extrajo (se movió) y
// no cuenta.
//
// Uso (desde web/):  npx tsx scripts/i18n/extraccion_identica.ts [base]
// base por omisión: el merge-base con origin/main. Sale con 1 si falta algo.
import { execFileSync } from "node:child_process";
import { readdirSync, statSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const WEB = path.resolve(__dirname, "..", "..");
const base = process.argv[2] ?? execFileSync("git", ["merge-base", "HEAD", "origin/main"], { cwd: WEB }).toString().trim();

const normal = (t: string) => t.replace(/\s+/g, " ").trim();

/**
 * Las EXCEPCIONES, una por una y con su motivo (decisión del fundador, 28 sep
 * 2026: la guarda no se afloja). Casan EXACTO por archivo y texto: cualquier
 * otro texto que salga de ese mismo archivo sigue fallando. Solo entran textos
 * que no son de pantalla y que el filtro de candidatos no sabe reconocer.
 */
const EXCEPCIONES: Array<{ archivo: string; texto: string; motivo: string }> = [
  {
    archivo: "web/app/api/project/[id]/checklist/route.ts",
    texto:
      "id, plan_id, dominio, etapa, orden, texto, destacado, estado, nota, completed_at, no_aplica_motivo, fecha_base, fecha_base_origen, fecha_base_original, banda, espera_externa, protege_item, deteccion, probabilidad, dolor, camino, nodos_origen, protege_nodos, created_at, updated_at",
    motivo: "lista de columnas del select; creció con heredado_de (migración 047)",
  },
  {
    archivo: "web/app/api/project/[id]/follow/route.ts",
    texto: "id, completado_at",
    motivo: "columnas del select de project_unlocks; la consulta se mudó a lib/cicloApertura.ts",
  },
  {
    archivo: "web/lib/expediente.ts",
    texto: "Seguimiento N",
    motivo: "texto de un comentario de código borrado; los ciclos se llaman ahora Profundización N / Replanteamiento N",
  },
];
const esExcepcion = (archivo: string, t: string) => EXCEPCIONES.some((e) => e.archivo === archivo && e.texto === t);

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    return statSync(p).isDirectory() ? archivos(p) : p.endsWith(".ts") && !p.endsWith(".test.ts") ? [p] : [];
  });
}

function textos(x: unknown, fuera: string[]) {
  if (typeof x === "string") fuera.push(x);
  else if (Array.isArray(x)) x.forEach((y) => textos(y, fuera));
  else if (x && typeof x === "object") Object.values(x).forEach((y) => textos(y, fuera));
}

/** Los textos de una línea de código que podrían ser visibles. */
function candidatos(linea: string): string[] {
  const fuera: string[] = [];
  for (const m of linea.matchAll(/"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)'/g)) fuera.push(m[1] ?? m[2]);
  for (const m of linea.matchAll(/`([^`]*)`/g)) fuera.push(...m[1].split(/\$\{[^}]*\}/));
  // texto de JSX: entre > y <, o una línea que es solo texto
  for (const m of linea.matchAll(/>([^<>{}]+)</g)) fuera.push(m[1]);
  const limpia = linea.trim();
  // (una línea suelta de un ternario o de una condición, "? X" o "&& y", es código)
  // (ni una propiedad "clave: valor ?? otro," ni una lista de dependencias "[a, b]")
  const esCodigo = /\?\?|\?\.|^\[|\]$|^[\w.]+:\s/.test(limpia);
  if (limpia && !esCodigo && !/[{}()=;<>"'`]/.test(limpia) && !/^(\/\/|\*|\/\*|\?|:|&&|\|\|)/.test(limpia)) fuera.push(limpia);
  return fuera
    // sin etiquetas HTML, igual que el catálogo (un `<p>Tu código…</p>` de un correo)
    .map((t) => normal(t.replace(/\\n/g, " ").replace(/&nbsp;/g, " ").replace(/<\/?\w+\/?>/g, " ")))
    .filter((t) => /[a-záéíóúñü]{2,}/i.test(t))
    // un "${x}" es la interpolación de una plantilla vieja, no un texto
    .filter((t) => !t.includes("${"))
    // clases de Tailwind, rutas, claves y nombres técnicos: no son texto visible
    .filter((t) => !/^[\w\-:/.[\]#%@&=?,]+$/.test(t) || /[áéíóúñ¿¡]/i.test(t) || /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/.test(t))
    .filter((t) => !t.split(" ").every((w) => /[-:[\]/]|^\d/.test(w) || /^(flex|grid|block|hidden|inline|relative|absolute|fixed|sticky|text|bg|border|rounded|shadow|font|items|justify|gap|p|m|w|h)$/.test(w)));
}

async function main() {
  const corpus: string[] = [];
  for (const archivo of archivos(path.join(WEB, "lib", "i18n", "mensajes"))) {
    const mod = (await import(pathToFileURL(archivo).href)) as Record<string, unknown>;
    for (const v of Object.values(mod)) if (v && typeof v === "object" && "es" in v) textos((v as { es: unknown }).es, corpus);
  }
  const corpusNormal = corpus.map((t) => normal(t.replace(/<\/?\w+\/?>/g, " ").replace(/\{\{\w+\}\}/g, " ")));
  // Palabra por palabra: "Guardar" no se da por encontrado dentro de "Guardarr".
  const estaEnCatalogo = (t: string) => {
    const esc = t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const re = new RegExp(`(^|[^\\p{L}\\p{N}])${esc}($|[^\\p{L}\\p{N}])`, "u");
    return corpusNormal.some((c) => re.test(c));
  };

  const diff = execFileSync(
    "git",
    ["diff", "-U0", base, "--", "app", "lib", "proxy.ts", ":(exclude)*.test.ts", ":(exclude)*.test.tsx", ":(exclude)lib/i18n", ":(exclude)lib/assets"],
    { cwd: WEB, maxBuffer: 256 * 1024 * 1024 }
  ).toString();

  const faltan: string[] = [];
  const exceptuados = new Set<string>();
  let revisados = 0;
  for (const bloque of diff.split(/^diff --git /m).slice(1)) {
    const archivo = bloque.split("\n")[0].split(" b/")[1] ?? "?";
    const quitadas = bloque.split("\n").filter((l) => l.startsWith("-") && !l.startsWith("---")).map((l) => l.slice(1));
    const agregadas = normal(bloque.split("\n").filter((l) => l.startsWith("+") && !l.startsWith("+++")).map((l) => l.slice(1)).join(" "));
    for (const linea of quitadas) {
      for (const t of candidatos(linea)) {
        if (agregadas.includes(t)) continue; // se movió, no se extrajo
        revisados++;
        if (estaEnCatalogo(t)) continue;
        if (esExcepcion(archivo, t)) {
          exceptuados.add(`${archivo}: "${t.slice(0, 60)}${t.length > 60 ? "…" : ""}"`);
          continue;
        }
        faltan.push(`${archivo}: "${t}"`);
      }
    }
  }
  console.log(`extracción idéntica: ${revisados} textos extraídos revisados contra ${corpus.length} textos del catálogo (base ${base.slice(0, 8)})`);
  for (const e of exceptuados) console.log(`  excepción declarada: ${e}`);
  if (faltan.length) {
    console.log(`FALTAN ${faltan.length} (salieron del código y no están tal cual en el catálogo):`);
    for (const f of [...new Set(faltan)]) console.log("  " + f);
    process.exit(1);
  }
  console.log("OK: todo texto que salió del código está tal cual en el catálogo.");
}

void main();
