/**
 * LA GUARDIA DE VIGENCIA de las etiquetas del riel (decisión del fundador,
 * 25 sep 2026). Cada etiqueta traducida guarda la HUELLA del texto español del
 * que salió (lib/i18n/etiquetas/huellas/<idioma>.json). Si el español cambia,
 * esta prueba falla hasta que se vuelva a traducir esa etiqueta.
 *
 * Por qué: la sesión del dataset corrigió 41 etiquetas en español (6871a11e y
 * 0f46772d) y sus traducciones a los diez idiomas ya estaban hechas con el
 * español viejo. Nada lo detectaba: la guardia de F5 solo exigía que existiera
 * una traducción, no que fuera de ESTE español. Una traducción vencida pasaba.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { cargarGrafo } from "../engine/graph";
import { ETIQUETAS_RIEL, type IdiomaDerivado } from "./etiquetasRiel";
import { etiquetasVencidas, huellaDe } from "./vigenciaEtiquetas";

describe("la guardia detecta una traducción vencida (casos de juguete)", () => {
  it("el español cambió y la traducción es la vieja: vencida", () => {
    // La traducción se hizo desde "Calcula el Valor Futuro"; el español hoy dice
    // "Calcula el Valor Presente por Franquicia". La huella guardada es la del viejo.
    const vivos = { pvf: "Calcula el Valor Presente por Franquicia" };
    const huellas = { pvf: huellaDe("Calcula el Valor Futuro") };
    expect(etiquetasVencidas(vivos, huellas)).toEqual(["pvf"]);
  });

  it("el español es el mismo del que salió la traducción: vigente", () => {
    const vivos = { pvf: "Calcula el Valor Presente por Franquicia" };
    const huellas = { pvf: huellaDe("Calcula el Valor Presente por Franquicia") };
    expect(etiquetasVencidas(vivos, huellas)).toEqual([]);
  });

  it("una etiqueta sin huella cuenta como vencida (no se sabe de qué español salió)", () => {
    expect(etiquetasVencidas({ a: "Mide tu Margen" }, {})).toEqual(["a"]);
  });

  it("la huella no depende de espacios sobrantes en los extremos", () => {
    expect(huellaDe("  Mide tu Margen ")).toBe(huellaDe("Mide tu Margen"));
    expect(huellaDe("Mide tu Margen")).not.toBe(huellaDe("Mide tu margen"));
  });
});

describe("la guardia sobre el grafo real y las diez traducciones", () => {
  const grafo = cargarGrafo();
  const vivos: Record<string, string> = {};
  for (const [id, n] of Object.entries(grafo)) if (!n.deprecado && n.etiqueta_arbol) vivos[id] = n.etiqueta_arbol;
  const idiomas = Object.keys(ETIQUETAS_RIEL) as IdiomaDerivado[];

  it.each(idiomas)("%s: cada etiqueta traducida es de su español vigente", (idioma) => {
    const ruta = path.join(__dirname, "etiquetas", "huellas", `${idioma}.json`);
    const huellas = JSON.parse(readFileSync(ruta, "utf8")) as Record<string, string>;
    const vencidas = etiquetasVencidas(vivos, huellas);
    expect(vencidas, `vencidas ${vencidas.length}; npx tsx scripts/i18n/etiquetasRiel.ts exportar ${idioma} …`).toEqual([]);
  });
});
