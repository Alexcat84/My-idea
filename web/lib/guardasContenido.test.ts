/**
 * Las guardas de contenido como datos con versión (auditoría final, punto 4, 28 sep 2026): el fichero que copia la
 * forja no puede divergir del código que aplica las guardas. Una sola fuente: el código; el fichero se regenera.
 */
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { FECHA_GUARDAS, guardasContenido, leerGlosario, VERSION_GUARDAS } from "./guardasContenido";
import { PAUTAS_PROCEDENCIA } from "./pautasProcedencia";
import { CAMPOS_DE_CLIENTE, REGLAS_VOZ_DE_NODO } from "./vozDeCliente";
import { REGLAS_VOZ } from "./i18n/frasesProhibidas";

const RAIZ = path.resolve(__dirname, "..", "..");
const FICHERO = path.join(RAIZ, "dataset", "metadata", "guardas_contenido.json");

describe("las guardas de contenido en datos, para la forja", () => {
  it("el fichero existe y coincide con el código (si no, npx tsx scripts/exportar_guardas.ts)", () => {
    expect(existsSync(FICHERO)).toBe(true);
    expect(JSON.parse(readFileSync(FICHERO, "utf8"))).toEqual(JSON.parse(JSON.stringify(guardasContenido(RAIZ))));
  });

  it("lleva versión y todas las reglas de voz, con sus patrones compilables", () => {
    const g = guardasContenido(RAIZ);
    expect(g.version).toBe(VERSION_GUARDAS);
    expect(g.voz.map((r) => r.id)).toEqual(REGLAS_VOZ.map((r) => r.id));
    for (const r of g.voz) {
      for (const lista of Object.values(r.porIdioma)) {
        for (const { patron, flags } of lista) expect(() => new RegExp(patron, flags)).not.toThrow();
      }
    }
  });

  it("la versión 1.1.0 (7 oct 2026) trae las pautas de procedencia (PROXIMOS_PASOS §6, punto 3)", () => {
    expect(VERSION_GUARDAS).toBe("1.1.0");
    expect(FECHA_GUARDAS).toBe("2026-10-07");
    const g = JSON.parse(readFileSync(FICHERO, "utf8"));
    expect(g.version).toBe("1.1.0");
    expect(g.procedencia.map((r: { id: string }) => r.id)).toEqual(PAUTAS_PROCEDENCIA.map((r) => r.id));
    expect(PAUTAS_PROCEDENCIA.map((r) => r.id)).toEqual(["prefijoProcedencia", "atribucionGenerica", "metodoConPersona", "nombrePropio"]);
  });

  it("dice qué reglas de voz se aplican a los campos de un nodo (las de lib/vozDeCliente.ts), para que la forja use la misma vara", () => {
    const g = JSON.parse(readFileSync(FICHERO, "utf8"));
    expect(g.reglas_voz_de_nodo).toEqual(["vozDeLibro", "marcasInternas"]);
    expect(g.reglas_voz_de_nodo).toEqual([...REGLAS_VOZ_DE_NODO]);
    for (const id of g.reglas_voz_de_nodo) expect(g.voz.some((r: { id: string }) => r.id === id), id).toBe(true);
  });

  it("cada pauta de procedencia del fichero compila y distingue sus dos fixtures: caza lo que debe y deja pasar lo limpio", () => {
    const g = JSON.parse(readFileSync(FICHERO, "utf8"));
    const atribucion = g.procedencia.find((r: { id: string }) => r.id === "atribucionGenerica");
    // la atribucion generica cubre los once idiomas de la interfaz
    for (const t of ["Los estudios muestran que funciona", "Studies show it works", "Selon les experts, oui", "Estudos mostram isso", "Studien zeigen das", "Gli studi mostrano che", "研究によると", "研究表明", "연구에 따르면", "تظهر الدراسات", "विशेषज्ञों के अनुसार"])
      expect(atribucion.patrones.some((p: { patron: string; flags: string }) => new RegExp(p.patron, p.flags).test(t)), t).toBe(true);
    const nombre = g.procedencia.find((r: { id: string }) => r.id === "nombrePropio");
    expect(nombre.patrones.map((p: { id: string }) => p.id)).toEqual(["autoria", "basado_en", "segun_nombre", "oficio_nombre", "dijo_nombre", "referencia"]);
    for (const r of g.procedencia) {
      const rx = r.patrones.map((p: { patron: string; flags: string }) => new RegExp(p.patron, p.flags.replace("g", "")));
      const exentos = (r.exentos ?? []).map((p: { patron: string; flags: string }) => new RegExp(p.patron, p.flags.includes("g") ? p.flags : p.flags + "g"));
      const caza = (t: string) => { const limpio = exentos.reduce((acc: string, e: RegExp) => acc.replace(e, ""), t); return rx.some((x: RegExp) => x.test(limpio)); };
      // dice a qué campos de un nodo se aplica: los visibles (el título del concepto es interno), y la pregunta base
      expect(r.campos_de_nodo.length, r.id).toBeGreaterThan(0);
      for (const c of r.campos_de_nodo) expect([...CAMPOS_DE_CLIENTE, "pregunta"], `${r.id}: ${c}`).toContain(c);
      expect(r.campos_de_nodo, r.id).not.toContain("titulo_concepto");
      expect(r.caza.length, r.id).toBeGreaterThan(0);
      expect(r.no_caza.length, r.id).toBeGreaterThan(0);
      for (const t of r.caza) expect(caza(t), `${r.id} debe cazar: ${t}`).toBe(true);
      for (const t of r.no_caza) expect(caza(t), `${r.id} no debe cazar: ${t}`).toBe(false);
    }
  });

  it("el glosario sale entero de su tabla: la fila de 'coger' y la de 'banderas rojas' están", () => {
    const g = leerGlosario(RAIZ);
    expect(g.length).toBeGreaterThanOrEqual(20);
    expect(g.some((f) => f.aparece.includes('"coger"'))).toBe(true);
    expect(g.some((f) => f.aparece.includes('"banderas rojas"'))).toBe(true);
  });
});
