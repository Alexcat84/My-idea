// Scheduler Inteligente, Fase 1: pruebas de la estimación por mayoría-de-3.
// El voto y el parser son puros (cálculo a mano en el comentario antes del
// assert, regla AGENTS.md). estimarLoteMayoria se prueba con un cliente falso
// (cero red): camino feliz, degradación a mayoría-de-2, y el FALLBACK (todas
// las corridas caen → todo null, sin lanzar, el plan jamás se bloquea).
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";
import {
  construirUserText,
  estimarLoteMayoria,
  parsearLote,
  rangoDeBanda,
  votoMayoriaBanda,
  votoMayoriaEspera,
} from "./estimacion";
import { usoVacio } from "../costmeter";

describe("votoMayoriaBanda: mayoría, empate → la banda mayor (conservador)", () => {
  it("mayoría clara: XL/M/M → M (M tiene 2 de 3)", () => {
    expect(votoMayoriaBanda(["XL", "M", "M"])).toBe("M");
  });

  it("mayoría clara: S/S/L → S", () => {
    expect(votoMayoriaBanda(["S", "S", "L"])).toBe("S");
  });

  it("empate de dos → la MAYOR: [S,M] → M", () => {
    // dos bandas, una cada una: empate → la mayor de las empatadas = M
    expect(votoMayoriaBanda(["S", "M"])).toBe("M");
  });

  it("empate a tres distintas → la MAYOR: [S,L,M] → L", () => {
    // 1/1/1: todas empatadas → la mayor = L
    expect(votoMayoriaBanda(["S", "L", "M"])).toBe("L");
  });

  it("empate arriba: [M,XL,XL,M] → XL (empate 2-2 → la mayor)", () => {
    expect(votoMayoriaBanda(["M", "XL", "XL", "M"])).toBe("XL");
  });

  it("sin votos → null", () => {
    expect(votoMayoriaBanda([])).toBeNull();
  });
});

describe("votoMayoriaEspera: mayoría; empate → true (conservador)", () => {
  it("mayoría false: [true,false,false] → false", () => {
    expect(votoMayoriaEspera([true, false, false])).toBe(false);
  });

  it("mayoría true: [true,true,false] → true", () => {
    expect(votoMayoriaEspera([true, true, false])).toBe(true);
  });

  it("empate 1-1 → true (conservador)", () => {
    expect(votoMayoriaEspera([true, false])).toBe(true);
  });

  it("sin votos → false", () => {
    expect(votoMayoriaEspera([])).toBe(false);
  });
});

describe("parsearLote: robusto, no inventa", () => {
  it("array limpio", () => {
    const v = parsearLote('[{"id":0,"banda":"S","espera_externa":false},{"id":1,"banda":"XL","espera_externa":true}]');
    expect(v).toEqual([
      { id: 0, banda: "S", espera: false },
      { id: 1, banda: "XL", espera: true },
    ]);
  });

  it("envuelto en fences ```json y prosa alrededor", () => {
    const texto = 'Claro:\n```json\n[{"id":0,"banda":"M","espera_externa":true}]\n```\nlisto';
    expect(parsearLote(texto)).toEqual([{ id: 0, banda: "M", espera: true }]);
  });

  it("descarta entradas mal formadas (banda inválida, id no entero, sin banda)", () => {
    const v = parsearLote(
      '[{"id":0,"banda":"Z"},{"id":1.5,"banda":"S","espera_externa":false},{"id":2,"banda":"L","espera_externa":true},{"banda":"S"}]'
    );
    expect(v).toEqual([{ id: 2, banda: "L", espera: true }]);
  });

  it("espera_externa ausente o no booleana → false por defecto", () => {
    expect(parsearLote('[{"id":0,"banda":"S"}]')).toEqual([{ id: 0, banda: "S", espera: false }]);
  });

  it("sin array → []", () => {
    expect(parsearLote("no hay json aquí")).toEqual([]);
    expect(parsearLote('{"id":0,"banda":"S"}')).toEqual([]);
  });
});

describe("rangoDeBanda: rango honesto, sin horas inventadas", () => {
  it("mapea cada banda a su frontera del prompt validado", () => {
    expect(rangoDeBanda("S")).toBe("~1 h");
    expect(rangoDeBanda("M")).toBe("~2-4 h");
    expect(rangoDeBanda("L")).toBe("una jornada");
    expect(rangoDeBanda("XL")).toBe("varios días");
  });

  it("sin banda (plan viejo / estimación fallida) → null, cero invención", () => {
    expect(rangoDeBanda(null)).toBeNull();
    expect(rangoDeBanda(undefined)).toBeNull();
  });
});

