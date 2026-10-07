/**
 * GUARDA UNICA DE PROCEDENCIA (fundador, 30 sep 2026). REGLA DURA, la primera de docs/REGLAS_DE_LA_CASA.md:
 * JAMAS un usuario debe saber, ni poder intuir, de donde provienen las respuestas de la app. Todo origen es
 * control interno.
 *
 * Junta las cuatro guardas que antes vivian separadas (engine/test_fuentes_de_cara.py,
 * lib/assets/sinInternos.test.ts, lib/reglaSinFuentes.test.ts y la parte de procedencia de
 * lib/engine/avisos.test.ts) y exige, en los once idiomas, que ningun texto que el cliente vea o reciba lleve:
 *   - el titulo de un libro de la lista canonica (dataset/metadata/fuentes_canonicas.json);
 *   - una clave interna (fuente, correcciones, citas...) en lo que se copia al navegador;
 *   - un aviso con el ano de la fuente;
 *   - una etiqueta de procedencia ("Sugerencia de My Idea");
 *   - una atribucion generica ("los estudios muestran", "segun los expertos", "la investigacion sugiere"...).
 * Y que toda llamada a la IA lleve la regla de no mencionar ni insinuar el origen.
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { LOCALES } from "./i18n/config";
import { bloquesDeSistema } from "./i18n/idiomaSalida";
import { REGLA_SIN_FUENTES } from "./reglaSinFuentes";
import { avisosNodo, JURISDICCION, VIGENCIA_NODOS } from "./engine/avisos";
import { cargarGrafo } from "./engine/graph";
import { normal, titulosCanonicos, titulosEn } from "./testFixtures/fuentesCanonicas";

const WEB = path.resolve(__dirname, "..");
const RAIZ = path.resolve(WEB, "..");
const ASSETS = path.join(WEB, "lib", "assets");
const CANON = path.join(RAIZ, "dataset", "metadata", "fuentes_canonicas.json");
const CAMPOS_NODO = ["etiqueta_arbol", "resumen_teorico", "entregable_esperado", "pasos_accionables", "condiciones_activacion"];

// ---------------------------------------------------------------- superficies de cara al cliente

function sinComentarios(src: string): string {
  return src.replace(/\/\*[\s\S]*?\*\//g, " ").replace(/(^|[^:"'`])\/\/[^\n]*/g, "$1");
}

function archivos(dir: string, filtro: (p: string) => boolean): string[] {
  const out: string[] = [];
  const recorrer = (d: string): void => {
    for (const e of readdirSync(d)) {
      const p = path.join(d, e);
      if (statSync(p).isDirectory()) recorrer(p);
      else if (filtro(p)) out.push(p);
    }
  };
  if (existsSync(dir)) recorrer(dir);
  return out.sort();
}

interface NodoCrudo { node_id: string; deprecado?: boolean; fuente?: unknown; [k: string]: unknown }

function nodosVivos(): NodoCrudo[] {
  const dir = path.join(RAIZ, "dataset", "nodos");
  return readdirSync(dir).filter((f) => f.endsWith(".json"))
    .map((f) => JSON.parse(readFileSync(path.join(dir, f), "utf-8")) as NodoCrudo)
    .filter((n) => !n.deprecado);
}

/** [donde, texto] de lo que el cliente ve o recibe, salvo el texto de los nodos. */
function textosDeInterfaz(): Array<[string, string]> {
  const out: Array<[string, string]> = [];
  for (const p of archivos(path.join(WEB, "lib", "i18n", "mensajes"), (p) => p.endsWith(".ts") && !p.includes(".test.")))
    out.push([path.relative(RAIZ, p), sinComentarios(readFileSync(p, "utf-8"))]);
  for (const p of archivos(path.join(WEB, "lib", "i18n", "etiquetas"), (p) => p.endsWith(".json") && !p.includes("huellas"))) {
    const d = JSON.parse(readFileSync(p, "utf-8")) as Record<string, unknown>;
    for (const [k, v] of Object.entries(d)) if (typeof v === "string") out.push([`${path.relative(RAIZ, p)}:${k}`, v]);
  }
  const cache = JSON.parse(readFileSync(path.join(ASSETS, "preguntas_cache.json"), "utf-8")) as Record<string, unknown>;
  for (const [k, v] of Object.entries(cache)) out.push([`preguntas_cache:${k}`, JSON.stringify(v)]);
  out.push(["prompts.json", readFileSync(path.join(ASSETS, "prompts.json"), "utf-8")]);
  for (const carpeta of ["app", "lib"])
    for (const p of archivos(path.join(WEB, carpeta), (p) => /\.tsx?$/.test(p) && !p.includes(".test.") && !p.includes(`${path.sep}mensajes${path.sep}`)))
      out.push([path.relative(RAIZ, p), sinComentarios(readFileSync(p, "utf-8"))]);
  return out;
}

