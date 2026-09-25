// Fase 3.0: pruebas de avanzarTurno(), la version resumible de
// ejecutar_recorrido. La fase normal (esperando_respuesta) mockea
// ./interprete por completo -- interpretarMultiSalto ya tiene su propia
// suite en interprete.test.ts, aqui solo importa la ORQUESTACION del
// bucle. La sub-fase de extension dirigida (Fase 2.8/2.9) mockea la
// brujula (../compass) y usa un cliente Anthropic falso para reproducir
// el guion exacto de engine/test_sigamos_salida.py: 'dame mi plan ya'
// corta la extension de inmediato, sin llegar a un 3er nodo.
import { beforeEach, describe, expect, it, vi } from "vitest";

const interpretarMultiSaltoFalso = vi.fn();
vi.mock("./interprete", () => ({
  interpretarMultiSalto: (...args: unknown[]) => interpretarMultiSaltoFalso(...args),
}));

const buscarAfinesFalso = vi.fn<(...args: unknown[]) => Promise<{ id: string; score: number }[]>>(
  async () => []
);
vi.mock("../compass", () => ({
  buscarAfines: (...args: unknown[]) => buscarAfinesFalso(...args),
}));

import { usoVacio } from "../costmeter";
import { cargarFamilies } from "../readiness";
import { cargarGrafo, cargarPreguntasCache } from "./graph";
import { avanzarTurno, estadoInicial } from "./recorrido";

const graph = cargarGrafo();
const families = cargarFamilies();
const preguntasCache = cargarPreguntasCache();

function respuestaClaudeJson(obj: unknown) {
  return {
    content: [{ type: "text", text: JSON.stringify(obj) }],
    usage: { input_tokens: 100, output_tokens: 20, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
  };
}

function respuestaClaudeTexto(texto: string) {
  return {
    content: [{ type: "text", text: texto }],
    usage: { input_tokens: 50, output_tokens: 10, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
  };
}

describe("avanzarTurno: fase esperando_respuesta (orquestacion, interpretarMultiSalto mockeado)", () => {
  beforeEach(() => {
    interpretarMultiSaltoFalso.mockReset();
  });

  it("avanzar con pregunta_necesaria=true agrega el nodo a la ruta y devuelve tipo=pregunta", async () => {
    const nid = "mapeo_capas_diseno";
    interpretarMultiSaltoFalso.mockResolvedValueOnce({
      resultado: {
        accion: "avanzar",
        camino: [nid],
        esSalto: false,
        preguntaNecesaria: true,
        preguntaAdaptada: "¿que capas has mapeado?",
        repregunta: null,
        perfilUpdate: null,
        prioridadDeclarada: null,
        numerosDetectados: null,
        tipoOfertaDetectado: null,
        unidadVentaDetectada: null,
      },
      acumulado: usoVacio(),
      historialMensajes: [],
    });

    const estado = estadoInicial({
      actualId: "design_thinking_fundamentos",
      perfilSesion: "perfil inicial",
      textoOriginal: "mi idea",
    });
    const r = await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: null,
      acumulado: usoVacio(),
      dbSessionId: "sess-1",
    });

    expect(r.tipo).toBe("pregunta");
    if (r.tipo !== "pregunta") throw new Error("esperaba tipo=pregunta");
    expect(r.estado.ruta).toEqual(["design_thinking_fundamentos", nid]);
    expect(r.estado.modos).toEqual(["conversado", "conversado"]);
    expect(r.pregunta).toBe("¿que capas has mapeado?");
    // El nodo que viaja al cliente lleva SOLO su etiqueta de cara: el
    // titulo_concepto se queda adentro (decision del fundador, jul 2026).
    expect(r.nodosNuevos).toEqual([
      {
        id: nid,
        etiqueta: graph[nid].etiqueta_arbol ?? graph[nid].titulo_concepto,
        modo: "conversado",
      },
    ]);
  });

  it("accion=salir cierra la fase sin pedir mas nada", async () => {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({
      resultado: {
        accion: "salir",
        camino: [],
        esSalto: false,
        preguntaNecesaria: false,
        preguntaAdaptada: null,
        repregunta: null,
        perfilUpdate: null,
        prioridadDeclarada: null,
        numerosDetectados: null,
        tipoOfertaDetectado: null,
        unidadVentaDetectada: null,
        razonamiento: "por aqui no hay senal de demanda real que sostenga las etapas",
      },
      acumulado: usoVacio(),
      historialMensajes: [],
    });

    const estado = estadoInicial({
      actualId: "design_thinking_fundamentos",
      perfilSesion: "perfil",
      textoOriginal: "mi idea",
    });
    const r = await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: "me quiero ir",
      acumulado: usoVacio(),
      dbSessionId: "sess-1",
    });

    expect(r.tipo).toBe("salio");
    if (r.tipo !== "salio") throw new Error("esperaba tipo=salio");
    expect(r.estado.fase).toBe("cerrada");
    // Canon 12: el cierre del camino core carga el motivo REAL del interprete
    // (la caja de vidrio "Lo que vi"), no una explicacion generica.
    expect(r.cierreCamino?.motivo).toBe("por aqui no hay senal de demanda real que sostenga las etapas");
  });

  it("resultado=null (fallo de red/presupuesto) se propaga como error_temporal sin mutar la ruta", async () => {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({ resultado: null, acumulado: usoVacio(), historialMensajes: [] });

    const estado = estadoInicial({
      actualId: "design_thinking_fundamentos",
      perfilSesion: "perfil",
      textoOriginal: "mi idea",
    });
    const r = await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: "algo",
      acumulado: usoVacio(),
      dbSessionId: "sess-1",
    });

    expect(r.tipo).toBe("error_temporal");
    if (r.tipo !== "error_temporal") throw new Error("esperaba tipo=error_temporal");
    expect(r.estado.ruta).toEqual(["design_thinking_fundamentos"]);
    expect(r.opciones.length).toBeGreaterThan(0);
  });

  it("ruta.length >= MAX_DEPTH corta el bucle y pasa a listo_para_plan sin llamar al interprete", async () => {
    const rutaLarga = new Array(15).fill("design_thinking_fundamentos");
    const modosLarga = new Array(15).fill("conversado");
    const estado = {
      ...estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t" }),
      ruta: rutaLarga,
      modos: modosLarga as ("conversado" | "silencioso" | "salto")[],
    };
    const r = await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: "algo",
      acumulado: usoVacio(),
      dbSessionId: "sess-1",
    });

    expect(r.tipo).toBe("listo_para_plan");
    expect(interpretarMultiSaltoFalso).not.toHaveBeenCalled();
  });
});

