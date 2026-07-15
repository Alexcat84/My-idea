// Fase 3.8 §6 — analytics del proyecto. Regla AGENTS.md: se siembra un
// proyecto sintético con fechas CONOCIDAS y cada métrica se calcula a mano
// en el comentario ANTES del assert. Fechas en UTC (Z) para que las
// diferencias sean exactas (inmunes a DST).
//
// Proyecto sembrado:
//   chispa      = 2026-03-01  ·  realizada = 2026-05-01  → total 61 días
//                 (mar: 1→abr1 = 31; abr1→may1 = 30; 31+30 = 61)
//   organizador = 2026-03-02
//   planesCore  = p1 inicial (2026-03-03, baseline confirmada)
//                 p2 seguimiento (2026-04-01, sin baseline)   → 2 ciclos
//   mundos      = quality @ 2026-03-20                        → 1 mundo
//   ítems (todos del plan p1 con baseline):
//     A e1 completed 03-10 · base 03-10           → dif  0  (a tiempo)
//     B e1 completed 03-13 · base 03-10           → dif +3  (tardía)
//     C e2 completed 03-20 · base 03-22           → dif −2  (adelantada)
//     D e2 completed 03-25 · base 03-25 · orig 03-20 → dif 0 (a tiempo, replan)
import { describe, expect, it } from "vitest";
import { informeMarkdown, calcularAnalytics, clasificarCumplimiento, construirHitos, type EntradaAnalytics } from "./analytics";

function iso(d: string) {
  return `${d}T12:00:00Z`;
}

const BASE: EntradaAnalytics = {
  proyectoCreatedAt: iso("2026-03-01"),
  realizadaAt: iso("2026-05-01"),
  organizadorAt: iso("2026-03-02"),
  planesCore: [
    { id: "p1", etiqueta: "inicial", created_at: iso("2026-03-03"), baseline_confirmada_at: iso("2026-03-03") },
    { id: "p2", etiqueta: "seguimiento", created_at: iso("2026-04-01"), baseline_confirmada_at: null },
  ],
  mundos: [{ dominio: "quality", unlocked_at: iso("2026-03-20") }],
  items: [
    { plan_id: "p1", etapa: 1, estado: "hecho", destacado: false, texto: "A", completed_at: iso("2026-03-10"), fecha_base: iso("2026-03-10"), fecha_base_original: null },
    { plan_id: "p1", etapa: 1, estado: "hecho", destacado: false, texto: "B", completed_at: iso("2026-03-13"), fecha_base: iso("2026-03-10"), fecha_base_original: null },
    { plan_id: "p1", etapa: 2, estado: "hecho", destacado: false, texto: "C", completed_at: iso("2026-03-20"), fecha_base: iso("2026-03-22"), fecha_base_original: null },
    { plan_id: "p1", etapa: 2, estado: "hecho", destacado: false, texto: "D", completed_at: iso("2026-03-25"), fecha_base: iso("2026-03-25"), fecha_base_original: iso("2026-03-20") },
  ],
};

describe("clasificarCumplimiento — umbrales del §6", () => {
  it("|dif| ≤ 1 día = a tiempo", () => {
    expect(clasificarCumplimiento(iso("2026-03-11"), iso("2026-03-10"))).toBe("a_tiempo"); // +1
    expect(clasificarCumplimiento(iso("2026-03-09"), iso("2026-03-10"))).toBe("a_tiempo"); // −1
  });
  it("> +1 día = tardía; < −1 día = adelantada", () => {
    expect(clasificarCumplimiento(iso("2026-03-13"), iso("2026-03-10"))).toBe("tardia"); // +3
    expect(clasificarCumplimiento(iso("2026-03-07"), iso("2026-03-10"))).toBe("adelantada"); // −3
  });
});

