// AUD-09 M02 y M03 (tanda 5, conteos): el Expediente, el Reporte de un mundo y
// el Registro de protección leían las tareas de TODOS los ciclos, mientras el
// tablero cuenta solo el plan vigente. Con un seguimiento hecho, el tablero
// decía 3 de 25 y el Expediente "Completaste 22 de 53" y "22 de 25".
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { accionesDelCicloVigente } from "./expediente";

describe("accionesDelCicloVigente: por espacio, solo el último plan", () => {
  it("quita las tareas de los planes reemplazados, espacio por espacio", () => {
    const planes = [
      { id: "core-1", dominio: "core", etiqueta: "inicial", created_at: "2026-08-01T00:00:00Z" },
      { id: "core-2", dominio: null, etiqueta: "seguimiento", created_at: "2026-09-01T00:00:00Z" },
      { id: "calidad-1", dominio: "quality", etiqueta: "inicial", created_at: "2026-08-10T00:00:00Z" },
      { id: "org", dominio: "core", etiqueta: "organizador", created_at: "2026-09-10T00:00:00Z" },
    ];
    const acciones = [
      { plan_id: "core-1", dominio: "core", texto: "vieja" },
      { plan_id: "core-2", dominio: "core", texto: "vigente" },
      { plan_id: "calidad-1", dominio: "quality", texto: "del mundo" },
    ];
    // A MANO: núcleo -> el último plan de ciclo es core-2 (el organizador no es
    // un ciclo); calidad -> calidad-1. Queda "vigente" y "del mundo".
    expect(accionesDelCicloVigente(acciones, planes).map((a) => a.texto)).toEqual(["vigente", "del mundo"]);
  });
});

describe("los documentos cuentan el ciclo vigente", () => {
  const leer = (rel: string) => readFileSync(path.join(__dirname, "..", rel), "utf8");
  it("el Expediente, el Reporte de mundo y el Registro filtran por el ciclo vigente", () => {
    const f = leer("app/api/project/[id]/documentos/route.ts");
    expect((f.match(/accionesDelCicloVigente\(/g) ?? []).length).toBeGreaterThanOrEqual(3);
  });
  it("'Acciones completadas: X de N activas' sale del ciclo vigente en el informe y en el papel", () => {
    expect(leer("lib/analytics.ts")).not.toMatch(/\*\*\$\{u\.accionesHechas\}\*\* de \*\*\$\{u\.accionesVigente\.total\}\*\*/);
    expect(leer("app/api/project/[id]/documentos/route.ts")).not.toMatch(/accionesCumplidas: u\.accionesHechas/);
  });
});
