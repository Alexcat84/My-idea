// AUD-09 M12 (tanda 5, mezcla núcleo y mundos): una sola instancia de Manos a la
// Obra servía al núcleo y al hub de un mundo, sin `key`: "Ponerlas después",
// "Recalcular" y "cambiar modo" de un espacio aparecían en el otro. Cada espacio
// monta su propia instancia.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

describe("cada espacio monta su propio Manos a la Obra", () => {
  it("la instancia lleva la llave de su espacio", () => {
    const f = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");
    expect(f).toMatch(/<ManosALaObra\s+key=\{espacioActivo\}/);
  });
});

// AUD-09 M13: tras comprar o cerrar el plan de un mundo, el done ponía ese plan
// en `planMd`, que es el plan del NÚCLEO: la vista del núcleo lo mostraba como
// "Tu Plan" (título en Manos, etapas en el Análisis) hasta recargar.
describe("el plan de un mundo no ocupa el lugar del plan del núcleo", () => {
  const f = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");
  it("el done solo escribe planMd cuando el plan es del núcleo", () => {
    expect(f).toMatch(/if \(dominioPlan === "core"\) \{\s*setPlanMd\(d\.markdown\)/);
  });
  it("al entregarse el plan de un mundo, se recarga el plan del núcleo y se vuelve al mundo", () => {
    expect(f).toMatch(/async function volverAlMundo\(dominio: string\)/);
    expect(f).toMatch(/setPlanMd\(det\?\.plan\?\.contenido_md \?\? null\);[\s\S]{0,200}irAMundo\(dominio\)/);
  });
  it("el espacio del plan viaja como parámetro (no se lee del estado viejo)", () => {
    expect(f).toMatch(/generarPlan\(sid, undefined, \{ dominio, esSeguimiento: false \}\)/);
  });
});
