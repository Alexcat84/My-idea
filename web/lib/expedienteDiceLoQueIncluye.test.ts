// AUD-09 M35 (tanda 7B, confianza; decisión del fundador 25 sep 2026): el
// Expediente se presentaba como "Todo tu desarrollo", y el tablero vivo de Tus
// Números no entra en él. Regla del fundador: el texto no promete lo que falta;
// el Expediente dice exactamente lo que incluye. (Tus Números dentro del
// Expediente queda como función futura en la ficha.)
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { CLAVE_EXPEDIENTE, indiceDeDocumentos } from "./expediente";

const ciclo = { planId: "p1", etiqueta: "completo", createdAt: "2026-03-01T12:00:00Z", contenidoMd: "# Plan" };

describe("el Expediente dice lo que incluye (AUD-09 M35)", () => {
  it("en marcha", () => {
    const e = indiceDeDocumentos([ciclo] as never, null).find((d) => d.clave === CLAVE_EXPEDIENTE)!;
    expect(e.subtitulo).toBe("Tu idea, tu plan y sus ciclos, tu avance, cada mundo y tu bitácora, hasta hoy");
  });
  it("cerrado", () => {
    const e = indiceDeDocumentos([ciclo] as never, "2026-05-01T12:00:00Z").find((d) => d.clave === CLAVE_EXPEDIENTE)!;
    expect(e.subtitulo).toBe("Tu idea, tu plan y sus ciclos, tu avance, cada mundo y tu bitácora, de la idea al cierre");
  });
  it("/creditos no dice que reúne la idea 'entera'", () => {
    const creditos = readFileSync(path.join(__dirname, "..", "app", "creditos", "page.tsx"), "utf8");
    expect(creditos).not.toMatch(/tu idea entera/);
  });
});