// --- Cliente falso: cada corrida devuelve el texto en cola, o rechaza. ---
function clienteFalso(respuestas: Array<string | Error>): Anthropic {
  let i = 0;
  return {
    messages: {
      create: vi.fn(async () => {
        const r = respuestas[Math.min(i, respuestas.length - 1)];
        i += 1;
        if (r instanceof Error) throw r;
        return { usage: { input_tokens: 10, output_tokens: 20 }, content: [{ type: "text", text: r }] };
      }),
    },
  } as unknown as Anthropic;
}

describe("estimarLoteMayoria: mayoría-de-3 con red simulada", () => {
  const items = [{ texto: "Redactar el ICP", etapa: 1 }, { texto: "Enviar correos y esperar", etapa: 2 }];

  it("camino feliz: 3 corridas concordantes → estimación por ítem", async () => {
    const resp = '[{"id":0,"banda":"M","espera_externa":false},{"id":1,"banda":"S","espera_externa":true}]';
    const { estimaciones } = await estimarLoteMayoria(clienteFalso([resp, resp, resp]), items, usoVacio());
    expect(estimaciones).toEqual([
      { banda: "M", espera_externa: false },
      { banda: "S", espera_externa: true },
    ]);
  });

  it("una corrida discrepa: [M,M,XL] para el ítem 0 → mayoría M", async () => {
    const c1 = '[{"id":0,"banda":"M","espera_externa":false},{"id":1,"banda":"S","espera_externa":true}]';
    const c2 = c1;
    const c3 = '[{"id":0,"banda":"XL","espera_externa":false},{"id":1,"banda":"S","espera_externa":true}]';
    const { estimaciones } = await estimarLoteMayoria(clienteFalso([c1, c2, c3]), items, usoVacio());
    expect(estimaciones[0]).toEqual({ banda: "M", espera_externa: false });
  });

  it("degradación a mayoría-de-2: 2 corridas válidas + 1 caída → sí estima", async () => {
    const ok = '[{"id":0,"banda":"L","espera_externa":false},{"id":1,"banda":"S","espera_externa":false}]';
    const { estimaciones } = await estimarLoteMayoria(
      clienteFalso([ok, new Error("red caída"), ok]),
      items,
      usoVacio()
    );
    // 2 votos por ítem (>= MIN_VOTOS) → estima
    expect(estimaciones[0]).toEqual({ banda: "L", espera_externa: false });
    expect(estimaciones[1]).toEqual({ banda: "S", espera_externa: false });
  });

  it("una sola corrida válida (< MIN_VOTOS) → null, no inventa con un voto", async () => {
    const ok = '[{"id":0,"banda":"L","espera_externa":false},{"id":1,"banda":"S","espera_externa":false}]';
    const { estimaciones } = await estimarLoteMayoria(
      clienteFalso([new Error("caída"), new Error("caída"), ok]),
      items,
      usoVacio()
    );
    expect(estimaciones).toEqual([null, null]);
  });

  it("FALLBACK: todas las corridas caen → todo null, sin lanzar (el plan jamás se bloquea)", async () => {
    const { estimaciones, acumulado } = await estimarLoteMayoria(
      clienteFalso([new Error("x"), new Error("x"), new Error("x")]),
      items,
      usoVacio()
    );
    expect(estimaciones).toEqual([null, null]);
    // acumulado intacto: nada que cobrar si nada respondió
    expect(acumulado).toEqual(usoVacio());
  });

  it("lista vacía → sin llamadas, sin costo", async () => {
    const c = clienteFalso(["[]"]);
    const { estimaciones } = await estimarLoteMayoria(c, [], usoVacio());
    expect(estimaciones).toEqual([]);
    expect((c.messages.create as ReturnType<typeof vi.fn>)).not.toHaveBeenCalled();
  });
});

describe("construirUserText: la lista con id por índice", () => {
  it("incluye cada tarea con su id y etapa", () => {
    const t = construirUserText([{ texto: "A", etapa: 1 }, { texto: "B" }]);
    expect(t).toContain('{"id":0,"tarea":"A","etapa":1}');
    expect(t).toContain('{"id":1,"tarea":"B","etapa":null}');
  });
});
