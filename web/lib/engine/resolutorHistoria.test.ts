import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { cargarGrafo, etiquetaArbol, resolverId, tituloDeNodo, type Grafo } from "./graph";

/**
 * LA PROMESA DE LA HISTORIA: "un nodo absorbido sigue EXISTIENDO para que su
 * historia resuelva".
 *
 * Estaba a medio cumplir (auditoría del motor, ago 2026): `ids_alias` se
 * escribía en cada fusión, se declaraba en el tipo, y ningún código lo leía.
 * Una referencia histórica caía en `?? nid` y el usuario veía el id crudo.
 *
 * Este archivo es el contrato de que la promesa se cumple entera, y se prueba
 * contra el GRAFO REAL de producción, no contra un fixture: la promesa es sobre
 * los nodos que existen, no sobre los que me convenga inventar.
 */
const graph = cargarGrafo();
const RAIZ = path.resolve(__dirname, "..", "..");
const FUENTE = readFileSync(path.join(RAIZ, "lib", "engine", "graph.ts"), "utf-8");

/** Los alias tal como están en el grafo: alias -> quien lo absorbió. */
function paresDeAlias(): Array<[string, string]> {
  const out: Array<[string, string]> = [];
  for (const [nid, n] of Object.entries(graph as Grafo)) {
    for (const a of n.ids_alias ?? []) if (a !== nid) out.push([a, nid]);
  }
  return out;
}

describe("resolverId — un id de cualquier era", () => {
  it("un nodo activo se resuelve a sí mismo", () => {
    const activo = Object.keys(graph).find((k) => !graph[k].deprecado)!;
    expect(resolverId(activo, graph)).toBe(activo);
  });

  it("TODO alias del grafo resuelve a un nodo que existe", () => {
    const pares = paresDeAlias();
    expect(pares.length).toBeGreaterThan(200); // hoy 285; si cae en picado, algo se borró
    const rotos = pares.filter(([a]) => {
      const r = resolverId(a, graph);
      return r === null || !graph[r];
    });
    expect(rotos, `alias que no resuelven: ${JSON.stringify(rotos.slice(0, 5))}`).toHaveLength(0);
  });

  it("los alias a ids que YA NO SON NODOS también resuelven — la era de la fusión-que-borraba", () => {
    // 77 alias apuntan a ids que no existen como nodo: son renombres de la
    // integración de packs, cuando fusionar borraba en vez de deprecar. Son
    // justo los que caían en el id crudo, y son la razón de este archivo.
    const huerfanos = paresDeAlias().filter(([a]) => !graph[a]);
    expect(huerfanos.length).toBeGreaterThan(50);
    for (const [a] of huerfanos) {
      const r = resolverId(a, graph)!;
      expect(graph[r], `${a} no resolvió`).toBeDefined();
      expect(graph[r].deprecado, `${a} resolvió a un deprecado`).toBeFalsy();
    }
  });

  it("sigue la CADENA: absorbido de una ronda que la ronda siguiente absorbió", () => {
    // 9 alias apuntan a un superviviente que a su vez fue absorbido después
    // (`costo_de_calidad_5` -> `_6` -> el superviviente de la ronda 2 del COQ).
    // Con un solo salto caerían en un deprecado y el usuario vería el título de
    // un nodo que tampoco se ofrece ya.
    //
    // OCHO llegan a un activo. El noveno NO, y es correcto que no llegue:
    // `involucramiento_sindical` -> `involucramiento_sindical_calidad`, que el
    // auditor RETIRÓ DE LA SELECCIÓN. No hay activo al que apuntar porque el
    // concepto se retiró entero, no se fusionó. Lo que se exige entonces es lo
    // único exigible: que el resolutor entregue el eslabón más reciente que
    // EXISTE, con su título, y no el id ni null.
    const cadenas = paresDeAlias().filter(([, sup]) => graph[sup]?.deprecado);
    expect(cadenas.length).toBeGreaterThan(0);
    const sinActivo: string[] = [];
    for (const [a] of cadenas) {
      const r = resolverId(a, graph)!;
      expect(graph[r], `${a} resolvió a algo que no existe`).toBeDefined();
      if (graph[r].deprecado) {
        sinActivo.push(a);
        // aun así tiene que contar una historia legible
        expect(tituloDeNodo(a, graph)).not.toBe(a);
        // y ser el ESLABÓN MÁS RECIENTE, no el punto de partida
        expect(r, `${a} devolvió su propio id en vez de avanzar`).not.toBe(a);
      }
    }
    expect(sinActivo, "apareció una cadena retirada nueva: adjudícala").toEqual([
      "involucramiento_sindical",
    ]);
  });

  it("un deprecado SIN sucesor resuelve a sí mismo, no a null", () => {
    // Los que el auditor retiró de la SELECCIÓN (programas de OSHA, NIOSH,
    // SBREFA, programas estatales): no hay equivalente universal al que
    // apuntar, y no debe haberlo. Pero el nodo conserva su título y su
    // contenido, así que su historia sigue contando algo.
    const reclamados = new Set(paresDeAlias().map(([a]) => a));
    const sinSucesor = Object.keys(graph).filter((k) => graph[k].deprecado && !reclamados.has(k));
    expect(sinSucesor.length).toBeGreaterThan(0);
    for (const nid of sinSucesor) {
      expect(resolverId(nid, graph)).toBe(nid);
      expect(tituloDeNodo(nid, graph)).not.toBe(nid); // tiene título de verdad
    }
  });

  it("un id que jamás existió devuelve null — y ese es el ÚNICO caso", () => {
    // La distinción que importa: `null` significa "esto no es un nodo de
    // ninguna era". Si el resolutor devolviera null para un absorbido, la
    // promesa seguiría rota con otro disfraz.
    expect(resolverId("esto_no_fue_nunca_un_nodo_9x", graph)).toBeNull();
  });
});

