/**
 * NINGUNA REFERENCIA DE ORIGEN LLEGA A LA IA (regla del fundador, 1 oct 2026; docs/REGLAS_DE_LA_CASA.md).
 *
 * No basta con la orden REGLA_SIN_FUENTES: la referencia no debe llegarle nunca a la IA. Toda llamada lee el texto de
 * los nodos del grafo de la web (cargarGrafo) y de las preguntas en cache, y esa vista la escribe un solo filtro,
 * scripts/origen_ia.py, al sincronizar. Esta guarda comprueba:
 *   1. el grafo y la cache enteros, que es lo unico que las llamadas pueden leer;
 *   2. los mensajes REALES que recibe la IA (cliente falso que los captura) en la clasificacion de la entrada, el
 *      interprete de la entrevista, la puerta del seguimiento y el material del plan, para una muestra de nodos de
 *      todos los espacios y para todos los nodos vivos que llevan un autor en el titulo del concepto;
 *   3. que ninguno lleve un campo interno.
 * Los identificadores de nodo (snake_case) se miden aparte: el contrato de salida de la IA los necesita.
 */
import { describe, expect, it, vi } from "vitest";
import type Anthropic from "@anthropic-ai/sdk";

vi.mock("./compass", () => ({
  MAX_SALTOS_POSIBLES_OFRECIDOS: 8,
  MIN_SCORE_SALTO: 0.3,
  buscarAfines: async () => [],
}));

import { usoVacio } from "./costmeter";
import { clasificarEntrada } from "./engine/clasificar";
import { cargarGrafo, cargarPreguntasCache } from "./engine/graph";
import { interpretarMultiSalto } from "./engine/interprete";
import { aMaterial } from "./engine/planRedactor";
import { seleccionarPuertaAvanzada } from "./engine/puertaAvanzada";
import { cargarFamilies } from "./readiness";
import { autoresCanonicos, autoresEn, titulosCanonicos, titulosEn } from "./testFixtures/fuentesCanonicas";

const graph = cargarGrafo();
const cache = cargarPreguntasCache();
const families = cargarFamilies();
const TITULOS = titulosCanonicos();
const AUTORES = autoresCanonicos();
const CAMPOS_TEXTO = ["titulo_concepto", "etiqueta_arbol", "resumen_teorico", "pasos_accionables", "entregable_esperado", "condiciones_activacion"] as const;
const INTERNOS = /"(fuente|fuentes_internas|correcciones|merged_originals|notas_extraccion|cita|libro|fichero|lineas)"\s*:/;

/** Lo que la IA lee como texto: sin los identificadores de nodo (snake_case), que se miden aparte. */
function sinIds(s: string): string {
  return s.replace(/[a-z0-9]+(?:_[a-z0-9]+)+/g, " ");
}

function origenEn(s: string): string[] {
  const t = sinIds(s);
  return [...titulosEn(t, TITULOS), ...autoresEn(t, AUTORES)];
}

const vivos = Object.entries(graph).filter(([, n]) => !(n as { deprecado?: boolean }).deprecado);
const CON_AUTOR_EN_TITULO = [
  "benchmarking_7_pasos_juran", "consejo_de_calidad", "aim_of_leadership", "cuatro_etapas_del_pensamiento_creativo",
  "ciclo_pdca_pdsa", "modelo_lubin_esty_4_etapas", "los_14_puntos_deming", "trilogia_de_juran", "accion_correctiva_sistematica",
];
const MUESTRA = [
  ...new Set([
    ...[...new Set(vivos.map(([, n]) => n.dominio))].flatMap((d) => vivos.filter(([, n]) => n.dominio === d).slice(0, 3).map(([id]) => id)),
    ...CON_AUTOR_EN_TITULO,
  ]),
];

function clienteQueCaptura(respuesta: Record<string, unknown>) {
  const pedidos: unknown[] = [];
  const cliente = {
    messages: {
      create: vi.fn(async (req: unknown) => {
        pedidos.push(req);
        return {
          content: [{ type: "text", text: JSON.stringify(respuesta) }],
          usage: { input_tokens: 100, output_tokens: 10 },
          stop_reason: "end_turn",
        };
      }),
    },
  } as unknown as Anthropic;
  return { cliente, pedidos };
}

