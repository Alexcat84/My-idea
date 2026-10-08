// Decisiones del fundador, LA BITÁCORA:
//  - PANTALLA (LineaBitacora, la usan Bitacora y BitacoraEspacio): lo más
//    reciente ARRIBA (26 sep 2026) en una LISTA CONTINUA, sin encabezados por mes
//    y sin enlaces "Ir al inicio" (27 sep 2026: se quitan).
//  - PAPEL (ContenidoBitacora: el PDF de la bitácora y la secuencia del
//    Expediente): orden cronológico, del más antiguo al más reciente, sin cambios.
//
// Cálculo a mano (AGENTS.md). Fixture en hora LOCAL, llega en orden ascendente
// (como lo entrega el servidor) y también desordenado:
//   c = 15 nov 2025 12:00   e = 5 dic 2025 08:00   a = 30 dic 2025 10:00
//   b = 2 ene 2026 09:00    d = 2 ene 2026 18:00
// Pantalla, descendente y seguida: d, b, a, e, c; ni "enero de 2026" ni ningún
//   otro encabezado de mes, ni un solo enlace "Ir al inicio" (en ningún idioma).
//   El 2 de enero tiene dos entradas: hora "18:00" antes que "09:00".
//   "el día en que empezó todo" es el día MÁS ANTIGUO (15 nov), al final.
// Papel, ascendente: c, e, a, b, d.
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";
import { ACTIVE_LOCALES, type ActiveLocale } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { BITACORA } from "@/lib/i18n/mensajes/bitacora";
import { LineaBitacora } from "./Bitacora";
import { ContenidoBitacora } from "./BitacoraPapel";

const local = (y: number, m: number, d: number, h: number) => new Date(y, m - 1, d, h).toISOString();
const ent = (fecha: string, texto: string): EntradaBitacora => ({ fecha, texto, peso: "accion", dominio: "core" });

const A = ent(local(2025, 12, 30, 10), "Entrada A del 30 de diciembre");
const B = ent(local(2026, 1, 2, 9), "Entrada B del 2 de enero temprano");
const C = ent(local(2025, 11, 15, 12), "Entrada C del 15 de noviembre");
const D = ent(local(2026, 1, 2, 18), "Entrada D del 2 de enero tarde");
const E = ent(local(2025, 12, 5, 8), "Entrada E del 5 de diciembre");
const ASCENDENTE = [C, E, A, B, D];
const DESORDEN = [A, B, C, D, E];

function posiciones(texto: string, agujas: string[]): number[] {
  return agujas.map((a) => {
    const i = texto.indexOf(a);
    expect(i, `falta «${a}»`).toBeGreaterThanOrEqual(0);
    return i;
  });
}
const creciente = (xs: number[]) => xs.every((x, i) => i === 0 || xs[i - 1] < x);
const veces = (texto: string, aguja: string) => texto.split(aguja).length - 1;

const pantalla = (entradas: EntradaBitacora[], idioma: ActiveLocale = "es") =>
  renderToStaticMarkup(
    <IdiomaProvider idioma={idioma}>
      <LineaBitacora entradas={entradas} />
    </IdiomaProvider>,
  );

describe("pantalla: una lista continua, lo más reciente primero", () => {
  for (const [nombre, entrada] of [["ascendente", ASCENDENTE], ["desordenada", DESORDEN]] as Array<[string, EntradaBitacora[]]>) {
    it(`entrada ${nombre}: d, b, a, e, c`, () => {
      const html = pantalla(entrada);
      expect(creciente(posiciones(html, [D.texto, B.texto, A.texto, E.texto, C.texto]))).toBe(true);
    });
  }

  it("los días también bajan: el 2 de enero arriba, el 15 de noviembre abajo; en el día, 18:00 antes que 09:00", () => {
    const html = pantalla(ASCENDENTE);
    expect(
      creciente(posiciones(html, ["2 de enero de 2026", "30 de diciembre de 2025", "5 de diciembre de 2025", "15 de noviembre de 2025"])),
    ).toBe(true);
    expect(creciente(posiciones(html, ["18:00", "09:00"]))).toBe(true);
  });

  // Decisión del fundador (corrida final, 8 oct 2026; revierte la de esa misma mañana): "el día en que empezó todo"
  // es la fecha MÁS ANTIGUA de la lista, la chispa o una tarea declarada como hecha antes. Fixture: la chispa el 30 de
  // diciembre (A); C (15 nov) y E (5 dic) son tareas declaradas antes de la chispa.
  //   → la etiqueta sale UNA vez, entre "15 de noviembre de 2025" (el día más antiguo) y el texto de C;
  //   → no aparece tras "30 de diciembre de 2025".
  it("'el día en que empezó todo' marca el día MÁS ANTIGUO (chispa o tarea declarada antes)", () => {
    const chispa: EntradaBitacora = { ...A, peso: "hito", chispa: true };
    const html = pantalla([C, E, chispa, B, D]);
    const primer = BITACORA.es.pagina.primerDia;
    expect(veces(html, primer)).toBe(1);
    expect(creciente(posiciones(html, ["15 de noviembre de 2025", primer, C.texto]))).toBe(true);
    expect(html.indexOf(primer)).toBeGreaterThan(html.indexOf("30 de diciembre de 2025"));
  });

  it("sin chispa en la lista (p. ej. la bitácora de un mundo) no hay 'primer día'", () => {
    expect(veces(pantalla(ASCENDENTE), BITACORA.es.pagina.primerDia)).toBe(0);
  });

  it("sin encabezados de mes (ni en español ni en inglés)", () => {
    for (const mes of [">enero de 2026<", ">diciembre de 2025<", ">noviembre de 2025<"]) expect(pantalla(ASCENDENTE)).not.toContain(mes);
    for (const mes of ["January 2026", "December 2025", "November 2025"]) expect(pantalla(ASCENDENTE, "en")).not.toContain(mes);
  });

  it.each([...ACTIVE_LOCALES])("%s: ningún encabezado de sección ni enlace 'Ir al inicio' en la lista", (idioma) => {
    const html = pantalla(ASCENDENTE, idioma);
    expect(html).not.toMatch(/<h3/);
    expect(html).not.toMatch(/<section/);
    expect(html).not.toMatch(/href="#/);
    expect(html).not.toContain("↑");
  });
});

describe("papel (PDF y Expediente): orden cronológico", () => {
  for (const [nombre, entrada] of [["desordenada", DESORDEN], ["descendente", [D, B, A, E, C]]] as Array<[string, EntradaBitacora[]]>) {
    it(`entrada ${nombre}: c, e, a, b, d y el rango del más antiguo al más reciente`, () => {
      const html = renderToStaticMarkup(<ContenidoBitacora entradas={entrada} />);
      expect(creciente(posiciones(html, [C.texto, E.texto, A.texto, B.texto, D.texto]))).toBe(true);
      // rango: "Del {{desde}} al {{hasta}}, …" con desde = c y hasta = d
      expect(html).toContain("Del 15 de noviembre de 2025 al 2 de enero de 2026,");
      // los encabezados de día (después del rango), en orden ascendente
      const trasRango = html.slice(html.indexOf("nada se reescribe."));
      expect(
        creciente(posiciones(trasRango, [">15 de noviembre de 2025<", ">5 de diciembre de 2025<", ">30 de diciembre de 2025<", ">2 de enero de 2026<"])),
      ).toBe(true);
    });
  }
});
