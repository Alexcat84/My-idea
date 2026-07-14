// Fase 3.5: evaluacionBrecha es determinística — mismos insumos, misma
// semilla, cero LLM. Esperados razonados A MANO sobre el asset real
// packs_entry_seeds.json (7 semillas por dominio, P1-HSEQ).
import { describe, expect, it } from "vitest";
import { evaluacionBrecha, semillasDelPack } from "./evaluacionBrecha";

describe("evaluacionBrecha (determinística, sin LLM)", () => {
  it("el asset horneado trae las semillas aprobadas por dominio (7 mundos)", () => {
    for (const pack of ["quality", "health_safety", "environmental", "exportacion", "franquicias"]) {
      expect(semillasDelPack(pack)).toHaveLength(7);
    }
    // seguridad_digital: 6 semillas aprobadas (v1.3.2)
    expect(semillasDelPack("seguridad_digital")).toHaveLength(6);
    // risk_management: 8 semillas aprobadas (v1.4), 2 por cada fase del canon
    expect(semillasDelPack("risk_management")).toHaveLength(8);
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

  // Fase v1.3.2: los mundos nuevos entran por el mapeo aprobado fase→semilla
  // (brecha_semillas.json), no por puntaje. Los HSEQ no están en el mapa y
  // conservan el comportamiento de arriba.
  it("mundos nuevos: el mapeo aprobado manda (decisiones de producto)", () => {
    // Exportación: ideación Y validación entran por la misma pregunta honesta
    // (¿a qué mercado y por qué ese?).
    expect(evaluacionBrecha("exportacion", null, null, "ideacion")!.semillaId).toBe("evaluacion_mercados_objetivo");
    expect(evaluacionBrecha("exportacion", null, null, "validacion")!.semillaId).toBe("evaluacion_mercados_objetivo");
    // Franquicias: validación = probar que UNA funciona antes de multiplicar.
    expect(evaluacionBrecha("franquicias", null, null, "validacion")!.semillaId).toBe("leverage_una_sola_franquicia");
    // Seguridad digital: al que idea, fundamentos de gestión de riesgo.
    expect(evaluacionBrecha("seguridad_digital", null, null, "ideacion")!.semillaId).toBe("fundamentos_gestion_riesgo");
    // Alias del canon: planificacion/ejecucion (patch decía construccion/operacion).
    expect(evaluacionBrecha("seguridad_digital", null, null, "planificacion")!.semillaId).toBe("getting_started_planning");
    expect(evaluacionBrecha("exportacion", null, null, "ejecucion")!.semillaId).toBe("documentacion_exportacion_basica");
    // Riesgos Bajo Control (v1.4): una puerta honesta por fase del canon.
    expect(evaluacionBrecha("risk_management", null, null, "ideacion")!.semillaId).toBe("correr_hacia_el_riesgo");
    expect(evaluacionBrecha("risk_management", null, null, "validacion")!.semillaId).toBe("haz_tu_lista_de_lo_que_puede_fallar");
    // Alias construccion→planificacion y operacion→ejecucion, verificado contra la fase real del nodo.
    expect(evaluacionBrecha("risk_management", null, null, "planificacion")!.semillaId).toBe("cuatro_caminos_ante_un_riesgo");
    expect(evaluacionBrecha("risk_management", null, null, "ejecucion")!.semillaId).toBe("revisa_tus_riesgos_con_un_ritmo");
  });

  it("mundos nuevos: semilla mapeada ya cubierta -> cae al puntaje dinámico", () => {
    const r = evaluacionBrecha("franquicias", null, null, "validacion", new Set(["leverage_una_sola_franquicia"]));
    expect(r).not.toBeNull();
    expect(r!.semillaId).not.toBe("leverage_una_sola_franquicia");
    // el fallback es el puntaje clásico, no otro mapeo
    expect(r!.razonamiento).toContain("puntaje");
  });
});
