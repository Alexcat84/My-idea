// AUD-09 M30 (tanda 7A, dinero): ?entrevista=1 nunca salía de la URL. Tras un
// cierre honesto (sin plan), recargar arrancaba OTRA exploración y gastaba un
// arranque del día sin que el usuario lo pidiera. La regla: el parámetro se
// CONSUME en el momento en que dispara el arranque automático.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { urlSinParametro } from "@/lib/urlSinParametro";

const fuente = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");

describe("?entrevista=1 se consume al arrancar (AUD-09 M30)", () => {
  it("urlSinParametro quita solo esa clave y conserva las demás", () => {
    expect(urlSinParametro("/idea/p1", "entrevista=1", "entrevista")).toBe("/idea/p1");
    expect(urlSinParametro("/idea/p1", "entrevista=1&vista=manos", "entrevista")).toBe("/idea/p1?vista=manos");
    expect(urlSinParametro("/idea/p1", "vista=manos", "entrevista")).toBe("/idea/p1?vista=manos");
  });

  it("IdeaView reemplaza la URL ANTES de pedir el arranque", () => {
    const rama = fuente.match(/else if \(quiereEntrevista && !d\.plan\) \{[\s\S]*?fetch\("\/api\/session\/start"/)?.[0] ?? "";
    expect(rama).toMatch(/router\.replace\(urlSinParametro\(/);
  });
});
