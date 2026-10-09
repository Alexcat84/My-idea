// DATOS DEL NEGOCIO COMO PREGUNTA, NUNCA COMO HECHO (decision del fundador, corrida final, 8 oct 2026).
// El juez de fidelidad del vuelo sostuvo 9 invenciones; casi todas eran hechos sobre el negocio de la persona que la IA
// dio por sabidos (docs/coherencia/2026-10-08/fidelidad.md, tramo C). Regla: todo dato sobre el negocio que la persona
// no dio y que no viene de sus nodos se escribe como pregunta o comprobacion, nunca como hecho. Aplica a todo redactor
// que escribe para la persona. Las frases reales del informe van en la regla como lo que NO se escribe.
import { describe, expect, it } from "vitest";
import PROMPTS from "./assets/prompts.json";

const P = PROMPTS as Record<string, string>;
const REDACTORES = ["SYSTEM_PLAN", "SYSTEM_DIAGNOSTICO_MUNDO", "SYSTEM_CAMINOS", "SYSTEM_ORGANIZADOR", "SYSTEM_REPORTE"] as const;
const FRASES_REALES = [
  "un lote hecho con el mismo proceso suele salir más parejo",
  "porque ahí un defecto te cuesta más",
  "para ver en pesos cuánto te cuesta un mes sin ese canal",
  "El correo es la llave maestra: quien entra ahí puede recuperar tu Instagram",
  "porque no te dejan lo mismo",
  "Anota el nombre del cliente que más te ha recomendado",
];

describe("ningun redactor da por hecho un dato del negocio que nadie dio", () => {
  it.each(REDACTORES)("%s lleva la regla: pregunta o comprobacion, nunca hecho", (nombre) => {
    expect(P[nombre]).toContain("DATOS DEL NEGOCIO");
    expect(P[nombre]).toMatch(/se escribe como PREGUNTA o como COMPROBACION, nunca como hecho/);
  });

  it.each(REDACTORES)("%s trae las frases reales del informe como lo que NO se escribe", (nombre) => {
    for (const frase of FRASES_REALES) expect(P[nombre]).toContain(frase);
  });

  it.each(REDACTORES)("%s: la moneda solo la que nombro la persona", (nombre) => {
    expect(P[nombre]).toMatch(/moneda[^.]*solo la que la persona nombro/i);
  });

  it("es UNA sola regla: el mismo texto en todos", () => {
    const bloque = (t: string) => t.slice(t.indexOf("DATOS DEL NEGOCIO"), t.indexOf("DATOS DEL NEGOCIO") + 900);
    expect(new Set(REDACTORES.map((n) => bloque(P[n]))).size).toBe(1);
  });
});

describe("el interprete guarda la moneda tal como la dijo la persona", () => {
  it("el signo $ no se convierte en USD", () => {
    const sistema = P.SYSTEM_INTERPRETE_MULTI;
    expect(sistema).not.toContain('\\"unidad\\": \\"USD\\"');
    expect(sistema).not.toContain('"unidad": "USD"');
    expect(sistema).toMatch(/moneda tal como la dijo la persona/);
  });
});
