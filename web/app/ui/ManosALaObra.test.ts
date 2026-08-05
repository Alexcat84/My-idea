/**
 * Scheduler Fase 2 — el CABLEADO del ritual: "Con fechas" y "Recalcular
 * pendientes" usan el empaquetado cuando hay bandas, y caen al sugeridor viejo
 * cuando falta una. Se prueba `calcularFechasRitual`, que es la decisión (el
 * resto del ritual es pintar); el reparto en sí ya lo prueba empaquetado.test.
 *
 * ANCLA 2026-08-03 (lunes). Semanas desde la del ancla:
 *   semana 1 → lun 10-ago · vie 14-ago     semana 3 → lun 24-ago · vie 28-ago
 *   semana 2 → lun 17-ago · vie 21-ago     semana 4 → lun 31-ago · vie 04-sep
 */
import { describe, expect, it } from "vitest";
import { calcularFechasRitual } from "./ManosALaObra";
import type { GrupoRitual, ItemChecklistUI } from "./ManosALaObra";

const ANCLA = "2026-08-03T10:00:00";

function item(over: Partial<ItemChecklistUI> & { id: string; etapa: number }): ItemChecklistUI {
  return {
    plan_id: "plan-1",
    dominio: "core",
    orden: 1,
    texto: "una tarea",
    destacado: false,
    estado: "pendiente",
    nota: null,
    completed_at: null,
    no_aplica_motivo: null,
    fecha_base: null,
    fecha_base_origen: null,
    fecha_base_original: null,
    banda: null,
    espera_externa: null,
    created_at: ANCLA,
    updated_at: ANCLA,
    ...over,
  };
}

function tramo(items: ItemChecklistUI[]): GrupoRitual[] {
  return [{ dominio: "core", nombre: "Tu viaje principal", planCreatedAt: ANCLA, titulos: {}, items }];
}

/** Dos M (3 h + 3 h) en la etapa 1: con 5 h/semana desbordan a dos semanas;
 *  el sugeridor viejo los pondría a los dos en el mismo viernes. */
const DOS_M = [
  item({ id: "a", etapa: 1, banda: "M" }),
  item({ id: "b", etapa: 1, banda: "M" }),
];

describe("el ritual EMPAQUETA cuando todas las tareas tienen banda", () => {
  it("con capacidad 5-10 (5 h/sem) las dos M caen en semanas distintas", () => {
    // A MANO: M(3 h) → acumulado 3 → ceil(3/5)-1 = 0 → semana 1 → vie 14-ago.
    //         M(3 h) → acumulado 6 → ceil(6/5)-1 = 1 → semana 2 → vie 21-ago.
    const { fechas: f } = calcularFechasRitual(tramo(DOS_M), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: true,
    });
    expect(f["a"]).toBe("2026-08-14");
    expect(f["b"]).toBe("2026-08-21");
  });

  it("la capacidad MANDA: con 20+ las mismas dos tareas caben en la misma semana", () => {
    // A MANO, 20 h/sem: acumulados 3 y 6 → las dos ceil(x/20)-1 = 0 → semana 1.
    const { fechas: f } = calcularFechasRitual(tramo(DOS_M), {
      diaPreferido: null,
      capacidad: "20+",
      empaquetable: true,
    });
    expect(f["a"]).toBe("2026-08-14");
    expect(f["b"]).toBe("2026-08-14");
  });
});

