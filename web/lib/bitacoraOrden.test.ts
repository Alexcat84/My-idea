// Decisión del fundador (26 sep 2026), LA BITÁCORA: la PANTALLA va de lo más
// reciente a lo más antiguo, agrupada por mes; los DOCUMENTOS (el .md, el papel
// del PDF y la secuencia del Expediente) van en orden CRONOLÓGICO, del más
// antiguo al más reciente, SIN IMPORTAR el orden en que lleguen las entradas.
//
// Cálculo a mano (AGENTS.md), con las cinco entradas del fixture en hora LOCAL
// y entregadas DESORDENADAS a propósito (a, b, c, d, e):
//   a = 30 dic 2025 10:00   b = 2 ene 2026 09:00   c = 15 nov 2025 12:00
//   d = 2 ene 2026 18:00    e = 5 dic 2025 08:00
// Cronológico ascendente (documentos): c (15 nov) < e (5 dic) < a (30 dic)
//   < b (2 ene 09:00) < d (2 ene 18:00)  →  c, e, a, b, d.
// Días del documento, en ese orden: "15 de noviembre de 2025",
//   "5 de diciembre de 2025", "30 de diciembre de 2025", "2 de enero de 2026".
// Rango del documento: del primero (c) al último (d) →
//   "> Del 15 de noviembre de 2025 al 2 de enero de 2026".
// Pantalla (descendente): el inverso exacto → d, b, a, e, c. Meses, del más
//   reciente al más antiguo, cruzando el cambio de año: "enero de 2026" [d, b],
//   "diciembre de 2025" [a, e], "noviembre de 2025" [c].
import { describe, expect, it } from "vitest";
import { bitacoraCuerpo, bitacoraMarkdown, mesesDeBitacora, ordenCronologico, type EntradaBitacora } from "./bitacoraCliente";
import { expedienteMarkdown, type DatosExpediente } from "./expediente";
import { mesConAno } from "./fechas";

const local = (y: number, m: number, d: number, h: number) => new Date(y, m - 1, d, h).toISOString();
const ent = (fecha: string, texto: string): EntradaBitacora => ({ fecha, texto, peso: "accion", dominio: "core" });

const A = ent(local(2025, 12, 30, 10), "Entrada A del 30 de diciembre");
const B = ent(local(2026, 1, 2, 9), "Entrada B del 2 de enero temprano");
const C = ent(local(2025, 11, 15, 12), "Entrada C del 15 de noviembre");
const D = ent(local(2026, 1, 2, 18), "Entrada D del 2 de enero tarde");
const E = ent(local(2025, 12, 5, 8), "Entrada E del 5 de diciembre");
const DESORDEN = [A, B, C, D, E];

/** Las posiciones de cada aguja en el texto, en el orden dado; todas deben existir. */
function posiciones(texto: string, agujas: string[]): number[] {
  return agujas.map((a) => {
    const i = texto.indexOf(a);
    expect(i, `falta «${a}»`).toBeGreaterThanOrEqual(0);
    return i;
  });
}
const creciente = (xs: number[]) => xs.every((x, i) => i === 0 || xs[i - 1] < x);

describe("mesConAno: el encabezado de mes, en el idioma pedido", () => {
  const SEPT = local(2026, 9, 10, 12);
  it("español: 'septiembre de 2026' (el ejemplo del fundador)", () => {
    expect(mesConAno(SEPT, "es")).toBe("septiembre de 2026");
  });
  it("inglés, japonés, coreano, alemán: el orden natural de cada idioma", () => {
    expect(mesConAno(SEPT, "en")).toBe("September 2026");
    expect(mesConAno(SEPT, "ja")).toBe("2026年9月");
    expect(mesConAno(SEPT, "ko")).toBe("2026년 9월");
    expect(mesConAno(SEPT, "de")).toBe("September 2026");
  });
});

