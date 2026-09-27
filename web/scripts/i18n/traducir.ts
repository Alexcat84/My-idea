/**
 * La herramienta de traducción de F3 (docs/i18n/F3_CONVENCIONES.md).
 *
 * Varios traductores trabajan a la vez, y cada catálogo es UN archivo que
 * recibe TODOS los idiomas: si cada uno editara los .ts, chocarían. Por eso el
 * traductor trabaja sobre JSON y esta herramienta lo valida y lo integra:
 *
 *   exportar <salida.json> <archivo.ts...>   el español (y el inglés, de apoyo)
 *                                            de esos catálogos, para traducir
 *   validar  <idioma> <entrada.json...>       mismas claves, {{marcadores}} y
 *                                            <etiquetas>, nada vacío, "My Idea",
 *                                            sin rayas ni ¿¡ (la voz)
 *   aplicar  <idioma> <entrada.json...>       escribe `const <idioma>…: typeof es…`
 *                                            en cada catálogo y lo suma al export
 *
 * Formato de la traducción: { "archivo.ts": { "EXPORT": { …el objeto… } } }.
 * Uso (desde web/): npx tsx scripts/i18n/traducir.ts validar fr /ruta/fr_1.json
 */
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { compararTraduccion } from "../../lib/i18n/auditor";
import { LOCALES } from "../../lib/i18n/config";

const DIR = path.join(__dirname, "..", "..", "lib", "i18n", "mensajes");
type Traduccion = Record<string, Record<string, unknown>>;

async function catalogosDe(archivo: string): Promise<Record<string, Record<string, unknown>>> {
  const mod = (await import(pathToFileURL(path.join(DIR, archivo)).href)) as Record<string, unknown>;
  const fuera: Record<string, Record<string, unknown>> = {};
  for (const [nombre, valor] of Object.entries(mod))
    if (valor && typeof valor === "object" && "es" in (valor as object)) fuera[nombre] = valor as Record<string, unknown>;
  return fuera;
}

function leer(rutas: string[]): Traduccion {
  const junta: Traduccion = {};
  for (const r of rutas) {
    const t = JSON.parse(readFileSync(r, "utf8")) as Traduccion;
    for (const [archivo, cats] of Object.entries(t)) junta[archivo] = { ...(junta[archivo] ?? {}), ...cats };
  }
  return junta;
}

function textos(x: unknown, fuera: string[] = []): string[] {
  if (typeof x === "string") fuera.push(x);
  else if (Array.isArray(x)) x.forEach((y) => textos(y, fuera));
  else if (x && typeof x === "object") Object.values(x).forEach((y) => textos(y, fuera));
  return fuera;
}

async function validar(idioma: string, t: Traduccion): Promise<string[]> {
  const fallas: string[] = [];
  for (const [archivo, cats] of Object.entries(t)) {
    const reales = await catalogosDe(archivo).catch(() => null);
    if (!reales) {
      fallas.push(`${archivo}: no existe en mensajes/`);
      continue;
    }
    for (const nombre of Object.keys(reales)) if (!(nombre in cats)) fallas.push(`${archivo}:${nombre}: falta el catálogo`);
    for (const [nombre, obj] of Object.entries(cats)) {
      const real = reales[nombre];
      if (!real) {
        fallas.push(`${archivo}:${nombre}: ese catálogo no existe`);
        continue;
      }
      fallas.push(...compararTraduccion(real.es, obj, `${archivo}:${nombre}`, idioma));
      for (const s of textos(obj)) {
        if (/[—–]/.test(s)) fallas.push(`${archivo}:${nombre} [${idioma}]: raya (— –) en "${s.slice(0, 60)}"`);
        if (/[¿¡]/.test(s)) fallas.push(`${archivo}:${nombre} [${idioma}]: ¿ o ¡ en "${s.slice(0, 60)}"`);
      }
    }
  }
  return fallas;
}

const ID = /^[A-Za-z_$][\w$]*$/;
function literal(x: unknown, sangria = ""): string {
  if (typeof x === "string") return JSON.stringify(x);
  const mas = sangria + "  ";
  if (Array.isArray(x)) {
    const corta = `[${x.map((y) => literal(y)).join(", ")}]`;
    if (corta.length <= 100 && x.every((y) => typeof y === "string")) return corta;
    return `[\n${x.map((y) => mas + literal(y, mas)).join(",\n")},\n${sangria}]`;
  }
  const obj = x as Record<string, unknown>;
  return `{\n${Object.entries(obj)
    .map(([k, v]) => `${mas}${ID.test(k) ? k : JSON.stringify(k)}: ${literal(v, mas)}`)
    .join(",\n")},\n${sangria}}`;
}

function aplicar(idioma: string, t: Traduccion) {
  for (const [archivo, cats] of Object.entries(t)) {
    const ruta = path.join(DIR, archivo);
    let fuente = readFileSync(ruta, "utf8");
    for (const [nombre, obj] of Object.entries(cats)) {
      const re = new RegExp(`^export const ${nombre}: PorIdioma<typeof (\\w+)> = \\{ ([^}]*) \\};$`, "m");
      const m = fuente.match(re);
      if (!m) throw new Error(`${archivo}: no encuentro el export de ${nombre}`);
      const [linea, varEs, lista] = m;
      if (new RegExp(`(^|, )${idioma}[,:]|(^|, )${idioma}$`).test(lista)) throw new Error(`${archivo}:${nombre}: ya tiene ${idioma}`);
      const varIdioma = idioma + varEs.slice(2);
      const nueva = `const ${varIdioma}: typeof ${varEs} = ${literal(obj)};\n\n${linea.replace(
        ` ${lista} }`,
        ` ${lista}, ${varEs === "es" ? idioma : `${idioma}: ${varIdioma}`} }`
      )}`;
      fuente = fuente.replace(linea, nueva);
    }
    writeFileSync(ruta, fuente);
  }
}

async function main() {
  const [orden, a, ...resto] = process.argv.slice(2);
  if (orden === "exportar") {
    const fuera: Record<string, Record<string, { es: unknown; en: unknown }>> = {};
    for (const archivo of resto) {
      fuera[archivo] = {};
      for (const [nombre, cat] of Object.entries(await catalogosDe(archivo))) fuera[archivo][nombre] = { es: cat.es, en: cat.en };
    }
    writeFileSync(a, JSON.stringify(fuera, null, 2));
    console.log(`exportados ${resto.length} archivos a ${a}`);
    return;
  }
  if (!(LOCALES as readonly string[]).includes(a) || a === "es") throw new Error(`idioma no válido: ${a}`);
  const t = leer(resto);
  const fallas = await validar(a, t);
  if (fallas.length) {
    console.log(`${fallas.length} FALLAS:\n` + fallas.map((f) => "  " + f).join("\n"));
    process.exit(1);
  }
  if (orden === "validar") return void console.log(`OK: ${Object.keys(t).length} archivos en ${a}, sin fallas`);
  if (orden === "aplicar") {
    aplicar(a, t);
    return void console.log(`aplicado ${a} en ${Object.keys(t).length} archivos`);
  }
  throw new Error(`orden desconocida: ${orden}`);
}

main().catch((e) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
