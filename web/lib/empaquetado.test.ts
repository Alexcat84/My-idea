/**
 * Scheduler Fase 2 — el empaquetado contra la capacidad real.
 *
 * Regla de la casa (AGENTS.md): la aritmética va CALCULADA A MANO en el
 * comentario ANTES del assert, jamás copiada de la salida de la función.
 *
 * ANCLA de todas las pruebas: 2026-08-03, que es LUNES (verificado: 2026-01-01
 * cae jueves; el 3 de agosto es el día 215 del año; (215-1) mod 7 = 4; jueves+4
 * = lunes). Semanas contadas desde la del ancla (semana 0):
 *
 *   semana 0 → lun 03-ago · vie 07-ago       semana 9  → lun 05-oct · vie 09-oct
 *   semana 1 → lun 10-ago · vie 14-ago       semana 10 → lun 12-oct · vie 16-oct
 *   semana 2 → lun 17-ago · vie 21-ago       semana 11 → lun 19-oct · vie 23-oct
 *   semana 3 → lun 24-ago · vie 28-ago       semana 12 → lun 26-oct · vie 30-oct
 *   semana 4 → lun 31-ago · vie 04-sep       semana 13 → lun 02-nov · vie 06-nov
 *   semana 5 → lun 07-sep · vie 11-sep       semana 14 → lun 09-nov · vie 13-nov
 *   semana 6 → lun 14-sep · vie 18-sep       semana 15 → lun 16-nov · vie 20-nov
 *   semana 7 → lun 21-sep · vie 25-sep       semana 16 → lun 23-nov · vie 27-nov
 *   semana 8 → lun 28-sep · vie 02-oct       semana 17 → lun 30-nov · vie 04-dic
 *                                            semana 18 → lun 07-dic · vie 11-dic
 */
import { describe, expect, it } from "vitest";
import {
  CAPACIDAD_DEFAULT,
  FACTOR_MAX,
  FACTOR_MIN,
  HORAS_MEDIA,
  HORAS_POR_SEMANA,
  LEAD_ESPERA_SEMANAS,
  MIN_MUESTRAS_FACTOR,
  empaquetarFechas,
  factorPorBanda,
  hayBandas,
} from "./empaquetado";
import { sugerirFechasBase } from "./fechasBase";
import type { ItemEmpaquetable } from "./empaquetado";

const ANCLA = "2026-08-03T10:00:00";

/** El MISMO plan para todas las pruebas de capacidad: dos etapas.
 *  Etapa 1: destacada S(1 h) + M(3 h) + M(3 h) + L(8 h) = 15 h
 *  Etapa 2: M(3 h) + XL(16 h) = 19 h                     (total 34 h) */
const PLAN: ItemEmpaquetable[] = [
  { id: "e1-destacada", etapa: 1, destacado: true, banda: "S" },
  { id: "e1-a", etapa: 1, destacado: false, banda: "M" },
  { id: "e1-b", etapa: 1, destacado: false, banda: "M" },
  { id: "e1-c", etapa: 1, destacado: false, banda: "L" },
  { id: "e2-a", etapa: 2, destacado: false, banda: "M" },
  { id: "e2-b", etapa: 2, destacado: false, banda: "XL" },
];

function fechasDe(items: ItemEmpaquetable[], capacidad: Parameters<typeof empaquetarFechas>[0]["capacidad"]) {
  const r = empaquetarFechas({ ancla: ANCLA, items, capacidad });
  return { mapa: Object.fromEntries(r.fechas.map((f) => [f.id, f.fecha])), r };
}

describe("las constantes son las del contrato, no números sueltos", () => {
  it("HORAS_MEDIA = S:1, M:3, L:8, XL:16", () => {
    expect(HORAS_MEDIA).toEqual({ S: 1, M: 3, L: 8, XL: 16 });
  });

  it("se planifica con el PISO del chip elegido (conservador, declarado)", () => {
    expect(HORAS_POR_SEMANA).toEqual({ "2-5": 2, "5-10": 5, "10-20": 10, "20+": 20 });
  });

  it("el chip por defecto es 5-10", () => {
    expect(CAPACIDAD_DEFAULT).toBe("5-10");
  });
});

