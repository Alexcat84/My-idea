/**
 * etiquetasCara.test.ts — la ley de la CARA del grafo, en CI.
 *
 * Decisión del fundador (jul 2026): el usuario jamás ve títulos técnicos ni
 * jerga. Ve `etiqueta_arbol`: natural, corta y familiar. `titulo_concepto`
 * queda reservado a forense, digest, bitácora y logs. Dos idiomas: técnico
 * adentro, natural afuera.
 *
 * Este archivo es el guardián permanente de esa ley. No audita una vez: corre
 * sobre las 3.742 etiquetas en cada suite, así que el día que el grafo crezca
 * con una etiqueta jergosa, el commit se cae aquí y no en producción.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { detectarFaltaDeAcentos } from "./detectorAcentos";
import { cargarGrafo, etiquetaArbol } from "./engine/graph";

const RAIZ = path.resolve(import.meta.dirname, "..", "..");
const leerJson = (rel: string) => JSON.parse(readFileSync(path.join(RAIZ, rel), "utf8"));

const graph = cargarGrafo();
const ETIQUETAS = Object.entries(graph).map(([id, n]) => [id, n.etiqueta_arbol ?? ""] as const);

/** El diccionario prohibido de ETIQUETAS_DE_CARA.md §C. `prefijo: true` cuando
 * la familia entera cuenta (pivot/pivote/pivotar), y palabra exacta cuando el
 * término suelto colisionaría con español real ("lean" es también "ellos
 * leen"; "voces" empieza por "voc"). */
const JERGA: Array<{ termino: string; prefijo?: boolean }> = [
  { termino: "canvas" },
  { termino: "pivot", prefijo: true },
  { termino: "equity" },
  { termino: "feedback" },
  { termino: "lead" },
  { termino: "leads" },
  { termino: "benchmark", prefijo: true },
  { termino: "onboarding" },
  { termino: "pitch" },
  { termino: "lean" },
  { termino: "prompt", prefijo: true },
  { termino: "startup", prefijo: true },
  { termino: "funnel" },
  { termino: "scorecard" },
  { termino: "mvp" },
  { termino: "voc" },
  { termino: "crowdfunding" },
  { termino: "kpi" },
  { termino: "kpis" },
];

/** §B: siglas familiares para el público, se conservan. */
const SIGLAS_EXENTAS = new Set(["IA", "CEO", "PIB", "RRHH", "TI", "ISO", "OSHA", "NIOSH", "FODA"]);

/**
 * PENDIENTE DE CURADURÍA (§E.4: reportar, jamás inventar arreglos).
 * Anglicismos que la lista D no cubre y para los que el diccionario de la casa
 * NO prescribe traducción: decidirlos es del fundador y el auditor, no mío.
 * Están DECLARADOS, no escondidos: mientras vivan aquí la suite pasa, pero
 * cualquier etiqueta jergosa NUEVA rompe. Vaciar esta lista cierra el tema.
 */
const ETIQUETAS_PENDIENTES: Record<string, string> = {
  mitos_stage_gate: "Entiende lo que Stage-Gate No Es",
  stage_gate_tipos_proyectos: "Adapta Stage-Gate a tu Proyecto",
};

/** Colisiones exactas que YA existían antes de esta fase, más las dos que la
 * lista D introdujo al unificar el vocabulario. Se congelan tal cual: la
 * curaduría es del fundador y el auditor. Una colisión NUEVA rompe la suite. */
const COLISIONES_CONOCIDAS = [
  "Asegura tu Crédito de Exportación",
  "Construye, Mide y Aprende",
  "Cumple las Reglas Antiboicot",
  "Define tus Términos de Venta",
  "Elige tus Canales de Venta",
  "Mide tu Progreso con Indicadores",
  "Protege tu Propiedad Intelectual",
].sort();

const sinAcentos = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "");
const palabras = (s: string) => s.trim().split(/\s+/).filter(Boolean);

/** Los términos prohibidos que aparecen en una etiqueta (vacío = limpia).
 * OJO con el escapado: en una plantilla, `\b` es un BACKSPACE y no la
 * frontera de palabra. Un detector así no muerde nunca y se ve idéntico a uno
 * que funciona; por eso abajo hay una prueba de vida. */
function jergaEn(etiqueta: string): string[] {
  const plano = sinAcentos(etiqueta).toLowerCase();
  return JERGA.filter(({ termino, prefijo }) =>
    new RegExp(prefijo ? `\\b${termino}` : `\\b${termino}\\b`).test(plano)
  ).map((j) => j.termino);
}

