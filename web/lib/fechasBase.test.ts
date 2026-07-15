// Fase 3.8 §4 — sugeridor determinístico. Regla AGENTS.md: cada fecha
// esperada se calcula A MANO en el comentario ANTES del assert; el assert
// sale del cálculo manual, jamás de correr la función.
//
// Anclaje de todos los casos: plan.created_at = "2026-03-02T10:00:00"
// (sin sufijo de zona → hora LOCAL). Calendario de marzo 2026:
//   Ene 1 2026 = jueves. Del 1-ene al 1-mar = 31+28 = 59 días (2026 no es
//   bisiesto). 59 mod 7 = 3 → jueves+3 = domingo. Entonces:
//     dom 1, LUN 2, mar 3 ... mar de 2026 empieza así.
//   Semanas ISO (lun-dom) relevantes:
//     Sem del 2-mar:  lun 2 ... vie 6 ... dom 8
//     Sem del 9-mar:  lun 9 ... vie 13 ... sáb 14 ... dom 15
//     Sem del 16-mar: lun 16 ... vie 20
//     Sem del 23-mar: lun 23 ... vie 27
import { describe, expect, it } from "vitest";
import { cadenciaRealSemanas, diaDominante, sugerirFechasBase } from "./fechasBase";

const BASE = "2026-03-02T10:00:00"; // lunes 2 de marzo 2026, local

describe("sugerirFechasBase — regla determinística del §4", () => {
  it("ítem regular de la etapa 1 → viernes de (base + 1 semana)", () => {
    // base(lun 2) + 1 semana = lun 9-mar → viernes de esa semana = 13-mar.
    const r = sugerirFechasBase({ planCreatedAt: BASE, items: [{ id: "a", etapa: 1, destacado: false }] });
    expect(r).toEqual([{ id: "a", fecha: "2026-03-13" }]);
  });

  it("ítem destacado ('Esta semana') de la etapa 1 → lunes de esa semana", () => {
    // base + 1 semana = lun 9-mar → inicio de su semana (lunes) = 9-mar.
    const r = sugerirFechasBase({ planCreatedAt: BASE, items: [{ id: "b", etapa: 1, destacado: true }] });
    expect(r).toEqual([{ id: "b", fecha: "2026-03-09" }]);
  });

  it("etapa 2 regular → viernes de (base + 2 semanas)", () => {
    // base + 2 semanas = lun 16-mar → viernes = 20-mar.
    const r = sugerirFechasBase({ planCreatedAt: BASE, items: [{ id: "c", etapa: 2, destacado: false }] });
    expect(r).toEqual([{ id: "c", fecha: "2026-03-20" }]);
  });

  it("varias etapas a la vez conservan su regla", () => {
    // etapa1 destacado → lun 9; etapa1 regular → vie 13; etapa2 regular →
    // vie 20; etapa3 regular → base+3sem = lun 23 → viernes = 27-mar.
    const r = sugerirFechasBase({
      planCreatedAt: BASE,
      items: [
        { id: "d1", etapa: 1, destacado: true },
        { id: "d2", etapa: 1, destacado: false },
        { id: "d3", etapa: 2, destacado: false },
        { id: "d4", etapa: 3, destacado: false },
      ],
    });
    expect(r).toEqual([
      { id: "d1", fecha: "2026-03-09" },
      { id: "d2", fecha: "2026-03-13" },
      { id: "d3", fecha: "2026-03-20" },
      { id: "d4", fecha: "2026-03-27" },
    ]);
  });

  it("día preferido (sábado) desplaza los regulares, no los destacados", () => {
    // diaPreferido = 6 (sábado). etapa 1 regular → sábado de la semana de
    // lun 9-mar = 14-mar. El destacado sigue en el inicio (lunes 9-mar).
    const r = sugerirFechasBase({
      planCreatedAt: BASE,
      diaPreferido: 6,
      items: [
        { id: "reg", etapa: 1, destacado: false },
        { id: "dest", etapa: 1, destacado: true },
      ],
    });
    expect(r).toEqual([
      { id: "reg", fecha: "2026-03-14" },
      { id: "dest", fecha: "2026-03-09" },
    ]);
  });
});

describe("diaDominante — patrón de día de cierre", () => {
  it("null si no hay completed_at", () => {
    expect(diaDominante([null, undefined])).toBeNull();
  });

  it("gana el día más frecuente (tres sábados vs un viernes → sábado=6)", () => {
    // Mar 1 2026 = domingo → mar 7 = sábado, mar 14 = sábado, mar 21 =
    // sábado; mar 13 = viernes. getDay() sábado = 6.
    const dia = diaDominante([
      "2026-03-07T09:00:00",
      "2026-03-14T09:00:00",
      "2026-03-21T09:00:00",
      "2026-03-13T09:00:00",
    ]);
    expect(dia).toBe(6);
  });
});

// ---------------------------------------------------------------------------
// Fase 4.0 §1[8] — el sugeridor del ciclo N+1 aprende la VELOCIDAD real del
// ciclo N. Antes la cadencia era fija (1 etapa = 1 semana) y le volvia a
// prometer una semana a quien tardaba tres. Calculos a mano ANTES del assert.
// ---------------------------------------------------------------------------
describe("cadenciaRealSemanas (Fase 4.0)", () => {
  it("sin datos, la cadencia de siempre: 1 semana por etapa", () => {
    expect(cadenciaRealSemanas([])).toBe(1);
    expect(cadenciaRealSemanas([{ etapa: 1, dias: 0 }])).toBe(1);
  });

  it("un usuario de ~1 semana por etapa se queda en 1", () => {
    // dias: 7 y 8 -> media 7.5 -> 7.5/7 = 1.07 -> redondea a 1
    expect(cadenciaRealSemanas([{ etapa: 1, dias: 7 }, { etapa: 2, dias: 8 }])).toBe(1);
  });

  it("un usuario de tres semanas por etapa recibe 3", () => {
    // dias: 18 y 24 -> media 21 -> 21/7 = 3 exacto
    expect(cadenciaRealSemanas([{ etapa: 1, dias: 18 }, { etapa: 2, dias: 24 }])).toBe(3);
  });

  it("se acota a 6 aunque el dato sea extremo", () => {
    // 365 dias/etapa -> 52 semanas -> tope 6
    expect(cadenciaRealSemanas([{ etapa: 1, dias: 365 }])).toBe(6);
  });
});

describe("sugerirFechasBase — la cadencia aprendida espacia las etapas", () => {
  // plan nace el jueves 2026-03-05. Cadencia 1 (default): etapa 1 -> viernes de
  // la semana +1 = 2026-03-13; etapa 2 -> viernes +2 = 2026-03-20.
  const items = [
    { id: "a", etapa: 1, destacado: false },
    { id: "b", etapa: 2, destacado: false },
  ];

  it("con cadencia 1 (default) mantiene el comportamiento de siempre", () => {
    const r = sugerirFechasBase({ planCreatedAt: "2026-03-05T12:00:00Z", items });
    expect(r.map((f) => f.fecha)).toEqual(["2026-03-13", "2026-03-20"]);
  });

  it("con cadencia 3, la etapa 1 cae a 3 semanas y la etapa 2 a 6", () => {
    // etapa 1 -> viernes de la semana +3 = 2026-03-27
    // etapa 2 -> viernes de la semana +6 = 2026-04-17
    const r = sugerirFechasBase({ planCreatedAt: "2026-03-05T12:00:00Z", items, cadenciaSemanas: 3 });
    expect(r.map((f) => f.fecha)).toEqual(["2026-03-27", "2026-04-17"]);
  });
});
