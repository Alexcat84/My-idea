/**
 * GUARDA: el contexto completo en cada llamada a la IA (Principio 1, 28 sep 2026; propuesta (b) de la fila 2 de
 * docs/auditoria_final/informes/estado_memoria_contexto.md, encargada por el fundador).
 *
 * Toda llamada a la IA del producto (lib/ y app/, sin las pruebas) lleva el contexto de la persona: la memoria del
 * proyecto y su ficha. El punto unico por el que pasan es lib/costmeter.ts (`llamarClaude` y
 * `llamarClaudeConversacion`, que reciben `opts.contexto` y lo ponen en su bloque con cache de 1 hora). La guarda es
 * ESTRUCTURAL: lee el codigo fuente con el compilador de TypeScript (el que resuelve de verdad a que funcion llama
 * cada llamada, imports y alias incluidos) y sigue el contexto hacia atras:
 *
 *  1. Cada llamada a `llamarClaude` / `llamarClaudeConversacion` debe pasar `contexto` en sus opciones, y no `null`,
 *     `undefined` ni "".
 *  2. Si lo que pasa es un PARAMETRO de la funcion que la envuelve (`consultaAlEspanol(..., contexto = null)`,
 *     `opts.contexto`, `{ contextoProyecto } = params`), esa funcion pasa a ser tambien un punto de llamada a la IA, y
 *     la regla 1 se aplica a TODOS sus llamadores. Asi hasta el sitio donde el contexto se produce (una llamada a
 *     `contextoDeSesion(...)`, el estado de la sesion...). Es lo que caza un envoltorio que llama con contexto pero al
 *     que nadie se lo da: el caso de `prioridad.ts` (llamaba a `consultaAlEspanol` sin el).
 *  3. Una llamada DIRECTA al SDK (`*.messages.create` / `*.messages.stream`) fuera de costmeter.ts se salta el punto
 *     unico: solo vale si su funcion lee un `contexto` que viene de sus parametros (entonces se exige a sus
 *     llamadores, como en 2) o que se produce alli mismo.
 *  4. Una referencia a `llamarClaude*` que no es una llamada (pasarla como callback, guardarla en una variable) no se
 *     puede seguir: falla.
 *
 * Una llamada NUEVA sin contexto hace fallar la guarda, se escriba como se escriba. Las unicas excepciones son las de
 * LISTA_BLANCA, cada una con su porque; una entrada que ya no corresponde a ninguna llamada tambien falla (la lista no
 * se pudre). Fuera de alcance, y dicho: web/scripts/ (arneses de desarrollo y medicion, no el producto).
 *
 * La segunda parte prueba la guarda contra un programa de juguete en memoria: si un dia deja de cazar, se nota aqui.
 */
import { describe, expect, it } from "vitest";
import fs from "node:fs";
import path from "node:path";
import ts from "typescript";

// ---------------------------------------------------------------------------------------------------------------
// La lista blanca: llamadas a la IA que van SIN contexto a sabiendas. Clave: archivo (relativo a web/) y la llamada.
// ---------------------------------------------------------------------------------------------------------------
const LISTA_BLANCA: Array<{ archivo: string; llamada: string; porque: string }> = [
  {
    archivo: "app/api/organizer/route.ts",
    llamada: "llamarClaude",
    porque:
      "El organizador (version JSON) es la primera llamada de una idea: nacerIdea acaba de crear el proyecto en esta " +
      "misma peticion, asi que su memoria esta vacia y no hay ficha ni hilo que pasar. Lo unico que hay es el texto de " +
      "la persona, que ya va entero en el mensaje.",
  },
  {
    archivo: "app/api/organizer/stream/route.ts",
    llamada: "messages.stream",
    porque:
      "El organizador en streaming: el mismo caso que el de JSON (el proyecto nace en esta peticion, memoria vacia). " +
      "Llama al SDK directo porque necesita el stream para encender las secciones del arbol en vivo; limpia los " +
      "guiones el mismo y cobra con registrarUso.",
  },
];

