// NINGUNA CAUSA INVENTADA (decision del fundador, corrida final, 8 oct 2026; juez de fidelidad, docs/coherencia/2026-10-08/fidelidad.md).
// El plan del nucleo de la persona dos_empleados escribio: «Eso suele pasar cuando las expectativas no están dichas con
// claridad y cuando enseñar un puesto cuesta más que hacerlo uno mismo.» La primera causa la dijo ella ("no les explico
// cómo quiero que lo hagan"); la segunda no la dijo nadie ni la da ningun nodo: invencion sostenida por el arbitro.
// Regla: ningun redactor afirma CAUSAS de la situacion de la persona (por que le pasa algo) que no haya dicho ella ni den
// sus nodos o su material. El consejo practico de la casa (como hacer algo) sigue permitido.
// Aplica a TODO redactor que escribe para la persona: el plan (y su seguimiento, que usa el mismo redactor), el
// diagnostico de mundo, los caminos del replanteamiento, la Claridad del organizador y el reporte de numeros.
import { describe, expect, it } from "vitest";
import PROMPTS from "./assets/prompts.json";

const REDACTORES = ["SYSTEM_PLAN", "SYSTEM_DIAGNOSTICO_MUNDO", "SYSTEM_CAMINOS", "SYSTEM_ORGANIZADOR", "SYSTEM_REPORTE"] as const;
const P = PROMPTS as Record<string, string>;

describe("ningun redactor afirma causas que nadie dio", () => {
  it.each(REDACTORES)("%s lleva la regla", (nombre) => {
    expect(P[nombre]).toContain("NINGUNA CAUSA INVENTADA");
    expect(P[nombre]).toMatch(/no afirmes CAUSAS de la situacion de la persona/);
    // el consejo practico sigue permitido
    expect(P[nombre]).toMatch(/El consejo practico[^.]*sigue permitido/);
  });

  it.each(REDACTORES)("%s trae el caso real como lo que NO se escribe", (nombre) => {
    expect(P[nombre]).toContain("cuando enseñar un puesto cuesta más que hacerlo uno mismo");
  });

  it("la regla es UNA sola: el mismo texto en todos (una fuente, no copias que divergen)", () => {
    const bloque = (t: string) => t.slice(t.indexOf("NINGUNA CAUSA INVENTADA"), t.indexOf("NINGUNA CAUSA INVENTADA") + 600);
    const textos = new Set(REDACTORES.map((n) => bloque(P[n])));
    expect(textos.size).toBe(1);
  });
});