describe("el mismo plan, dos personas distintas: el calendario respira distinto", () => {
  it("quien da 20+ horas (planifica con 20/sem) cierra el plan en 3 semanas", () => {
    // A MANO, capacidad 20 h/semana. La etapa 1 arranca en la semana 1 (la
    // siguiente al ancla: ninguna fecha nace vencida).
    //   ETAPA 1 (acumulado de horas → semana donde cae la hora final):
    //     destacada S: 1 h → ceil(1/20)-1 = 0 → semana 1, y por destacada: LUNES  = 10-ago
    //     M:  1+3 = 4 h  → ceil(4/20)-1  = 0 → semana 1 → viernes               = 14-ago
    //     M:  4+3 = 7 h  → ceil(7/20)-1  = 0 → semana 1 → viernes               = 14-ago
    //     L:  7+8 = 15 h → ceil(15/20)-1 = 0 → semana 1 → viernes               = 14-ago
    //     última semana de la etapa = 1 → PUERTA: la etapa 2 abre en la semana 2
    //   ETAPA 2:
    //     M:  3 h        → ceil(3/20)-1  = 0 → semana 2 → viernes               = 21-ago
    //     XL: 3+16 = 19 h→ ceil(19/20)-1 = 0 → semana 2 → viernes               = 21-ago
    const { mapa, r } = fechasDe(PLAN, "20+");
    expect(mapa["e1-destacada"]).toBe("2026-08-10");
    expect(mapa["e1-a"]).toBe("2026-08-14");
    expect(mapa["e1-b"]).toBe("2026-08-14");
    expect(mapa["e1-c"]).toBe("2026-08-14");
    expect(mapa["e2-a"]).toBe("2026-08-21");
    expect(mapa["e2-b"]).toBe("2026-08-21");
    expect(r.semanasTotales).toBe(3); // última semana usada (2) + 1
  });

  it("quien da 2-5 horas (planifica con 2/sem) tarda 19 semanas en el MISMO plan", () => {
    // A MANO, capacidad 2 h/semana. Mismo plan, misma ancla.
    //   ETAPA 1 (arranca en la semana 1):
    //     destacada S: 1 h  → ceil(1/2)-1  = 0 → semana 1, LUNES                = 10-ago
    //     M:  1+3 = 4 h     → ceil(4/2)-1  = 1 → semana 1+1 = 2  → viernes       = 21-ago
    //     M:  4+3 = 7 h     → ceil(7/2)-1  = 3 → semana 1+3 = 4  → viernes       = 04-sep
    //     L:  7+8 = 15 h    → ceil(15/2)-1 = 7 → semana 1+7 = 8  → viernes       = 02-oct
    //     última semana relativa = 7 → PUERTA: la etapa 2 abre en 1+7+1 = semana 9
    //   ETAPA 2:
    //     M:  3 h           → ceil(3/2)-1  = 1 → semana 9+1  = 10 → viernes      = 16-oct
    //     XL: 3+16 = 19 h   → ceil(19/2)-1 = 9 → semana 9+9  = 18 → viernes      = 11-dic
    const { mapa, r } = fechasDe(PLAN, "2-5");
    expect(mapa["e1-destacada"]).toBe("2026-08-10");
    expect(mapa["e1-a"]).toBe("2026-08-21");
    expect(mapa["e1-b"]).toBe("2026-09-04");
    expect(mapa["e1-c"]).toBe("2026-10-02");
    expect(mapa["e2-a"]).toBe("2026-10-16");
    expect(mapa["e2-b"]).toBe("2026-12-11");
    expect(r.semanasTotales).toBe(19); // última semana usada (18) + 1
  });

  it("34 horas de trabajo: el de 20/sem termina 16 semanas antes que el de 2/sem", () => {
    // No es una opinión: 34 h a 2 h/semana son 17 semanas de trabajo; a 20 h/semana,
    // dos. La diferencia de semanasTotales tiene que ser esa magnitud, no cero.
    const rapido = empaquetarFechas({ ancla: ANCLA, items: PLAN, capacidad: "20+" });
    const lento = empaquetarFechas({ ancla: ANCLA, items: PLAN, capacidad: "2-5" });
    expect(lento.semanasTotales - rapido.semanasTotales).toBe(16);
  });
});

