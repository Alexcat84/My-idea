// AUD-09 (tanda 5, fallas silenciosas; decisión del fundador 25 sep 2026):
// toda escritura que falla deja rastro. supabase-js NO lanza cuando una
// escritura falla: devuelve { error }. Una línea `await supabase.from(x)
// .update(...)` que descarta ese resultado pierde el error sin síntoma (así se
// perdían la bitácora, las fechas del ritual y "mover fecha", que además
// respondían "ok"). Esta guardiana barre las rutas y lib/.
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { registrarBitacora } from "./db";

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    if (statSync(p).isDirectory()) return n === "node_modules" || n === "testUtils" ? [] : archivos(p);
    return /\.ts$/.test(n) && !/\.test\.ts$/.test(n) ? [p] : [];
  });
}

const ESCRITURA_DESCARTADA =
  /(^|\n)[ \t]*await[ \t]+(supabase|admin)\s*\.from\(\s*["'][a-z_]+["']\s*\)\s*\.(update|insert|delete|upsert)\(/g;

describe("toda escritura a la base mira su resultado", () => {
  it("ninguna ruta ni módulo de lib/ descarta el { error } de una escritura", () => {
    const raiz = path.join(__dirname, "..");
    const hallazgos: string[] = [];
    for (const f of [...archivos(path.join(raiz, "app", "api")), ...archivos(path.join(raiz, "lib"))]) {
      const texto = readFileSync(f, "utf8");
      for (const m of texto.matchAll(ESCRITURA_DESCARTADA)) {
        const linea = texto.slice(0, m.index).split("\n").length + 1;
        hallazgos.push(`${path.relative(raiz, f)}:${linea}`);
      }
    }
    expect(hallazgos).toEqual([]);
  });
});

describe("registrarBitacora deja rastro si la escritura falla", () => {
  it("un error de la base se registra en el log (y no bloquea la acción)", async () => {
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    const supabase = {
      from: () => ({ insert: async () => ({ data: null, error: { message: "la tabla no responde" } }) }),
    } as unknown as SupabaseClient;
    await expect(registrarBitacora(supabase, "p1", "fecha_movida", {})).resolves.toBeUndefined();
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });
});
