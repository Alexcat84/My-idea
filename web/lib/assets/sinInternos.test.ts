/**
 * NADA INTERNO LLEGA AL NAVEGADOR (decision del fundador del 27 sep 2026, punto 2; REGLA ESTRICTA del 26 sep):
 * los ficheros del grafo que se copian a web/ y todo lo que el navegador puede descargar no llevan la fuente de
 * un nodo, sus fuentes internas, sus correcciones, sus citas, ni titulos ni autores de libros. Las fuentes viven
 * solo en dataset/ (metadatos internos); scripts/sync_assets_web.py escribe aqui la VISTA WEB, sin ellas.
 *
 * Tres barreras:
 *   1. ninguna clave interna en ningun asset (a cualquier profundidad);
 *   2. ningun titulo de libro de la lista canonica (dataset/metadata/fuentes_canonicas.json) en ningun asset;
 *   3. ningun componente de cliente ("use client") alcanza por sus imports un asset de datos que no sea de
 *      cara al cliente: el grafo, las instrucciones de la IA y las listas curadas se quedan en el servidor.
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { titulosCanonicos, titulosEn } from "../testFixtures/fuentesCanonicas";

const WEB = path.resolve(__dirname, "../..");
const ASSETS = path.resolve(__dirname);

/** Las claves que solo existen en los metadatos internos. */
const CLAVES_INTERNAS = new Set([
  "fuente", "fuentes", "fuentes_internas", "correcciones", "merged_originals", "cita", "citas",
  "libro", "libros", "autor", "autores", "fichero", "frase", "texto_anterior",
]);

/** Los unicos assets de datos que un componente de cliente puede importar: copy de produccion. */
const ASSETS_DE_CLIENTE = new Set(["packs_catalog.json"]);

function clavesInternas(v: unknown, ruta: string, out: string[]): void {
  if (Array.isArray(v)) v.forEach((x, i) => clavesInternas(x, `${ruta}[${i}]`, out));
  else if (v && typeof v === "object") {
    for (const [k, x] of Object.entries(v)) {
      if (CLAVES_INTERNAS.has(k)) out.push(`${ruta}.${k}`);
      clavesInternas(x, `${ruta}.${k}`, out);
    }
  }
}

const assetsJson = readdirSync(ASSETS).filter((f) => f.endsWith(".json"));

describe("nada interno llega al navegador (fundador, 27 sep 2026)", () => {
  it("ningun asset lleva una clave interna (fuente, fuentes_internas, correcciones, citas, libros, autores)", () => {
    const fallos: string[] = [];
    for (const f of assetsJson) {
      const out: string[] = [];
      clavesInternas(JSON.parse(readFileSync(path.join(ASSETS, f), "utf-8")), f, out);
      if (out.length) fallos.push(`${f}: ${out.length} claves internas, p. ej. ${out.slice(0, 3).join(", ")}`);
    }
    expect(fallos).toEqual([]);
  });

  it("ningun asset nombra un libro de la lista canonica", () => {
    const titulos = titulosCanonicos();
    expect(titulos.length).toBeGreaterThan(40);
    const fallos: string[] = [];
    for (const f of assetsJson) {
      const hallados = titulosEn(readFileSync(path.join(ASSETS, f), "utf-8"), titulos);
      if (hallados.length) fallos.push(`${f}: ${hallados.join(", ")}`);
    }
    expect(fallos).toEqual([]);
  });

  it("ningun componente de cliente importa el grafo, las instrucciones de la IA ni las listas curadas", () => {
    const fuentes = new Map<string, string>();
    const recorrer = (dir: string): void => {
      for (const e of readdirSync(dir)) {
        const p = path.join(dir, e);
        if (statSync(p).isDirectory()) recorrer(p);
        else if (/\.tsx?$/.test(e) && !/\.test\./.test(e)) fuentes.set(p, readFileSync(p, "utf-8"));
      }
    };
    for (const d of ["app", "lib", "components"]) if (existsSync(path.join(WEB, d))) recorrer(path.join(WEB, d));
    const resolver = (desde: string, spec: string): string | null => {
      const base = spec.startsWith("@/") ? path.join(WEB, spec.slice(2)) : spec.startsWith(".") ? path.resolve(path.dirname(desde), spec) : null;
      if (!base) return null;
      for (const ext of ["", ".ts", ".tsx", "/index.ts", "/index.tsx"]) {
        const c = base + ext;
        if (fuentes.has(c) || (c.endsWith(".json") && existsSync(c))) return c;
      }
      return null;
    };
    const IMPORT = /(?:^|\n)\s*(import|export)(\s+type)?\s[^'"]*?from\s+['"]([^'"]+)['"]|import\(\s*['"]([^'"]+)['"]\s*\)/g;
    const deps = (p: string): string[] => {
      const out: string[] = [];
      for (const m of (fuentes.get(p) ?? "").matchAll(IMPORT)) {
        if (m[2]) continue; // import type: no llega al paquete
        const r = resolver(p, m[3] ?? m[4]);
        if (r) out.push(r);
      }
      return out;
    };
    const clientes = [...fuentes.entries()].filter(([, s]) => /^\s*(\/\*[\s\S]*?\*\/\s*)?["']use client["']/.test(s)).map(([p]) => p);
    expect(clientes.length).toBeGreaterThan(10);
    const fallos = new Set<string>();
    for (const c of clientes) {
      const visto = new Set<string>();
      const pila: Array<[string, string[]]> = [[c, [c]]];
      while (pila.length) {
        const [p, camino] = pila.pop()!;
        if (visto.has(p)) continue;
        visto.add(p);
        if (p.endsWith(".json")) {
          if (path.dirname(p) === ASSETS && !ASSETS_DE_CLIENTE.has(path.basename(p))) {
            fallos.add(camino.map((x) => path.relative(WEB, x)).join(" > "));
          }
          continue;
        }
        for (const d of deps(p)) pila.push([d, [...camino, d]]);
      }
    }
    expect([...fallos].slice(0, 5), `${fallos.size} caminos de un componente de cliente a un asset interno`).toEqual([]);
  });

  it("caso negativo: las barreras detectan una clave interna y un titulo", () => {
    const out: string[] = [];
    clavesInternas({ nodos: { x: { fuente: "The Lean Startup - Eric Ries" } } }, "falso", out);
    expect(out).toEqual(["falso.nodos.x.fuente"]);
    expect(titulosEn("como dice The Lean Startup, valida", titulosCanonicos())).toEqual(["the lean startup"]);
  });
});