describe("una etapa que DESBORDA su semana se reparte en varias", () => {
  it("dos M (3 h + 3 h) con capacidad 5 caen en semanas distintas", () => {
    // A MANO, capacidad 5 h/semana, etapa 1 (arranca en la semana 1):
    //   M: 3 h      → ceil(3/5)-1 = 0 → semana 1 → viernes = 14-ago
    //   M: 3+3 = 6 h→ ceil(6/5)-1 = 1 → semana 2 → viernes = 21-ago   (desborde)
    const { mapa } = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
      ],
      "5-10"
    );
    expect(mapa["a"]).toBe("2026-08-14");
    expect(mapa["b"]).toBe("2026-08-21");
  });

  it("una XL más grande que la semana entera ocupa las semanas que necesita y entrega al terminar", () => {
    // A MANO: XL = 16 h con capacidad 5 h/semana → ceil(16/5)-1 = 4-1 = 3.
    // Cuatro semanas de trabajo: entrega el viernes de la semana 1+3 = 4 = 04-sep.
    const { mapa } = fechasDe([{ id: "xl", etapa: 1, destacado: false, banda: "XL" }], "5-10");
    expect(mapa["xl"]).toBe("2026-09-04");
  });

  it("la puerta: la etapa 2 abre DESPUÉS de la última semana que ocupó la 1", () => {
    // A MANO, capacidad 5: la etapa 1 (M+M) ocupa las semanas 1 y 2 (arriba).
    // Puerta → la etapa 2 abre en la semana 3: su M entrega el viernes = 28-ago.
    // Ninguna tarea de la etapa 2 comparte semana de entrega con la última de la 1.
    const { mapa } = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 2, destacado: false, banda: "M" },
      ],
      "5-10"
    );
    expect(mapa["b"]).toBe("2026-08-21"); // última de la etapa 1, semana 2
    expect(mapa["c"]).toBe("2026-08-28"); // primera de la etapa 2, semana 3
    expect(mapa["c"] > mapa["b"]).toBe(true);
  });
});

describe("la destacada es el arranque de SU etapa: el lunes de su primera semana", () => {
  it("la destacada de la etapa 1 cae el lunes de la semana 1", () => {
    // A MANO: la etapa 1 abre en la semana 1 → lunes = 10-ago.
    const { mapa } = fechasDe(PLAN, "5-10");
    expect(mapa["e1-destacada"]).toBe("2026-08-10");
  });

  it("la destacada de una etapa POSTERIOR cae el lunes de la primera semana de ESA etapa", () => {
    // A MANO, capacidad 5: la etapa 1 (M+M = 6 h) ocupa las semanas 1 y 2.
    // Puerta → la etapa 2 abre en la semana 3: su destacada va al LUNES = 24-ago
    // (y no al viernes, ni al lunes de la semana 1).
    const { mapa } = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "d2", etapa: 2, destacado: true, banda: "S" },
        { id: "c", etapa: 2, destacado: false, banda: "M" },
      ],
      "5-10"
    );
    expect(mapa["d2"]).toBe("2026-08-24");
  });

  it("la destacada consume su hora: empuja al resto de su etapa", () => {
    // A MANO, capacidad 5, etapa 1 con destacada S(1 h) + M(3 h) + M(3 h):
    //   destacada: 1 h        → semana 1, LUNES                  = 10-ago
    //   M: 1+3 = 4 h → ceil(4/5)-1 = 0 → semana 1 → viernes       = 14-ago
    //   M: 4+3 = 7 h → ceil(7/5)-1 = 1 → semana 2 → viernes       = 21-ago
    // Sin la hora de la destacada, el segundo M cabría en la semana 1 (6 h > 5,
    // igual desbordaría). Con ella el acumulado es 7 y desborda igual: lo que se
    // prueba es que la destacada SÍ entra en la cuenta.
    const { mapa } = fechasDe(
      [
        { id: "d", etapa: 1, destacado: true, banda: "S" },
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
      ],
      "5-10"
    );
    expect(mapa["d"]).toBe("2026-08-10");
    expect(mapa["a"]).toBe("2026-08-14");
    expect(mapa["b"]).toBe("2026-08-21");
  });
});

