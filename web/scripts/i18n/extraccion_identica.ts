// i18n F2: la prueba de que la extracción no cambió ningún texto visible.
//
// Toma el diff del código (web/app, web/lib y web/proxy.ts, sin pruebas ni el
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
  if (limpia && !/[{}()=;<>"'`]/.test(limpia) && !/^(\/\/|\*|\/\*)/.test(limpia)) fuera.push(limpia);
  return fuera
    .map((t) => normal(t.replace(/\\n/g, " ").replace(/&nbsp;/g, " ")))
    .filter((t) => /[a-záéíóúñü]{2,}/i.test(t))
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
    ["diff", "-U0", base, "--", "app", "lib", "proxy.ts", ":(exclude)*.test.ts", ":(exclude)*.test.tsx", ":(exclude)lib/i18n"],
    { cwd: WEB, maxBuffer: 256 * 1024 * 1024 }
  ).toString();

  const faltan: string[] = [];
  let revisados = 0;
  for (const bloque of diff.split(/^diff --git /m).slice(1)) {
    const archivo = bloque.split("\n")[0].split(" b/")[1] ?? "?";
    const quitadas = bloque.split("\n").filter((l) => l.startsWith("-") && !l.startsWith("---")).map((l) => l.slice(1));
    const agregadas = normal(bloque.split("\n").filter((l) => l.startsWith("+") && !l.startsWith("+++")).map((l) => l.slice(1)).join(" "));
    for (const linea of quitadas) {
      for (const t of candidatos(linea)) {
        if (agregadas.includes(t)) continue; // se movió, no se extrajo
        revisados++;
        if (!estaEnCatalogo(t)) faltan.push(`${archivo}: "${t}"`);
      }
    }
  }
  console.log(`extracción idéntica: ${revisados} textos extraídos revisados contra ${corpus.length} textos del catálogo (base ${base.slice(0, 8)})`);
  if (faltan.length) {
    console.log(`FALTAN ${faltan.length} (salieron del código y no están tal cual en el catálogo):`);
    for (const f of [...new Set(faltan)]) console.log("  " + f);
    process.exit(1);
  }
  console.log("OK: todo texto que salió del código está tal cual en el catálogo.");
}

void main();
