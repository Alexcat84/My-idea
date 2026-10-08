// FICHA DE MEMORIA: papel y "tiene jefe" (decision del fundador, corrida final, 8 oct 2026; requisito antes de la beta).
// La prueba de coherencia del 8 oct (docs/coherencia/2026-10-08/informe.md) fallo en los dos casos:
//  1. un DUEÑO quedo con papel 'desconocido' en toda la corrida (sola y dos_empleados, del nucleo a cada mundo);
//  2. una PERSONA SOLA (Marta: trabaja sola, sin empleados, socios ni jefe, y tiene aparte un trabajo de medio tiempo
//     en una tienda) quedo con tiene_jefe true desde Riesgos.
// Causas en el codigo: el contrato final del interprete ("Responde SOLO un JSON: {...}") no nombraba ficha_update, asi
// que el modelo casi nunca la mandaba; cuando la mandaba, "dueña"/"dueño" (con ñ, como se escribe) no era "dueno" y
// fusionarFicha la tiraba; y nada ataba "tiene jefe" al papel ni a ESTE proyecto (otro empleo no cuenta).
// Regla: dueno = dueña o fundadora de su negocio => en este proyecto no tiene jefe; empleado = trabaja para otro => si.
import { describe, expect, it } from "vitest";
import PROMPTS from "../assets/prompts.json";
import { fichaVacia, fusionarFicha, type FichaContexto } from "./memoria";

const parcial = (p: Record<string, unknown>) => p as unknown as Partial<FichaContexto>;

describe("caso 1: un dueño no puede quedar como 'desconocido'", () => {
  it("el contrato final del interprete pide ficha_update", () => {
    const sistema = (PROMPTS as Record<string, string>).SYSTEM_INTERPRETE_MULTI;
    const contrato = sistema.slice(sistema.lastIndexOf("Responde SOLO un JSON"));
    expect(contrato).toContain('"ficha_update"');
  });

  it.each([
    ["dueño", "dueno"],
    ["dueña", "dueno"],
    ["Dueña", "dueno"],
    ["duena", "dueno"],
    ["fundadora", "dueno"],
    ["fundador", "dueno"],
    ["propietario", "dueno"],
    ["empleada", "empleado"],
    ["Empleado", "empleado"],
    ["directiva", "directivo"],
  ])("papel '%s' se lee como '%s'", (dicho, esperado) => {
    expect(fusionarFicha(fichaVacia(), parcial({ papel: dicho })).papel).toBe(esperado);
  });

  it("un papel que no se reconoce no pisa el conocido", () => {
    const a = fusionarFicha(fichaVacia(), { papel: "dueno" });
    expect(fusionarFicha(a, parcial({ papel: "astronauta" })).papel).toBe("dueno");
  });

  it("tiene_jefe dicho como texto ('no', 'sí') tambien entra", () => {
    expect(fusionarFicha(fichaVacia(), parcial({ papel: "directivo", tiene_jefe: "sí" })).tiene_jefe).toBe(true);
    expect(fusionarFicha(fichaVacia(), parcial({ papel: "directivo", tiene_jefe: "no" })).tiene_jefe).toBe(false);
  });
});

describe("caso 2: una persona sola no puede quedar con jefe", () => {
  it("la dueña sola que ya estaba sin jefe no gana un jefe por mencionar su otro empleo", () => {
    const marta = fusionarFicha(fichaVacia(), parcial({ papel: "dueña", tiene_jefe: false, equipo: { personas: 1, descripcion: "trabaja sola" } }));
    expect(fusionarFicha(marta, { tiene_jefe: true }).tiene_jefe).toBe(false);
  });

  it("saber que es dueña basta para saber que en su negocio no tiene jefe", () => {
    expect(fusionarFicha(fichaVacia(), { papel: "dueno" }).tiene_jefe).toBe(false);
    expect(fusionarFicha(fichaVacia(), parcial({ papel: "dueña", tiene_jefe: true })).tiene_jefe).toBe(false);
  });

  it("quien trabaja para otro si tiene jefe", () => {
    expect(fusionarFicha(fichaVacia(), { papel: "empleado" }).tiene_jefe).toBe(true);
  });

  it("si de verdad cambia de papel, cambia el jefe con el", () => {
    const a = fusionarFicha(fichaVacia(), { papel: "dueno" });
    const b = fusionarFicha(a, { papel: "empleado" });
    expect(b).toMatchObject({ papel: "empleado", tiene_jefe: true });
  });

  it("el interprete sabe que el jefe es el de ESTE proyecto, no el de otro empleo", () => {
    const sistema = (PROMPTS as Record<string, string>).SYSTEM_INTERPRETE_MULTI;
    expect(sistema).toMatch(/tiene_jefe[^.]*ESTE proyecto/);
    expect(sistema).toMatch(/otro empleo[^.]*no cuenta/);
  });
});
