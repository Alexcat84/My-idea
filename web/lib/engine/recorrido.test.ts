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
