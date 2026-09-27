// i18n F6: los generadores de documentos en el idioma que se les pide (el del
// proyecto, D2), con la elisión del italiano en cada fecha tras un artículo.
//
// Lo esperado, a mano: la plantilla italiana de fechas es "{{d}} {{mes}} {{ano}}"
// (8 marzo 2026) y las frases son "**Hai iniziato** il {{fecha}}", "generato il
// {{fecha}}", "[fatta il {{fecha}}](#f-hecho)", "> Dal {{desde}} al {{hasta}}".
// Con 8 ("otto") y 11 ("undici"), que empiezan por vocal, el artículo se elide:
// il → l', dal → dall', al → all' (regla completa en lib/i18n/elision.test.ts).
// En coreano la fecha es "{{ano}}년 {{mes}} {{d}}일" → "2026년 3월 8일".
import { describe, expect, it } from "vitest";
import { cicloMarkdown, expedienteMarkdown, reporteMundoMarkdown, type DatosExpediente } from "./expediente";
import { bitacoraMarkdown, type EntradaBitacora } from "./bitacoraCliente";

// Mediodía local: el día del calendario no se corre por la zona horaria.
const OCHO_MARZO = new Date(2026, 2, 8, 12).toISOString();
const ONCE_ABRIL = new Date(2026, 3, 11, 12).toISOString();
const NUEVE_MARZO = new Date(2026, 2, 9, 12).toISOString();

const datos = (extra: Partial<DatosExpediente> = {}): DatosExpediente => ({
  nombre: "Pane",
  entradaOriginal: "Voglio vendere pane",
  creadaAt: OCHO_MARZO,
  realizadaAt: null,
  cierreMotivo: null,
  organizadorMd: null,
  ciclos: [],
  acciones: [
    { etapa: 1, texto: "Chiama cinque clienti", estado: "hecho", completedAt: OCHO_MARZO, fechaBase: null },
    { etapa: 1, texto: "Prepara il listino", estado: "pendiente", completedAt: null, fechaBase: ONCE_ABRIL },
  ],
  numerosMd: null,
  mundos: [],
  informeMd: null,
  bitacoraMd: null,
  generadoAt: ONCE_ABRIL,
  ...extra,
});

describe("Expediente en italiano: l'8, l'11", () => {
  const md = expedienteMarkdown(datos(), "it");
  it("la fecha de inicio y la de generación eliden el artículo", () => {
    expect(md).toContain("**Hai iniziato** l'8 marzo 2026");
    expect(md).toContain("> Fascicolo completo · generato l'11 aprile 2026");
  });
  it("las fechas de las acciones también", () => {
    expect(md).toContain("[fatta l'8 marzo 2026](#f-hecho)");
    expect(md).toContain("[prevista per l'11 aprile 2026](#f-prev)");
  });
  it("con otro día no hay elisión (9 = «nove»)", () => {
    expect(expedienteMarkdown(datos({ creadaAt: NUEVE_MARZO }), "it")).toContain("**Hai iniziato** il 9 marzo 2026");
  });
  it("en español, igual que siempre", () => {
    expect(expedienteMarkdown(datos(), "es")).toContain("**Empezaste** el 8 de marzo de 2026");
  });
});

describe("Reporte de un mundo y bitácora en italiano", () => {
  it("el reporte: generato l'11", () => {
    const md = reporteMundoMarkdown(
      {
        nombreIdea: "Pane",
        nombreMundo: "Qualità e Fiducia",
        ciclos: [],
        acciones: [],
        comoTeFueMd: null,
        bitacoraMd: null,
        completadoAt: OCHO_MARZO,
        generadoAt: ONCE_ABRIL,
      },
      "it"
    );
    expect(md).toContain("generato l'11 aprile 2026");
    expect(md).toContain("Concluso l'8 marzo 2026");
  });

  it("la bitácora: «Dall'8 marzo 2026 all'11 aprile 2026»", () => {
    const entradas: EntradaBitacora[] = [
      { fecha: OCHO_MARZO, texto: "Primo passo", peso: "accion", dominio: "core" },
      { fecha: ONCE_ABRIL, texto: "Secondo passo", peso: "accion", dominio: "core" },
    ];
    expect(bitacoraMarkdown("Pane", entradas, ONCE_ABRIL, undefined, undefined, "it")).toContain(
      "> Dall'8 marzo 2026 all'11 aprile 2026"
    );
    expect(bitacoraMarkdown("Pane", [], ONCE_ABRIL, undefined, undefined, "it")).toContain("> Generata l'11 aprile 2026");
  });
});

describe("el plan suelto (un ciclo) en el idioma pedido", () => {
  it("la portadilla lleva la fecha del idioma: coreano", () => {
    const md = cicloMarkdown("Pan", "나의 계획", { planId: "p", etiqueta: "inicial", createdAt: OCHO_MARZO, contenidoMd: "# X" }, "ko");
    expect(md.split("\n")[0]).toBe("> Pan · 나의 계획 · 2026년 3월 8일");
  });
  it("en español, igual que siempre", () => {
    const md = cicloMarkdown("Pan", "Tu Plan", { planId: "p", etiqueta: "inicial", createdAt: OCHO_MARZO, contenidoMd: "# X" });
    expect(md).toBe("> Pan · Tu Plan · 8 de marzo de 2026\n\n# X\n");
  });
});
