// AUD-09 (tanda 5, barrido de precios viejos): AGENTS.md, "los precios viven en
// precios.ts; nada más los define (ni canon, ni comentarios)". Un comentario o
// un documento que contradice precios.ts no es una segunda opinión: es un bug.
// La AUD-09 encontró cifras de antes del "Catálogo congruente" (plan 5,
// seguimientos 2, mundo 3, Tus Números 2, cortesía 20) vivas como afirmaciones
// actuales. La historia ("era 2 créditos", "antes decía") se queda: esta
// guardiana solo prohíbe las frases que las afirman como vigentes.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { PRECIOS } from "./precios";

const raiz = path.join(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(raiz, rel), "utf8");

const PROHIBIDAS: Array<[string, RegExp]> = [
  ["web/app/api/project/[id]/follow/route.ts", /2 creditos, TANTO|seguimiento: 2,|"2 core \/ 2 mundo"/],
  ["web/app/api/project/[id]/numeros/route.ts", /tus_numeros \(2\)/],
  ["web/app/api/session/start/route.ts", /plan_completo \(5\)/],
  ["web/app/api/session/[id]/plan/route.ts", /PAGADO \(5 creditos\)|core inicial 5|core 5, seguimiento 2/],
  ["web/lib/creditos.ts", /La cortesía \(20\) se otorga UNA vez/],
  ["web/lib/engine/reeleccionPuerta.ts", /pagado 3 créditos/],
  ["docs/FLUJO_TRACKING.md", /es el precio \(2 créditos|Plan core \(La Exploración\): \*\*5\*\*|Activar un mundo: \*\*3\*\*|Tus Números: 2, UNA VEZ|2 créditos \(core\) \/ 2 \(mundo\)|cuesta \*\*2 créditos, tanto/],
  ["docs/diseno-canon/REGLAS_Y_TOKENS.md", /\| 5 créditos \| \$4\.99 \| tu plan completo|Cortesía de la beta: 20|La Exploración 5, plan de un mundo/],
  ["docs/PREVIEW_MUNDOS_PLAN.md", /[^0-9]3 créditos/],
  ["docs/ANALISIS_PRECIOS.md", /7 dominios complementarios/],
  ["docs/BANCO_DE_TEXTOS.md", /Los 7 mundos|Las 5 etapas|pagará 5\s+créditos/],
];

describe("ninguna afirmación vigente contradice precios.ts", () => {
  it("las cifras de precios.ts son las del Catálogo congruente", () => {
    expect(PRECIOS).toMatchObject({ plan_completo: 10, seguimiento: 5, mundo_activar: 5, mundo_seguimiento: 5, tus_numeros: 0 });
  });
  for (const [rel, patron] of PROHIBIDAS) {
    it(rel, () => {
      expect(leer(rel)).not.toMatch(patron);
    });
  }
});