describe("FALLBACK: con una sola tarea sin banda, el tramo entero vuelve al sugeridor viejo", () => {
  it("reparte por ETAPA, no por capacidad (las dos de la etapa 1, el mismo viernes)", () => {
    // A MANO (sugeridor viejo): etapa 1 → semana 1 → viernes 14-ago para las dos,
    // aunque una sea una XL de 16 h. Es el comportamiento histórico, intacto.
    const { fechas: f } = calcularFechasRitual(
      tramo([item({ id: "a", etapa: 1, banda: "XL" }), item({ id: "b", etapa: 1, banda: null })]),
      { diaPreferido: null, capacidad: "2-5", empaquetable: false }
    );
    expect(f["a"]).toBe("2026-08-14");
    expect(f["b"]).toBe("2026-08-14");
  });

  it("en el fallback la capacidad elegida NO cambia ninguna fecha", () => {
    const items = [item({ id: "a", etapa: 1, banda: null }), item({ id: "b", etapa: 2, banda: null })];
    const { fechas: lento } = calcularFechasRitual(tramo(items), { diaPreferido: null, capacidad: "2-5", empaquetable: false });
    const { fechas: rapido } = calcularFechasRitual(tramo(items), { diaPreferido: null, capacidad: "20+", empaquetable: false });
    expect(lento).toEqual(rapido);
  });

  it("el fallback sigue respetando la cadencia aprendida del ciclo previo", () => {
    // A MANO: con cadenciaSemanas = 2, la etapa 1 cae a 1x2 = 2 semanas → vie 21-ago
    // (el aprendizaje de la Fase 4.0 no se pierde por la llegada del scheduler).
    const { fechas: f } = calcularFechasRitual(tramo([item({ id: "a", etapa: 1, banda: null })]), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: false,
      cadenciaSemanas: 2,
    });
    expect(f["a"]).toBe("2026-08-21");
  });
});

describe("cada tramo cuenta desde SU plan (un mundo activado después no hereda el ancla del núcleo)", () => {
  it("dos tramos con anclas distintas producen fechas distintas para la misma etapa", () => {
    // A MANO: el tramo del núcleo ancla el 03-ago → su etapa 1 cae en la semana 1
    // (vie 14-ago). El del mundo ancla dos semanas después (17-ago) → su etapa 1
    // cae en SU semana 1 (vie 28-ago).
    const tramos: GrupoRitual[] = [
      { dominio: "core", nombre: "Tu viaje principal", planCreatedAt: ANCLA, titulos: {}, items: [item({ id: "c", etapa: 1, banda: "M" })] },
      {
        dominio: "quality",
        nombre: "Calidad",
        planCreatedAt: "2026-08-17T10:00:00",
        titulos: {},
        items: [item({ id: "m", etapa: 1, banda: "M", dominio: "quality" })],
      },
    ];
    const { fechas: f } = calcularFechasRitual(tramos, { diaPreferido: null, capacidad: "5-10", empaquetable: true });
    expect(f["c"]).toBe("2026-08-14");
    expect(f["m"]).toBe("2026-08-28");
  });
});

describe("F4 — el multiplicador personal entra por el mismo cable, y solo donde debe", () => {
  it("con factor 2 en las M, el reparto usa las horas REALES del usuario", () => {
    // A MANO, capacidad 5 h/sem: con factor 2, una M son 6 h para este usuario.
    //   a: 6 h  → ceil(6/5)-1  = 1 → semana 2 → vie 21-ago
    //   b: 12 h → ceil(12/5)-1 = 2 → semana 3 → vie 28-ago
    const { fechas: f } = calcularFechasRitual(tramo(DOS_M), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: true,
      factoresPorDominio: { core: { M: 2 } },
    });
    expect(f["a"]).toBe("2026-08-21");
    expect(f["b"]).toBe("2026-08-28");
  });

  it("el factor es POR ESPACIO: el del núcleo no toca las fechas del mundo", () => {
    // A MANO, capacidad 5: la M del núcleo lleva factor 2 (6 h → semana 2 desde
    // su ancla = 21-ago); la del mundo no tiene factor (3 h → su semana 1 = 28-ago,
    // contando desde SU ancla del 17-ago).
    const tramos: GrupoRitual[] = [
      { dominio: "core", nombre: "Tu viaje principal", planCreatedAt: ANCLA, titulos: {}, items: [item({ id: "c", etapa: 1, banda: "M" })] },
      {
        dominio: "quality",
        nombre: "Calidad",
        planCreatedAt: "2026-08-17T10:00:00",
        titulos: {},
        items: [item({ id: "m", etapa: 1, banda: "M", dominio: "quality" })],
      },
    ];
    const { fechas: f } = calcularFechasRitual(tramos, {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: true,
      factoresPorDominio: { core: { M: 2 } },
    });
    expect(f["c"]).toBe("2026-08-21");
    expect(f["m"]).toBe("2026-08-28");
  });

  it("sin factores el reparto es idéntico al de siempre (cero invención)", () => {
    const { fechas: base } = calcularFechasRitual(tramo(DOS_M), { diaPreferido: null, capacidad: "5-10", empaquetable: true });
    const { fechas: vacio } = calcularFechasRitual(tramo(DOS_M), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: true,
      factoresPorDominio: { core: {} },
    });
    expect(vacio).toEqual(base);
  });

  it("en el FALLBACK el factor no pinta nada (el sugeridor viejo no sabe de bandas)", () => {
    const { fechas: conFactor } = calcularFechasRitual(tramo([item({ id: "a", etapa: 1, banda: null })]), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: false,
      factoresPorDominio: { core: { M: 4 } },
    });
    expect(conFactor["a"]).toBe("2026-08-14");
  });
});