describe("calcularAnalytics — capa universal", () => {
  const a = calcularAnalytics(BASE).universal;

  it("duración total = 61 días", () => {
    expect(a.duracionTotalDias).toBe(61);
  });
  it("acciones hechas = 4", () => {
    expect(a.accionesHechas).toBe(4);
  });
  it("ritmo = 4 / (61/7) = 0.459 → 0.5 acciones/semana", () => {
    expect(a.ritmoAccionesPorSemana).toBe(0.5);
  });
  it("racha más larga = 15 días (03-10 a 03-25, gaps 3,7,5 ≤ 7)", () => {
    expect(a.rachaMasLargaDias).toBe(15);
  });
  it("ciclos de plan = 2, mundos = 1", () => {
    expect(a.ciclosDePlan).toBe(2);
    expect(a.mundos).toBe(1);
  });
  it("duración por etapa: e1 = 12 (03-01→03-13), e2 = 12 (03-13→03-25)", () => {
    expect(a.duracionPorEtapa).toEqual([
      { etapa: 1, dias: 12 },
      { etapa: 2, dias: 12 },
    ]);
  });
});

describe("calcularAnalytics — capa de cumplimiento", () => {
  const c = calcularAnalytics(BASE).cumplimiento!;

  it("conteos: 2 a tiempo, 1 adelantada, 1 tardía sobre 4", () => {
    expect(c.aTiempo).toBe(2);
    expect(c.adelantadas).toBe(1);
    expect(c.tardias).toBe(1);
    expect(c.totalConFecha).toBe(4);
  });
  it("porcentajes: 50 / 25 / 25", () => {
    expect(c.pctATiempo).toBe(50);
    expect(c.pctAdelantadas).toBe(25);
    expect(c.pctTardias).toBe(25);
  });
  it("desviación media = (0+3−2+0)/4 = 0.25 → 0.3 días", () => {
    expect(c.desviacionMediaDias).toBe(0.3);
  });
  it("replanificaciones = 1 (solo D tiene fecha_base_original)", () => {
    expect(c.replanificaciones).toBe(1);
  });
  it("barras gemelas: e1 base 9 / real 12; e2 base 24 / real 24", () => {
    expect(c.porEtapa).toEqual([
      { etapa: 1, baseDias: 9, realDias: 12 },
      { etapa: 2, baseDias: 24, realDias: 24 },
    ]);
  });
});

describe("calcularAnalytics — sin baseline → sin capa de cumplimiento", () => {
  it("cumplimiento es null cuando ningún plan tiene baseline", () => {
    const sinBase: EntradaAnalytics = {
      ...BASE,
      planesCore: BASE.planesCore.map((p) => ({ ...p, baseline_confirmada_at: null })),
    };
    const r = calcularAnalytics(sinBase);
    expect(r.cumplimiento).toBeNull();
    expect(r.universal.accionesHechas).toBe(4); // la universal sigue viva
  });
});

describe("construirHitos", () => {
  it("ordena chispa, claridad, planes, mundo y realizada (6 hitos)", () => {
    const h = construirHitos(BASE, iso("2026-05-01"));
    expect(h.map((x) => x.tipo)).toEqual(["chispa", "claridad", "plan", "mundo", "plan", "realizada"]);
  });
  it("incluirAcciones suma un hito por ítem completado (4 acciones)", () => {
    const h = construirHitos(BASE, iso("2026-05-01"), true);
    expect(h.filter((x) => x.tipo === "accion")).toHaveLength(4);
  });
});

