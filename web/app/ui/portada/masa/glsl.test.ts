/**
 * Guarda de los shaders de la portada. En las muestras de la masa un
 * shader fallo por dos cosas con el mismo nombre, y nadie lo vio porque
 * se revisaron sin navegador. Aqui, sin GPU, se verifica por texto:
 *  - ningun nombre global (uniform, attribute, varying, #define, funcion)
 *    se repite, salvo sobrecargas de funcion con otra firma;
 *  - ninguna variable local tapa un global o una funcion;
 *  - nada choca con palabras de GLSL ni con lo que three.js antepone;
 *  - cada shader declara exactamente los uniformes que el motor le da;
 *  - todo varying que lee el fragmento lo escribe el vertice.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { AJUSTES } from "./calidad";
import {
  FONDO_CSS,
  FRAGMENTO_ACABADO,
  FRAGMENTO_COMPOSICION,
  FRAGMENTO_RESPALDO,
  fragmentoLiquido,
  UNIFORMES_ACABADO,
  UNIFORMES_COMPOSICION,
  UNIFORMES_LIQUIDO,
  UNIFORMES_RESPALDO,
  VERTICE_PANTALLA,
  VERTICE_RESPALDO,
} from "./glsl";

const TIPOS = "(?:float|int|bool|void|[bi]?vec[234]|mat[234]|sampler2D|samplerCube)";

/** Lo que three.js declara antes del codigo de un ShaderMaterial (WebGL2). */
const PREFIJO_THREE = [
  "modelMatrix", "modelViewMatrix", "projectionMatrix", "viewMatrix", "normalMatrix", "cameraPosition",
  "isOrthographic", "position", "normal", "uv", "uv1", "uv2", "uv3", "color", "instanceMatrix",
  "instanceColor", "pc_fragColor", "gl_FragColor", "texture2D", "textureCube", "HIGH_PRECISION",
  "SHADER_TYPE", "SHADER_NAME", "PI", "PI2", "saturate", "toneMapping", "toneMappingExposure",
];

/** Palabras clave, reservadas y funciones integradas de GLSL ES 3.0 que no deben usarse como nombre. */
const GLSL_RESERVADAS = [
  "attribute", "const", "uniform", "varying", "layout", "centroid", "flat", "smooth", "break", "continue",
  "do", "for", "while", "switch", "case", "default", "if", "else", "in", "out", "inout", "float", "int",
  "void", "bool", "true", "false", "invariant", "discard", "return", "struct", "lowp", "mediump", "highp",
  "precision", "sample", "input", "output", "filter", "common", "partition", "active", "patch", "half",
  "fixed", "long", "short", "double", "unsigned", "superp", "sizeof", "cast", "namespace", "using",
  "interface", "class", "union", "enum", "typedef", "template", "this", "goto", "inline", "noinline",
  "public", "static", "extern", "external", "volatile", "resource", "coherent", "restrict", "readonly",
  "writeonly", "noperspective", "subroutine", "asm",
  "texture", "mix", "step", "smoothstep", "clamp", "length", "distance", "normalize", "dot", "cross",
  "reflect", "refract", "pow", "exp", "exp2", "log", "log2", "sin", "cos", "tan", "asin", "acos", "atan",
  "abs", "sign", "floor", "ceil", "fract", "mod", "min", "max", "sqrt", "inversesqrt", "faceforward",
  "radians", "degrees", "round", "trunc", "transpose", "inverse", "determinant", "outerProduct", "any", "all",
];

interface Declaraciones {
  uniformes: string[];
  atributos: string[];
  varyings: string[];
  defines: string[];
  funciones: Array<{ nombre: string; firma: string }>;
  locales: string[];
}

