// AUD-09 H01: el seguimiento anunciaba 10 créditos y cobraba 5. IdeaView
// entraba a toda sesión de seguimiento con dominio "core" y pintaba
// PRECIOS.plan_completo tecleado en los botones, mientras el servidor cobraba
// montoDelPlan(dominio, esSeguimiento). La regla: el precio en pantalla sale
// de la MISMA función que usa el cobro, según el espacio y el tipo de sesión.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { finDeEntrevista } from "@/lib/finDeEntrevista";

const fuente = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");

describe("el precio del fin de entrevista sale de la fuente única (AUD-09 H01)", () => {
  // Cálculo a mano contra web/lib/precios.ts (plan_completo 10, seguimiento 5,
  // mundo_activar 5, mundo_seguimiento 5):
  //   núcleo, primera entrevista  -> plan_completo       = 10
  //   núcleo, seguimiento         -> seguimiento         = 5
  //   mundo, preview              -> diagnóstico gratis  = 0 (el plan se compra aparte)
  //   mundo, seguimiento          -> mundo_seguimiento   = 5, y es PLAN, no diagnóstico
  it("núcleo, primera entrevista: plan de 10", () => {
    expect(finDeEntrevista("core", false)).toEqual({ esDiagnostico: false, costo: 10 });
  });
  it("núcleo, seguimiento: plan de 5", () => {
    expect(finDeEntrevista("core", true)).toEqual({ esDiagnostico: false, costo: 5 });
  });
  it("mundo, preview: diagnóstico gratis", () => {
    expect(finDeEntrevista("quality", false)).toEqual({ esDiagnostico: true, costo: 0 });
  });
  it("mundo, seguimiento: plan de 5, nunca un diagnóstico", () => {
    expect(finDeEntrevista("quality", true)).toEqual({ esDiagnostico: false, costo: 5 });
  });

  it("IdeaView no teclea el precio del plan en sus botones", () => {
    expect(fuente).not.toMatch(/PRECIOS\.plan_completo/);
  });

  it("IdeaView no fuerza el dominio 'core' al entrar a un seguimiento", () => {
    expect(fuente).not.toMatch(/onSeguimientoIniciado=\{\(data\) => entrarASesionNueva\(data as RespuestaTurno, "core"\)\}/);
  });
});