describe("avanzarTurno: extension dirigida (sigamos) respeta 'dame mi plan ya' de inmediato", () => {
  const candidato1 = "accruals_y_activos_prepagados";
  const candidato2 = "amortizacion_y_periodo_de_gracia";

  beforeEach(() => {
    buscarAfinesFalso.mockReset();
    buscarAfinesFalso.mockResolvedValue([
      { id: candidato1, score: 0.5 },
      { id: candidato2, score: 0.4 },
    ]);
    expect(families[candidato1]).toBe("viabilidad_economica");
    expect(families[candidato2]).toBe("viabilidad_economica");
  });

  it("pregunta 2 nodos reales y corta al tercero en cuanto el usuario pide el plan", async () => {
    const estadoBase = {
      ...estadoInicial({ actualId: "leap_of_faith_assumptions", perfilSesion: "Hace macetas, trabaja solo.", textoOriginal: "quiero saber si mi idea tiene futuro" }),
      profundizarOfrecido: true,
      fase: "esperando_profundizar" as const,
      preguntaPendiente: "¿seguimos un poco o lo quieres ya?",
    };

    const { cliente: cliente1, llamadas: llamadas1 } = clienteConLlamadas([
      respuestaClaudeJson({ decision: "continuar" }),
      respuestaClaudeTexto("¿ya sacaste la cuenta de cuanto te cuesta cada pieza?"),
    ]);
    const turno1 = await avanzarTurno({
      client: cliente1 as never,
      graph,
      families,
      preguntasCache,
      estado: estadoBase,
      respuestaUsuario: "cobro por pieza pero no se cuanto me cuesta en materiales o tiempo",
      acumulado: usoVacio(),
      dbSessionId: "sess-2",
    });
    expect(llamadas1.length).toBe(2);
    expect(turno1.tipo).toBe("pregunta");
    if (turno1.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(turno1.estado.ruta).toEqual(["leap_of_faith_assumptions", candidato1]);
    expect(turno1.estado.fase).toBe("extendiendo_dirigido");

    const { cliente: cliente2, llamadas: llamadas2 } = clienteConLlamadas([
      respuestaClaudeJson({ decision: "continuar" }),
      respuestaClaudeTexto("segunda pregunta dirigida"),
    ]);
    const turno2 = await avanzarTurno({
      client: cliente2 as never,
      graph,
      families,
      preguntasCache,
      estado: turno1.estado,
      respuestaUsuario: "una respuesta real cualquiera",
      acumulado: turno1.acumulado,
      dbSessionId: "sess-2",
    });
    expect(llamadas2.length).toBe(2);
    expect(turno2.tipo).toBe("pregunta");
    if (turno2.tipo !== "pregunta") throw new Error("esperaba pregunta");
    expect(turno2.estado.ruta).toEqual(["leap_of_faith_assumptions", candidato1, candidato2]);

    const { cliente: cliente3, llamadas: llamadas3 } = clienteConLlamadas([
      respuestaClaudeJson({ decision: "generar_ya" }),
    ]);
    const turno3 = await avanzarTurno({
      client: cliente3 as never,
      graph,
      families,
      preguntasCache,
      estado: turno2.estado,
      respuestaUsuario: "dame mi plan ya, con esto alcanza",
      acumulado: turno2.acumulado,
      dbSessionId: "sess-2",
    });
    expect(llamadas3.length).toBe(1);
    expect(turno3.tipo).toBe("listo_para_plan");
    // Exactamente 2 nodos nuevos (no un 3ro): la prueba real de que corta a tiempo.
    expect(turno3.estado.ruta).toEqual(["leap_of_faith_assumptions", candidato1, candidato2]);
    expect(turno3.estado.sigamosDirigido).toBeNull();
  });
});

function clienteConLlamadas(respuestas: unknown[]) {
  const llamadas: unknown[] = [];
  let idx = 0;
  const create = vi.fn(async (kwargs: unknown) => {
    llamadas.push(kwargs);
    const item = respuestas[idx++];
    if (item instanceof Error) throw item;
    return item;
  });
  return { cliente: { messages: { create } }, llamadas };
}

// AUD-09 H13 (decisión del fundador, 25 sep 2026): que la entrevista de un
// mundo siempre tenga salida es deber del MOTOR, no del grafo. Un nodo sin
// sucesores puede ser un final legítimo del contenido; la entrevista no. Cuando
// llega a uno, el motor elige otra puerta del mismo mundo con la misma lógica
// que usa cuando el intérprete decide salir, sin repetir lo ya visitado.
import { esOfrecible, sucesoresNivel as sucesoresH13 } from "./graph";

function estadoEnMundo(nid: string, dominio: string) {
  return {
    ...estadoInicial({
      actualId: nid,
      perfilSesion: "vende por internet y quiere ordenar su operación",
      textoOriginal: "mi idea",
      dominioSesion: dominio,
      dominiosDesbloqueados: ["core", dominio],
    }),
    preguntaPendiente: "¿Cómo va eso hoy?",
  };
}

describe("avanzarTurno: un callejón de un mundo no termina la entrevista (AUD-09 H13)", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());

  it("la puerta del checklist de cláusulas ya no muere tras una pregunta", async () => {
    const nid = "ten_un_checklist_de_clausulas_de_contrato";
    const r = await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado: estadoEnMundo(nid, "compras"),
      respuestaUsuario: "firmo sin revisar mucho",
      acumulado: usoVacio(),
      dbSessionId: "sess-h13",
    });
    expect(r.tipo).toBe("pregunta");
    const nueva = r.estado.ruta[r.estado.ruta.length - 1];
    expect(nueva).not.toBe(nid);
    expect(graph[nueva].dominio).toBe("compras");
    expect(r.estado.fallbackEvents.some((e) => e.tipo === "puerta_reelegida")).toBe(true);
  });

  it("NINGÚN nodo sin sucesor de los mundos deja la entrevista sin salida", async () => {
    const callejones = Object.entries(graph)
      .filter(([nid, n]) => n.dominio && n.dominio !== "core" && esOfrecible(nid, graph, [n.dominio]))
      .filter(([nid, n]) => sucesoresH13(nid, graph, new Set([nid]), undefined, ["core", n.dominio as string]).length === 0)
      .map(([nid, n]) => ({ nid, dominio: n.dominio as string }));
    expect(callejones.length).toBeGreaterThan(50);
    const sinSalida: string[] = [];
    for (const c of callejones) {
      const r = await avanzarTurno({
        client: {} as never,
        graph,
        families,
        preguntasCache,
        estado: estadoEnMundo(c.nid, c.dominio),
        respuestaUsuario: "sigo",
        acumulado: usoVacio(),
        dbSessionId: "sess-h13",
      });
      const nueva = r.estado.ruta[r.estado.ruta.length - 1];
      if (r.tipo !== "pregunta" || nueva === c.nid || graph[nueva]?.dominio !== c.dominio) sinSalida.push(`${c.dominio}:${c.nid}`);
    }
    expect(sinSalida).toEqual([]);
  }, 60_000);
});

