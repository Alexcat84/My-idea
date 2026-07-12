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
import { diaDominante, sugerirFechasBase } from "./fechasBase";

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
