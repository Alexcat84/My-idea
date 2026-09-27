// Decisiones del fundador sobre la acción de cada etapa:
//  - 26 sep 2026: la acción de cada etapa se rotula "Primera acción" (sin fecha).
//  - 27 sep 2026: en Manos a la Obra, el rótulo Y EL CONTENIDO de "Esta semana"
//    DESAPARECEN de la vista del plan (el entregable), también en los planes ya
//    guardados, sin regenerarlos: ahí ya no aplica, porque cada paso tiene su
//    "Primera acción". Solo queda el bloque único de arriba de Manos a la Obra,
//    calculado por la app. Lo mismo para "El lunes que viene", la acción con
//    plazo de la sección de números de los planes viejos.
// Lo esperado sale del catálogo: PLAN_DOCUMENTO.es.primeraAccion = "Primera acción".
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES, type ActiveLocale } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { PLAN_DOCUMENTO } from "@/lib/i18n/mensajes/planDocumento";
import { PlanDocumento } from "./PlanDocumento";

const ACCION = "Pregúntale cuánto pagaría.";
const plan = (rotulo: string) =>
  ["# Plan", "", "## Etapa 1: Valida", "", "**Pasos:**", "1. Llama a Ana.", "", `${rotulo} ${ACCION}`].join("\n");

function pintar(md: string, idiomaDocumento?: ActiveLocale) {
  return renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <PlanDocumento md={md} nombreIdea="Pan" idiomaDocumento={idiomaDocumento} />
    </IdiomaProvider>
  );
}

describe("PlanDocumento: la Primera acción de los planes nuevos se muestra", () => {
  it("un plan nuevo lleva su Primera acción, con su rótulo", () => {
    const html = pintar(plan("**Primera acción:**"));
    expect(html).toContain(`>${PLAN_DOCUMENTO.es.primeraAccion}<`);
    expect(html).toContain(ACCION);
  });
});

describe("PlanDocumento: 'Esta semana' de un plan viejo desaparece (rótulo y contenido)", () => {
  it("el plan viejo no muestra el contenido de 'Esta semana' ni ningún recuadro de acción", () => {
    const html = pintar(plan("**Esta semana:**"));
    expect(html).not.toContain(ACCION);
    expect(html).not.toContain("Esta semana");
    expect(html).not.toContain(`>${PLAN_DOCUMENTO.es.primeraAccion}<`);
    // lo demás del plan sigue: la etapa y sus pasos
    expect(html).toContain("Llama a Ana.");
  });

  it("'El lunes que viene' de la sección de números de un plan viejo, tampoco", () => {
    const md = ["# Plan", "", "## ¿Puede sostenerse tu idea?", "", "- **Costo por ciclo:** $10", "", "**El lunes que viene:** Llama a tres proveedores."].join("\n");
    const html = pintar(md);
    expect(html).not.toContain("Llama a tres proveedores.");
  });

  it.each([...ACTIVE_LOCALES])("%s: el plan viejo no muestra 'Esta semana' en el idioma del documento", (idioma) => {
    const html = pintar(plan("**Esta semana:**"), idioma);
    expect(html).not.toContain(ACCION);
    expect(html).not.toContain(PLAN_DOCUMENTO[idioma].estaSemana);
  });
});