// AUD-09 M16 (tanda 5, mezcla núcleo y mundos): la entrevista de un mundo
// filtraba sus sucesores con TODOS los dominios desbloqueados (núcleo + cada
// mundo previsualizado): la de Calidad podía derivar hacia Riesgos por una arista
// vieja de mundo a mundo. Una sesión de mundo camina su mundo (y el núcleo).
describe("avanzarTurno: la entrevista de un mundo no cruza a otro mundo (AUD-09 M16)", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());

  it("al intérprete le llegan solo el núcleo y el mundo de la sesión", async () => {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({ resultado: null, acumulado: usoVacio(), eventos: [] });
    const estado = {
      ...estadoInicial({
        actualId: "identificacion_de_riesgos",
        perfilSesion: "p",
        textoOriginal: "t",
        dominioSesion: "quality",
        dominiosDesbloqueados: ["core", "quality", "risk_management"],
      }),
      preguntaPendiente: "¿Cómo identificas tus riesgos?",
    };
    await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: "los anoto",
      acumulado: usoVacio(),
      dbSessionId: "sess-m16",
    });
    const args = interpretarMultiSaltoFalso.mock.calls[0]?.[0] as { dominiosDesbloqueados?: string[] } | undefined;
    expect(args?.dominiosDesbloqueados).toEqual(["core", "quality"]);
  });
});

