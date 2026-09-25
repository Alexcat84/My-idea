// i18n F4 (DISENO §3.5): el árabe se lee de derecha a izquierda. Con
// <html dir="rtl">, las clases LÓGICAS de Tailwind (ms/me, ps/pe, start/end,
// text-start/end, rounded-s/e, border-s/e) se reflejan solas; las FÍSICAS
// (ml/mr, pl/pr, left/right, text-left/right, rounded-l/r, border-l/r) no.
// Esta guardia barre app/ y falla ante cualquier clase física. Única
// excepción: el centrado exacto (left-1/2 junto a -translate-x-1/2), que no
// depende de la dirección.
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const FISICA =
  /^(?:[^\s:]+:)*(-?(?:ml|mr|pl|pr)-\S+|-?(?:left|right)-\S+|rounded-(?:l|r|tl|tr|bl|br)(?:-\S+)?|border-(?:l|r)(?:-\S+)?|text-(?:left|right)|float-(?:left|right)|space-x-\S+)$/;
const CENTRADO = /^(?:[^\s:]+:)*left-1\/2$/;

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    return statSync(p).isDirectory() ? archivos(p) : p.endsWith(".tsx") && !p.includes(".test.") ? [p] : [];
  });
}

export function clasesFisicas(fuente: string): string[] {
  const fuera: string[] = [];
  for (const m of fuente.matchAll(/"([^"\n]*)"|`([^`]*)`|'([^'\n]*)'/g)) {
    const texto = m[1] ?? m[2] ?? m[3] ?? "";
    const tokens = texto.split(/\s+/);
    const centrado = tokens.some((t) => /-translate-x-1\/2$/.test(t));
    for (const t of tokens) if (FISICA.test(t) && !(centrado && CENTRADO.test(t))) fuera.push(t);
  }
  return fuera;
}

describe("dirección de lectura (F4, árabe)", () => {
  it("la guardia distingue física, lógica y centrado", () => {
    expect(clasesFisicas('className="ml-2 pr-3 text-left sm:left-0 rounded-l-lg"')).toEqual(["ml-2", "pr-3", "text-left", "sm:left-0", "rounded-l-lg"]);
    expect(clasesFisicas('className="ms-2 pe-3 text-start sm:start-0 rounded-s-lg"')).toEqual([]);
    expect(clasesFisicas('className="absolute left-1/2 -translate-x-1/2"')).toEqual([]);
    expect(clasesFisicas('"[&>li]:before:-left-[20px]"')).toEqual(["[&>li]:before:-left-[20px]"]);
  });
  it("ningún componente usa clases de dirección física", () => {
    const raiz = path.join(__dirname, "..", "..", "app");
    const hallazgos = archivos(raiz).flatMap((f) =>
      clasesFisicas(readFileSync(f, "utf8")).map((c) => `${path.relative(raiz, f)}: ${c}`)
    );
    expect(hallazgos).toEqual([]);
  });
});
