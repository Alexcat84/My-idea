// Integración del mundo 11 (decisiones del fundador, 28 sep 2026): ningún texto
// que vea o reciba el cliente habla con voz de libro ("el libro", "el texto",
// "el autor", "the book") ni lleva marcas de auditoría de la extracción (rutas
// de archivo, números de línea, "UNIDAD DE ORIGEN", identificadores de regla
// como "D.27"). Las reglas viven en i18n/frasesProhibidas.ts (vozDeLibro y
// marcasInternas) y ya corren sobre los catálogos y las etiquetas en los once
// idiomas; aquí se barre el TEXTO DE LOS NODOS que llega a la IA o a la pantalla
// (docs/fidelidad/CAMPOS_QUE_LLEGAN.md) y las preguntas en caché.
//
// El pack del mundo 11 no entra en esta prueba hasta que se integra (entonces ya
// está en el grafo vivo); su barrido en rojo antes de limpiarlo es
// scripts/saneamiento/vozDelPack.ts, con su salida guardada como evidencia.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { CAMPOS_DE_CLIENTE, faltasDeCliente, faltasDeNodo } from "./vozDeCliente";

const ASSETS = path.join(__dirname, "assets");
const grafo = JSON.parse(readFileSync(path.join(ASSETS, "master_graph.json"), "utf8")) as {
  nodos: Record<string, Record<string, unknown>>;
};
const cache = JSON.parse(readFileSync(path.join(ASSETS, "preguntas_cache.json"), "utf8")) as Record<string, unknown>;

describe("la voz de cliente: ni voz de libro ni marcas de auditoría", () => {
  it("dos fragmentos reales del pack del mundo 11, antes de limpiarlo, caen (en rojo primero)", () => {
    const resumen =
      "UNIDAD DE ORIGEN: fuentes/scott_radical_candor/cap_13.md, unidad Afterword. Sale de las lineas 187 a 198. " +
      "POR QUE ES PROCEDIMIENTO Y NO UNA POSTURA, con D.27 delante: el propio libro dice en la linea 189 que...";
    const paso = "Ve a la reunion general que ya existe. El texto lo dice asi: We would utilize the inspectors.";
    const reglas = (t: string) => [...new Set(faltasDeCliente(t).map((f) => f.regla))].sort();
    expect(reglas(resumen)).toEqual(["marcasInternas", "vozDeLibro"]);
    expect(reglas(paso)).toEqual(["vozDeLibro"]);
    expect([
      ...new Set(faltasDeNodo({ node_id: "x", pasos_accionables: [paso], resumen_teorico: resumen }).map((f) => f.campo)),
    ]).toEqual(["resumen_teorico", "pasos_accionables[0]"]);
  });

  it("barre todos los campos que llegan a la IA o a la pantalla", () => {
    expect([...CAMPOS_DE_CLIENTE].sort()).toEqual(
      ["condiciones_activacion", "entregable_esperado", "etiqueta_arbol", "pasos_accionables", "resumen_teorico", "titulo_concepto"].sort()
    );
  });

  it("ningún nodo vivo del grafo de la web la rompe", () => {
    const hallazgos = Object.values(grafo.nodos).flatMap((n) =>
      faltasDeNodo(n).map((f) => `${f.node_id}.${f.campo} [${f.regla}] "${f.texto}"`)
    );
    expect(hallazgos).toEqual([]);
  });

  it("ninguna pregunta en caché la rompe", () => {
    const hallazgos = Object.entries(cache).flatMap(([nid, v]) =>
      faltasDeCliente(JSON.stringify(v)).map((f) => `${nid} [${f.regla}] "${f.texto}"`)
    );
    expect(hallazgos).toEqual([]);
  });
});
