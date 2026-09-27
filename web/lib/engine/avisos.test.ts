/**
 * Los avisos de la tarjeta (decision del fundador del 26 sep 2026, saneamiento tanda 1; docs/POLITICA_MARCO_PAIS.md):
 * clase B y C de jurisdiccion, y vigencia. La prueba lee las listas curadas tal como las sincroniza
 * scripts/sync_assets_web.py y exige que cada entrada se pueda mostrar en los once idiomas.
 */
import { describe, expect, it } from "vitest";
import { LOCALES } from "../i18n/config";
import { AVISO_NODO } from "../i18n/mensajes/avisoNodo";
import { titulosCanonicos, titulosEn } from "../testFixtures/fuentesCanonicas";
import { avisosNodo, JURISDICCION, VIGENCIA_NODOS } from "./avisos";
import { cargarGrafo } from "./graph";

const graph = cargarGrafo();
const ids = (clase: string) => Object.entries(JURISDICCION).filter(([, j]) => j.clase === clase).map(([id]) => id);

describe("avisos de la tarjeta: jurisdiccion y vigencia", () => {
  it("un nodo de clase B de Estados Unidos avisa el reencuadre", () => {
    const id = ids("B").find((k) => JURISDICCION[k].pais === "US" && !VIGENCIA_NODOS[k]);
    expect(id, "no hay ningun nodo B de EE.UU. sin vigencia en la lista").toBeTruthy();
    expect(avisosNodo(id!, graph, "es")).toEqual(["Ejemplo de Estados Unidos: busca el equivalente en tu país."]);
    expect(avisosNodo(id!, graph, "en")).toEqual(["Example from the United States: look for the equivalent in your country."]);
  });

  it("un nodo de clase C de Estados Unidos avisa la frontera", () => {
    const id = ids("C").find((k) => JURISDICCION[k].pais === "US" && !VIGENCIA_NODOS[k]);
    expect(id).toBeTruthy();
    expect(avisosNodo(id!, graph, "es")).toEqual(["Aplica si operas o vendes en Estados Unidos."]);
    expect(avisosNodo(id!, graph, "fr")).toEqual(["S'applique si tu opères ou vends aux États-Unis."]);
  });

  it("un nodo con vigencia avisa el ano, sin nombrar el libro", () => {
    const id = Object.keys(VIGENCIA_NODOS).find((k) => !JURISDICCION[k] && VIGENCIA_NODOS[k].anio);
    expect(id).toBeTruthy();
    expect(avisosNodo(id!, graph, "es")).toEqual([`Esta información puede haber cambiado desde ${VIGENCIA_NODOS[id!].anio}: verifica la norma vigente en tu país.`]);
  });

  it("REGLA ESTRICTA (fundador, 26 sep 2026): ningun aviso nombra un libro ni su fuente, en ningun idioma", () => {
    const titulos = titulosCanonicos();
    const fallos: string[] = [];
    for (const id of new Set([...Object.keys(VIGENCIA_NODOS), ...Object.keys(JURISDICCION)])) {
      for (const idioma of LOCALES) {
        for (const aviso of avisosNodo(id, graph, idioma)) {
          if (titulosEn(aviso, titulos).length) fallos.push(`${id} ${idioma}: "${aviso}"`);
        }
      }
    }
    expect(fallos.slice(0, 5), `${fallos.length} avisos nombran un libro`).toEqual([]);
  });

  it("caso negativo: un nodo sin pais ni vigencia no avisa nada, y la clase A tampoco", () => {
    const sin = Object.keys(graph).find((k) => !graph[k].deprecado && !JURISDICCION[k] && !VIGENCIA_NODOS[k]);
    expect(avisosNodo(sin!, graph, "es")).toEqual([]);
    for (const id of ids("A").filter((k) => !VIGENCIA_NODOS[k])) expect(avisosNodo(id, graph, "es")).toEqual([]);
  });

  it("cada entrada es de un nodo vivo, y cada pais y cada libro se pueden mostrar en los once idiomas", () => {
    for (const [id, j] of Object.entries(JURISDICCION)) {
      expect(graph[id], id).toBeTruthy();
      expect(graph[id].deprecado, id).not.toBe(true);
      expect(["A", "B", "C"]).toContain(j.clase);
      if (j.clase === "A" || j.pais === "INT") continue;
      const pais = j.pais;
      for (const idioma of LOCALES) expect(AVISO_NODO[idioma].paises[pais], `${id} ${pais} ${idioma}`).toBeTruthy();
    }
    for (const [id, v] of Object.entries(VIGENCIA_NODOS)) {
      expect(graph[id], id).toBeTruthy();
      expect(v.anio === null || (v.anio > 1900 && v.anio < 2100), id).toBe(true);
    }
    for (const idioma of LOCALES) {
      const id = Object.keys(JURISDICCION).find((k) => JURISDICCION[k].clase !== "A") ?? Object.keys(VIGENCIA_NODOS)[0];
      for (const a of avisosNodo(id, graph, idioma)) expect(a).not.toMatch(/\{\{/);
    }
  });
});
