/**
 * REGLA ESTRICTA del fundador (26 sep 2026), punto 4: la IA jamas nombra un libro ni cita a un autor como fuente en
 * lo que la persona lee. La regla viaja en TODA llamada a la IA como un bloque fijo de sistema (bloquesDeSistema),
 * y esta prueba exige que ninguna llamada se salte ese camino.
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { bloquesDeSistema } from "./i18n/idiomaSalida";
import { REGLA_SIN_FUENTES } from "./reglaSinFuentes";

const WEB = path.resolve(__dirname, "..");

describe("la IA no cita libros ni autores como fuente (fundador, 26 sep 2026)", () => {
  it("la regla prohibe el titulo del libro y el autor como fuente, y deja el concepto con nombre propio", () => {
    expect(REGLA_SIN_FUENTES).toMatch(/libro/);
    expect(REGLA_SIN_FUENTES).toMatch(/autor/);
    expect(REGLA_SIN_FUENTES).toMatch(/ciclo de Deming/);
  });

  it("toda llamada lleva la regla, en espanol y en cualquier otro idioma, sin tocar el prompt cacheado", () => {
    for (const idioma of ["es", "en", "ar", null]) {
      const b = bloquesDeSistema("PROMPT", idioma);
      expect(b[0]).toEqual({ type: "text", text: "PROMPT", cache_control: { type: "ephemeral" } });
      expect(b.some((x) => x.text === REGLA_SIN_FUENTES), String(idioma)).toBe(true);
    }
  });

  it("ninguna llamada a la IA arma su sistema sin bloquesDeSistema", () => {
    const fallos: string[] = [];
    const recorrer = (dir: string): void => {
      for (const e of readdirSync(dir)) {
        const p = path.join(dir, e);
        if (statSync(p).isDirectory()) recorrer(p);
        else if (/\.tsx?$/.test(e) && !/\.test\./.test(e)) {
          const src = readFileSync(p, "utf-8");
          for (const m of src.matchAll(/messages\.(create|stream)\(/g)) {
            const linea = src.slice(src.lastIndexOf("\n", m.index) + 1, m.index).trim();
            if (linea.startsWith("//") || linea.startsWith("*")) continue; // un comentario no llama a nadie
            const tramo = src.slice(m.index, m.index! + 600);
            if (!/system:\s*bloquesDeSistema\(/.test(tramo)) fallos.push(`${path.relative(WEB, p)}: ${m[0]}`);
          }
        }
      }
    };
    recorrer(path.join(WEB, "lib"));
    recorrer(path.join(WEB, "app"));
    expect(fallos).toEqual([]);
  });
});
