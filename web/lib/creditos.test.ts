// ETAPA 2 — la logica PURA de la capa de creditos: la regla de concepto del
// plan (actualizada por la 4.5: el plan de mundo cobra mundo_activar a la
// entrega, el preview fue gratis), los montos desde precios.ts (jamas
// hardcodeados) y el 402 en palabras de persona. Las RPC (consumo atomico,
// idempotencia, cortesia unica, refund) se verifican EN VIVO en el vuelo de
// dinero (scripts/vuelo_beta.ts), no aqui: mockear un ledger seria fingir.
import { describe, expect, it } from "vitest";
import { conceptoDelPlan, mensajeSaldoInsuficiente, montoDelPlan, CORTESIA_BETA } from "./creditos";
import { esInvitadoInvisible } from "./identidad";
import { PRECIOS } from "./precios";

describe("conceptoDelPlan / montoDelPlan: la regla de concepto (§5 + 4.5)", () => {
  it("core inicial -> plan_completo (5)", () => {
    expect(conceptoDelPlan("core", false)).toBe("plan_completo");
    expect(montoDelPlan("core", false)).toBe(PRECIOS.plan_completo);
    expect(montoDelPlan("core", false)).toBe(5);
  });
  it("core seguimiento -> seguimiento (2)", () => {
    expect(conceptoDelPlan("core", true)).toBe("seguimiento");
    expect(montoDelPlan("core", true)).toBe(2);
  });
  it("mundo inicial -> mundo_activar (3): el preview fue gratis, el PLAN se compra", () => {
    expect(conceptoDelPlan("quality", false)).toBe("mundo_activar");
    expect(montoDelPlan("quality", false)).toBe(3);
  });
  it("mundo seguimiento -> mundo_seguimiento (2)", () => {
    expect(conceptoDelPlan("risk_management", true)).toBe("mundo_seguimiento");
    expect(montoDelPlan("risk_management", true)).toBe(2);
  });
});

describe("la cortesia y el 402", () => {
  it("la cortesia de beta es 20", () => {
    expect(CORTESIA_BETA).toBe(20);
  });
  it("el 402 habla en palabras de persona y no pierde el trabajo", () => {
    const m = mensajeSaldoInsuficiente(3, 5);
    expect(m).toBe("Te quedan 3 créditos; esto cuesta 5. Tu trabajo queda guardado tal como está.");
    expect(mensajeSaldoInsuficiente(1, 2)).toContain("1 crédito;"); // singular
  });
});

describe("esInvitadoInvisible: la frontera", () => {
  it("anonimo de Supabase -> invisible", () => {
    expect(esInvitadoInvisible({ is_anonymous: true, email: undefined })).toBe(true);
  });
  it("invitado de respaldo (@invitado.my-idea.local) -> invisible", () => {
    expect(esInvitadoInvisible({ is_anonymous: false, email: "visitante-x@invitado.my-idea.local" })).toBe(true);
  });
  it("cuenta real con correo -> NO invisible", () => {
    expect(esInvitadoInvisible({ is_anonymous: false, email: "fundador@gmail.com" })).toBe(false);
  });
  it("sin usuario -> invisible (nunca dejar pasar un null)", () => {
    expect(esInvitadoInvisible(null)).toBe(true);
  });
});