describe("el día de cierre aprendido manda sobre el viernes", () => {
  it("con diaPreferido = sábado, las entregas caen en sábado (la destacada sigue en lunes)", () => {
    // A MANO: sábado = 6. Semana 1 → sábado = 15-ago; su lunes sigue siendo 10-ago.
    const r = empaquetarFechas({
      ancla: ANCLA,
      items: [
        { id: "d", etapa: 1, destacado: true, banda: "S" },
        { id: "a", etapa: 1, destacado: false, banda: "M" },
      ],
      capacidad: "5-10",
      diaPreferido: 6,
    });
    const mapa = Object.fromEntries(r.fechas.map((f) => [f.id, f.fecha]));
    expect(mapa["a"]).toBe("2026-08-15");
    expect(mapa["d"]).toBe("2026-08-10");
  });
});

describe("REGRESIÓN: sin bandas no se empaqueta, y el sugeridor viejo sigue intacto", () => {
  it("hayBandas es false si UNA sola tarea no tiene banda", () => {
    expect(hayBandas(PLAN)).toBe(true);
    expect(hayBandas([...PLAN, { id: "x", etapa: 2, destacado: false, banda: null }])).toBe(false);
  });

  it("hayBandas es false con la lista vacía (no hay nada que empaquetar)", () => {
    expect(hayBandas([])).toBe(false);
  });

  it("el fallback sugerirFechasBase no cambió: etapa N → viernes de la semana N, destacada → lunes", () => {
    // A MANO (comportamiento HISTÓRICO, el que ya estaba en producción): con la
    // misma ancla, la etapa 1 cae a una semana del plan → semana 1: viernes
    // 14-ago para las regulares y lunes 10-ago para la destacada; la etapa 2 cae
    // a dos semanas → semana 2: viernes 21-ago. El reparto NO mira las bandas.
    const s = sugerirFechasBase({
      planCreatedAt: ANCLA,
      items: [
        { id: "d", etapa: 1, destacado: true },
        { id: "a", etapa: 1, destacado: false },
        { id: "b", etapa: 2, destacado: false },
      ],
    });
    const mapa = Object.fromEntries(s.map((f) => [f.id, f.fecha]));
    expect(mapa["d"]).toBe("2026-08-10");
    expect(mapa["a"]).toBe("2026-08-14");
    expect(mapa["b"]).toBe("2026-08-21");
  });

  it("el empaquetado y el fallback arrancan la MISMA semana (son intercambiables sin salto)", () => {
    // La primera etapa abre en la semana 1 en los dos caminos: quien cae al
    // fallback no ve el plan saltar una semana atrás ni adelante.
    const emp = empaquetarFechas({
      ancla: ANCLA,
      items: [{ id: "a", etapa: 1, destacado: false, banda: "S" }],
      capacidad: "20+",
    });
    const sug = sugerirFechasBase({ planCreatedAt: ANCLA, items: [{ id: "a", etapa: 1, destacado: false }] });
    expect(emp.fechas[0].fecha).toBe(sug[0].fecha);
  });
});