// ---------------------------------------------------------------------------------------------------------------
// El analizador.
// ---------------------------------------------------------------------------------------------------------------
type Hueco = { param: number; prop: string | null };
type Hallazgo = { archivo: string; linea: number; funcion: string; llamada: string; motivo: string };
type Llamada = { archivo: string; linea: number; funcion: string; llamada: string; contexto: string };
type Resultado = { hallazgos: Hallazgo[]; llamadas: Llamada[]; puntos: string[] };

const NOMBRES_PUNTO_UNICO = new Set(["llamarClaude", "llamarClaudeConversacion"]);

function analizar(
  program: ts.Program,
  raiz: string,
  enAlcance: (rel: string) => boolean,
  costmeterRel: string
): Resultado {
  const checker = program.getTypeChecker();
  const rel = (sf: ts.SourceFile) => path.relative(raiz, sf.fileName).split(path.sep).join("/");
  const archivos = program.getSourceFiles().filter((sf) => !sf.isDeclarationFile && enAlcance(rel(sf)));
  const hallazgos: Hallazgo[] = [];
  const llamadas: Llamada[] = [];

  const sinParentesis = (e: ts.Expression): ts.Expression => {
    let x = e;
    while (ts.isParenthesizedExpression(x) || ts.isAsExpression(x) || ts.isNonNullExpression(x) || ts.isSatisfiesExpression(x))
      x = x.expression;
    return x;
  };
  const nombreDe = (n: ts.Node | undefined): string => {
    if (!n) return "(modulo)";
    if ((ts.isFunctionDeclaration(n) || ts.isMethodDeclaration(n)) && n.name) return n.name.getText();
    if ((ts.isArrowFunction(n) || ts.isFunctionExpression(n)) && ts.isVariableDeclaration(n.parent)) return n.parent.name.getText();
    if ((ts.isArrowFunction(n) || ts.isFunctionExpression(n)) && ts.isPropertyAssignment(n.parent)) return n.parent.name.getText();
    return "(funcion anonima)";
  };
  const funcionQueEnvuelve = (n: ts.Node): ts.SignatureDeclaration | undefined => {
    let p = n.parent;
    while (p && !ts.isFunctionLike(p)) p = p.parent;
    return p as ts.SignatureDeclaration | undefined;
  };
  const funcionConNombre = (n: ts.Node): string => {
    let f = funcionQueEnvuelve(n);
    while (f && nombreDe(f) === "(funcion anonima)") f = funcionQueEnvuelve(f);
    return nombreDe(f);
  };
  const donde = (n: ts.Node) => {
    const sf = n.getSourceFile();
    return { archivo: rel(sf), linea: sf.getLineAndCharacterOfPosition(n.getStart()).line + 1, funcion: funcionConNombre(n) };
  };
  const simbolo = (n: ts.Node): ts.Symbol | undefined => {
    const s = ts.isShorthandPropertyAssignment(n.parent) && n.parent.name === n
      ? checker.getShorthandAssignmentValueSymbol(n.parent)
      : checker.getSymbolAtLocation(n);
    return s && s.flags & ts.SymbolFlags.Alias ? checker.getAliasedSymbol(s) : s;
  };

  // Los puntos de llamada a la IA: declaracion -> donde recibe el contexto.
  const puntos = new Map<ts.Node, { hueco: Hueco; nombre: string }>();
  const pendientes: ts.Node[] = [];
  const agregarPunto = (decl: ts.SignatureDeclaration, hueco: Hueco) => {
    const previo = puntos.get(decl);
    if (previo) {
      if (previo.hueco.param !== hueco.param || previo.hueco.prop !== hueco.prop) {
        hallazgos.push({
          ...donde(decl),
          llamada: nombreDe(decl),
          motivo: `el contexto entra por dos sitios distintos (${JSON.stringify(previo.hueco)} y ${JSON.stringify(hueco)}); la guarda no sabe seguirlo`,
        });
      }
      return;
    }
    puntos.set(decl, { hueco, nombre: nombreDe(decl) });
    pendientes.push(decl);
  };
  const huecoDeParametro = (p: ts.ParameterDeclaration, prop: string | null): Hueco => ({
    param: (p.parent as ts.SignatureDeclaration).parameters.indexOf(p),
    prop,
  });

  // Que pasa con el valor del contexto. Devuelve el motivo del fallo, o null si vale. Si viene de un parametro, la
  // funcion dueña se vuelve punto de llamada (regla 2).
  const evaluar = (e: ts.Expression, profundidad = 0): string | null => {
    const x = sinParentesis(e);
    if (profundidad > 8) return null;
    if (x.kind === ts.SyntaxKind.NullKeyword) return "pasa contexto null";
    if (ts.isIdentifier(x) && x.text === "undefined") return "pasa contexto undefined";
    if (ts.isVoidExpression(x)) return "pasa contexto undefined";
    if ((ts.isStringLiteral(x) || ts.isNoSubstitutionTemplateLiteral(x)) && x.text.trim() === "") return "pasa contexto vacio";
    if (ts.isConditionalExpression(x)) return evaluar(x.whenTrue, profundidad + 1) ?? evaluar(x.whenFalse, profundidad + 1);
    if (ts.isBinaryExpression(x) && [ts.SyntaxKind.QuestionQuestionToken, ts.SyntaxKind.BarBarToken].includes(x.operatorToken.kind)) {
      // `a ?? null` vale lo que valga `a` (el respaldo null solo aplica si `a` falta).
      return evaluar(x.left, profundidad + 1);
    }
    if (ts.isIdentifier(x)) {
      const decl = simbolo(x)?.valueDeclaration;
      if (!decl) return null;
      if (ts.isParameter(decl)) {
        agregarPunto(decl.parent as ts.SignatureDeclaration, huecoDeParametro(decl, null));
        return null;
      }
      if (ts.isBindingElement(decl)) {
        const prop = (decl.propertyName ?? decl.name).getText();
        const patron = decl.parent;
        if (ts.isObjectBindingPattern(patron)) {
          if (ts.isParameter(patron.parent)) {
            agregarPunto(patron.parent.parent as ts.SignatureDeclaration, huecoDeParametro(patron.parent, prop));
            return null;
          }
          if (ts.isVariableDeclaration(patron.parent) && patron.parent.initializer) {
            const origen = sinParentesis(patron.parent.initializer);
            const od = ts.isIdentifier(origen) ? simbolo(origen)?.valueDeclaration : undefined;
            if (od && ts.isParameter(od)) {
              agregarPunto(od.parent as ts.SignatureDeclaration, huecoDeParametro(od, prop));
              return null;
            }
          }
        }
        return null; // destructurado de otra cosa: se produce aqui
      }
      if (ts.isVariableDeclaration(decl)) {
        if (!decl.initializer) return null;
        return evaluar(decl.initializer, profundidad + 1);
      }
      return null;
    }
    if (ts.isPropertyAccessExpression(x)) {
      const base = sinParentesis(x.expression);
      const bd = ts.isIdentifier(base) ? simbolo(base)?.valueDeclaration : undefined;
      if (bd && ts.isParameter(bd)) {
        agregarPunto(bd.parent as ts.SignatureDeclaration, huecoDeParametro(bd, x.name.text));
      }
      return null; // de un parametro (seguido) o del estado de la sesion
    }
    return null; // una llamada (contextoDeSesion(...)), una plantilla...: el contexto se produce aqui
  };

  // El argumento que llena el hueco en una llamada concreta.
  const revisarLlamada = (call: ts.CallExpression, hueco: Hueco, nombre: string) => {
    const d = donde(call);
    const falla = (motivo: string) => hallazgos.push({ ...d, llamada: nombre, motivo });
    const arg = call.arguments[hueco.param];
    if (!arg) return falla(hueco.prop ? `no pasa las opciones con '${hueco.prop}'` : "no pasa el contexto");
    if (hueco.prop === null) {
      const m = evaluar(arg);
      llamadas.push({ ...d, llamada: nombre, contexto: arg.getText() });
      return m ? falla(m) : undefined;
    }
    let objeto: ts.Expression = sinParentesis(arg);
    if (ts.isIdentifier(objeto)) {
      const od = simbolo(objeto)?.valueDeclaration;
      if (od && ts.isParameter(od)) {
        agregarPunto(od.parent as ts.SignatureDeclaration, huecoDeParametro(od, hueco.prop));
        llamadas.push({ ...d, llamada: nombre, contexto: `${objeto.getText()} (opciones del llamador)` });
        return;
      }
      if (od && ts.isVariableDeclaration(od) && od.initializer) objeto = sinParentesis(od.initializer);
    }
    if (!ts.isObjectLiteralExpression(objeto)) return falla(`no se puede verificar '${hueco.prop}' (las opciones no son un objeto literal)`);
    const prop = objeto.properties.find(
      (p) => (ts.isPropertyAssignment(p) || ts.isShorthandPropertyAssignment(p)) && p.name.getText() === hueco.prop
    );
    if (!prop) {
      if (objeto.properties.some((p) => ts.isSpreadAssignment(p))) {
        return falla(`'${hueco.prop}' podria venir de un spread; la guarda no lo sigue: escribelo explicito`);
      }
      return falla(`no lleva '${hueco.prop}'`);
    }
    const valor = ts.isPropertyAssignment(prop) ? prop.initializer : (prop as ts.ShorthandPropertyAssignment).name;
    llamadas.push({ ...d, llamada: nombre, contexto: `${hueco.prop}: ${valor.getText()}` });
    const m = evaluar(valor);
    if (m) falla(m);
  };

  // Todas las llamadas del alcance, una vez.
  const todas: Array<{ call: ts.CallExpression; decl: ts.Node | undefined }> = [];
  const crudas: ts.CallExpression[] = [];
  const referencias: ts.Identifier[] = [];
  for (const sf of archivos) {
    const visitar = (n: ts.Node) => {
      if (ts.isCallExpression(n)) {
        todas.push({ call: n, decl: checker.getResolvedSignature(n)?.declaration });
        const c = n.expression;
        if (
          ts.isPropertyAccessExpression(c) &&
          (c.name.text === "create" || c.name.text === "stream") &&
          ts.isPropertyAccessExpression(c.expression) &&
          c.expression.name.text === "messages" &&
          rel(sf) !== costmeterRel
        ) {
          crudas.push(n);
        }
      }
      if (ts.isIdentifier(n) && NOMBRES_PUNTO_UNICO.has(n.text)) referencias.push(n);
      ts.forEachChild(n, visitar);
    };
    visitar(sf);
  }

  // Punto de partida: las dos funciones del punto unico, en costmeter.ts. El hueco: su parametro de opciones.
  const costmeter = archivos.find((sf) => rel(sf) === costmeterRel);
  if (!costmeter) throw new Error(`no encuentro ${costmeterRel}`);
  const base: ts.FunctionDeclaration[] = [];
  costmeter.forEachChild((n) => {
    if (ts.isFunctionDeclaration(n) && n.name && NOMBRES_PUNTO_UNICO.has(n.name.text)) base.push(n);
  });
  if (base.length !== NOMBRES_PUNTO_UNICO.size) throw new Error(`costmeter.ts ya no tiene ${[...NOMBRES_PUNTO_UNICO].join(" y ")}`);
  for (const f of base) {
    const i = f.parameters.findIndex((p) => {
      const t = checker.getNonNullableType(checker.getTypeAtLocation(p));
      return !!t.getProperty("contexto");
    });
    if (i < 0) throw new Error(`${f.name!.text} ya no recibe 'contexto' en sus opciones`);
    puntos.set(f, { hueco: { param: i, prop: "contexto" }, nombre: f.name!.text });
    pendientes.push(f);
  }

  // Regla 3: las llamadas directas al SDK.
  for (const call of crudas) {
    const nombre = `messages.${(call.expression as ts.PropertyAccessExpression).name.text}`;
    const d = donde(call);
    // El contexto que lee la funcion (o las que la envuelven): `x.contexto` o un identificador `contexto`.
    let leido: ts.Expression | undefined;
    for (let f = funcionQueEnvuelve(call); f && !leido; f = funcionQueEnvuelve(f)) {
      const buscar = (n: ts.Node) => {
        if (leido) return;
        if (ts.isPropertyAccessExpression(n) && n.name.text === "contexto") leido = n;
        else if (ts.isIdentifier(n) && n.text === "contexto" && !ts.isPropertyAccessExpression(n.parent)) leido = n;
        else ts.forEachChild(n, buscar);
      };
      const cuerpo = (f as ts.FunctionLikeDeclaration).body;
      if (cuerpo) buscar(cuerpo);
    }
    if (!leido) {
      hallazgos.push({ ...d, llamada: nombre, motivo: "llamada directa al SDK sin contexto" });
      continue;
    }
    llamadas.push({ ...d, llamada: nombre, contexto: leido.getText() });
    const m = evaluar(leido);
    if (m) hallazgos.push({ ...d, llamada: nombre, motivo: m });
  }

  // Reglas 1 y 2, hasta que no aparezcan puntos nuevos.
  const revisados = new Set<ts.Node>();
  while (pendientes.length > 0) {
    pendientes.length = 0;
    for (const { call, decl } of todas) {
      if (!decl || revisados.has(call)) continue;
      const punto = puntos.get(decl);
      if (!punto) continue;
      revisados.add(call);
      revisarLlamada(call, punto.hueco, punto.nombre);
    }
  }

  // Regla 4: las referencias que no son una llamada.
  for (const id of referencias) {
    const decl = simbolo(id)?.valueDeclaration;
    if (!decl || !base.includes(decl as ts.FunctionDeclaration)) continue;
    const p = id.parent;
    const esLlamada = ts.isCallExpression(p) && p.expression === id;
    const esDeclaracion = ts.isFunctionDeclaration(p) && p.name === id;
    const esImportExport = ts.isImportSpecifier(p) || ts.isExportSpecifier(p) || ts.isImportClause(p);
    if (!esLlamada && !esDeclaracion && !esImportExport) {
      hallazgos.push({ ...donde(id), llamada: id.text, motivo: "referencia que no es una llamada (callback o alias): la guarda no la puede seguir" });
    }
  }

  return {
    hallazgos,
    llamadas,
    puntos: [...puntos.entries()].map(([decl, p]) => `${rel(decl.getSourceFile())} › ${p.nombre} ${JSON.stringify(p.hueco)}`),
  };
}