describe("el día de cierre aprendido se conserva en los dos caminos", () => {
  it("empaquetando: con diaPreferido sábado, la entrega cae en sábado", () => {
    // A MANO: sábado = 6 → semana 1 → 15-ago.
    const { fechas: f } = calcularFechasRitual(tramo([item({ id: "a", etapa: 1, banda: "M" })]), {
      diaPreferido: 6,
      capacidad: "5-10",
      empaquetable: true,
    });
    expect(f["a"]).toBe("2026-08-15");
  });

  it("en el fallback también", () => {
    const { fechas: f } = calcularFechasRitual(tramo([item({ id: "a", etapa: 1, banda: null })]), {
      diaPreferido: 6,
      capacidad: "5-10",
      empaquetable: false,
    });
    expect(f["a"]).toBe("2026-08-15");
  });
});

describe("P5 — las anclas viajan por el mismo cable, con su aviso etiquetado", () => {
  it("con ancla alcanzable, el reparto adelanta y NO hay aviso", () => {
    // A MANO, capacidad 5: B (ancla vie 28-ago) gana prioridad → vie 14-ago.
    const r = calcularFechasRitual(
      tramo([item({ id: "a", etapa: 1, banda: "M" }), item({ id: "b", etapa: 1, banda: "M" })]),
      {
        diaPreferido: null,
        capacidad: "5-10",
        empaquetable: true,
        anclas: { b: { fecha: "2026-08-28T12:00:00.000Z", etiqueta: "#3 · Compra el lote inicial" } },
      }
    );
    expect(r.fechas["b"]).toBe("2026-08-14");
    expect(r.noLlegan).toEqual({});
  });

  it("cuando no llega, el aviso sale con la ETIQUETA de lo protegido (#N · título)", () => {
    // A MANO, capacidad 5: ancla 18-ago → deseada 11-ago; lo mejor posible es
    // el vie 14-ago → no llega, y el aviso nombra a quién protege.
    const r = calcularFechasRitual(tramo([item({ id: "b", etapa: 1, banda: "M" })]), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: true,
      anclas: { b: { fecha: "2026-08-18T12:00:00.000Z", etiqueta: "#3 · Compra el lote inicial" } },
    });
    expect(r.fechas["b"]).toBe("2026-08-14"); // la honesta, jamás adelantada a mano
    expect(r.noLlegan).toEqual({ b: "#3 · Compra el lote inicial" });
  });

  it("el FALLBACK no ancla (declarado): sin bandas, ni prioridad ni avisos", () => {
    const r = calcularFechasRitual(tramo([item({ id: "b", etapa: 1, banda: null })]), {
      diaPreferido: null,
      capacidad: "5-10",
      empaquetable: false,
      anclas: { b: { fecha: "2026-08-18T12:00:00.000Z", etiqueta: "#3 · Compra el lote inicial" } },
    });
    expect(r.fechas["b"]).toBe("2026-08-14");
    expect(r.noLlegan).toEqual({});
  });
});