// i18n F5: la entrevista de una idea en coreano la escribe la IA en coreano
// (el idioma de la IDEA viaja en el estado), y la de una sesión de antes de F5
// (sin idioma en el estado) sigue en español.
describe("avanzarTurno: el idioma de la idea llega al intérprete (i18n F5)", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());

  async function turnoCon(idioma: string | undefined) {
    interpretarMultiSaltoFalso.mockResolvedValueOnce({ resultado: null, acumulado: usoVacio(), eventos: [] });
    const base = estadoInicial({ actualId: "leap_of_faith_assumptions", perfilSesion: "p", textoOriginal: "t", idioma });
    const estado = { ...base, preguntaPendiente: "¿?" };
    if (idioma === undefined) delete (estado as { idioma?: string }).idioma;
    await avanzarTurno({
      client: {} as never,
      graph,
      families,
      preguntasCache,
      estado,
      respuestaUsuario: "r",
      acumulado: usoVacio(),
      dbSessionId: "sess-i18n",
      idioma: "en",
    });
    return interpretarMultiSaltoFalso.mock.calls[0]?.[0] as { idiomaSalida?: string | null; idioma?: string };
  }

  it("idea en coreano con la interfaz en inglés: la IA en coreano, las plantillas en coreano", async () => {
    const args = await turnoCon("ko");
    expect(args.idiomaSalida).toBe("ko");
    expect(args.idioma).toBe("ko");
  });

  it("idea en ruso (fuera de los once): la IA en ruso, las plantillas en la interfaz", async () => {
    const args = await turnoCon("ru");
    expect(args.idiomaSalida).toBe("ru");
    expect(args.idioma).toBe("en");
  });

  it("sesión de antes de F5 (sin idioma): español en todo", async () => {
    const args = await turnoCon(undefined);
    expect(args.idiomaSalida).toBeNull();
    expect(args.idioma).toBe("es");
  });

  it("estadoInicial sin idioma lo fija en español", () => {
    expect(estadoInicial({ actualId: "x", perfilSesion: "p", textoOriginal: "t" }).idioma).toBe("es");
  });
});

// D3 (i18n F5): el riel es navegación, así que sus etiquetas van en el idioma
// de la INTERFAZ (la etiqueta derivada), aunque la idea esté en otro idioma.
import { ETIQUETAS_RIEL } from "../i18n/etiquetasRiel";

describe("avanzarTurno: el riel en el idioma de la interfaz (D3)", () => {
  beforeEach(() => interpretarMultiSaltoFalso.mockReset());

  it("nodosNuevos llevan la etiqueta derivada del idioma de la interfaz", async () => {
    const nid = "mapeo_capas_diseno";
    const antes = ETIQUETAS_RIEL.en[nid];
    ETIQUETAS_RIEL.en[nid] = "Map Your Design Layers";
    try {
      interpretarMultiSaltoFalso.mockResolvedValueOnce({
        resultado: {
          accion: "avanzar", camino: [nid], esSalto: false, preguntaNecesaria: true, preguntaAdaptada: "디자인?",
          repregunta: null, perfilUpdate: null, prioridadDeclarada: null, numerosDetectados: null,
          tipoOfertaDetectado: null, unidadVentaDetectada: null,
        },
        acumulado: usoVacio(),
        historialMensajes: [],
      });
      const estado = estadoInicial({ actualId: "design_thinking_fundamentos", perfilSesion: "p", textoOriginal: "t", idioma: "ko" });
      const r = await avanzarTurno({
        client: {} as never, graph, families, preguntasCache, estado,
        respuestaUsuario: null, acumulado: usoVacio(), dbSessionId: "sess-d3", idioma: "en",
      });
      if (r.tipo !== "pregunta") throw new Error("esperaba tipo=pregunta");
      expect(r.nodosNuevos[0].etiqueta).toBe("Map Your Design Layers");
    } finally {
      if (antes === undefined) delete ETIQUETAS_RIEL.en[nid];
      else ETIQUETAS_RIEL.en[nid] = antes;
    }
  });
});