describe("F3 — la espera de terceros: se dispara temprano y entrega tarde", () => {
  it("la constante del colchón es UNA semana, nombrada", () => {
    expect(LEAD_ESPERA_SEMANAS).toBe(1);
  });

  it("la entrega de la tarea con espera corre +1 semana", () => {
    // A MANO, capacidad 20 h/sem, etapa 1 (abre en la semana 1):
    //   A (M, espera): trabajo → ceil(3/20)-1 = 0; entrega = 0 + 1 (colchón)
    //     → semana 1+1 = 2 → viernes = 21-ago
    // Sin espera, esa misma A entregaría el viernes de la semana 1 = 14-ago.
    const { mapa } = fechasDe([{ id: "a", etapa: 1, destacado: false, banda: "M", espera_externa: true }], "20+");
    expect(mapa["a"]).toBe("2026-08-21");
    const { mapa: sinEspera } = fechasDe([{ id: "a", etapa: 1, destacado: false, banda: "M" }], "20+");
    expect(sinEspera["a"]).toBe("2026-08-14");
  });

  it("la espera NO consume capacidad: sus hermanas de etapa no se mueven", () => {
    // A MANO, capacidad 5 h/sem, etapa 1 = [A (M, espera), B (M), C (M)]:
    //   A: trabajo ceil((0+3)/5)-1 = 0; entrega 0+1 = 1 → semana 2 → vie 21-ago
    //      NO suma al acumulado (sigue en 0).
    //   B: trabajo ceil((0+3)/5)-1 = 0 → semana 1 → vie 14-ago; acumulado = 3
    //   C: trabajo ceil((3+3)/5)-1 = 1 → semana 2 → vie 21-ago; acumulado = 6
    const conEspera = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M", espera_externa: true },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 1, destacado: false, banda: "M" },
      ],
      "5-10"
    ).mapa;
    expect(conEspera["a"]).toBe("2026-08-21");
    expect(conEspera["b"]).toBe("2026-08-14");
    expect(conEspera["c"]).toBe("2026-08-21");

    // Si A SÍ consumiera capacidad, B se iría a la semana 2 y C a la 2 también:
    //   A: acumulado 3 → semana 1; B: acumulado 6 → ceil(6/5)-1 = 1 → semana 2;
    //   C: acumulado 9 → ceil(9/5)-1 = 1 → semana 2.
    // Ese es exactamente el empujón que la regla evita: el tiempo de terceros no
    // se le cobra a la semana del usuario.
    const siConsumiera = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 1, destacado: false, banda: "M" },
      ],
      "5-10"
    ).mapa;
    expect(siConsumiera["b"]).toBe("2026-08-21"); // empujada
    expect(conEspera["b"]).not.toBe(siConsumiera["b"]);
  });

  it("la tarea con espera trae su INICIO temprano: el lunes de la primera semana de su etapa", () => {
    // A MANO: la etapa 1 abre en la semana 1 → su lunes = 10-ago. La entrega es
    // el 21-ago (viernes de la semana 2, con colchón): empieza pronto, entrega tarde.
    const { r } = fechasDe([{ id: "a", etapa: 1, destacado: false, banda: "M", espera_externa: true }], "20+");
    const a = r.fechas.find((f) => f.id === "a")!;
    expect(a.inicioTemprano).toBe("2026-08-10");
    expect(a.fecha).toBe("2026-08-21");
    expect(a.inicioTemprano! < a.fecha).toBe(true);
  });

  it("una espera de una etapa POSTERIOR arranca el lunes de SU etapa, no el de la primera", () => {
    // A MANO, capacidad 20: la etapa 1 (M) ocupa la semana 1; puerta → la etapa 2
    // abre en la semana 2, cuyo lunes es 17-ago. Su espera entrega el viernes de
    // la semana 2+1 = 3 → 28-ago.
    const { r } = fechasDe(
      [
        { id: "e1", etapa: 1, destacado: false, banda: "M" },
        { id: "e2", etapa: 2, destacado: false, banda: "M", espera_externa: true },
      ],
      "20+"
    );
    const e2 = r.fechas.find((f) => f.id === "e2")!;
    expect(e2.inicioTemprano).toBe("2026-08-17");
    expect(e2.fecha).toBe("2026-08-28");
  });

  it("la PUERTA respeta el cierre real: si la espera cierra la etapa, la siguiente abre después", () => {
    // A MANO, capacidad 20, etapa 1 = [A (M, espera), B (M)], etapa 2 = [C (M)]:
    //   A: trabajo 0, entrega 0+1 = 1 → semana 2 (21-ago). No consume.
    //   B: trabajo ceil(3/20)-1 = 0 → semana 1 (14-ago).
    //   cierre de la etapa 1 = max(trabajo 0, entrega 1) = 1
    //   PUERTA → la etapa 2 abre en 1+1+1 = semana 3 → C = viernes 28-ago.
    const { mapa } = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M", espera_externa: true },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 2, destacado: false, banda: "M" },
      ],
      "20+"
    );
    expect(mapa["a"]).toBe("2026-08-21");
    expect(mapa["b"]).toBe("2026-08-14");
    expect(mapa["c"]).toBe("2026-08-28");
    // Sin la espera, el cierre de la etapa 1 sería la semana 1 y C abriría en la
    // 2 (21-ago): la etapa siguiente NO se monta encima de la espera pendiente.
    const sinEspera = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "b", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 2, destacado: false, banda: "M" },
      ],
      "20+"
    ).mapa;
    expect(sinEspera["c"]).toBe("2026-08-21");
    expect(mapa["c"] > sinEspera["c"]).toBe(true);
  });

  it("la destacada con espera conserva su LUNES y corre de semana", () => {
    // A MANO, capacidad 20: la destacada de la etapa 1 entrega el lunes de la
    // semana 1 (10-ago); con espera, el lunes de la semana 1+1 = 2 → 17-ago.
    // El día no cambia (sigue siendo el arranque), la semana sí.
    const { mapa } = fechasDe([{ id: "d", etapa: 1, destacado: true, banda: "S", espera_externa: true }], "20+");
    expect(mapa["d"]).toBe("2026-08-17");
    const { mapa: sinEspera } = fechasDe([{ id: "d", etapa: 1, destacado: true, banda: "S" }], "20+");
    expect(sinEspera["d"]).toBe("2026-08-10");
  });

  it("REGRESIÓN: con espera_externa false o ausente, nada cambió", () => {
    // El plan de referencia (sin esperas) tiene que dar EXACTAMENTE las mismas
    // fechas que antes de F3, y declarar false explícito debe ser idéntico a
    // omitirlo.
    const { mapa: omitido } = fechasDe(PLAN, "2-5");
    expect(omitido["e1-destacada"]).toBe("2026-08-10");
    expect(omitido["e1-a"]).toBe("2026-08-21");
    expect(omitido["e1-b"]).toBe("2026-09-04");
    expect(omitido["e1-c"]).toBe("2026-10-02");
    expect(omitido["e2-a"]).toBe("2026-10-16");
    expect(omitido["e2-b"]).toBe("2026-12-11");
    const { mapa: explicito } = fechasDe(
      PLAN.map((i) => ({ ...i, espera_externa: false })),
      "2-5"
    );
    expect(explicito).toEqual(omitido);
  });

  it("sin espera NO se inventa un inicio temprano", () => {
    const { r } = fechasDe([{ id: "a", etapa: 1, destacado: false, banda: "M" }], "20+");
    expect(r.fechas[0].inicioTemprano).toBeUndefined();
  });
});