describe("la promesa, vista desde donde el usuario mira", () => {
  it("una referencia histórica de CUALQUIER era muestra título, jamás id crudo", () => {
    const pares = paresDeAlias();
    const crudos = pares.filter(([a]) => {
      const e = etiquetaArbol(a, graph);
      const t = tituloDeNodo(a, graph);
      return e === a || t === a;
    });
    expect(
      crudos,
      `estos alias siguen mostrando el id crudo: ${JSON.stringify(crudos.slice(0, 5))}`
    ).toHaveLength(0);
  });

  it("y también la muestra un deprecado citado directamente", () => {
    const dep = Object.keys(graph).filter((k) => graph[k].deprecado);
    expect(dep.length).toBeGreaterThan(100);
    for (const nid of dep) {
      expect(etiquetaArbol(nid, graph), `${nid} muestra su id`).not.toBe(nid);
    }
  });
});

describe("el remache: los sitios que caían al id crudo pasan por el resolutor", () => {
  // Sin esto, el resolutor puede existir perfecto y no estar cableado, que es
  // exactamente la avería que vino a arreglar: una promesa escrita y no leída.
  const leer = (rel: string) => readFileSync(path.join(RAIZ, rel), "utf-8");

  it("juezSesion no arma su material con ids", () => {
    const src = leer("lib/engine/juezSesion.ts");
    expect(src).toContain("tituloDeNodo");
    expect(src, "volvió el acceso directo al grafo").not.toContain("titulo_concepto ?? nid");
  });

  it("recorrido no mete un id en el perfil de sesión", () => {
    const src = leer("lib/engine/recorrido.ts");
    expect(src).toContain("tituloDeNodo(nidActual, graph)");
    expect(src).not.toContain("titulo_concepto ?? nidActual");
  });

  it("etiquetaArbol resuelve antes de leer", () => {
    expect(FUENTE).toMatch(/export function etiquetaArbol[\s\S]{0,200}resolverId/);
  });

  it("el mapa de alias no se reconstruye en cada llamada", () => {
    // 3.835 nodos recorridos por cada título sería un costo escondido en el
    // camino más caliente del motor.
    expect(FUENTE).toContain("if (_alias) return _alias;");
  });
});
