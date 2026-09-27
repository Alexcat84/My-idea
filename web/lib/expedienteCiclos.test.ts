// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026): en
// el Expediente cada ciclo posterior dice cuál fue (profundización o
// replanteamiento, numerados por tipo) y lleva lo que la persona contó al
// pedirlo, citado antes de su plan. Lo esperado sale del catálogo.
import { describe, expect, it } from "vitest";
import { cicloMarkdown, titulosDeCiclos, type CicloExpediente } from "./expediente";
import { interpolar } from "./i18n/interpolar";
import { EXPEDIENTE } from "./i18n/mensajes/expediente";

const t = EXPEDIENTE.es.ciclos;
const c = (planId: string, etiqueta: string, relato: string | null = null): CicloExpediente => ({
  planId,
  etiqueta,
  createdAt: "2026-09-01T12:00:00Z",
  contenidoMd: `# ${planId}`,
  relato,
});

describe("los ciclos del Expediente", () => {
  it("numera por tipo: Tu Plan, Profundización 1, Replanteamiento 1, Profundización 2", () => {
    const ts = titulosDeCiclos([c("p0", "completo"), c("p1", "seguimiento"), c("p2", "replanteamiento"), c("p3", "seguimiento")]);
    expect(ts.map((x) => x.titulo)).toEqual([
      t.tuPlan,
      interpolar(t.profundizacion, { n: 1 }),
      interpolar(t.replanteamiento, { n: 1 }),
      interpolar(t.profundizacion, { n: 2 }),
    ]);
    expect(ts[2].subtitulo).toBe(t.replanteamientoSubtitulo);
  });

  it("el relato va citado antes del plan; sin relato no hay línea", () => {
    const con = cicloMarkdown("Pan", "R1", c("p2", "replanteamiento", "Se cayó  el\nlocal."));
    expect(con).toContain(`> ${interpolar(t.relato, { relato: "Se cayó el local." })}`);
    expect(con.indexOf("> Lo que contaste")).toBeLessThan(con.indexOf("# p2"));
    expect(cicloMarkdown("Pan", "P1", c("p1", "seguimiento"))).not.toContain("> Lo que contaste");
  });
});