describe("F4 — el multiplicador personal: se aprende del ritmo real, sin inventar", () => {
  // A MANO, la vara: con capacidad "20+" se planifica con 20 h/semana, así que
  // una M (3 h) PROMETE 3/20 x 7 = 1.05 días de calendario = 25.2 horas.
  // Para que el usuario tarde EL DOBLE, sus cierres van cada 2.1 días = 50.4 h
  // = 50 h 24 min. Desde el 03-ago 12:00:
  //   t0 = 03-ago 12:00   (ancla: la primera cumplida NO da muestra)
  //   t1 = 05-ago 14:24   (+50 h 24 min)  → muestra 1
  //   t2 = 07-ago 16:48   (+50 h 24 min)  → muestra 2
  //   t3 = 09-ago 19:12   (+50 h 24 min)  → muestra 3
  // Tres muestras de razón 2.1 / 1.05 = 2.0 exacta → factor M = 2.
  const CIERRES_DOBLE = [
    "2026-08-03T12:00:00.000Z",
    "2026-08-05T14:24:00.000Z",
    "2026-08-07T16:48:00.000Z",
    "2026-08-09T19:12:00.000Z",
  ];
  const hechasM = CIERRES_DOBLE.map((completed_at) => ({ banda: "M" as const, completed_at }));

  it("el usuario cuyas M tardan el DOBLE: su factor M es 2", () => {
    const f = factorPorBanda({ hechas: hechasM, capacidad: "20+" });
    expect(f.M).toBeCloseTo(2, 6);
  });

  it("y su recálculo lo refleja: las mismas tareas se reparten con las horas reales", () => {
    // A MANO, capacidad "5-10" (5 h/sem), etapa 1 con dos M:
    //   SIN factor: 3 h → ceil(3/5)-1 = 0 → semana 1 (vie 14-ago)
    //               6 h → ceil(6/5)-1 = 1 → semana 2 (vie 21-ago)
    //   CON factor 2 (una M son 6 h para este usuario):
    //               6 h  → ceil(6/5)-1  = 1 → semana 2 (vie 21-ago)
    //               12 h → ceil(12/5)-1 = 2 → semana 3 (vie 28-ago)
    const items: ItemEmpaquetable[] = [
      { id: "a", etapa: 1, destacado: false, banda: "M" },
      { id: "b", etapa: 1, destacado: false, banda: "M" },
    ];
    const sin = empaquetarFechas({ ancla: ANCLA, items, capacidad: "5-10" });
    const con = empaquetarFechas({ ancla: ANCLA, items, capacidad: "5-10", factores: { M: 2 } });
    const m = (r: typeof sin) => Object.fromEntries(r.fechas.map((f) => [f.id, f.fecha]));
    expect(m(sin)).toEqual({ a: "2026-08-14", b: "2026-08-21" });
    expect(m(con)).toEqual({ a: "2026-08-21", b: "2026-08-28" });
  });

  it("SIN muestras: el mapa sale vacío y el empaquetado no cambia una sola fecha", () => {
    expect(factorPorBanda({ hechas: [], capacidad: "5-10" })).toEqual({});
    const items: ItemEmpaquetable[] = [{ id: "a", etapa: 1, destacado: false, banda: "M" }];
    const sin = empaquetarFechas({ ancla: ANCLA, items, capacidad: "5-10" });
    const conVacio = empaquetarFechas({ ancla: ANCLA, items, capacidad: "5-10", factores: {} });
    expect(conVacio.fechas).toEqual(sin.fechas);
  });

  it("con MENOS de 3 muestras no se aprende nada (dos tareas no son un patrón)", () => {
    // Los mismos cierres, recortados a tres cumplidas = solo DOS muestras.
    const f = factorPorBanda({ hechas: hechasM.slice(0, 3), capacidad: "20+" });
    expect(f.M).toBeUndefined();
    expect(MIN_MUESTRAS_FACTOR).toBe(3);
  });

  it("la banda sin muestras no contagia a la que sí las tiene", () => {
    // Tres muestras de M (factor 2) y ninguna de L: L no aparece, y en el
    // empaquetado se comporta como factor 1.
    const f = factorPorBanda({ hechas: hechasM, capacidad: "20+" });
    expect(f.M).toBeCloseTo(2, 6);
    expect(f.L).toBeUndefined();
  });

  it("las tareas con ESPERA EXTERNA no ensucian el factor (su reloj lo mueven otros)", () => {
    // Entre t0 y t1 se cuela una tarea con espera cerrada 30 días después: si
    // contara, arrastraría el factor M por las nubes. Se excluye, y quedan las
    // muestras limpias de razón 2.
    const conEspera = [
      { banda: "M" as const, completed_at: "2026-08-03T12:00:00.000Z" },
      { banda: "M" as const, completed_at: "2026-08-05T14:24:00.000Z" },
      { banda: "M" as const, completed_at: "2026-08-07T16:48:00.000Z" },
      { banda: "M" as const, completed_at: "2026-08-09T19:12:00.000Z" },
      { banda: "M" as const, completed_at: "2026-09-10T19:12:00.000Z", espera_externa: true },
    ];
    expect(factorPorBanda({ hechas: conEspera, capacidad: "20+" }).M).toBeCloseTo(2, 6);
  });

  it("una vacación no reescribe el calendario: manda la mediana, no la media", () => {
    // A MANO: cuatro muestras de M. Tres de 2.1 días (razón 2) y una de 42 días
    // (razón 40) por un hueco largo. La MEDIA sería (2+2+2+40)/4 = 11.5, que a
    // 3 h la M daría 34.5 h por tarea: absurdo. La MEDIANA de [2,2,2,40] es 2.
    const conHueco = [
      { banda: "M" as const, completed_at: "2026-08-03T12:00:00.000Z" },
      { banda: "M" as const, completed_at: "2026-08-05T14:24:00.000Z" }, // razón 2
      { banda: "M" as const, completed_at: "2026-08-07T16:48:00.000Z" }, // razón 2
      { banda: "M" as const, completed_at: "2026-08-09T19:12:00.000Z" }, // razón 2
      { banda: "M" as const, completed_at: "2026-09-20T19:12:00.000Z" }, // razón 40
    ];
    expect(factorPorBanda({ hechas: conHueco, capacidad: "20+" }).M).toBeCloseTo(2, 6);
  });

  it("el factor se acota: ni un dato sucio dispara el plan a un año, ni lo colapsa", () => {
    // Tres cierres separados un año → razones enormes; el techo las corta en 4.
    const lentisimo = [
      { banda: "S" as const, completed_at: "2026-01-01T12:00:00.000Z" },
      { banda: "S" as const, completed_at: "2026-05-01T12:00:00.000Z" },
      { banda: "S" as const, completed_at: "2026-09-01T12:00:00.000Z" },
      { banda: "S" as const, completed_at: "2027-01-01T12:00:00.000Z" },
    ];
    expect(factorPorBanda({ hechas: lentisimo, capacidad: "2-5" }).S).toBe(FACTOR_MAX);

    // Cuatro cerradas el MISMO día → razón 0; el piso las sube a 0.5.
    const todasDeGolpe = [
      { banda: "S" as const, completed_at: "2026-08-03T09:00:00.000Z" },
      { banda: "S" as const, completed_at: "2026-08-03T09:00:00.000Z" },
      { banda: "S" as const, completed_at: "2026-08-03T09:00:00.000Z" },
      { banda: "S" as const, completed_at: "2026-08-03T09:00:00.000Z" },
    ];
    expect(factorPorBanda({ hechas: todasDeGolpe, capacidad: "2-5" }).S).toBe(FACTOR_MIN);
  });

  it("las tareas sin banda o sin fecha de cierre no cuentan", () => {
    const sucias = [
      { banda: null, completed_at: "2026-08-03T12:00:00.000Z" },
      { banda: "M" as const, completed_at: null },
      { banda: "M" as const, completed_at: "no es una fecha" },
      ...hechasM,
    ];
    expect(factorPorBanda({ hechas: sucias, capacidad: "20+" }).M).toBeCloseTo(2, 6);
  });
});