const formato = (h: Hallazgo) => `${h.archivo}:${h.linea} (${h.funcion}) → ${h.llamada}: ${h.motivo}`;

// ---------------------------------------------------------------------------------------------------------------
// 1. El codigo real.
// ---------------------------------------------------------------------------------------------------------------
const WEB = path.resolve(__dirname, "..");

function fuentesDelProducto(): string[] {
  const salida: string[] = [];
  const recorrer = (dir: string) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) recorrer(p);
      else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name) && !e.name.endsWith(".d.ts")) salida.push(p);
    }
  };
  recorrer(path.join(WEB, "lib"));
  recorrer(path.join(WEB, "app"));
  return salida;
}

const enProducto = (rel: string) => /^(lib|app)\//.test(rel) && !/\.test\.tsx?$/.test(rel);

describe("guarda: contexto en toda llamada a la IA", () => {
  const config = ts.readConfigFile(path.join(WEB, "tsconfig.json"), ts.sys.readFile);
  const opciones = ts.parseJsonConfigFileContent(config.config, ts.sys, WEB).options;
  const program = ts.createProgram(fuentesDelProducto(), { ...opciones, noEmit: true, incremental: false });
  const r = analizar(program, WEB, enProducto, "lib/costmeter.ts");
  // Para auditar a mano lo que la guarda ve: GUARDA_DETALLE=1 npx vitest run lib/contextoEnTodaLlamada.test.ts
  if (process.env.GUARDA_DETALLE) {
    console.log(["PUNTOS DE LLAMADA A LA IA", ...r.puntos, "", "LLAMADAS", ...r.llamadas.map((l) => `${l.archivo}:${l.linea} (${l.funcion}) → ${l.llamada} con ${l.contexto}`), "", "SIN CONTEXTO", ...r.hallazgos.map(formato)].join("\n"));
  }

  it("encuentra las llamadas a la IA (si encuentra pocas, la guarda se rompio, no el codigo)", () => {
    // Al 7 oct 2026 hay mas de veinte llamadas a llamarClaude* en lib/ y app/; un numero bajo dice que el
    // compilador dejo de resolverlas (una ruta de tsconfig, un alias) y la guarda pasaria en vacio.
    expect(r.llamadas.length).toBeGreaterThan(20);
    expect(r.llamadas.some((l) => l.archivo === "lib/engine/prioridad.ts" && l.llamada === "consultaAlEspanol")).toBe(true);
    expect(r.llamadas.some((l) => l.archivo === "lib/engine/redactorPlan.ts" && l.llamada === "messages.stream")).toBe(true);
  });

  it("ninguna llamada a la IA va sin contexto, salvo la lista blanca", () => {
    const fuera = r.hallazgos.filter((h) => !LISTA_BLANCA.some((b) => b.archivo === h.archivo && b.llamada === h.llamada));
    expect(fuera.map(formato), "llamadas a la IA sin contexto").toEqual([]);
  });

  it("la lista blanca esta viva: cada entrada corresponde a exactamente una llamada sin contexto, y tiene su porque", () => {
    for (const b of LISTA_BLANCA) {
      expect(b.porque.length, `${b.archivo}: la entrada necesita su porque`).toBeGreaterThan(40);
      const casan = r.hallazgos.filter((h) => h.archivo === b.archivo && h.llamada === b.llamada);
      expect(casan.map(formato), `${b.archivo} › ${b.llamada}`).toHaveLength(1);
    }
  });
});