describe("etiquetas de cara: la lista curada está aplicada", () => {
  it("las 68 etiquetas de la lista D del auditor están en el grafo", () => {
    const lista = leerJson("dataset/metadata/etiquetas_de_cara_v1.json") as Record<string, string>;
    expect(Object.keys(lista)).toHaveLength(68);
    const sinAplicar = Object.entries(lista).filter(([id, etq]) => graph[id]?.etiqueta_arbol !== etq);
    expect(sinAplicar, `sin aplicar: ${JSON.stringify(sinAplicar)}`).toEqual([]);
  });

  it("las derivadas del diccionario de la casa también", () => {
    const casa = leerJson("dataset/metadata/etiquetas_de_cara_v1_casa.json") as Record<string, string>;
    for (const [id, etq] of Object.entries(casa)) {
      if (id.startsWith("_")) continue;
      expect(graph[id]?.etiqueta_arbol, id).toBe(etq);
    }
  });

  it("los títulos técnicos quedaron INTACTOS (ahí viven la PI y las fuentes)", () => {
    // Un parche de cara que tocara titulo_concepto rompería la paridad con
    // los libros: se comprueba con un nodo de cada lista.
    expect(graph.six_sigma_dmaic.titulo_concepto).toMatch(/DMAIC/i);
    expect(graph.disenar_prompts_efectivos_para_ia.titulo_concepto).toMatch(/Prompts/i);
  });
});

describe("detector permanente de jerga (§C) sobre las 3.742 etiquetas", () => {
  // El guardián se demuestra a sí mismo ANTES de aplaudir el corpus: un
  // detector que no muerde deja pasar todo y se ve idéntico a uno que
  // funciona. Estos dos casos son su prueba de vida.
  it("MUERDE las etiquetas jergosas conocidas", () => {
    const casos: Array<[string, string]> = [
      ["Usa tu Business Model Canvas", "canvas"],
      ["Decide Pivotar o Perseverar", "pivot"],
      ["Reparte el Equity", "equity"],
      ["Construye tu MVP", "mvp"],
      ["Escucha la VoC de tus Clientes", "voc"],
      ["Prepara tu Pitch", "pitch"],
      ["Diseña Prompts que Funcionen", "prompt"],
      ["Define tu Startup", "startup"],
      ["Pide Feedback", "feedback"],
    ];
    for (const [etiqueta, termino] of casos) {
      expect(jergaEn(etiqueta), etiqueta).toContain(termino);
    }
  });

  it("no muerde español legítimo que solo se le parece", () => {
    // "Voces" empieza por "voc" y "lean" es también "ellos leen": si el
    // detector los marcara, la curaduría acabaría rompiendo etiquetas buenas.
    for (const etiqueta of [
      "Suma Voces Externas Confiables",
      "Mejora en Cinco Pasos",
      "Domina tus Instrucciones a la IA",
      "Cambiar de Rumbo o Avanzar",
    ]) {
      expect(jergaEn(etiqueta), etiqueta).toEqual([]);
    }
  });

  it("ninguna etiqueta usa el vocabulario prohibido", () => {
    const faltas = ETIQUETAS.filter(([id]) => !(id in ETIQUETAS_PENDIENTES)).flatMap(([id, etq]) =>
      jergaEn(etq).map((t) => `${id}: "${etq}" contiene "${t}"`)
    );
    expect(faltas, faltas.join("\n")).toEqual([]);
  });

  it("ninguna etiqueta usa siglas fuera de las exentas (§B)", () => {
    const faltas: string[] = [];
    for (const [id, etq] of ETIQUETAS) {
      if (id in ETIQUETAS_PENDIENTES) continue;
      for (const palabra of etq.match(/[\p{Lu}\p{N}]{2,}/gu) ?? []) {
        // Los alfanuméricos con cifra (3D, 5S, 6S) son medidas, no siglas
        // inglesas: se leen igual en español y no son jerga.
        if (/\d/.test(palabra)) continue;
        if (!SIGLAS_EXENTAS.has(palabra)) faltas.push(`${id}: "${etq}" usa la sigla "${palabra}"`);
      }
    }
    expect(faltas, faltas.join("\n")).toEqual([]);
  });

  it("ninguna etiqueta pasa de 6 palabras (la norma real del corpus)", () => {
    const largas = ETIQUETAS.filter(([, etq]) => palabras(etq).length > 6).map(
      ([id, etq]) => `${id}: "${etq}" (${palabras(etq).length})`
    );
    expect(largas, largas.join("\n")).toEqual([]);
  });

  it("ninguna etiqueta pierde una tilde", () => {
    const faltas = ETIQUETAS.flatMap(([id, etq]) =>
      detectarFaltaDeAcentos(etq).map((p) => `${id}: "${etq}" -> ${p}`)
    );
    expect(faltas, faltas.join("\n")).toEqual([]);
  });

  it("ninguna etiqueta está vacía ni cae al id como último recurso", () => {
    const vacias = ETIQUETAS.filter(([id, etq]) => !etq.trim() || etq === id).map(([id]) => id);
    expect(vacias).toEqual([]);
  });

  it("lo pendiente de curaduría sigue siendo exactamente lo declarado", () => {
    // Si el fundador cura estos dos, este test avisa para vaciar la lista: una
    // excepción que sobrevive a su motivo se convierte en un permiso silencioso.
    for (const [id, etq] of Object.entries(ETIQUETAS_PENDIENTES)) {
      expect(graph[id]?.etiqueta_arbol, `${id} ya cambió: bórralo de ETIQUETAS_PENDIENTES`).toBe(etq);
    }
  });
});

