// AUD-09 M04 (decisión del fundador, 25 sep 2026): EL ACTA DE CIERRE ES UNA FOTO.
// Hoy se recalculaba en vivo: cerrar con 19 de 24 y marcar tres más después
// hacía que el acta dijera 22 de 24. Ahora se guarda una instantánea al cerrar,
// el acta se pinta desde ella, y la vista en vivo se llama "estado actual".
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { informeMarkdown, type Analytics } from "./analytics";
import type { ActaCierre } from "./acta";
import { ANALISIS } from "./i18n/mensajes/analisis";

function analyticsCon(hechas: number, total: number): Analytics {
  return {
    universal: {
      accionesVigente: { hechas, total },
      accionesHechas: hechas,
      duracionTotalDias: 40,
      ritmoAccionesPorSemana: 3,
      rachaMasLargaDias: 4,
      ciclosDePlan: 1,
      mundos: 0,
      retiradas: [],
      duracionPorEtapa: [],
    },
    mundos: [],
    hitos: [],
    cumplimiento: null,
    cierreMotivo: null,
  } as unknown as Analytics;
}

describe("el acta de cierre sale de la instantánea, no del estado en vivo", () => {
  const acta: ActaCierre = {
    dominio: "core",
    cerrada_at: "2026-09-10T12:00:00.000Z",
    cierre_motivo: "ya vendo cada semana",
    instantanea: { acciones: { hechas: 19, total: 24 }, retiradas: 0, ciclos: 1, mundos: [] },
  };

  it("después del cierre el acta sigue diciendo lo del momento (19 de 24), aunque hoy haya 22", () => {
    const md = informeMarkdown("Macetas", analyticsCon(22, 24), "2026-09-10T12:00:00.000Z", (d) => d, acta);
    const i = md.indexOf("## Acta de cierre");
    const j = md.indexOf("\n## ", i + 1);
    const seccionActa = md.slice(i, j);
    // A MANO: 19 / 24 = 0,79 -> 79 %.
    expect(seccionActa).toContain("**19 de 24** (79%)");
    expect(seccionActa).not.toContain("22 de 24");
  });

  it("la vista en vivo se llama estado actual y lleva las cifras de hoy", () => {
    const md = informeMarkdown("Macetas", analyticsCon(22, 24), "2026-09-10T12:00:00.000Z", (d) => d, acta);
    expect(md).toContain("## Estado actual");
    expect(md).toMatch(/## Estado actual[\s\S]*22 de 24/);
  });

  it("la pantalla del análisis pinta el acta desde la instantánea", () => {
    const f = readFileSync(path.join(__dirname, "..", "app", "ui", "AnalisisProyecto.tsx"), "utf8");
    expect(f).toMatch(/acta\.instantanea\.acciones\.hechas/);
    // i18n F2: la frase vive en el catálogo; la pantalla la usa por su clave.
    expect(ANALISIS.es.proyecto.estadoActual).toBe("Estado actual");
    expect(ANALISIS.es.proyecto.estadoActualLinea).toContain("Estado actual");
    expect(f).toMatch(/\bt\.estadoActual\b/);
    expect(f).toMatch(/\bt\.estadoActualLinea\b/);
  });
});