/** [donde, texto] de cada campo de un nodo vivo que llega a la pantalla o a la IA. */
function textosDeNodos(nodos: NodoCrudo[]): Array<[string, string]> {
  const out: Array<[string, string]> = [];
  for (const n of nodos)
    for (const c of CAMPOS_NODO) {
      const v = n[c];
      const lista = Array.isArray(v) ? v : v ? [v] : [];
      lista.forEach((t, i) => out.push([`${n.node_id}.${c}${Array.isArray(v) ? `[${i}]` : ""}`, typeof t === "string" ? t : JSON.stringify(t)]));
    }
  return out;
}

const NODOS = nodosVivos();
const INTERFAZ = textosDeInterfaz();
const DE_NODOS = textosDeNodos(NODOS);
const TODOS = [...INTERFAZ, ...DE_NODOS];

// ---------------------------------------------------------------- 1. titulos de libros

describe("procedencia: ningun libro ni autor llega al cliente", () => {
  it("cada fuente de un nodo vivo esta en la lista canonica, y cada nodo vivo tiene etiqueta", () => {
    const canon = JSON.parse(readFileSync(CANON, "utf-8")) as { fuentes: Record<string, unknown> };
    const fallos: string[] = [];
    for (const n of NODOS) {
      for (const f of String(n.fuente ?? "").split(" | ").map((x) => x.trim()).filter(Boolean))
        if (!(f in canon.fuentes)) fallos.push(`${n.node_id}: la fuente no esta en la lista canonica`);
      if (!String(n.etiqueta_arbol ?? "").trim()) fallos.push(`${n.node_id}: sin etiqueta_arbol (la pantalla caeria al titulo)`);
    }
    expect(fallos.slice(0, 10), `${fallos.length} fallos`).toEqual([]);
  });

  it("ningun texto de cara al cliente nombra un libro de la lista canonica (interfaz, etiquetas, preguntas, prompts, codigo y nodos)", () => {
    const titulos = titulosCanonicos();
    expect(titulos.length).toBeGreaterThan(40);
    const canon = JSON.parse(readFileSync(CANON, "utf-8")) as { _adjudicados?: Record<string, unknown> };
    const adjudicados = canon._adjudicados ?? {};
    const fallos: string[] = [];
    for (const [donde, texto] of TODOS)
      for (const t of titulosEn(texto, titulos)) if (!(`${donde}|${t}` in adjudicados)) fallos.push(`${donde}: nombra "${t}"`);
    expect(fallos.slice(0, 10), `${fallos.length} textos nombran un libro`).toEqual([]);
  });
});

// ---------------------------------------------------------------- 2. nada interno en el navegador

const CLAVES_INTERNAS = new Set([
  "fuente", "fuentes", "fuentes_internas", "correcciones", "merged_originals", "cita", "citas",
  "libro", "libros", "autor", "autores", "fichero", "frase", "texto_anterior",
  "notas_extraccion", "texto_anterior_en",
]);
const ASSETS_DE_CLIENTE = new Set(["packs_catalog.json"]);

function clavesInternas(v: unknown, ruta: string, out: string[]): void {
  if (Array.isArray(v)) v.forEach((x, i) => clavesInternas(x, `${ruta}[${i}]`, out));
  else if (v && typeof v === "object")
    for (const [k, x] of Object.entries(v)) {
      if (CLAVES_INTERNAS.has(k)) out.push(`${ruta}.${k}`);
      clavesInternas(x, `${ruta}.${k}`, out);
    }
}

