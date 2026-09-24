// AUD-09 M21 (tanda 5, fallas silenciosas): si la lectura del saldo fallaba, las
// tres superficies (el chip, /ideas y /creditos) mostraban "0 créditos". Un cero
// falso es una mentira sobre dinero. Lectura única: null con rastro si falla, 0
// solo si de verdad no hay cuenta.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it, vi } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { leerSaldo } from "./saldo";

const cliente = (r: { data: unknown; error: unknown }) =>
  ({ from: () => ({ select: () => ({ maybeSingle: async () => r }) }) }) as unknown as SupabaseClient;

describe("leerSaldo", () => {
  it("con cuenta devuelve su saldo", async () => {
    expect(await leerSaldo(cliente({ data: { creditos_total: 15 }, error: null }))).toBe(15);
  });
  it("sin cuenta de créditos, 0", async () => {
    expect(await leerSaldo(cliente({ data: null, error: null }))).toBe(0);
  });
  it("si la lectura falla, null y rastro en el log (nunca un 0 falso)", async () => {
    const errores = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(await leerSaldo(cliente({ data: null, error: { message: "no responde" } }))).toBeNull();
    expect(errores).toHaveBeenCalled();
    errores.mockRestore();
  });
});

describe("las tres superficies leen el saldo por la lectura única", () => {
  const app = path.join(__dirname, "..", "app");
  for (const rel of ["api/account/saldo/route.ts", "ideas/page.tsx", "creditos/page.tsx"]) {
    it(rel, () => {
      const f = readFileSync(path.join(app, rel), "utf8");
      expect(f).toMatch(/leerSaldo\(/);
      expect(f).not.toMatch(/creditos_total \?\? 0/);
    });
  }
});
