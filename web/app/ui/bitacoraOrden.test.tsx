// Decisión del fundador (26 sep 2026), LA BITÁCORA:
//  - PANTALLA (LineaBitacora, la usan Bitacora y BitacoraEspacio): lo más
//    reciente ARRIBA, con encabezados de mes en el idioma de la interfaz y un
//    enlace "Ir al inicio" cuando la lista es larga.
//  - PAPEL (ContenidoBitacora: el PDF de la bitácora y la secuencia del
//    Expediente): orden cronológico, del más antiguo al más reciente.
//
// Cálculo a mano (AGENTS.md). Fixture en hora LOCAL, llega en orden ascendente
// (como lo entrega el servidor) y también desordenado:
//   c = 15 nov 2025 12:00   e = 5 dic 2025 08:00   a = 30 dic 2025 10:00
//   b = 2 ene 2026 09:00    d = 2 ene 2026 18:00
// Pantalla, descendente: d, b, a, e, c. Meses: "enero de 2026" (d, b),
//   "diciembre de 2025" (a, e), "noviembre de 2025" (c): tres encabezados.
//   El 2 de enero tiene dos entradas: hora "18:00" antes que "09:00".
//   "el día en que empezó todo" es el día MÁS ANTIGUO (15 nov), ahora al final.
//   Tres meses = lista larga: un "Ir al inicio" al cierre de cada mes → 3.
// Papel, ascendente: c, e, a, b, d.
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import type { EntradaBitacora } from "@/lib/bitacoraCliente";
import { LOCALES } from "@/lib/i18n/config";
import { IdiomaProvider } from "@/lib/i18n/IdiomaProvider";
import { BITACORA } from "@/lib/i18n/mensajes/bitacora";
import { FECHAS } from "@/lib/i18n/mensajes/fechas";
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

const pantalla = (entradas: EntradaBitacora[], idioma: "es" | "en" = "es") =>
  renderToStaticMarkup(
    <IdiomaProvider idioma={idioma}>
      <LineaBitacora entradas={entradas} />
    </IdiomaProvider>,
  );

describe("pantalla: lo más reciente primero, agrupado por mes", () => {
  for (const [nombre, entrada] of [["ascendente", ASCENDENTE], ["desordenada", DESORDEN]] as Array<[string, EntradaBitacora[]]>) {
    it(`entrada ${nombre}: d, b, a, e, c`, () => {
      const html = pantalla(entrada);
      expect(creciente(posiciones(html, [D.texto, B.texto, A.texto, E.texto, C.texto]))).toBe(true);
    });
  }

  it("tres encabezados de mes, del más reciente al más antiguo, cruzando el año, cada uno una vez", () => {
    const html = pantalla(ASCENDENTE);
    expect(creciente(posiciones(html, ["enero de 2026", "diciembre de 2025", "noviembre de 2025"]))).toBe(true);
    expect(veces(html, ">enero de 2026<")).toBe(1);
    expect(veces(html, ">diciembre de 2025<")).toBe(1);
    expect(veces(html, ">noviembre de 2025<")).toBe(1);
    // Cada mes va ANTES que sus entradas: enero < d < b < diciembre < a < e < noviembre < c
    expect(
      creciente(posiciones(html, [">enero de 2026<", D.texto, B.texto, ">diciembre de 2025<", A.texto, E.texto, ">noviembre de 2025<", C.texto])),
    ).toBe(true);
  });

  it("los días también bajan: el 2 de enero arriba, el 15 de noviembre abajo; en el día, 18:00 antes que 09:00", () => {
    const html = pantalla(ASCENDENTE);
    expect(
      creciente(posiciones(html, ["2 de enero de 2026", "30 de diciembre de 2025", "5 de diciembre de 2025", "15 de noviembre de 2025"])),
    ).toBe(true);
    expect(creciente(posiciones(html, ["18:00", "09:00"]))).toBe(true);
  });

  it("'el día en que empezó todo' sigue marcando el día más antiguo (ahora al final)", () => {
    const html = pantalla(ASCENDENTE);
    const primer = BITACORA.es.pagina.primerDia;
    expect(veces(html, primer)).toBe(1);
    expect(creciente(posiciones(html, ["15 de noviembre de 2025", primer, C.texto]))).toBe(true);
  });

  it("los encabezados de mes siguen el idioma de la interfaz", () => {
    const html = pantalla(ASCENDENTE, "en");
    expect(creciente(posiciones(html, ["January 2026", "December 2025", "November 2025"]))).toBe(true);
    expect(html).not.toContain("enero de 2026");
  });
});

describe("pantalla: el enlace 'Ir al inicio'", () => {
  it("lista larga (tres meses): un 'Ir al inicio' al cierre de cada mes, que apunta al inicio de la lista", () => {
    const html = pantalla(ASCENDENTE);
    expect(BITACORA.es.pagina.irAlInicio).toBe("Ir al inicio");
    expect(veces(html, "Ir al inicio")).toBe(3);
    const ancla = /id="([^"]+)"[^>]*tabindex="-1"|tabindex="-1"[^>]*id="([^"]+)"/.exec(html);
    expect(ancla).not.toBeNull();
    const id = ancla![1] ?? ancla![2];
    expect(veces(html, `href="#${id}"`)).toBe(3);
    // el último está después de la última entrada (al final de la lista)
    expect(html.lastIndexOf("Ir al inicio")).toBeGreaterThan(html.indexOf(C.texto));
  });

  it("lista corta (un mes, dos entradas): sin enlace", () => {
    const html = pantalla([B, D]);
    expect(html).not.toContain("Ir al inicio");
  });

  it("en inglés, con su texto del catálogo", () => {
    expect(pantalla(ASCENDENTE, "en")).toContain(BITACORA.en.pagina.irAlInicio);
  });

  it("los once idiomas tienen su 'Ir al inicio' y su plantilla de mes con año", () => {
    for (const l of LOCALES) {
      expect(BITACORA[l].pagina.irAlInicio.trim(), l).not.toBe("");
      expect(FECHAS[l].mesAno, l).toContain("{{mes}}");
      expect(FECHAS[l].mesAno, l).toContain("{{ano}}");
    }
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
