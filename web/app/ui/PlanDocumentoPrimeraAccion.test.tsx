// Decisión del fundador (26 sep 2026): la acción de cada etapa se rotula
// "Primera acción" (sin fecha). Los planes guardados con "**Esta semana:**" no
// se regeneran: se MUESTRAN con el rótulo nuevo, en el idioma del documento.
// Lo esperado sale del catálogo: PLAN_DOCUMENTO.es.primeraAccion = "Primera
// acción", PLAN_DOCUMENTO.ko.primeraAccion = "첫 실행 항목".
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { PLAN_DOCUMENTO } from "@/lib/i18n/mensajes/planDocumento";
import { PlanDocumento } from "./PlanDocumento";

const plan = (rotulo: string) =>
  ["# Plan", "", "## Etapa 1: Valida", "", "**Pasos:**", "1. Llama a Ana.", "", `${rotulo} Pregúntale cuánto pagaría.`].join("\n");

function pintar(md: string, idiomaDocumento?: "es" | "ko") {
  return renderToStaticMarkup(
    <IdiomaProvider idioma="es">
      <PlanDocumento md={md} nombreIdea="Pan" idiomaDocumento={idiomaDocumento} />
    </IdiomaProvider>
  );
}

describe("PlanDocumento: la acción de la etapa se rotula Primera acción", () => {
  it("un plan viejo con **Esta semana:** se ve igual que uno nuevo, sin 'Esta semana'", () => {
    const viejo = pintar(plan("**Esta semana:**"));
    const nuevo = pintar(plan("**Primera acción:**"));
    expect(viejo).toBe(nuevo);
    expect(viejo).toContain(`>${PLAN_DOCUMENTO.es.primeraAccion}<`);
    expect(viejo).not.toContain("Esta semana");
    expect(viejo).toContain("Pregúntale cuánto pagaría.");
  });

  it("en el idioma del documento (coreano), el rótulo del catálogo", () => {
    const html = pintar(plan("**Esta semana:**"), "ko");
    expect(html).toContain(`>${PLAN_DOCUMENTO.ko.primeraAccion}<`);
    expect(html).not.toContain(PLAN_DOCUMENTO.ko.estaSemana);
  });
});