// ---------------------------------------------------------------------------
// Fase 4.0 §3 — lo que el BLOQUE DE REALIDAD necesita y antes no se calculaba.
// Todo a mano sobre el MISMO proyecto sembrado arriba.
// ---------------------------------------------------------------------------
describe("calcularAnalytics — señales para el bloque de realidad (§3)", () => {
  it("diasSinAvance: del ultimo completed_at al fin", () => {
    // ultimo avance = D @ 03-25. fin = realizada @ 05-01.
    // 03-25 -> 04-25 = 31 dias; 04-25 -> 05-01 = 6 dias; 31+6 = 37.
    expect(calcularAnalytics(BASE).universal.diasSinAvance).toBe(37);
  });

  it("diasSinAvance es null si nunca hubo un avance", () => {
    const sinAvance = { ...BASE, items: BASE.items.map((i) => ({ ...i, completed_at: null })) };
    expect(calcularAnalytics(sinAvance).universal.diasSinAvance).toBeNull();
  });

  it("vida del plan vigente: el ultimo plan por created_at (p2)", () => {
    const u = calcularAnalytics(BASE).universal;
    // p2 nacio 04-01; fin 05-01; abril tiene 30 dias -> 30.
    expect(u.planVigenteAt).toBe(iso("2026-04-01"));
    expect(u.diasDeVidaPlanVigente).toBe(30);
  });

  it("tardiasTop: solo B, con sus 3 dias de retraso y su etapa", () => {
    // De los 4 items, el unico tardio es B (base 03-10, hecho 03-13 -> +3).
    expect(calcularAnalytics(BASE).cumplimiento?.tardiasTop).toEqual([
      { texto: "B", etapa: 1, diasRetraso: 3 },
    ]);
  });

  it("tardiasTop ordena por retraso descendente y corta en 5", () => {
    const seis = Array.from({ length: 6 }, (_, k) => ({
      plan_id: "p1",
      etapa: 1,
      estado: "hecho",
      destacado: false,
      texto: `T${k}`,
      // base 03-10; hecho 03-(11+k) -> retraso 1+k dias (k=0 -> +1 = a tiempo)
      completed_at: iso(`2026-03-${String(11 + k).padStart(2, "0")}`),
      fecha_base: iso("2026-03-10"),
      fecha_base_original: null,
    }));
    const top = calcularAnalytics({ ...BASE, items: seis }).cumplimiento!.tardiasTop;
    // k=0 (+1) es "a tiempo" y NO entra; quedan k=1..5 -> retrasos 2,3,4,5,6.
    // Orden descendente: 6,5,4,3,2 (T5,T4,T3,T2,T1). Son 5: no se corta nada.
    expect(top.map((t) => t.diasRetraso)).toEqual([6, 5, 4, 3, 2]);
    expect(top[0].texto).toBe("T5");
  });

  it("replanificados: CUALES movieron su fecha, no solo cuantos", () => {
    const c = calcularAnalytics(BASE).cumplimiento!;
    expect(c.replanificaciones).toBe(1);
    expect(c.replanificados).toEqual([{ texto: "D", etapa: 2 }]);
  });

  it("el modo del camino se arrastra tal cual", () => {
    expect(calcularAnalytics(BASE).modoCamino).toBeNull();
    expect(calcularAnalytics({ ...BASE, modoCamino: "fechas" }).modoCamino).toBe("fechas");
    expect(calcularAnalytics({ ...BASE, modoCamino: "ritmo" }).modoCamino).toBe("ritmo");
  });
});

// ---------------------------------------------------------------------------
// Fase 4.0 §8 — EL ACTA DE CIERRE en el informe exportado.
// ---------------------------------------------------------------------------
describe("informeMarkdown — acta de cierre (§8)", () => {
  it("sin realizadaAt no hay acta: el informe es el de siempre", () => {
    const md = informeMarkdown("Mi idea", calcularAnalytics(BASE));
    expect(md).not.toContain("## Acta de cierre");
  });

  it("realizado: abre con el acta, el estado final y el porcentaje", () => {
    // accionesVigente = items del plan vigente (p2). En BASE todos los items
    // son de p1, asi que el vigente (p2) tiene 0 de 0 -> sin porcentaje.
    const md = informeMarkdown("Mi idea", calcularAnalytics(BASE), iso("2026-05-01"));
    expect(md).toContain("## Acta de cierre");
    expect(md).toContain("**Proyecto realizado** el 2026-05-01");
    expect(md).toContain("Acciones al cerrar: **0 de 0**");
  });

  it("con motivo, el informe lo cita en la voz del usuario", () => {
    const a = calcularAnalytics({ ...BASE, cierreMotivo: "Ya validé lo que\nnecesitaba saber." });
    const md = informeMarkdown("Mi idea", a, iso("2026-05-01"));
    expect(md).toContain("### Por qué la cerraste aquí");
    // los saltos de linea se aplanan para no romper la cita markdown
    expect(md).toContain("> Ya validé lo que necesitaba saber.");
  });

  it("sin motivo (cerro sin escribir), el acta existe pero no inventa cita", () => {
    const md = informeMarkdown("Mi idea", calcularAnalytics(BASE), iso("2026-05-01"));
    expect(md).toContain("## Acta de cierre");
    expect(md).not.toContain("### Por qué la cerraste aquí");
  });
});
