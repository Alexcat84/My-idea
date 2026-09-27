// AUD-09 M39 (tanda 7B, confianza): el resumen "Cómo te fue" del Expediente en
// PDF decía SIEMPRE "Vas por buen camino" y, sin replanificaciones, "Mantuviste
// tu ritmo cerca de tu plan", también a mi ritmo (sin plan de fechas) o con todo
// tardío. El resumen habla con los datos, no con un veredicto fijo.
import { describe, expect, it } from "vitest";
import { resumenCaminoExpediente } from "./resumenExpediente";

const cumplimiento = (c: Partial<{ aTiempo: number; adelantadas: number; tardias: number; totalConFecha: number; replanificaciones: number; desviacionVsInicialDias: number }>) => ({
  aTiempo: 0, adelantadas: 0, tardias: 0, totalConFecha: 0, replanificaciones: 0, desviacionVsInicialDias: 0, ...c,
});

describe("resumenCaminoExpediente (AUD-09 M39)", () => {
  it("una idea abierta no recibe un veredicto", () => {
    expect(resumenCaminoExpediente({ cerrada: false, modo: "fechas", cumplimiento: null }).intro).toBe("Esto es lo que llevas hasta aquí.");
  });

  it("con todo tardío, no dice que mantuvo el ritmo: dice lo que pasó", () => {
    // A MANO: 4 acciones con fecha: 0 a tiempo, 0 antes, 4 después.
    const r = resumenCaminoExpediente({ cerrada: false, modo: "fechas", cumplimiento: cumplimiento({ tardias: 4, totalConFecha: 4 }) });
    expect(r.loQueMovio).toBe("De tus 4 acciones con fecha, 0 salieron a tiempo, 0 antes y 4 después de lo planeado.");
  });

  it("a mi ritmo no hay plan de fechas contra el cual medir", () => {
    expect(resumenCaminoExpediente({ cerrada: true, modo: "ritmo", cumplimiento: null }).loQueMovio).toBe(
      "Avanzaste a tu ritmo, sin fechas contra las cuales medirte."
    );
  });

  it("con fechas pero sin sellarlas, se dice", () => {
    expect(resumenCaminoExpediente({ cerrada: false, modo: "fechas", cumplimiento: null }).loQueMovio).toBe(
      "Aún no sellaste tus fechas, así que no hay un plan contra el cual medir tu ritmo."
    );
  });

  it("las replanificaciones se cuentan como antes", () => {
    // A MANO: 2 replanificaciones, +3.5 días de media frente al plan inicial.
    const r = resumenCaminoExpediente({ cerrada: true, modo: "fechas", cumplimiento: cumplimiento({ replanificaciones: 2, desviacionVsInicialDias: 3.5, totalConFecha: 5 }) });
    expect(r.intro).toBe("Empezaste con una idea y llegaste hasta el cierre. Esto es lo que dejó el camino.");
    expect(r.loQueMovio).toBe("Frente a tu plan inicial te moviste +3.5 días de media a lo largo de 2 replanificaciones. Ajustar el mapa fue parte del método.");
  });
});

import { readFileSync } from "node:fs";
import path from "node:path";

describe("la ruta de documentos usa el resumen honesto (AUD-09 M39)", () => {
  it("sin frases fijas", () => {
    const ruta = readFileSync(path.join(__dirname, "..", "app", "api", "project", "[id]", "documentos", "route.ts"), "utf8");
    expect(ruta).toMatch(/resumenCaminoExpediente\(/);
    expect(ruta).not.toMatch(/Vas por buen camino/);
    expect(ruta).not.toMatch(/Mantuviste tu ritmo cerca de tu plan/);
  });
});