describe("unicidad de etiquetas (§E.4: reportar, no inventar arreglos)", () => {
  it("no aparece ninguna colisión NUEVA", () => {
    const porEtiqueta = new Map<string, string[]>();
    for (const [id, etq] of ETIQUETAS) {
      porEtiqueta.set(etq, [...(porEtiqueta.get(etq) ?? []), id]);
    }
    const colisiones = [...porEtiqueta.entries()].filter(([, ids]) => ids.length > 1);
    const nuevas = colisiones
      .filter(([etq]) => !COLISIONES_CONOCIDAS.includes(etq))
      .map(([etq, ids]) => `"${etq}" -> ${ids.join(", ")}`);
    expect(nuevas, nuevas.join("\n")).toEqual([]);
    // Y las conocidas siguen siendo las mismas: si el fundador resuelve una,
    // el test lo dice para sacarla de la lista.
    expect(colisiones.map(([etq]) => etq).sort()).toEqual(COLISIONES_CONOCIDAS);
  });
});

describe("fix de raíz: el nombre técnico no sale de casa", () => {
  it("etiquetaArbol devuelve la etiqueta de cara, nunca el título del libro", () => {
    // Los cuatro que el auditor nombró como la prueba del rescate.
    for (const id of ["definicion_startup", "six_sigma_dmaic", "medicion_kpi", "crear_pitch"]) {
      const cara = etiquetaArbol(id, graph);
      expect(cara).not.toBe(graph[id].titulo_concepto);
      expect(sinAcentos(cara).toLowerCase()).not.toMatch(/startup|dmaic|kpi|pitch/);
    }
  });

  it("ninguna superficie de cliente lee titulo_concepto", () => {
    // El hallazgo del rescate fue de CABLEADO, no de contenido: una pantalla
    // leía el título técnico. Esto impide que vuelva a pasar por descuido.
    const superficies = [
      "web/app/ui/ArbolPensante.tsx",
      "web/app/ui/PlanDocumento.tsx",
      "web/app/ui/DocumentoPapel.tsx",
      "web/app/ui/ManosALaObra.tsx",
      "web/app/ui/Descargas.tsx",
      "web/app/idea/[id]/IdeaView.tsx",
      "web/app/api/idea/[id]/route.ts",
      "web/app/api/session/start/route.ts",
      "web/app/api/project/[id]/follow/route.ts",
      "web/app/api/project/[id]/world/[pack]/start/route.ts",
      "web/app/api/project/[id]/documentos/route.ts",
    ];
    const culpables = superficies.filter((rel) => readFileSync(path.join(RAIZ, rel), "utf8").includes("titulo_concepto"));
    expect(culpables, `estas superficies de usuario leen titulo_concepto: ${culpables.join(", ")}`).toEqual([]);
  });

  it("el nodo que viaja al cliente no tiene dónde meter el título técnico", () => {
    // NodoTranscrito perdió el campo `titulo` a propósito: si alguien lo
    // devuelve, tsc falla y este test documenta por qué.
    const recorrido = readFileSync(path.join(RAIZ, "web/lib/engine/recorrido.ts"), "utf8");
    const bloque = recorrido.slice(recorrido.indexOf("export interface NodoTranscrito"));
    expect(bloque.slice(0, bloque.indexOf("}"))).not.toMatch(/^\s*titulo\s*:/m);
  });
});