describe("procedencia: nada interno llega al navegador", () => {
  const assetsJson = readdirSync(ASSETS).filter((f) => f.endsWith(".json"));

  it("ningun asset lleva una clave interna ni nombra un libro", () => {
    const titulos = titulosCanonicos();
    const fallos: string[] = [];
    for (const f of assetsJson) {
      const crudo = readFileSync(path.join(ASSETS, f), "utf-8");
      const out: string[] = [];
      clavesInternas(JSON.parse(crudo), f, out);
      if (out.length) fallos.push(`${f}: ${out.length} claves internas, p. ej. ${out.slice(0, 3).join(", ")}`);
      const hallados = titulosEn(crudo, titulos);
      if (hallados.length) fallos.push(`${f}: ${hallados.join(", ")}`);
    }
    expect(fallos).toEqual([]);
  });

  it("ningun componente de cliente importa el grafo, las instrucciones de la IA ni las listas curadas", () => {
    const fuentes = new Map<string, string>();
    for (const d of ["app", "lib", "components"])
      for (const p of archivos(path.join(WEB, d), (p) => /\.tsx?$/.test(p) && !p.includes(".test."))) fuentes.set(p, readFileSync(p, "utf-8"));
    const resolver = (desde: string, spec: string): string | null => {
      const base = spec.startsWith("@/") ? path.join(WEB, spec.slice(2)) : spec.startsWith(".") ? path.resolve(path.dirname(desde), spec) : null;
      if (!base) return null;
      for (const ext of ["", ".ts", ".tsx", "/index.ts", "/index.tsx"]) {
        const c = base + ext;
        if (fuentes.has(c) || (c.endsWith(".json") && existsSync(c))) return c;
      }
      return null;
    };
    const IMPORT = /(?:^|\n)\s*(import|export)(\s+type)?\s[^'"]*?from\s+['"]([^'"]+)['"]|import\(\s*['"]([^'"]+)['"]\s*\)/g;
    const deps = (p: string): string[] => {
      const out: string[] = [];
      for (const m of (fuentes.get(p) ?? "").matchAll(IMPORT)) {
        if (m[2]) continue;
        const r = resolver(p, m[3] ?? m[4]);
        if (r) out.push(r);
      }
      return out;
    };
    const clientes = [...fuentes.entries()].filter(([, s]) => /^\s*(\/\*[\s\S]*?\*\/\s*)?["']use client["']/.test(s)).map(([p]) => p);
    expect(clientes.length).toBeGreaterThan(10);
    const fallos = new Set<string>();
    for (const c of clientes) {
      const visto = new Set<string>();
      const pila: Array<[string, string[]]> = [[c, [c]]];
      while (pila.length) {
        const [p, camino] = pila.pop()!;
        if (visto.has(p)) continue;
        visto.add(p);
        if (p.endsWith(".json")) {
          if (path.dirname(p) === ASSETS && !ASSETS_DE_CLIENTE.has(path.basename(p))) fallos.add(camino.map((x) => path.relative(WEB, x)).join(" > "));
          continue;
        }
        for (const d of deps(p)) pila.push([d, [...camino, d]]);
      }
    }
    expect([...fallos].slice(0, 5), `${fallos.size} caminos de un componente de cliente a un asset interno`).toEqual([]);
  });
});

// ---------------------------------------------------------------- 3. la regla en toda llamada a la IA

describe("procedencia: la IA no menciona ni insinua el origen", () => {
  it("la regla prohibe libros, autores, estudios, investigaciones, expertos y etiquetas de procedencia", () => {
    for (const rx of [/libro/, /autor/, /estudio/, /investigaci/, /experto/, /procedencia/, /insin/])
      expect(REGLA_SIN_FUENTES, String(rx)).toMatch(rx);
    expect(REGLA_SIN_FUENTES).not.toMatch(/sí puedes usarlo \(el ciclo de Deming/);
  });

  // Regla D5 (docs/REGLAS_DE_LA_CASA.md). Desde el 7 oct 2026 (decision del fundador, hallazgo C7 de la auditoria de
  // prompts) la regla ya no pone ejemplos de metodos con nombre: viajaba en toda llamada y le ofrecia a la IA metodos
  // que el material de esa llamada no traia. Lo que se verifica es lo mismo de antes, sin los ejemplos: un metodo se
  // nombra solo si viene en el material, se explica sin atribuirlo a nadie y con su nombre neutro si lo tiene.
  it("D5: un metodo se nombra solo si viene en el material, se explica sin atribuirlo a nadie y con su nombre neutro si lo tiene", () => {
    expect(REGLA_SIN_FUENTES).toMatch(/Un método se nombra solo si viene en el material que recibes/);
    expect(REGLA_SIN_FUENTES).toMatch(/se explica sin atribuirlo a nadie/);
    expect(REGLA_SIN_FUENTES).toMatch(/si tiene un nombre neutro, usa ese/);
    expect(REGLA_SIN_FUENTES).toMatch(/no el que lleva el apellido de una persona/);
    for (const ejemplo of [/PDCA/, /Ishikawa/, /cinco porqués/, /cinco fuerzas/])
      expect(REGLA_SIN_FUENTES, `la regla ya no pone el ejemplo ${ejemplo}`).not.toMatch(ejemplo);
  });

  it("toda llamada lleva la regla, en espanol y en cualquier otro idioma, sin tocar el prompt cacheado", () => {
    for (const idioma of ["es", "en", "ar", null]) {
      const b = bloquesDeSistema("PROMPT", idioma);
      expect(b[0]).toEqual({ type: "text", text: "PROMPT" });
      expect(b[1]).toEqual({ type: "text", text: REGLA_SIN_FUENTES });
      expect(b[2].cache_control).toEqual({ type: "ephemeral", ttl: "1h" });
    }
  });

  it("ninguna llamada a la IA arma su sistema sin bloquesDeSistema", () => {
    const fallos: string[] = [];
    for (const d of ["lib", "app"])
      for (const p of archivos(path.join(WEB, d), (p) => /\.tsx?$/.test(p) && !p.includes(".test."))) {
        const src = readFileSync(p, "utf-8");
        for (const m of src.matchAll(/messages\.(create|stream)\(/g)) {
          const linea = src.slice(src.lastIndexOf("\n", m.index) + 1, m.index).trim();
          if (linea.startsWith("//") || linea.startsWith("*")) continue;
          if (!/system:\s*bloquesDeSistema\(/.test(src.slice(m.index, m.index! + 600))) fallos.push(`${path.relative(WEB, p)}: ${m[0]}`);
        }
      }
    expect(fallos).toEqual([]);
  });
});

// ---------------------------------------------------------------- 4. avisos de la tarjeta

describe("procedencia: los avisos no revelan el origen", () => {
  const graph = cargarGrafo();
  const ids = [...new Set([...Object.keys(VIGENCIA_NODOS), ...Object.keys(JURISDICCION)])];

  it("ningun aviso nombra un libro, en ningun idioma", () => {
    const titulos = titulosCanonicos();
    const fallos: string[] = [];
    for (const id of ids)
      for (const idioma of LOCALES)
        for (const aviso of avisosNodo(id, graph, idioma)) if (titulosEn(aviso, titulos).length) fallos.push(`${id} ${idioma}: "${aviso}"`);
    expect(fallos.slice(0, 5), `${fallos.length} avisos nombran un libro`).toEqual([]);
  });

  it("el aviso de vigencia no lleva ano en ningun idioma: el ano de la fuente es dato interno (fundador, 30 sep 2026)", () => {
    const fallos: string[] = [];
    for (const id of Object.keys(VIGENCIA_NODOS))
      for (const idioma of LOCALES)
        for (const aviso of avisosNodo(id, graph, idioma)) if (/(1[89]|20)\d\d|\{\{/.test(aviso)) fallos.push(`${id} ${idioma}: "${aviso}"`);
    expect(fallos.slice(0, 5), `${fallos.length} avisos con ano`).toEqual([]);
    const id = Object.keys(VIGENCIA_NODOS).find((k) => !JURISDICCION[k])!;
    expect(avisosNodo(id, graph, "es")).toEqual(["Verifica la norma vigente en tu país: estas reglas cambian con el tiempo."]);
  });

  it("la copia web de vigencia no lleva el ano: solo dice que nodos avisan", () => {
    const vista = JSON.parse(readFileSync(path.join(ASSETS, "vigencia.json"), "utf-8")) as { nodos: Record<string, unknown> };
    const conAnio = Object.entries(vista.nodos).filter(([, v]) => JSON.stringify(v).includes("anio"));
    expect(conAnio.length, `${conAnio.length} entradas con ano en la copia web`).toBe(0);
  });
});

// ---------------------------------------------------------------- 5. etiquetas de procedencia

/** La instruccion a la IA cita las frases prohibidas como ejemplo: no es texto de cara al cliente. */
const ES_INSTRUCCION = (donde: string) => donde.replace(/\\/g, "/").endsWith("web/lib/reglaSinFuentes.ts");

/** El prefijo de procedencia en los once idiomas (fundador, 30 sep 2026: el texto visible queda limpio). */
const PREFIJO = /sugerencia de my idea|suggestion (?:from|de|by) my idea|my idea suggest|sugest[aã]o (?:da|de|do) my idea|vorschlag (?:von|aus) my idea|suggerimento (?:di|da) my idea|my idea(?:の提案|の提案|建议|의 제안| का सुझाव)|اقتراح my idea/i;

describe("procedencia: ninguna etiqueta de procedencia", () => {
  it("ningun texto de cara al cliente lleva el prefijo de procedencia, en ningun idioma", () => {
    const fallos = TODOS.filter(([donde, t]) => !ES_INSTRUCCION(donde) && PREFIJO.test(t)).map(([donde]) => donde);
    expect(fallos.slice(0, 10), `${fallos.length} textos con prefijo de procedencia`).toEqual([]);
  });
});

// ---------------------------------------------------------------- 6. atribuciones genericas

/**
 * Atribuir un consejo a estudios, investigaciones, expertos o la literatura insinua un origen (D1). Se dice
 * directamente. Los patrones no muerden las instrucciones al usuario ("busca en la literatura", "segun los datos
 * obtenidos", "no se ha probado con usuarios"): solo la atribucion de un hecho.
 */
const VERBO_ES = "(?:muestra|muestran|demuestra|demuestran|demostr[oó]|demostraron|indica|indican|revela|revelan|sugiere|sugieren|confirma|confirman|ha mostrado|han mostrado|ha demostrado|han demostrado|encontr[oó]|encontraron|señala|señalan)";
const ATRIBUCION: RegExp[] = [
  // espanol
  new RegExp(`\\b(?:un|el|los|varios|algunos|diversos|numerosos|muchos) estudios? ${VERBO_ES}`, "i"),
  new RegExp(`\\b(?:la|las) investigaci(?:ón|on|ones) ${VERBO_ES}`, "i"),
  new RegExp(`\\b(?:la evidencia|la ciencia) ${VERBO_ES}`, "i"),
  /\bseg[uú]n (?:los |las |la |el |diversos |varios |algunos )?(?:expertos|especialistas|estudios|investigaciones|investigaci[oó]n|la literatura|investigadores|autores|analistas|estudios citados)/i,
  /\blos (?:expertos|especialistas|investigadores|analistas) (?:recomiendan|coinciden|sugieren|dicen|afirman|advierten|han encontrado|encontraron)/i,
  /\b(?:est[aá]|ha sido|se ha) (?:demostrado|comprobado) que/i,
  // los otros diez idiomas de la interfaz
  /\b(?:studies|research|evidence) (?:shows?|suggests?|has shown|have shown|proves?|indicates?)\b|\bexperts (?:recommend|agree|say)\b|\baccording to (?:studies|research|experts)\b/i,
  /\b(?:les études|la recherche) (?:montrent|montre|suggèrent|suggère)\b|\bselon (?:les experts|des études|les études)\b/i,
  /\b(?:estudos|a pesquisa) (?:mostram|mostra|sugerem|sugere)\b|\bsegundo (?:especialistas|estudos|os especialistas)\b/i,
  /\b(?:studien|die forschung) (?:zeigen|zeigt|belegen|belegt)\b|\blaut (?:studien|experten)\b|\bexperten empfehlen\b/i,
  /\b(?:gli studi|la ricerca) (?:mostrano|mostra|dimostrano|dimostra|suggeriscono)\b|\bsecondo (?:gli esperti|gli studi|studi)\b/i,
  /研究によると|研究では|専門家によると|研究表明|研究显示|专家建议|据研究|연구에 따르면|전문가들은|تُظهر الدراسات|تظهر الدراسات|وفقًا للدراسات|يقول الخبراء|अध्ययनों से पता|विशेषज्ञों के अनुसार|शोध बताता/,
];

describe("procedencia: ninguna atribucion generica", () => {
  it("ningun texto de cara al cliente atribuye lo que dice a estudios, investigaciones, expertos o la literatura", () => {
    const fallos = TODOS.filter(([donde, t]) => !ES_INSTRUCCION(donde) && ATRIBUCION.some((rx) => rx.test(t))).map(([donde]) => donde);
    expect(fallos.slice(0, 25), `${fallos.length} textos con atribucion generica`).toEqual([]);
  });
});

// ---------------------------------------------------------------- 7. metodos con nombre de persona

/**
 * Regla de procedencia del fundador (1 oct 2026, docs/REGLAS_DE_LA_CASA.md D5): todo lo que presenta la app es consejo
 * de My Idea. Un metodo se nombra y se explica, pero nunca se atribuye ("segun Deming", "como decia Drucker", "Jane
 * Jacobs demostro"), y si tiene nombre neutro se usa ese ("ciclo PDCA", no "ciclo de Deming"). El titulo del concepto
 * es material interno para la IA y no entra. Una persona de la lista solo puede aparecer dentro de un nombre de metodo
 * sin alternativa neutra corriente.
 */
const PERSONAS = /\b(Deming|Shewhart|Juran|Crosby|Taguchi|Heinrich|Drucker|Christensen|Geoffrey Moore|Jacobs|Goodall|Eames|Porter|Feigenbaum|Osterwalder|Fulton Suri|Kotter|Covey|Maslow|Eisenhower)\b/;
// Decision del fundador (1 oct 2026, punto 1): un nombre de metodo con apellido NO es atribucion. En lo que ve el
// cliente se prefiere el nombre neutro cuando existe (ciclo PDCA, trilogia de la calidad, las cuatro etapas del proceso
// creativo); si no existe, el nombre se queda. Estos son los que no tienen nombre neutro corriente.
const METODO_SIN_NEUTRO = /diagramas? de Eames|(?:los )?14 puntos de Deming/gi;
const CAMPOS_VISIBLES = new Set(["etiqueta_arbol", "resumen_teorico", "entregable_esperado", "pasos_accionables", "condiciones_activacion"]);

function personaEn(t: string): string | null {
  const m = t.replace(METODO_SIN_NEUTRO, "").match(PERSONAS);
  return m ? m[1] : null;
}

describe("procedencia: ningun metodo se atribuye a una persona", () => {
  it("ningun campo visible de un nodo vivo nombra a una persona como fuente ni usa un metodo con persona que tiene nombre neutro", () => {
    const fallos = DE_NODOS.filter(([donde]) => CAMPOS_VISIBLES.has(donde.split(".")[1].replace(/\[\d+\]$/, "")))
      .map(([donde, t]) => [donde, personaEn(t)] as const).filter(([, p]) => p).map(([donde, p]) => `${donde}: ${p}`);
    expect(fallos.slice(0, 25), `${fallos.length} campos con una persona`).toEqual([]);
  });
});

// ---------------------------------------------------------------- casos negativos

describe("procedencia: casos negativos (la guarda muerde)", () => {
  it("detecta un titulo, una clave interna y una llamada sin la regla", () => {
    expect(titulosEn("Como dice The Lean Startup, valida antes de construir.", titulosCanonicos())).toEqual(["the lean startup"]);
    const out: string[] = [];
    clavesInternas({ nodos: { x: { fuente: "The Lean Startup - Eric Ries" } } }, "falso", out);
    expect(out).toEqual(["falso.nodos.x.fuente"]);
    expect(normal("Según")).toBe("segun");
  });

  it("detecta el prefijo y las atribuciones, y deja pasar las instrucciones al usuario", () => {
    expect(PREFIJO.test("Sugerencia de My Idea: guarda el comprobante")).toBe(true);
    for (const t of ["Los estudios muestran que escribir ayuda.", "La investigación sugiere que funciona.", "según diversos estudios (Rasmussen)", "Studies show it works.", "Selon les experts, c'est utile."])
      expect(ATRIBUCION.some((rx) => rx.test(t)), t).toBe(true);
    for (const t of ["Investigar la literatura sobre antropología cultural del país", "Confirmar el objetivo según los datos obtenidos", "Una estrategia que no se ha probado con usuarios reales", "aunque todavía no está probado que lo logren"])
      expect(ATRIBUCION.some((rx) => rx.test(t)), t).toBe(false);
  });

  it("detecta la persona como fuente y deja pasar el metodo sin nombre neutro", () => {
    for (const t of ["Como decía Drucker, no hay nada tan inútil", "El ciclo de Deming tiene cuatro pasos", "Deja el Triángulo de Heinrich"])
      expect(personaEn(t), t).not.toBeNull();
    // decision del fundador (1 oct 2026, punto 1): un nombre de metodo con apellido no es atribucion; sin nombre
    // neutro corriente, se queda ("los 14 puntos de Deming")
    for (const t of ["Usa el diagrama de Eames para ver la intersección", "Aplica el ciclo PDCA", "Ordena tus causas con un diagrama de Pareto", "Repasa los 14 puntos de Deming con tu equipo"])
      expect(personaEn(t), t).toBeNull();
  });
});