// ---------------------------------------------------------------------------------------------------------------
// 2. La guarda contra un programa de juguete: caza lo que debe cazar y deja pasar lo que vale.
// ---------------------------------------------------------------------------------------------------------------
describe("guarda: contexto en toda llamada a la IA (prueba de la propia guarda)", () => {
  const RAIZ = path.resolve("/juguete");
  const ARCHIVOS: Record<string, string> = {
    "lib/costmeter.ts": `
      export interface LlamadaOpts { contexto?: string | null; componente?: string }
      export async function llamarClaude(c: unknown, s: string, u: string, m: string, a: unknown, opts: LlamadaOpts = {}) { return { c, s, u, m, a, opts }; }
      export async function llamarClaudeConversacion(c: unknown, s: string, h: unknown[], u: string, m: string, a: unknown, opts: LlamadaOpts = {}) { return { c, s, h, u, m, a, opts }; }
    `,
    "lib/memoria.ts": `export function contextoDeSesion(e: { contextoProyecto?: string | null }): string | null { return e.contextoProyecto ?? null; }`,
    "lib/envoltorio.ts": `
      import { llamarClaude } from "./costmeter";
      export async function traducir(t: string, contexto: string | null = null) { return llamarClaude(null, "s", t, "m", null, { contexto }); }
      export async function conOpciones(t: string, opts: { contexto?: string | null } = {}) { return llamarClaude(null, "s", t, "m", null, { componente: "x", contexto: opts.contexto }); }
      export async function conParams(params: { contextoProyecto?: string | null }) { const { contextoProyecto = null } = params; return llamarClaude(null, "s", "u", "m", null, { contexto: contextoProyecto }); }
    `,
    "app/bien.ts": `
      import { traducir, conOpciones, conParams } from "../lib/envoltorio";
      import { llamarClaude as alias } from "../lib/costmeter";
      import { contextoDeSesion } from "../lib/memoria";
      export async function bien(estado: { contextoProyecto?: string | null }) {
        const contexto = contextoDeSesion(estado);
        await traducir("x", contexto);
        await conOpciones("x", { contexto });
        await conParams({ contextoProyecto: estado.contextoProyecto });
        await alias(null, "s", "u", "m", null, { contexto: contexto ?? null });
      }
      export async function cruda(client: any, opts: { contexto: string | null }) { const content = opts.contexto ? [opts.contexto] : []; return client.messages.stream({ content }); }
      export async function usaCruda(estado: { contextoProyecto?: string | null }) { return cruda(null, { contexto: contextoDeSesion(estado) }); }
    `,
    "app/mal.ts": `
      import { traducir, conOpciones, conParams } from "../lib/envoltorio";
      import { llamarClaude, llamarClaudeConversacion } from "../lib/costmeter";
      import { cruda } from "./bien";
      export async function nuevaSinContexto() { return llamarClaude(null, "s", "u", "m", null, { componente: "nueva" }); }
      export async function conNull() { return llamarClaudeConversacion(null, "s", [], "u", "m", null, { contexto: null }); }
      export async function sinOpciones() { return llamarClaude(null, "s", "u", "m", null); }
      export async function envoltorioSinContexto() { return traducir("x"); }
      export async function envoltorioConUndefined() { return conOpciones("x", { contexto: undefined }); }
      export async function paramsSinContexto() { return conParams({}); }
      export async function crudaSinNada(client: any) { return client.messages.create({ model: "m" }); }
      export async function crudaConNull() { return cruda(null, { contexto: null }); }
      export async function vacia() { const contexto = null; return traducir("x", contexto); }
      export const comoCallback = [llamarClaude];
    `,
  };
  const abs = (rel: string) => path.join(RAIZ, rel);
  const opciones: ts.CompilerOptions = { noLib: true, types: [], strict: true, module: ts.ModuleKind.ESNext, moduleResolution: ts.ModuleResolutionKind.Bundler, target: ts.ScriptTarget.ES2020 };
  const host = ts.createCompilerHost(opciones);
  const virtual = new Map(Object.entries(ARCHIVOS).map(([k, v]) => [path.normalize(abs(k)), v]));
  const leer = (f: string) => virtual.get(path.normalize(f));
  host.fileExists = (f) => virtual.has(path.normalize(f));
  host.readFile = (f) => leer(f);
  host.getSourceFile = (f, lang) => {
    const t = leer(f);
    return t === undefined ? undefined : ts.createSourceFile(f, t, lang, true);
  };
  host.directoryExists = () => true;
  host.getCurrentDirectory = () => RAIZ;
  const program = ts.createProgram(Object.keys(ARCHIVOS).map(abs), opciones, host);
  const r = analizar(program, RAIZ, enProducto, "lib/costmeter.ts");
  const cazadas = new Set(r.hallazgos.map((h) => `${h.archivo} ${h.funcion}`));

  it("caza cada llamada sin contexto, directa o a traves de un envoltorio", () => {
    for (const f of [
      "nuevaSinContexto",
      "conNull",
      "sinOpciones",
      "envoltorioSinContexto",
      "envoltorioConUndefined",
      "paramsSinContexto",
      "crudaSinNada",
      "crudaConNull",
      "vacia",
      "(modulo)",
    ]) {
      expect(cazadas.has(`app/mal.ts ${f}`), `${f} deberia fallar; cazadas: ${[...cazadas].join(", ")}`).toBe(true);
    }
  });

  it("no da por mala ninguna llamada que si lleva contexto, y sigue los envoltorios hasta quien lo produce", () => {
    expect(r.hallazgos.filter((h) => h.archivo !== "app/mal.ts").map(formato)).toEqual([]);
    expect(r.puntos.some((p) => p.includes("traducir"))).toBe(true);
    expect(r.puntos.some((p) => p.includes("conOpciones"))).toBe(true);
    expect(r.puntos.some((p) => p.includes("conParams"))).toBe(true);
    expect(r.puntos.some((p) => p.includes("cruda"))).toBe(true);
  });
});
