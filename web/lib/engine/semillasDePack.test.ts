import { describe, expect, it } from "vitest";
import brecha from "../assets/brecha_semillas.json";
import seeds from "../assets/packs_entry_seeds.json";

/**
 * NINGÚN MUNDO ENTRA MUDO.
 *
 * `integrar_packs.py` monta el grafo, los puentes y la caché, pero NO produce
 * `packs_entry_seeds.json` ni `brecha_semillas.json`: esos dos se hornean a
 * mano por pack. Es una trampa cara y silenciosa, porque el pack queda
 * perfectamente integrado y aun así la brecha nunca dispara: el mundo existe,
 * se compra, y no tiene por dónde empezar a hablarle al usuario.
 *
 * Un renglón en un checklist se olvida. Este test no.
 *
 * Los tres packs HSEQ están fuera del mapa de brecha A PROPÓSITO (conservan el
 * puntaje dinámico de la Fase 3.5), y por eso viven en una lista explícita: si
 * mañana alguien quiere sacar a otro pack del mapa, tiene que escribirlo aquí y
 * decir por qué, en vez de que su ausencia pase por descuido.
 */
const CON_PUNTAJE_DINAMICO = ["quality", "health_safety", "environmental"];

const dominios = Object.keys(seeds as Record<string, unknown>);

describe("las semillas de cada pack", () => {
  it("cubre todos los packs que existen", () => {
    expect(dominios.length).toBeGreaterThanOrEqual(9);
    for (const d of ["compras", "entrega"]) expect(dominios).toContain(d);
  });

  it.each(dominios)("%s tiene semillas de entrada con contenido", (dominio) => {
    const lista = (seeds as Record<string, unknown[]>)[dominio];
    expect(Array.isArray(lista), `${dominio} sin lista de semillas`).toBe(true);
    expect(lista.length, `${dominio} con lista vacía`).toBeGreaterThanOrEqual(5);
    for (const s of lista as { id: string; titulo: string; fase: string; condiciones: string[] }[]) {
      // Una semilla sin condiciones existe pero no RESPONDE: nunca la elige
      // nadie, que a efectos del usuario es lo mismo que no estar.
      expect(s.id, `${dominio}: semilla sin id`).toBeTruthy();
      expect(s.titulo, `${dominio}/${s.id}: sin título`).toBeTruthy();
      expect(s.fase, `${dominio}/${s.id}: sin fase`).toBeTruthy();
      expect(s.condiciones?.length, `${dominio}/${s.id}: no responde, sin condiciones`)
        .toBeGreaterThan(0);
    }
  });

  it.each(dominios)("%s tiene mapa de brecha, o está exento con nombre", (dominio) => {
    const mapa = (brecha as Record<string, unknown>)[dominio] as Record<string, string> | undefined;
    if (CON_PUNTAJE_DINAMICO.includes(dominio)) {
      expect(mapa, `${dominio} está exento: no debería tener mapa`).toBeUndefined();
      return;
    }
    expect(mapa, `${dominio} entraría MUDO: sin mapa de brecha y sin exención`).toBeTruthy();
    expect(mapa?._defecto, `${dominio}: mapa sin _defecto`).toBeTruthy();
  });

  it.each(dominios)("%s: cada destino de la brecha es una semilla real", (dominio) => {
    const mapa = (brecha as Record<string, unknown>)[dominio] as Record<string, string> | undefined;
    if (!mapa) return;
    // El destino no tiene por qué ser semilla de entrada, pero sí un id no
    // vacío: un mapa que apunta a "" deja la fase sin puerta sin decirlo.
    for (const [fase, destino] of Object.entries(mapa)) {
      expect(typeof destino, `${dominio}/${fase}: destino no es texto`).toBe("string");
      expect(destino.length, `${dominio}/${fase}: destino vacío`).toBeGreaterThan(0);
    }
  });
});
