// AUD-09 H09: "Cargando tu espacio…" podía no terminar nunca. IdeaView exigía
// plan y checklist y, si faltaba cualquiera, pintaba el placeholder sin salida;
// el fallo de /checklist se tragaba en silencio. Camino reproducible: invitado
// en Claridad, Tus Números, login, vuelta a ?vista=manos SIN plan.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { estadoEspacio } from "./esperaEspacio";

describe("estadoEspacio: toda espera del espacio tiene salida", () => {
  it("sin plan no hay nada que cargar: se va a la vista de la idea", () => {
    expect(estadoEspacio({ hayPlan: false, hayChecklist: false, errorChecklist: null })).toBe("sin_plan");
  });
  it("si /checklist falló, se dice y se ofrece reintentar", () => {
    expect(estadoEspacio({ hayPlan: true, hayChecklist: false, errorChecklist: "no pudimos cargar" })).toBe("error");
  });
  it("con plan y el checklist en camino, espera", () => {
    expect(estadoEspacio({ hayPlan: true, hayChecklist: false, errorChecklist: null })).toBe("cargando");
  });
  it("con los dos, listo", () => {
    expect(estadoEspacio({ hayPlan: true, hayChecklist: true, errorChecklist: null })).toBe("listo");
  });
});

describe("IdeaView usa la regla y no se traga el fallo del checklist", () => {
  const f = readFileSync(path.join(__dirname, "..", "app", "idea", "[id]", "IdeaView.tsx"), "utf8");
  it("decide la espera con estadoEspacio", () => {
    expect(f).toMatch(/estadoEspacio\(/);
  });
  it("el fallo de /checklist deja un mensaje, no un comentario", () => {
    expect(f).not.toMatch(/el checklist es progresivo: sin él, la vista Manos avisa sola/);
    expect(f).toMatch(/setErrorChecklist\(/);
  });
});