describe("ninguna referencia de origen llega a la IA", () => {
  it("la muestra cubre todos los espacios y los nodos con autor en el titulo", () => {
    const dominios = new Set(MUESTRA.map((id) => graph[id].dominio));
    expect(dominios.size).toBeGreaterThanOrEqual(11);
    for (const id of CON_AUTOR_EN_TITULO) expect(graph[id], id).toBeTruthy();
  });

  it("el grafo de la web no lleva ningun titulo ni autor canonico en ningun texto de nodo", () => {
    const restos: string[] = [];
    for (const [id, n] of Object.entries(graph)) {
      for (const c of CAMPOS_TEXTO) {
        const v = (n as unknown as Record<string, unknown>)[c];
        for (const s of Array.isArray(v) ? v : [v]) {
          if (typeof s === "string" && origenEn(s).length) restos.push(`${id}.${c}: ${origenEn(s).join(", ")}`);
        }
      }
    }
    expect(restos).toEqual([]);
  });

  it("las preguntas en cache tampoco", () => {
    const restos = Object.entries(cache).filter(([, v]) => origenEn(JSON.stringify(v)).length).map(([k]) => k);
    expect(restos).toEqual([]);
  });

  it("los mensajes reales de la clasificacion de la entrada", async () => {
    const { cliente, pedidos } = clienteQueCaptura({ puerta: MUESTRA[0], razon: "x" });
    await clasificarEntrada(cliente, "quiero mejorar la calidad de mi taller", MUESTRA, graph, usoVacio());
    expect(pedidos.length).toBeGreaterThan(0);
    const s = JSON.stringify(pedidos);
    expect(s).not.toMatch(INTERNOS);
    expect(origenEn(s)).toEqual([]);
  });

  it("los mensajes reales del interprete, con cada nodo de la muestra como nodo actual", async () => {
    const hallados: string[] = [];
    for (const actualId of MUESTRA) {
      const { cliente, pedidos } = clienteQueCaptura({ accion: "avanzar", camino: [], pregunta_necesaria: true });
      await interpretarMultiSalto({
        client: cliente,
        actualId,
        graph,
        visitados: new Set([actualId]),
        perfilSesion: "Tengo un taller y quiero mejorar.",
        textoOriginal: "quiero mejorar la calidad de mi taller",
        preguntaHecha: "¿Qué te preocupa más?",
        respuestaUsuario: "que los clientes vuelvan",
        repreguntasDisponibles: 1,
        preguntasCache: cache,
        historialMensajes: [],
        acumulado: usoVacio(),
      } as never).catch(() => null);
      expect(pedidos.length, actualId).toBeGreaterThan(0);
      const s = JSON.stringify(pedidos);
      expect(s, actualId).not.toMatch(INTERNOS);
      for (const x of origenEn(s)) hallados.push(`${actualId}: ${x}`);
    }
    expect(hallados).toEqual([]);
  });

  it("los mensajes reales de la puerta del seguimiento, en cada fase", async () => {
    const hallados: string[] = [];
    const todos = [...new Set(vivos.map(([, n]) => n.dominio).filter((d): d is string => !!d))];
    for (const fase of ["ideacion", "validacion", "planificacion", "ejecucion"]) {
      const { cliente, pedidos } = clienteQueCaptura({ puerta: null });
      await seleccionarPuertaAvanzada(cliente, "contraté a dos personas", null, fase, families, graph, new Set(), [], usoVacio(), todos).catch(() => null);
      const s = JSON.stringify(pedidos);
      expect(s).not.toMatch(INTERNOS);
      for (const x of origenEn(s)) hallados.push(`${fase}: ${x}`);
    }
    expect(hallados).toEqual([]);
  });

  it("el material real del plan", () => {
    const s = JSON.stringify(MUESTRA.map((id) => aMaterial(id, graph, families)));
    expect(s).not.toMatch(INTERNOS);
    expect(origenEn(s)).toEqual([]);
  });

  it("la orden fija de toda llamada no nombra a ningun autor ni libro de la lista", async () => {
    const { REGLA_SIN_FUENTES } = await import("./reglaSinFuentes");
    expect(origenEn(REGLA_SIN_FUENTES)).toEqual([]);
  });

  it("detecta lo que debe detectar (casos negativos)", () => {
    expect(origenEn("Benchmarking de 7 Pasos (Juran)")).toEqual(["Juran"]);
    expect(origenEn("según Deming, mide el sistema")).toEqual(["Deming"]);
    expect(origenEn("la razón por la que compra ('reason to buy')")).toEqual([]);
    expect(origenEn("como hizo BMW con el MINI Cooper")).toEqual([]);
    expect(origenEn("el nodo benchmarking_7_pasos_juran")).toEqual([]);
  });
});

/**
 * Los identificadores de nodo viajan en el texto (clasificacion, interprete, puerta, replanteamiento y plan: el
 * modelo responde con ids). Hay ids vivos con un apellido de la lista. Esta lista es la PENDIENTE declarada ante el
 * fundador (acta, seccion 11): no puede crecer; si se renombran, se vacia.
 */
const IDS_CON_APELLIDO_PENDIENTES = [
  "accion_correctiva_crosby", "benchmarking_7_pasos_juran", "benchmarking_trilogia_juran", "crosby_creatividad_gerencial",
  "crosby_habilidad_transmision", "crosby_implementacion_gerencial", "crosby_liderazgo_abierto",
  "crosby_programa_14_pasos_introduccion", "juran_quality_by_design", "juran_rcca_metodo", "los_14_puntos_deming",
  "mejora_calidad_crosby", "modelo_lubin_esty_4_etapas", "modelo_transformacion_juran", "planificacion_calidad_crosby",
  "proceso_benchmarking_juran_7pasos", "quality_awareness_crosby", "reglas_deming_consultoria_calidad", "trilogia_de_juran",
  "trilogia_juran_qa_qc", "wallas_etapa_incubacion", "wallas_etapa_preparacion", "wallas_etapa_verificacion",
  "wallas_intimacion_fringe_consciousness", "wallas_pensamiento_regulado",
];

describe("identificadores de nodo con un apellido de la lista", () => {
  it("no aparece ninguno nuevo fuera de la pendiente declarada", () => {
    const apellidos = new Set(AUTORES.filter((a) => !/[\s.]/.test(a)).map((a) => a.toLowerCase()));
    const conApellido = vivos.map(([id]) => id).filter((id) => id.split("_").some((p) => apellidos.has(p))).sort();
    expect(conApellido).toEqual([...IDS_CON_APELLIDO_PENDIENTES].sort());
  });
});
