// i18n F3, decisión del fundador (24 sep 2026): antes de traducir, se corrige la
// tanda de errores del español que F2 encontró y no tocó (F2_INFORME.md). Esta
// guardia recorre TODOS los catálogos en español y falla ante las faltas de esa
// tanda, para que no vuelvan (ni se traduzcan): palabras que en español
// correcto siempre llevan tilde (el detector del plan, lib/detectorAcentos, más
// las de esta tanda que él no caza), el "--" como raya, el "que que" y los
// plurales armados a mano ("{{u}}s"). Lo que va entre comillas simples es un
// nombre de campo de la API ('numeros'), no texto: se ignora.
import { readdirSync, statSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { describe, expect, it } from "vitest";
import { detectarFaltaDeAcentos } from "../detectorAcentos";
import { pareceCatalogo } from "./auditor";

const DIR = path.join(__dirname, "mensajes");

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    return statSync(p).isDirectory() ? archivos(p) : p.endsWith(".ts") && !p.endsWith(".test.ts") ? [p] : [];
  });
}

// Las de esta tanda que el detector no caza (sin homógrafo válido sin tilde).
const SIN_TILDE = /(?<![\p{L}])(invalid[oa]s?|valid[oa]s?|sesion|accion|vacio|envia|atoro|cuentame|estan|analisis)(?![\p{L}])/giu;
// Frases de la tanda donde "mas", "donde", "que" y "este" iban sin tilde (esas
// palabras sí tienen forma válida sin tilde: solo se vigilan en su frase).
const FRASES = /la mas directa|vender mas|donde estas parado|que es lo que mas|alguna cifra este en|es mas probable/giu;

function faltas(texto: string): string[] {
  // Fuera los nombres de campo ('numeros') y los marcadores ({{dias}}): no son texto.
  const t = texto.replace(/'[^'\s]*'/g, "").replace(/\{\{\w+\}\}(?!s\b)/g, "");
  return [
    ...detectarFaltaDeAcentos(t),
    ...[...t.matchAll(SIN_TILDE)].map((m) => m[0]),
    ...[...t.matchAll(FRASES)].map((m) => m[0]),
    ...(/\s--\s/.test(t) ? ["--"] : []),
    ...(/\bque que\b/i.test(t) ? ["que que"] : []),
    ...(/\}\}s\b/.test(t) ? ["{{…}}s"] : []),
    ...(/\.\.\./.test(t) ? ["..."] : []),
  ];
}

describe("ortografía del español en los catálogos", () => {
  it("la guardia caza lo que debe (casos de la tanda)", () => {
    expect(faltas("cuerpo invalido")).toEqual(["invalido"]);
    expect(faltas("Tus numeros de verdad")).toEqual(["numeros"]);
    expect(faltas("cifras -- revisa")).toEqual(["--"]);
    expect(faltas("Cuántas {{u}}s haces")).toEqual(["{{…}}s"]);
    expect(faltas("Preparando...")).toEqual(["..."]);
    expect(faltas("'numeros' debe ser un objeto")).toEqual([]);
    expect(faltas("Vender más, por ahora, no")).toEqual([]);
    expect(faltas("accion inválida")).toEqual(["accion"]);
    expect(faltas("Etapa {{etapa}}: {{dias}} días")).toEqual([]);
  });

  it("ningún texto en español del catálogo trae una falta de la tanda", { timeout: 60_000 }, async () => {
    const hallazgos: string[] = [];
    for (const archivo of archivos(DIR)) {
      const mod = (await import(pathToFileURL(archivo).href)) as Record<string, unknown>;
      for (const [nombre, valor] of Object.entries(mod)) {
        if (!pareceCatalogo(valor)) continue;
        const recorrer = (x: unknown, ruta: string) => {
          if (typeof x === "string") {
            const f = faltas(x);
            if (f.length) hallazgos.push(`${path.basename(archivo)}:${nombre}${ruta} ${JSON.stringify(f)}`);
          } else if (x && typeof x === "object") for (const [k, v] of Object.entries(x)) recorrer(v, `${ruta}.${k}`);
        };
        recorrer((valor as Record<string, unknown>).es, "");
      }
    }
    expect(hallazgos).toEqual([]);
  });
});
