// AUD-09 M32 (tanda 7A, dinero): el canon 03 pone bajo "Explorar estas
// suposiciones" el aviso de precio de La Exploración, y la app no lo mostraba:
// el usuario empezaba sin saber lo que cuesta. La cifra sale de precios.ts (el
// "5" del mockup es errata de Design) y la frase dice CUÁNDO se cobra: al
// entregar el plan, y solo si se entrega.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { AVISO_PRECIO_EXPLORACION, avisoPrecioExploracion } from "./avisoExploracion";

const leer = (rel: string) => readFileSync(path.join(__dirname, "..", rel), "utf8");

describe("el aviso de precio antes de explorar (AUD-09 M32)", () => {
  it("dice el precio de precios.ts y cuándo se cobra", () => {
    // A MANO: PRECIOS.plan_completo = 10.
    expect(AVISO_PRECIO_EXPLORACION).toBe(
      "La Exploración usa 10 créditos, que se cobran solo cuando recibes tu plan. Tu Claridad es gratis y queda guardada para siempre."
    );
    // i18n F2: la versión por idioma da lo mismo en el base.
    expect(avisoPrecioExploracion("es")).toBe(AVISO_PRECIO_EXPLORACION);
  });

  it("los dos botones de explorar lo muestran", () => {
    for (const rel of ["app/nueva/page.tsx", "app/idea/[id]/IdeaView.tsx"]) {
      const src = leer(rel);
      // i18n F2: el botón usa la clave del catálogo de la Claridad, y el aviso
      // se pide en el idioma de la pantalla.
      const i = src.indexOf("{tc.explorarSuposiciones}");
      expect(i, rel).toBeGreaterThan(-1);
      expect(src.slice(i, i + 900), rel).toMatch(/\{avisoPrecioExploracion\(idioma\)\}/);
    }
  });
});
