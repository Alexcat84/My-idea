// Fase 4.5: la logica pura del preview de los mundos. La maquina de estados
// del §4, el derecho a re-preview, y la frontera del §3 como guardia.
import { describe, expect, it } from "vitest";
import { estadoMundo, puedeRePreview, violacionesFronteraPreview } from "./previewMundos";

describe("estadoMundo: la maquina de cuatro estados (§4)", () => {
  it("sin plan core, TODO esta bloqueado (candado de secuencia), haya fila o no", () => {
    expect(estadoMundo(null, false)).toBe("bloqueado");
    expect(estadoMundo({ preview_at: "2026-07-18T10:00:00Z" }, false)).toBe("bloqueado");
    expect(estadoMundo({ plan_pagado_at: "2026-07-18T10:00:00Z" }, false)).toBe("bloqueado");
  });

  it("con plan core y sin fila: abierto (vitrina invitante)", () => {
    expect(estadoMundo(null, true)).toBe("abierto");
  });

  it("preview arrancado pero sin resumen todavia: sigue abierto (en curso)", () => {
    expect(estadoMundo({ preview_at: "2026-07-18T10:00:00Z", resumen_md: null }, true)).toBe("abierto");
  });

  it("con resumen persistido: diagnostico_listo (el estado protagonista)", () => {
    expect(
      estadoMundo({ preview_at: "2026-07-18T10:00:00Z", resumen_md: "## Lo que vi", resumen_at: "2026-07-18T10:12:00Z" }, true)
    ).toBe("diagnostico_listo");
  });

  it("con plan pagado: plan_comprado, gane a todo lo demas", () => {
    expect(
      estadoMundo(
        { preview_at: "2026-07-18T10:00:00Z", resumen_md: "x", resumen_at: "2026-07-18T10:12:00Z", plan_pagado_at: "2026-07-18T11:00:00Z" },
        true
      )
    ).toBe("plan_comprado");
  });

  it("unlock del modelo viejo (fila sin preview ni pago): abierto, no roto", () => {
    expect(estadoMundo({}, true)).toBe("abierto");
  });
});

describe("puedeRePreview: un preview por mundo, ciclo nuevo lo re-abre", () => {
  const conResumen = { resumen_at: "2026-07-10T10:00:00Z" };
  it("sin resumen: disponible", () => {
    expect(puedeRePreview(null, null)).toBe(true);
    expect(puedeRePreview({ resumen_at: null }, null)).toBe(true);
  });
  it("con resumen y sin plan core mas nuevo: NO se re-corre", () => {
    expect(puedeRePreview(conResumen, null)).toBe(false);
    expect(puedeRePreview(conResumen, "2026-07-09T10:00:00Z")).toBe(false);
  });
  it("plan core MAS NUEVO que el resumen: realidad nueva, mirada nueva", () => {
    expect(puedeRePreview(conResumen, "2026-07-15T10:00:00Z")).toBe(true);
  });
});

describe("violacionesFronteraPreview: diagnostico, jamas plan encubierto (§3)", () => {
  it("un diagnostico legitimo pasa limpio", () => {
    const resumen = [
      "## Lo que encontre en tu proyecto",
      "- Tu kit ya tiene tres ventas reales, pero nadie ha medido si el cliente vuelve.",
      "- No hay registro de quejas ni de garantias: la confianza hoy es intuicion.",
      "## Lo que un plan de Calidad y Confianza te estructuraria",
      "Un sistema simple para que el cliente confie, vuelva y te recomiende, con la medicion minima para saberlo.",
      "## Veredicto",
      "Este mundo encaja con tu momento: tienes clientes reales y cero medicion de su confianza.",
    ].join("\n");
    expect(violacionesFronteraPreview(resumen)).toEqual([]);
  });

  it('caza "Esta semana" (accion calendarizada)', () => {
    expect(violacionesFronteraPreview("Esta semana abre una hoja y registra cada queja.")).not.toEqual([]);
  });

  it('caza "Entregable" (estructura de plan)', () => {
    expect(violacionesFronteraPreview("**Entregable:** una tabla de seguimiento.")).not.toEqual([]);
  });

  it("caza etapas numeradas", () => {
    expect(violacionesFronteraPreview("## Etapa 1: mide la confianza")).not.toEqual([]);
    expect(violacionesFronteraPreview("En la etapa 2 vas a construir el registro.")).not.toEqual([]);
  });

  it("caza una lista de ejecucion (3+ items numerados)", () => {
    const md = "1. Abre una hoja\n2. Registra cada queja\n3. Llama al cliente";
    expect(violacionesFronteraPreview(md)).not.toEqual([]);
  });

  it("dos items numerados sueltos NO disparan (umbral conservador)", () => {
    expect(violacionesFronteraPreview("1. tema uno\n2. tema dos")).toEqual([]);
  });
});