describe("ordenCronologico y mesesDeBitacora", () => {
  it("ordenCronologico: c, e, a, b, d (sin tocar el arreglo de entrada)", () => {
    const copia = [...DESORDEN];
    expect(ordenCronologico(DESORDEN).map((e) => e.texto)).toEqual([C, E, A, B, D].map((e) => e.texto));
    expect(DESORDEN).toEqual(copia);
  });

  it("mesesDeBitacora: lo más reciente primero, un grupo por mes, cruzando el año", () => {
    const meses = mesesDeBitacora(DESORDEN);
    expect(meses.map((m) => mesConAno(m.fecha, "es"))).toEqual(["enero de 2026", "diciembre de 2025", "noviembre de 2025"]);
    expect(meses.map((m) => m.entradas.map((e) => e.texto))).toEqual([
      [D.texto, B.texto],
      [A.texto, E.texto],
      [C.texto],
    ]);
  });

  it("mismo mes y año distinto NO se juntan (enero 2025 y enero 2026 son dos grupos)", () => {
    // enero 2025 (10:00) y enero 2026 (10:00): dos meses, el de 2026 arriba.
    const meses = mesesDeBitacora([ent(local(2025, 1, 20, 10), "viejo"), ent(local(2026, 1, 20, 10), "nuevo")]);
    expect(meses.map((m) => mesConAno(m.fecha, "es"))).toEqual(["enero de 2026", "enero de 2025"]);
  });
});

describe("documentos: orden cronológico, del más antiguo al más reciente", () => {
  it("bitacoraCuerpo ordena los días y las entradas de forma ascendente aunque lleguen desordenadas", () => {
    const md = bitacoraCuerpo(DESORDEN).join("\n");
    expect(
      creciente(
        posiciones(md, ["15 de noviembre de 2025", "5 de diciembre de 2025", "30 de diciembre de 2025", "2 de enero de 2026"]),
      ),
    ).toBe(true);
    expect(creciente(posiciones(md, [C.texto, E.texto, A.texto, B.texto, D.texto]))).toBe(true);
    // Cada día aparece UNA vez (un día desordenado no se parte en dos encabezados).
    expect(md.split("### 2 de enero de 2026").length - 1).toBe(1);
    // El 2 de enero tiene dos entradas: lleva la hora, 09:00 antes que 18:00.
    expect(creciente(posiciones(md, ["**09:00**", "**18:00**"]))).toBe(true);
  });

  it("bitacoraMarkdown: el rango va del más antiguo al más reciente", () => {
    const md = bitacoraMarkdown("Idea", DESORDEN, local(2026, 2, 1, 12));
    expect(md).toContain("> Del 15 de noviembre de 2025 al 2 de enero de 2026");
    expect(creciente(posiciones(md, [C.texto, E.texto, A.texto, B.texto, D.texto]))).toBe(true);
  });

  it("aunque le llegue en el orden de la PANTALLA (descendente), el documento sale ascendente", () => {
    const pantalla = [D, B, A, E, C];
    const md = bitacoraMarkdown("Idea", pantalla, local(2026, 2, 1, 12));
    expect(md).toContain("> Del 15 de noviembre de 2025 al 2 de enero de 2026");
    expect(creciente(posiciones(md, [C.texto, E.texto, A.texto, B.texto, D.texto]))).toBe(true);
  });

  it("el Expediente (.md) lleva la secuencia en orden cronológico", () => {
    const datos: DatosExpediente = {
      nombre: "Idea",
      entradaOriginal: "texto",
      creadaAt: local(2025, 11, 15, 12),
      realizadaAt: null,
      cierreMotivo: null,
      organizadorMd: null,
      ciclos: [],
      acciones: [],
      numerosMd: null,
      mundos: [],
      informeMd: null,
      bitacoraMd: bitacoraCuerpo(DESORDEN).join("\n"),
      generadoAt: local(2026, 2, 1, 12),
    };
    const md = expedienteMarkdown(datos);
    expect(creciente(posiciones(md, [C.texto, E.texto, A.texto, B.texto, D.texto]))).toBe(true);
  });
});
