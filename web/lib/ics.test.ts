import { describe, expect, it } from "vitest";
import { generarIcs } from "./ics";

const AHORA = new Date("2026-07-30T12:00:00Z");

describe("generarIcs — Nivel 0 del calendario (.ics)", () => {
  const ics = generarIcs({
    nombreIdea: "Mi idea, con comas",
    ahora: AHORA,
    tareas: [
      { id: "t1", texto: "Habla con cinco personas; toma notas", etapa: 2, fechaBase: "2026-08-05T00:00:00Z" },
      { id: "t2", texto: "Publica el video", etapa: 1, fechaBase: "2026-08-10T00:00:00Z" },
    ],
  });

  it("abre y cierra el VCALENDAR con su versión y prodid", () => {
    expect(ics).toContain("BEGIN:VCALENDAR");
    expect(ics).toContain("VERSION:2.0");
    expect(ics).toContain("PRODID:-//My Idea//Calendario//ES");
    expect(ics.trimEnd().endsWith("END:VCALENDAR")).toBe(true);
  });

  it("un VEVENT por tarea, con UID estable y alarma", () => {
    expect(ics.match(/BEGIN:VEVENT/g)).toHaveLength(2);
    expect(ics).toContain("UID:t1@myideaproject.com");
    expect(ics).toContain("UID:t2@myideaproject.com");
    expect(ics.match(/BEGIN:VALARM/g)).toHaveLength(2);
    expect(ics).toContain("TRIGGER:-PT0M");
  });

  it("el evento arranca a las 09:00 local (flotante) de la fecha_base", () => {
    // 2026-08-05 (la hora local del entorno de test define el día; el evento es
    // a las 09:00 de ESE día en hora flotante). Comprobamos el patrón de inicio/fin.
    expect(ics).toMatch(/DTSTART:2026080\dT090000\b/);
    expect(ics).toMatch(/DTEND:2026080\dT093000\b/);
  });

  it("escapa comas y punto y coma en el texto", () => {
    expect(ics).toContain("SUMMARY:Habla con cinco personas\\; toma notas");
  });

  it("DTSTAMP va en UTC con Z", () => {
    expect(ics).toContain("DTSTAMP:20260730T120000Z");
  });

  it("sin tareas: un calendario válido y vacío", () => {
    const vacio = generarIcs({ nombreIdea: "X", tareas: [], ahora: AHORA });
    expect(vacio).toContain("BEGIN:VCALENDAR");
    expect(vacio).not.toContain("BEGIN:VEVENT");
  });
});

describe("generarIcs — [Espacio] en el SUMMARY (T6, D3): la etiqueta de espacio", () => {
  const base = { id: "w1", texto: "Llama a un cliente", etapa: 1, fechaBase: "2026-08-05T00:00:00Z" };
  const uidDe = (s: string) => s.match(/UID:[^\r\n]+/)![0];

  it("con espacio, prefija el SUMMARY con [Espacio] — y el UID NO cambia", () => {
    const con = generarIcs({ nombreIdea: "Idea", ahora: AHORA, tareas: [{ ...base, espacio: "Calidad" }] });
    expect(con).toContain("SUMMARY:[Calidad] Llama a un cliente");
    // el UID sale del id, no del título: mismo evento, sin duplicar en Google (Nivel 1)
    expect(con).toContain("UID:w1@myideaproject.com");
  });

  it("sin espacio, el SUMMARY va sin prefijo (ruido cero)", () => {
    const sin = generarIcs({ nombreIdea: "Idea", ahora: AHORA, tareas: [base] });
    expect(sin).toContain("SUMMARY:Llama a un cliente");
    expect(sin).not.toContain("[");
  });

  it("el UID es IDÉNTICO con y sin etiqueta: cambiar el título NO re-crea el evento", () => {
    const con = generarIcs({ nombreIdea: "Idea", ahora: AHORA, tareas: [{ ...base, espacio: "Calidad" }] });
    const sin = generarIcs({ nombreIdea: "Idea", ahora: AHORA, tareas: [base] });
    expect(uidDe(con)).toBe("UID:w1@myideaproject.com");
    expect(uidDe(con)).toBe(uidDe(sin));
  });

  it("escapa el texto pero conserva el prefijo del espacio", () => {
    const c = generarIcs({
      nombreIdea: "Idea",
      ahora: AHORA,
      tareas: [{ ...base, texto: "Habla; toma notas", espacio: "Calidad" }],
    });
    expect(c).toContain("SUMMARY:[Calidad] Habla\\; toma notas");
  });
});