describe("bordes que no pueden reventar en producción", () => {
  it("lista vacía → sin fechas", () => {
    const r = empaquetarFechas({ ancla: ANCLA, items: [], capacidad: "5-10" });
    expect(r.fechas).toEqual([]);
  });

  it("las etapas se ordenan aunque lleguen desordenadas", () => {
    // A MANO, capacidad 20: la etapa 1 (M) abre en la semana 1 → 14-ago; puerta →
    // la etapa 2 (M) abre en la semana 2 → 21-ago. El orden de ENTRADA no manda.
    const { mapa } = fechasDe(
      [
        { id: "e2", etapa: 2, destacado: false, banda: "M" },
        { id: "e1", etapa: 1, destacado: false, banda: "M" },
      ],
      "20+"
    );
    expect(mapa["e1"]).toBe("2026-08-14");
    expect(mapa["e2"]).toBe("2026-08-21");
  });

  it("etapas no consecutivas (1 y 3) se encadenan igual: la puerta es el orden, no el número", () => {
    // A MANO, capacidad 20: la etapa 1 abre en la semana 1 (14-ago) y la etapa 3
    // es la siguiente que existe → abre en la semana 2 (21-ago). No se inventan
    // semanas vacías por el hueco de numeración.
    const { mapa } = fechasDe(
      [
        { id: "a", etapa: 1, destacado: false, banda: "M" },
        { id: "c", etapa: 3, destacado: false, banda: "M" },
      ],
      "20+"
    );
    expect(mapa["a"]).toBe("2026-08-14");
    expect(mapa["c"]).toBe("2026-08-21");
  });

  it("devuelve una fecha por tarea, en el orden de entrada", () => {
    const r = empaquetarFechas({ ancla: ANCLA, items: PLAN, capacidad: "5-10" });
    expect(r.fechas.map((f) => f.id)).toEqual(PLAN.map((i) => i.id));
  });

  it("el ancla a media semana no adelanta nada: manda la semana, no el día", () => {
    // A MANO: ancla miércoles 05-ago (misma semana ISO que el lunes 03-ago). La
    // etapa 1 sigue abriendo en la semana 1 → viernes 14-ago, igual que con el
    // ancla del lunes. Y el lunes de la destacada (10-ago) JAMÁS cae antes del
    // ancla: es el borde por el que la primera etapa no arranca en la semana 0.
    const r = empaquetarFechas({
      ancla: "2026-08-05T09:00:00",
      items: [
        { id: "d", etapa: 1, destacado: true, banda: "S" },
        { id: "a", etapa: 1, destacado: false, banda: "M" },
      ],
      capacidad: "5-10",
    });
    const mapa = Object.fromEntries(r.fechas.map((f) => [f.id, f.fecha]));
    expect(mapa["a"]).toBe("2026-08-14");
    expect(mapa["d"]).toBe("2026-08-10");
    expect(mapa["d"] > "2026-08-05").toBe(true);
  });
});
