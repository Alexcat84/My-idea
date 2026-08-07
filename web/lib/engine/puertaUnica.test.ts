import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { buscarAfines } from "../compass";
import { cargarEntrySeeds, esOfrecible, etiquetaArbol, sucesoresNivel, type Grafo } from "./graph";

const RAIZ = path.resolve(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

/**
 * LA PUERTA ÚNICA DE OFERTA.
 *
 * Ley adoptada en la cirugía de Calidad (ago 2026): todo camino que le proponga
 * un nodo al usuario pasa por `esOfrecible`, y por ningún otro filtro. Antes
 * había dos criterios de dominio escritos por separado (graph.ts y una copia a
 * mano dentro de compass.ts); el de compass ignoraba la deprecación, así que el
 * índice semántico habría seguido ofreciendo nodos ya fundidos.
 *
 * Un criterio de elegibilidad repartido no falla de golpe: falla en el camino
 * que alguien olvidó actualizar, y el síntoma sale semanas después en el
 * recorrido de una persona.
 *
 * Aquí se prueba lo mismo por los TRES caminos contra la MISMA puerta.
 */
const GRAFO: Grafo = {
  vivo: {
    node_id: "vivo", fase_proyecto: "ideacion", dominio: "core",
    titulo_concepto: "Un nodo que sí se ofrece", resumen_teorico: "…",
    nodos_siguientes: ["fundido", "otro_vivo"],
  },
  otro_vivo: {
    node_id: "otro_vivo", fase_proyecto: "ideacion", dominio: "core",
    titulo_concepto: "Otro que sí", resumen_teorico: "…",
  },
  fundido: {
    node_id: "fundido", fase_proyecto: "ideacion", dominio: "core",
    titulo_concepto: "Costo de la Mala Calidad (Cómo se Mide)",
    resumen_teorico: "…", deprecado: true,
  },
};

describe("la puerta única de oferta", () => {
  it("un deprecado no es ofrecible, y uno vivo sí", () => {
    expect(esOfrecible("vivo", GRAFO)).toBe(true);
    expect(esOfrecible("fundido", GRAFO)).toBe(false);
    // y el que no existe tampoco, sin reventar
    expect(esOfrecible("no_existe", GRAFO)).toBe(false);
  });

  it("CAMINO 1 — los sucesores del recorrido no lo ofrecen", () => {
    const s = sucesoresNivel("vivo", GRAFO, new Set());
    expect(s).toContain("otro_vivo");
    expect(s, "el recorrido ofreció un nodo fundido").not.toContain("fundido");
  });

  it("CAMINO 2 — las semillas de entrada no lo ofrecen", () => {
    // Sin grafo devuelve la lista cruda (es lo que hacen los callers viejos);
    // con grafo pasa por la puerta. Una semilla deprecada abriría el recorrido
    // entero por un nodo que ya no se ofrece.
    const grafoConSemilla: Grafo = { ...GRAFO };
    const crudas = cargarEntrySeeds();
    expect(crudas.length).toBeGreaterThan(0);
    for (const s of cargarEntrySeeds(grafoConSemilla)) {
      expect(esOfrecible(s, grafoConSemilla)).toBe(true);
    }
  });

  it("CAMINO 3 — el índice semántico no lo ofrece", () => {
    // buscarAfines() entero no se puede correr aquí: embedQuery necesita clave
    // y red, y sin ellas devuelve [] — un test contra la función completa
    // pasaría en verde SIN PROBAR NADA. Así que se prueba lo que de verdad
    // decide: que el bucle de compass consulta la puerta, y que la puerta
    // funciona con la forma MÍNIMA de nodo que ese camino le pasa (el índice
    // solo carga `dominio`, no el nodo entero).
    const comoLoVeCompass = { fundido: { dominio: "core", deprecado: true },
                              vivo: { dominio: "core" } };
    expect(esOfrecible("fundido", comoLoVeCompass)).toBe(false);
    expect(esOfrecible("vivo", comoLoVeCompass)).toBe(true);

    const compass = leer("lib/compass.ts");
    const bucle = compass.slice(compass.indexOf("for (const { id, score } of puntuados)"),
                                compass.indexOf("return resultados;"));
    expect(bucle, "el bucle del índice no pasa por la puerta").toContain("esOfrecible(id,");
    expect(typeof buscarAfines).toBe("function");
  });

  it("no queda ningún filtro de elegibilidad fuera de la puerta", () => {
    // La copia a mano que vivía en compass.ts es la que hay que impedir que
    // vuelva: un `.dominio ?? "core"` comparado contra la lista de dominios.
    for (const archivo of ["lib/compass.ts", "lib/engine/recorrido.ts",
                           "lib/engine/planRedactor.ts", "lib/engine/puertaAvanzada.ts",
                           "lib/engine/reeleccionPuerta.ts"]) {
      const fuente = leer(archivo);
      expect(fuente, `${archivo} filtra dominio por su cuenta`)
        .not.toMatch(/dominios\??\.\s*includes\([^)]*dominio/);
      expect(fuente, `${archivo} mira deprecado por su cuenta`)
        .not.toMatch(/\.deprecado/);
    }
  });
});

describe("la historia resuelve aunque el nodo esté deprecado", () => {
  it("etiquetaArbol muestra el TÍTULO, jamás el id crudo", () => {
    // El id es uno real de esta cirugía: costo_de_mala_calidad_copq_2, que el
    // auditor excluyó de la fusión, y su gemelo fundido. Si un deprecado
    // dejara de resolver, aquí saldría el identificador en pantalla.
    expect(etiquetaArbol("fundido", GRAFO)).toBe("Costo de la Mala Calidad (Cómo se Mide)");
    expect(etiquetaArbol("fundido", GRAFO)).not.toBe("fundido");
  });

  it("el deprecado sigue en el grafo, con su contenido", () => {
    expect(GRAFO.fundido).toBeDefined();
    expect(GRAFO.fundido.titulo_concepto.length).toBeGreaterThan(0);
    expect(GRAFO.fundido.resumen_teorico.length).toBeGreaterThan(0);
  });
});