function sinComentarios(fuente: string): string {
  return fuente.replace(/\/\*[\s\S]*?\*\//g, "").replace(/\/\/.*$/gm, "");
}

function leer(fuente: string): Declaraciones {
  const s = sinComentarios(fuente);
  const de = (re: RegExp) => [...s.matchAll(re)].map((m) => m[1]);
  const funciones = [...s.matchAll(new RegExp(`^\\s*${TIPOS}\\s+(\\w+)\\s*\\(([^)]*)\\)\\s*\\{`, "gm"))].map((m) => ({
    nombre: m[1],
    // firma = tipos de los parametros, sin nombres
    firma: m[2]
      .split(",")
      .map((p) => p.trim().split(/\s+/).slice(0, -1).join(" "))
      .join(","),
  }));
  const globales = /^\s*(?:uniform|attribute|varying|precision)\b.*$/gm;
  const cuerpo = s.replace(globales, "");
  return {
    uniformes: de(new RegExp(`\\buniform\\s+${TIPOS}\\s+(\\w+)\\s*;`, "g")),
    atributos: de(new RegExp(`\\battribute\\s+${TIPOS}\\s+(\\w+)\\s*;`, "g")),
    varyings: de(new RegExp(`\\bvarying\\s+${TIPOS}\\s+(\\w+)\\s*;`, "g")),
    defines: de(/^#define\s+(\w+)/gm),
    funciones,
    // declaraciones de variables (y parametros) dentro de funciones
    locales: [...cuerpo.matchAll(new RegExp(`\\b${TIPOS}\\s+(\\w+)\\s*(?=[=;,)])`, "g"))].map((m) => m[1]),
  };
}

function problemas(fuente: string, conPrefijoThree: boolean): string[] {
  const d = leer(fuente);
  const fallas: string[] = [];
  const globales = [...d.uniformes, ...d.atributos, ...d.varyings, ...d.defines];
  const vistos = new Set<string>();
  for (const g of globales) {
    if (vistos.has(g)) fallas.push(`global repetido: ${g}`);
    vistos.add(g);
  }
  const firmas = new Set<string>();
  for (const f of d.funciones) {
    const clave = `${f.nombre}(${f.firma})`;
    if (firmas.has(clave)) fallas.push(`funcion repetida con la misma firma: ${clave}`);
    firmas.add(clave);
    if (vistos.has(f.nombre)) fallas.push(`funcion con nombre de global: ${f.nombre}`);
  }
  const nombresFuncion = new Set(d.funciones.map((f) => f.nombre));
  for (const l of d.locales) {
    if (vistos.has(l)) fallas.push(`local que tapa un global: ${l}`);
    if (nombresFuncion.has(l)) fallas.push(`local que tapa una funcion: ${l}`);
  }
  const prohibidas = new Set([...GLSL_RESERVADAS, ...(conPrefijoThree ? PREFIJO_THREE : [])]);
  for (const nombre of [...globales, ...nombresFuncion, ...d.locales]) {
    if (prohibidas.has(nombre)) fallas.push(`nombre reservado: ${nombre}`);
  }
  return fallas;
}

const liquidos = (Object.keys(AJUSTES) as Array<keyof typeof AJUSTES>).map((nivel) => ({
  nombre: `liquido (${nivel})`,
  fuente: fragmentoLiquido(AJUSTES[nivel]),
}));

const TODOS: Array<{ nombre: string; fuente: string; three: boolean }> = [
  ...liquidos.map((s) => ({ ...s, three: true })),
  { nombre: "vertice pantalla", fuente: VERTICE_PANTALLA, three: true },
  { nombre: "composicion", fuente: FRAGMENTO_COMPOSICION, three: true },
  { nombre: "acabado", fuente: FRAGMENTO_ACABADO, three: true },
  { nombre: "vertice respaldo", fuente: VERTICE_RESPALDO, three: false },
  { nombre: "fragmento respaldo", fuente: FRAGMENTO_RESPALDO, three: false },
];

describe("shaders de la portada: nombres", () => {
  for (const s of TODOS) {
    it(`${s.nombre}: sin repetidos, sin tapados, sin reservados`, () => {
      expect(problemas(s.fuente, s.three)).toEqual([]);
    });
  }

  it("el verificador si detecta un nombre repetido (control de la guarda)", () => {
    const malo = "uniform float uA;\nuniform float uA;\nfloat f(vec3 q) { float f = 1.0; return f; }\n";
    const fallas = problemas(malo, true);
    expect(fallas).toContain("global repetido: uA");
    expect(fallas).toContain("local que tapa una funcion: f");
  });

  it("el verificador si detecta un nombre que three.js ya declara", () => {
    expect(problemas("vec3 normal(vec3 q) { return q; }", true)).toContain("nombre reservado: normal");
  });
});

describe("shaders de la portada: uniformes y varyings", () => {
  const casos: Array<[string, string, readonly string[]]> = [
    ...liquidos.map((s): [string, string, readonly string[]] => [s.nombre, s.fuente, UNIFORMES_LIQUIDO]),
    ["composicion", FRAGMENTO_COMPOSICION, UNIFORMES_COMPOSICION],
    ["acabado", FRAGMENTO_ACABADO, UNIFORMES_ACABADO],
    ["vertice respaldo", VERTICE_RESPALDO, UNIFORMES_RESPALDO],
  ];
  for (const [nombre, fuente, esperados] of casos) {
    it(`${nombre}: declara exactamente los uniformes que el motor le da`, () => {
      expect([...leer(fuente).uniformes].sort()).toEqual([...esperados].sort());
    });
  }

  const pares: Array<[string, string, string]> = [
    ["respaldo", VERTICE_RESPALDO, FRAGMENTO_RESPALDO],
    ["liquido", VERTICE_PANTALLA, fragmentoLiquido(AJUSTES.alto)],
    ["composicion", VERTICE_PANTALLA, FRAGMENTO_COMPOSICION],
  ];
  for (const [nombre, vertice, fragmento] of pares) {
    it(`${nombre}: cada varying del fragmento lo escribe el vertice`, () => {
      const escritos = new Set(leer(vertice).varyings);
      for (const v of leer(fragmento).varyings) expect(escritos.has(v)).toBe(true);
    });
  }
});

describe("fondo del hero", () => {
  it("el degradado CSS del hero es el mismo que pinta el shader", () => {
    const css = readFileSync(path.resolve(__dirname, "..", "..", "landing.css"), "utf-8");
    expect(css).toContain(`background: ${FONDO_CSS};`);
    // y las paradas del shader son las del CSS: #0b0a14 -> #050409 (38 %) -> negro (72 %)
    expect(FRAGMENTO_COMPOSICION).toContain("vec3(11.0, 10.0, 20.0) / 255.0");
    expect(FRAGMENTO_COMPOSICION).toContain("vec3(5.0, 4.0, 9.0) / 255.0");
    expect(FRAGMENTO_COMPOSICION).toContain("r < 0.38");
    expect(FRAGMENTO_COMPOSICION).toContain("(r - 0.38) / 0.34");
  });
});
