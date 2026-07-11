// Fase 3.5: evaluacionBrecha es determinística — mismos insumos, misma
// semilla, cero LLM. Esperados razonados A MANO sobre el asset real
// packs_entry_seeds.json (7 semillas por dominio, P1-HSEQ).
import { describe, expect, it } from "vitest";
import { evaluacionBrecha, semillasDelPack } from "./evaluacionBrecha";

describe("evaluacionBrecha (determinística, sin LLM)", () => {
  it("el asset horneado trae 7 semillas por dominio", () => {
    for (const pack of ["quality", "health_safety", "environmental"]) {
      expect(semillasDelPack(pack)).toHaveLength(7);
    }
  });

  it("mismos insumos -> misma semilla (determinismo)", () => {
    const a = evaluacionBrecha("quality", "vendo macetas y tengo quejas de piezas con burbujas", "producto_fisico", "ejecucion");
    const b = evaluacionBrecha("quality", "vendo macetas y tengo quejas de piezas con burbujas", "producto_fisico", "ejecucion");
    expect(a).not.toBeNull();
    expect(a!.semillaId).toBe(b!.semillaId);
  });

  it("la fase del proyecto inclina la elección (+5 misma fase)", () => {
    // Sin contexto de texto, gana una semilla cuya fase empata con la del
    // proyecto (todas las quality de fase 'ejecucion' puntúan 5; las demás
    // 0 o 3): el resultado debe tener fase == ejecucion.
    const r = evaluacionBrecha("quality", null, null, "ejecucion");
    const semilla = semillasDelPack("quality").find((s) => s.id === r!.semillaId)!;
    expect(semilla.fase).toBe("ejecucion");
  });

  it("excluye semillas ya cubiertas y devuelve null si no queda ninguna", () => {
    const todas = new Set(semillasDelPack("environmental").map((s) => s.id));
    expect(evaluacionBrecha("environmental", null, null, "ideacion", todas)).toBeNull();
    const casiTodas = new Set([...todas].slice(1));
    const r = evaluacionBrecha("environmental", null, null, "ideacion", casiTodas);
    expect(r!.semillaId).toBe([...todas][0]);
  });

  it("pack inexistente -> null", () => {
    expect(evaluacionBrecha("finanzas", null, null, "ideacion")).toBeNull();
  });
});
