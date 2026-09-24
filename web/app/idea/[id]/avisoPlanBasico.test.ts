// AUD-09 H02: el servidor mandaba un evento "aviso" que consumirSSE ignoraba;
// quien recibía un plan armado sin IA no se enteraba. Hoy el done trae
// version_basica y el aviso, y la pantalla lo muestra junto al plan.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const fuente = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");

describe("el aviso del plan básico llega a la pantalla (AUD-09 H02)", () => {
  it("el done guarda el aviso que manda el servidor", () => {
    expect(fuente).toMatch(/setAvisoPlan\(d\.aviso \?\? null\)/);
  });
  it("el aviso se pinta junto al plan", () => {
    expect(fuente).toMatch(/\{avisoPlan && planMd && \(/);
  });
});

// Tras recargar, el aviso sigue: /api/idea lo deriva del evento que la ruta del
// plan deja en las decisiones de su sesión.
import { avisoDelPlan, AVISO_VERSION_BASICA } from "@/lib/engine/planRedactor";

const fuenteRuta = readFileSync(path.join(__dirname, "..", "..", "api", "idea", "[id]", "route.ts"), "utf8");

describe("el aviso del plan básico sobrevive a la recarga (AUD-09 H02)", () => {
  it("una sesión con el evento plan_version_basica da el aviso", () => {
    expect(avisoDelPlan([{ tipo: "decision_turno" }, { tipo: "plan_version_basica", motivo: "techo" }])).toBe(
      AVISO_VERSION_BASICA
    );
  });
  it("sin el evento, o sin decisiones, no hay aviso", () => {
    expect(avisoDelPlan([{ tipo: "decision_turno" }])).toBeNull();
    expect(avisoDelPlan(null)).toBeNull();
  });
  it("/api/idea entrega el aviso con el plan y la pantalla lo lee al cargar", () => {
    expect(fuenteRuta).toMatch(/aviso: avisoDelPlan\(/);
    expect(fuente).toMatch(/setAvisoPlan\(d\.plan\.aviso \?\? null\)/);
  });
});
